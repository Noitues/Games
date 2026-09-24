"""Respawn never stacks (batch_0045 game 332): fountain, then base, then the
Rules 3.4 overflow ring, else wait a round."""
from engine.abilities import respawn
from engine.config import make_config
from engine.game import new_game, upkeep
from engine.state import Wave
from tests.conftest import PICKS


def _fill(st, board, hexes, prefix):
    for n, h in enumerate(hexes):
        st.waves[f"{prefix}{n}"] = Wave(uid=f"{prefix}{n}", team="north", lane="mid", chips=3,
                                        path_idx=0, hexpos=h)
    st.touch()


def _reveal_base(st, board):
    base = board.tile_of[board.fountain["north"]]
    st.hidden_mask &= ~(1 << base)
    st.touch()
    return base


def test_respawn_overflows_to_the_ring_when_the_base_is_full(board, kits):
    st = new_game(board, kits, PICKS, make_config(), first="north")
    base = _reveal_base(st, board)
    fixed = {s.hexpos for s in st.structures.values() if s.alive}
    champs = [c for c in st.champs.values() if c.team == "north"]
    victim, others = champs[0], champs[1:]
    free = [h for h in board.tile_hexes[base] if h not in fixed]
    for c, h in zip(others, free):          # four champions take four base hexes
        c.hexpos = h
    _fill(st, board, free[len(others):], "wfill")
    victim.alive = False
    victim.track = 0
    assert respawn(st, victim) is True
    assert board.tile_of[victim.hexpos] != base
    assert any(victim.hexpos in board.neighbors[h] for h in board.tile_hexes[base])
    assert not any(u.uid != victim.uid and u.alive and u.hexpos == victim.hexpos
                   for u in st.all_units())


def test_respawn_waits_when_base_and_ring_are_full(board, kits, monkeypatch):
    st = new_game(board, kits, PICKS, make_config(), first="north")
    base = _reveal_base(st, board)
    fixed = {s.hexpos for s in st.structures.values() if s.alive}
    champs = [c for c in st.champs.values() if c.team == "north"]
    victim, others = champs[0], champs[1:]
    free = [h for h in board.tile_hexes[base] if h not in fixed]
    for c, h in zip(others, free):
        c.hexpos = h
    _fill(st, board, free[len(others):], "wbase")
    ring = {nb for h in board.tile_hexes[base] for nb in board.neighbors[h]
            if board.tile_of.get(nb) != base}
    _fill(st, board, sorted(ring), "wring")
    victim.alive = False
    victim.track = 0
    assert respawn(st, victim) is False and not victim.alive
    # a hex frees up; the next Upkeep brings the champion back without stacking
    st.waves["wring0"].alive = False
    st.touch()

    class _G:                                  # upkeep only needs a placer
        def placer(self, *a, **k):
            return {}
    upkeep(st, _G())
    assert victim.alive
    assert not any(u.uid != victim.uid and u.alive and u.hexpos == victim.hexpos
                   for u in st.all_units())
