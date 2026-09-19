"""T2_search: depth-limited look-ahead over the snake order (Prompts 4.C).

The search expands the most promising of its own activations, replies with a
cheap T1 model of the opponent, and evaluates the leaf. Two things keep it
inside a time budget:

* the root is prefiltered by the same greedy score T1 uses;
* every reply is generated with a tightened enumeration config, so the
  opponent model sees a coarse but representative option list.

Macro planning lives in the T2 weight profile (lane and jungle assignment,
objective pull, recall timing) rather than in bespoke code.
"""
from __future__ import annotations

import time
from typing import List, Optional, Tuple

from engine.game import apply_activation, legal_activations, world_phase
from engine.state import other

from .evaluation import T2_MACRO, evaluate
from .t1_greedy import SHADOW, T1Greedy

DEFAULTS = {
    "root_k": 6,              # own activations expanded at the root
    "plies": 2,               # 1 = greedy, 2 = + opponent reply, 3 = + our follow-up
    "time_budget_ms": 260,    # per decision
    "opp_enum": {"step_cap": 2, "plan_cap": 2, "max_dest": 6, "max_options": 40,
                 "placement_cap": 2},
    # Resolve the World Phase at the leaf instead of predicting it. Damage in
    # this game lands in the World Phase (Rules 5.3), so a leaf that has not
    # resolved it misreads every tower dive and minion trade.
    "leaf_world": False,
    "temp_scale": 1.0,        # <1 sharpens the softmax over searched values
}


class T2Search(T1Greedy):
    tier = "T2_search"
    weights = T2_MACRO

    def __init__(self, seed: int, temperature: float = 0.0, config=None):
        super().__init__(seed, temperature, config)
        cfg = dict(DEFAULTS)
        cfg.update({k: v for k, v in (config or {}).items() if k in DEFAULTS})
        self.search = cfg
        self.leaf_weights = dict(self.weights, incoming_own=0.0, incoming_enemy=0.0,
                                 death_risk=0.0, kill_chance=0.0)

    # ------------------------------------------------------------------ core
    def choose_activation(self, state, legal):
        options = [a for a in legal if not a.is_pass]
        if not options:
            return legal[-1]
        deadline = time.perf_counter() + self.search["time_budget_ms"] / 1000.0
        rough = sorted(((self.score_activation(state, a), i, a)
                        for i, a in enumerate(options)), key=lambda t: -t[0])
        top = rough[: self.search["root_k"]]
        scored: List[Tuple[float, object]] = []
        for rough_score, _, act in top:
            # A searched value sits on a different scale from a greedy one: it
            # already contains the opponent's best reply. Never mix the two in
            # one softmax - out of time simply means a smaller candidate set.
            if scored and time.perf_counter() > deadline:
                break
            child = state.clone()
            try:
                apply_activation(child, act, SHADOW)
                child.refresh_visibility(allow_flip_back=True, placer=SHADOW.placer)
            except Exception:
                continue
            scored.append((self._descend(child, 1, deadline), act))
        if not scored:
            return top[0][2] if top else legal[-1]
        # Passing is searched on the same scale as every other option.
        idle = state.clone()
        scored.append((self._descend(idle, 1, deadline) - 0.5, legal[-1]))
        return self._softmax_pick(scored)

    def _softmax_pick(self, scored):
        """Same softmax as T1, with an optional sharpening factor."""
        saved = self.temperature
        self.temperature = max(1e-6, saved * self.search["temp_scale"])
        try:
            return super()._softmax_pick(scored)
        finally:
            self.temperature = saved

    def leaf_value(self, state) -> float:
        if not self.search["leaf_world"]:
            return self.value(state)
        probe = state.clone()
        try:
            world_phase(probe)
        except Exception:
            return self.value(state)
        return evaluate(probe, self.team, self.leaf_weights)

    def _descend(self, state, ply: int, deadline: float) -> float:
        if ply >= self.search["plies"] or state.winner is not None \
                or time.perf_counter() > deadline:
            return self.leaf_value(state)
        actor = self._next_actor(state, ply)
        reply = self._model_reply(state, actor)
        if reply is None:
            return self.leaf_value(state)
        try:
            apply_activation(state, reply, SHADOW)
            state.refresh_visibility(allow_flip_back=True, placer=SHADOW.placer)
        except Exception:
            return self.leaf_value(state)
        return self._descend(state, ply + 1, deadline)

    def _next_actor(self, state, ply: int) -> str:
        """Who activates next, read from the snake order the engine publishes."""
        order = getattr(state, "turn_order", None)
        idx = getattr(state, "turn_index", None)
        if order and idx is not None and idx + ply < len(order):
            return order[idx + ply]
        return other(self.team) if ply % 2 == 1 else self.team

    def _model_reply(self, state, actor: str):
        """T1's choice for `actor`, on a coarse option list."""
        saved = state.config
        state.config = dict(saved, enum=self.search["opp_enum"])
        try:
            legal = legal_activations(state, actor)
            options = [a for a in legal if not a.is_pass]
            if not options:
                return None
            best, best_s = None, -1e18
            for a in options:
                probe = state.clone()
                try:
                    apply_activation(probe, a, SHADOW)
                except Exception:
                    continue
                s = evaluate(probe, actor, self.weights)
                if s > best_s:
                    best, best_s = a, s
            return best
        finally:
            state.config = saved
