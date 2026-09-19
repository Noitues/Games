"""Policy-side checks: legality, determinism and the tier contract."""
import importlib

import pytest

from engine.config import make_config
from engine.game import legal_activations, new_game
from engine.run import Game
from tests.conftest import PICKS

AI = importlib.import_module("ai.policy_v1_1_0")


@pytest.mark.parametrize("tier", sorted(AI.TIERS))
def test_every_tier_returns_a_legal_option(board, kits, tier):
    st = new_game(board, kits, PICKS, make_config(), first="north")
    st.teams["north"].ap = 5
    pol = AI.make(tier, 3, 0.3, team="north")
    legal = legal_activations(st, "north")
    for _ in range(5):
        act = pol.choose_activation(st, legal)
        assert act in legal


def test_t2_reads_the_published_snake_order(board, kits):
    st = new_game(board, kits, PICKS, make_config(), first="north")
    pol = AI.make("T2_search", 1, 0.0, team="north")
    st.turn_order = ["north", "south", "south", "north"]
    st.turn_index = 0
    assert pol._next_actor(st, 1) == "south"
    assert pol._next_actor(st, 2) == "south"
    st.turn_index = 3
    assert pol._next_actor(st, 1) == "south"        # falls back past the end


def test_t2_stays_inside_its_time_budget(board, kits):
    import time
    st = new_game(board, kits, PICKS, make_config(), first="north")
    st.teams["north"].ap = 6
    pol = AI.make("T2_search", 1, 0.3, {"time_budget_ms": 60}, team="north")
    legal = legal_activations(st, "north")
    t0 = time.perf_counter()
    pol.choose_activation(st, legal)
    # The root prefilter runs before the budget applies, so allow generous slack;
    # what matters is that the search does not run unbounded.
    assert (time.perf_counter() - t0) < 3.0


def test_exploit_profiles_differ_from_the_baseline(board, kits):
    from ai.policy_v1_1_0.evaluation import W
    for name, profile in AI.PROFILES.items():
        assert profile != W, name
        assert set(profile) == set(W), name


def test_assists_are_credited(board, kits):
    from engine.resolve import deal_hits
    st = new_game(board, kits, PICKS, make_config())
    st.round = 4
    helper, killer = st.champs["n_kestrel"], st.champs["n_ashwyn"]
    victim = st.champs["s_dax"]
    deal_hits(st, "north", victim, 2, "hit", helper)
    deal_hits(st, "north", victim, victim.hp, "hit", killer)
    assert not victim.alive
    assert killer.kills == 1 and helper.assists == 1 and killer.assists == 0


def test_t2_full_game_is_legal(board, kits):
    st = new_game(board, kits, PICKS, make_config(), first="north")
    pols = {t: AI.make("T2_search", 5 + i, 0.3, {"time_budget_ms": 40}, team=t)
            for i, t in enumerate(("north", "south"))}
    res = Game(st, pols, seed=5, strict=True).run()
    assert not [a for a in res.anomalies if a.startswith("ILLEGAL")]


def test_t2_never_mixes_searched_and_unsearched_scores(board, kits, monkeypatch):
    """Out of time means fewer candidates, never a greedy score competing with
    a searched one (they sit on different scales)."""
    st = new_game(board, kits, PICKS, make_config(), first="north")
    st.teams["north"].ap = 6
    pol = AI.make("T2_search", 2, 0.0, {"time_budget_ms": 0, "root_k": 5}, team="north")
    seen = []
    orig = pol._descend
    pol._descend = lambda *a, **k: (seen.append(1), orig(*a, **k))[1]
    legal = legal_activations(st, "north")
    act = pol.choose_activation(st, legal)
    assert act in legal
    # With a zero budget exactly one candidate plus the pass option is searched.
    assert len(seen) == 2
