"""Run N seeds × arms in parallel, resumably, then (optionally) the paired-preference phase.

    python batch.py pilot-01 --seeds 3 --arms A,B,C --backend claude_cli --parallel 3 --prefs

- Runs with the same seed index share run_index, so every arm of a seed gets the same cohort,
  personality assignment, prep packet and dice stream.
- Resume: a run whose JSON already has a final status is skipped. Partial or crashed runs are re-run,
  and the per-run response cache replays every agent call already made, so they continue where
  they stopped.
- Token caps: --token-cap-run stops a single run (status "truncated"); --token-cap-batch stops
  launching new LLM calls anywhere in the batch.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from agents import PERSONALITIES, Agent, render_transcript
from chargen import cohort_index_for_run, generate_cohort
from engine import derive_seed
from llm import MODELS, AgentFailure, BudgetExceeded, LLMClient, TokenMeter
from run import ROOT, WORLD, Session

FINAL = {"complete", "invalid", "truncated"}


def seeds_for(batch_id: str, n: int, base: int | None) -> list[int]:
    b = base if base is not None else derive_seed(0, f"batch:{batch_id}") % 100000
    return [b + i for i in range(n)]


def run_job(job: dict, cfg: dict, batch_meter: TokenMeter) -> dict:
    s = Session(arm_key=job["arm"], seed=job["seed"], run_index=job["run_index"], batch_id=cfg["batch_id"],
                backend=cfg["backend"], out_dir=cfg["out_dir"], cache_dir=cfg["cache_dir"],
                token_cap=cfg["token_cap_run"], batch_meter=batch_meter, models=cfg["models"],
                max_scenes=cfg["max_scenes"], cohort_id=job["cohort_id"])
    rec = s.run()
    return {"run_id": rec["run_id"], "status": rec["status"], "tokens": rec["tokens"],
            "error": (rec.get("error") or "")[-300:], "elapsed_s": rec["elapsed_s"]}


# ====================================================================== paired preference
PREF_SYSTEM = ("You are a tabletop roleplaying game player. {style} You will read two anonymised session "
               "transcripts in which your character, {name}, took part, and say which session you would rather "
               "have played. Judge by your own taste as that player. Answer only with the JSON requested.")


def story_only(rec: dict) -> str:
    """Narration and player lines only: mechanical table lines differ by rule set and would unblind."""
    entries = [t for t in rec["transcript"] if t["kind"] != "mechanics"]
    return render_transcript(entries, None, 24000)


def run_preferences(cfg: dict, arms: list[str], seeds: list[int], batch_meter: TokenMeter) -> dict:
    out_dir = cfg["out_dir"]
    path = out_dir / "_preferences.json"
    prefs = json.loads(path.read_text()) if path.exists() else {"items": []}
    done = {(i["seed"], i["arm_x"], i["arm_y"], i["character_id"]) for i in prefs["items"]}
    recs = {}
    for p in out_dir.glob("*.json"):
        if p.name.startswith("_"):
            continue
        r = json.loads(p.read_text())
        if r["status"] == "complete":
            recs[(r["arm"], r["seed"])] = r
    client = LLMClient(cfg["backend"], cache_dir=cfg["cache_dir"] / "_prefs", run_id=f"{cfg['batch_id']}-prefs",
                       run_meter=TokenMeter(None), batch_meter=batch_meter, models=cfg["models"],
                       scripted=__import__("scripted").Scripted(seed=0, run_id="prefs"))
    jobs = []
    for seed in seeds:
        for ax, ay in itertools.combinations(arms, 2):
            if (ax, seed) not in recs or (ay, seed) not in recs:
                continue
            rx, ry = recs[(ax, seed)], recs[(ay, seed)]
            for a in rx["assignments"]:
                key = (seed, ax, ay, a["character_id"])
                if key not in done:
                    jobs.append((seed, ax, ay, a, rx, ry))

    def one(job):
        seed, ax, ay, a, rx, ry = job
        rng = random.Random(derive_seed(seed, f"pref:{ax}{ay}{a['character_id']}"))
        order = [(ax, rx), (ay, ry)]
        rng.shuffle(order)
        style = PERSONALITIES[a["personality_id"]][1]
        agent = Agent(client, "player", f"pref-{seed}-{ax}{ay}-{a['character_id']}",
                      PREF_SYSTEM.format(style=style, name=a["name"]))
        prompt = (f"== Session 1 ==\n{story_only(order[0][1])}\n\n== Session 2 ==\n{story_only(order[1][1])}\n\n"
                  f"Which session would you rather have played as {a['name']}? choice '1' or '2', and a one-sentence reason.")
        ans = agent.ask("preference", prompt, {"engine": None})
        pick = order[0][0] if ans.get("choice") == "1" else order[1][0]
        return {"seed": seed, "arm_x": ax, "arm_y": ay, "character_id": a["character_id"],
                "personality_id": a["personality_id"], "shown_first": order[0][0], "preferred_arm": pick,
                "reason": ans.get("reason", ""), "synthetic": cfg["backend"] == "scripted"}
    with ThreadPoolExecutor(max_workers=cfg["parallel"] * 2) as ex:
        for res in ex.map(one, jobs):
            prefs["items"].append(res)
            path.write_text(json.dumps(prefs, indent=1))
    return prefs


def main() -> None:
    ap = argparse.ArgumentParser(description="Run a batch of Scene-Deck sessions.")
    ap.add_argument("batch_id")
    ap.add_argument("--seeds", type=int, default=3, help="number of seeds (run indices)")
    ap.add_argument("--seed-base", type=int, default=None)
    ap.add_argument("--seed-list", default=None, help="comma-separated explicit seeds (regression re-runs)")
    ap.add_argument("--arms", default="A,B,C")
    ap.add_argument("--arm-counts", default=None,
                    help="e.g. A=10,B=1,C=1: arm X runs on the first N seeds only (seeds = the largest N)")
    ap.add_argument("--backend", default="claude_cli", choices=["claude_cli", "scripted"])
    ap.add_argument("--parallel", type=int, default=6)
    ap.add_argument("--token-cap-run", type=int, default=4_000_000)
    ap.add_argument("--token-cap-batch", type=int, default=60_000_000)
    ap.add_argument("--max-scenes", type=int, default=5)
    ap.add_argument("--cohort-id", default=None, help="force one cohort for every run (pilot)")
    ap.add_argument("--player-model", default=None)
    ap.add_argument("--gm-model", default=None)
    ap.add_argument("--prefs", action="store_true", help="run the paired transcript preference phase")
    a = ap.parse_args()
    arms = a.arms.split(",")
    counts = None
    if a.arm_counts:
        counts = {k: int(v) for k, v in (x.split("=") for x in a.arm_counts.split(","))}
        arms = list(counts)
        a.seeds = max(counts.values())
    seeds = [int(x) for x in a.seed_list.split(",")] if a.seed_list else seeds_for(a.batch_id, a.seeds, a.seed_base)
    models = {}
    if a.player_model:
        models["player"] = models["interviewer"] = a.player_model
    if a.gm_model:
        models["gm"] = models["referee"] = models["analyst"] = a.gm_model
    out_dir = ROOT / "runs" / a.batch_id
    out_dir.mkdir(parents=True, exist_ok=True)
    cfg = {"batch_id": a.batch_id, "backend": a.backend, "out_dir": out_dir, "cache_dir": ROOT / "cache" / a.batch_id,
           "token_cap_run": a.token_cap_run, "models": models, "max_scenes": a.max_scenes, "parallel": a.parallel}
    manifest = {"batch_id": a.batch_id, "arms": arms, "seeds": seeds, "backend": a.backend,
                "models": {**MODELS, **models}, "max_scenes": a.max_scenes, "token_cap_run": a.token_cap_run,
                "token_cap_batch": a.token_cap_batch, "cohort_id": a.cohort_id, "arm_counts": counts, "started": time.strftime("%Y-%m-%dT%H:%M:%S")}
    (out_dir / "_manifest.json").write_text(json.dumps(manifest, indent=1))
    batch_meter = TokenMeter(a.token_cap_batch)
    # Cohorts first (sequentially), so parallel runs never race to create the same one.
    jobs = []
    for i, seed in enumerate(seeds):
        cid = a.cohort_id or f"{a.batch_id}-cohort{cohort_index_for_run(i):02d}"
        client = LLMClient(a.backend, cache_dir=None, run_id=cid, run_meter=TokenMeter(None), batch_meter=batch_meter,
                           models=models)
        generate_cohort(cid, derive_seed(0, f"cohort:{cid}") % 10**6, backend=a.backend, client=client, world=WORLD)
        for arm in arms:
            if counts and i >= counts[arm]:
                continue
            run_id = f"{a.batch_id}__{arm}__s{seed}__r{i}"
            p = out_dir / f"{run_id}.json"
            if p.exists() and json.loads(p.read_text()).get("status") in FINAL:
                continue
            jobs.append({"arm": arm, "seed": seed, "run_index": i, "cohort_id": cid})
    print(f"{len(jobs)} runs to do ({len(seeds)} seeds × {len(arms)} arms; others already final)", flush=True)
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=a.parallel) as ex:
        futs = {ex.submit(run_job, j, cfg, batch_meter): j for j in jobs}
        for f in as_completed(futs):
            try:
                r = f.result()
            except Exception as e:   # never let one run kill the batch
                r = {"run_id": str(futs[f]), "status": "crashed", "error": repr(e)}
            print(json.dumps(r), flush=True)
    print(f"runs done in {time.time() - t0:.0f}s; batch tokens {batch_meter.as_dict()}", flush=True)
    if a.prefs:
        try:
            prefs = run_preferences(cfg, arms, seeds, batch_meter)
            print(f"preferences: {len(prefs['items'])} judgments", flush=True)
        except (BudgetExceeded, AgentFailure) as e:
            print(f"preference phase stopped: {e}", flush=True)
    manifest["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    manifest["batch_tokens"] = batch_meter.as_dict()
    (out_dir / "_manifest.json").write_text(json.dumps(manifest, indent=1))


if __name__ == "__main__":
    main()
