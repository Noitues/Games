# Batch report: scripted-mc-01

Runs: 120 ({'complete': 120}). Spec version(s): ['0.1.0']. Backend(s): ['scripted']. Tokens: 0 (≈ $0.00).

## Blinded analyst conclusions

_Written by the Analyst agent from blinded labels **before** unblinding._

(Analyst agent not run: --no-llm)


## Unblinding

| Blinded label | Arm |
| --- | --- |
| Arm 1 | B |
| Arm 2 | A |
| Arm 3 | C |

## Structural metrics (per session, mean [95% bootstrap CI])

| Metric | A | B | C |
| --- | --- | --- | --- |
| Every player's backstory drove an event | 0.97 [0.93, 1.00] (n=40) | 0.03 [0.00, 0.07] (n=40) | 0.00 [0.00, 0.00] (n=40) |
| Every player's own card surfaced from the deck | 0.97 [0.93, 1.00] (n=40) | — | — |
| Deck draws / session (target 5–8) | 5.83 [5.62, 6.03] (n=40) | 0.00 [0.00, 0.00] (n=40) | 5.62 [5.35, 5.88] (n=40) |
| Draw costs using the drawn card: engine tag check | 1.00 [1.00, 1.00] (n=40) | — | 1.00 [1.00, 1.00] (n=40) |
| Draw costs using the drawn card: referee judgment | 1.00 [1.00, 1.00] (n=40) | — | 1.00 [1.00, 1.00] (n=40) |
| Mean player FP at session end (target 1–5) | 2.68 [2.39, 2.99] (n=40) | 2.48 [2.23, 2.75] (n=40) | 2.55 [2.32, 2.78] (n=40) |
| Spotlight Gini: turns | 0.08 [0.06, 0.10] (n=40) | 0.08 [0.06, 0.10] (n=40) | 0.09 [0.07, 0.10] (n=40) |
| Spotlight Gini: invokes | 0.36 [0.31, 0.40] (n=40) | 0.38 [0.33, 0.44] (n=40) | 0.38 [0.34, 0.43] (n=40) |
| Scenes / session | 4.30 [4.08, 4.53] (n=40) | 5.00 [5.00, 5.00] (n=40) | 4.40 [4.17, 4.62] (n=40) |
| Clock marks | 5.03 [4.28, 5.80] (n=40) | 2.45 [1.88, 3.02] (n=40) | 4.83 [4.05, 5.60] (n=40) |
| Compels accepted | 4.25 [3.77, 4.80] (n=40) | 1.77 [1.43, 2.12] (n=40) | 3.98 [3.50, 4.42] (n=40) |
| Compels refused | 1.90 [1.52, 2.30] (n=40) | 0.80 [0.55, 1.05] (n=40) | 1.77 [1.43, 2.12] (n=40) |
| GM-improvised complications | 2.30 [1.90, 2.75] (n=40) | 7.47 [6.70, 8.28] (n=40) | 1.98 [1.60, 2.35] (n=40) |
| Card-supplied complications | 9.60 [9.32, 9.88] (n=40) | 0.00 [0.00, 0.00] (n=40) | 9.20 [8.68, 9.62] (n=40) |
| Improvisation share | 0.19 [0.16, 0.21] (n=40) | 1.00 [1.00, 1.00] (n=40) | 0.17 [0.14, 0.20] (n=40) |
| Rule violations (engine + referee) | 1.27 [0.80, 1.82] (n=40) | 0.53 [0.28, 0.85] (n=40) | 1.02 [0.62, 1.45] (n=40) |
|   — engine refusals | 1.27 [0.80, 1.82] (n=40) | 0.53 [0.28, 0.85] (n=40) | 1.02 [0.62, 1.45] (n=40) |
|   — referee | 0.00 [0.00, 0.00] (n=40) | 0.00 [0.00, 0.00] (n=40) | 0.00 [0.00, 0.00] (n=40) |
| Ambiguity records | 10.22 [9.40, 11.12] (n=40) | 1.98 [1.62, 2.40] (n=40) | 9.25 [8.47, 9.97] (n=40) |
| Backstory guarantee failures | 0.05 [0.00, 0.15] (n=40) | 0.00 [0.00, 0.00] (n=40) | 0.00 [0.00, 0.00] (n=40) |
| Within-session variance of involvement | — | — | — |
| Compel accept ratio | 0.691 | 0.689 | 0.691 |
| Tension values seen | {2: 12, 3: 81, 4: 64, 5: 39, 6: 16} | {} | {2: 10, 3: 110, 4: 45, 5: 29, 6: 22} |

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

- A-B: {'B': 82, 'A': 78}
- A-C: {'A': 91, 'C': 69}
- B-C: {'B': 81, 'C': 79}

### Fate point flow by personality (mean per session: earned / spent / end)

- **A**: instigator 1.9/2.4/2.5; lurker 1.4/0.75/3.65; method_actor 2.05/1.3/3.75; optimizer 1.45/3.15/1.3; protector 2.2/1.65/3.55; rules_lawyer 1.2/2.85/1.35; storyteller 2.05/1.55/3.5; tactician 1.7/2.85/1.85
- **B**: instigator 1.35/1.75/2.6; lurker 1/0.9/3.1; method_actor 1.15/0.75/3.4; optimizer 0.85/2.65/1.2; protector 1.2/1.1/3.1; rules_lawyer 1/2.05/1.95; storyteller 1.25/0.95/3.3; tactician 1.1/2.9/1.2
- **C**: instigator 1.8/2.1/2.7; lurker 1.45/0.85/3.6; method_actor 2/1.15/3.85; optimizer 1.95/3.7/1.25; protector 1.85/1.85/3; rules_lawyer 0.85/3.2/0.65; storyteller 1.8/1.3/3.5; tactician 1.5/2.65/1.85

### Complaint clusters (keyword buckets over 'most frustrating')

- **A**: {}
- **B**: {}
- **C**: {}

## Ambiguities

| Count | ID / section | Issue | Interim ruling |
| --- | --- | --- | --- |
| 120 | AMB-12 | Stress box values are unspecified. | Fate Core: boxes 1 and 2; Physique/Will +1/+2 adds a 3 box, +3 or more adds 3 and 4. |
| 86 | AMB-16 | A draw is required but the deck is empty outside a climax. | The cost uses a face-up GM tag, as in a climax. |
| 80 | AMB-01 | Arm A lists 'Attention', which the spec never defines. | Not modelled. |
| 80 | AMB-22 | Does a GLOBAL anchor give the GM a free invoke like a GM card? | Yes, GLOBAL cards placed on the rail give the GM 1 free invoke that scene. |
| 68 | AMB-02 | Backstory guarantee needs 'the next Beat Frame', but frames are never forced. | Pulled cards force a guarantee Beat Frame at the start of the next scene. |
| 60 | AMB-14 | Who decides a beat 'went badly' for its stakes clock? | GM agent reports it at scene end; the Referee audits it. |
| 57 | AMB-19 | Tie on an attack: 'success at minor cost' but 0 shifts of harm. | Attacker gets a boost (Fate Core) and the deck draw still happens. |
| 56 | AMB-26 | Several Beat Frames are queued for the same scene. | One per scene; the guarantee frame first, the rest carry to later scenes. |
| 55 | AMB-03 | Does the session end after the climax scene? | Yes: the climax scene is the last scene of the session. |
| 54 | AMB-10 | Growth from 'roll fails after one of its tags was invoked' — invoked by whom? | Owner's own invokes only. |
| 51 | AMB-04 | Do tension adjustment rows stack? | All applicable rows are summed, then clamped to 1-6. |
| 46 | AMB-23 | Success at major cost on an attack: how much harm lands? | The attack lands for 1 shift. |
| 38 | AMB-20 | §6 Altered scene draws a card, but §4's closed list of draw triggers omits it. | §6 is more specific: Altered scenes draw. |
| 2 | AMB-25 | Backstory guarantee pulled a card but no scene remains. | Guarantee fails and is recorded; nothing is invented. |
| 2 | AMB-05 | Rail overflow with no non-GLOBAL GM card on the rail. | Evict the oldest non-GLOBAL card of any kind. |
| 2 | AMB-06 | Interrupt with no unused prepared Beat Frame. | Engine picks an unused starter-library frame by seeded RNG. |
| 1 | AMB-24 | A clock fills mid-scene: when does its Beat Frame happen? | It is queued for the start of the next scene. |

## Referee friction points (all runs)


## Player one-sentence verdicts on backstory use


## Run status

| Run | Status | Scenes | Draws | Tokens | Error |
| --- | --- | --- | --- | --- | --- |
| scripted-mc-01__A__s63850__r0 | complete | 3 | 5 | 0 |  |
| scripted-mc-01__A__s63851__r1 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__A__s63852__r2 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__A__s63853__r3 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__A__s63854__r4 | complete | 5 | 5 | 0 |  |
| scripted-mc-01__A__s63855__r5 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__A__s63856__r6 | complete | 3 | 6 | 0 |  |
| scripted-mc-01__A__s63857__r7 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__A__s63858__r8 | complete | 4 | 5 | 0 |  |
| scripted-mc-01__A__s63859__r9 | complete | 4 | 5 | 0 |  |
| scripted-mc-01__A__s63860__r10 | complete | 5 | 7 | 0 |  |
| scripted-mc-01__A__s63861__r11 | complete | 4 | 5 | 0 |  |
| scripted-mc-01__A__s63862__r12 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__A__s63863__r13 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__A__s63864__r14 | complete | 4 | 5 | 0 |  |
| scripted-mc-01__A__s63865__r15 | complete | 5 | 5 | 0 |  |
| scripted-mc-01__A__s63866__r16 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__A__s63867__r17 | complete | 4 | 7 | 0 |  |
| scripted-mc-01__A__s63868__r18 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__A__s63869__r19 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__A__s63870__r20 | complete | 5 | 5 | 0 |  |
| scripted-mc-01__A__s63871__r21 | complete | 4 | 5 | 0 |  |
| scripted-mc-01__A__s63872__r22 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__A__s63873__r23 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__A__s63874__r24 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__A__s63875__r25 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__A__s63876__r26 | complete | 4 | 5 | 0 |  |
| scripted-mc-01__A__s63877__r27 | complete | 5 | 7 | 0 |  |
| scripted-mc-01__A__s63878__r28 | complete | 4 | 5 | 0 |  |
| scripted-mc-01__A__s63879__r29 | complete | 3 | 6 | 0 |  |
| scripted-mc-01__A__s63880__r30 | complete | 3 | 6 | 0 |  |
| scripted-mc-01__A__s63881__r31 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__A__s63882__r32 | complete | 5 | 5 | 0 |  |
| scripted-mc-01__A__s63883__r33 | complete | 5 | 7 | 0 |  |
| scripted-mc-01__A__s63884__r34 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__A__s63885__r35 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__A__s63886__r36 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__A__s63887__r37 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__A__s63888__r38 | complete | 4 | 7 | 0 |  |
| scripted-mc-01__A__s63889__r39 | complete | 3 | 6 | 0 |  |
| scripted-mc-01__B__s63850__r0 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63851__r1 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63852__r2 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63853__r3 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63854__r4 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63855__r5 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63856__r6 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63857__r7 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63858__r8 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63859__r9 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63860__r10 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63861__r11 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63862__r12 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63863__r13 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63864__r14 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63865__r15 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63866__r16 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63867__r17 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63868__r18 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63869__r19 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63870__r20 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63871__r21 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63872__r22 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63873__r23 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63874__r24 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63875__r25 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63876__r26 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63877__r27 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63878__r28 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63879__r29 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63880__r30 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63881__r31 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63882__r32 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63883__r33 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63884__r34 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63885__r35 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63886__r36 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63887__r37 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63888__r38 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__B__s63889__r39 | complete | 5 | 0 | 0 |  |
| scripted-mc-01__C__s63850__r0 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63851__r1 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63852__r2 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63853__r3 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63854__r4 | complete | 3 | 5 | 0 |  |
| scripted-mc-01__C__s63855__r5 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63856__r6 | complete | 4 | 5 | 0 |  |
| scripted-mc-01__C__s63857__r7 | complete | 5 | 4 | 0 |  |
| scripted-mc-01__C__s63858__r8 | complete | 4 | 5 | 0 |  |
| scripted-mc-01__C__s63859__r9 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__C__s63860__r10 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__C__s63861__r11 | complete | 5 | 4 | 0 |  |
| scripted-mc-01__C__s63862__r12 | complete | 5 | 7 | 0 |  |
| scripted-mc-01__C__s63863__r13 | complete | 5 | 4 | 0 |  |
| scripted-mc-01__C__s63864__r14 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__C__s63865__r15 | complete | 5 | 3 | 0 |  |
| scripted-mc-01__C__s63866__r16 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63867__r17 | complete | 5 | 5 | 0 |  |
| scripted-mc-01__C__s63868__r18 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63869__r19 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__C__s63870__r20 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__C__s63871__r21 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63872__r22 | complete | 4 | 5 | 0 |  |
| scripted-mc-01__C__s63873__r23 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63874__r24 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__C__s63875__r25 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63876__r26 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__C__s63877__r27 | complete | 3 | 5 | 0 |  |
| scripted-mc-01__C__s63878__r28 | complete | 5 | 5 | 0 |  |
| scripted-mc-01__C__s63879__r29 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63880__r30 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63881__r31 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__C__s63882__r32 | complete | 3 | 6 | 0 |  |
| scripted-mc-01__C__s63883__r33 | complete | 3 | 5 | 0 |  |
| scripted-mc-01__C__s63884__r34 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__C__s63885__r35 | complete | 5 | 6 | 0 |  |
| scripted-mc-01__C__s63886__r36 | complete | 5 | 7 | 0 |  |
| scripted-mc-01__C__s63887__r37 | complete | 3 | 5 | 0 |  |
| scripted-mc-01__C__s63888__r38 | complete | 4 | 6 | 0 |  |
| scripted-mc-01__C__s63889__r39 | complete | 4 | 7 | 0 |  |
