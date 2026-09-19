"""Single-game driver and per-game statistics."""
from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from .actions import PASS, Activation, CardPlay, Placement, Purchase
from .config import DEFAULT_CONFIG
from .game import (SNAKE, apply_activation, apply_card, apply_purchase,
                   assert_state, legal_activations, legal_card_plays,
                   legal_purchases, new_game, upkeep, world_phase)
from .hexmap import Board
from .state import GameState, TEAMS, other

ABILITY_KEYS = ("L0", "Q", "W", "E", "R")


@dataclass
class GameResult:
    winner: Optional[str] = None
    end_reason: str = ""
    rounds: int = 0
    seed: int = 0
    picks: Dict[str, List[str]] = field(default_factory=dict)
    first: str = "north"
    champ: Dict[str, dict] = field(default_factory=dict)
    team_ap_source: Dict[str, Dict[str, int]] = field(default_factory=dict)
    team_ap_spent: Dict[str, Dict[str, int]] = field(default_factory=dict)
    items: Dict[str, Dict[str, int]] = field(default_factory=dict)
    objectives: List[dict] = field(default_factory=list)
    first_tower: Optional[Tuple[int, str]] = None
    towers_down: Dict[str, int] = field(default_factory=dict)
    structure_hp_left: Dict[str, int] = field(default_factory=dict)
    anomalies: List[str] = field(default_factory=list)
    replay: Optional[List[dict]] = None
    decisions: int = 0
    options_seen: int = 0


class Game:
    def __init__(self, state: GameState, policies: Dict[str, object], seed: int = 0,
                 replay: bool = False, strict: bool = True):
        self.state = state
        self.policies = policies
        self.seed = seed
        self.replay = replay
        self.strict = strict
        self.record: Dict[str, object] = {}
        self._opp_seen: set = set()
        self.res = GameResult(seed=seed)

    # ------------------------------------------------------------- callbacks
    def placer(self, state: GameState, tile: int, champs, free):
        out = {}
        by_team: Dict[str, list] = {}
        for c in champs:
            by_team.setdefault(c.team, []).append(c)
        avail = list(free)
        for team, cs in by_team.items():
            pol = self.policies[team]
            cap = state.config["enum"]["placement_cap"]
            opts: List[Placement] = []
            for combo in itertools.permutations(avail, min(len(cs), len(avail))):
                opts.append(Placement(tuple((c.uid, h) for c, h in zip(cs, combo))))
                if len(opts) >= cap:
                    break
            if not opts:
                continue
            choice = pol.choose_flip_placement(state, {"tile": tile}, opts)
            for uid, h in choice.mapping:
                out[uid] = h
                if h in avail:
                    avail.remove(h)
        return out

    # ------------------------------------------------------------------- run
    def run(self) -> GameResult:
        st = self.state
        cfg = st.config
        self.res.picks = {t: [c.cid for c in st.champs.values() if c.team == t] for t in TEAMS}
        self.res.first = st.priority
        for c in st.champs.values():
            self.res.champ[c.uid] = {
                "cid": c.cid, "team": c.team, "role": c.role, "kills": 0, "deaths": 0,
                "ap": 0, "rounds_dead": 0, "rounds_cd": 0, "uses": {k: 0 for k in ABILITY_KEYS},
                "opp": {k: 0 for k in ABILITY_KEYS}, "items": [], "struct_dmg": 0,
            }
        sig_history: List[tuple] = []
        while st.winner is None and st.round < cfg["round_limit"]:
            upkeep(st, self)
            self._check(f"upkeep r{st.round}")
            for c in st.champs.values():
                if not c.alive:
                    self.res.champ[c.uid]["rounds_dead"] += 1
                elif c.track > 0:
                    self.res.champ[c.uid]["rounds_cd"] += 1
            self.action_phase()
            if st.winner is None:
                world_phase(st)
                st.refresh_visibility(allow_flip_back=True, placer=self.placer)
                self._check(f"world r{st.round}")
                self.shop_phase()
            sig = self._signature()
            sig_history.append(sig)
            if len(sig_history) >= 4 and len(set(sig_history[-4:])) == 1:
                st.note(f"stalemate: no chip/HP/structure change for 3 rounds (round {st.round})")
        if st.winner is None:
            st.winner, st.end_reason = self._tiebreak()
        self._finish()
        return self.res

    def action_phase(self) -> None:
        st = self.state
        p1 = st.priority
        order = [p1 if i == 0 else other(p1) for i in SNAKE]
        st.turn_order = order
        st.event("round", n=st.round, priority=p1,
                 ap={t: st.teams[t].ap for t in ("north", "south")})
        for slot, team in enumerate(order):
            st.turn_index = slot
            if st.winner is not None:
                return
            rec: Dict[str, object] = {}
            legal = legal_activations(st, team, rec)
            self.res.decisions += 1
            self.res.options_seen += len(legal)
            for triple in rec.get("opp", ()):    # type: ignore[union-attr]
                if triple in self._opp_seen:
                    continue
                self._opp_seen.add(triple)
                self.res.champ[triple[1]]["opp"][triple[2]] += 1
            act = self.policies[team].choose_activation(st, legal)
            if act is None or act.is_pass:
                continue
            if act not in legal:
                st.note("policy returned an option outside the legal list")
                if self.strict:
                    raise AssertionError("illegal activation")
                continue
            plays = legal_card_plays(st, act)
            play = self.policies[team].choose_card_play(st, act, plays) if plays else None
            if act.ability:
                self.res.champ[act.champ]["uses"][act.ability] += 1
            ap_before = st.teams[team].ap
            apply_activation(st, act, self)
            st.event("act", champ=act.champ, ability=act.ability, recall=act.recall,
                     dest=list(act.dest) if act.dest else None,
                     card=(play.card if play is not None else None),
                     ap=st.teams[team].ap - ap_before)
            if play is not None:
                apply_card(st, act, play)
            st.refresh_visibility(allow_flip_back=True, placer=self.placer)
            self._check(f"activation r{st.round}")

    def shop_phase(self) -> None:
        st = self.state
        for team in (st.priority, other(st.priority)):
            for _ in range(6):
                legal = legal_purchases(st, team)
                if not legal:
                    break
                buys = self.policies[team].choose_shop(st, legal)
                if not buys:
                    break
                progressed = False
                for p in buys:
                    if apply_purchase(st, team, p):
                        progressed = True
                if not progressed:
                    break

    # --------------------------------------------------------------- helpers
    def _signature(self) -> tuple:
        st = self.state
        return (
            sum(c.hp for c in st.champs.values() if c.alive),
            sum(s.chips for s in st.structures.values()),
            sum(w.chips for w in st.waves.values()),
            sum(m.chips for m in st.monsters.values()),
        )

    def _check(self, label: str) -> None:
        errs = assert_state(self.state)
        if errs:
            for e in errs:
                self.state.note(f"ILLEGAL[{label}]: {e}")
            if self.strict:
                raise AssertionError(f"{label}: {errs[:3]}")

    def _tiebreak(self) -> Tuple[Optional[str], str]:
        st = self.state
        lost = {t: st.teams[t].towers_lost for t in TEAMS}
        if lost["north"] != lost["south"]:
            return ("north" if lost["south"] > lost["north"] else "south", "round_limit_towers")
        hp = {t: sum(s.chips for s in st.structures.values() if s.team == t) for t in TEAMS}
        if hp["north"] != hp["south"]:
            return ("north" if hp["north"] > hp["south"] else "south", "round_limit_hp")
        kills = {t: st.teams[t].kills for t in TEAMS}
        if kills["north"] != kills["south"]:
            return ("north" if kills["north"] > kills["south"] else "south", "round_limit_kills")
        return (None, "round_limit_draw")

    def _finish(self) -> None:
        st = self.state
        self.res.rounds = st.round
        self.res.winner = st.winner
        self.res.end_reason = st.end_reason or "nexus"
        for c in st.champs.values():
            d = self.res.champ[c.uid]
            d.update(kills=c.kills, deaths=c.deaths, assists=c.assists, ap=c.ap_earned,
                     items=sorted(c.items), struct_dmg=c.dmg_to_structures)
        for t in TEAMS:
            self.res.team_ap_source[t] = dict(st.teams[t].ap_by_source)
            self.res.team_ap_spent[t] = dict(st.teams[t].ap_spent)
            self.res.items[t] = dict(st.teams[t].items_bought)
            self.res.towers_down[t] = st.teams[t].towers_lost
            self.res.structure_hp_left[t] = sum(s.chips for s in st.structures.values()
                                                if s.team == t)
        for ev in st.log:
            if ev["t"] == "monster_killed":
                self.res.objectives.append(ev)
            if ev["t"] == "structure_down" and self.res.first_tower is None:
                owner = "north" if ev["uid"].startswith("n_") else "south"
                self.res.first_tower = (ev["round"], other(owner))
        self.res.anomalies = list(st.anomalies)
        if self.replay:
            self.res.replay = list(st.log)
