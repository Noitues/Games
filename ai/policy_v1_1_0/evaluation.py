"""Shared evaluation function for every scoring policy.

One function, one weight table. A policy changes behaviour by passing a weight
profile, not by getting its own evaluator (Prompts 4.C: keep the evaluation
mostly shared). Per-champion knowledge stays limited to the role hint table.
"""
from __future__ import annotations

from typing import Dict, Optional

from engine.hexmap import hex_distance
from engine.resolve import adjacent_units
from engine.state import GameState, other

# Baseline profile. Terms added in ai 1.1.0 default to 0 so that T1 behaves
# exactly as it did in ai 1.0.0 and batches stay comparable.
W = {
    "nexus_enemy": 9.0, "nexus_own": 7.0,
    "tower_enemy": 2.2, "tower_own": 1.6,
    "hp_own": 1.3, "hp_enemy": 1.3,
    "alive_own": 3.0, "alive_enemy": 3.0,
    "ap": 0.9,
    "wave_enemy": 0.55, "wave_own": 0.45,
    "wave_push": 0.30,
    "dragon": 9.0, "baron": 7.0,
    "monster_chip": 0.0,        # >0 rewards chipping a live monster down
    "incoming_own": 1.1, "incoming_enemy": 0.55,
    "death_risk": 7.0, "kill_chance": 6.0,
    "cooldown": 0.9,
    "lane": 0.16,
    "recall_ready": 0.5,
    # --- macro terms, off by default ---
    "objective_pull": 0.0,      # jungler drawn to a live Dragon or Baron
    "recall_value": 0.0,        # a hurt champion sitting in its own base
    "home_bias": 0.0,           # stay near the home Nexus (turtle)
    "enemy_cd": 0.0,            # enemy cards stuck on the cooldown track
    "struct_focus": 0.0,        # extra pull toward enemy structures
}

# Macro profile for T2: lane and jungle assignment, objective setups, recall
# timing. Weights only; the search does the planning.
T2_MACRO = dict(W, monster_chip=0.25, objective_pull=0.35, recall_value=2.0)

ROLE_LANE = {"Top": "top", "Mid": "mid", "ADC": "bot", "Support": "bot", "Jungle": None}
MAJOR = ("dragon", "baron")


def _lane_cost(state: GameState, c) -> float:
    lane = ROLE_LANE.get(c.role)
    board = state.board
    if lane is None:
        targets = [m.hexpos for m in state.monsters.values() if m.alive] or \
                  [h for hs in board.monsters.values() for h in hs]
    else:
        targets = board.lane_paths[c.team][lane]
    return min(hex_distance(c.hexpos, h) for h in targets)


def predicted_world_damage(state: GameState, c) -> int:
    """Hits this champion would take in the next World Phase (Rules 5.3)."""
    node = state.node_of_unit(c)
    dmg = 0
    armor = 1 if "cloth_armor" in c.items else 0
    for u in adjacent_units(state, node, exclude=c.uid):
        if u.kind == "structure" and u.stype == "tower" and u.team != c.team:
            dmg += state.config["tower_hits_champion"] - armor
        elif u.kind == "wave" and u.team != c.team:
            dmg += 1 - armor
        elif u.kind == "monster":
            dmg += state.config["monster_hits"] - armor
    return max(0, dmg)


def evaluate(state: GameState, team: str, w: Optional[Dict[str, float]] = None) -> float:
    w = w or W
    foe = other(team)
    board = state.board
    score = 0.0
    for s in state.structures.values():
        if not s.alive:
            score += (w["tower_enemy"] * 8 if s.team == foe else -w["tower_own"] * 8)
            continue
        if s.stype == "nexus":
            score += (-w["nexus_enemy"] * s.chips if s.team == foe else w["nexus_own"] * s.chips)
        else:
            score += (-w["tower_enemy"] * s.chips if s.team == foe else w["tower_own"] * s.chips)
    live_major = [m for m in state.monsters.values() if m.alive and m.mtype in MAJOR]
    home = board.nexus[team]
    for c in state.champs.values():
        own = c.team == team
        if not c.alive:
            score += -w["alive_own"] * 2 if own else w["alive_enemy"] * 2
            continue
        score += (w["hp_own"] * c.hp) if own else (-w["hp_enemy"] * c.hp)
        dmg = predicted_world_damage(state, c)
        if own:
            score -= w["incoming_own"] * dmg
            if dmg >= c.hp + c.shield:
                score -= w["death_risk"]
            score -= w["cooldown"] * c.track
            score -= w["lane"] * _lane_cost(state, c)
            if w["home_bias"]:
                score -= w["home_bias"] * hex_distance(c.hexpos, home)
            if w["objective_pull"] and c.role == "Jungle" and live_major:
                score -= w["objective_pull"] * min(hex_distance(c.hexpos, m.hexpos)
                                                   for m in live_major)
            if w["recall_value"] and c.hp <= 2 and \
                    board.tile_of[c.hexpos] == board.tile_of[board.fountain[team]]:
                score += w["recall_value"]
        else:
            score += w["incoming_enemy"] * dmg
            if dmg >= c.hp + c.shield:
                score += w["kill_chance"]
            if w["enemy_cd"]:
                score += w["enemy_cd"] * c.track
    for wave in state.waves.values():
        if wave.team == team:
            score += w["wave_own"] * wave.chips + w["wave_push"] * wave.path_idx
        else:
            score -= w["wave_enemy"] * wave.chips + w["wave_push"] * wave.path_idx
    ts, tf = state.teams[team], state.teams[foe]
    score += w["ap"] * ts.ap
    score += w["dragon"] * (ts.dragons - tf.dragons)
    score += w["baron"] * (min(1, ts.baron_track) - min(1, tf.baron_track))
    if w["monster_chip"]:
        for m in state.monsters.values():
            if m.alive:
                score -= w["monster_chip"] * m.chips * (2.0 if m.mtype in MAJOR else 1.0)
    if w["struct_focus"]:
        for c in state.champs.values():
            if c.team != team or not c.alive:
                continue
            targets = [s.hexpos for s in state.structures.values()
                       if s.team == foe and s.alive and s.stype == "tower"]
            if targets:
                score -= w["struct_focus"] * min(hex_distance(c.hexpos, h) for h in targets)
    return score
