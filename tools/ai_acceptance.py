#!/usr/bin/env python3
"""Run the AI acceptance tests of Prompts 4.C and write one report.

Reads the three head-to-head batches the Facilitator ordered, runs the exploit
sweep against T2, and grades every acceptance check. Evidence only.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.batch import run_batch
from engine.kits import load_roster
from engine.stats import wilson
from engine.state import TEAMS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPLOITS = ["X_exploit_dive", "X_exploit_farm", "X_exploit_splitpush",
            "X_exploit_objectives", "X_exploit_turtle", "X_exploit_cdlock"]


def load(batch_id: str) -> dict:
    with open(os.path.join(ROOT, "reports", f"{batch_id}.json")) as fh:
        return json.load(fh)


def head_to_head(rep: dict) -> tuple:
    """p1's win rate: p1 always takes the first-priority seat."""
    g = rep["game"]
    return g["priority_wr"], g["priority_ci"][0], g["priority_ci"][1]


def run_exploits(games: int, seed: int, workers: int, ai: str, roster: str) -> list:
    rows = []
    for name in EXPLOITS:
        spec = {
            "batch_id": f"exploit_{name}", "rules": "1.0.0", "roster": roster, "ai": ai,
            "roster_path": os.path.join(ROOT, "roster", f"roster_v{roster}.json"),
            "matchup": {"p1": name, "p2": "T2_search", "temperature": 0.3},
            "p1": name, "p2": "T2_search", "temperature": 0.3,
            "games": games, "seat_swap": True, "seed": seed, "replays": 0,
        }
        t0 = time.time()
        res = run_batch(spec, workers=workers)
        wins = sum(1 for r in res if r["winner"] is not None and r["winner"] == r["first"])
        decided = sum(1 for r in res if r["winner"] is not None)
        p, lo, hi = wilson(wins, max(1, decided))
        anomalies = sum(len(r["anomalies"]) for r in res)
        rows.append({"policy": name, "games": len(res), "wr": p, "lo": lo, "hi": hi,
                     "anomalies": anomalies, "runtime": time.time() - t0,
                     "median_rounds": sorted(r["rounds"] for r in res)[len(res) // 2]})
        print(f"  {name:<24} {p:5.1f}% [{lo:.1f}, {hi:.1f}]  "
              f"{rows[-1]['runtime']:.0f}s  anomalies={anomalies}")
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--t1vt0", dest="b_t1t0", default="batch_0005")
    ap.add_argument("--t2vt1", dest="b_t2t1", default="batch_0006")
    ap.add_argument("--mirror", dest="b_mirror", default="batch_0007")
    ap.add_argument("--exploit-games", type=int, default=60)
    ap.add_argument("--seed", type=int, default=777100)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--ai", default="1.1.0")
    ap.add_argument("--roster", default="1.1.0")
    args = ap.parse_args()

    t1t0, t2t1, mirror = load(args.b_t1t0), load(args.b_t2t1), load(args.b_mirror)
    kits = load_roster(os.path.join(ROOT, "roster", f"roster_v{args.roster}.json"))

    print("exploit sweep vs T2_search:")
    exploits = run_exploits(args.exploit_games, args.seed, args.workers, args.ai, args.roster)

    checks = []
    p, lo, hi = head_to_head(t1t0)
    checks.append(("T1 beats T0 in >=90% of games", f"{p:.1f}% [{lo:.1f}, {hi:.1f}]",
                   "PASS" if lo >= 90 else ("FAIL" if hi < 90 else "INCONCLUSIVE"),
                   args.b_t1t0))
    p, lo, hi = head_to_head(t2t1)
    checks.append(("T2 beats T1 in >=65% of games", f"{p:.1f}% [{lo:.1f}, {hi:.1f}]",
                   "PASS" if lo >= 65 else ("FAIL" if hi < 65 else "INCONCLUSIVE"),
                   args.b_t2t1))
    p, lo, hi = head_to_head(mirror)
    checks.append(("Mirror T2 vs T2, seats swapped, lands at 50 +/- 2%",
                   f"{p:.1f}% [{lo:.1f}, {hi:.1f}]",
                   "PASS" if lo >= 48 and hi <= 52 else
                   ("FAIL" if hi < 48 or lo > 52 else "INCONCLUSIVE"), args.b_mirror))
    illegal = sum(v for rep in (t1t0, t2t1, mirror) for k, v in rep["anomalies"].items()
                  if k.startswith("ILLEGAL"))
    illegal += sum(r["anomalies"] for r in exploits)
    checks.append(("No illegal action is ever submitted", f"{illegal} illegal states",
                   "PASS" if illegal == 0 else "FAIL", "all batches"))

    unused = []
    for c in mirror["champions"]:
        for key, val in c["usage"].items():
            if val is not None and val <= 5:
                unused.append((c["id"], key, val))
    checks.append(("Every ability used >5% of the time under T2",
                   f"{len(unused)} of {sum(1 for c in mirror['champions'] for v in c['usage'].values() if v is not None)} below 5%",
                   "PASS" if not unused else "FAIL", args.b_mirror))
    rt = mirror["header"]["runtime_s"] / max(1, mirror["header"]["games"])
    checks.append(("Decisions stay inside the time budget",
                   f"{rt:.2f}s per game wall clock on {args.workers} workers; "
                   f"a 2,000-game T2 batch projects to {rt * 2000 / 60:.0f} min",
                   "PASS" if rt * 2000 / 60 <= 120 else "FAIL", args.b_mirror))
    worst = max(exploits, key=lambda r: r["wr"])
    checks.append(("No exploit policy beats T2 more than 60% (Phase 5 gate)",
                   f"worst is {worst['policy']} at {worst['wr']:.1f}% [{worst['lo']:.1f}, {worst['hi']:.1f}]",
                   "PASS" if worst["hi"] <= 60 else
                   ("FAIL" if worst["lo"] > 60 else "INCONCLUSIVE"), "exploit sweep"))

    L = [f"# AI acceptance report - ai {args.ai}, roster {args.roster}", "",
         f"Generated {time.strftime('%Y-%m-%d %H:%M:%S')}. Batches: {args.b_t1t0} "
         f"(T1 vs T0), {args.b_t2t1} (T2 vs T1), {args.b_mirror} (T2 mirror), plus a "
         f"{args.exploit_games}-game sweep per exploit policy against T2.", "",
         "## Acceptance checks (Prompts 4.C)", "",
         "| check | value | verdict | evidence |", "|---|---|---|---|"]
    for name, value, verdict, ev in checks:
        L.append(f"| {name} | {value} | **{verdict}** | {ev} |")
    L += ["", "## Exploit sweep vs T2_search", "",
          "| policy | games | win rate [95% CI] | median rounds | illegal states |",
          "|---|---|---|---|---|"]
    for r in exploits:
        L.append(f"| {r['policy']} | {r['games']} | {r['wr']:.1f} [{r['lo']:.1f}, {r['hi']:.1f}] | "
                 f"{r['median_rounds']} | {r['anomalies']} |")
    if unused:
        L += ["", "## Abilities under 5% use in the mirror batch", "",
              "| champion | ability | cost | usage |", "|---|---|---|---|"]
        for cid, key, val in sorted(unused, key=lambda t: t[2]):
            cost = kits[cid]["abilities"][key]["cost"]
            L.append(f"| {cid} | {key} | {cost} AP | {val:.1f}% |")
    L.append("")
    out = os.path.join(ROOT, "reports", f"ai_acceptance_v{args.ai}.md")
    with open(out, "w") as fh:
        fh.write("\n".join(L))
    with open(out.replace(".md", ".json"), "w") as fh:
        json.dump({"checks": [{"check": c, "value": v, "verdict": d, "evidence": e}
                              for c, v, d, e in checks], "exploits": exploits,
                   "unused_abilities": unused}, fh, indent=2)
    print(f"\nwrote {out}")
    for name, value, verdict, _ in checks:
        print(f"  [{verdict:<13}] {name}: {value}")


if __name__ == "__main__":
    main()
