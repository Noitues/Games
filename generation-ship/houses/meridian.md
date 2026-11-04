# House Meridian, the Flowkeepers

**Template:** River Surges in Sunlight · **Curve:** standard

Logistics and movement. They run the conduits and supply, move Crew, vent threat and spread influence widely.

- **Guilds:** Bureaucrats (primary) / Farmers (secondary)
- **Weaknesses:** Moderate damage; it moves problems rather than solving them.

## Tracks
The first value is the starting value. ★ marks a special slot.

| Track | Values |
|---|---|
| Credits per generation | 1 → 2 → ★ +Farmers → 3 → ★ +Bureaucrats → 5 |
| Card plays | 2 → ★ +1 card drawn → 3 → ★ +Bureaucrats → ★ +1 card drawn → 4 |

Hand = plays + 2. Clone 2.

## Special rule
Meridian influence in Agricultural sections counts as Havens for range.

## Innate: Reroute (slow)
Tiers are cumulative; the effect column is the full effect at that tier. *Reached* is how often a generation reaches at least that tier (house bots, calibration run).

| Tier | Threshold | Effect | PP | Reached |
|---|---|---|---|---|
| 1 | Bureaucrats 1 + Farmers 1 | vent 2 Glitch; gather 2 Crew (range 2, ANY) | 2.3 | 70% |
| 2 | Bureaucrats 2 + Farmers 2 | vent 2 Glitch/Fault; gather 1 Crew; Patch (range 2, ANY) | 4.6 | 39% |
| 3 | Bureaucrats 3 + Farmers 2 | vent 2 Glitch/Fault; vent 1 Failure; gather 1 Crew; Patch; Quarantine the source (range 2, ANY) | 7.45 | 4% |

## Growth
Shared menu: A place influence and uncover a track slot · B gain 2 credits · C draw +2 cards and gain 1 credit.
- Growth A: range 2

## Starting influence
1 in an Agricultural section and 1 adjacent to it

*Generated from `data/houses.json` by `tools/house_sheets.py`.*
