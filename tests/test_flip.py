"""Rules 3.2-3.5: flips, placement, overflow, flip-back."""
from engine.actions import Placement
from engine.state import place_units_on_flip


def test_tile_flips_when_both_teams_inside(state, board, game):
    t = board.tile_index["Mid River"]
    state.champs["n_ashwyn"].hexpos = (0, 0)
    state.touch()
    state.refresh_visibility()
    assert state.hidden_mask >> t & 1
    state.champs["s_dax"].hexpos = (1, -1)
    state.touch()
    state.refresh_visibility(placer=game.placer)
    assert not state.hidden_mask >> t & 1


def test_flip_back_when_one_team_remains(state, board, game):
    t = board.tile_index["Mid River"]
    state.champs["n_ashwyn"].hexpos = (0, 0)
    state.champs["s_dax"].hexpos = (1, -1)
    state.touch()
    state.refresh_visibility(placer=game.placer)
    assert not state.hidden_mask >> t & 1
    # (2, -1) still borders Mid River, and under RQ-036 an adjacent enemy keeps
    # an occupied hexgroup revealed. Step off the edge entirely to flip back.
    state.champs["s_dax"].hexpos = (3, -2)
    state.touch()
    state.refresh_visibility(placer=game.placer)
    assert state.hidden_mask >> t & 1


def test_flip_gives_every_champion_its_own_hex(state, board, game):
    t = board.tile_index["Mid River"]
    for uid in ("n_ashwyn", "n_kestrel", "n_lumen"):
        state.champs[uid].hexpos = (0, 0)
    state.champs["s_dax"].hexpos = (1, 0)
    state.touch()
    state.refresh_visibility(placer=game.placer)
    assert not state.hidden_mask >> t & 1
    spots = [state.champs[u].hexpos for u in ("n_ashwyn", "n_kestrel", "n_lumen", "s_dax")]
    assert len(set(spots)) == 4


def test_overflow_places_extra_units_adjacent(state, board, game):
    """Rules 3.4 [DEFAULT]."""
    t = board.tile_index["North Blue Buff"]      # 3 hexes, one holds Blue Buff
    hexes = board.tile_hexes[t]
    state.monsters["blue_buff_0"].alive = True
    state.monsters["blue_buff_0"].chips = 4
    movers = ["n_ashwyn", "n_kestrel", "n_lumen", "n_thornjaw"]
    for uid in movers:
        state.champs[uid].hexpos = hexes[0]
    state.champs["s_dax"].hexpos = hexes[1]
    state.touch()
    state.force_visible(t, placer=game.placer)
    spots = {state.champs[u].hexpos for u in movers}
    assert len(spots) == 4
    assert any(s not in hexes for s in spots), "overflow spills outside the tile"


def test_wards_pin_a_tile_visible(state, board):
    t = board.tile_index["Mid River"]
    state.round = 3
    state.wards[t] = 4                     # Control Ward: through the next round
    state.refresh_visibility()
    assert not state.hidden_mask >> t & 1
    state.round = 5
    state.refresh_visibility()
    assert state.hidden_mask >> t & 1


def test_reveal_then_move_does_not_stack(state, board, game):
    """A REVEAL inside an ability can flip the tile the same ability moves into
    (Mossgrove W). The move must still land on a legal, empty hex."""
    from engine.abilities import apply_plan
    from engine.game import assert_state
    t = board.tile_index["North Red Buff"]
    mg = state.champs["s_mossgrove"]
    dax = state.champs["s_dax"]
    mg.hexpos, dax.hexpos = (-5, 0), (-5, 1)
    state.touch()
    state.refresh_visibility(placer=game.placer)
    apply_plan(state, mg, "W", (t, ("T", t)))
    state.refresh_visibility(placer=game.placer)
    assert assert_state(state) == []


def test_move_is_refused_when_the_hex_was_taken_meanwhile(state, board):
    """A destination chosen during enumeration can be occupied by the time the
    movement resolves; the mover then stays where it is."""
    from engine.resolve import move_unit
    state.hidden_mask = 0
    a, b = state.champs["n_kestrel"], state.champs["n_thornjaw"]
    a.hexpos, b.hexpos = (0, 0), (1, 0)
    state.touch()
    move_unit(state, a, ("H", 1, 0), ("H", 0, 0))
    assert a.hexpos == (0, 0) and b.hexpos == (1, 0)
    move_unit(state, a, ("H", -1, 1), ("H", 0, 0))
    assert a.hexpos == (-1, 1)


def test_bump_and_continue(state, board, game):
    """RQ-016: after the bump flips the tile, the mover spends what is left of
    its movement inside it (Rules 3.3 step 4)."""
    from engine.game import apply_activation, legal_activations
    t = board.tile_index["Mid River"]
    hider = state.champs["s_dax"]
    hider.hexpos = (0, 0)
    mover = state.champs["n_thornjaw"]               # Speed 4
    mover.hexpos = (0, -3)
    state.touch()
    state.refresh_visibility(placer=game.placer)
    assert state.hidden_mask >> t & 1

    acts = [a for a in legal_activations(state, "north")
            if a.champ == mover.uid and a.flip_entry == t]
    assert acts, "a bump into the occupied hidden tile is offered"
    pushes = [a for a in acts if a.intent is not None]
    assert pushes, "with movement left over, pushing on is offered too"

    apply_activation(state, pushes[0], game)
    state.refresh_visibility(allow_flip_back=True, placer=game.placer)
    assert not state.hidden_mask >> t & 1, "the tile flipped"
    assert board.tile_of[mover.hexpos] == t, "and the mover carried on into it"


def test_bump_without_intent_stops_at_the_edge(state, board, game):
    from engine.game import apply_activation, legal_activations
    t = board.tile_index["Mid River"]
    state.champs["s_dax"].hexpos = (0, 0)
    mover = state.champs["n_thornjaw"]
    mover.hexpos = (0, -3)
    state.touch()
    state.refresh_visibility(placer=game.placer)
    act = next(a for a in legal_activations(state, "north")
               if a.champ == mover.uid and a.flip_entry == t and a.intent is None)
    apply_activation(state, act, game)
    assert board.tile_of[mover.hexpos] != t


def test_an_adjacent_enemy_reveals_an_occupied_hexgroup(state, board, game):
    """RQ-036: cover works at a distance, not at arm's length."""
    t = board.tile_index["Mid River"]
    state.champs["n_ashwyn"].hexpos = (0, 0)          # hiding inside
    state.champs["s_dax"].hexpos = (3, -2)            # far away: still hidden
    state.touch()
    state.refresh_visibility(placer=game.placer)
    assert state.hidden_mask >> t & 1

    state.champs["s_dax"].hexpos = (2, -1)            # steps onto the edge
    state.touch()
    state.refresh_visibility(placer=game.placer)
    assert not state.hidden_mask >> t & 1, "standing on the edge looks in"


def test_an_empty_hexgroup_is_not_revealed_by_standing_next_to_it(state, board, game):
    t = board.tile_index["Mid River"]
    for c in state.champs.values():
        c.hexpos = state.board.fountain[c.team]
    state.champs["s_dax"].hexpos = (2, -1)            # adjacent, but nobody inside
    state.touch()
    state.refresh_visibility(placer=game.placer)
    assert state.hidden_mask >> t & 1


def test_a_friendly_hexgroup_is_not_revealed_by_its_own_team(state, board, game):
    t = board.tile_index["Mid River"]
    state.champs["n_ashwyn"].hexpos = (0, 0)
    state.champs["n_kestrel"].hexpos = (2, -1)        # same team on the edge
    state.touch()
    state.refresh_visibility(placer=game.placer)
    assert state.hidden_mask >> t & 1


def test_cover_no_longer_restricts_what_you_may_use(state, board, game):
    """RQ-036 retired the RQ-034 ambush gate: playing from cover is the point
    of cover. What limits sniping is the adjacency reveal and short ranges."""
    from engine.resolve import can_act_outside
    c = state.champs["n_kestrel"]
    c.hexpos = (0, -1)
    state.touch()
    state.refresh_visibility(placer=game.placer)
    node = state.node_of_unit(c)
    assert state.hidden_mask >> board.tile_of[c.hexpos] & 1
    for key in ("L0", "Q", "W", "E", "R"):
        assert can_act_outside(state, c, node, key), key


def test_camp_clearing_from_cover_is_untouched(state, board, game):
    """Acting inside your own hexgroup reveals nothing."""
    from engine.abilities import apply_plan
    m = state.monsters["dragon_0"]
    m.alive, m.chips = True, 8
    c = state.champs["n_thornjaw"]
    c.hexpos = (2, -1)
    tile = board.tile_of[c.hexpos]
    state.touch()
    state.refresh_visibility(placer=game.placer)
    apply_plan(state, c, "Q", (m.uid,))
    assert state.hidden_mask >> tile & 1
