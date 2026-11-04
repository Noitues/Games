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

---

# Run 2: Keel at 2 plays, pacing retuned

## Changes
- **Keel** starts at **2 card plays** (track 2 → 2 → 2 → 3 → 4).
- **Win conditions shifted one step stricter:**
  - I: no threat and no Decay
  - II: no threat
  - III: no Faults or Failures
- **Purpose pool:** 5 per player (was 4).
- **Decay pool:** 3 per player + 1 (was 2 + 1).

## Why these settings
House bots, 4 pairings × 25–40 games per setting (`sim/tune.js`):

| Setting | Win rate | Win generation | Wins at tier III |
|---|---|---|---|
| Original pacing (Keel at 2 plays) | 78% | 5.6 | 40% (58% at II) |
| Slower Purpose only (8 per player, 4 per tier) | 49% | 9.0 | 0% (wins slide to tiers I/II) |
| More threat (2 Glitches per seed) | 7–54% | 6–10 | up to 97%, but games were short or brutal |
| **Shifted conditions, Purpose 5, Decay 3 + 1** | **66%** | **8.4** | **77%** |

**Takeaway:** pacing knobs alone couldn't move wins to tier III. Tier II's original condition was nearly as easy as tier III's, so the conditions themselves had to change.

## Pairing sweep (house bots, 100 games each, seed 9)

| Pairing | Win | Gens | Tier III wins | Decay loss | Time loss |
|---|---|---|---|---|---|
| Galvan + Meridian | 82% | 8.2 | 43% | 17% | 1% |
| Meridian + Vigil | 75% | 7.8 | 61% | 25% | 0% |
| Galvan + Vigil | 71% | 8.0 | 54% | 29% | 0% |
| Galvan + Keel | 58% | 8.9 | 35% | 35% | 7% |
| Meridian + Keel | 54% | 8.7 | 38% | 36% | 10% |
| Keel + Vigil | 49% | 8.0 | 37% | 47% | 4% |

## Findings
- **Pacing hit the target:**
  - average win rate about 65%,
  - games last about 8–9 generations and wins come at 7.9–8.7,
  - most wins at Understanding III,
  - **running out of events now matters** (up to 10% of games).
- **Keel improved but is still the weakest house.** It now plays about 2 cards and spends about 1.2 credits per generation (was 1.1 and 0.2). The gap to the other pairings shrank from about 30 points to about 20.
  - Its innate still rarely reaches tier II (3%).
  - Load-Bearing's Brace only helps when a collapse hits a Keel Haven.
  - Next levers: cheaper Keel innate thresholds, or a stronger special rule.
- **Galvan + Meridian still wins often at tier II (38%).** Both houses repair aggressively, so they clear every Glitch.
- **Innate tier III is still about 0–2%** for every house.
- **Remarkables rose to 6–8 per game.** The longer games give more chances to draw them.

---

# Run 3: starting threat in every section type

## Changes
- **Boards start like Spirit Island**, with threat already on them. Each board gets 1 Failure, 2 Faults and 1 Glitch, each in a different section type, rotated so boards differ. Threat by type per board is 3 / 2 / 2 / 1. Decay starts next to the Failure.
- **Pools retuned for the heavier start:** Purpose **4** per player, Decay **4** per player + 1.

## Tuning grid (house bots, 4 pairings × 30 games)

| Purpose / Decay per player | Win rate | Win generation | Wins at tier III |
|---|---|---|---|
| **4 / 4** | **63%** | **8.2** | **88%** |
| 4 / 3 | 55% | 8.0 | 86% |
| 5 / 4 | 58% | 8.9 | 79% |
| 5 / 3 | 53% | 8.7 | 76% |

## Pairing sweep (house bots, 100 games each, seed 9)

| Pairing | Win | Win gen | Tier III wins | Decay loss | Time loss |
|---|---|---|---|---|---|
| Galvan + Meridian | 80% | 7.8 | 73% | 20% | 0% |
| Meridian + Vigil | 74% | 7.7 | 72% | 24% | 2% |
| Galvan + Vigil | 67% | 8.1 | 63% | 29% | 4% |
| Meridian + Keel | 57% | 8.6 | 56% | 42% | 1% |
| Galvan + Keel | 56% | 8.9 | 53% | 38% | 6% |
| Keel + Vigil | 49% | 8.5 | 47% | 48% | 3% |

## Findings
- **Average win rate is about 64%**, and **about 94% of wins come at Understanding III**. Tier II wins dropped from 12–38% to 1–7%, because Glitches are now everywhere from the start.
- **Keel is still about 20 points behind** the other pairings. Its innate reaches tier II only 3–4% of the time.
- **Innate tier III is still at 0–1.5%.**
