"""ai 1.4.0: a state machine over the personalities (Handoff §9)."""
import importlib

import pytest

from engine.config import make_config
from engine.game import new_game
from engine.run import Game
from tests.conftest import PICKS

AI = importlib.import_module("ai.policy_v1_4_0")
OLD = importlib.import_module("ai.policy_v1_3_0")
MACHINES = sorted(k for k in AI.TIERS if k.startswith("SM_"))


def test_1_3_0_is_untouched():
    assert not [k for k in OLD.TIERS if k.startswith("SM_")]
    assert set(OLD.TIERS) <= set(AI.TIERS)


def test_signals_cover_the_listed_names(state):
    sig = AI.signals(state, "north")
    assert set(sig) == set(AI.SIGNALS)
    assert sig["round"] == 0 and sig["tower_diff"] == 0 and sig["alive_own"] == 5


def test_rules_fire_in_order_and_default_otherwise():
    spec = {"name": "SM_t", "default": "laner", "commit": 0,
            "rules": [{"if": [["tower_diff", ">=", 1]], "then": "sieger"},
                      {"if": [["tower_diff", "<=", -1]], "then": "warder"}]}
    AI.validate_machine(spec)
    base = {k: 0 for k in AI.SIGNALS}
    assert AI.next_state(spec, dict(base, tower_diff=2), "laner", -1, 5) == "sieger"
    assert AI.next_state(spec, dict(base, tower_diff=-1), "laner", -1, 5) == "warder"
    assert AI.next_state(spec, base, "sieger", -1, 5) == "laner"


def test_commit_holds_a_state():
    spec = {"name": "SM_t", "default": "laner", "commit": 3,
            "rules": [{"if": [["tower_diff", ">=", 1]], "then": "sieger"}]}
    base = {k: 0 for k in AI.SIGNALS}
    # entered sieger at round 4 with commit 3: locked through round 6, free at 7
    assert AI.next_state(spec, base, "sieger", 7, 6) == "sieger"
    assert AI.next_state(spec, base, "sieger", 7, 7) == "laner"


@pytest.mark.parametrize("bad", [
    {"name": "g1_x", "default": "laner"},                                  # no SM_ prefix
    {"name": "SM_x", "default": "ganker"},                                 # unknown state
    {"name": "SM_x", "default": "laner", "rules": [{"if": [["towers", ">", 1]], "then": "sieger"}]},
    {"name": "SM_x", "default": "laner", "rules": [{"if": [["round", "~", 1]], "then": "sieger"}]},
])
def test_a_bad_machine_fails_at_load(bad):
    with pytest.raises(ValueError):
        AI.validate_machine(bad)


def _play(board, kits, tier, rounds, seed=11):
    st = new_game(board, kits, PICKS, make_config(round_limit=rounds), first="north")
    pols = {t: AI.make(tier if t == "north" else "T2_search", seed + i, 0.3,
                       {"time_budget_ms": 40}, team=t) for i, t in enumerate(("north", "south"))}
    res = Game(st, pols, seed=seed, strict=True).run()
    return res, pols["north"]


@pytest.mark.parametrize("tier", MACHINES)
def test_every_machine_plays_a_legal_game_and_logs_its_states(board, kits, tier):
    res, pol = _play(board, kits, tier, rounds=4)
    assert not [a for a in res.anomalies if a.startswith("ILLEGAL")]
    rounds = [r for r, _ in pol.occupancy]
    assert rounds == sorted(set(rounds)) and len(rounds) >= 3     # once per round, no repeats
    assert {s for _, s in pol.occupancy} <= set(AI.PERSONALITIES)


def test_the_clock_machine_switches_on_the_round(board, kits):
    _, pol = _play(board, kits, "SM_g1_clock3", rounds=10)
    by_round = dict(pol.occupancy)
    assert by_round[2] == "laner" and by_round[6] == "objective" and by_round[9] == "sieger"


def test_switching_swaps_the_whole_profile(board, kits):
    st = new_game(board, kits, PICKS, make_config(), first="north")
    pol = AI.make("SM_g1_clock2", 1, 0.3, {"time_budget_ms": 40}, team="north")
    assert pol.weights == AI.PERSONALITIES["laner"]
    st.round = 4
    pol._tick(st)
    assert pol.state_name == "sieger" and pol.weights == AI.PERSONALITIES["sieger"]
    assert pol.leaf_weights["kill_chance"] == 0.0 and pol.leaf_weights["struct_focus"] == \
        AI.PERSONALITIES["sieger"]["struct_focus"]
