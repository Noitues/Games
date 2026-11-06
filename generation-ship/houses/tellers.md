# House Tellers, the Keepers of the Story

**Template:** Bringer of Dreams and Nightmares · **Curve:** standard

They control the story. Their damage never destroys anything; it becomes Purpose and Contains the threat.

- **Guilds:** Bureaucrats (primary) / Medics (secondary)
- **Weaknesses:** Can't clear threat themselves, so teammates must do the removing.

## Tracks
The first value is the starting value. ★ marks a special slot.

| Track | Values |
|---|---|
| Credits per generation | 1 → 2 → ★ +Medics → 3 → ★ +Bureaucrats → 4 |
| Card plays | 2 → ★ +1 card drawn → 3 → ★ +Medics → ★ +1 card drawn → 4 |

Hand = plays + 2. Clone 1.

## Special rule
Damage from Tellers' cards does not destroy threat: it Contains it instead (each piece that takes its full health gets a Contain marker, so it deals no damage at the next Collapse), and each point generates 3 Purpose.

## Innate: Steady Voices (slow)
Tiers are cumulative; the effect column is the full effect at that tier. *Reached* is how often a generation reaches at least that tier (house bots, calibration run).

| Tier | Threshold | Effect | PP | Reached |
|---|---|---|---|---|
| 1 | Bureaucrats 2 | Contain 1 Fault; Lockout (range 1, ANY) | 2.0 | 52% |
| 2 | Bureaucrats 2 + Medics 1 | Contain 2 Fault; Lockout; Brace 2 (range 1, ANY) | 4.0 | 49% |
| 3 | Bureaucrats 3 + Medics 2 | Contain 1 Failure; Contain 1 Fault; Quarantine; gather 2 Crew; Lockout (range 1, ANY) | 6.5 | 9% |

## Growth
Shared menu: A place influence and uncover a track slot · B gain 2 credits · C draw +2 cards and gain 1 credit.


## Starting influence
1 in a Government section and 1 in an Infrastructure section

*Generated from `data/houses.json` by `tools/house_sheets.py`.*
