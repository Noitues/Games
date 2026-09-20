"""Rules 5, 6: round structure, snake order, cooldowns, respawn, recall."""
from engine.abilities import apply_plan
from engine.actions import Activation
from engine.game import (SNAKE, apply_activation, legal_activations, new_game,
                         upkeep)
from engine.resolve import ability_cooldown
from engine.state import other


def test_snake_order(state):
    p1 = state.priority
    order = [p1 if i == 0 else other(p1) for i in SNAKE]
    assert order == [p1, other(p1), other(p1), p1, p1,
                     other(p1), other(p1), p1, p1, other(p1)]
    assert len(order) == 10
    assert order.count(p1) == 5


def test_priority_alternates_each_round(state, game):
    upkeep(state, game)
    assert state.round == 1 and state.priority == "north"
    upkeep(state, game)
    assert state.round == 2 and state.priority == "south"
    upkeep(state, game)
    assert state.priority == "north"


def test_whole_card_goes_on_cooldown(state, game):
    c = state.champs["n_kestrel"]
    c.hexpos = (0, -1)          # within R's line of the south mid T1 at (0,2)
    state.teams["north"].ap = 3
    state.touch()
    act = next(a for a in legal_activations(state, "north")
               if a.champ == c.uid and a.ability == "R")
    apply_activation(state, act, game)
    assert c.track == ability_cooldown(c, state.kits["kestrel"]["abilities"]["R"]) == 3
    assert not any(a.champ == c.uid for a in legal_activations(state, "north"))


def test_move_only_activation_is_free(state, game):
    c = state.champs["n_kestrel"]
    act = next(a for a in legal_activations(state, "north")
               if a.champ == c.uid and a.ability is None and not a.recall)
    apply_activation(state, act, game)
    assert c.track == 0 and c.activated


def test_one_activation_per_champion_per_round(state, game):
    c = state.champs["n_kestrel"]
    c.activated = True
    assert not any(a.champ == c.uid for a in legal_activations(state, "north"))
    upkeep(state, game)
    assert any(a.champ == c.uid for a in legal_activations(state, "north"))


def test_cooldown_track_counts_down_and_returns_the_card(state, game):
    c = state.champs["n_kestrel"]
    c.track = 2
    upkeep(state, game)
    assert c.track == 1
    upkeep(state, game)
    assert c.track == 0


def test_dead_champion_respawns_at_full_hp(state, game):
    from engine.resolve import kill_champion
    state.round = 3
    c = state.champs["n_kestrel"]
    c.hp = 1
    kill_champion(state, c, "south", None)
    assert c.track == 2 and not c.alive
    upkeep(state, game)           # round 4
    assert not c.alive and c.track == 1
    upkeep(state, game)           # round 5
    assert c.alive and c.hp == c.max_hp
    assert c.hexpos == state.board.fountain["north"]


def test_fountain_heals_at_upkeep(state, game):
    c = state.champs["n_kestrel"]
    c.hp = 2
    assert state.board.tile_of[c.hexpos] == state.board.tile_of[state.board.fountain["north"]]
    upkeep(state, game)
    assert c.hp == c.max_hp


def test_recall_puts_the_champion_at_its_fountain(state, game):
    c = state.champs["n_kestrel"]
    c.hexpos = (0, 0)
    state.touch()
    home = state.board.node_of(state.board.fountain["north"], state.hidden_mask)
    act = next(a for a in legal_activations(state, "north")
               if a.champ == c.uid and a.recall and a.dest == home and a.ability is None)
    apply_activation(state, act, game)
    base = state.board.tile_of[state.board.fountain["north"]]
    assert state.board.tile_of[c.hexpos] == base
    # Remaining movement may be spent from the fountain (Rules 5.2).
    assert any(a.recall and a.dest != home
               for a in legal_activations(state, "north") if a.champ == "n_lumen")


def test_delay_and_haste_move_cards_on_the_track(state, game):
    vellum = state.champs["s_vellum"]
    target = state.champs["n_kestrel"]
    apply_plan(state, vellum, "W", (target.uid, None))
    assert target.track == 1
    lumen = state.champs["n_lumen"]
    apply_plan(state, lumen, "E", (target.uid,))
    assert target.track == 0


def test_round_limit_tiebreak(board, kits, cfg):
    from engine.run import Game
    from tests.conftest import PICKS
    st = new_game(board, kits, PICKS, cfg)
    st.round = cfg["round_limit"]
    st.teams["south"].towers_lost = 2
    g = Game(st, {}, seed=0)
    winner, reason = g._tiebreak()
    assert winner == "north" and reason == "round_limit_towers"
