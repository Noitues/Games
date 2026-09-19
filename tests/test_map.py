"""Rules 2: geometry, tiles, structures, camps, hidden-route distances."""
import itertools

from engine.hexmap import hex_distance


def test_127_hexes_radius_6(board):
    assert len(board.hexes) == 127
    for q, r in board.hexes:
        assert max(abs(q), abs(r), abs(-q - r)) <= 6
    assert len(set(board.hexes)) == 127


def test_27_tiles_sizes_and_width(board):
    assert board.n_tiles == 27
    assert sorted({len(t) for t in board.tile_hexes}) == [3, 4, 5, 7]
    for hexes in board.tile_hexes:
        assert len(hexes) <= 7
        for a, b in itertools.combinations(hexes, 2):
            assert hex_distance(a, b) <= 2


def test_every_hex_in_exactly_one_tile(board):
    assert len(board.tile_of) == 127


def test_layout_mirror_symmetry(board):
    """Rules 2.1: the tile layout is mirror-symmetric north-south and east-west."""
    hexes = set(board.hexes)
    for q, r in hexes:
        assert (q, -q - r) in hexes
        assert (-q, r + q) in hexes


def test_structure_positions(board):
    assert board.fountain["north"] == (0, -6)
    assert board.nexus["north"] == (0, -5)
    assert board.towers["north"] == {"mid_T2": (0, -4), "mid_T1": (0, -2), "bot_T2": (3, -6),
                                     "bot_T1": (6, -6), "top_T2": (-3, -3), "top_T1": (-6, 0)}
    for name, h in board.towers["north"].items():
        q, r = board.towers["south"][name]
        assert (q, r) == (-h[0], -h[1]), "south is the 180 degree rotation"


def test_monster_point_symmetry_and_pit_distance(board):
    assert board.monsters["dragon"] == [(3, -1)]
    assert board.monsters["baron"] == [(-3, 1)]
    assert hex_distance((3, -1), board.nexus["south"]) == 6
    assert hex_distance((3, -1), board.nexus["north"]) == 7
    assert hex_distance((-3, 1), board.nexus["north"]) == 6
    assert hex_distance((-3, 1), board.nexus["south"]) == 7
    for kind in ("blue_buff", "red_buff", "wolves", "raptors", "krugs"):
        a, b = board.monsters[kind]
        assert b == (-a[0], -a[1]), f"{kind} is not point-symmetric"


def _tile_steps(board, a, b):
    """Distance in tiles when every tile on the route is hidden."""
    mask = (1 << board.n_tiles) - 1
    na = board.node_of(a, mask)
    nb = board.node_of(b, mask)
    return board.distance(na, nb, mask)


def test_hidden_route_distances(board):
    """Rules 2.2 hidden-route table."""
    base_n = board.fountain["north"]
    assert _tile_steps(board, base_n, board.towers["north"]["top_T1"]) == 2
    assert _tile_steps(board, base_n, board.towers["north"]["bot_T1"]) == 2
    assert _tile_steps(board, base_n, (3, -1)) == 3          # Dragon Pit
    assert _tile_steps(board, base_n, (-3, 1)) == 3          # Baron Pit
    assert _tile_steps(board, base_n, (0, 0)) == 3           # Mid River
    assert _tile_steps(board, base_n, board.towers["south"]["top_T1"]) == 4
    assert _tile_steps(board, base_n, board.towers["south"]["bot_T1"]) == 4
    assert _tile_steps(board, base_n, board.fountain["south"]) == 6


def test_lane_paths_end_next_to_enemy_nexus(board):
    for team, foe in (("north", "south"), ("south", "north")):
        for lane, path in board.lane_paths[team].items():
            assert hex_distance(path[-1], board.nexus[foe]) == 1
            for a, b in zip(path, path[1:]):
                assert hex_distance(a, b) == 1
