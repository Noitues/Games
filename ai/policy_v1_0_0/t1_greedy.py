"""T1_greedy: scores every legal activation with the shared evaluation
function and picks among the best with a softmax (Prompts Part 4.C)."""
from __future__ import annotations

import math
from typing import List

from engine.game import apply_activation, apply_card
from engine.state import other

from .base import Policy
from .evaluation import evaluate

SHOP_PRIORITY = {
    "Top":     ["ruby_crystal", "long_sword", "cloth_armor", "vampiric_blade", "ionian_charm", "boots"],
    "Jungle":  ["long_sword", "ruby_crystal", "vampiric_blade", "boots", "ionian_charm", "cloth_armor"],
    "Mid":     ["longbow", "ionian_charm", "ruby_crystal", "long_sword", "boots", "cloth_armor"],
    "ADC":     ["long_sword", "longbow", "vampiric_blade", "ruby_crystal", "boots", "ionian_charm"],
    "Support": ["longbow", "ruby_crystal", "boots", "cloth_armor", "ionian_charm", "vampiric_blade"],
}
CARD_VALUE = {"health_potion": 1.0, "stopwatch": 1.4, "control_ward": 0.8,
              "frost_charm": 0.7, "swift_tonic": 0.5}


class _ShadowGame:
    """Stand-in for Game during look-ahead: placements are taken as given."""

    def placer(self, state, tile, champs, free):
        out = {}
        avail = list(free)
        for c in champs:
            if c.hexpos in avail:
                avail.remove(c.hexpos)
                out[c.uid] = c.hexpos
            elif avail:
                out[c.uid] = avail.pop(0)
        return out


SHADOW = _ShadowGame()


class T1Greedy(Policy):
    tier = "T1_greedy"

    def score_activation(self, state, act) -> float:
        s = state.clone()
        try:
            apply_activation(s, act, SHADOW)
            s.refresh_visibility(allow_flip_back=True, placer=SHADOW.placer)
        except Exception:
            return -1e9
        return evaluate(s, self.team)

    def choose_activation(self, state, legal):
        options = [a for a in legal if not a.is_pass]
        if not options:
            return legal[-1]
        scored = [(self.score_activation(state, a), a) for a in options]
        base = evaluate(state, self.team)
        scored.append((base - 0.5, legal[-1]))          # passing is rarely right
        return self._softmax_pick(scored)

    def _softmax_pick(self, scored):
        best = max(s for s, _ in scored)
        t = max(1e-6, self.temperature)
        weights = []
        for s, a in scored:
            weights.append(math.exp(max(-40.0, (s - best) / (t * 6.0))))
        total = sum(weights)
        r = self.rng.random() * total
        acc = 0.0
        for (s, a), w in zip(scored, weights):
            acc += w
            if r <= acc:
                return a
        return scored[0][1]

    def choose_card_play(self, state, activation, legal):
        if not legal:
            return None
        best, best_s = None, 0.0
        for play in legal:
            s = state.clone()
            try:
                apply_activation(s, activation, SHADOW)
                before = evaluate(s, self.team)
                apply_card(s, activation, play)
                gain = evaluate(s, self.team) - before
            except Exception:
                continue
            gain -= CARD_VALUE.get(play.card, 0.0)      # keep cards for later
            if gain > best_s:
                best, best_s = play, gain
        return best

    def choose_shop(self, state, legal):
        ts = state.teams[self.team]
        champs = {c.uid: c for c in state.champs.values() if c.team == self.team}
        best = None
        best_key = None
        for p in legal:
            if p.champ is not None:
                c = champs.get(p.champ)
                if c is None:
                    continue
                prio = SHOP_PRIORITY[c.role]
                if p.item not in prio:
                    continue
                key = (0, prio.index(p.item), c.uid)
            else:
                key = (1, 5 - CARD_VALUE.get(p.item, 0.0) * 2, p.item)
            if best_key is None or key < best_key:
                best, best_key = p, key
        # Spend down: keep nothing, unspent AP is lost (Rules 5.4).
        return [best] if best else []

    def choose_flip_placement(self, state, event, legal):
        best, best_s = legal[0], -1e18
        for pl in legal:
            s = state.clone()
            for uid, h in pl.mapping:
                c = s.champs.get(uid)
                if c is not None:
                    c.hexpos = h
            s.touch()
            sc = evaluate(s, self.team)
            if sc > best_s:
                best, best_s = pl, sc
        return best
