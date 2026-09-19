#!/usr/bin/env python3
"""Render a roster JSON as a readable card sheet with budget worksheets."""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.kits import ability_gross, ability_net, budget, stat_points, validate_kit


def icons(ab: dict) -> str:
    out = []
    for s in ab["steps"]:
        ic = s["icon"]
        bits = [ic]
        if s.get("k", 1) > 1 and ic in ("HIT",):
            bits[0] = f"HIT x{s['k']}"
        elif ic in ("AREA", "LINE") and s.get("k"):
            bits[0] = f"{ic} {s['k']}"
        if s.get("n") is not None and ic != "LINE":
            bits.append(str(s["n"]))
        if ic == "LINE":
            bits.append(f"len {s['n']}")
        if s.get("range") and ic not in ("MOVE", "DASH", "BLINK"):
            bits.append(f"r{s['range']}")
        if s.get("area"):
            bits.append("(area)")
        tgt = s.get("target")
        if tgt == "enemy_champion":
            bits.append("<>")
        elif tgt in ("ally_champion", "self"):
            bits.append("+")
        out.append(" ".join(bits))
    return " -> ".join(out)


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "roster/roster_v1.0.0.json"
    data = json.load(open(path))
    L = [f"# Roster v{data['version']} (rules {data['rules']})", "",
         data.get("notes", ""), ""]
    for k in data["champions"]:
        b = budget(k)
        errs = validate_kit(k)
        L += [f"## {k['name']} — {k['role']}", "",
              f"*{k['identity']}*", "",
              f"**HP {k['stats']['hp']} · Speed {k['stats']['speed']}** "
              f"(stats {stat_points(k['stats']):+g} points)", "",
              "| ability | cost / CD | icon sequence | gross | net |",
              "|---|---|---|---|---|"]
        for key in ("Q", "W", "E", "R"):
            ab = k["abilities"][key]
            L.append(f"| {key} | {ab['cost']} / {ab['cooldown']} | {icons(ab)} | "
                     f"{ability_gross(ab):g} | {ability_net(ab):g} |")
        L += ["", f"**Budget total: {b['total']:g}** "
                  f"({'on budget' if not errs else 'INVALID: ' + '; '.join(errs)})", "",
              f"Notes: {k.get('notes', '-')}", ""]
    L += ["## Budget summary", "",
          "| champion | role | HP | Speed | stats | Q | W | E | R | total |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for k in data["champions"]:
        b = budget(k)
        L.append(f"| {k['name']} | {k['role']} | {k['stats']['hp']} | {k['stats']['speed']} | "
                 f"{b['stats']:g} | {b['Q']:g} | {b['W']:g} | {b['E']:g} | {b['R']:g} | {b['total']:g} |")
    L += ["", "L0 (every champion): 0 AP, cooldown 1, HIT 1 adjacent.", ""]
    out = path.replace(".json", ".md")
    open(out, "w").write("\n".join(L))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
