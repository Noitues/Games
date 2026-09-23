"""LLM backends.

``claude_cli``: each call is an isolated ``claude -p`` subprocess with a replaced system prompt, no
tools, no session persistence, no settings or MCP, and JSON-schema output. No two calls share a
context window; an agent's "memory" is whatever the orchestrator puts in its prompt.

``scripted``: deterministic heuristic bots (scripted.py). Zero tokens. Surveys are synthetic.

Every response is cached on disk under (run_id, call sequence number, prompt hash), so re-running
a crashed run replays the cached agent answers and resumes exactly where it stopped.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tempfile
import threading
import time
from pathlib import Path

MODELS = {
    "player": "claude-haiku-4-5-20251001",
    "gm": "claude-sonnet-5",
    "referee": "claude-sonnet-5",
    "interviewer": "claude-haiku-4-5-20251001",
    "analyst": "claude-sonnet-5",
    "judge": "claude-sonnet-5",
    "chargen": "claude-sonnet-5",
    "strong": "claude-opus-5-5",
}
# Thinking effort per role: nearly all completion tokens were hidden thinking in the first probe.
EFFORT = {"player": "low", "interviewer": "low", "gm": "low", "referee": "medium", "analyst": "medium",
          "judge": "medium", "chargen": "medium"}

# Hard dice-claim patterns: an agent stating dice faces or a roll result it was never given.
DICE_CLAIM = [
    re.compile(r"(?<![\w\-+])[+\-0]\s[+\-0]\s[+\-0]\s[+\-0](?![\w\-+])"),               # 4dF faces
    re.compile(r"\b(?:i|we|you|he|she|they)\s+roll(?:ed|s)?\s+(?:a|an)?\s*[+\-]?\d", re.I),
    re.compile(r"\brolled\s+(?:a|an)\s+[+\-]?\d", re.I),
    re.compile(r"\bdice\s+(?:show|came up|come up|land(?:ed)?)\b", re.I),
]


class BudgetExceeded(Exception):
    pass


class AgentFailure(Exception):
    pass


def dice_claims(obj) -> list[str]:
    hits = []

    def walk(x):
        if isinstance(x, str):
            for p in DICE_CLAIM:
                m = p.search(x)
                if m:
                    hits.append(x[max(0, m.start() - 40): m.end() + 40])
        elif isinstance(x, dict):
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(obj)
    return hits


class TokenMeter:
    def __init__(self, cap: int | None):
        self.cap = cap
        self.prompt = 0
        self.completion = 0
        self.cost_usd = 0.0
        self.calls = 0
        self.lock = threading.Lock()

    def add(self, p: int, c: int, cost: float) -> None:
        with self.lock:
            self.prompt += p
            self.completion += c
            self.cost_usd += cost
            self.calls += 1

    @property
    def total(self) -> int:
        return self.prompt + self.completion

    def check(self) -> None:
        if self.cap and self.total > self.cap:
            raise BudgetExceeded(f"token cap {self.cap} exceeded ({self.total})")

    def as_dict(self) -> dict:
        return {"prompt": self.prompt, "completion": self.completion, "cost_usd": round(self.cost_usd, 4),
                "calls": self.calls}


class LLMClient:
    def __init__(self, backend: str, *, cache_dir: Path | None, run_id: str,
                 run_meter: TokenMeter, batch_meter: TokenMeter | None = None,
                 models: dict | None = None, scripted=None, timeout: int = 300):
        self.backend = backend
        self.cache_dir = cache_dir
        self.run_id = run_id
        self.meter = run_meter
        self.batch_meter = batch_meter
        self.models = {**MODELS, **(models or {})}
        self.scripted = scripted
        self.timeout = timeout
        self.seq: dict[str, int] = {}
        self._seq_lock = threading.Lock()
        self.calls: list[dict] = []
        if cache_dir:
            cache_dir.mkdir(parents=True, exist_ok=True)

    def model_for(self, role: str) -> str:
        return self.models.get(role, self.models["player"])

    def call(self, *, role: str, agent: str, kind: str, system: str, prompt: str, schema: dict,
             ctx: dict | None = None) -> dict:
        with self._seq_lock:   # per-agent counters keep cache keys stable under parallel calls
            n = self.seq[agent] = self.seq.get(agent, 0) + 1
        model = self.model_for(role)
        key = hashlib.sha256(json.dumps([self.run_id, agent, n, model, system, prompt, schema],
                                        sort_keys=True).encode()).hexdigest()[:32]
        cpath = self.cache_dir / f"{key}.json" if self.cache_dir else None
        if cpath and cpath.exists():
            rec = json.loads(cpath.read_text())
            self.calls.append({"seq": n, "agent": agent, "kind": kind, "cached": True,
                               "prompt_tokens": 0, "completion_tokens": 0})
            return rec["output"]
        if self.backend == "scripted":
            out = self.scripted.respond(role=role, agent=agent, kind=kind, ctx=ctx or {}, n=n)
            usage = (0, 0, 0.0)
        else:
            self.meter.check()
            if self.batch_meter:
                self.batch_meter.check()
            out, usage = self._claude(model, system, prompt, schema, EFFORT.get(role, "low"))
        self.meter.add(*usage)
        if self.batch_meter:
            self.batch_meter.add(*usage)
        self.calls.append({"seq": n, "agent": agent, "kind": kind, "cached": False,
                           "prompt_tokens": usage[0], "completion_tokens": usage[1]})
        if cpath:
            cpath.write_text(json.dumps({"agent": agent, "kind": kind, "model": model,
                                         "output": out}, ensure_ascii=False))
        return out

    def _claude(self, model: str, system: str, prompt: str, schema: dict, effort: str) -> tuple[dict, tuple]:
        env = {k: v for k, v in os.environ.items()
               if k not in ("CLAUDE_CODE_SESSION_ID", "CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT")}
        last_err = ""
        for attempt in range(4):
            with tempfile.TemporaryDirectory(prefix="sde_agent_") as td:
                sp = Path(td) / "system.txt"
                sp.write_text(system)
                cmd = ["claude", "-p", "--model", model, "--effort", effort, "--output-format", "json",
                       "--system-prompt-file", str(sp), "--tools", "", "--no-session-persistence",
                       "--setting-sources", "", "--strict-mcp-config",
                       "--json-schema", json.dumps(schema)]
                try:
                    proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                                          cwd=td, env=env, timeout=self.timeout)
                except subprocess.TimeoutExpired:
                    last_err = "timeout"
                    time.sleep(2 ** attempt)
                    continue
            try:
                d = json.loads(proc.stdout)
            except json.JSONDecodeError:
                last_err = (proc.stdout[-300:] + proc.stderr[-300:])
                time.sleep(2 ** attempt)
                continue
            u = d.get("usage", {})
            usage = (u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0)
                     + u.get("cache_creation_input_tokens", 0), u.get("output_tokens", 0),
                     float(d.get("total_cost_usd", 0.0)))
            if d.get("is_error"):
                last_err = str(d.get("result"))[:300]
                self.meter.add(*usage)
                time.sleep(2 ** attempt)
                continue
            out = d.get("structured_output")
            if out is None:
                try:
                    out = json.loads(d.get("result", ""))
                except (json.JSONDecodeError, TypeError):
                    m = re.search(r"\{.*\}", d.get("result", "") or "", re.S)
                    out = json.loads(m.group(0)) if m else None
            if isinstance(out, dict):
                return out, usage
            last_err = f"no structured output: {str(d.get('result'))[:200]}"
            self.meter.add(*usage)
        raise AgentFailure(f"claude -p failed after retries: {last_err}")
