"""Agent roles: what each one sees, what it is asked, and the JSON it must return.

Visibility is enforced by construction: every prompt is assembled here from only the pieces its
role may see (see the roster in docs/harness_prompt.md). ``leak_check`` greps player-facing text
for words that would reveal the evaluation.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from llm import LLMClient, dice_claims

HERE = Path(__file__).parent
PROMPTS = HERE / "prompts"
SPEC_PATH = HERE.parent / "RULES_SPEC.md"

PERSONALITIES = {
    "optimizer": ("Optimizer", "You play to win the mechanics. You hoard fate points and spend them "
                  "efficiently, invoke whenever it changes an outcome, and argue for every mechanical advantage."),
    "storyteller": ("Storyteller", "You love the fiction. You elaborate scenes, invent vivid detail about "
                    "your character's past, and answer the GM's questions at length."),
    "protector": ("Protector", "You put the other characters' safety ahead of your own goals. You step "
                  "into danger for them and usually accept compels that protect someone."),
    "rules_lawyer": ("Rules lawyer", "You know the rules well and hold the GM to them. You refuse compels "
                     "whenever you can afford to, and you look for loopholes and unclear rulings."),
    "instigator": ("Instigator", "You escalate. You attack problems head-on, pick fights, and create trouble "
                   "when things get slow."),
    "lurker": ("Lurker", "You are quiet at the table. You rarely speak up and usually pass your turn unless "
               "the GM or another player addresses your character by name. When addressed, you answer briefly."),
    "tactician": ("Tactician", "You plan. You scout, gather information, and set up advantages before "
                  "committing to risky actions."),
    "method_actor": ("Method actor", "You stay in character at all times, even when it hurts your character's "
                     "interests. You make the choice your character would make, not the smart one."),
}
PERSONALITY_ORDER = ["optimizer", "storyteller", "protector", "rules_lawyer", "instigator", "lurker",
                     "tactician", "method_actor"]

BANNED_FOR_PLAYERS = ["playtest", "placebo", "baseline", "experiment", "metric", "metrics", "arm a", "arm b",
                      "arm c", "hypothesis", "design goal", "design goals", "scene-deck engine", "rules spec"]
_BANNED_RE = re.compile(r"(?<![a-z])(" + "|".join(re.escape(w) for w in BANNED_FOR_PLAYERS) + r")(?![a-z])", re.I)


def redact(text: str) -> str:
    """Remove evaluation vocabulary from agent-written fiction before a player sees it."""
    return _BANNED_RE.sub("[…]", text)

NO_DICE = ("The dice are rolled for you by the table. Never state dice faces, roll totals or numbers "
           "from a roll; describe only what your character does and says.")


# ------------------------------------------------------------------ JSON schema helpers
def S(t, **kw):
    return {"type": t, **kw}


def OBJ(props: dict, req: list[str] | None = None) -> dict:
    return {"type": "object", "properties": props, "required": req or [], "additionalProperties": False}


def ARR(item) -> dict:
    return {"type": "array", "items": item}


STR = S("string")
INT = S("integer")
BOOL = S("boolean")
TAGREF = OBJ({"card_id": STR, "tag": STR}, ["card_id", "tag"])
NPC_DEF = OBJ({"name": STR, "rating": INT, "stress": INT, "hostile": BOOL, "card_id": STR},
              ["name", "rating", "hostile"])
STORY_CARD = OBJ({"type": S("string", enum=["NPC", "THREAD"]), "title": STR, "power_tags": ARR(STR),
                  "weakness": STR, "pile": STR}, ["type", "title", "power_tags", "weakness"])

SCHEMAS = {
    "gm_frame": OBJ({"planned_scene": STR, "narration": STR, "central_question": STR,
                     "npcs": ARR(NPC_DEF), "address": ARR(STR), "used_card": TAGREF},
                    ["planned_scene", "narration", "central_question", "npcs", "address"]),
    "gm_beat_fill": OBJ({"fills": ARR(OBJ({"blank": STR, "card_id": STR, "tag_used": STR, "text": STR},
                                          ["blank", "card_id", "tag_used", "text"])),
                         "questions": ARR(OBJ({"player": STR, "card_id": STR, "question": STR},
                                              ["player", "card_id", "question"])),
                         "compels": ARR(OBJ({"card_id": STR, "player": STR, "tag_used": STR, "complication": STR,
                                             "refusal_cost": OBJ({"card_id": STR, "tag": STR, "text": STR},
                                                                 ["card_id", "tag", "text"])},
                                            ["card_id", "player", "tag_used", "complication", "refusal_cost"]))},
                        ["fills", "questions", "compels"]),
    "gm_adjudicate": OBJ({
        "rolls": ARR(OBJ({"player": STR, "needs_roll": BOOL, "opposing_tags": ARR(TAGREF), "npc": STR,
                          "gm_invokes": ARR(TAGREF),
                          "hostile_invokes": ARR(OBJ({"player": STR, "card_id": STR}, ["player", "card_id"])),
                          "target_card": STR}, ["player", "needs_roll", "opposing_tags"])),
        "npc_actions": ARR(OBJ({"npc": STR, "target": STR, "harm": S("string", enum=["physical", "mental"]),
                                "description": STR}, ["npc", "target", "harm", "description"])),
        "compels": ARR(OBJ({"player": STR, "card_id": STR, "tag": STR, "complication": STR},
                           ["player", "tag", "complication"])),
    }, ["rolls", "npc_actions", "compels"]),
    "gm_costs": OBJ({"items": ARR(OBJ({"event_id": INT, "card_id": STR, "tag_used": STR, "text": STR,
                                       "refusal_cost": OBJ({"card_id": STR, "tag": STR, "text": STR},
                                                           ["card_id", "tag", "text"])},
                                      ["event_id", "card_id", "tag_used", "text"]))}, ["items"]),
    "gm_narrate": OBJ({"narration": STR, "scene_over": BOOL, "address": ARR(STR),
                       "end": OBJ({"fled_or_bypassed": ARR(STR), "resolved_threats": ARR(STR), "goal_filled": BOOL,
                                   "keep_on_rail": ARR(STR), "new_story_cards": ARR(STORY_CARD),
                                   "retire_story_cards": ARR(STR), "fiction_triggers_fired": ARR(STR),
                                   "beat_went_badly": BOOL})},
                      ["narration", "scene_over", "address"]),
    "gm_post": OBJ({"summary": STR, "threats_left_play": ARR(OBJ({"card_id": STR, "alive": BOOL, "new_tag": STR},
                                                                 ["card_id", "alive"]))}, ["summary", "threats_left_play"]),
    "write_story": OBJ({"type": S("string", enum=["NPC", "THREAD"]), "title": STR, "power_tags": ARR(STR),
                        "weakness": STR}, ["type", "title", "power_tags", "weakness"]),
    "player_declare": OBJ({"action": S("string", enum=["pass", "roleplay", "overcome", "create_advantage",
                                                       "attack", "concede"]),
                           "skill": STR, "target_card": STR, "target_npc": STR, "advantage_name": STR,
                           "description": STR, "speech": STR, "sacrifice_card": STR},
                          ["action", "description"]),
    "player_post_roll": OBJ({"invokes": ARR(OBJ({"source_id": STR, "tag": STR}, ["source_id", "tag"])),
                             "take_major_cost": BOOL, "use_story_ally": BOOL}, ["invokes", "take_major_cost"]),
    "player_compel": OBJ({"accept": BOOL, "speech": STR, "answer": STR}, ["accept"]),
    "player_answer": OBJ({"answer": STR}, ["answer"]),
    "player_absorb": OBJ({"option": INT, "consequence_text": STR, "strain_card_id": STR, "strain_tag": STR},
                         ["option"]),
    "player_peek": OBJ({"move_to_bottom": BOOL}, ["move_to_bottom"]),
    "survey": OBJ({"fun": INT, "involvement": INT, "connection": INT, "control": INT, "play_again": INT,
                   "best_moment": STR, "most_frustrating": STR, "background_used": STR, "wanted_but_couldnt": STR,
                   "one_sentence": STR},
                  ["fun", "involvement", "connection", "control", "play_again", "best_moment",
                   "most_frustrating", "background_used", "wanted_but_couldnt", "one_sentence"]),
    "preference": OBJ({"choice": S("string", enum=["1", "2"]), "reason": STR}, ["choice", "reason"]),
    "referee": OBJ({"violations": ARR(OBJ({"section": STR, "issue": STR, "event_id": INT}, ["section", "issue"])),
                    "ambiguities": ARR(OBJ({"section": STR, "issue": STR, "interim_ruling": STR},
                                           ["section", "issue", "interim_ruling"])),
                    "cost_checks": ARR(OBJ({"event_id": INT, "used_drawn_card": BOOL, "note": STR},
                                           ["event_id", "used_drawn_card"])),
                    "friction": ARR(STR)}, ["violations", "ambiguities", "cost_checks", "friction"]),
    "interviewer": OBJ({"players": ARR(OBJ({"name": STR, "turns": INT, "references_to_others_background": INT},
                                           ["name", "turns", "references_to_others_background"]))}, ["players"]),
    "judge": OBJ({"overall": INT, "engagement": INT, "coherence": INT, "spotlight_fairness": INT, "player_agency": INT,
                  "complication_quality": INT,
                  "backstory": ARR(OBJ({"name": STR, "used": BOOL, "score": INT, "note": STR}, ["name", "used", "score"])),
                  "best_moment": STR, "worst_moment": STR, "notes": STR},
                 ["overall", "engagement", "coherence", "spotlight_fairness", "player_agency", "complication_quality",
                  "backstory", "best_moment", "worst_moment", "notes"]),
    "analyst": OBJ({"conclusions": STR, "key_findings": ARR(STR), "caveats": ARR(STR)},
                   ["conclusions", "key_findings", "caveats"]),
    "chargen": OBJ({"characters": ARR(OBJ({
        "name": STR, "pronouns": STR, "concept": STR,
        "binder": ARR(OBJ({"type": STR, "title": STR, "power_tags": ARR(STR), "weakness": STR},
                          ["type", "title", "power_tags", "weakness"])),
        "story_cards": ARR(OBJ({"type": STR, "title": STR, "power_tags": ARR(STR), "weakness": STR},
                               ["type", "title", "power_tags", "weakness"])),
        "skills": OBJ({"great": STR, "good": ARR(STR), "fair": ARR(STR), "average": ARR(STR)},
                      ["great", "good", "fair", "average"]),
        "approaches": OBJ({"plus3": STR, "plus2": ARR(STR), "plus1": ARR(STR), "plus0": STR},
                          ["plus3", "plus2", "plus1", "plus0"]),
        "fae": OBJ({"high_concept": STR, "trouble": STR, "aspects": ARR(STR)}, ["high_concept", "trouble", "aspects"]),
    }, ["name", "pronouns", "concept", "binder", "story_cards", "skills", "approaches", "fae"]))}, ["characters"]),
}


def spec_for_agents() -> str:
    """The spec minus what no in-game agent needs: the sources table, §12 (this protocol) and §13
    (open questions). Cuts the GM/Referee system prompt by about a quarter."""
    text = SPEC_PATH.read_text()
    text = text.split("## 12. Agent playtest protocol")[0]
    a = text.find("**What each source contributes**")
    b = text.find("**Rules baseline:**")
    if a != -1 and b != -1:
        text = text[:a] + text[b:]
    return text


def load_prompt(name: str) -> str:
    return (PROMPTS / name).read_text()


def leak_check(text: str) -> list[str]:
    low = text.lower()
    return [w for w in BANNED_FOR_PLAYERS if re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", low)]


class DiceClaimError(Exception):
    pass


class Agent:
    """One seat at the table. Stateless between calls: its memory is the prompt we build."""

    def __init__(self, client: LLMClient, role: str, name: str, system: str, on_note=None):
        self.client = client
        self.role = role
        self.name = name
        self.system = system
        self.on_note = on_note or (lambda *a: None)

    def ask(self, kind: str, prompt: str, ctx: dict | None = None) -> dict:
        schema = SCHEMAS[kind]
        if self.role == "player":
            leaks = leak_check(self.system + "\n" + prompt)
            if leaks:
                raise AssertionError(f"prompt leak to player {self.name}: {leaks}")
        out = self.client.call(role=self.role, agent=self.name, kind=kind, system=self.system,
                               prompt=prompt, schema=schema, ctx=ctx)
        if self.role in ("player", "gm"):
            claims = dice_claims(out)
            if claims:
                self.on_note("dice_claim_retry", self.name, kind, claims[:2])
                out = self.client.call(role=self.role, agent=self.name, kind=kind, system=self.system,
                                       prompt=prompt + "\n\nIMPORTANT: your previous answer stated dice or roll "
                                       "numbers. Do not. " + NO_DICE, schema=schema, ctx=ctx)
                claims = dice_claims(out)
                if claims:
                    raise DiceClaimError(f"{self.name} ({kind}) described a roll result: {claims[0]!r}")
        return out


# ------------------------------------------------------------------ system prompts
def player_system(char: dict, personality: str, arm: dict, world_name: str) -> str:
    title, desc = PERSONALITIES[personality]
    rules = load_prompt(arm["rules_summary"])
    return (
        f"You are a player at a tabletop roleplaying game, playing the character {char['name']} "
        f"({char.get('pronouns', 'they/them')}) in a story set in {world_name}.\n\n"
        f"How you play: {desc}\n\n"
        f"{NO_DICE}\n\n"
        "Speak in first person for your character in 'speech' (one to three sentences), and put what your "
        "character does in 'description'. Use only card or aspect IDs that appear in what you are shown. "
        "Answer only with the JSON requested.\n\n"
        f"--- Rules you know ---\n{rules}"
    )


def gm_system(arm: dict, world: dict, prep_text: str) -> str:
    if arm["deck"]:
        rules = spec_for_agents()
        interface = load_prompt("gm_interface_AC.md")
    else:
        rules = load_prompt("gm_rules_B.md")
        interface = load_prompt("gm_interface_B.md")
    return (
        "You are the GM of a tabletop roleplaying game for four players. A software engine at the table "
        "owns every number: dice, fate points, the deck, clocks, tension and stress. You never roll, never "
        "state dice or totals, and never decide when a card is drawn. You make fictional and tactical choices "
        "only, through the JSON fields you are asked for. " + NO_DICE + "\n\n"
        f"--- How you talk to the engine ---\n{interface}\n\n"
        f"--- Setting: {world['name']} ---\n{world['setting']}\n\n"
        f"--- Your prep for this session ---\n{prep_text}\n\n"
        f"--- Rules ---\n{rules}"
    )


def referee_system(arm: dict) -> str:
    rules = spec_for_agents() if arm["deck"] else load_prompt("gm_rules_B.md")
    return (
        "You are the Referee. You check a game's mechanical event log against the rules below. You judge "
        "rules only, not the quality of the story. A software engine already enforced dice, fate point "
        "arithmetic and draw triggers; its refusals are listed separately. Your job: find rule VIOLATIONS "
        "the log shows (cite the section), AMBIGUITIES where the rules did not decide what should happen "
        "(cite the section and the interim ruling the table used), and for each deck-draw cost, whether "
        "the cost text actually used the drawn card's tags. Do not invent problems; an empty list is fine.\n\n"
        f"--- Rules ---\n{rules}"
    )


INTERVIEWER_SYSTEM = (
    "You read transcripts of tabletop roleplaying sessions and extract simple counts. You are precise "
    "and literal. Answer only with the JSON requested."
)

JUDGE_SYSTEM = (
    "You are an experienced tabletop roleplaying game designer judging the story of ONE recorded session. You "
    "see only what was said at the table. Judge the session on its own merits; do not guess how it was run or "
    "what rules produced it. Be calibrated: a 5 is an ordinary, competent session, and 9-10 is rare. Answer only "
    "with the JSON requested."
)

ANALYST_SYSTEM = (
    "You are a careful data analyst. You are given blinded aggregate results from sessions of a tabletop "
    "game played under three rule variants labelled Arm 1, Arm 2 and Arm 3. You do not know which label is "
    "which variant. Write conclusions that follow from the numbers only, state uncertainty plainly, and "
    "report negative or null results as clearly as positive ones."
)


def render_transcript(entries: list[dict], viewer: str | None, max_chars: int = 16000,
                      current_scene: int | None = None) -> str:
    """Viewer None = omniscient (GM/interviewer). With current_scene set (compact mode), earlier scenes
    keep only the GM's narration, trimmed, as a recap; the current scene is shown in full."""
    lines = []
    for e in entries:
        if viewer is not None and e["visible_to"] not in ("all", viewer):
            continue
        if e["kind"] == "private":
            continue
        if current_scene is not None and e["scene"] < current_scene:
            if e["speaker"] != "GM":
                continue
            body = e["text"] if viewer is None else redact(e["text"])
            lines.append(f"(S{e['scene']} recap) GM: {body[:350]}")
            continue
        tag = "" if e["kind"] != "mechanics" else "[table] "
        body = e["text"] if viewer is None else redact(e["text"])
        lines.append(f"(S{e['scene']}) {e['speaker']}: {tag}{body}")
    text = "\n".join(lines)
    if len(text) > max_chars:
        text = "…(earlier play omitted)…\n" + text[-max_chars:]
    return text or "(nothing yet)"


def j(x) -> str:
    return json.dumps(x, ensure_ascii=False, indent=1)
