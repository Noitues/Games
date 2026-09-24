"""A unit entering a hidden tile takes a hex of its own (batch_0045 anomalies)."""
from engine.config import make_config
from engine.game import new_game
from engine.resolve import move_unit
from engine.state import Wave
from tests.conftest import PICKS


def _wave(st, uid, team, hexpos, lane="mid"):
    w = Wave(uid=uid, team=team, lane=lane, chips=3, path_idx=0, hexpos=hexpos)
    st.waves[uid] = w
    st.touch()
    return w


def test_a_wave_pushed_into_its_base_does_not_land_on_the_tower(board, kits):
    st = new_game(board, kits, PICKS, make_config(), first="north")
    base = board.tile_of[board.fountain["north"]]
    assert st.hidden_mask >> base & 1                      # the base starts face down
    tower = next(s for s in st.structures.values() if s.uid == "n_mid_T2")
    w = _wave(st, "w_test", "north", board.spawn["north"]["mid"])
    move_unit(st, w, ("T", base), from_node=("H",) + tuple(w.hexpos))
    assert board.tile_of[w.hexpos] == base
    assert w.hexpos != tower.hexpos
    assert not any(x.uid != w.uid and x.alive and x.kind != "champion" and x.hexpos == w.hexpos
                   for x in st.all_units())


def test_two_waves_never_share_a_hex_inside_a_hidden_tile(board, kits):
    st = new_game(board, kits, PICKS, make_config(), first="north")
    base = board.tile_of[board.fountain["north"]]
    a = _wave(st, "w_a", "north", board.spawn["north"]["mid"])
    move_unit(st, a, ("T", base), from_node=("H",) + tuple(a.hexpos))
    b = _wave(st, "w_b", "north", board.spawn["north"]["mid"])
    move_unit(st, b, ("T", base), from_node=("H",) + tuple(b.hexpos))
    assert a.hexpos != b.hexpos


def test_a_full_tile_refuses_the_move(board, kits):
    st = new_game(board, kits, PICKS, make_config(), first="north")
    base = board.tile_of[board.fountain["north"]]
    hexes = list(board.tile_hexes[base])
    fixed = {s.hexpos for s in st.structures.values() if s.alive}
    n = 0
    for h in hexes:
        if h not in fixed:
            _wave(st, f"w_fill{n}", "north", h); n += 1
    late = _wave(st, "w_late", "north", board.spawn["north"]["mid"])
    before = late.hexpos
    move_unit(st, late, ("T", base), from_node=("H",) + tuple(before))
    assert late.hexpos == before
