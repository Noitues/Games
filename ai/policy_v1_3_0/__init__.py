"""ai 1.3.0 - flank awareness, and personalities that want different games.

Two changes over 1.2.0, both asked for by the lead designer.

**Flank awareness.** A hidden hexgroup beside a lane is a gank avenue. The
evaluation now prices that directly: standing next to one that holds enemies is
a risk, standing next to an empty one is worth a little because it denies the
approach. The visible effect is that a laner picks the side of its lane away
from the dangerous hexgroup instead of walking down the middle of it, which
matters most in mid, where both river hexgroups are in reach.

**Personalities.** One evaluation, several appetites. These are not the exploit
policies - each is meant to be a reasonable way to play, so that a batch of
mixed match-ups reads more like a play-test evening than a mirror does. A
mirror measures the game against one taste; a spread of personalities measures
it against several, which is what the balance numbers are supposed to survive.

ai 1.2.0 stays exactly as batches 0008-0035 ran it.
"""
from ai.policy_v1_1_0 import EXPLOITS, Policy, T0Random  # noqa: F401
from ai.policy_v1_1_0.evaluation import T2_MACRO, W
from ai.policy_v1_1_0.t1_greedy import T1Greedy as _T1Greedy
from ai.policy_v1_2_0 import T2Search as _T2Search

# Flank terms, on for every ai 1.3.0 policy.
FLANK = {"flank_risk": 1.6, "flank_watch": 0.45}

BASE_T1 = dict(W, **FLANK)
BASE_T2 = dict(T2_MACRO, **FLANK)

#: Each personality is a full weight profile plus, where it matters, its own
#: card prices (`buy` to acquire, `cards` to hold) and shop order. Cheap cards are played freely; dear ones are
#: hoarded, so a low `cards` value means "spend these".
PERSONALITIES = {
    # Plays on vision and safety: wards the gank avenues, keeps out of reach,
    # and would rather give up a chip than a champion.
    "warder": dict(
        BASE_T2, flank_watch=1.1, flank_risk=2.4, death_risk=10.0, incoming_own=1.6,
        # Buys wards eagerly and plays them on sight: the buy price is high,
        # the holding price is below zero.
        buy={"control_ward": 3.2, "stopwatch": 1.0, "health_potion": 0.9},
        cards={"control_ward": -0.6, "stopwatch": 1.2, "health_potion": 0.8,
               "frost_charm": 0.6, "swift_tonic": 0.4}),
    # Wants the five-on-five: stays grouped and looks for kills.
    "brawler": dict(
        BASE_T2, group_bias=0.55, kill_chance=9.0, alive_enemy=4.2, hp_enemy=1.7,
        struct_focus=0.0, lane=0.08, flank_risk=0.9),
    # Plays the map: towers, wave state, and the Nexus behind them.
    "sieger": dict(
        BASE_T2, struct_focus=0.9, tower_enemy=3.4, nexus_enemy=11.0,
        wave_push=0.55, wave_own=0.7, kill_chance=4.0),
    # Plays the clock: Dragon, Baron and the camps that buy them.
    "objective": dict(
        BASE_T2, objective_pull=0.9, dragon=12.0, baron=10.0, monster_chip=0.5,
        lane=0.10),
    # Plays the lane: farms, keeps its distance, and punishes a mistake.
    "laner": dict(
        BASE_T2, lane=0.34, wave_enemy=0.8, wave_own=0.65, ap=1.2,
        flank_risk=2.2, death_risk=8.5),
}


class T1Greedy(_T1Greedy):
    weights = BASE_T1


class T2Search(_T2Search):
    weights = BASE_T2


def _personality(name: str):
    profile = PERSONALITIES[name]

    class Personality(_T2Search):
        weights = profile
        tier = f"T2_{name}"          # so a mixed batch can be read per personality

    Personality.__name__ = f"T2_{name}"
    Personality.__qualname__ = Personality.__name__
    return Personality


TIERS = {"T0_random": T0Random, "T1_greedy": T1Greedy, "T2_search": T2Search}
TIERS.update({f"T2_{name}": _personality(name) for name in PERSONALITIES})
TIERS.update(EXPLOITS)

#: The spread a mixed play-test batch draws from.
PERSONALITY_POOL = tuple(f"T2_{name}" for name in PERSONALITIES)


def make(tier: str, seed: int, temperature: float = 0.3, config: dict | None = None,
         team: str = "north"):
    cls = TIERS[tier]
    pol = cls(seed=seed, temperature=temperature, config=config or {})
    pol.team = team
    return pol
