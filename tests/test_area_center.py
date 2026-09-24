"""Rules 1.8.0: an AREA is a radius-1 disc around a chosen centre; Longbow moves
the centre, not the disc (RQ-045)."""
from engine.config import make_config
from engine.game import new_game
from engine.resolve import area_centers, area_targets, step_choices
from engine.state import Wave
from tests.conftest import PICKS


def _open(board, kits, **over):
    st = new_game(board, kits, PICKS, make_config(**over), first="north")
    st.hidden_mask = 0                       # everything face up: plain hex geometry
    st.touch()
    return st


def _wave(st, uid, team, hexpos):
    st.waves[uid] = Wave(uid=uid, team=team, lane="mid", chips=3, path_idx=0, hexpos=hexpos)
    st.touch()
    return st.waves[uid]


def _line(board, start, steps):
    """Walk `steps` hexes in one fixed direction from start."""
    from engine.hexmap import DIRS
    d = DIRS[0]
    out = []
    h = start
    for _ in range(steps):
        h = (h[0] + d[0], h[1] + d[1])
        out.append(h)
    return out


def test_area_reaches_two_hexes_but_the_disc_is_radius_one(board, kits):
    st = _open(board, kits)
    c = st.champs["n_ashwyn"]
    c.hexpos = (0, 0)
    for other in st.champs.values():
        if other.uid != c.uid:
            other.hexpos = (9, 9) if other.hexpos == (0, 0) else other.hexpos
    st.touch()
    a, b, far = _line(board, (0, 0), 3)      # 1, 2 and 3 hexes away in a line
    w1 = _wave(st, "w1", "south", a)
    w2 = _wave(st, "w2", "south", b)
    w3 = _wave(st, "w3", "south", far)
    step = kits["ashwyn"]["abilities"]["W"]["steps"][0]
    node = st.node_of_unit(c)
    centers = step_choices(st, c, node, step, None, "W", 50)
    assert centers, "an AREA with targets in reach must offer a centre"
    reach = set()
    for ctr in centers:
        reach |= {u.uid for u in area_targets(st, node, ctr, "north", "enemy_any")}
    assert {"w1", "w2"} <= reach and "w3" not in reach
    # no single centre hits both a unit 1 away and one 3 away: the disc is radius 1
    for ctr in centers:
        hit = {u.uid for u in area_targets(st, node, ctr, "north", "enemy_any")}
        assert not ({"w1", "w3"} <= hit)


def test_longbow_moves_the_centre_not_the_disc(board, kits):
    st = _open(board, kits)
    c = st.champs["n_ashwyn"]
    c.hexpos = (0, 0)
    c.items.add("longbow")
    st.touch()
    a, b, far = _line(board, (0, 0), 3)
    _wave(st, "w3", "south", far)
    step = kits["ashwyn"]["abilities"]["W"]["steps"][0]
    node = st.node_of_unit(c)
    assert len(area_centers(st, node, 2)) > len(area_centers(st, node, 1))
    centers = step_choices(st, c, node, step, None, "W", 50)
    reach = set()
    for ctr in centers:
        reach |= {u.uid for u in area_targets(st, node, ctr, "north", "enemy_any")}
    assert "w3" in reach                        # centre 2 away, disc 1: reach 3
    for ctr in centers:                         # but never more than 7 hexes at once
        assert len(st.board.nodes_within(ctr, 1, st.hidden_mask)) <= 7


def test_old_blast_at_the_feet_is_still_reachable(board, kits):
    st = _open(board, kits, area_center=False)
    c = st.champs["n_ashwyn"]
    c.hexpos = (0, 0)
    st.touch()
    a, b, far = _line(board, (0, 0), 3)
    _wave(st, "w2", "south", b)
    step = kits["ashwyn"]["abilities"]["W"]["steps"][0]
    node = st.node_of_unit(c)
    assert step_choices(st, c, node, step, None, "W", 50) == []      # 2 away, range 1: nothing
    c.items.add("longbow")
    assert step_choices(st, c, node, step, None, "W", 50) == [None]  # radius 2 disc
