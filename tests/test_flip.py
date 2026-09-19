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
    state.champs["s_dax"].hexpos = (2, -1)
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
