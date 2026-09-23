

def test_personalities_are_distinguishable_and_complete():
    """A mixed batch is only readable if each personality reports as itself."""
    from ai.policy_v1_3_0 import PERSONALITIES, PERSONALITY_POOL, TIERS, make
    from ai.policy_v1_1_0.evaluation import W
    assert len(PERSONALITIES) >= 4
    for name in PERSONALITIES:
        pol = make(f"T2_{name}", 1, team="north")
        assert pol.tier == f"T2_{name}"
        missing = set(W) - set(pol.weights)
        assert not missing, f"{name} is missing weights {missing}"
    assert set(PERSONALITY_POOL) <= set(TIERS)


def test_the_warder_buys_wards_and_spends_them():
    from ai.policy_v1_3_0 import make
    w, s = make("T2_warder", 1), make("T2_sieger", 1)
    assert w.card_buy_value("control_ward") > s.card_buy_value("control_ward")
    assert w.card_value("control_ward") < s.card_value("control_ward")


def test_flank_terms_read_the_board(state, board, game):
    """A hidden hexgroup holding enemies is a threat to stand beside; an empty
    one is worth watching (ai 1.3.0)."""
    from ai.policy_v1_1_0.evaluation import flank_read
    t = board.tile_index["Mid River"]
    hider = state.champs["s_dax"]
    watcher = state.champs["n_kestrel"]
    for c in state.champs.values():
        c.hexpos = state.board.fountain[c.team]
    hider.hexpos = (0, 0)
    watcher.hexpos = (0, -1)                 # on Mid River's edge
    state.touch()
    threat, watch = flank_read(state, "north")
    assert threat[watcher.uid] >= 1, "an enemy-held hexgroup next door is a threat"
    hider.hexpos = state.board.fountain["south"]
    state.touch()
    threat, watch = flank_read(state, "north")
    assert threat[watcher.uid] == 0 and watch[watcher.uid] >= 1
