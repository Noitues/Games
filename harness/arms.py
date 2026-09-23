"""Rule variants ("arms"). An arm is a flat dict of switches the engine and orchestrator read.

ARM_A — Scene-Deck: the full RULES_SPEC.md.
ARM_B — Baseline Fate: FAE-shaped characters (high concept, trouble, 3 aspects), no deck, no
        tension, no story piles, no clocks; the GM improvises complications freely.
ARM_C — Placebo: identical to A, but every "player" card in the deck and every player story pile
        card is a generic complication from harness/data/placebo.json.

Variants for spec §13 are built with ``variant(base, **overrides)``.
"""

from __future__ import annotations

ARM_A = {
    "arm": "A", "label": "Scene-Deck",
    "cards": True, "deck": True, "placebo": False, "tension": True, "story_piles": True,
    "clocks": True, "beat_frames": True, "growth": True,
    "resolution": "core_skills", "tension_rule": "invokes_vs_compels",   # spec 0.3.0 §6
    "gm_fp_per_player": 1, "gm_fp_flat": None, "max_passive": 4, "surface_free_invokes": 1,
    "attention_listed": True,   # the brief's Arm A mentions "Attention" (AMB-01)
    "rules_summary": "player_rules_AC.md",
}

ARM_B = {
    "arm": "B", "label": "Baseline Fate",
    "cards": False, "deck": False, "placebo": False, "tension": False, "story_piles": False,
    "clocks": False, "beat_frames": False, "growth": False,
    "resolution": "core_skills",   # see docs/design_notes.md: B_FAE switches to approaches
    "gm_fp_per_player": 1, "gm_fp_flat": None, "max_passive": 4, "surface_free_invokes": 0,
    "attention_listed": False,
    "rules_summary": "player_rules_B.md",
}

ARM_C = {**ARM_A, "arm": "C", "label": "Placebo", "placebo": True}

ARMS = {"A": ARM_A, "B": ARM_B, "C": ARM_C}


def variant(base: dict, name: str, **overrides) -> dict:
    v = {**base, **overrides}
    v["arm"] = f"{base['arm']}:{name}"
    return v


VARIANTS = {
    "B_FAE": variant(ARM_B, "FAE", resolution="fae"),
    "A_surface2": variant(ARM_A, "surface2", surface_free_invokes=2),
    "A_surface0": variant(ARM_A, "surface0", surface_free_invokes=0),
    "A_gmfp_flat2": variant(ARM_A, "gmfp_flat2", gm_fp_flat=2),
    "A_passive5": variant(ARM_A, "passive5", max_passive=5),
    "A_tension_v01": variant(ARM_A, "tension_v01", tension_rule="spec_0_1"),   # the old §6 table
}


def get_arm(key: str) -> dict:
    if key in ARMS:
        return dict(ARMS[key])
    if key in VARIANTS:
        return dict(VARIANTS[key])
    raise KeyError(f"unknown arm {key}")
