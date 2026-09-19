#!/usr/bin/env python3
"""Compact text viewer for the JSON replays a batch writes (Prompts 4.D)."""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def render(game: dict, limit: int = 0) -> str:
    L = [f"game {game['game']}: {game['picks']['north']} (north) vs "
         f"{game['picks']['south']} (south)",
         f"winner: {game['winner']} in {game['rounds']} rounds", ""]
    for ev in game["events"]:
        t = ev["t"]
        if t == "round":
            L.append(f"--- round {ev['n']}  priority {ev['priority']}  "
                     f"AP north {ev['ap']['north']} / south {ev['ap']['south']}")
        elif t == "act":
            bits = [f"  {ev['champ']:<14}"]
            if ev.get("recall"):
                bits.append("recall")
            if ev.get("dest"):
                d = ev["dest"]
                bits.append(f"-> {'tile ' + str(d[1]) if d[0] == 'T' else tuple(d[1:])}")
            bits.append(ev["ability"] or "move only")
            if ev.get("card"):
                bits.append(f"+{ev['card']}")
            if ev.get("ap"):
                bits.append(f"[{ev['ap']:+d} AP]")
            L.append(" ".join(bits))
        elif t == "kill":
            L.append(f"  *** {ev['victim']} dies (credit {ev['team']})")
        elif t == "structure_down":
            L.append(f"  *** {ev['uid']} destroyed")
        elif t == "monster_killed":
            L.append(f"  *** {ev['mtype']} taken by {ev['team']}")
        if limit and len(L) >= limit:
            L.append("  ...")
            break
    return "\n".join(L)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("replays", help="reports/batch_XXXX_replays.json")
    ap.add_argument("--game", type=int, default=0, help="index within the file")
    ap.add_argument("--limit", type=int, default=0, help="max lines")
    args = ap.parse_args()
    with open(args.replays) as fh:
        games = json.load(fh)
    print(render(games[args.game], args.limit))


if __name__ == "__main__":
    main()
