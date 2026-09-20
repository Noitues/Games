import json

"""Rules 14: every kit is legal and on budget."""
from engine.kits import ability_gross, ability_net, budget, validate_kit


def test_roster_is_balanced_across_roles(kits):
    roles = {}
    for k in kits.values():
        roles.setdefault(k["role"], []).append(k["id"])
    assert sorted(roles) == ["ADC", "Jungle", "Mid", "Support", "Top"]
    counts = {len(v) for v in roles.values()}
    assert len(counts) == 1, f"uneven roles: { {r: len(v) for r, v in roles.items()} }"
    assert counts.pop() >= 2
    assert len({k["name"] for k in kits.values()}) == len(kits)


def test_identities_are_distinct(kits):
    """Prompts 4.B guardrail: no two champions share a kit."""
    seen = {}
    for k in kits.values():
        sig = (k["stats"]["hp"], k["stats"]["speed"],
               json.dumps([k["abilities"][a] for a in ("Q", "W", "E", "R")], sort_keys=True))
        assert sig not in seen, f"{k['id']} duplicates {seen.get(sig)}"
        seen[sig] = k["id"]


def test_kits_validate(kits):
    errs = [e for k in kits.values() for e in validate_kit(k)]
    assert errs == [], errs


def test_budget_band(kits):
    for k in kits.values():
        assert 20 <= budget(k)["total"] <= 24


def test_rulebook_worked_examples():
    """Rules 14.2 v1 table: Bastion totals 21, Kestrel totals 23. The examples
    belong to the seed table, so they are checked against the roster that was
    built to it."""
    import os
    from engine.kits import load_roster
    v1 = load_roster(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                  "roster", "roster_v1.1.0.json"))
    assert budget(v1["bastion"], "v1")["total"] == 21
    assert budget(v1["kestrel"], "v1")["total"] == 23
    assert ability_gross(v1["kestrel"]["abilities"]["R"]) == 16
    assert ability_net(v1["kestrel"]["abilities"]["R"], "v1") == 3


def test_recalibrated_table_flattens_the_kits(kits):
    """RQ-030 / P-0001: no ability may be a dud, and no R may dwarf its kit."""
    from engine.kits import POINTS
    for k in kits.values():
        grosses = {s: ability_gross(k["abilities"][s]) for s in ("Q", "W", "E", "R")}
        basics = sum(grosses[s] for s in ("Q", "W", "E")) / 3
        assert grosses["R"] <= 1.75 * basics + 1e-9, k["id"]
        for s in ("Q", "W", "E", "R"):
            assert ability_net(k["abilities"][s], "v2") >= 3, f"{k['id']}.{s}"


def test_each_champion_has_an_affordable_ap_ability(kits):
    """Prompts 4.B: at least one AP-cost ability usable in most lane spots."""
    for k in kits.values():
        paid = [a for a in ("Q", "W", "E", "R") if k["abilities"][a]["cost"] > 0]
        assert paid, k["id"]
        assert min(k["abilities"][a]["cost"] for a in paid) <= 2
