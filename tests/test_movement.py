"""Rules 3.1, 4.1-4.3: hidden tiles, distance, stacking, blocking, recall."""
from engine.game import champion_speed, legal_activations, new_game
from engine.hexmap import Board
from engine.resolve import reachable
from engine.state import other


def hide_all(state):
    state.hidden_mask = (1 << state.board.n_tiles) - 1
    state.touch()


def test_hidden_tile_is_one_space_for_range(state, board):
    """Rules 3.1/4.1: a unit inside a hidden tile is at range 1 from every
    bordering hex."""
    mask = state.hidden_mask
    t = board.tile_index["Mid River"]
    assert mask >> t & 1
    node = ("T", t)
    within1 = board.nodes_within(node, 1, mask)
    border = set()
    for h in board.tile_hexes[t]:
        for nb in board.neighbors[h]:
            if board.tile_of[nb] != t:
                border.add(board.node_of(nb, mask))
    assert border <= set(within1)


def test_enter_and_leave_cost_one(state, board):
    c = state.champs["n_ashwyn"]
    c.hexpos = (0, 0)
    state.touch()
    start = state.node_of_unit(c)
    assert start[0] == "T"                       # Mid River is hidden
    one_step = reachable(state, c, start, 1)
    tiles = {n[1] for n in one_step if n[0] == "T"}
    assert len(tiles) >= 3, "leaving a hidden tile costs 1 for any adjacent space"


def test_visible_hex_holds_one_unit(state, board):
    c = state.champs["n_ashwyn"]
    d = state.champs["n_kestrel"]
    t = board.tile_index["Mid River"]
    state.hidden_mask &= ~(1 << t)
    c.hexpos, d.hexpos = (0, 0), (1, 0)
    state.touch()
    assert not state.can_stop(("H", 1, 0), "north")
    assert state.can_stop(("H", -1, 0), "north")


def test_hidden_tile_holds_many_units_of_one_team(state, board):
    t = board.tile_index["Mid River"]
    for uid in ("n_ashwyn", "n_kestrel", "n_lumen"):
        state.champs[uid].hexpos = (0, 0)
    state.touch()
    assert state.can_stop(("T", t), "north")
    assert not state.can_stop(("T", t), "south")


def test_enemy_blocks_and_friendly_is_pass_through(state, board):
    t = board.tile_index["Mid River"]
    state.hidden_mask &= ~(1 << t)
    a = state.champs["n_ashwyn"]
    b = state.champs["s_dax"]
    f = state.champs["n_kestrel"]
    a.hexpos, b.hexpos, f.hexpos = (0, 0), (1, 0), (-1, 1)
    state.touch()
    stops = reachable(state, a, ("H", 0, 0), 1)
    assert ("H", 1, 0) not in stops              # enemy blocks
    assert ("H", -1, 1) not in stops             # cannot stop on a friend
    stops2 = reachable(state, a, ("H", 0, 0), 2)
    assert any(n[0] == "H" and n[1:] == (-2, 2) or n[0] == "T" for n in stops2)


def test_monsters_block_everything(state, board):
    t = board.tile_index["Dragon Pit"]
    state.hidden_mask &= ~(1 << t)
    state.monsters["dragon_0"].alive = True
    state.monsters["dragon_0"].chips = 8
    c = state.champs["n_ashwyn"]
    c.hexpos = (2, -1)
    state.touch()
    stops = reachable(state, c, ("H", 2, -1), 1)
    assert ("H", 3, -1) not in stops


def test_monster_shares_a_hidden_tile(state, board):
    """Rules 3.2/4.1 [DEFAULT]: monsters never flip a tile and are adjacent to
    everything inside it."""
    t = board.tile_index["Dragon Pit"]
    state.monsters["dragon_0"].alive = True
    state.monsters["dragon_0"].chips = 8
    c = state.champs["n_thornjaw"]
    c.hexpos = (2, -1)
    state.touch()
    state.refresh_visibility()
    assert state.hidden_mask >> t & 1, "a monster does not cause a flip"
    assert state.node_of_unit(c) == state.node_of_unit(state.monsters["dragon_0"])


def test_recall_only_from_a_hidden_tile(state, board):
    c = state.champs["n_kestrel"]
    t = board.tile_index["Mid River"]
    c.hexpos = (0, 0)
    state.touch()
    c.speed = 1
    acts = [a for a in legal_activations(state, "north") if a.champ == "n_kestrel"]
    assert any(a.recall for a in acts), "1 movement recalls from inside a hidden tile"
    # Standing on a visible hex, the champion must first walk into a hidden
    # tile (1 movement) and only then pay the recall (1 more).
    state.hidden_mask &= ~(1 << t)
    state.touch()
    acts = [a for a in legal_activations(state, "north") if a.champ == "n_kestrel"]
    assert not any(a.recall for a in acts)
    c.speed = 2
    acts = [a for a in legal_activations(state, "north") if a.champ == "n_kestrel"]
    assert any(a.recall for a in acts)


def test_slow_and_root_reduce_movement(state):
    c = state.champs["n_thornjaw"]
    assert champion_speed(state, c) == 4
    c.slow = 2
    assert champion_speed(state, c) == 2
    c.rooted = True
    assert champion_speed(state, c) == 0
