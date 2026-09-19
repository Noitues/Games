"""Rules 5.3, 6.4, 7, 8: hits, chips as AP, death, towers, protection order."""
import pytest

from engine.abilities import apply_plan
from engine.game import world_phase
from engine.resolve import deal_hits, death_track_pos, structure_targetable


def test_chip_removed_by_a_champion_becomes_ap(state):
    c = state.champs["n_kestrel"]
    tower = state.structures["s_mid_T1"]
    state.teams["north"].ap = 0
    got = deal_hits(state, "north", tower, 3, "chips_structure", c)
    assert got == 3
    assert state.teams["north"].ap == 3
    assert c.ap_earned == 3
    assert tower.chips == 5


def test_world_phase_chips_go_to_the_supply(state):
    tower = state.structures["s_mid_T1"]
    state.teams["north"].ap = 0
    deal_hits(state, "north", tower, 2, "world", None)
    assert state.teams["north"].ap == 0
    assert tower.chips == 6


def test_hitting_a_champion_gains_no_ap_but_a_kill_gives_one(state):
    a = state.champs["n_kestrel"]
    v = state.champs["s_dax"]
    state.teams["north"].ap = 0
    deal_hits(state, "north", v, 3, "hit", a)
    assert state.teams["north"].ap == 0
    assert v.hp == v.max_hp - 3
    deal_hits(state, "north", v, v.hp, "hit", a)
    assert not v.alive
    assert state.teams["north"].ap == 1
    assert a.kills == 1 and v.deaths == 1


def test_death_timer_bands(state):
    assert death_track_pos(1) == 2 and death_track_pos(4) == 2
    assert death_track_pos(5) == 3 and death_track_pos(8) == 3
    assert death_track_pos(9) == 4 and death_track_pos(17) == 4


def test_shield_absorbs_hits_then_expires(state):
    c = state.champs["n_bastion"]
    state.round = 3
    c.shield, c.shield_until = 4, 4
    deal_hits(state, "south", c, 3, "hit", state.champs["s_dax"])
    assert c.hp == c.max_hp and c.shield == 1
    state.round = 5
    deal_hits(state, "south", c, 2, "hit", state.champs["s_dax"])
    assert c.hp == c.max_hp - 2


def test_tower_damage_and_cloth_armor(state, board):
    """Rules 5.3: 2 hits to a champion, 1 chip from a wave; Cloth Armor -1."""
    t = board.tile_index["Mid Lane S Outer"]
    state.hidden_mask &= ~(1 << t)
    c = state.champs["n_ashwyn"]
    c.hexpos = (0, 1)                     # next to the south mid T1 at (0,2)
    state.touch()
    world_phase(state)
    assert c.hp == c.max_hp - 2
    c.hp = c.max_hp
    c.items.add("cloth_armor")
    world_phase(state)
    assert c.hp == c.max_hp - 1


def test_monsters_hit_both_teams(state, board):
    t = board.tile_index["Dragon Pit"]
    state.hidden_mask &= ~(1 << t)
    m = state.monsters["dragon_0"]
    m.alive, m.chips = True, 8
    n, s = state.champs["n_kestrel"], state.champs["s_dax"]
    n.hexpos, s.hexpos = (2, -1), (3, -2)
    state.touch()
    world_phase(state)
    assert n.hp == n.max_hp - 1 and s.hp == s.max_hp - 1


def test_protection_order(state):
    t1 = state.structures["s_mid_T1"]
    t2 = state.structures["s_mid_T2"]
    nexus = state.structures["s_nexus"]
    assert structure_targetable(state, t1)
    assert not structure_targetable(state, t2)
    assert not structure_targetable(state, nexus)
    t1.alive = False
    assert structure_targetable(state, t2)
    assert not structure_targetable(state, nexus)
    t2.alive = False
    assert structure_targetable(state, nexus)


def test_nexus_kill_sets_the_winner(state):
    for s in state.structures.values():
        if s.team == "south" and s.stype == "tower" and s.lane == "mid":
            s.alive = False
    nexus = state.structures["s_nexus"]
    deal_hits(state, "north", nexus, 12, "chips_structure", state.champs["n_kestrel"])
    assert state.winner == "north"


def test_simultaneous_world_damage(state, board):
    """Rules 5.3: two opposing waves lose chips at the same rate."""
    from engine.state import Wave
    state.hidden_mask = 0                      # every tile face up: no tile-range reach
    state.waves["wa"] = Wave(uid="wa", team="north", lane="mid", chips=3, path_idx=0, hexpos=(0, 0))
    state.waves["wb"] = Wave(uid="wb", team="south", lane="mid", chips=3, path_idx=0, hexpos=(-1, 1))
    state.touch()
    world_phase(state)
    assert state.waves["wa"].chips == 2 and state.waves["wb"].chips == 2


def test_hidden_tile_extends_a_towers_reach(state, board):
    """RULE-Q 004 ruling: a hidden tile is one space (Rules 3.1), so a tower
    inside one reaches every hex bordering the tile."""
    from engine.state import Wave
    t = board.tile_index["Mid Lane S Outer"]         # holds the south mid T1
    assert state.hidden_mask >> t & 1
    state.waves["wa"] = Wave(uid="wa", team="north", lane="mid", chips=3, path_idx=0, hexpos=(0, 0))
    state.touch()
    world_phase(state)
    assert state.waves["wa"].chips == 2
    state.hidden_mask &= ~(1 << t)                   # face up: (0,2) is 2 hexes away
    state.touch()
    world_phase(state)
    assert state.waves["wa"].chips == 2
