"""Champion kits and the Rules 14.2 design-budget calculator."""
from __future__ import annotations

import json
from typing import Dict, List, Optional

# Rules 14.2 point tables. v1 is the rulebook's seed table; v2 is the RQ-030
# recalibration: an ability is priced against the activation it consumes, not
# only against its AP cost, so the credits shrink and the per-ability floor
# rises. Rosters name the table they were built to.
POINTS = {
    "v1": {"ap_credit": 3.0, "cd_credit": 2.0, "min_net": 2.0, "max_r_ratio": None},
    # v2 also caps the spread inside a kit: under whole-card cooldown every
    # ability spends the same activation, so a kit whose R dwarfs its Q, W and
    # E is a kit with one real ability. RQ-030.
    "v2": {"ap_credit": 2.0, "cd_credit": 1.5, "min_net": 3.0, "max_r_ratio": 1.75},
    # v3 is the RQ-035 economy recalibration. AREA and LINE were priced by the
    # hits they deal, not by the chips they bank, so a 0 AP AREA touching three
    # units banked three AP for nothing. Their value now climbs with reach, and
    # an ability that carries one cannot be free.
    "v3": {"ap_credit": 2.0, "cd_credit": 1.5, "min_net": 3.0, "max_r_ratio": 1.75,
           "area_base": 6.0, "area_per_range": 0.0, "line_base": 3.0,
           "min_cost_area_line": 1},
}
DEFAULT_POINTS = "v1"

ICONS_DAMAGE = {"HIT", "AREA", "LINE"}
ICONS_SELF_MOVE = {"MOVE", "DASH", "BLINK"}
ICONS_CONTROL = {"PUSH", "PULL", "SLOW", "ROOT", "DELAY"}
ICONS_SUPPORT = {"HEAL", "SHIELD", "HASTE", "REVEAL"}
ALL_ICONS = ICONS_DAMAGE | ICONS_SELF_MOVE | ICONS_CONTROL | ICONS_SUPPORT

L0 = {"cost": 0, "cooldown": 1,
      "steps": [{"icon": "HIT", "k": 1, "range": 1, "target": "enemy_any"}]}


def step_points(step: dict, points: str = DEFAULT_POINTS) -> float:
    """Rules 14.2 point values for one icon step."""
    t = POINTS[points]
    ic = step["icon"]
    if ic == "HIT":
        k = step.get("k", 1)
        r = step.get("range", 1)
        return k * (3 + max(0, r - 1))
    if ic == "AREA":
        k = step.get("k", 1)
        r = step.get("range", 1)
        if "area_base" in t:
            return k * (t["area_base"] + t["area_per_range"] * max(0, r - 1))
        return k * (5 if r <= 1 else 7)
    if ic == "LINE":
        return step.get("k", 1) * (t.get("line_base", 2.0) + step.get("n", 1))
    if ic == "MOVE":
        return 1.0 * step.get("n", 1)
    if ic == "DASH":
        return 1.5 * step.get("n", 1)
    if ic == "BLINK":
        return 2.0 * step.get("n", 1)
    if ic in ("PUSH", "PULL"):
        return 2.0 * step.get("n", 1)
    if ic == "SLOW":
        return 1.5 * step.get("n", 1)
    if ic == "ROOT":
        return 8.0 if step.get("area") else 5.0
    if ic == "DELAY":
        return 8.0
    if ic == "HEAL":
        return 2.0 * step.get("n", 1) + (1 if step.get("range", 1) >= 2 else 0)
    if ic == "SHIELD":
        return 1.5 * step.get("n", 1) + (1 if step.get("range", 1) >= 2 else 0)
    if ic == "HASTE":
        return 6.0 + (1 if step.get("range", 1) >= 2 else 0)
    if ic == "REVEAL":
        return 3.0
    raise ValueError(f"unknown icon {ic}")


def ability_gross(ab: dict, points: str = DEFAULT_POINTS) -> float:
    return sum(step_points(s, points) for s in ab["steps"])


def ability_net(ab: dict, points: str = DEFAULT_POINTS) -> float:
    t = POINTS[points]
    return (ability_gross(ab, points) - t["ap_credit"] * ab.get("cost", 0)
            - t["cd_credit"] * max(0, ab.get("cooldown", 1) - 1))


def stat_points(stats: dict) -> float:
    return 3 * (stats["hp"] - 6) + 5 * (stats["speed"] - 3)


def budget(kit: dict, points: Optional[str] = None) -> dict:
    points = points or kit.get("points", DEFAULT_POINTS)
    out = {"stats": stat_points(kit["stats"])}
    total = out["stats"]
    for key in ("Q", "W", "E", "R"):
        net = ability_net(kit["abilities"][key], points)
        out[key] = net
        total += net
    out["total"] = total
    return out


def validate_kit(kit: dict, points: Optional[str] = None) -> List[str]:
    """Rules 14.2 constraints. Returns a list of problems (empty == valid).

    A kit may carry ``budget_exception``: a stated reason for sitting outside
    the band or the spread cap on purpose. The budget is only a first guess at
    equal power, so a kit whose measured win rate lands in band is balanced
    whatever the arithmetic says. Exceptions suppress the two whole-kit checks
    and nothing else - every ability still has to be worth its activation, and
    a farming engine still cannot be free.
    """
    points = points or kit.get("points", DEFAULT_POINTS)
    min_net = POINTS[points]["min_net"]
    errs: List[str] = []
    st = kit["stats"]
    if not 6 <= st["hp"] <= 9:
        errs.append(f"{kit['id']}: HP {st['hp']} outside 6-9")
    if not 2 <= st["speed"] <= 4:
        errs.append(f"{kit['id']}: Speed {st['speed']} outside 2-4")
    grosses = {}
    for key in ("Q", "W", "E", "R"):
        ab = kit["abilities"][key]
        if not 0 <= ab.get("cost", 0) <= 3:
            errs.append(f"{kit['id']}.{key}: cost {ab.get('cost')} outside 0-3")
        if ab.get("cooldown", 1) < 1:
            errs.append(f"{kit['id']}.{key}: cooldown < 1")
        for s in ab["steps"]:
            if s["icon"] not in ALL_ICONS:
                errs.append(f"{kit['id']}.{key}: unknown icon {s['icon']}")
        net = ability_net(ab, points)
        if net < min_net:
            errs.append(f"{kit['id']}.{key}: net value {net} < {min_net}"
                        " (an ability must be worth the activation it spends)")
        grosses[key] = ability_gross(ab, points)
    excused = bool(kit.get("budget_exception"))
    if grosses["R"] < max(grosses[k] for k in ("Q", "W", "E")):
        errs.append(f"{kit['id']}: R gross {grosses['R']} is not the highest {grosses}")
    min_cost = POINTS[points].get("min_cost_area_line")
    if min_cost:
        for key in ("Q", "W", "E", "R"):
            ab = kit["abilities"][key]
            if any(st["icon"] in ("AREA", "LINE") for st in ab["steps"]) \
                    and ab.get("cost", 0) < min_cost:
                errs.append(f"{kit['id']}.{key}: AREA/LINE at {ab.get('cost', 0)} AP - a "
                            f"farming engine has to cost at least {min_cost}")
    ratio_cap = POINTS[points].get("max_r_ratio")
    if ratio_cap:
        basics = sum(grosses[k] for k in ("Q", "W", "E")) / 3.0
        if basics and grosses["R"] > ratio_cap * basics and not excused:
            errs.append(f"{kit['id']}: R gross {grosses['R']} is more than "
                        f"{ratio_cap}x the Q/W/E mean {basics:.1f} - one real ability")
    tot = budget(kit, points)["total"]
    if excused:
        return errs
    if not 20 <= tot <= 24:
        errs.append(f"{kit['id']}: budget total {tot} outside 22 +/- 2")
    if kit.get("budget", {}).get("total") is not None:
        claimed = kit["budget"]["total"]
        if abs(claimed - tot) > 1e-6:
            errs.append(f"{kit['id']}: claimed budget {claimed} != computed {tot}")
    n_delay = sum(1 for k in ("Q", "W", "E", "R")
                  for s in kit["abilities"][k]["steps"] if s["icon"] == "DELAY")
    n_haste = sum(1 for k in ("Q", "W", "E", "R")
                  for s in kit["abilities"][k]["steps"] if s["icon"] == "HASTE")
    if n_delay > 1:
        errs.append(f"{kit['id']}: {n_delay} DELAY steps (cap 1)")
    if n_haste > 1:
        errs.append(f"{kit['id']}: {n_haste} HASTE steps (cap 1)")
    return errs


def load_roster(path: str) -> Dict[str, dict]:
    with open(path) as fh:
        data = json.load(fh)
    kits = {k["id"]: k for k in data["champions"]}
    points = data.get("points", DEFAULT_POINTS)
    for k in kits.values():
        k.setdefault("points", points)
        k["abilities"]["L0"] = json.loads(json.dumps(L0))
    return kits
