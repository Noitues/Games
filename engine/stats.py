"""Confidence intervals and multiple-test correction (Prompts Part 4.D)."""
from __future__ import annotations

import math
import random
from typing import Dict, List, Optional, Sequence, Tuple

Z95 = 1.959963984540054


def wilson(k: int, n: int, z: float = Z95) -> Tuple[float, float, float]:
    """Wilson score interval for a rate, returned as (p, lo, hi) in percent."""
    if n == 0:
        return (0.0, 0.0, 100.0)
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (100 * p, 100 * max(0.0, centre - half), 100 * min(1.0, centre + half))


def bootstrap(values: Sequence[float], stat=lambda v: sum(v) / len(v),
              reps: int = 400, seed: int = 12345) -> Tuple[float, float, float]:
    if not values:
        return (0.0, 0.0, 0.0)
    rng = random.Random(seed)
    n = len(values)
    point = stat(values)
    draws = []
    for _ in range(reps):
        sample = [values[rng.randrange(n)] for _ in range(n)]
        draws.append(stat(sample))
    draws.sort()
    lo = draws[int(0.025 * reps)]
    hi = draws[min(reps - 1, int(0.975 * reps))]
    return (point, lo, hi)


def median(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    v = sorted(values)
    n = len(v)
    return v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2])


def percentile(values: Sequence[float], p: float) -> float:
    if not values:
        return 0.0
    v = sorted(values)
    i = min(len(v) - 1, max(0, int(round(p * (len(v) - 1)))))
    return v[i]


def verdict(lo: float, hi: float, target_lo: float, target_hi: float) -> str:
    """PASS only if the whole interval sits inside the target band, FAIL only
    if it sits entirely outside; otherwise INCONCLUSIVE."""
    if lo >= target_lo and hi <= target_hi:
        return "PASS"
    if hi < target_lo or lo > target_hi:
        return "FAIL"
    return "INCONCLUSIVE"


def two_prop_z(k1: int, n1: int, k2: int, n2: int) -> float:
    """Two-sided p-value for a difference of two rates (normal approximation)."""
    if n1 == 0 or n2 == 0:
        return 1.0
    p1, p2 = k1 / n1, k2 / n2
    p = (k1 + k2) / (n1 + n2)
    se = math.sqrt(max(1e-12, p * (1 - p) * (1 / n1 + 1 / n2)))
    z = (p1 - p2) / se if se else 0.0
    return math.erfc(abs(z) / math.sqrt(2))


def holm(pvals: Dict[str, float], alpha: float = 0.05) -> Dict[str, bool]:
    """Holm-Bonferroni: returns {key: significant}."""
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m = len(items)
    out: Dict[str, bool] = {}
    reject = True
    for i, (k, p) in enumerate(items):
        if reject and p <= alpha / (m - i):
            out[k] = True
        else:
            reject = False
            out[k] = False
    return out
