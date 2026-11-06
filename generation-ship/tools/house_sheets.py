"""Generate houses/<id>.md from data/houses.json (+ measured data/calibration.json).

The data file is the source of truth; run this after changing a house:
    python3 tools/house_sheets.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
houses = json.loads((ROOT / "data/houses.json").read_text())["houses"]
cal_path = ROOT / "data/calibration.json"
cal = json.loads(cal_path.read_text()).get("houseInnate", {}) if cal_path.exists() else {}

IDENTITY = {
    "galvan": ("Fast, aggressive repair crews who hit threat hard and early but can't protect anything.",
               "No Brace, no Crew support, slow influence spread."),
    "meridian": ("Logistics and movement. They run the conduits and supply, move Crew, vent threat and spread influence widely.",
                 "Moderate damage; it moves problems rather than solving them."),
    "keel": ("Slow, sturdy guardians of the ship's structure and its people. Every section they hold is braced at Dusk.",
             "Low damage; it protects rather than clears."),
    "vigil": ("Keepers of the Archive and the Mission. They inspire the crew, generate Purpose, and reach anywhere people gather.",
              "Little damage, fragile influence."),
    "foremen": ("Crew-first leaders. They gather people where the trouble is and make Crew hit harder when they fight back.",
                "Little direct card damage; depends on Crew surviving."),
    "gardeners": ("They spread influence fast and turn it into living armor: Decay that would land on them takes their influence instead.",
                  "Rooted spends influence, and a house with no influence loses the game for everyone."),
    "voidwardens": ("Masters of the Outer Hull. Threat they vent out of a Hull section is thrown into the void.",
                    "Can only add influence to Outer Hull sections; weak in the Core."),
    "tellers": ("They control the story. Their damage never destroys anything; it becomes Purpose and Contains the threat.",
                "Can't clear threat themselves, so teammates must do the removing."),
}

VERB = {"gather_crew": "gather {n} Crew", "brace": "Brace {n}", "damage": "{n} damage", "lockout": "Lockout",
        "downgrade_failure": "downgrade {n} Failure", "vent_glitch": "vent {n} Glitch", "vent_glitch_or_fault": "vent {n} Glitch/Fault",
        "vent_failure": "vent {n} Failure", "patch": "Patch", "quarantine_source": "Quarantine the source", "quarantine": "Quarantine",
        "contain_fault": "Contain {n} Fault", "contain_failure": "Contain {n} Failure", "restore_decay": "restore {n} Decay",
        "add_crew": "add {n} Crew", "purpose": "+{n} Purpose", "foresee": "foresee", "temper_legacy": "temper the Elder's Legacy",
        "crew_strike": "every Crew there deals its damage now"}


def slot(v):
    if isinstance(v, dict):
        k, n = next(iter(v.items()))
        return {"element": f"★ +{n}", "fast_play": "★ +1 fast play", "clone": "★ +1 clone slot", "draw": "★ +1 card drawn"}[k]
    return str(v)


def effects(e):
    return "; ".join(VERB.get(k, k).format(n=v) for k, v in e.items())


for h in houses:
    ident, weak = IDENTITY.get(h["id"], ("", ""))
    g = h["guilds"]
    c = cal.get(h["id"])
    rows = []
    for t in h["innate"]["tiers"]:
        req = " + ".join(f"{k} {v}" for k, v in t["threshold"].items())
        where = f" (range {t['range']}, {t['target']})" if t["range"] is not None else ""
        reach = f"{100 * sum(c['reach'][t['tier']:]):.0f}%" if c else "-"
        rows.append(f"| {t['tier']} | {req} | {effects(t['effects'])}{where} | {t['pp']} | {reach} |")
    overrides = []
    for k, v in (h.get("growth_overrides") or {}).items():
        overrides.append(f"Growth {k}: " + ", ".join(f"{a} {b}" for a, b in v.items() if a not in ("pp",)))
    for k, v in (h.get("growth_perk") or {}).items():
        overrides.append(f"Growth {k} perk: {v['text']}")
    md = f"""# House {h['name']}

**Template:** {h['template']} · **Curve:** {h['curve']}

{ident}

- **Guilds:** {g['primary']} (primary) / {g['secondary']} (secondary)
- **Weaknesses:** {weak}

## Tracks
The first value is the starting value. ★ marks a special slot.

| Track | Values |
|---|---|
| Credits per generation | {' → '.join(slot(x) for x in h['tracks']['credits'])} |
| Card plays | {' → '.join(slot(x) for x in h['tracks']['plays'])} |

Hand = plays + {h['hand_bonus']}. Clone {h['clone']}.

## Special rule
{h['special']['text']}

## Innate: {h['innate']['name']} ({h['innate']['speed']})
Tiers are cumulative; the effect column is the full effect at that tier. *Reached* is how often a generation reaches at least that tier (house bots, calibration run).

| Tier | Threshold | Effect | PP | Reached |
|---|---|---|---|---|
{chr(10).join(rows)}

## Growth
Shared menu: A place influence and uncover a track slot · B gain 2 credits · C draw +2 cards and gain 1 credit.
{chr(10).join('- ' + o for o in overrides) if overrides else ''}

## Starting influence
{h['starting_influence']['text']}

*Generated from `data/houses.json` by `tools/house_sheets.py`.*
"""
    (ROOT / "houses" / f"{h['id']}.md").write_text(md)
print("wrote", len(houses), "sheets")
