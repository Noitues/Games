"""Interim rulings for spec gaps.

Every entry is a place where RULES_SPEC.md does not decide what the engine must do. The engine
calls ``Rulings.fire(id, detail)`` each time it actually relies on one of these, which records an
AMBIGUITY on the run. That way the analyst counts how often each gap is *hit*, not merely that it
exists. See docs/design_notes.md for the prose version.
"""

from __future__ import annotations

# AMB-02 and AMB-25 were resolved by spec 0.2.0 (§4 backstory guarantee) and no longer fire.
RULINGS: dict[str, dict[str, str]] = {
    "AMB-01": {"section": "brief", "issue": "Arm A lists 'Attention', which the spec never defines.",
               "interim_ruling": "Not modelled."},
    "AMB-02": {"section": "§4/§7", "issue": "Backstory guarantee needs 'the next Beat Frame', but frames are never forced.",
               "interim_ruling": "Pulled cards force a guarantee Beat Frame at the start of the next scene."},
    "AMB-03": {"section": "§4", "issue": "Does the session end after the climax scene?",
               "interim_ruling": "Yes: the climax scene is the last scene of the session."},
    "AMB-04": {"section": "§6", "issue": "Do tension adjustment rows stack?",
               "interim_ruling": "All applicable rows are summed, then clamped to 1-6."},
    "AMB-05": {"section": "§7/§6A", "issue": "Rail overflow with no non-GLOBAL GM card on the rail.",
               "interim_ruling": "Evict the oldest non-GLOBAL card of any kind."},
    "AMB-06": {"section": "§6", "issue": "Interrupt with no unused prepared Beat Frame.",
               "interim_ruling": "Engine picks an unused starter-library frame by seeded RNG."},
    "AMB-07": {"section": "§3/§4", "issue": "Tie draws a player card: is the minor cost the compel, or separate?",
               "interim_ruling": "The compel complication is the cost; on refusal the cost uses a face-up GM tag."},
    "AMB-08": {"section": "§3", "issue": "Major cost 'must use its weakness tag' overlaps the surfacing compel.",
               "interim_ruling": "Same as AMB-07: the compel is the cost."},
    "AMB-09": {"section": "§6/§4", "issue": "Altered-scene draw of a player card: does §4's compel apply?",
               "interim_ruling": "Yes, every Session Deck draw of a player card runs §4."},
    "AMB-10": {"section": "§9", "issue": "Growth from 'roll fails after one of its tags was invoked' — invoked by whom?",
               "interim_ruling": "Owner's own invokes only."},
    "AMB-11": {"section": "§3", "issue": "Timing of GM opposing tags/invokes is unspecified.",
               "interim_ruling": "GM commits before the roll; players invoke after seeing the dice."},
    "AMB-12": {"section": "§8", "issue": "Stress box values are unspecified.",
               "interim_ruling": "Fate Core: boxes 1 and 2; Physique/Will +1/+2 adds a 3 box, +3 or more adds 3 and 4."},
    "AMB-14": {"section": "§5/§7", "issue": "Who decides a beat 'went badly' for its stakes clock?",
               "interim_ruling": "GM agent reports it at scene end; the Referee audits it."},
    "AMB-15": {"section": "§3", "issue": "Hostile-invoke fate point when the session ends first.",
               "interim_ruling": "Paid at the end of that scene, including the final scene."},
    "AMB-16": {"section": "§4", "issue": "A draw is required but the deck is empty outside a climax.",
               "interim_ruling": "The cost uses a face-up GM tag, as in a climax."},
    "AMB-17": {"section": "§7", "issue": "Fictional triggers cannot be confirmed from the mechanical log.",
               "interim_ruling": "GM agent reports fictional triggers; the Referee audits them."},
    "AMB-18": {"section": "§5", "issue": "A GM card drawn for a Beat Frame blank has no 'cost' to build.",
               "interim_ruling": "The GM must use one of its tags in the filled blank."},
    "AMB-19": {"section": "§3", "issue": "Tie on an attack: 'success at minor cost' but 0 shifts of harm.",
               "interim_ruling": "Attacker gets a boost (Fate Core) and the deck draw still happens."},
    "AMB-20": {"section": "§4 vs §6", "issue": "§6 Altered scene draws a card, but §4's closed list of draw triggers omits it.",
               "interim_ruling": "§6 is more specific: Altered scenes draw."},
    "AMB-21": {"section": "§4/§6", "issue": "Is an Interrupt a draw in itself, or only via its Beat Frame's draws?",
               "interim_ruling": "Only the Beat Frame's per-blank draws happen; no extra interrupt draw."},
    "AMB-22": {"section": "§3/§7", "issue": "Does a GLOBAL anchor give the GM a free invoke like a GM card?",
               "interim_ruling": "Yes, GLOBAL cards placed on the rail give the GM 1 free invoke that scene."},
    "AMB-23": {"section": "§3", "issue": "Success at major cost on an attack: how much harm lands?",
               "interim_ruling": "The attack lands for 1 shift."},
    "AMB-24": {"section": "§7", "issue": "A clock fills mid-scene: when does its Beat Frame happen?",
               "interim_ruling": "It is queued for the start of the next scene."},
    "AMB-25": {"section": "§4", "issue": "Backstory guarantee pulled a card but no scene remains.",
               "interim_ruling": "Guarantee fails and is recorded; nothing is invented."},
    "AMB-27": {"section": "§3", "issue": "Success with style on create advantage: the aspect's 2 free invokes AND the deck peek, or one of them?",
               "interim_ruling": "Both: the aspect keeps 2 free invokes and the player may also peek."},
    "AMB-26": {"section": "§5", "issue": "Several Beat Frames are queued for the same scene.",
               "interim_ruling": "One per scene; the guarantee frame first, the rest carry to later scenes."},
}


class Rulings:
    def __init__(self) -> None:
        self.fired: list[dict] = []

    def fire(self, rid: str, detail: str = "", scene: int | None = None) -> None:
        base = RULINGS[rid]
        self.fired.append({"id": rid, "section": base["section"], "issue": base["issue"],
                           "interim_ruling": base["interim_ruling"], "detail": detail,
                           "scene": scene, "source": "engine"})
