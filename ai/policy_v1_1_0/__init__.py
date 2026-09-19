from .base import Policy
from .exploit import EXPLOITS, PROFILES
from .t0_random import T0Random
from .t1_greedy import T1Greedy
from .t2_search import T2Search

TIERS = {"T0_random": T0Random, "T1_greedy": T1Greedy, "T2_search": T2Search}
TIERS.update(EXPLOITS)


def make(tier: str, seed: int, temperature: float = 0.3, config: dict | None = None,
         team: str = "north"):
    cls = TIERS[tier]
    pol = cls(seed=seed, temperature=temperature, config=config or {})
    pol.team = team
    return pol
