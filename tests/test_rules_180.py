"""Rules 1.8.0: structures fall to L0 and waves only, structure chips are not
AP, the Dragon card is reusable, the Baron is permanent (P-0010, P-0011)."""
from engine.actions import Activation, CardPlay
from engine.config import make_config
from engine.game import (apply_activation, apply_card, legal_activations, legal_card_plays,
                         new_game, upkeep)
from engine.resolve import can_be_hit, deal_hits, monster_reward, step_spec
from tests.conftest import PICKS


class _G:
    def placer(self, *a, **k):
        return {}


def _state(board, kits, **over):
    return new_game(board, kits, PICKS, make_config(**over), first="north")


def _tower(st, uid="s_bot_T1"):
    return st.structures[uid]


def test_only_l0_may_target_a_structure(board, kits):
    st = _state(board, kits)
    tower = _tower(st)
    area = {"icon": "AREA", "k": 1, "range": 1, "target": "enemy_any"}
    assert step_spec(st, area, "W") == "enemy_no_structure"
    assert step_spec(st, area, "L0") == "enemy_any"
    assert not can_be_hit(st, tower, "north", "enemy_no_structure")
    assert can_be_hit(st, tower, "north", "enemy_any")
    old = _state(board, kits, abilities_hit_structures=True)
    assert step_spec(old, area, "W") == "enemy_any"


def test_an_ability_next_to_a_tower_cannot_hit_it(board, kits):
    st = _state(board, kits)
    tower = _tower(st)
    c = st.champs["n_ashwyn"]
    # stand ashwyn (Mid, AREA W) beside the enemy bot T1, both tiles face up
    nb = next(h for h in board.neighbors[tower.hexpos]
              if not any(u.alive and u.hexpos == h for u in st.all_units()))
    st.hidden_mask &= ~(1 << board.tile_of[nb]); st.hidden_mask &= ~(1 << board.tile_of[tower.hexpos])
    c.hexpos = nb; st.teams["north"].ap = 5; st.touch()
    before = tower.chips
    legal = legal_activations(st, "north", {})
    w_here = [a for a in legal if a.champ == c.uid and a.ability == "W" and a.dest == st.node_of_unit(c)]
    for a in w_here:
        s = st.clone()
        apply_activation(s, a, _G())
        assert s.structures[tower.uid].chips == before
    l0 = [a for a in legal if a.champ == c.uid and a.ability == "L0" and a.dest == st.node_of_unit(c)
          and a.plan and a.plan[0] == tower.uid]
    assert l0, "L0 must still be able to hit the tower"


def test_structure_chips_are_not_ap(board, kits):
    st = _state(board, kits)
    tower = _tower(st)
    c = st.champs["n_ashwyn"]
    ap = st.teams["north"].ap
    removed = deal_hits(st, "north", tower, 2, "chips_structure", c)
    assert removed == 2 and st.teams["north"].ap == ap
    assert c.dmg_to_structures == 2 and c.ap_earned == 0
    wave = next(iter(st.waves.values())) if st.waves else None
    old = _state(board, kits, structure_chips_pay=True)
    deal_hits(old, "north", _tower(old), 2, "chips_structure", old.champs["n_ashwyn"])
    assert old.teams["north"].ap == ap + 2


def test_dragon_card_is_reusable_on_a_cooldown(board, kits):
    st = _state(board, kits)
    dragon = next(m for m in st.monsters.values() if m.mtype == "dragon")
    monster_reward(st, dragon, "north")
    ts = st.teams["north"]
    assert ts.cards.count("dragon") == 1 and ts.dragons == 1
    c = st.champs["n_ashwyn"]
    victim = st.champs["s_dax"]
    nb = next(h for h in board.neighbors[victim.hexpos] if board.tile_of[h] == board.tile_of[victim.hexpos])
    c.hexpos = nb; st.touch()
    act = Activation(champ=c.uid, dest=st.node_of_unit(c), ability="L0")
    plays = [p for p in legal_card_plays(st, act) if p.card == "dragon"]
    assert any(p.target == victim.uid for p in plays)
    assert not any(p.target.startswith("s_") and p.target in st.structures for p in plays)
    hp = victim.hp
    apply_card(st, act, CardPlay("dragon", victim.uid))
    assert victim.hp == hp - 2
    assert "dragon" not in ts.cards and ts.dragon_track == [3]
    for _ in range(3):
        upkeep(st, _G())
    assert ts.dragon_track == [] and ts.cards.count("dragon") == 1
    assert st.teams["north"].ap_by_source.get("base") is not None   # no dragon AP in base


def test_dragon_pays_no_ap_and_holds_at_most_two_cards(board, kits):
    st = _state(board, kits)
    dragon = next(m for m in st.monsters.values() if m.mtype == "dragon")
    for _ in range(3):
        monster_reward(st, dragon, "north")
    assert st.teams["north"].cards.count("dragon") == 2
    upkeep(st, _G())
    assert st.teams["north"].ap == st.config["ap_base"]


def test_baron_is_permanent(board, kits):
    st = _state(board, kits)
    baron = next(m for m in st.monsters.values() if m.mtype == "baron")
    monster_reward(st, baron, "south")
    for _ in range(8):
        upkeep(st, _G())
    assert st.teams["south"].baron_track > 0
    old = _state(board, kits, baron_permanent=False)
    monster_reward(old, next(m for m in old.monsters.values() if m.mtype == "baron"), "south")
    for _ in range(4):
        upkeep(old, _G())
    assert old.teams["south"].baron_track == 0


def test_a_tower_pays_one_round_of_income_when_it_falls(board, kits):
    st = _state(board, kits)
    tower = _tower(st)
    c = st.champs["n_ashwyn"]
    ap = st.teams["north"].ap
    deal_hits(st, "north", tower, tower.chips, "chips_structure", c)
    assert not tower.alive
    assert st.teams["north"].ap == ap + st.config["ap_base"]
    assert st.teams["north"].ap_by_source.get("tower_kill") == 3
    # a wave finishing a tower pays its team too (no attacker)
    t2 = st.structures["s_bot_T2"]
    deal_hits(st, "north", t2, t2.chips, "chips_structure", None)
    assert not t2.alive and st.teams["north"].ap == ap + 2 * st.config["ap_base"]
    # the Nexus pays nothing: it ends the game
    for s in st.structures.values():
        if s.team == "south" and s.stype == "tower":
            s.alive = False
    nexus = st.structures["s_nexus"]
    before = st.teams["north"].ap
    deal_hits(st, "north", nexus, nexus.chips, "chips_structure", c)
    assert st.winner == "north" and st.teams["north"].ap == before
    old = _state(board, kits, tower_kill_ap=0)
    deal_hits(old, "north", _tower(old), _tower(old).chips, "chips_structure", old.champs["n_ashwyn"])
    assert old.teams["north"].ap == 0
