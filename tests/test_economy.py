"""Rules 7, 11, 12: AP refresh, buff cards, the shop."""
from engine.actions import Purchase
from engine.game import apply_purchase, legal_purchases, upkeep
from engine.resolve import deal_hits


def test_ap_refreshes_to_three_and_does_not_carry_over(state, game):
    state.teams["north"].ap = 11
    upkeep(state, game)
    assert state.teams["north"].ap == 3


def test_dragon_cards_add_ap_up_to_the_cap(state, game):
    state.teams["north"].dragons = 3
    upkeep(state, game)
    assert state.teams["north"].ap == 5


def test_killing_blue_buff_grants_a_card(state):
    m = state.monsters["blue_buff_0"]
    m.alive, m.chips = True, 4
    deal_hits(state, "north", m, 4, "chips_monster", state.champs["n_thornjaw"])
    assert "blue_buff" in state.teams["north"].cards
    assert state.teams["north"].ap == 4          # its chips are the AP
    assert m.respawn_round == state.round + 4


def test_killing_dragon_and_baron(state):
    d = state.monsters["dragon_0"]
    d.alive, d.chips = True, 8
    deal_hits(state, "south", d, 8, "chips_monster", state.champs["s_mossgrove"])
    assert state.teams["south"].dragons == 1
    b = state.monsters["baron_0"]
    b.alive, b.chips = True, 12
    deal_hits(state, "south", b, 12, "chips_monster", state.champs["s_mossgrove"])
    assert state.teams["south"].baron_track == 3


def test_shop_purchases_and_item_effects(state):
    ts = state.teams["north"]
    ts.ap = 10
    c = state.champs["n_kestrel"]
    assert apply_purchase(state, "north", Purchase("ruby_crystal", c.uid))
    assert c.max_hp == 10 and ts.ap == 6
    assert apply_purchase(state, "north", Purchase("boots", c.uid))
    assert c.speed == 4 and ts.ap == 2
    assert not apply_purchase(state, "north", Purchase("ruby_crystal", c.uid))


def test_card_copies_are_capped_at_two(state):
    ts = state.teams["north"]
    ts.ap = 20
    for _ in range(2):
        assert apply_purchase(state, "north", Purchase("health_potion"))
    assert not apply_purchase(state, "north", Purchase("health_potion"))
    assert not any(p.item == "health_potion" for p in legal_purchases(state, "north"))


def test_long_sword_doubles_l0(state):
    from engine.abilities import apply_plan
    c = state.champs["n_kestrel"]
    c.items.add("long_sword")
    tower = state.structures["s_mid_T1"]
    c.hexpos = (0, 1)
    state.hidden_mask = 0
    state.touch()
    apply_plan(state, c, "L0", (tower.uid,))
    assert tower.chips == 6


def test_longbow_extends_range(state):
    from engine.resolve import ability_range
    c = state.champs["n_kestrel"]
    assert ability_range(c, "Q", 3) == 3
    c.items.add("longbow")
    assert ability_range(c, "Q", 3) == 4
    assert ability_range(c, "L0", 1) == 1


def test_ionian_charm_lowers_cooldowns(state):
    from engine.resolve import ability_cooldown
    c = state.champs["n_kestrel"]
    r = state.kits["kestrel"]["abilities"]["R"]
    assert ability_cooldown(c, r) == 3
    c.items.add("ionian_charm")
    assert ability_cooldown(c, r) == 2
    assert ability_cooldown(c, state.kits["kestrel"]["abilities"]["Q"]) == 1


def test_vampiric_blade_heals_on_chips(state):
    c = state.champs["n_kestrel"]
    c.items.add("vampiric_blade")
    c.hp = 4
    deal_hits(state, "north", state.structures["s_mid_T1"], 3, "chips_structure", c)
    assert c.hp == 7
