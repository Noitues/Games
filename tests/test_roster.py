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
    """RQ-030 / P-0001: no ability may be a dud, and no R may dwarf its kit.

    Each kit is judged against the table it was built to, which the roster
    declares, so this keeps holding as the table is recalibrated.
    """
    from engine.kits import POINTS
    for k in kits.values():
        pts = k.get("points", "v1")
        cap = POINTS[pts]["max_r_ratio"]
        floor = POINTS[pts]["min_net"]
        grosses = {s: ability_gross(k["abilities"][s], pts) for s in ("Q", "W", "E", "R")}
        basics = sum(grosses[s] for s in ("Q", "W", "E")) / 3
        if not k.get("budget_exception"):
            assert grosses["R"] <= cap * basics + 1e-9, k["id"]
        for s in ("Q", "W", "E", "R"):
            assert ability_net(k["abilities"][s], pts) >= floor, f"{k['id']}.{s}"


def test_each_champion_has_an_affordable_ap_ability(kits):
    """Prompts 4.B: at least one AP-cost ability usable in most lane spots."""
    for k in kits.values():
        paid = [a for a in ("Q", "W", "E", "R") if k["abilities"][a]["cost"] > 0]
        assert paid, k["id"]
        assert min(k["abilities"][a]["cost"] for a in paid) <= 2


def test_area_and_line_are_never_free(kits):
    """RQ-035 / P-0004: a farming engine has to cost AP (Rules 14.2)."""
    for kit in kits.values():
        for key in ("Q", "W", "E", "R"):
            ab = kit["abilities"][key]
            if any(s["icon"] in ("AREA", "LINE") for s in ab["steps"]):
                assert ab["cost"] >= 1, f"{kit['id']}.{key} banks chips for free"


def test_area_value_climbs_with_reach():
    from engine.kits import step_points
    r1 = step_points({"icon": "AREA", "k": 1, "range": 1}, "v3")
    r2 = step_points({"icon": "AREA", "k": 1, "range": 2}, "v3")
    assert r2 > r1 and r2 - r1 == 4


def test_a_budget_exception_is_stated_not_silent(kits):
    """A kit may sit outside the band on purpose, but it has to say why: the
    budget is a first guess at equal power, and win rate is the real test."""
    for kit in kits.values():
        if kit.get("budget_exception"):
            assert len(kit["budget_exception"]) > 40, kit["id"]
            for key in ("Q", "W", "E", "R"):
                ab = kit["abilities"][key]
                if any(s["icon"] in ("AREA", "LINE") for s in ab["steps"]):
                    assert ab["cost"] >= 1, "an exception does not excuse a free farming engine"
