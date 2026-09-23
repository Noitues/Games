"""ai 1.4.0 - a state machine over the 1.3.0 personalities (Handoff §9).

The five personalities in 1.3.0 are fixed for a whole game, which is not how
anyone plays. A team opens on lane discipline, groups when an objective is
up, sieges when it is ahead and wards when it is behind. This package makes
the team AI a machine whose **states are the personalities** and whose
**transitions read the game state**, re-evaluated once per round at the
first decision after Upkeep (never mid-round: switching appetite between
activations makes the snake order incoherent and the logs unreadable).

A machine is data, not code, so it can be bred:

    {"name": "SM_g1_map", "default": "laner", "commit": 3,
     "rules": [{"if": [["tower_diff", ">=", 1]], "then": "sieger"},
               {"if": [["tower_diff", "<=", -1]], "then": "warder"}]}

Rules are tried in order and the first whose conditions all hold names the
state; none holding means `default`. `commit` locks a state for that many
rounds once entered, which is the hysteresis that stops a machine flapping.
Every signal a rule may read is listed in `SIGNALS`, computed by `signals()`
from `GameState` and the policy's own short memory of deaths.

Candidates live in `machines/*.json`, one file per generation, and register
as tiers so a batch draws them the way it draws personalities. Each machine
records which state it occupied each round in `occupancy`, and the batch
runner copies that into the game result so a report can say what a winning
machine actually did.

ai 1.3.0 stays exactly as batches 0036-0040 ran it.
"""
from __future__ import annotations

import glob
import json
import operator
import os
from typing import Dict, List, Tuple

from ai.policy_v1_3_0 import (  # noqa: F401
    BASE_T2, EXPLOITS, PERSONALITIES, PERSONALITY_POOL, Policy, T0Random, T1Greedy,
    T2Search, TIERS as _TIERS_1_3_0,
)
from ai.policy_v1_2_0 import T2Search as _T2Calibrated
from engine.state import other

OPS = {">=": operator.ge, "<=": operator.le, ">": operator.gt, "<": operator.lt,
       "==": operator.eq, "!=": operator.ne}

#: Everything a transition may read, with what it means. Kept flat and
#: numeric so a breeder can mutate thresholds without knowing the game.
SIGNALS = {
    "round": "round number",
    "towers_own_lost": "own towers destroyed", "towers_enemy_lost": "enemy towers destroyed",
    "tower_diff": "enemy towers lost minus own towers lost (positive = ahead on the map)",
    "towers_own_standing": "own towers alive", "towers_enemy_standing": "enemy towers alive",
    "nexus_own_hp": "chips left on own Nexus", "nexus_enemy_hp": "chips left on enemy Nexus",
    "alive_own": "own champions alive", "alive_enemy": "enemy champions alive",
    "alive_diff": "alive_own minus alive_enemy",
    "hp_own": "HP pool of own living champions", "hp_enemy": "HP pool of enemy living champions",
    "hp_diff": "hp_own minus hp_enemy",
    "dragons_own": "Dragon cards held", "dragons_enemy": "Dragon cards the enemy holds",
    "baron_own": "1 while own Baron card is on the track", "baron_enemy": "the same for the enemy",
    "dragon_up": "1 if Dragon is alive or appears by next round", "baron_up": "the same for Baron",
    "objective_up": "1 if either is",
    "ap_rate_own": "own AP earned per round so far", "ap_rate_enemy": "the same for the enemy",
    "ap_diff": "ap_rate_own minus ap_rate_enemy",
    "kills_own": "own champion kills so far", "kills_enemy": "enemy champion kills so far",
    "deaths_own_recent": "own champion deaths in the last two rounds",
    "deaths_enemy_recent": "enemy champion deaths in the last two rounds",
    "fight_won": "deaths_enemy_recent minus deaths_own_recent",
}

MEMORY_ROUNDS = 2


def signals(state, team: str, memory: List[Tuple[int, int, int]] | None = None) -> Dict[str, float]:
    """The flat view of the game a machine transitions on. `memory` is the
    policy's list of (round, own_deaths, enemy_deaths) from earlier rounds."""
    enemy = other(team)
    own, opp = state.teams[team], state.teams[enemy]
    r = state.round
    champs = list(state.champs.values())
    alive_own = sum(1 for c in champs if c.team == team and c.alive)
    alive_enemy = sum(1 for c in champs if c.team == enemy and c.alive)
    hp_own = sum(c.hp for c in champs if c.team == team and c.alive)
    hp_enemy = sum(c.hp for c in champs if c.team == enemy and c.alive)
    deaths_own = sum(c.deaths for c in champs if c.team == team)
    deaths_enemy = sum(c.deaths for c in champs if c.team == enemy)
    structs = list(state.structures.values())
    towers_own = sum(1 for s in structs if s.stype == "tower" and s.team == team and s.alive)
    towers_enemy = sum(1 for s in structs if s.stype == "tower" and s.team == enemy and s.alive)
    nexus = {s.team: s.chips for s in structs if s.stype == "nexus"}

    def up(mtype: str) -> int:
        for m in state.monsters.values():
            if m.mtype == mtype:
                return int(m.alive or m.respawn_round <= r + 1)
        return 0

    dragon_up, baron_up = up("dragon"), up("baron")
    ap_own = sum(own.ap_by_source.values()) / max(1, r)
    ap_enemy = sum(opp.ap_by_source.values()) / max(1, r)
    past = [m for m in (memory or []) if m[0] <= r - MEMORY_ROUNDS]
    base_own, base_enemy = (past[-1][1], past[-1][2]) if past else (0, 0)
    d_own, d_enemy = deaths_own - base_own, deaths_enemy - base_enemy
    return {
        "round": r,
        "towers_own_lost": own.towers_lost, "towers_enemy_lost": opp.towers_lost,
        "tower_diff": opp.towers_lost - own.towers_lost,
        "towers_own_standing": towers_own, "towers_enemy_standing": towers_enemy,
        "nexus_own_hp": nexus.get(team, 0), "nexus_enemy_hp": nexus.get(enemy, 0),
        "alive_own": alive_own, "alive_enemy": alive_enemy, "alive_diff": alive_own - alive_enemy,
        "hp_own": hp_own, "hp_enemy": hp_enemy, "hp_diff": hp_own - hp_enemy,
        "dragons_own": own.dragons, "dragons_enemy": opp.dragons,
        "baron_own": int(own.baron_track > 0), "baron_enemy": int(opp.baron_track > 0),
        "dragon_up": dragon_up, "baron_up": baron_up, "objective_up": int(dragon_up or baron_up),
        "ap_rate_own": ap_own, "ap_rate_enemy": ap_enemy, "ap_diff": ap_own - ap_enemy,
        "kills_own": own.kills, "kills_enemy": opp.kills,
        "deaths_own_recent": d_own, "deaths_enemy_recent": d_enemy, "fight_won": d_enemy - d_own,
    }


def validate_machine(spec: dict) -> dict:
    """Fail loudly at import on a typo, not quietly in game 300 of a batch."""
    name = spec.get("name")
    if not name or not name.startswith("SM_"):
        raise ValueError(f"machine name must start with SM_: {name!r}")
    states = set(spec.get("states") or PERSONALITIES)
    unknown = states - set(PERSONALITIES)
    if unknown:
        raise ValueError(f"{name}: unknown states {sorted(unknown)}")
    if spec.get("default") not in states:
        raise ValueError(f"{name}: default {spec.get('default')!r} not in states")
    if int(spec.get("commit", 0)) < 0:
        raise ValueError(f"{name}: commit must be >= 0")
    for rule in spec.get("rules", []):
        if rule.get("then") not in states:
            raise ValueError(f"{name}: rule targets unknown state {rule.get('then')!r}")
        for cond in rule.get("if", []):
            sig, op, _ = cond
            if sig not in SIGNALS:
                raise ValueError(f"{name}: unknown signal {sig!r}")
            if op not in OPS:
                raise ValueError(f"{name}: unknown operator {op!r}")
    return spec


def next_state(spec: dict, sig: Dict[str, float], current: str, committed_until: int,
               rnd: int) -> str:
    """The pure transition: which state the machine should be in this round."""
    if rnd < committed_until:
        return current
    for rule in spec.get("rules", []):
        if all(OPS[op](sig[s], v) for s, op, v in rule.get("if", [])):
            return rule["then"]
    return spec["default"]


class StateMachine(_T2Calibrated):
    """A T2 search whose evaluation weights are a personality chosen per round."""
    tier = "SM"
    machine: dict = {"name": "SM", "default": "laner", "commit": 0, "rules": []}
    weights = BASE_T2

    def __init__(self, seed: int, temperature: float = 0.0, config=None):
        super().__init__(seed, temperature, config)
        self.state_name = self.machine["default"]
        self._last_round = -1
        self._committed_until = -1
        self.occupancy: List[Tuple[int, str]] = []
        self._memory: List[Tuple[int, int, int]] = []
        self._apply(self.state_name)

    # The personality's whole profile, including its card prices and shop
    # order, becomes this policy's weights; an explicit config still wins.
    def _apply(self, name: str) -> None:
        profile = dict(PERSONALITIES[name])
        profile.update((self.config or {}).get("weights", {}))
        self.weights = profile
        self.leaf_weights = dict(profile, incoming_own=0.0, incoming_enemy=0.0,
                                 death_risk=0.0, kill_chance=0.0)

    def _tick(self, state) -> None:
        if state.shadow or state.round == self._last_round:
            return
        self._last_round = state.round
        sig = signals(state, self.team, self._memory)
        champs = state.champs.values()
        self._memory.append((state.round,
                             sum(c.deaths for c in champs if c.team == self.team),
                             sum(c.deaths for c in champs if c.team != self.team)))
        new = next_state(self.machine, sig, self.state_name, self._committed_until, state.round)
        if new != self.state_name:
            self.state_name = new
            self._apply(new)
            self._committed_until = state.round + int(self.machine.get("commit", 0))
        self.occupancy.append((state.round, self.state_name))

    def choose_activation(self, state, legal):
        self._tick(state)
        return super().choose_activation(state, legal)

    def choose_flip_placement(self, state, event, legal):
        self._tick(state)
        return super().choose_flip_placement(state, event, legal)

    def choose_card_play(self, state, activation, legal):
        self._tick(state)
        return super().choose_card_play(state, activation, legal)

    def choose_shop(self, state, legal):
        self._tick(state)
        return super().choose_shop(state, legal)


def machine_class(spec: dict):
    spec = validate_machine(spec)

    class Machine(StateMachine):
        machine = spec
        tier = spec["name"]

    Machine.__name__ = spec["name"]
    Machine.__qualname__ = spec["name"]
    return Machine


MACHINE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "machines")


def load_machines(path: str = MACHINE_DIR) -> Dict[str, dict]:
    out: Dict[str, dict] = {}
    for fn in sorted(glob.glob(os.path.join(path, "*.json"))):
        with open(fn) as fh:
            for spec in json.load(fh):
                spec = validate_machine(spec)
                if spec["name"] in out:
                    raise ValueError(f"duplicate machine name {spec['name']} in {fn}")
                out[spec["name"]] = spec
    return out


MACHINES = load_machines()

TIERS = dict(_TIERS_1_3_0)
TIERS.update({name: machine_class(spec) for name, spec in MACHINES.items()})

#: The machines a generation file defines, by generation prefix (SM_g1_...).
def generation(prefix: str) -> Tuple[str, ...]:
    return tuple(n for n in MACHINES if n.startswith(f"SM_{prefix}_"))


def make(tier: str, seed: int, temperature: float = 0.3, config: dict | None = None,
         team: str = "north"):
    cls = TIERS[tier]
    pol = cls(seed=seed, temperature=temperature, config=config or {})
    pol.team = team
    return pol
