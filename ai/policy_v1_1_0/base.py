"""Policy interface (Multi-Agent Prompts Part 3.3).

The engine lists every legal option; a policy only chooses among them.
Policies are deterministic for a given seed.
"""
from __future__ import annotations

import random
from typing import List, Optional


class Policy:
    tier = "T0_random"

    def __init__(self, seed: int, temperature: float = 0.0, config: Optional[dict] = None):
        self.seed = seed
        self.temperature = temperature
        self.config = config or {}
        self.rng = random.Random(seed)
        self.team = "north"

    # ------------------------------------------------------------- decisions
    def choose_activation(self, state, legal):
        raise NotImplementedError

    def choose_flip_placement(self, state, event, legal):
        return legal[0]

    def choose_card_play(self, state, activation, legal):
        return None

    def choose_shop(self, state, legal):
        return []
