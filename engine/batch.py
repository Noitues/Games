"""Batch runner: team sampling, seat swapping, parallel execution."""
from __future__ import annotations

import json
import os
import random
import time
from dataclasses import asdict
from multiprocessing import Pool
from typing import Dict, List, Optional, Tuple

from ai.policy_v1_0_0 import make as make_policy
from engine.config import make_config
from engine.game import new_game
from engine.hexmap import Board
from engine.kits import load_roster
from engine.run import Game, GameResult
from engine.state import TEAMS

ROLES = ("Top", "Jungle", "Mid", "ADC", "Support")
_CACHE: Dict[str, object] = {}


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
    pols = {}
    for t, tier in (("north", spec["p1"] if first == "north" else spec["p2"]),
                    ("south", spec["p2"] if first == "north" else spec["p1"])):
        pols[t] = make_policy(tier, spec["seed"] * 7919 + i * 31 + (0 if t == "north" else 1),
                              spec.get("temperature", 0.3), team=t)
    tiers = {t: pols[t].tier for t in TEAMS}
    g = Game(st, pols, seed=i, replay=i < spec.get("replays", 0), strict=False)
    t0 = time.time()
    res = g.run()
    out = asdict(res)
    out["tiers"] = tiers
    out["runtime"] = time.time() - t0
    out["game_index"] = i
    return out


def run_batch(spec: dict, workers: int = 0) -> List[dict]:
    n = spec["games"]
    jobs = [(i, spec) for i in range(n)]
    workers = workers or min(os.cpu_count() or 1, 8)
    if workers == 1:
        return [play_one(j) for j in jobs]
    with Pool(workers) as pool:
        return pool.map(play_one, jobs, chunksize=max(1, n // (workers * 8)))
