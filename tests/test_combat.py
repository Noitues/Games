"""Rules 5.3, 6.4, 7, 8: hits, chips as AP, death, towers, protection order."""
import pytest

from engine.abilities import apply_plan
from engine.game import world_phase
from engine.resolve import deal_hits, death_track_pos, structure_targetable


def test_chip_removed_by_a_champion_becomes_ap(state):
    c = state.champs["n_kestrel"]
    tower = state.structures["s_mid_T1"]
    full = tower.chips
    state.teams["north"].ap = 0
    got = deal_hits(state, "north", tower, 3, "chips_structure", c)
    assert got == 3
    assert state.teams["north"].ap == 3
    assert c.ap_earned == 3
    assert tower.chips == full - 3


def test_world_phase_chips_go_to_the_supply(state):
    tower = state.structures["s_mid_T1"]
    full = tower.chips
    state.teams["north"].ap = 0
    deal_hits(state, "north", tower, 2, "world", None)
    assert state.teams["north"].ap == 0
    assert tower.chips == full - 2


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


def test_tower_in_a_hidden_tile_reaches_only_its_own_hex(state, board):
    """RQ-002: a hidden tile is a movement shortcut, not an effect shortcut."""
    from engine.state import Wave
    t = board.tile_index["Mid Lane S Outer"]         # holds the south mid T1 at (0,2)
    assert state.hidden_mask >> t & 1
    state.waves["wa"] = Wave(uid="wa", team="north", lane="mid", chips=3, path_idx=0,
                             hexpos=(0, 0))
    state.touch()
    world_phase(state)
    assert state.waves["wa"].chips == 3, "(0,0) is two hexes from the tower"
    state.waves["wa"].hexpos = (0, 1)                # now hex-adjacent to (0,2)
    state.touch()
    world_phase(state)
    assert state.waves["wa"].chips == 2


def _clear_the_edges(state, board, tile, keep=(), reserved=()):
    """Park every champion that is not part of the test well away from ``tile``.

    Under RQ-036 any adjacent enemy reveals an occupied hexgroup, so a test
    about concealment has to control who is standing on the edge.
    """
    ring = {n for h in board.tile_hexes[tile] for n in board.neighbors.get(h, ())}
    ring |= set(board.tile_hexes[tile]) | set(reserved)
    spare = [h for h in board.hexes if h not in ring]
    i = 0
    for c in state.champs.values():
        if c.uid in keep:
            continue
        c.hexpos = spare[i]
        i += 1
    state.touch()


def test_champion_in_a_hidden_tile_cannot_be_targeted_from_outside(state, board):
    """RQ-001: the tile is a refuge."""
    from engine.resolve import units_within
    t = board.tile_index["Mid River"]
    hider, shooter = state.champs["n_ashwyn"], state.champs["s_dax"]
    _clear_the_edges(state, board, t, keep=(hider.uid, shooter.uid),
                     reserved=((0, 0), (3, -2)))
    # The shooter has to stand off the edge: under RQ-036 an adjacent enemy
    # reveals an occupied hexgroup, and a revealed champion is targetable.
    hider.hexpos, shooter.hexpos = (0, 0), (3, -2)
    state.touch()
    state.refresh_visibility()
    assert state.hidden_mask >> t & 1
    assert state.hidden_mask >> t & 1, "nobody is standing on the edge"
    seen = [u.uid for u, _ in units_within(state, state.node_of_unit(shooter), 4,
                                           "south", "enemy_champion", shooter.hexpos)]
    assert hider.uid not in seen
    # Only champions are concealed: north's mid T1, also inside a hidden tile,
    # is still a legal target at plain hex range.
    seen_any = [u.uid for u, _ in units_within(state, state.node_of_unit(shooter), 4,
                                               "south", "enemy_any", shooter.hexpos)]
    assert "n_mid_T1" in seen_any


def test_concealment_is_one_way(state, board):
    """As ruled, a champion may still act out of a hidden tile. The risk that
    this creates is RQ-032, open with the lead designer."""
    from engine.resolve import units_within
    hider = state.champs["n_ashwyn"]
    hider.hexpos = (0, 0)
    state.touch()
    state.refresh_visibility()
    assert state.hidden_mask >> board.tile_of[hider.hexpos] & 1
    seen = [u.uid for u, _ in units_within(state, state.node_of_unit(hider), 3,
                                           "north", "enemy_any", hider.hexpos)]
    assert "s_mid_T1" in seen, "a concealed champion can still act outward"


def test_a_camp_still_hits_a_champion_sharing_its_hidden_tile(state, board):
    m = state.monsters["dragon_0"]
    m.alive, m.chips = True, 8
    c = state.champs["n_thornjaw"]
    c.hexpos = (2, -1)                                # inside the Dragon Pit tile
    state.touch()
    state.refresh_visibility()
    assert state.hidden_mask >> board.tile_of[c.hexpos] & 1
    world_phase(state)
    assert c.hp == c.max_hp - 1


def test_waves_in_hidden_tiles_still_trade(state, board):
    """The refuge must not stall lanes: fixed-hex units fight by hex."""
    from engine.state import Wave
    state.waves["wa"] = Wave(uid="wa", team="north", lane="mid", chips=3, path_idx=0,
                             hexpos=(0, 0))
    state.waves["wb"] = Wave(uid="wb", team="south", lane="mid", chips=3, path_idx=0,
                             hexpos=(0, 1))
    state.touch()
    state.refresh_visibility()
    world_phase(state)
    assert state.waves["wa"].chips == 2 and state.waves["wb"].chips == 2


def test_line_catches_by_hex_and_skips_concealed_champions(state, board):
    from engine.resolve import line_targets
    t = board.tile_index["Mid River"]
    shooter = state.champs["n_kestrel"]
    exposed = state.champs["s_dax"]
    _clear_the_edges(state, board, t, keep=(shooter.uid, exposed.uid),
                     reserved=((0, -2), (0, 0), (1, 0)))
    shooter.hexpos = (0, -2)                          # off Mid River's edge (RQ-036)
    exposed.hexpos = (0, 0)                           # shares Mid River with nobody else
    state.touch()
    state.refresh_visibility()
    src_tile = board.tile_of[shooter.hexpos]
    caught = line_targets(state, shooter.hexpos, (0, 1), 6, "north", "enemy_any", src_tile)
    assert exposed.uid not in [u.uid for u in caught], "concealed in its own hidden tile"
    state.champs["n_ashwyn"].hexpos = (1, 0)          # north enters Mid River: it flips
    state.touch()
    state.refresh_visibility()
    assert not state.hidden_mask >> t & 1
    # A flip hands out real hexes to everyone in the revealed hexgroup, and
    # under RQ-036 the shooter's own hexgroup can be revealed too, so put both
    # ends of the line back where the test wants them.
    shooter.hexpos = (0, -2)
    exposed.hexpos = (0, 0)
    state.touch()
    caught = line_targets(state, shooter.hexpos, (0, 1), 6, "north", "enemy_any", src_tile)
    assert exposed.uid in [u.uid for u in caught]
