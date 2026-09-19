#!/usr/bin/env python3
"""Head-to-head calibration runs for the AI Developer.

Each variant plays p1 (the first-priority seat) against a fixed opponent, so
the reported number is that variant's win rate. Seats and priority swap every
other game, so the number is not a seat artefact.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.batch import run_batch
from engine.stats import wilson

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def head_to_head(name, p1, p2, games, seed, workers, p1_config=None, p2_config=None,
                 ai="1.1.0", roster="1.1.0"):
    spec = {"batch_id": f"cal_{name}", "rules": "1.0.0", "roster": roster, "ai": ai,
            "roster_path": os.path.join(ROOT, "roster", f"roster_v{roster}.json"),
            "matchup": {"p1": p1, "p2": p2, "temperature": 0.3},
            "p1": p1, "p2": p2, "temperature": 0.3, "games": games,
            "seat_swap": True, "seed": seed, "replays": 0,
            "p1_config": p1_config or {}, "p2_config": p2_config or {}}
    t0 = time.time()
    res = run_batch(spec, workers=workers)
    decided = [r for r in res if r["winner"] is not None]
    wins = sum(1 for r in decided if r["winner"] == r["first"])
    p, lo, hi = wilson(wins, max(1, len(decided)))
    rounds = sorted(r["rounds"] for r in res)
    out = {"name": name, "p1": p1, "p2": p2, "games": len(res), "wr": p, "lo": lo, "hi": hi,
           "median_rounds": rounds[len(rounds) // 2], "runtime": time.time() - t0,
           "anomalies": sum(len(r["anomalies"]) for r in res),
           "p1_config": p1_config or {}}
    print(f"{name:<28} {p:5.1f}% [{lo:5.1f}, {hi:5.1f}]  n={len(res)}  "
          f"{out['runtime']:5.0f}s  median {out['median_rounds']}r  anomalies={out['anomalies']}")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", help="json file with a list of variant specs")
    ap.add_argument("--games", type=int, default=60)
    ap.add_argument("--seed", type=int, default=880001)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    with open(args.plan) as fh:
        plan = json.load(fh)
    rows = []
    for v in plan:
        rows.append(head_to_head(v["name"], v["p1"], v["p2"], v.get("games", args.games),
                                 args.seed, args.workers, v.get("p1_config"),
                                 v.get("p2_config")))
    if args.out:
        with open(args.out, "w") as fh:
            json.dump(rows, fh, indent=2)
        print("wrote", args.out)


if __name__ == "__main__":
    main()
