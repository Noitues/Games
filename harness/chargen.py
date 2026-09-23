"""Character cohorts and personality rotation.

A cohort is 4 characters. Generation is seeded: the seed picks concept/origin/bond/drive/flaw/name
seeds from harness/data/chargen_tables.json, and an LLM writes the cards from those picks. The
result (plus the exact prompt, seed and model) is saved to harness/cohorts/<cohort_id>.json and that
file is the source of truth afterwards, so a cohort is reproducible even though LLM output is not.
With the scripted backend, or if the LLM output fails validation twice, templates are used instead.

Personality rotation is a cyclic Latin rectangle over the batch's run index r and seat p:
    personality(r, p) = PERSONALITY_ORDER[(r + 2p) mod 8]
Each run gets 4 distinct personalities, and over any 8 consecutive runs every personality sits in
every seat exactly once. Cohorts change every 5 runs, so the rotation spans cohorts (see
docs/design_notes.md).
"""

from __future__ import annotations

import argparse
import copy
import json
import random
from pathlib import Path

from agents import PERSONALITY_ORDER, SCHEMAS
from engine import derive_seed

HERE = Path(__file__).parent
TABLES = json.loads((HERE / "data" / "chargen_tables.json").read_text())
COHORT_DIR = HERE / "cohorts"
RUNS_PER_COHORT = 5
N_SEATS = 4


def personalities_for_run(run_index: int) -> list[str]:
    return [PERSONALITY_ORDER[(run_index + 2 * p) % len(PERSONALITY_ORDER)] for p in range(N_SEATS)]


def cohort_index_for_run(run_index: int) -> int:
    return run_index // RUNS_PER_COHORT


def _picks(seed: int) -> list[dict]:
    rng = random.Random(derive_seed(seed, "chargen"))
    names = rng.sample(TABLES["names"], N_SEATS)
    return [{"name": names[i], "concept": c, "origin": o, "bond": b, "drive": d, "flaw": f}
            for i, (c, o, b, d, f) in enumerate(zip(rng.sample(TABLES["concepts"], N_SEATS),
                                                   rng.sample(TABLES["origins"], N_SEATS),
                                                   rng.sample(TABLES["bonds"], N_SEATS),
                                                   rng.sample(TABLES["drives"], N_SEATS),
                                                   rng.sample(TABLES["flaws"], N_SEATS)))]


def chargen_prompt(picks: list[dict], world: dict) -> str:
    return (
        f"Write 4 player characters for a Fate game set in {world['name']}.\n\nSetting:\n{world['setting']}\n\n"
        "Named places and groups you may tie characters to: "
        + ", ".join(sorted({c["title"] for c in world["cards"] if c["type"] in ("LOCATION", "FACTION")})) + ".\n\n"
        "Each character needs:\n"
        "- binder: exactly 4 theme cards in this order: 2 ROOTS (an origin, a person, a place or a comfort), "
        "then 2 REACH (an oath, a burden, a power or a goal). Each card: a title, exactly 3 power tags "
        "(2-5 words each, each names one thing the character can do, has or is) and 1 weakness tag that can "
        "plausibly cause trouble in a scene. At least one ROOTS power tag must name a specific named person, "
        "group or place.\n"
        "- story_cards: exactly 2: one NPC drawn from a ROOTS tag, one THREAD (an open question) drawn from a "
        "REACH tag, same tag format.\n"
        "- skills (Fate Core skill names only: " + ", ".join(TABLES["skills"]) + "): one great, two good, "
        "three fair, four average, all different.\n"
        "- approaches (Careful, Clever, Flashy, Forceful, Quick, Sneaky): one +3, two +2, two +1, one +0.\n"
        "- fae: the SAME character in Fate Accelerated form: a high concept, a trouble that mirrors one card "
        "weakness, and 3 aspects that compress the four cards (keep the same named people and places).\n\n"
        "Use these seeds, one per character, in order:\n"
        + json.dumps(picks, indent=1)
        + "\n\nMake the four characters distinct in role, and give each at least one tie to another "
        "character's people or places only if it arises naturally."
    )


def _initials(name: str, used: set[str]) -> str:
    parts = [p for p in name.replace("-", " ").split() if p]
    ini = (parts[0][0] + (parts[1][0] if len(parts) > 1 else parts[0][1])).upper()
    base, k = ini, 0
    while ini in used:
        k += 1
        ini = base[0] + chr(ord("A") + (ord(base[1]) - ord("A") + k) % 26)
    used.add(ini)
    return ini


def normalize(raw: dict, idx: int, used: set[str]) -> dict:
    """Validate one LLM character and convert it to the template shape. Raises ValueError."""
    name = raw["name"].strip()
    ini = _initials(name, used)
    code = f"PC-{name.split()[0].upper()}"
    binder = raw["binder"]
    if len(binder) != 4 or [c["type"].upper() for c in binder] != ["ROOTS", "ROOTS", "REACH", "REACH"]:
        raise ValueError(f"{name}: binder must be 2 ROOTS then 2 REACH")
    cards = []
    for i, c in enumerate(binder):
        if len(c["power_tags"]) != 3 or not c["weakness"].strip():
            raise ValueError(f"{name}: card {i} needs 3 power tags and a weakness")
        cards.append({"id": f"{ini}-{i+1:02d}", "type": c["type"].upper(), "owner": code, "title": c["title"],
                      "power_tags": [t.strip() for t in c["power_tags"]], "weakness": c["weakness"].strip(),
                      "track": {"kind": "growth", "size": 3}, "blurb": ""})
    story = []
    for i, c in enumerate(raw["story_cards"][:2]):
        tags = [t.strip() for t in c["power_tags"]][:3]
        if len(tags) != 3:
            raise ValueError(f"{name}: story card needs 3 tags")
        story.append({"id": f"{ini}-{5+i:02d}", "type": "NPC" if i == 0 else "THREAD", "owner": code,
                      "title": c["title"], "power_tags": tags, "weakness": c["weakness"],
                      "track": {"kind": "weight", "size": 1}, "blurb": ""})
    sk = raw["skills"]
    order = [sk["great"]] + list(sk["good"]) + list(sk["fair"]) + list(sk["average"])
    valid = {s.lower(): s for s in TABLES["skills"]}
    if len(order) != 10 or len({s.lower() for s in order}) != 10 or any(s.lower() not in valid for s in order):
        raise ValueError(f"{name}: bad skill pyramid {order}")
    skills = {}
    for s, v in zip(order, [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]):
        skills[valid[s.lower()]] = v
    ap = raw["approaches"]
    aorder = [ap["plus3"]] + list(ap["plus2"]) + list(ap["plus1"]) + [ap["plus0"]]
    avalid = {a.lower(): a for a in TABLES["approaches"]}
    if sorted(a.lower() for a in aorder) != sorted(avalid):
        raise ValueError(f"{name}: bad approaches {aorder}")
    approaches = {avalid[a.lower()]: v for a, v in zip(aorder, [3, 2, 2, 1, 1, 0])}
    fae = raw["fae"]
    if len(fae["aspects"]) != 3:
        raise ValueError(f"{name}: FAE needs 3 aspects")
    return {"id": f"CH-{idx+1}", "name": name, "pronouns": raw.get("pronouns", "they/them"),
            "concept": raw["concept"], "skills": skills, "approaches": approaches, "binder": cards,
            "story_cards": story, "fae": {"high_concept": fae["high_concept"], "trouble": fae["trouble"],
                                          "aspects": list(fae["aspects"])}}


def from_templates(seed: int) -> list[dict]:
    rng = random.Random(derive_seed(seed, "templates"))
    chars = copy.deepcopy(rng.sample(TABLES["templates"], N_SEATS))
    for i, c in enumerate(chars):
        c["template_id"] = c["id"]
        c["id"] = f"CH-{i+1}"
    return chars


def generate_cohort(cohort_id: str, seed: int, *, backend: str, client=None, world: dict) -> dict:
    path = COHORT_DIR / f"{cohort_id}.json"
    if path.exists():
        return json.loads(path.read_text())
    picks = _picks(seed)
    prompt = chargen_prompt(picks, world)
    record = {"cohort_id": cohort_id, "seed": seed, "picks": picks, "generation_prompt": prompt,
              "model": None, "source": "templates", "errors": []}
    chars = None
    if backend != "scripted" and client is not None:
        from agents import Agent
        agent = Agent(client, "chargen", "chargen", "You write tabletop RPG characters to an exact format.")
        record["model"] = client.model_for("chargen")
        for attempt in range(2):
            try:
                out = agent.ask("chargen", prompt)
                used: set[str] = set()
                chars = [normalize(r, i, used) for i, r in enumerate(out["characters"][:N_SEATS])]
                if len(chars) != N_SEATS:
                    raise ValueError("need 4 characters")
                record["source"] = "llm"
                break
            except (ValueError, KeyError, TypeError) as e:
                record["errors"].append(f"attempt {attempt+1}: {e}")
                chars = None
    if chars is None:
        chars = from_templates(seed)
    record["characters"] = chars
    COHORT_DIR.mkdir(exist_ok=True)
    path.write_text(json.dumps(record, indent=1, ensure_ascii=False))
    return record


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate (or show) a cohort.")
    ap.add_argument("cohort_id")
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--backend", default="claude_cli", choices=["claude_cli", "scripted"])
    a = ap.parse_args()
    from llm import LLMClient, TokenMeter
    world = json.loads((HERE / "data" / "world.json").read_text())
    client = LLMClient(a.backend, cache_dir=None, run_id=a.cohort_id, run_meter=TokenMeter(None))
    rec = generate_cohort(a.cohort_id, a.seed, backend=a.backend, client=client, world=world)
    print(json.dumps({"cohort_id": rec["cohort_id"], "source": rec["source"], "errors": rec["errors"],
                      "characters": [(c["name"], c["concept"]) for c in rec["characters"]]}, indent=1))
