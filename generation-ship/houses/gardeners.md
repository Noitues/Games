# House Gardeners, the Greenkeepers

**Template:** A Spread of Rampant Green · **Curve:** standard

They spread influence fast and turn it into living armor: Decay that would land on them takes their influence instead.

- **Guilds:** Farmers (primary) / Scholars (secondary)
- **Weaknesses:** Rooted spends influence, and a house with no influence loses the game for everyone.

## Tracks
The first value is the starting value. ★ marks a special slot.

| Track | Values |
|---|---|
| Credits per generation | 1 → 1 → 2 → ★ +Farmers → 3 → 5 |
| Card plays | 2 → 2 → 2 → 3 → ★ +1 clone slot → 4 |

Hand = plays + 2. Clone 1.

## Special rule
Once per generation, when Decay would be placed in a section with Gardener influence, remove 1 Gardener influence there instead.

## Innate: Cultivate (slow)
Tiers are cumulative; the effect column is the full effect at that tier. *Reached* is how often a generation reaches at least that tier (house bots, calibration run).

| Tier | Threshold | Effect | PP | Reached |
|---|---|---|---|---|
| 1 | Farmers 2 | Patch; Brace 1 (range 1, ANY) | 2.0 | 56% |
| 2 | Farmers 2 + Scholars 1 | Patch; add 1 Crew (range 1, ANY) | 4.5 | 41% |
| 3 | Farmers 3 + Scholars 2 | Patch; add 1 Crew; restore 1 Decay (range 1, ANY) | 7.5 | 7% |

## Growth
Shared menu: A place influence and uncover a track slot · B gain 2 credits · C draw +2 cards and gain 1 credit.
- Growth A: influence 2

## Starting influence
1 in an Agricultural section and 1 adjacent to it

*Generated from `data/houses.json` by `tools/house_sheets.py`.*
