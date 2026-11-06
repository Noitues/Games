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

## Balance (house bots, hull-module boards, default pair layout)

All 28 two-house pairings, each played in **both seat orders** (each house on both boards), 30 games per order: 1,680 games.

| House | Strength | vs average |
|---|---|---|
| Keel | 82% | +4.4 |
| Galvan | 81% | +3.5 |
| Voidwardens | 81% | +3.2 |
| Foremen | 79% | +1.8 |
| Tellers | 76% | −1.1 |
| Meridian | 74% | −3.5 |
| Vigil | 73% | −4.2 |
| Gardeners | 73% | −4.2 |

- **Overall:** 77% wins at level 0.
- **Spread:** every house is within ±4.4 points. The noise is about ±2.3 points per house at this sample size.

The earlier first-guess economy curves (Power Point totals per track) are kept in git history. The tracks have since changed with tuning, and simulation now measures power directly.
