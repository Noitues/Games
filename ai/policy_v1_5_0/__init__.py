"""ai 1.5.0 - the exploit set rebuilt on T2 (the RQ-043 caveat).

The seven `X_exploit_*` policies are T1 greedy weight profiles (ai 1.1.0), and
the Phase 5 gate they were read against (`batch_0045`) is a T2 field. Their
zeroes therefore measure T1 against T2 as much as the exploit against the
rules, which is the caveat RQ-043 recorded. This package adds the same seven
distortions on the T2 search, as `X2_exploit_*` tiers, so that a Phase 5
re-run says what the rules allow rather than what a one-ply policy manages.

Each `X2_exploit_*` profile is the 1.3.0 T2 base (macro weights plus flank
terms) with exactly the weights its T1 twin moves away from the T1 base, at
the same values. Nothing is retuned: an exploit is still "the shared evaluator
with one appetite pushed to the extreme" (Prompts 4.C), only searched two
plies deep instead of one. The T1 set stays registered for the old reports.

ai 1.4.0 stays exactly as batches 0041-0055 ran it.
"""
from __future__ import annotations

from ai.policy_v1_1_0.evaluation import W
from ai.policy_v1_1_0.exploit import PROFILES as T1_EXPLOIT_PROFILES
from ai.policy_v1_2_0 import T2Search as _T2Search
from ai.policy_v1_4_0 import (  # noqa: F401
    BASE_T2, EXPLOITS, MACHINES, MEMORY_ROUNDS, OPS, PERSONALITIES, PERSONALITY_POOL,
    Policy, SIGNALS, T0Random, T1Greedy, T2Search, TIERS as _TIERS_1_4_0, generation,
    machine_class, next_state, signals, validate_machine,
)


def distortion(profile: dict) -> dict:
    """The weights a T1 exploit profile moves away from the T1 base, with
    their values. This is what makes the exploit the exploit."""
    return {k: v for k, v in profile.items() if k not in W or W[k] != v}


#: X2_exploit_<name>: the T2 base with the T1 exploit's distortion applied.
T2_EXPLOIT_PROFILES = {
    name.replace("X_", "X2_", 1): dict(BASE_T2, **distortion(profile))
    for name, profile in T1_EXPLOIT_PROFILES.items()
}


def _exploit(name: str):
    profile = T2_EXPLOIT_PROFILES[name]

    class Exploit(_T2Search):
        weights = profile
        tier = name                  # so section 9c/9d read each exploit as itself

    Exploit.__name__ = name
    Exploit.__qualname__ = name
    return Exploit


T2_EXPLOITS = {name: _exploit(name) for name in T2_EXPLOIT_PROFILES}

TIERS = dict(_TIERS_1_4_0)
TIERS.update(T2_EXPLOITS)

#: The pool a Phase 5 sweep draws its exploit from.
T2_EXPLOIT_POOL = tuple(sorted(T2_EXPLOITS))


def make(tier: str, seed: int, temperature: float = 0.3, config: dict | None = None,
         team: str = "north"):
    cls = TIERS[tier]
    pol = cls(seed=seed, temperature=temperature, config=config or {})
    pol.team = team
    return pol
