#!/usr/bin/env python3
"""Phase read (RQ-049): does each phase of the game pay, in order?

The designer's target order is laning (last hits and jungle) -> sieging and
objectives -> team fights and sieging -> Baron and ending. This reads the
per-round trace a batch dumps (GameResult.trace) and answers two questions
per phase:

  1. Where does the AP come from in that window? A phase is rewarded when its
     own source is the largest earned (non-base) share of the window.
  2. Does winning that phase win the game? The leader's win rate at the
     phase's checkpoint, with a Wilson interval.

Usage: phase_read.py reports/raw/<batch>.jsonl.gz [more ...] [--json out.json]
"""
from __future__ import annotations

import argparse
import gzip
import json
import math
import os
import sys
from collections import Counter, defaultdict

TEAMS = ("north", "south")
WINDOWS = (("laning", 1, 4), ("siege_objectives", 5, 8), ("fights_siege", 9, 12), ("baron_end", 13, 99))
# How each AP source is filed. Anything not named here is farm: wave and
# monster chips under whatever step name the engine gives them.
SOURCE_CLASS = {"base": "base", "kill": "kills", "tower_kill": "towers", "last_hit": "farm",
                "blue_buff": "farm"}


def other(t):
    return "south" if t == "north" else "north"


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"),) * 3
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, c - h, c + h


def load(paths):
    for p in paths:
        op = gzip.open if p.endswith(".gz") else open
        with op(p, "rt") as fh:
            for line in fh:
                if line.strip():
                    yield json.loads(line)


def at(trace, r):
    """The trace entry at the end of round r, or the last one before it."""
    best = None
    for e in trace:
        if e["r"] <= r:
            best = e
    return best


def classed(ap):
    out = Counter()
    for src, n in ap.items():
        out[SOURCE_CLASS.get(src, "farm")] += n
    return out


def read(games):
    n = 0
    ends = Counter()
    rounds = []
    window_ap = {w[0]: Counter() for w in WINDOWS}
    leaders = {k: [0, 0, 0] for k in ("farm_r4", "structures_dragons_r8", "kills_r9_12", "baron")}
    firsts = defaultdict(list)
    baron_taken = 0
    nexus_by_baron_holder = [0, 0]
    tier_wins = Counter()
    tier_games = Counter()
    for g in games:
        tr = g.get("trace") or []
        if not tr:
            continue
        n += 1
        ends[g["end_reason"]] += 1
        rounds.append(g["rounds"])
        w = g.get("winner")
        for t in TEAMS:
            tier = (g.get("tiers") or {}).get(t)
            if tier:
                tier_games[tier] += 1
                tier_wins[tier] += int(w == t)
        # AP by class per window: difference of cumulative sources.
        prev = {t: Counter() for t in TEAMS}
        for e in tr:
            win = next(name for name, lo, hi in WINDOWS if lo <= e["r"] <= hi)
            for t in TEAMS:
                cur = classed(e["ap"][t])
                for k in set(cur) | set(prev[t]):
                    window_ap[win][k] += cur[k] - prev[t][k]
                prev[t] = cur
        # Round of each first.
        seen = set()
        for e in tr:
            for t in TEAMS:
                if "kill" not in seen and e["kills"][t] > 0:
                    seen.add("kill"); firsts["first_kill"].append(e["r"])
                if "tower" not in seen and e["towers_lost"][t] > 0:
                    seen.add("tower"); firsts["first_tower"].append(e["r"])
                if "dragon" not in seen and e["dragons"][t] > 0:
                    seen.add("dragon"); firsts["first_dragon"].append(e["r"])
                if "baron" not in seen and e["baron"][t]:
                    seen.add("baron"); firsts["first_baron"].append(e["r"])

        def score(key, lead_team):
            if lead_team is None:
                leaders[key][2] += 1
                return
            leaders[key][1] += 1
            leaders[key][0] += int(w == lead_team)

        def lead(vals):
            a, b = vals["north"], vals["south"]
            return None if a == b else ("north" if a > b else "south")

        e4 = at(tr, 4)
        if e4:
            score("farm_r4", lead({t: classed(e4["ap"][t])["farm"] for t in TEAMS}))
        e8 = at(tr, 8)
        if e8 and g["rounds"] >= 5:
            score("structures_dragons_r8",
                  lead({t: e8["towers_lost"][other(t)] + e8["dragons"][t] for t in TEAMS}))
        e12 = at(tr, 12)
        if e12 and e8 and g["rounds"] >= 9:
            score("kills_r9_12", lead({t: e12["kills"][t] - e8["kills"][t] for t in TEAMS}))
        holder = next((t for e in tr for t in TEAMS if e["baron"][t]), None)
        if holder:
            baron_taken += 1
            score("baron", holder)
            if g["end_reason"].startswith("nexus") or "nexus" in g["end_reason"]:
                nexus_by_baron_holder[1] += 1
                nexus_by_baron_holder[0] += int(w == holder)
    med = lambda xs: sorted(xs)[len(xs) // 2] if xs else None
    out = {"games": n, "end_reason": dict(ends), "rounds_median": med(rounds),
           "rounds_p90": sorted(rounds)[int(len(rounds) * 0.9)] if rounds else None,
           "firsts_median": {k: med(v) for k, v in firsts.items()},
           "firsts_share": {k: len(v) / n if n else 0 for k, v in firsts.items()},
           "baron_taken": baron_taken / n if n else 0,
           "nexus_kills_by_baron_holder": nexus_by_baron_holder,
           "window_ap_share": {}, "leader_wr": {},
           "tier_wr": {k: tier_wins[k] / tier_games[k] for k in sorted(tier_games)}}
    for name, _, _ in WINDOWS:
        c = window_ap[name]
        earned = sum(v for k, v in c.items() if k != "base")
        out["window_ap_share"][name] = {k: round(c[k] / earned, 3) if earned else 0
                                        for k in ("farm", "towers", "kills")}
        out["window_ap_share"][name]["earned_per_game"] = round(earned / n, 2) if n else 0
    for k, (won, decided, tied) in leaders.items():
        p, lo, hi = wilson(won, decided)
        out["leader_wr"][k] = {"wr": round(p, 3), "lo": round(lo, 3), "hi": round(hi, 3),
                               "n": decided, "tied": tied}
    return out


def to_text(name, o):
    lines = [f"== {name}: {o['games']} games, median {o['rounds_median']} rounds "
             f"(p90 {o['rounds_p90']}), ends {o['end_reason']}"]
    lines.append("  firsts (median round, share of games): " + ", ".join(
        f"{k} r{o['firsts_median'][k]} ({o['firsts_share'][k]:.0%})" for k in sorted(o["firsts_median"])))
    lines.append(f"  Baron taken in {o['baron_taken']:.0%}; Nexus endings won by the Baron holder "
                 f"{o['nexus_kills_by_baron_holder'][0]}/{o['nexus_kills_by_baron_holder'][1]}")
    lines.append("  earned AP by window (share farm / towers / kills, AP per game):")
    for w, s in o["window_ap_share"].items():
        lines.append(f"    {w:<18} {s['farm']:.0%} / {s['towers']:.0%} / {s['kills']:.0%}   "
                     f"{s['earned_per_game']}")
    lines.append("  leader win rate (Wilson 95%):")
    for k, s in o["leader_wr"].items():
        lines.append(f"    {k:<22} {s['wr']:.1%} [{s['lo']:.1%}, {s['hi']:.1%}]  n={s['n']} tied={s['tied']}")
    if o["tier_wr"]:
        lines.append("  personality WR: " + ", ".join(f"{k} {v:.1%}" for k, v in o["tier_wr"].items()))
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()
    res = {}
    for p in args.paths:
        name = os.path.basename(p).split(".")[0]
        res[name] = read(load([p]))
        print(to_text(name, res[name]))
    if args.json:
        with open(args.json, "w") as fh:
            json.dump(res, fh, indent=2)


if __name__ == "__main__":
    sys.exit(main())
