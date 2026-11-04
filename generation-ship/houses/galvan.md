# House Galvan, the Spark-Wardens

**Template:** Lightning's Swift Strike · **Curve:** front-loaded

Fast, aggressive repair crews who hit threat hard and early but can't protect anything.

- **Guilds:** Engineers (primary) / Navigators (secondary)
- **Weaknesses:** No Brace, no Crew support, slow influence spread.

## Tracks
The first value is the starting value. ★ marks a special slot.

| Track | Values |
|---|---|
| Credits per generation | 1 → 1 → 1 → ★ +Engineers → 2 → 2 |
| Card plays | 3 → 3 → 3 → ★ +1 fast play → 4 |

Hand = plays + 2. Clone 1.

## Special rule
For each Engineer element you have, one additional played card (not your nominee) may resolve fast.

## Innate: Arc Repair (fast)
Tiers are cumulative; the effect column is the full effect at that tier. *Reached* is how often a generation reaches at least that tier (house bots, calibration run).

| Tier | Threshold | Effect | PP | Reached |
|---|---|---|---|---|
| 1 | Engineers 2 | 2 damage (range 0, ANY) | 2.0 | 58% |
| 2 | Engineers 3 + Navigators 1 | 3 damage; Lockout (range 1, ANY) | 5.0 | 44% |
| 3 | Engineers 3 + Navigators 2 | 4 damage; Lockout; downgrade 1 Failure (range 1, ANY) | 8.1 | 4% |

## Growth
Shared menu: A place influence and uncover a track slot · B gain 2 credits · C draw +2 cards and gain 1 credit.
- Growth B perk: +1 extra fast play this generation

## Starting influence
2 in Outer Hull sections

*Generated from `data/houses.json` by `tools/house_sheets.py`.*
