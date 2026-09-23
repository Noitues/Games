"""Batch runner: team sampling, seat swapping, parallel execution."""
from __future__ import annotations

import json
import os
import random
import time
from dataclasses import asdict
from multiprocessing import Pool
from typing import Dict, List, Optional, Tuple

import importlib
from engine.config import make_config
from engine.game import new_game
from engine.hexmap import Board
from engine.kits import load_roster
from engine.run import Game, GameResult
from engine.state import TEAMS

ROLES = ("Top", "Jungle", "Mid", "ADC", "Support")
_CACHE: Dict[str, object] = {}


def _policy_factory(ai_version: str):
    mod = importlib.import_module(f"ai.policy_v{ai_version.replace('.', '_')}")
    return mod.make


def _resources(roster_path: str):
    if "board" not in _CACHE:
        _CACHE["board"] = Board.load()
    if roster_path not in _CACHE:
        _CACHE[roster_path] = load_roster(roster_path)
    return _CACHE["board"], _CACHE[roster_path]


def sample_picks(kits: dict, rng: random.Random) -> Dict[str, List[str]]:
    """random_by_role_no_duplicates: with 2 champions per role, every champion
    appears in every game, on one side or the other."""
    by_role: Dict[str, List[str]] = {}
    for k in kits.values():
        by_role.setdefault(k["role"], []).append(k["id"])
    picks = {"north": [], "south": []}
    for role in ROLES:
        pair = sorted(by_role[role])
        rng.shuffle(pair)
        picks["north"].append(pair[0])
        picks["south"].append(pair[1])
    return picks


def play_one(args: tuple) -> dict:
    (i, spec) = args
    board, kits = _resources(spec["roster_path"])
    cfg = make_config(**spec.get("config_overrides", {}))
    rng = random.Random(spec["seed"] * 1_000_003 + (i // 2))
    picks = sample_picks(kits, rng)
    swap = (i % 2 == 1) and spec.get("seat_swap", True)
    if swap:
        picks = {"north": picks["south"], "south": picks["north"]}
    first = "south" if swap else "north"
    st = new_game(board, kits, picks, cfg, first=first)
    make_policy = _policy_factory(spec.get("ai", "1.0.0"))
    p1_cfg = spec.get("p1_config") or {}
    p2_cfg = spec.get("p2_config") or {}
    p1_tier, p2_tier = spec["p1"], spec["p2"]
    pool = spec.get("personality_pool")
    if pool:
        # A play-test evening, not a mirror: each side draws an appetite. The
        # pair is drawn from the game index so both seats of a swapped pair see
        # the same two personalities in opposite seats.
        prng = random.Random(spec["seed"] * 104_729 + (i // 2))
        p1_tier, p2_tier = prng.sample(list(pool), 2) if len(pool) > 1 else (pool[0], pool[0])
    pols = {}
    seats = (("north", p1_tier, p1_cfg), ("south", p2_tier, p2_cfg)) if first == "north" \
        else (("north", p2_tier, p2_cfg), ("south", p1_tier, p1_cfg))
    for t, tier, pcfg in seats:
        pols[t] = make_policy(tier, spec["seed"] * 7919 + i * 31 + (0 if t == "north" else 1),
                              spec.get("temperature", 0.3), config=dict(pcfg), team=t)
    tiers = {t: pols[t].tier for t in TEAMS}
    g = Game(st, pols, seed=i, replay=i < spec.get("replays", 0), strict=False)
    t0 = time.time()
    res = g.run()
    out = asdict(res)
    out["tiers"] = tiers
    # ai 1.4.0 state machines record which personality they occupied each
    # round; a fixed personality has no such record.
    out["states"] = {t: getattr(pols[t], "occupancy", None) for t in TEAMS}
    out["runtime"] = time.time() - t0
    out["game_index"] = i
    return out


def run_batch(spec: dict, workers: int = 0, checkpoint: Optional[str] = None) -> List[dict]:
    """Play every game in the spec. With `checkpoint`, each finished game is
    appended to that JSONL file as it completes and games already in it are
    not replayed, so a run killed part-way (the cloud container is reclaimed
    when idle) resumes where it stopped instead of starting over."""
    n = spec["games"]
    done: Dict[int, dict] = {}
    if checkpoint and os.path.exists(checkpoint):
        with open(checkpoint) as fh:
            for line in fh:
                if line.strip():
                    r = json.loads(line)
                    if r.get("game_index", -1) < n:
                        done[r["game_index"]] = r
    jobs = [(i, spec) for i in range(n) if i not in done]
    spec["resumed_games"] = len(done)
    workers = workers or min(os.cpu_count() or 1, 8)

    def keep(r: dict) -> None:
        done[r["game_index"]] = r
        if checkpoint:
            with open(checkpoint, "a") as fh:
                fh.write(json.dumps(r) + "\n")

    if workers == 1:
        for j in jobs:
            keep(play_one(j))
    elif jobs:
        with Pool(workers) as pool:
            for r in pool.imap_unordered(play_one, jobs, chunksize=1):
                keep(r)
    return [done[i] for i in range(n)]
