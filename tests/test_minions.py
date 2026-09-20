"""Rules 9 and 11: waves, lane movement, spawns, Baron empowerment."""
from engine.game import move_waves, spawn_waves, upkeep
from engine.state import Wave


def test_waves_spawn_on_odd_rounds_with_three_chips(state, game):
    state.round = 1
    spawn_waves(state)
    assert len(state.waves) == 6
    assert all(w.chips == 3 for w in state.waves.values())
    lanes = {(w.team, w.lane) for w in state.waves.values()}
    assert len(lanes) == 6


def test_wave_size_grows_from_round_seven(state):
    state.round = 7
    spawn_waves(state)
    assert all(w.chips == 4 for w in state.waves.values())


def test_waves_move_two_hexes_along_the_lane(state, board):
    state.round = 1
    spawn_waves(state)
    w = next(w for w in state.waves.values() if w.team == "north" and w.lane == "mid")
    assert w.hexpos == board.spawn["north"]["mid"]
    move_waves(state, "north")
    assert w.path_idx == 2
    assert w.hexpos == board.lane_paths["north"]["mid"][2]


def test_wave_passes_through_its_own_tower_but_cannot_stop_on_it(state, board):
    """Rules 4.3 / 9.2."""
    path = board.lane_paths["north"]["mid"]
    idx = path.index((0, -2))               # north mid T1 sits here
    state.waves["w"] = Wave(uid="w", team="north", lane="mid", chips=3,
                            path_idx=idx - 1, hexpos=path[idx - 1])
    state.touch()
    move_waves(state, "north")
    assert state.waves["w"].hexpos == path[idx + 1]


def test_enemy_unit_stops_a_wave(state, board):
    path = board.lane_paths["north"]["mid"]
    state.hidden_mask = 0
    state.waves["w"] = Wave(uid="w", team="north", lane="mid", chips=3, path_idx=1, hexpos=path[1])
    state.champs["s_dax"].hexpos = path[2]
    state.touch()
    move_waves(state, "north")
    assert state.waves["w"].path_idx == 1


def test_spawn_merges_into_a_friendly_wave(state, board):
    state.round = 1
    h = board.spawn["north"]["mid"]
    state.waves["w"] = Wave(uid="w", team="north", lane="mid", chips=3, path_idx=0, hexpos=h)
    state.touch()
    spawn_waves(state)
    assert state.waves["w"].chips == 6


def test_spawn_is_skipped_when_an_enemy_holds_the_hex(state, board):
    state.round = 1
    state.hidden_mask = 0
    h = board.spawn["north"]["mid"]
    state.champs["s_dax"].hexpos = h
    state.touch()
    spawn_waves(state)
    assert not any(w.team == "north" and w.lane == "mid" for w in state.waves.values())


def test_baron_empowers_waves(state, board):
    state.round = 7
    state.teams["north"].baron_track = 3
    spawn_waves(state)
    north = [w for w in state.waves.values() if w.team == "north"]
    south = [w for w in state.waves.values() if w.team == "south"]
    assert all(w.chips == 6 and w.empowered for w in north)
    assert all(w.chips == 4 and not w.empowered for w in south)


def test_empowered_waves_deal_two_hits_to_structures(state, board):
    from engine.game import world_phase
    state.hidden_mask = 0
    tower = state.structures["s_mid_T1"]
    full = tower.chips
    state.waves["w"] = Wave(uid="w", team="north", lane="mid", chips=3, path_idx=0,
                            hexpos=(0, 1), empowered=True)
    state.touch()
    world_phase(state)
    assert tower.chips == full - 2


def test_spawn_is_skipped_when_a_friendly_champion_holds_the_hex(state, board):
    """RQ-027: only a friendly wave may share the spawn hex, by merging."""
    state.round = 1
    state.hidden_mask = 0
    h = board.spawn["north"]["mid"]
    state.champs["n_kestrel"].hexpos = h
    state.touch()
    spawn_waves(state)
    assert not any(w.team == "north" and w.lane == "mid" for w in state.waves.values())


def test_monster_waits_for_a_clear_hex(state, game):
    """RQ-018."""
    m = state.monsters["wolves_0"]
    m.alive, m.chips, m.respawn_round = False, 0, 1
    state.champs["n_thornjaw"].hexpos = m.hexpos
    state.touch()
    upkeep(state, game)
    assert not m.alive
    state.champs["n_thornjaw"].hexpos = state.board.fountain["north"]
    state.touch()
    upkeep(state, game)
    assert m.alive and m.chips == m.max_chips
