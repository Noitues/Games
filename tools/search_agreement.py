#!/usr/bin/env python3
"""How often does the searched best move differ from the greedy best?

If a searching policy and a one-ply greedy policy pick the same activation
almost every time, depth cannot buy much, and that is a statement about the
game's decision structure rather than about the AI.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.batch import sample_picks
from engine.config import make_config
from engine.game import new_game
from engine.hexmap import Board
from engine.kits import load_roster
from engine.run import Game
from engine.stats import wilson

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build(ai_mod, cfg):
    T2 = ai_mod.TIERS["T2_search"]

    class Recording(T2):
        def __init__(self, *a, **kw):
            super().__init__(*a, **kw)
            self.stats = {"decisions": 0, "same": 0, "gap": 0.0, "flips": []}

        def choose_activation(self, state, legal):
            options = [a for a in legal if not a.is_pass]
            if not options:
                return super().choose_activation(state, legal)
            greedy = max(options, key=lambda a: self.score_activation(state, a))
            saved_t = self.temperature
            self.temperature = 1e-9          # read the search's argmax, not its sample
            try:
                searched = super().choose_activation(state, legal)
            finally:
                self.temperature = saved_t
            self.stats["decisions"] += 1
            if searched == greedy:
                self.stats["same"] += 1
            else:
                g = self.score_activation(state, greedy) - self.score_activation(state, searched)
                self.stats["gap"] += g
                if len(self.stats["flips"]) < 12:
                    champ = getattr(searched, "champ", None)
                    self.stats["flips"].append(
                        {"round": state.round, "champ": champ,
                         "greedy_ability": greedy.ability, "searched_ability": searched.ability,
                         "greedy_minus_searched_greedyvalue": round(g, 2)})
            return searched
    return Recording


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=10)
    ap.add_argument("--seed", type=int, default=99001)
    ap.add_argument("--ai", default="1.1.0")
    ap.add_argument("--roster", default="1.1.0")
    ap.add_argument("--config", default="{}")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    import importlib
    ai_mod = importlib.import_module(f"ai.policy_v{args.ai.replace('.', '_')}")
    Recording = build(ai_mod, json.loads(args.config))
    board = Board.load()
    kits = load_roster(os.path.join(ROOT, "roster", f"roster_v{args.roster}.json"))
    total = {"decisions": 0, "same": 0, "gap": 0.0}
    flips = []
    for i in range(args.games):
        rng = random.Random(args.seed + i)
        picks = sample_picks(kits, rng)
        st = new_game(board, kits, picks, make_config(), first="north")
        rec = Recording(seed=args.seed + i, temperature=0.3, config=json.loads(args.config))
        rec.team = "north"
        opp = ai_mod.make("T1_greedy", args.seed + 500 + i, 0.3, team="south")
        Game(st, {"north": rec, "south": opp}, seed=i, strict=False).run()
        total["decisions"] += rec.stats["decisions"]
        total["same"] += rec.stats["same"]
        total["gap"] += rec.stats["gap"]
        flips.extend(rec.stats["flips"])
    p, lo, hi = wilson(total["same"], max(1, total["decisions"]))
    disagreements = total["decisions"] - total["same"]
    out = {"games": args.games, "decisions": total["decisions"],
           "agreement_pct": p, "agreement_ci": [lo, hi],
           "disagreements": disagreements,
           "mean_greedy_value_given_up": (total["gap"] / disagreements) if disagreements else 0.0,
           "examples": flips[:12]}
    print(json.dumps({k: v for k, v in out.items() if k != "examples"}, indent=2))
    if args.out:
        with open(args.out, "w") as fh:
            json.dump(out, fh, indent=2)
        print("wrote", args.out)


if __name__ == "__main__":
    main()
