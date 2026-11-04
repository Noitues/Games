# House Tellers, the Keepers of the Story

**Template:** Bringer of Dreams and Nightmares · **Curve:** standard

They control the story. Their damage never destroys anything; it becomes Purpose and calms the threat (Isolate).

- **Guilds:** Bureaucrats (primary) / Medics (secondary)
- **Weaknesses:** Can't clear threat themselves, so teammates must do the removing.

## Tracks
The first value is the starting value. ★ marks a special slot.

| Track | Values |
|---|---|
| Credits per generation | 1 → 2 → 2 → 3 → ★ +Bureaucrats → 4 |
| Card plays | 2 → 2 → 3 → ★ +Medics → 3 → 4 |

Hand = plays + 2. Clone 1.

## Special rule
Damage from Tellers' cards does not destroy threat; each point generates 2 Purpose and Isolates 1 damage of threat in that section (it deals that much less at the next Collapse).

## Innate: Steady Voices (slow)
Tiers are cumulative; the effect column is the full effect at that tier. *Reached* is how often a generation reaches at least that tier (house bots, calibration run).

| Tier | Threshold | Effect | PP | Reached |
|---|---|---|---|---|
| 1 | Bureaucrats 2 | Isolate 1 Fault; Lockout (range 1, ANY) | 2.0 | 52% |
| 2 | Bureaucrats 2 + Medics 1 | Isolate 2 Fault; Lockout; Brace 2 (range 1, ANY) | 4.0 | 49% |
| 3 | Bureaucrats 3 + Medics 2 | Isolate 1 Failure; Isolate 1 Fault; Quarantine; gather 2 Crew; Lockout (range 1, ANY) | 6.5 | 9% |

## Growth
Shared menu: A place influence and uncover a track slot · B gain 2 credits · C draw +2 cards and gain 1 credit.


## Starting influence
1 in a Government section and 1 in an Infrastructure section

*Generated from `data/houses.json` by `tools/house_sheets.py`.*
