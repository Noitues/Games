#!/usr/bin/env python3
"""Which abilities does a batch actually use, and what predicts that?

The Rules 14.3 usage target is a per-ability threshold, so a failing report
lists 47 dead abilities and stops there. That list does not say whether the
roster has 47 separate weak kits or one shared cause.

This tool reads a batch report plus the roster it was played with and groups
the same usage numbers by slot, AP cost, cooldown and 14.2 budget value. A kit
problem scatters; a pricing problem lines up.

Denominator note: the engine records an opportunity for an ability in a round
only when the champion could activate, the ability was affordable, and it had
a legal plan (RQ-014). Every ability ready in the same round therefore shares
that round's denominator, so the per-champion shares below compete directly.
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import statistics
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

ABIL = ("Q", "W", "E", "R")


def load(batch: str, roster: str):
    bpath = batch if os.path.sep in batch else os.path.join(ROOT, "reports", f"{batch}.json")
    rpath = roster if os.path.sep in roster else os.path.join(ROOT, "roster", f"roster_v{roster}.json")
    with open(bpath) as fh:
        b = json.load(fh)
    with open(rpath) as fh:
        r = json.load(fh)
    return b, r


def build_rows(batch, roster):
    """One row per (champion, ability), carrying its price and its use."""
    usage = {c["id"]: c["usage"] for c in batch["champions"]}
    rows = []
    for champ in roster["champions"]:
        use = usage.get(champ["id"])
        if not use:
            continue
        total = sum(v for v in use.values() if v) or 1.0
        for slot in ABIL:
            spec = champ["abilities"][slot]
            rows.append({
                "champ": champ["id"], "role": champ["role"], "slot": slot,
                "cost": spec["cost"], "cd": spec["cooldown"],
                "budget": champ["budget"][slot],
                "use": use[slot] or 0.0,
                "share": (use[slot] or 0.0) / total * 100,
            })
    return rows


def group(rows, key, label):
    out = [f"| {label} | abilities | mean use | median use | under 5% |",
           "|---|---|---|---|---|"]
    for val in sorted({r[key] for r in rows}):
        sel = [r for r in rows if r[key] == val]
        uses = [r["use"] for r in sel]
        dead = sum(1 for u in uses if u < 5.0)
        out.append(f"| {val} | {len(sel)} | {statistics.mean(uses):.1f}% | "
                   f"{statistics.median(uses):.1f}% | {dead}/{len(sel)} |")
    return "\n".join(out)


def concentration(rows):
    by = collections.defaultdict(list)
    for r in rows:
        by[r["champ"]].append(r)
    out = ["| champion | top ability | its share | abilities >=5% of activations |",
           "|---|---|---|---|"]
    live = []
    for champ in sorted(by, key=lambda c: -max(r["share"] for r in by[c])):
        kit = by[champ]
        top = max(kit, key=lambda r: r["share"])
        n = sum(1 for r in kit if r["share"] >= 5.0)
        live.append(n)
        out.append(f"| {champ} | {top['slot']} | {top['share']:.0f}% | {n} of 4 |")
    return "\n".join(out), live


def render(batch, roster, rows, name):
    live_tbl, live = concentration(rows)
    dead = [r for r in rows if r["use"] < 5.0]
    top_heavy = sum(1 for c in {r["champ"] for r in rows}
                    if max(r["share"] for r in rows if r["champ"] == c) >= 70)
    parts = [
        f"# Ability usage diagnosis - {name}, roster {roster['version']}",
        "",
        f"{len(dead)} of {len(rows)} abilities fall under the Rules 14.3 5% "
        f"threshold. The roster carries {len(live)} champions; a mean of "
        f"{statistics.mean(live):.2f} of their 4 abilities clear 5% of that "
        f"champion's own activations, and {top_heavy} of {len(live)} champions "
        "spend 70% or more of their activations on a single ability.",
        "",
        "## Usage by slot", "", group(rows, "slot", "slot"), "",
        "## Usage by AP cost", "", group(rows, "cost", "AP cost"), "",
        "## Usage by cooldown", "", group(rows, "cd", "cooldown"), "",
        "## Usage by 14.2 budget value", "", group(rows, "budget", "budget"), "",
        "## Concentration per champion", "", live_tbl, "",
    ]
    return "\n".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch", default="batch_0009", help="batch id or path to its json")
    ap.add_argument("--roster", default="1.1.0", help="roster version or path to its json")
    ap.add_argument("--out", default=None, help="write markdown here instead of stdout")
    args = ap.parse_args()

    batch, roster = load(args.batch, args.roster)
    rows = build_rows(batch, roster)
    if not rows:
        print("no champion usage in that batch", file=sys.stderr)
        return 1
    text = render(batch, roster, rows, args.batch)
    if args.out:
        with open(args.out, "w") as fh:
            fh.write(text + "\n")
        print(f"wrote {args.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
