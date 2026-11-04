"""Generate events, Discoveries and Ship in Crisis cards (data/*.json).

Deterministic (seed 1). Prices follow GDD.md "Balance framework"; per-section
effects are priced at REF_SECTIONS sections, like Reign/Legacy.
"""
import json, random, sys
from collections import Counter
from pathlib import Path

SEED = 1
TYPES = ["Infrastructure", "Residential", "Government", "Agricultural"]
REF_SECTIONS = 2

# ---------------------------------------------------------------- events
STAGE2_TWISTS = {
    "Infrastructure": {"phase": "collapse", "rule": "faults_plus_one",
                       "text": "Power surge: at Collapse, each Fault deals +1 damage."},
    "Residential": {"phase": "collapse", "rule": "extra_crew_loss",
                    "text": "Panic: at Collapse, destroy 1 additional Crew in each matching section that has threat."},
    "Government": {"phase": "grow", "rule": "grow_adds_glitch",
                   "text": "Red tape: at Grow, each matching section that gains a Fault also gains a Glitch."},
    "Agricultural": {"phase": "seed", "rule": "seed_adjacent",
                     "text": "Spreading rot: at Seed, also seed each section adjacent to a matching section that has threat."},
}


def events():
    cards = []
    for i, t in enumerate(TYPES, 1):
        cards.append({"id": f"E1-{i}", "stage": 1, "types": [t], "twist": None})
    for i, t in enumerate(TYPES, 1):
        cards.append({"id": f"E2-{i}", "stage": 2, "types": [t], "twist": STAGE2_TWISTS[t]})
    cards.append({"id": "E2-5", "stage": 2, "types": ["Hull"], "twist": None,
                  "note": "Outer Hull card (Spirit Island's coastal card); matches every Hull section of any type."})
    pairs = [(a, b) for i, a in enumerate(TYPES) for b in TYPES[i + 1:]]
    for i, (a, b) in enumerate(pairs, 1):
        cards.append({"id": f"E3-{i}", "stage": 3, "types": [a, b], "twist": None})
    landfall = {"id": "LANDFALL", "stage": 4, "types": ["ALL"], "twist": None,
                "note": "Set aside; Landfall toggle only. Matches every section. Win when it retires to the Wall."}
    return {"cards": cards, "landfall": landfall,
            "deck_build": {"stage_counts": {"1": 3, "2": 4, "3": 5},
                           "escalation": "After dealing Stage II, mark one random dealt Stage II card with the Escalation symbol.",
                           "order": "Stage I on top, then II, then III; each stage shuffled separately."}}

# ---------------------------------------------------------- discoveries
# effect key -> (PP per unit, per_section?, text)
D_EFFECTS = {
    "remove_glitch":   (1.0, True,  "remove {n} Glitch"),
    "remove_fault":    (2.0, True,  "remove {n} Fault"),
    "downgrade_fault": (1.5, True,  "downgrade {n} Fault"),
    "downgrade_failure": (1.5, True, "downgrade {n} Failure"),
    "damage":          (1.0, True,  "{n} damage"),
    "skip_grow":       (1.5, True,  "skip the Grow"),
    "skip_seed":       (1.0, True,  "skip the Seed"),
    "brace":           (0.5, True,  "Brace {n}"),
    "gather_crew":     (0.5, True,  "gather {n} Crew"),
    "add_crew":        (3.0, False, "add {n} Crew to any one section"),
    "restore_decay":   (3.0, False, "restore {n} Decay anywhere"),
    "purpose":         (1.0, False, "+{n} Purpose"),
    "credits_each":    (2.0, False, "each house gains {n} credit(s)"),  # 2 houses ref
    "foresee":         (0.5, False, "foresee"),
}
FAMILIES = {
    "Repair":     ["remove_glitch", "remove_fault", "damage", "downgrade_fault", "downgrade_failure"],
    "Control":    ["skip_grow", "skip_seed", "remove_glitch", "foresee"],
    "Protection": ["brace", "gather_crew", "restore_decay"],
    "People":     ["gather_crew", "add_crew", "purpose", "credits_each"],
}
TIER_BUDGET = {"I": 4.0, "II": 6.0, "III": 8.0}
# Breakthrough: ~1 PP per generation, effect in ONE section of players' choice.
BT_OPTIONS = {
    "Repair":     [("dusk", {"damage": 1}), ("day", {"remove_glitch": 1})],
    "Control":    [("day", {"skip_seed": 1}), ("dawn", {"foresee": 1, "remove_glitch": 1})],
    "Protection": [("dusk", {"brace": 2}), ("dusk", {"gather_crew": 2})],
    "People":     [("day", {"purpose": 1}), ("day", {"gather_crew": 2})],
}


def fill(rng, verbs, budget, tol=0.25):
    for _ in range(500):
        eff, left = Counter(), budget
        for _ in range(30):
            v = rng.choice(verbs)
            price, per_sec, _ = D_EFFECTS[v]
            unit = price * (REF_SECTIONS if per_sec else 1)
            if (v not in eff and len(eff) >= 2) or unit > left + tol:
                continue
            if v in ("skip_grow", "skip_seed", "foresee") and eff[v]:
                continue
            eff[v] += 1; left -= unit
            if left <= tol: break
        if abs(left) <= tol and eff:
            return dict(eff), round(budget - left, 2)
    raise RuntimeError("discovery fill failed")


def describe(eff, scope):
    parts = []
    for v, n in eff.items():
        price, per_sec, txt = D_EFFECTS[v]
        t = txt.format(n=n)
        parts.append(f"{t} in each {scope} section" if per_sec else t)
    return "; ".join(parts)


def discoveries(rng, n=24):
    cards, fams = [], list(FAMILIES)
    for i in range(n):
        fam = fams[i % len(fams)]
        scope = rng.choice(TYPES + ["Outer Hull"])
        tiers = {}
        for tier, budget in TIER_BUDGET.items():
            eff, pp = fill(rng, FAMILIES[fam], budget)
            tiers[tier] = {"effects": eff, "scope": scope, "pp": pp,
                           "text": describe(eff, scope)}
        timing, bt = rng.choice(BT_OPTIONS[fam])
        bt_scope = rng.choice(TYPES + ["Outer Hull"])
        bt_pp = sum(D_EFFECTS[v][0] * k for v, k in bt.items())
        bt_text = "; ".join(D_EFFECTS[v][2].format(n=k) for v, k in bt.items())
        cards.append({"id": f"D{i + 1:02d}", "family": fam, "tiers": tiers,
                      "breakthrough": {"timing": timing, "effects": bt, "scope": bt_scope,
                                       "pp_per_generation": bt_pp,
                                       "text": f"Each {timing.capitalize()}: {bt_text} in one {bt_scope} section."}})
    return cards

# --------------------------------------------------------------- crisis
CRISIS = [
    {"id": "X1", "name": "Rationing", "rule": "credits_drain",
     "text": "At the start of each Day, each house loses 1 credit (if it has any)."},
    {"id": "X2", "name": "Structural Fatigue", "rule": "double_cascade",
     "text": "Each cascade places 2 Decay in adjacent sections instead of 1 (players choose)."},
    {"id": "X3", "name": "Despair", "rule": "decay_costs_purpose",
     "text": "Each time Decay is placed, lose 1 Purpose."},
    {"id": "X4", "name": "Failing Systems", "rule": "decay_seeds",
     "text": "At each Grow, add 1 Glitch to every section with Decay that has no threat."},
]


def main(out):
    rng = random.Random(SEED)
    out = Path(out)
    (out / "events.json").write_text(json.dumps(events(), indent=1))
    disc = discoveries(rng)
    (out / "discoveries.json").write_text(json.dumps(disc, indent=1))
    (out / "crisis.json").write_text(json.dumps(
        {"refill_per_player": 1, "pick": "one at random during setup, face down", "cards": CRISIS},
        indent=1))
    print("events written; discoveries:", len(disc),
          Counter(d["family"] for d in disc), "; crisis:", len(CRISIS))
    print(json.dumps(disc[0], indent=1)[:900])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "data")
