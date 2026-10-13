"""Export golden scenarios from the Python engine for the Lua parity harness.

    python tools/tts_parity.py [--games 6] [--config reports/requests/batch_0075.json]

Plays real engine games (AI vs AI). At every Upkeep and every World Phase it
snapshots the state, runs the engine's own step on a copy, and records
(before, after). tts/tests/run.lua replays each `before` through
tts/lua/core.lua and compares with `after`. Output:
``tts/tests/scenarios.json``.

The copies are stepped with the engine's default flip placement (no AI
placer), so the expected result is deterministic; the game itself goes on
with the AI's choices. Each scenario is a state from a real game.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import random
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import engine.run as run_mod                                # noqa: E402
from engine import game as game_mod                         # noqa: E402
from engine.batch import _policy_factory, sample_picks      # noqa: E402
from engine.config import make_config                       # noqa: E402
from engine.game import new_game                            # noqa: E402
from engine.hexmap import Board                             # noqa: E402
from engine.kits import load_roster                         # noqa: E402

ROSTER = os.path.join(ROOT, "roster", "roster_v1.9.0.json")
OUT = os.path.join(ROOT, "tts", "tests", "scenarios.json")


def snapshot(st) -> dict:
    """The state the Lua core models, in its own shape (tts/lua/core.lua)."""
    names = st.board.tile_names
    hidden = [names[t] for t in range(st.board.n_tiles) if st.hidden_mask >> t & 1]
    teams = {}
    for t, ts in st.teams.items():
        cards = {}
        for c in ts.cards:
            cards[c] = cards.get(c, 0) + 1
        teams[t] = {"ap": ts.ap, "kills": ts.kills, "towers_lost": ts.towers_lost,
                    "baron": ts.baron_track > 0, "dragons": ts.dragons,
                    "dragon_track": list(ts.dragon_track), "cards": cards}
    return {
        "round": st.round, "priority": st.priority, "next_uid": st.next_uid,
        "winner": st.winner, "end_reason": st.end_reason,
        "hidden": hidden,
        "wards": {names[t]: r for t, r in getattr(st, "wards", {}).items()},
        "champs": [{"uid": c.uid, "cid": c.cid, "team": c.team, "hp": c.hp, "max_hp": c.max_hp,
                    "hex": list(c.hexpos), "alive": c.alive, "track": c.track,
                    "shield": c.shield, "shield_until": c.shield_until,
                    "items": sorted(c.items)} for c in st.champs.values()],
        "waves": [{"uid": w.uid, "team": w.team, "lane": w.lane, "chips": w.chips,
                   "path_idx": w.path_idx, "hex": list(w.hexpos), "empowered": w.empowered}
                  for w in st.waves.values()],
        "structures": [{"uid": s.uid, "team": s.team, "stype": s.stype, "lane": s.lane,
                        "tier": s.tier, "chips": s.chips, "hex": list(s.hexpos),
                        "alive": s.alive} for s in st.structures.values()],
        "monsters": [{"uid": m.uid, "mtype": m.mtype, "chips": m.chips, "max_chips": m.max_chips,
                      "hex": list(m.hexpos), "alive": m.alive,
                      "respawn_round": m.respawn_round} for m in st.monsters.values()],
        "teams": teams,
    }


class _NoPlacer:
    @staticmethod
    def placer(*_a, **_k):
        return None


def synthetic(board, kits, cfg, seed: int) -> list:
    """World Phases where a minion wave takes a structure, which AI games
    rarely produce (champions take most towers in the Action Phase). Built
    from a fresh game: an enemy wave on its lane path next to the target, the
    target at 2 chips (a plain wave leaves 1, an Empowered one fells it) and,
    for the Nexus, one lane of towers down. The
    engine computes the expected result as usual."""
    from engine.state import Wave
    out = []
    rng = random.Random(seed)
    for team in ("north", "south"):
        enemy = "south" if team == "north" else "north"
        for target in ("top_T1", "mid_T1", "bot_T1", "nexus"):
            for empowered in (False, True):
                st = new_game(board, kits, sample_picks(kits, rng), copy.deepcopy(cfg))
                st.round = 9
                lane = "mid" if target == "nexus" else target.split("_")[0]
                tgt = st.structures[f"{team[0]}_{target}"]
                if target == "nexus":
                    for tier in (1, 2):
                        st.structures[f"{team[0]}_{lane}_T{tier}"].alive = False
                        st.structures[f"{team[0]}_{lane}_T{tier}"].chips = 0
                tgt.chips = 2          # one hit leaves 1; an Empowered wave fells it
                # lane names mirror between teams (North's bot path runs past
                # South's top towers): use whichever enemy lane passes by
                spot = next((ln, i) for ln, path in board.lane_paths[enemy].items()
                            for i, h in enumerate(path)
                            if max(abs(h[0] - tgt.hexpos[0]), abs(h[1] - tgt.hexpos[1]),
                                   abs(h[0] - tgt.hexpos[0] + h[1] - tgt.hexpos[1])) == 1
                            and not any(u.alive and u.hexpos == h for u in st.all_units()))
                wave_lane, idx = spot
                path = board.lane_paths[enemy][wave_lane]
                uid = f"w{st.next_uid}"
                st.next_uid += 1
                st.waves[uid] = Wave(uid=uid, team=enemy, lane=wave_lane, chips=5, path_idx=idx,
                                     hexpos=path[idx], empowered=empowered)
                if empowered:
                    st.teams[enemy].baron_track = 10 ** 6
                st.touch()
                st.refresh_visibility(allow_flip_back=True, placer=None)
                before = snapshot(st)
                game_mod.world_phase(st)
                st.refresh_visibility(allow_flip_back=True, placer=None)
                out.append({"step": "world", "before": before, "after": snapshot(st),
                            "label": f"wave takes {team} {target}"
                                     + (" (empowered)" if empowered else "")})
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--games", type=int, default=8)
    ap.add_argument("--config", default=os.path.join(ROOT, "reports", "requests", "batch_0075.json"))
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--tiers", default="T1_greedy,T2_sieger",
                    help="AI tiers, cycled game by game")
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--synthetic-only", action="store_true",
                    help="keep the game scenarios already in --out and redo the synthetic ones")
    args = ap.parse_args(argv)
    with open(args.config) as fh:
        cfg = make_config(**json.load(fh).get("config_overrides", {}))
    board, kits = Board.load(), load_roster(ROSTER)
    make_policy = _policy_factory("1.5.0")
    scenarios = []

    real_upkeep, real_world = run_mod.upkeep, run_mod.world_phase

    def upkeep(st, game):
        before = snapshot(st)
        twin = copy.deepcopy(st)
        game_mod.upkeep(twin, _NoPlacer)
        scenarios.append({"step": "upkeep", "before": before, "after": snapshot(twin)})
        real_upkeep(st, game)

    def world(st):
        before = snapshot(st)
        twin = copy.deepcopy(st)
        game_mod.world_phase(twin)
        twin.refresh_visibility(allow_flip_back=True, placer=None)
        scenarios.append({"step": "world", "before": before, "after": snapshot(twin)})
        real_world(st)

    if args.synthetic_only and os.path.exists(args.out):
        with open(args.out) as fh:
            scenarios = [x for x in json.load(fh)["scenarios"] if "label" not in x]
        args.games = 0
    run_mod.upkeep, run_mod.world_phase = upkeep, world
    try:
        for i in range(args.games):
            rng = random.Random(args.seed + i)
            picks = sample_picks(kits, rng)
            first = "north" if i % 2 == 0 else "south"
            st = new_game(board, kits, picks, copy.deepcopy(cfg), first=first)
            tier = args.tiers.split(",")[i % len(args.tiers.split(","))]
            pols = {t: make_policy(tier, args.seed * 31 + i * 2 + k, 0.3, team=t)
                    for k, t in enumerate(("north", "south"))}
            res = run_mod.Game(st, pols, seed=i, strict=False).run()
            print(f"game {i} ({tier}): {res.rounds} rounds, winner {res.winner} ({res.end_reason}); "
                  f"{len(scenarios)} scenarios so far")
    finally:
        run_mod.upkeep, run_mod.world_phase = real_upkeep, real_world
    scenarios += synthetic(board, kits, cfg, args.seed)
    with open(args.out, "w") as fh:
        json.dump({"config": os.path.relpath(args.config, ROOT), "scenarios": scenarios}, fh)
    print(f"wrote {os.path.relpath(args.out, ROOT)}: {len(scenarios)} scenarios")
    return 0


if __name__ == "__main__":
    sys.exit(main())
