#!/usr/bin/env python3
"""Refit a roster to a new Rules 14.2 point table (RQ-030).

The Designer's rule for this patch: keep every champion's identity - same
icons, same shape, same role - and change only numbers, preferring the fewest
edits that land the kit in the band with every ability worth its activation.
"""
from __future__ import annotations

import argparse
import copy
import itertools
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.kits import (POINTS, ability_gross, ability_net, budget,
                         stat_points, validate_kit)

BAND = (20, 24)
SCALED = {"HIT", "AREA", "LINE", "HEAL", "SHIELD"}   # steps whose size we may tune


RANGE_EDIT_COST = 3      # range is identity: a range 3 marksman is not a range 1 one


def step_variants(step: dict):
    """Number tweaks for one icon step, nearest-first. Each variant carries the
    identity cost of the edit, not just a count."""
    out = [(step, 0)]
    ic = step["icon"]
    if ic in ("HIT", "AREA", "LINE", "HEAL", "SHIELD"):
        key = "k" if ic in ("HIT", "AREA", "LINE") else "n"
        base = step.get(key, 1)
        for delta in (-1, -2, 1, 2):
            if 1 <= base + delta <= 4:
                v = dict(step)
                v[key] = base + delta
                out.append((v, 1))
    rng_key = "n" if ic == "LINE" else ("range" if "range" in step else None)
    if rng_key:
        base = step.get(rng_key, 1)
        for delta in (-1, 1, -2):
            lo = 1 if ic != "LINE" else 2
            if lo <= base + delta <= 6:
                v = dict(step)
                v[rng_key] = base + delta
                out.append((v, RANGE_EDIT_COST))
    return out


def ability_variants(ab: dict, points: str, limit: int = 110):
    """Candidate rewrites of one ability, with an edit count."""
    seen = {}
    step_options = [step_variants(s) for s in ab["steps"]]
    for combo in itertools.product(*step_options):
        steps = [c[0] for c in combo]
        edits_steps = sum(c[1] for c in combo)
        if sum(1 for c in combo if c[1]) > 3:
            continue
        # RQ-030 is about cheap abilities being unused, so shedding points by
        # raising the price is normally off the table: the points come out of
        # gross. The one exception is the RQ-035 floor - an AREA or LINE is a
        # farming engine and may not be free - so such an ability may be lifted
        # to the floor, and no further.
        floor = 0
        if any(st["icon"] in ("AREA", "LINE") for st in ab["steps"]):
            floor = POINTS[points].get("min_cost_area_line", 0)
        lo = max(floor, 0)
        options = {max(lo, ab["cost"]), max(lo, ab["cost"] - 1)}
        for cost in sorted(options):
            for cd in sorted({ab["cooldown"], max(1, ab["cooldown"] - 1)}):
                # Carry everything the refit does not tune - the RQ-034 ambush
                # tag above all - rather than rebuilding the ability from its
                # numbers and quietly dropping it.
                cand = dict(ab)
                cand.update(cost=cost, cooldown=cd, steps=[dict(s) for s in steps])
                edits = edits_steps + (cost != ab["cost"]) + (cd != ab["cooldown"])
                if edits > 7:
                    continue
                key = json.dumps(cand, sort_keys=True)
                if key not in seen or seen[key][1] > edits:
                    seen[key] = (cand, edits)
    out = [(c, e, ability_net(c, points), ability_gross(c, points)) for c, e in seen.values()
           if ability_net(c, points) >= POINTS[points]["min_net"]]
    out.sort(key=lambda t: (t[1], abs(t[2] - 6)))
    return out[:limit]


def refit(kit: dict, points: str):
    best = None
    variants = {k: ability_variants(kit["abilities"][k], points) for k in "QWER"}
    if not all(variants.values()):
        return None
    # Stats carry the champion's identity - a 9 HP tank that becomes a 6 HP
    # tank is a different champion - so a stat step costs far more than an
    # ability number here, and the original stats are always tried first.
    hp0, sp0 = kit["stats"]["hp"], kit["stats"]["speed"]
    stat_options = sorted(((hp, sp) for hp in range(6, 10) for sp in range(2, 5)),
                          key=lambda t: 6 * abs(t[0] - hp0) + 8 * abs(t[1] - sp0))
    for hp, sp in stat_options:
        target = 22 - stat_points({"hp": hp, "speed": sp})
        for r_cand, r_edits, r_net, r_gross in variants["R"]:
            for q, w, e in itertools.product(variants["Q"], variants["W"], variants["E"]):
                if max(q[3], w[3], e[3]) >= r_gross:
                    continue                       # R must stay the biggest gross
                cap = POINTS[points].get("max_r_ratio")
                if cap and r_gross > cap * (q[3] + w[3] + e[3]) / 3.0:
                    continue                       # and must not dwarf them
                total = q[2] + w[2] + e[2] + r_net
                if abs(total + stat_points({"hp": hp, "speed": sp}) - 22) > 2:
                    continue
                edits = q[1] + w[1] + e[1] + r_edits
                edits += 6 * abs(hp - hp0) + 8 * abs(sp - sp0)
                score = (edits, abs(total - target))
                if best is None or score < best[0]:
                    out = copy.deepcopy(kit)
                    out["stats"] = {"hp": hp, "speed": sp}
                    for key, cand in zip("QWER", (q[0], w[0], e[0], r_cand)):
                        out["abilities"][key] = cand
                    best = (score, out)
        if best and best[0][0] <= 2:
            break                                   # already a near-identical kit
    return best[1] if best else None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("roster")
    ap.add_argument("--points", default="v2")
    ap.add_argument("--version", default="1.2.0")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    data = json.load(open(args.roster))
    out_champs, failures = [], []
    for kit in data["champions"]:
        kit = copy.deepcopy(kit)
        kit.pop("budget", None)
        fitted = refit(kit, args.points)
        if fitted is None:
            failures.append(kit["id"])
            continue
        fitted["points"] = args.points
        fitted["version"] = args.version
        b = budget(fitted, args.points)
        fitted["budget"] = {k: (int(v) if float(v).is_integer() else v) for k, v in b.items()}
        errs = validate_kit(fitted, args.points)
        if errs:
            failures.append(f"{kit['id']}: {errs}")
        out_champs.append(fitted)
        changed = [k for k in "QWER" if fitted["abilities"][k] != kit["abilities"][k]]
        stat_note = "" if fitted["stats"] == kit["stats"] else f" stats {kit['stats']}->{fitted['stats']}"
        print(f"{kit['id']:<12} total {b['total']:<5} changed {','.join(changed) or '-'}{stat_note}")
    if failures:
        print("FAILED:", failures)
        sys.exit(1)
    data["champions"] = out_champs
    data["version"] = args.version
    data["points"] = args.points
    data["notes"] = ("Refit to the RQ-030 recalibration of Rules 14.2: credits cut to "
                     "-1.5 per AP and -1 per cooldown round, and every ability must net "
                     "at least 4 because it spends a whole activation. Identities, icons "
                     "and roles are unchanged; only numbers moved.")
    out = args.out or args.roster.replace(".json", "_refit.json")
    json.dump(data, open(out, "w"), indent=2)
    print("wrote", out)


if __name__ == "__main__":
    main()
