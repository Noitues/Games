"""RQ-049 phase rules: towers unlock by tier and round, the Nexus needs the
Baron (or the clock), the last hit on a wave pays a bonus, and every game
carries a per-round trace. All off by default."""
from engine.config import make_config
from engine.game import new_game
from engine.resolve import can_be_hit, deal_hits
from engine.state import Wave
from tests.conftest import PICKS

PHASE = {"tower_unlock_round": {"1": 5, "2": 9}, "nexus_needs_baron": True,
         "nexus_unlock_round": 16, "last_hit_ap": 1}


def _st(board, kits, **over):
    return new_game(board, kits, PICKS, make_config(**over), first="north")


def test_defaults_leave_structures_open(board, kits):
    st = _st(board, kits)
    st.round = 1
    assert can_be_hit(st, st.structures["s_mid_T1"], "north", "enemy_any")


def test_towers_unlock_by_tier_and_round(board, kits):
    st = _st(board, kits, **PHASE)
    t1, t2 = st.structures["s_mid_T1"], st.structures["s_mid_T2"]
    st.round = 4
    assert not can_be_hit(st, t1, "north", "enemy_any")
    st.round = 5
    assert can_be_hit(st, t1, "north", "enemy_any")
    t1.alive = False
    st.round = 8
    assert not can_be_hit(st, t2, "north", "enemy_any")
    st.round = 9
    assert can_be_hit(st, t2, "north", "enemy_any")


def test_nexus_needs_baron_or_the_clock(board, kits):
    st = _st(board, kits, **PHASE)
    for s in st.structures.values():
        if s.team == "south" and s.stype == "tower" and s.lane == "mid":
            s.alive = False
    nexus = st.structures["s_nexus"]
    st.round = 12
    assert not can_be_hit(st, nexus, "north", "enemy_any")
    st.teams["north"].baron_track = 10 ** 6
    assert can_be_hit(st, nexus, "north", "enemy_any")
    st.teams["north"].baron_track = 0
    st.round = 16
    assert can_be_hit(st, nexus, "north", "enemy_any")


def test_last_hit_on_a_wave_pays_a_bonus(board, kits):
    st = _st(board, kits, **PHASE)
    w = Wave(uid="w_t", team="south", lane="mid", chips=3, path_idx=0, hexpos=(0, 0))
    st.waves["w_t"] = w
    st.touch()
    c = st.champs["n_ashwyn"]
    st.teams["north"].ap = 0
    deal_hits(st, "north", w, 2, "chips_wave", c)
    assert st.teams["north"].ap == 2
    deal_hits(st, "north", w, 1, "chips_wave", c)
    assert st.teams["north"].ap == 4 and st.teams["north"].ap_by_source["last_hit"] == 1
    # a wave's own world-phase kill (no champion) pays nothing
    w2 = Wave(uid="w_u", team="south", lane="mid", chips=1, path_idx=0, hexpos=(0, 1))
    st.waves["w_u"] = w2
    deal_hits(st, "north", w2, 1, "world", None)
    assert st.teams["north"].ap == 4


def test_every_game_carries_a_round_trace(board, kits):
    import importlib
    from engine.run import Game
    AI = importlib.import_module("ai.policy_v1_5_0")
    st = new_game(board, kits, PICKS, make_config(round_limit=3, **PHASE), first="north")
    pols = {t: AI.make("SM_g3_phase" if t == "north" else "T2_sieger", 3 + i, 0.3,
                       {"time_budget_ms": 30}, team=t) for i, t in enumerate(("north", "south"))}
    res = Game(st, pols, seed=3, strict=True).run()
    assert [e["r"] for e in res.trace] == [1, 2, 3]
    assert set(res.trace[-1]) >= {"ap", "kills", "towers_lost", "dragons", "baron"}
    assert res.towers_down == {"north": 0, "south": 0}      # nothing unlocks before round 5
