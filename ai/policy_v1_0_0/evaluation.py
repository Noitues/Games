"""Shared evaluation function for the scoring policies.

Weights are deliberately shared across every champion; per-champion knowledge
is limited to the small role hint table below (Prompts Part 4.C).
"""
from __future__ import annotations

from typing import Dict

from engine.hexmap import hex_distance
from engine.state import GameState, other

W = {
    "nexus_enemy": 9.0, "nexus_own": 7.0,
    "tower_enemy": 2.2, "tower_own": 1.6,
    "hp_own": 1.3, "hp_enemy": 1.3,
    "alive_own": 3.0, "alive_enemy": 3.0,
    "ap": 0.9,
    "wave_enemy": 0.55, "wave_own": 0.45,
    "wave_push": 0.30,
    "dragon": 9.0, "baron": 7.0,
    "monster_chip": 0.35,
    "incoming_own": 1.1, "incoming_enemy": 0.55,
    "death_risk": 7.0, "kill_chance": 6.0,
    "cooldown": 0.9,
    "lane": 0.16,
    "recall_ready": 0.5,
}

ROLE_LANE = {"Top": "top", "Mid": "mid", "ADC": "bot", "Support": "bot", "Jungle": None}


def _lane_cost(state: GameState, c) -> float:
    lane = ROLE_LANE.get(c.role)
    board = state.board
    if lane is None:
        targets = [h for hs in board.monsters.values() for h in hs]
    else:
        targets = board.lane_paths[c.team][lane]
    return min(hex_distance(c.hexpos, h) for h in targets)


def predicted_world_damage(state: GameState, c) -> int:
    """Hits this champion would take in the next World Phase (Rules 5.3)."""
    from engine.resolve import adjacent_units
    node = state.node_of_unit(c)
    dmg = 0
    for u in adjacent_units(state, node, exclude=c.uid):
        if u.kind == "structure" and u.stype == "tower" and u.team != c.team:
            dmg += state.config["tower_hits_champion"] - (1 if "cloth_armor" in c.items else 0)
        elif u.kind == "wave" and u.team != c.team:
            dmg += 1 - (1 if "cloth_armor" in c.items else 0)
        elif u.kind == "monster":
            dmg += state.config["monster_hits"] - (1 if "cloth_armor" in c.items else 0)
    return max(0, dmg)


def evaluate(state: GameState, team: str) -> float:
    foe = other(team)
    score = 0.0
    for s in state.structures.values():
        if not s.alive:
            score += (W["tower_enemy"] * 8 if s.team == foe else -W["tower_own"] * 8)
            continue
        if s.stype == "nexus":
            score += (-W["nexus_enemy"] * s.chips if s.team == foe
                      else W["nexus_own"] * s.chips)
        else:
            score += (-W["tower_enemy"] * s.chips if s.team == foe
                      else W["tower_own"] * s.chips)
    for c in state.champs.values():
        own = c.team == team
        if not c.alive:
            score += -W["alive_own"] * 2 if own else W["alive_enemy"] * 2
            continue
        score += (W["hp_own"] * c.hp) if own else (-W["hp_enemy"] * c.hp)
        dmg = predicted_world_damage(state, c)
        if own:
            score -= W["incoming_own"] * dmg
            if dmg >= c.hp + c.shield:
                score -= W["death_risk"]
            score -= W["cooldown"] * c.track
            score -= W["lane"] * _lane_cost(state, c)
        else:
            score += W["incoming_enemy"] * dmg
            if dmg >= c.hp + c.shield:
                score += W["kill_chance"]
    for w in state.waves.values():
        if w.team == team:
            score += W["wave_own"] * w.chips + W["wave_push"] * w.path_idx
        else:
            score -= W["wave_enemy"] * w.chips + W["wave_push"] * w.path_idx
    ts, tf = state.teams[team], state.teams[foe]
    score += W["ap"] * ts.ap
    score += W["dragon"] * (ts.dragons - tf.dragons)
    score += W["baron"] * (min(1, ts.baron_track) - min(1, tf.baron_track))
    for m in state.monsters.values():
        if m.alive and m.mtype in ("dragon", "baron"):
            score -= W["monster_chip"] * m.chips * 0.0     # value comes from the kill
    return score
