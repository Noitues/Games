# House Foremen, the Shift-Callers

**Template:** Thunderspeaker · **Curve:** standard

Crew-first leaders. They gather people where the trouble is and make Crew hit harder when they fight back.

- **Guilds:** Laborers (primary) / Keepers (secondary)
- **Weaknesses:** Little direct card damage; depends on Crew surviving.

## Tracks
The first value is the starting value. ★ marks a special slot.

| Track | Values |
|---|---|
| Credits per generation | 1 → 2 → ★ +Laborers → ★ +Laborers → 3 → ★ +Keepers |
| Card plays | 2 → ★ +1 card drawn → 3 → ★ +1 fast play → ★ +1 card drawn → 4 |

Hand = plays + 2. Clone 1.

## Special rule
Crew in sections with Foremen influence deal +1 damage each when they fight back after a Collapse.

## Innate: Rally the Shift (slow)
Tiers are cumulative; the effect column is the full effect at that tier. *Reached* is how often a generation reaches at least that tier (house bots, calibration run).

| Tier | Threshold | Effect | PP | Reached |
|---|---|---|---|---|
| 1 | Laborers 2 | gather 2 Crew; Brace 2 (range 1, ANY) | 2.0 | 48% |
| 2 | Laborers 2 + Keepers 1 | gather 2 Crew; Brace 2; Isolate 1 Fault (range 1, ANY) | 4.0 | 40% |
| 3 | Laborers 3 + Keepers 2 | gather 3 Crew; every Crew there deals its damage now; Brace 3 (range 1, ANY) | 6.5 | 5% |

## Growth
Shared menu: A place influence and uncover a track slot · B gain 2 credits · C draw +2 cards and gain 1 credit.


## Starting influence
1 in a Residential section and 1 in an Agricultural section

*Generated from `data/houses.json` by `tools/house_sheets.py`.*
