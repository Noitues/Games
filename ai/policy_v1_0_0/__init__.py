from .base import Policy
from .t0_random import T0Random
from .t1_greedy import T1Greedy

TIERS = {"T0_random": T0Random, "T1_greedy": T1Greedy}


def make(tier: str, seed: int, temperature: float = 0.3, config: dict | None = None,
         team: str = "north"):
    cls = TIERS[tier]
    pol = cls(seed=seed, temperature=temperature, config=config or {})
    pol.team = team
    return pol
