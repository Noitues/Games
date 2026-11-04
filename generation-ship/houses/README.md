# Houses v0

Each house is built from the **Balance framework** in [`../GDD.md`](../GDD.md). Its Spirit Island template sets the identity and the curve shape. All PP values are first estimates, to be calibrated by Monte Carlo playtesting.

| House | Template | Identity | Guilds (primary / secondary) | Curve |
|---|---|---|---|---|
| [Galvan](galvan.md) | Lightning's Swift Strike | Fast, aggressive repair | Engineers / Navigators | Front-loaded |
| [Meridian](meridian.md) | River Surges in Sunlight | Movement and logistics | Bureaucrats / Farmers | Standard |
| [Keel](keel.md) | Vital Strength of the Earth | Slow, defensive | Medics / Laborers | Steep |
| [Vigil](vigil.md) | Shadows Flicker Like Flame | Purpose and reach | Keepers / Scholars | Standard |

All eight guilds have a home.

## Economy curves (reference pacing, tracks only)

Value per generation = 2 × card plays + credits (+ raw element, fast and clone slots once uncovered). Innates and special rules are excluded until their hit rates are measured.

| House | Total (12 gens) | Gens 1–4 | Gens 9–12 | Late ÷ early | Target shape | Result |
|---|---|---|---|---|---|---|
| Galvan | 101.0 | 28.0 | 41.0 | **1.46** | < 1.5 | ✓ |
| Meridian | 105.0 | 26.0 | 43.0 | **1.65** | 1.5–2.0 | ✓ |
| Keel | 101.0 | 20.0 | 48.0 | **2.40** | > 2.0 | ✓ |
| Vigil | 107.5 | 26.0 | 45.0 | **1.73** | 1.5–2.0 | ✓ |

Average 103.6; the ±5% band is 98.4–108.8. All four houses are inside it.

Per-generation values:

| Gen | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Galvan | 7 | 7 | 7 | 7 | 7 | 8 | 8 | 9 | 9 | 10 | 10 | 12 |
| Meridian | 6 | 6 | 6 | 8 | 8 | 9 | 9 | 10 | 10 | 11 | 11 | 11 |
| Keel | 4 | 4 | 5 | 7 | 7 | 8 | 8 | 10 | 10 | 12 | 12 | 14 |
| Vigil | 6 | 6 | 6 | 8 | 8 | 9 | 9 | 10.5 | 10.5 | 11.5 | 11.5 | 11.5 |

## Not yet balanced

Rough estimates of special rules and other extras, per game:

| House | Extras | ≈ PP per game |
|---|---|---|
| Galvan | Overclock | 21 |
| Meridian | Supply Lines, hand +3, clone 2 | 24 |
| Keel | Load-Bearing | 8 |
| Vigil | Voices Among the Crew | 6 |

With these added, Meridian and Galvan run high and Keel runs low. The fix waits for Monte Carlo data on special-rule triggers and innate hit rates.

## Shared growth menu (pick one per generation)

| Option | Effect | PP |
|---|---|---|
| A. Influence | Place 1 influence from a track, within range 1 | 2 |
| B. Credits | Gain 2 credits, plus the house perk | 2 + perk |
| C. Draw | Draw +2 cards this generation (or take a Remarkable by draw substitution), and gain 1 credit | 2.5 |

The +1 credit on option C was added so every house's options sit within ±1 PP of each other, as the framework requires. Without it, option C was worth about 1.5.
