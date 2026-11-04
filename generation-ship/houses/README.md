# Houses

Eight houses, built from the GDD's Balance framework and then tuned by simulation. Each sheet (`<id>.md`) is generated from `data/houses.json` by `tools/house_sheets.py`; change the data, then regenerate.

| House | Spirit Island template | Identity | Guilds (primary / secondary) |
|---|---|---|---|
| [Galvan](galvan.md) | Lightning's Swift Strike | Fast, aggressive repair | Engineers / Navigators |
| [Meridian](meridian.md) | River Surges in Sunlight | Movement and logistics | Bureaucrats / Farmers |
| [Keel](keel.md) | Vital Strength of the Earth | Defensive; braces its sections | Medics / Laborers |
| [Vigil](vigil.md) | Shadows Flicker Like Flame | Purpose and reach | Keepers / Scholars |
| [Foremen](foremen.md) | Thunderspeaker | Crew-led offense | Laborers / Keepers |
| [Gardeners](gardeners.md) | A Spread of Rampant Green | Influence as armor | Farmers / Scholars |
| [Voidwardens](voidwardens.md) | Ocean's Hungry Grasp | Outer Hull specialists | Navigators / Engineers |
| [Tellers](tellers.md) | Bringer of Dreams and Nightmares | Damage becomes Purpose | Bureaucrats / Medics |

Every guild is the primary or secondary guild of exactly two houses.

## Balance (house bots, all 28 two-house pairings, 50 games each)

Strength = average win rate of the pairings a house appears in.

| House | Strength | vs average |
|---|---|---|
| Vigil | 77% | +3.4 |
| Keel | 77% | +3.1 |
| Foremen | 75% | +1.1 |
| Meridian | 75% | +0.9 |
| Voidwardens | 73% | −0.9 |
| Galvan | 72% | −1.7 |
| Gardeners | 72% | −2.3 |
| Tellers | 70% | −3.7 |

- **Overall:** 74% wins at level 0, about 82% of them at Understanding III, around generation 8.6.
- **Spread:** every house is within ±4 points. The noise is about ±3 points per house at this sample size.
- **How we got here:** see `sim/RESULTS.md`, runs 4–5.

The earlier first-guess economy curves (Power Point totals per track) are kept in git history. The tracks have since changed with tuning, and simulation now measures power directly.
