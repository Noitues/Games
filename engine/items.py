"""Shop catalogue (Rules 12) and buff cards (Rules 11)."""
from __future__ import annotations

# Permanent stat boosts: one copy per champion (Rules 12 [DEFAULT]).
STAT_ITEMS = {
    "ruby_crystal":   {"cost": 4, "effect": "+2 max HP, heal 2"},
    "boots":          {"cost": 4, "effect": "+1 Speed (max 5)"},
    "vampiric_blade": {"cost": 5, "effect": "heal 1 per chip removed"},
    "cloth_armor":    {"cost": 5, "effect": "-1 hit from each World Phase source"},
    "long_sword":     {"cost": 6, "effect": "L0 deals 2 hits"},
    "longbow":        {"cost": 6, "effect": "+1 range on Q/W/E/R"},
    "ionian_charm":   {"cost": 8, "effect": "-1 cooldown (min 1)"},
}

# One-use cards held in the team's hand; at most 2 copies each (Rules 12).
CARD_ITEMS = {
    "swift_tonic":  {"cost": 1, "effect": "+2 Speed this activation"},
    "health_potion": {"cost": 2, "effect": "heal 3"},
    "control_ward": {"cost": 2, "effect": "pin a tile visible"},
    "frost_charm":  {"cost": 2, "effect": "-2 Speed on an enemy champion within 2"},
    "stopwatch":    {"cost": 3, "effect": "move a card 1 down the cooldown track"},
}

BUFF_CARDS = {
    "blue_buff": {"effect": "+2 AP"},
    "red_buff":  {"effect": "2 hits on one adjacent target"},
}

ALL_ITEMS = {**STAT_ITEMS, **CARD_ITEMS}
MAX_CARD_COPIES = 2


def cost(name: str) -> int:
    return ALL_ITEMS[name]["cost"]
