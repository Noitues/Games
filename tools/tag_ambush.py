#!/usr/bin/env python3
"""Tag each champion's ambush ability - the one it may use out of cover (RQ-034).

The lead designer's rule: roughly one per champion, two for junglers, and it
should be a move-and-attack that commits the champion rather than a poke that
lets it snipe from cover. Where a kit has no move-and-attack, the shortest
ranged damage ability is the closest thing to committing.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MOVE = {"DASH", "BLINK", "MOVE", "CHARGE"}
DAMAGE = {"HIT", "AREA", "LINE"}
PER_ROLE = {"Jungle": 2}          # junglers live in the fog; everyone else gets one


def ability_profile(ab: dict) -> dict:
    icons = [s["icon"] for s in ab["steps"]]
    reach = max([s.get("range") or s.get("n") or 1 for s in ab["steps"]] or [1])
    return {"move": any(i in MOVE for i in icons), "damage": any(i in DAMAGE for i in icons),
            "reach": reach, "icons": "+".join(icons)}


def score(ab: dict) -> tuple:
    """Higher is a better ambush. Committing beats poking."""
    p = ability_profile(ab)
    return (p["move"] and p["damage"],      # a move-and-attack is the ideal
            p["damage"],                    # then a real attack: a champion whose
                                            # only tag was a BLINK could not ambush
                                            # at all, it could only run
            p["move"],
            -p["reach"],                    # then the shortest reach: least sniping
            -ab["cooldown"], -ab["cost"])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("roster")
    ap.add_argument("--out", required=True)
    ap.add_argument("--version", default="1.3.0")
    args = ap.parse_args()
    data = json.load(open(args.roster))
    print(f"{'champion':<13}{'role':<9}{'tagged':<8}{'why'}")
    for kit in data["champions"]:
        n = PER_ROLE.get(kit["role"], 1)
        ranked = sorted("QWER", key=lambda s: score(kit["abilities"][s]), reverse=True)
        chosen = ranked[:n]
        for s in "QWER":
            kit["abilities"][s]["from_hidden"] = s in chosen
        kit["version"] = args.version
        p = ability_profile(kit["abilities"][chosen[0]])
        why = ("move-and-attack" if p["move"] and p["damage"] else
               "closes the gap" if p["move"] else
               f"shortest-reach attack (r{p['reach']})" if p["damage"] else "only option")
        print(f"{kit['id']:<13}{kit['role']:<9}{','.join(chosen):<8}{p['icons']} - {why}")
    data["version"] = args.version
    data["notes"] = (data.get("notes", "") + " RQ-034: each champion carries one ambush "
                     "ability usable out of a hidden hexgroup, two for junglers; using one "
                     "outward flips the hexgroup face up for the rest of the round.").strip()
    json.dump(data, open(args.out, "w"), indent=2)
    print("\nwrote", args.out)


if __name__ == "__main__":
    main()
