"""RQ-049: structures start high and decay a step a round; a champion kill
is worth a number of the current minion waves; the last hit on a wave pays a
bonus; every game carries a per-round trace. All off by default."""
from engine.config import make_config
from engine.game import decay_structures, new_game, wave_size
from engine.resolve import deal_hits, kill_champion, kill_reward
from engine.state import Wave
from tests.conftest import PICKS

DECAY = {"tower_hp": 10, "nexus_hp": 16, "structure_decay": 1, "kill_ap_waves": 1.5,
         "last_hit_ap": 1}


def _st(board, kits, **over):
    return new_game(board, kits, PICKS, make_config(**over), first="north")


def test_defaults_do_not_decay(board, kits):
    st = _st(board, kits)
    before = {k: s.chips for k, s in st.structures.items()}
    st.round = 5
    decay_structures(st)
    assert {k: s.chips for k, s in st.structures.items()} == before


def test_structures_lose_a_step_a_round_down_to_the_floor(board, kits):
    st = _st(board, kits, **DECAY)
    t, nx = st.structures["s_mid_T1"], st.structures["s_nexus"]
    st.round = 1
    decay_structures(st)
    assert (t.chips, nx.chips) == (10, 16)          # round 1 is untouched
    for r in range(2, 12):
        st.round = r
        decay_structures(st)
    assert (t.chips, nx.chips) == (1, 6)            # ten steps, tower held at the floor
    assert t.alive                                  # decay alone never destroys
    t.chips = 3                                     # damage and decay add up
    st.round = 12
    decay_structures(st)
    assert t.chips == 2


def test_decay_every_other_round_with_type_floors(board, kits):
    st = _st(board, kits, **dict(DECAY, structure_decay_every=2,
                                 tower_decay_floor=4, nexus_decay_floor=8))
    t, nx = st.structures["s_mid_T1"], st.structures["s_nexus"]
    seen = []
    for r in range(1, 16):
        st.round = r
        decay_structures(st)
        seen.append(t.chips)
    # rounds 3, 5, 7, ... take a step; the tower stops at its floor of 4
    assert seen[:8] == [10, 10, 9, 9, 8, 8, 7, 7]
    assert t.chips == 4 and nx.chips == 9          # nexus: 16 - 7 steps
    st.round = 17
    decay_structures(st)
    assert nx.chips == 8
    st.round = 19
    decay_structures(st)
    assert nx.chips == 8                           # held at its floor


def test_kill_is_worth_waves(board, kits):
    st = _st(board, kits, **DECAY)
    st.round = 1
    assert wave_size(st) == 3 and kill_reward(st) == 5     # 1.5 x 3 = 4.5 -> 5
    st.round = 7
    assert kill_reward(st) == 6                            # 1.5 x 4
    st.round = 13
    assert kill_reward(st) == 8                            # 1.5 x 5 = 7.5 -> 8
    st2 = _st(board, kits, kill_ap=3)
    assert kill_reward(st2) == 3                           # off: the flat value
    st.teams["north"].ap = 0
    st.round = 7
    kill_champion(st, st.champs["s_" + PICKS["south"][0]] if "s_" + PICKS["south"][0] in st.champs
                  else next(c for c in st.champs.values() if c.team == "south"), "north", None)
    assert st.teams["north"].ap_by_source["champion_kill"] == 6


def test_last_hit_on_a_wave_pays_a_bonus(board, kits):
    st = _st(board, kits, **DECAY)
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
    st = new_game(board, kits, PICKS, make_config(round_limit=3, **DECAY), first="north")
    pols = {t: AI.make("SM_g3_phase" if t == "north" else "T2_sieger", 3 + i, 0.3,
                       {"time_budget_ms": 30}, team=t) for i, t in enumerate(("north", "south"))}
    res = Game(st, pols, seed=3, strict=True).run()
    assert [e["r"] for e in res.trace] == [1, 2, 3]
    assert set(res.trace[-1]) >= {"ap", "kills", "towers_lost", "dragons", "baron"}
