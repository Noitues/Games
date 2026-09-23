# Batch report: scripted-v031

Runs: 22 ({'complete': 22}). Spec version(s): ['0.3.1']. Backend(s): ['scripted']. Tokens: 0 (≈ $0.00).

## Blind per-session judge (compiled after unblinding)

_Each session was scored alone by a judge that saw only the story (no mechanics lines, and no deck, card or tension vocabulary or card IDs) under a random session ID. Scores were joined to arms only afterwards._

| Score (1–10) | A (20 sessions) | B (1 sessions) | C (1 sessions) |
| --- | --- | --- | --- |
| overall | 5.25 [4.45, 6.05] (n=20) | 8.00 (n=1) | 5.00 (n=1) |
| engagement | 5.65 [4.95, 6.35] (n=20) | 6.00 (n=1) | 4.00 (n=1) |
| coherence | 5.50 [4.70, 6.20] (n=20) | 6.00 (n=1) | 5.00 (n=1) |
| spotlight_fairness | 5.75 [4.95, 6.50] (n=20) | 5.00 (n=1) | 3.00 (n=1) |
| player_agency | 5.55 [4.75, 6.30] (n=20) | 7.00 (n=1) | 8.00 (n=1) |
| complication_quality | 5.25 [4.45, 6.10] (n=20) | 3.00 (n=1) | 5.00 (n=1) |
| backstory_score | 5.08 [4.71, 5.42] (n=80) | 5.25 [4.00, 6.50] (n=4) | 3.50 [3.00, 4.50] (n=4) |
| backstory_used_rate | 0.55 [0.44, 0.65] (n=80) | 1.00 [1.00, 1.00] (n=4) | 0.25 [0.00, 0.75] (n=4) |
| all_players_backstory_used | 0.10 [0.00, 0.25] (n=20) | 1.00 (n=1) | 0.00 (n=1) |
| lurker_backstory_score | 5.10 [4.10, 6.20] (n=10) | — | — |

_Synthetic (scripted backend): these judge scores are random placeholders._


## Structural metrics (per session, mean [95% bootstrap CI])

| Metric | A | B | C |
| --- | --- | --- | --- |
| Every player's backstory drove an event | 1.00 [1.00, 1.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Every player's own card surfaced from the deck | 1.00 [1.00, 1.00] (n=20) | — | — |
| Deck draws / session (target 5–8) | 5.70 [5.20, 6.10] (n=20) | 0.00 (n=1) | 6.00 (n=1) |
| Draw costs using the drawn card: engine tag check | 1.00 [1.00, 1.00] (n=20) | — | 1.00 (n=1) |
| Draw costs whose text uses the tag (after rewrite) | 1.00 [1.00, 1.00] (n=20) | — | 1.00 (n=1) |
| Draw costs that needed a GM rewrite | 0.00 [0.00, 0.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Draw costs using the drawn card: referee judgment | 1.00 [1.00, 1.00] (n=20) | — | 1.00 (n=1) |
| Minutes per session | 0.00 [0.00, 0.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Cost per session (USD) | 0.00 [0.00, 0.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Mean player FP at session end (target 1–5) | 2.91 [2.49, 3.34] (n=20) | 1.25 (n=1) | 2.00 (n=1) |
| Spotlight Gini: turns | 0.07 [0.05, 0.10] (n=20) | 0.03 (n=1) | 0.00 (n=1) |
| Spotlight Gini: invokes | 0.41 [0.32, 0.49] (n=20) | 0.19 (n=1) | 0.25 (n=1) |
| Scenes / session | 4.30 [4.00, 4.60] (n=20) | 5.00 (n=1) | 5.00 (n=1) |
| Clock marks | 5.10 [4.20, 6.00] (n=20) | 2.00 (n=1) | 6.00 (n=1) |
| Compels accepted | 4.35 [3.85, 4.90] (n=20) | 5.00 (n=1) | 3.00 (n=1) |
| Compels refused | 1.40 [1.10, 1.75] (n=20) | 1.00 (n=1) | 4.00 (n=1) |
| GM-improvised complications | 1.85 [1.25, 2.50] (n=20) | 9.00 (n=1) | 3.00 (n=1) |
| Card-supplied complications | 9.65 [9.15, 10.15] (n=20) | 0.00 (n=1) | 11.00 (n=1) |
| Improvisation share | 0.15 [0.10, 0.19] (n=20) | 1.00 (n=1) | 0.21 (n=1) |
| Rule violations (engine + referee) | 0.75 [0.30, 1.20] (n=20) | 0.00 (n=1) | 1.00 (n=1) |
|   — engine refusals | 0.75 [0.30, 1.20] (n=20) | 0.00 (n=1) | 1.00 (n=1) |
|   — referee | 0.00 [0.00, 0.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Ambiguity records | 8.55 [7.55, 9.70] (n=20) | 2.00 (n=1) | 12.00 (n=1) |
| Backstory guarantee failures | 0.00 [0.00, 0.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Within-session variance of involvement | — | — | — |
| Compel accept ratio | 0.757 | 0.833 | 0.429 |
| Tension values seen | {1: 5, 2: 10, 3: 36, 4: 29, 5: 14, 6: 12} | {} | {3: 1, 4: 2, 5: 1, 6: 2} |

## Experiential (LLM player self-reports, 1–7; weak evidence)

| Score | A | B | C |
| --- | --- | --- | --- |
| fun | — | — | — |
| involvement | — | — | — |
| connection | — | — | — |
| control | — | — | — |
| play_again | — | — | — |

### Paired differences (same seed, same character and personality)

- **A-B**: involvement —; connection —; fun —; control —
- **A-C**: involvement —; connection —; fun —; control —
- **C-B**: involvement —; connection —; fun —; control —

Lurker involvement by arm: 

### Survey means by personality

| Personality | A involvement | B involvement | C involvement | A connection | B connection | C connection |
| --- | --- | --- | --- | --- | --- | --- |

### Paired transcript preference (blinded, same cohort and seed)

- not run

### Fate point flow by personality (mean per session: earned / spent / end)

- **A**: instigator 1.6/1.6/3; lurker 2.1/0.4/4.7; method_actor 2.6/1.1/4.5; optimizer 1.1/3.4/0.7; protector 1.8/1.6/3.2; rules_lawyer 0.8/3.2/0.6; storyteller 2.4/0.8/4.6; tactician 1.2/2.2/2
- **B**: instigator 3/3/3; optimizer 5/8/0; protector 1/3/1; tactician 2/4/1
- **C**: instigator 2/0/5; optimizer 1/3/1; protector 1/3/1; tactician 1/3/1

### Complaint clusters (keyword buckets over 'most frustrating')

- **A**: {}
- **B**: {}
- **C**: {}

## Ambiguities

| Count | ID / section | Issue | Interim ruling |
| --- | --- | --- | --- |
| 26 | AMB-27 | Success with style on create advantage: the aspect's 2 free invokes AND the deck peek, or one of them? | Both: the aspect keeps 2 free invokes and the player may also peek. |
| 22 | AMB-12 | Stress box values are unspecified. | Fate Core: boxes 1 and 2; Physique/Will +1/+2 adds a 3 box, +3 or more adds 3 and 4. |
| 21 | AMB-01 | Arm A lists 'Attention', which the spec never defines. | Not modelled. |
| 21 | AMB-22 | Does a GLOBAL anchor give the GM a free invoke like a GM card? | Yes, GLOBAL cards placed on the rail give the GM 1 free invoke that scene. |
| 19 | AMB-16 | A draw is required but the deck is empty outside a climax. | The cost uses a face-up GM tag, as in a climax. |
| 16 | AMB-03 | Does the session end after the climax scene? | Yes: the climax scene is the last scene of the session. |
| 14 | AMB-10 | Growth from 'roll fails after one of its tags was invoked' — invoked by whom? | Owner's own invokes only. |
| 12 | AMB-14 | Who decides a beat 'went badly' for its stakes clock? | GM agent reports it at scene end; the Referee audits it. |
| 11 | AMB-20 | §6 Altered scene draws a card, but §4's closed list of draw triggers omits it. | §6 is more specific: Altered scenes draw. |
| 8 | AMB-23 | Success at major cost on an attack: how much harm lands? | The attack lands for 1 shift. |
| 8 | AMB-26 | Several Beat Frames are queued for the same scene. | One per scene; the guarantee frame first, the rest carry to later scenes. |
| 7 | AMB-19 | Tie on an attack: 'success at minor cost' but 0 shifts of harm. | Attacker gets a boost (Fate Core) and the deck draw still happens. |

## Referee friction points (all runs)


## Player one-sentence verdicts on backstory use


## Run status

| Run | Status | Scenes | Draws | Tokens | Error |
| --- | --- | --- | --- | --- | --- |
| scripted-v031__A__s89081__r0 | complete | 5 | 6 | 0 |  |
| scripted-v031__A__s89082__r1 | complete | 4 | 6 | 0 |  |
| scripted-v031__A__s89083__r2 | complete | 4 | 7 | 0 |  |
| scripted-v031__A__s89084__r3 | complete | 4 | 5 | 0 |  |
| scripted-v031__A__s89085__r4 | complete | 5 | 6 | 0 |  |
| scripted-v031__A__s89086__r5 | complete | 5 | 6 | 0 |  |
| scripted-v031__A__s89087__r6 | complete | 4 | 6 | 0 |  |
| scripted-v031__A__s89088__r7 | complete | 4 | 6 | 0 |  |
| scripted-v031__A__s89089__r8 | complete | 4 | 7 | 0 |  |
| scripted-v031__A__s89090__r9 | complete | 4 | 6 | 0 |  |
| scripted-v031__A__s89091__r10 | complete | 5 | 6 | 0 |  |
| scripted-v031__A__s89092__r11 | complete | 5 | 7 | 0 |  |
| scripted-v031__A__s89093__r12 | complete | 4 | 6 | 0 |  |
| scripted-v031__A__s89094__r13 | complete | 5 | 5 | 0 |  |
| scripted-v031__A__s89095__r14 | complete | 3 | 5 | 0 |  |
| scripted-v031__A__s89096__r15 | complete | 5 | 6 | 0 |  |
| scripted-v031__A__s89097__r16 | complete | 4 | 5 | 0 |  |
| scripted-v031__A__s89098__r17 | complete | 5 | 2 | 0 |  |
| scripted-v031__A__s89099__r18 | complete | 3 | 5 | 0 |  |
| scripted-v031__A__s89100__r19 | complete | 4 | 6 | 0 |  |
| scripted-v031__B__s89081__r0 | complete | 5 | 0 | 0 |  |
| scripted-v031__C__s89081__r0 | complete | 5 | 6 | 0 |  |
