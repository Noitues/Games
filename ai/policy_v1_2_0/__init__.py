"""ai 1.2.0 - same policies as 1.1.0, with T2_search retuned.

Calibration (reports/calibration/plan_*.json, 890 games against T1) found three
levers that each add a few points and none that changes the picture:

| variant (vs T1)                | win rate            |
|--------------------------------|---------------------|
| T2 as shipped in 1.1.0         | 55.5% [48.6, 62.2]  |
| + World Phase resolved at leaf | 56.7% [44.1, 68.4]  |
| + sharper softmax              | 60.0% [53.1, 66.5]  |
| + full-fidelity opponent model | 62.0% [54.0, 69.4]  |

1.2.0 ships all three together. ai 1.1.0 stays exactly as batches 0005-0007
ran it, so those reports remain reproducible.
"""
from ai.policy_v1_1_0 import EXPLOITS, PROFILES, Policy, T0Random, T1Greedy  # noqa: F401
from ai.policy_v1_1_0.t2_search import T2Search as _T2Search

T2_DEFAULTS = {
    "root_k": 10,
    "plies": 2,
    "time_budget_ms": 1600,
    "leaf_world": True,
    "temp_scale": 0.15,
    "opp_enum": {"step_cap": 4, "plan_cap": 4, "max_dest": 14, "max_options": 140,
                 "placement_cap": 3},
}


class T2Search(_T2Search):
    """T2 with the calibrated defaults; an explicit config still wins."""

    def __init__(self, seed: int, temperature: float = 0.0, config=None):
        merged = dict(T2_DEFAULTS)
        merged.update(config or {})
        super().__init__(seed, temperature, merged)


TIERS = {"T0_random": T0Random, "T1_greedy": T1Greedy, "T2_search": T2Search}
TIERS.update(EXPLOITS)


def make(tier: str, seed: int, temperature: float = 0.3, config: dict | None = None,
         team: str = "north"):
    pol = TIERS[tier](seed=seed, temperature=temperature, config=config or {})
    pol.team = team
    return pol
