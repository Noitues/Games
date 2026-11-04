# Monte Carlo findings, run 1

House bots, 2 players, offset pairing, 150 games per pairing (`--sweep --games 150 --seed 3`).

## 1. Keel is far too weak, and the cause is a rule interaction
Every pairing that includes Keel wins **52–64%**. Pairings without Keel win **87–94%**.

| Keel stat | Value |
|---|---|
| Plays per generation | 1.1–1.2 |
| Credits spent per generation | 0.1–0.2 |
| Innate tier II or higher | under 1% |

The cause:
- **Keel starts with 1 card play, and the nominee is free.** For its first several generations Keel's only play is its free nominee, so it never needs credits.
- **Its credit-rich, steep identity never activates.** Wealth only pays off with more plays (or Remarkables, which need a hand of 4+).

Options:
- (a) Make the nominee pay full cost, or a reduced cost, or make it free only for Commons.
- (b) Start Keel at 2 plays.
- (c) Let Keel spend credits on something besides plays (e.g. Brace per credit).

## 2. Games end early: wins come at generation 5–7 of a 13-generation clock
- About 3.5 Discoveries are earned per game, so **Understanding II arrives quickly**. Its condition ("no Faults or Failures") is then met within a generation or two.
- Losses to the event deck running out are under 2%. The clock almost never matters.
- **Steep curves can't pay off**, because the reference pacing assumed 12 generations. This also makes the Keel problem worse.

Levers:
- a larger Purpose pool (currently 4 per player),
- more Discoveries per tier,
- or tier conditions that also require a minimum generation.

## 3. Innate thresholds: tier III is almost unreachable
Rates at which each innate tier is reached:

| House | No tier | Tier I | Tier II | Tier III |
|---|---|---|---|---|
| Galvan | 54–58% | 31–34% | 11–12% | ~0% |
| Meridian | 40–42% | 46–50% | 9–12% | ~1% |
| Vigil | 65% | 27–30% | 5–8% | ~0% |
| Keel | 63–67% | 33–37% | ~0% | ~0% |

- Card element-threshold bonuses are met **42–62%** of the time they're attempted.
- The framework prices elements as if tiers II and III are reachable. **Element costs should rise sharply for tiers II and III**, or raw track elements should be more generous.

## 4. Other measurements
- **Galvan's Overclock:** about 1.35 extra fast plays per generation.
- **Discoveries:** Breakthrough is chosen about twice as often as Apply (about 2.3 vs 1.1 per game).
- **Remarkables:** 4–5 per game for non-Keel houses, about 1 for Keel.
- **Losses** are almost entirely from the Decay pool emptying. Influence losses are rare (≤2%).
- **Free nominee:** the planner always nominates its most expensive card. That makes free Remarkables a strong pattern, and is part of finding 1.

## Bot strength
| Bot | Win rate (Galvan + Keel) |
|---|---|
| random | 0% |
| tactician | 5% |
| planner | 48–53% |
| house (with round rollouts) | 62–63% |

Each layer adds measurably. Next bot improvements:
- coordinate commits across houses (plan the second house after simulating the first),
- roll out growth choices,
- cooperative house targeting.
