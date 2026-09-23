"""Tunable numbers. Everything here is a rulebook value or a pacing lever."""
from __future__ import annotations

import copy

DEFAULT_CONFIG = {
    "monsters": {
        "wolves":    {"hp": 3, "spawn": 1, "respawn": 3},
        "raptors":   {"hp": 3, "spawn": 1, "respawn": 3},
        "krugs":     {"hp": 3, "spawn": 1, "respawn": 3},
        "blue_buff": {"hp": 4, "spawn": 1, "respawn": 4},
        "red_buff":  {"hp": 4, "spawn": 1, "respawn": 4},
        "dragon":    {"hp": 8, "spawn": 3, "respawn": 4},
        "baron":     {"hp": 12, "spawn": 7, "respawn": 5},
    },
    "tower_hp": 11,     # P-0002: was 8; lengthens the siege into the 13-15 round target
    "nexus_hp": 12,
    "wave_chips": 3,
    "wave_chips_late": 4,
    "wave_growth_round": 7,
    # P-0003: a second growth step. Once champions fight (RQ-034) the siege
    # stalls and a tail of games reaches the round limit; escalating the waves
    # late closes those out without touching the median.
    "wave_chips_late2": 5,
    "wave_growth_round2": 13,
    "wave_spawn_odd_rounds_only": True,
    "wave_speed": 2,
    "baron_wave_bonus": 2,
    "ap_base": 3,
    "dragon_cap": 2,
    "tower_hits_champion": 2,
    "tower_hits_wave": 1,
    "monster_hits": 1,
    "round_limit": 20,
    # RQ-032: with concealment one-way, a champion can act out of a hidden
    # hexgroup without ever being reachable. Turning this on flips the
    # hexgroup face up for the round as soon as its occupant affects anything
    # outside it - you may hide, but shooting gives you away.
    "reveal_on_outward_effect": False,
    # RQ-036: an occupied hexgroup is revealed while an enemy champion stands
    # on an adjacent hex. Cover works at a distance, not at arm's length.
    "adjacency_reveal": True,
    # How close an enemy champion has to be to reveal an occupied hexgroup.
    # 1 is the rule as written (standing on the edge looks in). At 2 it matches
    # the reach cap from P-0007, so anything that can hit you can see you.
    "reveal_radius": 1,
    # RQ-034's ambush gate, retired by RQ-036 but kept switchable.
    "ambush_gate": False,
    # Enumeration caps (engine performance; reported under Anomalies).
    "enum": {"step_cap": 4, "plan_cap": 6, "max_dest": 18, "max_options": 220,
             "placement_cap": 6},
}


def make_config(**overrides) -> dict:
    cfg = copy.deepcopy(DEFAULT_CONFIG)
    for k, v in overrides.items():
        if isinstance(v, dict) and isinstance(cfg.get(k), dict):
            cfg[k].update(v)
        else:
            cfg[k] = v
    return cfg
