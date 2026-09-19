"""Champion kits and the Rules 14.2 design-budget calculator."""
from __future__ import annotations

import json
from typing import Dict, List

ICONS_DAMAGE = {"HIT", "AREA", "LINE"}
ICONS_SELF_MOVE = {"MOVE", "DASH", "BLINK"}
ICONS_CONTROL = {"PUSH", "PULL", "SLOW", "ROOT", "DELAY"}
ICONS_SUPPORT = {"HEAL", "SHIELD", "HASTE", "REVEAL"}
ALL_ICONS = ICONS_DAMAGE | ICONS_SELF_MOVE | ICONS_CONTROL | ICONS_SUPPORT

L0 = {"cost": 0, "cooldown": 1,
      "steps": [{"icon": "HIT", "k": 1, "range": 1, "target": "enemy_any"}]}


def step_points(step: dict) -> float:
    """Rules 14.2 point values for one icon step."""
    ic = step["icon"]
    if ic == "HIT":
        k = step.get("k", 1)
        r = step.get("range", 1)
        return k * (3 + max(0, r - 1))
    if ic == "AREA":
        k = step.get("k", 1)
        r = step.get("range", 1)
        return k * (5 if r <= 1 else 7)
    if ic == "LINE":
        return step.get("k", 1) * (2 + step.get("n", 1))
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


def ability_gross(ab: dict) -> float:
    return sum(step_points(s) for s in ab["steps"])


def ability_net(ab: dict) -> float:
    return ability_gross(ab) - 3 * ab.get("cost", 0) - 2 * max(0, ab.get("cooldown", 1) - 1)


def stat_points(stats: dict) -> float:
    return 3 * (stats["hp"] - 6) + 5 * (stats["speed"] - 3)


def budget(kit: dict) -> dict:
    out = {"stats": stat_points(kit["stats"])}
    total = out["stats"]
    for key in ("Q", "W", "E", "R"):
        net = ability_net(kit["abilities"][key])
        out[key] = net
        total += net
    out["total"] = total
    return out


def validate_kit(kit: dict) -> List[str]:
    """Rules 14.2 constraints. Returns a list of problems (empty == valid)."""
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
        net = ability_net(ab)
        if net < 2:
            errs.append(f"{kit['id']}.{key}: net value {net} < 2")
        grosses[key] = ability_gross(ab)
    if grosses["R"] < max(grosses[k] for k in ("Q", "W", "E")):
        errs.append(f"{kit['id']}: R gross {grosses['R']} is not the highest {grosses}")
    tot = budget(kit)["total"]
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
    for k in kits.values():
        k["abilities"]["L0"] = json.loads(json.dumps(L0))
    return kits
