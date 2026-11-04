"""Generate the people deck (Common + Remarkable cards) from the PP balance framework.

Deterministic: same seed -> same deck. Outputs data/people.json and data/people.csv,
and prints summary statistics. All prices mirror GDD.md "Balance framework".
"""
import csv, json, random, sys
from collections import Counter
from pathlib import Path

SEED = 1
N_COMMON, N_REMARKABLE = 300, 100
GUILDS = ["Engineers", "Farmers", "Medics", "Bureaucrats",
          "Navigators", "Scholars", "Laborers", "Keepers"]
HOME_TYPE = {"Engineers": "Infrastructure", "Laborers": "Infrastructure",
             "Medics": "Residential", "Keepers": "Residential",
             "Farmers": "Agricultural", "Bureaucrats": "Government",
             "Scholars": "Government", "Navigators": "Hull"}

# verb -> (PP per unit, max units, text template, minimum tier)
VERBS = {
    "damage":          (1.0, 6, "{n} damage", "C"),
    "downgrade":       (1.5, 2, "downgrade {n} threat piece(s)", "C"),
    "vent_glitch":     (0.5, 3, "vent {n} Glitch(es)", "C"),
    "vent_fault":      (1.0, 2, "vent {n} Fault(s)", "C"),
    "vent_failure":    (1.5, 1, "vent {n} Failure", "R"),
    "patch":           (1.5, 1, "Patch", "C"),
    "lockout":         (1.0, 1, "Lockout", "C"),
    "isolate_fault":   (1.0, 2, "Isolate {n} Fault(s)", "C"),
    "isolate_failure": (1.5, 1, "Isolate {n} Failure", "C"),
    "brace":           (0.5, 6, "Brace {n}", "C"),
    "quarantine":      (1.0, 1, "Quarantine", "C"),
    "gather_crew":     (0.5, 3, "gather {n} Crew", "C"),
    "move_crew":       (0.5, 3, "move {n} Crew", "C"),
    "add_crew":        (3.0, 2, "add {n} Crew", "C"),
    "restore_decay":   (3.0, 2, "restore {n} Decay", "C"),
    "add_influence":   (2.0, 1, "add {n} influence", "C"),
    "move_influence":  (1.0, 2, "move {n} influence", "C"),
    "purpose":         (1.0, 4, "+{n} Purpose", "C"),
    "credits":         (1.0, 3, "+{n} credits", "C"),
    "foresee":         (0.5, 1, "foresee", "C"),
    "temper_legacy":   (3.0, 1, "temper the Elder's Legacy", "R"),
}
# Card-balance repricing (sim/cards.js pick rates, Common cards): price x (1 + 1.5 x pick-rate difference
# vs same-cost cards), clamped to 0.7-1.3, for verbs on 10+ cards. Damage and influence were underpriced;
# move influence, Quarantine and foresee overpriced.
REPRICE = {"add_influence": 1.21, "damage": 1.135, "add_crew": 1.075, "restore_decay": 1.045,
           "vent_glitch": 1.03, "downgrade": 1.015, "lockout": 0.985, "brace": 0.94, "vent_fault": 0.94,
           "credits": 0.94, "purpose": 0.94, "gather_crew": 0.94, "patch": 0.91, "isolate_fault": 0.91,
           "foresee": 0.88, "quarantine": 0.835, "move_influence": 0.805}
# Tested and REJECTED (see sim/RESULTS.md "Card balance"): applying REPRICE and 1.15 PP per credit dropped
# the win rate from 76% to 59% without narrowing the pick-rate spread. Kept off; set APPLY_REPRICE to retry.
APPLY_REPRICE = False
if APPLY_REPRICE:
    for _v, _f in REPRICE.items():
        _p, _mx, _t, _tier = VERBS[_v]
        VERBS[_v] = (round(_p * _f, 3), _mx, _t, _tier)
COMMON_PP_PER_CREDIT = 1.15 if APPLY_REPRICE else 1.0

GLOBAL_VERBS = {"purpose", "credits", "foresee", "temper_legacy"}  # no section needed
HOUSE_VERBS = ["credits", "add_influence", "move_influence", "purpose"]

POOLS = {  # guild -> verb weights (identity tendencies)
    "Engineers":   {"damage": 5, "downgrade": 3, "patch": 1, "isolate_fault": 1},
    "Laborers":    {"damage": 3, "vent_glitch": 2, "vent_fault": 2, "brace": 2,
                    "restore_decay": 1, "gather_crew": 1},
    "Medics":      {"brace": 4, "gather_crew": 3, "move_crew": 1, "add_crew": 1, "isolate_fault": 1},
    "Farmers":     {"patch": 3, "gather_crew": 2, "add_crew": 2, "restore_decay": 1},
    "Bureaucrats": {"quarantine": 2, "move_influence": 2, "credits": 2, "vent_fault": 2,
                    "isolate_fault": 1},
    "Navigators":  {"vent_glitch": 2, "vent_fault": 1, "vent_failure": 1, "lockout": 3,
                    "foresee": 2, "move_crew": 1, "damage": 1},
    "Scholars":    {"purpose": 3, "downgrade": 2, "isolate_fault": 1, "isolate_failure": 1,
                    "foresee": 1},
    "Keepers":     {"purpose": 3, "add_influence": 2, "temper_legacy": 1, "brace": 1},
}

RANGE_MULT = {0: 0.8, 1: 1.0, 2: 1.15, 3: 1.3}
TARGET_MULT = {"ANY": 1.0, "type": 0.85, "narrow": 0.75}

# Reign: applied at start of Day. Legacy: applied at Dusk in each section matching
# the paired event; priced at LEGACY_SECTIONS reference sections.
REIGN_VERBS = {"brace": 0.5, "patch": 1.5, "lockout": 1.0, "gather_crew": 0.5,
               "damage": 1.0, "purpose": 1.0, "credits_each_house": 1.0}
REIGN_TEXT = {"brace": "Brace {n} in each section matching its event",
              "patch": "Patch each section matching its event",
              "lockout": "Lockout each section matching its event",
              "gather_crew": "gather {n} Crew into each section matching its event",
              "damage": "{n} damage in each section matching its event",
              "purpose": "+{n} Purpose",
              "credits_each_house": "each house gains {n} credit(s)"}
REIGN_SECTIONS, PLAYERS_REF = 2, 2
LEGACY_VERBS = {"add_glitch": 1.0, "add_fault": 2.0, "add_failure": 3.0,
                "destroy_crew": 3.0, "add_decay": 4.0, "lose_influence": 2.0,
                "add_unrest": 1.5, "lose_purpose": 1.0, "lose_credits_each_house": 1.0}
LEGACY_TEXT = {"add_glitch": "add {n} Glitch", "add_fault": "add {n} Fault",
               "add_failure": "add {n} Failure", "destroy_crew": "destroy {n} Crew",
               "add_decay": "add {n} Decay", "lose_influence": "each house loses {n} influence",
               "add_unrest": "add {n} Unrest", "lose_purpose": "-{n} Purpose",
               "lose_credits_each_house": "each house loses {n} credit(s)"}
LEGACY_SECTIONS = 2
PER_SECTION = {"add_glitch", "add_fault", "add_failure", "destroy_crew", "add_decay",
               "lose_influence", "add_unrest"}

THRESHOLD_PP_PER_ELEMENT = 1.0
# Step 1 recalibration: if sim/calibrate.js has measured how often card thresholds of each size are
# met, price the bonus so its expected value is about EXPECTED_PP_PER_ELEMENT per required element
# (harder thresholds pay more), clamped to 1-3 PP per element.
EXPECTED_PP_PER_ELEMENT = 0.5
CALIBRATION = {}
_cal = Path(__file__).resolve().parent.parent / "data" / "calibration.json"
if _cal.exists():
    CALIBRATION = json.loads(_cal.read_text()).get("thresholdRate", {})


def threshold_pp_per_element(n):
    rate = CALIBRATION.get(str(n))
    if not rate:
        return THRESHOLD_PP_PER_ELEMENT
    return max(1.0, min(3.0, EXPECTED_PP_PER_ELEMENT / rate))


def wchoice(rng, weights):
    keys = list(weights)
    return rng.choices(keys, [weights[k] for k in keys])[0]


MAX_VERBS = {"C": 2, "R": 3}


def eff_price(v, mult):
    """Range/target modifiers apply only to section effects, not global ones."""
    return VERBS[v][0] * (1.0 if v in GLOBAL_VERBS else mult)


def fill(rng, pool, budget, tier, mult, max_verbs, tol=0.25):
    """Greedy-random fill of effects whose modified PP sums to budget."""
    for _ in range(400):
        effects, left = Counter(), budget
        tries = 0
        while left > tol and tries < 50:
            tries += 1
            v = wchoice(rng, pool)
            _, mx, _, mintier = VERBS[v]
            price = eff_price(v, mult)
            if mintier == "R" and tier == "C":
                continue
            if v not in effects and len(effects) >= max_verbs:
                continue
            room = (mx * 2 if tier == "R" else mx) - effects[v]
            n = min(room, int((left + tol) // price))
            if n <= 0:
                continue
            n = rng.randint(1, n)
            effects[v] += n
            left -= n * price
        if abs(left) <= tol + 1e-9 and effects:
            return dict(effects)
    return None


def text_of(effects):
    return "; ".join(VERBS[v][2].format(n=n) for v, n in effects.items())


def pp_of(effects, mult):
    return sum(eff_price(v, mult) * n for v, n in effects.items())


def make_reign_legacy(rng, tier, primary):
    lo, hi, margin = (2, 4, 1.0) if tier == "C" else (4, 7, 2.0)
    for _ in range(500):
        r_target = rng.randint(lo, hi)
        reign, left = Counter(), float(r_target)
        for _ in range(20):
            v = rng.choice(list(REIGN_VERBS))
            unit = REIGN_VERBS[v] * (PLAYERS_REF if v == "credits_each_house"
                                     else 1 if v == "purpose" else REIGN_SECTIONS)
            if unit <= left + 0.01 and (v not in ("patch", "lockout") or reign[v] == 0):
                reign[v] += 1; left -= unit
            if left < 0.5: break
        if abs(left) > 0.01: continue
        l_target = r_target - margin
        legacy, left = Counter(), l_target
        for _ in range(20):
            v = rng.choice(list(LEGACY_VERBS))
            unit = LEGACY_VERBS[v] * (LEGACY_SECTIONS if v in PER_SECTION else
                                     PLAYERS_REF if v == "lose_credits_each_house" else 1)
            if unit <= left + 0.01:
                legacy[v] += 1; left -= unit
            if left < 0.5: break
        if abs(left) > 0.01: continue
        return ({"effects": dict(reign), "pp": r_target,
                 "text": "; ".join(REIGN_TEXT[v].format(n=n) for v, n in reign.items())},
                {"effects": dict(legacy), "pp": l_target, "per_section": LEGACY_SECTIONS,
                 "text": "; ".join(LEGACY_TEXT[v].format(n=n) for v, n in legacy.items())})
    raise RuntimeError("reign/legacy fit failed")


def icon_bag(rng, n_cards):
    """Distinct guilds per card; guild totals kept even across the deck."""
    counts = [rng.choices([2, 3, 4], [1, 2, 1])[0] for _ in range(n_cards)]
    total = sum(counts)
    remaining = Counter({g: total // len(GUILDS) + 1 for g in GUILDS})
    cards = []
    for c in counts:
        icons = []
        for _ in range(c):
            opts = [g for g in GUILDS if g not in icons and remaining[g] > 0]
            g = rng.choices(opts, [remaining[o] for o in opts])[0]
            icons.append(g); remaining[g] -= 1
        cards.append(icons)
    return cards


def make_card(rng, cid, tier, icons):
    primary = icons[0]
    secondary = next((g for g in icons[1:] if g != primary), primary)
    if tier == "C":
        cost = rng.choices([0, 1, 2, 3], [15, 35, 35, 15])[0]
        value = 2 + (cost if COMMON_PP_PER_CREDIT == 1.0 else COMMON_PP_PER_CREDIT * cost)
    else:
        cost = rng.choices(range(2, 9), [8, 14, 18, 18, 16, 14, 12])[0]
        value = 2 + 1.5 * cost
    house_target = tier == "C" and rng.random() < 0.08 or tier == "R" and rng.random() < 0.05
    if house_target:
        target = {"kind": "house", "range": None, "type": "another house"}
        mult = 1.0
        pool = {v: 1 for v in HOUSE_VERBS}
    else:
        rng_v = rng.choices([0, 1, 2, 3], [20, 45, 25, 10])[0]
        tk = rng.choices(["ANY", "type", "narrow"], [30, 50, 20])[0]
        ttype = {"ANY": "ANY", "type": HOME_TYPE[primary] if HOME_TYPE[primary] != "Hull"
                 else "Hull", "narrow": rng.choice(["Hull", "section with Crew",
                                                     "section with Decay",
                                                     "section with a Failure"])}[tk]
        if ttype == "Hull" and tk == "type":
            tk = "narrow"
        mult = RANGE_MULT[rng_v] * TARGET_MULT[tk]
        target = {"kind": "section", "range": rng_v, "type": ttype, "class": tk}
        pool = Counter(POOLS[primary])
        for v, w in POOLS[secondary].items():
            pool[v] += w * 0.5
    effects = fill(rng, pool, value, tier, mult, MAX_VERBS[tier])
    if effects is None:
        return None
    card = {"id": cid, "tier": "Common" if tier == "C" else "Remarkable",
            "cost": cost, "guilds": icons, "target": target,
            "effects": effects, "text": text_of(effects),
            "pp_target": round(value, 2), "pp_actual": round(pp_of(effects, mult), 2)}
    has_threshold = tier == "R" or rng.random() < 0.25
    if has_threshold:
        ng = 1 if tier == "C" and rng.random() < 0.5 else 2
        gs = [primary] if ng == 1 else [primary, secondary]
        total = rng.randint(2, 3) if tier == "C" else rng.randint(3, 6)
        req = Counter()
        for k in range(total):
            req[gs[k % len(gs)]] += 1
        bonus = fill(rng, pool, total * threshold_pp_per_element(total), tier, mult, 2)
        if bonus:
            card["threshold"] = {"elements": dict(req), "effects": bonus,
                                 "text": text_of(bonus),
                                 "pp": round(pp_of(bonus, mult), 2)}
    card["reign"], card["legacy"] = make_reign_legacy(rng, tier, primary)
    return card


def main(out_dir):
    rng = random.Random(SEED)
    cards = []
    for tier, n, prefix in (("C", N_COMMON, "C"), ("R", N_REMARKABLE, "R")):
        bags = icon_bag(rng, n)
        for i in range(n):
            c = None
            while c is None:
                c = make_card(rng, f"{prefix}{i + 1:03d}", tier, bags[i])
            cards.append(c)
    out = Path(out_dir)
    (out / "people.json").write_text(json.dumps(cards, indent=1))
    with open(out / "people.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "tier", "cost", "guilds", "target", "effect", "threshold",
                    "threshold_effect", "reign", "legacy", "pp_target", "pp_actual"])
        for c in cards:
            t = c["target"]
            tgt = t["type"] if t["kind"] == "house" else f'range {t["range"]}, {t["type"]}'
            th = c.get("threshold")
            w.writerow([c["id"], c["tier"], c["cost"], " ".join(c["guilds"]), tgt, c["text"],
                        " + ".join(f"{g} {n}" for g, n in th["elements"].items()) if th else "",
                        th["text"] if th else "", c["reign"]["text"], c["legacy"]["text"],
                        c["pp_target"], c["pp_actual"]])
    # stats
    icons = Counter(g for c in cards for g in c["guilds"])
    print("cards", len(cards), "| icons/card", round(sum(icons.values()) / len(cards), 2))
    print("icons by guild", dict(icons))
    for tier in ("Common", "Remarkable"):
        cs = [c for c in cards if c["tier"] == tier]
        dev = [c["pp_actual"] - c["pp_target"] for c in cs]
        print(tier, len(cs), "| cost curve", dict(sorted(Counter(c["cost"] for c in cs).items())),
              "| thresholds", sum("threshold" in c for c in cs),
              "| PP deviation mean %.2f max %.2f" % (sum(dev) / len(dev), max(map(abs, dev))))
    print("verbs", Counter(v for c in cards for v in c["effects"]).most_common())


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "data")
