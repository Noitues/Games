"""T0_random: the baseline. Uniform over legal options, but never passes up a
free farm (L0 on a minion wave)."""
from __future__ import annotations

from .base import Policy


class T0Random(Policy):
    tier = "T0_random"

    def choose_activation(self, state, legal):
        farms = []
        for a in legal:
            if a.is_pass or a.ability != "L0":
                continue
            for ch in a.plan:
                u = state.unit(ch) if isinstance(ch, str) else None
                if u is not None and u.kind == "wave" and u.team != self.team:
                    farms.append(a)
                    break
        pool = farms or [a for a in legal if not a.is_pass] or legal
        return self.rng.choice(pool)

    def choose_card_play(self, state, activation, legal):
        if legal and self.rng.random() < 0.3:
            return self.rng.choice(legal)
        return None

    def choose_shop(self, state, legal):
        if not legal:
            return []
        return [self.rng.choice(legal)]

    def choose_flip_placement(self, state, event, legal):
        return self.rng.choice(legal)
