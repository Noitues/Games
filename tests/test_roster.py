"""Rules 14: every kit is legal and on budget."""
from engine.kits import ability_gross, ability_net, budget, validate_kit


def test_ten_champions_two_per_role(kits):
    assert len(kits) == 10
    roles = {}
    for k in kits.values():
        roles.setdefault(k["role"], []).append(k["id"])
    assert sorted(roles) == ["ADC", "Jungle", "Mid", "Support", "Top"]
    assert all(len(v) == 2 for v in roles.values())


def test_kits_validate(kits):
    errs = [e for k in kits.values() for e in validate_kit(k)]
    assert errs == [], errs


def test_budget_band(kits):
    for k in kits.values():
        assert 20 <= budget(k)["total"] <= 24


def test_rulebook_worked_examples(kits):
    """Rules 14.2: Bastion totals 21, Kestrel totals 23."""
    assert budget(kits["bastion"])["total"] == 21
    assert budget(kits["kestrel"])["total"] == 23
    assert ability_gross(kits["kestrel"]["abilities"]["R"]) == 16
    assert ability_net(kits["kestrel"]["abilities"]["R"]) == 3


def test_each_champion_has_an_affordable_ap_ability(kits):
    """Prompts 4.B: at least one AP-cost ability usable in most lane spots."""
    for k in kits.values():
        paid = [a for a in ("Q", "W", "E", "R") if k["abilities"][a]["cost"] > 0]
        assert paid, k["id"]
        assert min(k["abilities"][a]["cost"] for a in paid) <= 2
