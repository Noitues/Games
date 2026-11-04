# House Vigil, the Lamplighters

**Template:** Shadows Flicker Like Flame · **Curve:** standard

Keepers of the Archive and the Mission. They inspire the crew, generate Purpose, and reach anywhere people gather.

- **Guilds:** Keepers (primary) / Scholars (secondary)
- **Weaknesses:** Little damage, fragile influence.

## Tracks
The first value is the starting value. ★ marks a special slot.

| Track | Values |
|---|---|
| Credits per generation | 1 → 2 → 2 → ★ +Keepers → 3 → 3 |
| Card plays | 2 → 2 → 3 → ★ +Scholars → 3 → 4 |

Hand = plays + 2. Clone 1.

## Special rule
Vigil may target from any section with Crew by paying 1 extra credit.

## Innate: Kindle Purpose (slow)
Tiers are cumulative; the effect column is the full effect at that tier. *Reached* is how often a generation reaches at least that tier (house bots, calibration run).

| Tier | Threshold | Effect | PP | Reached |
|---|---|---|---|---|
| 1 | Keepers 2 | +2 Purpose | 2.0 | 45% |
| 2 | Keepers 3 + Scholars 1 | +4 Purpose; foresee | 4.5 | 42% |
| 3 | Keepers 3 + Scholars 2 | +5 Purpose; foresee; temper the Elder's Legacy | 8.5 | 10% |

## Growth
Shared menu: A place influence and uncover a track slot · B gain 2 credits · C draw +2 cards and gain 1 credit.
- Growth C: text Draw +2 cards this generation (or take a Remarkable) and gain 1 Purpose, effects {'extra_draw': 2, 'purpose': 1}

## Starting influence
1 in a Government section and 1 in a Residential section

*Generated from `data/houses.json` by `tools/house_sheets.py`.*
