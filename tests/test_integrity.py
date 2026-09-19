"""Engine integrity: full games run with every assertion on."""
import pytest

from ai.policy_v1_0_0 import make
from engine.config import make_config
from engine.game import new_game
from engine.run import Game
from tests.conftest import PICKS


@pytest.mark.parametrize("tier,seed", [("T0_random", 1), ("T0_random", 2), ("T1_greedy", 3)])
def test_full_game_has_no_illegal_state(board, kits, tier, seed):
    st = new_game(board, kits, PICKS, make_config(), first="north")
    pols = {t: make(tier, seed + i, 0.3, team=t) for i, t in enumerate(("north", "south"))}
    res = Game(st, pols, seed=seed, strict=True).run()
    assert res.rounds <= 20
    assert not [a for a in res.anomalies if a.startswith("ILLEGAL")]
    assert res.winner in ("north", "south", None)


def test_policies_are_deterministic_for_a_seed(board, kits):
    outs = []
    for _ in range(2):
        st = new_game(board, kits, PICKS, make_config(), first="north")
        pols = {t: make("T1_greedy", 7 + i, 0.3, team=t)
                for i, t in enumerate(("north", "south"))}
        r = Game(st, pols, seed=7, strict=True).run()
        outs.append((r.winner, r.rounds, r.end_reason))
    assert outs[0] == outs[1]


def test_champion_hp_never_exceeds_max(board, kits):
    st = new_game(board, kits, PICKS, make_config(), first="south")
    pols = {t: make("T1_greedy", 11 + i, 0.4, team=t)
            for i, t in enumerate(("north", "south"))}
    Game(st, pols, seed=11, strict=True).run()
    for c in st.champs.values():
        assert 0 <= c.hp <= c.max_hp
