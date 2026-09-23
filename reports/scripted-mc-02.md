# Batch report: scripted-mc-02

Runs: 120 ({'complete': 120}). Spec version(s): ['0.2.0']. Backend(s): ['scripted']. Tokens: 0 (≈ $0.00).

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
| Every player's backstory drove an event | 1.00 [1.00, 1.00] (n=40) | 0.05 [0.00, 0.12] (n=40) | 0.03 [0.00, 0.07] (n=40) |
| Every player's own card surfaced from the deck | 1.00 [1.00, 1.00] (n=40) | — | — |
| Deck draws / session (target 5–8) | 5.70 [5.33, 6.00] (n=40) | 0.00 [0.00, 0.00] (n=40) | 5.80 [5.55, 6.05] (n=40) |
| Draw costs using the drawn card: engine tag check | 1.00 [1.00, 1.00] (n=40) | — | 1.00 [0.99, 1.00] (n=40) |
| Draw costs using the drawn card: referee judgment | 1.00 [1.00, 1.00] (n=40) | — | 1.00 [0.99, 1.00] (n=40) |
| Mean player FP at session end (target 1–5) | 2.90 [2.63, 3.17] (n=40) | 2.41 [2.14, 2.67] (n=40) | 2.67 [2.37, 2.98] (n=40) |
| Spotlight Gini: turns | 0.08 [0.07, 0.10] (n=40) | 0.08 [0.06, 0.09] (n=40) | 0.08 [0.07, 0.10] (n=40) |
| Spotlight Gini: invokes | 0.36 [0.32, 0.40] (n=40) | 0.38 [0.32, 0.43] (n=40) | 0.34 [0.28, 0.40] (n=40) |
| Scenes / session | 4.38 [4.15, 4.60] (n=40) | 5.00 [5.00, 5.00] (n=40) | 4.28 [4.10, 4.45] (n=40) |
| Clock marks | 5.65 [4.53, 6.83] (n=40) | 2.25 [1.52, 3.02] (n=40) | 5.50 [4.72, 6.35] (n=40) |
| Compels accepted | 4.22 [3.77, 4.70] (n=40) | 1.62 [1.30, 1.98] (n=40) | 4.30 [3.83, 4.80] (n=40) |
| Compels refused | 1.90 [1.60, 2.23] (n=40) | 0.88 [0.60, 1.18] (n=40) | 2.15 [1.80, 2.50] (n=40) |
| GM-improvised complications | 2.20 [1.88, 2.52] (n=40) | 6.85 [5.97, 7.72] (n=40) | 2.50 [2.02, 3.02] (n=40) |
| Card-supplied complications | 9.60 [9.25, 9.93] (n=40) | 0.00 [0.00, 0.00] (n=40) | 9.75 [9.47, 10.00] (n=40) |
| Improvisation share | 0.18 [0.16, 0.21] (n=40) | 1.00 [1.00, 1.00] (n=40) | 0.19 [0.16, 0.22] (n=40) |
| Rule violations (engine + referee) | 0.95 [0.57, 1.35] (n=40) | 0.45 [0.25, 0.65] (n=40) | 1.23 [0.82, 1.73] (n=40) |
|   — engine refusals | 0.95 [0.57, 1.35] (n=40) | 0.45 [0.25, 0.65] (n=40) | 1.23 [0.82, 1.73] (n=40) |
|   — referee | 0.00 [0.00, 0.00] (n=40) | 0.00 [0.00, 0.00] (n=40) | 0.00 [0.00, 0.00] (n=40) |
| Ambiguity records | 9.95 [9.10, 10.80] (n=40) | 1.82 [1.50, 2.20] (n=40) | 9.60 [8.90, 10.38] (n=40) |
| Backstory guarantee failures | 0.00 [0.00, 0.00] (n=40) | 0.00 [0.00, 0.00] (n=40) | 0.00 [0.00, 0.00] (n=40) |
| Within-session variance of involvement | — | — | — |
| Compel accept ratio | 0.69 | 0.65 | 0.667 |
| Tension values seen | {1: 4, 2: 11, 3: 78, 4: 73, 5: 31, 6: 18} | {} | {2: 7, 3: 99, 4: 51, 5: 37, 6: 17} |

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

- **A**: instigator 1.35/2.2/2.55; lurker 1.4/1.3/3.4; method_actor 1.6/1.6/3.6; optimizer 1.2/2.7/1.95; protector 1.55/1.05/3.8; rules_lawyer 0.75/2.9/1.25; storyteller 2.15/1.05/4.4; tactician 1.05/2.3/2.25
- **B**: instigator 0.45/1.7/2.45; lurker 0.5/1/2.7; method_actor 0.7/1.35/2.9; optimizer 0.55/2.6/1.65; protector 0.45/1.85/2.1; rules_lawyer 0.35/2.1/1.85; storyteller 0.55/1.1/3.15; tactician 1.15/2.3/2.5
- **C**: instigator 0.8/2/2.25; lurker 1.45/1.3/3.4; method_actor 1.85/0.85/4.45; optimizer 1.2/3.4/1.45; protector 1.2/1.35/3; rules_lawyer 0.5/3/1.1; storyteller 1.7/0.9/4.35; tactician 0.85/3/1.35

### Complaint clusters (keyword buckets over 'most frustrating')

- **A**: {}
- **B**: {}
- **C**: {}

## Ambiguities

| Count | ID / section | Issue | Interim ruling |
| --- | --- | --- | --- |
| 120 | AMB-12 | Stress box values are unspecified. | Fate Core: boxes 1 and 2; Physique/Will +1/+2 adds a 3 box, +3 or more adds 3 and 4. |
| 82 | AMB-27 | Success with style on create advantage: the aspect's 2 free invokes AND the deck peek, or one of them? | Both: the aspect keeps 2 free invokes and the player may also peek. |
| 82 | AMB-16 | A draw is required but the deck is empty outside a climax. | The cost uses a face-up GM tag, as in a climax. |
| 80 | AMB-01 | Arm A lists 'Attention', which the spec never defines. | Not modelled. |
| 80 | AMB-22 | Does a GLOBAL anchor give the GM a free invoke like a GM card? | Yes, GLOBAL cards placed on the rail give the GM 1 free invoke that scene. |
| 60 | AMB-03 | Does the session end after the climax scene? | Yes: the climax scene is the last scene of the session. |
| 59 | AMB-26 | Several Beat Frames are queued for the same scene. | One per scene; the guarantee frame first, the rest carry to later scenes. |
| 56 | AMB-23 | Success at major cost on an attack: how much harm lands? | The attack lands for 1 shift. |
| 56 | AMB-14 | Who decides a beat 'went badly' for its stakes clock? | GM agent reports it at scene end; the Referee audits it. |
| 53 | AMB-10 | Growth from 'roll fails after one of its tags was invoked' — invoked by whom? | Owner's own invokes only. |
| 46 | AMB-04 | Do tension adjustment rows stack? | All applicable rows are summed, then clamped to 1-6. |
| 36 | AMB-19 | Tie on an attack: 'success at minor cost' but 0 shifts of harm. | Attacker gets a boost (Fate Core) and the deck draw still happens. |
| 32 | AMB-20 | §6 Altered scene draws a card, but §4's closed list of draw triggers omits it. | §6 is more specific: Altered scenes draw. |
| 6 | AMB-05 | Rail overflow with no non-GLOBAL GM card on the rail. | Evict the oldest non-GLOBAL card of any kind. |
| 5 | AMB-06 | Interrupt with no unused prepared Beat Frame. | Engine picks an unused starter-library frame by seeded RNG. |
| 2 | AMB-24 | A clock fills mid-scene: when does its Beat Frame happen? | It is queued for the start of the next scene. |

## Referee friction points (all runs)


## Player one-sentence verdicts on backstory use


## Run status

| Run | Status | Scenes | Draws | Tokens | Error |
| --- | --- | --- | --- | --- | --- |
| scripted-mc-02__A__s63850__r0 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__A__s63851__r1 | complete | 5 | 7 | 0 |  |
| scripted-mc-02__A__s63852__r2 | complete | 5 | 7 | 0 |  |
| scripted-mc-02__A__s63853__r3 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__A__s63854__r4 | complete | 4 | 5 | 0 |  |
| scripted-mc-02__A__s63855__r5 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__A__s63856__r6 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__A__s63857__r7 | complete | 5 | 7 | 0 |  |
| scripted-mc-02__A__s63858__r8 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__A__s63859__r9 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__A__s63860__r10 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__A__s63861__r11 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__A__s63862__r12 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__A__s63863__r13 | complete | 5 | 3 | 0 |  |
| scripted-mc-02__A__s63864__r14 | complete | 5 | 7 | 0 |  |
| scripted-mc-02__A__s63865__r15 | complete | 5 | 2 | 0 |  |
| scripted-mc-02__A__s63866__r16 | complete | 4 | 7 | 0 |  |
| scripted-mc-02__A__s63867__r17 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__A__s63868__r18 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__A__s63869__r19 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__A__s63870__r20 | complete | 4 | 5 | 0 |  |
| scripted-mc-02__A__s63871__r21 | complete | 3 | 5 | 0 |  |
| scripted-mc-02__A__s63872__r22 | complete | 5 | 7 | 0 |  |
| scripted-mc-02__A__s63873__r23 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__A__s63874__r24 | complete | 4 | 5 | 0 |  |
| scripted-mc-02__A__s63875__r25 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__A__s63876__r26 | complete | 4 | 5 | 0 |  |
| scripted-mc-02__A__s63877__r27 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__A__s63878__r28 | complete | 4 | 5 | 0 |  |
| scripted-mc-02__A__s63879__r29 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__A__s63880__r30 | complete | 3 | 5 | 0 |  |
| scripted-mc-02__A__s63881__r31 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__A__s63882__r32 | complete | 3 | 6 | 0 |  |
| scripted-mc-02__A__s63883__r33 | complete | 5 | 5 | 0 |  |
| scripted-mc-02__A__s63884__r34 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__A__s63885__r35 | complete | 5 | 3 | 0 |  |
| scripted-mc-02__A__s63886__r36 | complete | 4 | 5 | 0 |  |
| scripted-mc-02__A__s63887__r37 | complete | 3 | 7 | 0 |  |
| scripted-mc-02__A__s63888__r38 | complete | 3 | 6 | 0 |  |
| scripted-mc-02__A__s63889__r39 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__B__s63850__r0 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63851__r1 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63852__r2 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63853__r3 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63854__r4 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63855__r5 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63856__r6 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63857__r7 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63858__r8 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63859__r9 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63860__r10 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63861__r11 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63862__r12 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63863__r13 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63864__r14 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63865__r15 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63866__r16 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63867__r17 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63868__r18 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63869__r19 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63870__r20 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63871__r21 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63872__r22 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63873__r23 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63874__r24 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63875__r25 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63876__r26 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63877__r27 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63878__r28 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63879__r29 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63880__r30 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63881__r31 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63882__r32 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63883__r33 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63884__r34 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63885__r35 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63886__r36 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63887__r37 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63888__r38 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__B__s63889__r39 | complete | 5 | 0 | 0 |  |
| scripted-mc-02__C__s63850__r0 | complete | 4 | 5 | 0 |  |
| scripted-mc-02__C__s63851__r1 | complete | 3 | 5 | 0 |  |
| scripted-mc-02__C__s63852__r2 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63853__r3 | complete | 5 | 7 | 0 |  |
| scripted-mc-02__C__s63854__r4 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63855__r5 | complete | 4 | 5 | 0 |  |
| scripted-mc-02__C__s63856__r6 | complete | 4 | 7 | 0 |  |
| scripted-mc-02__C__s63857__r7 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63858__r8 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__C__s63859__r9 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__C__s63860__r10 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63861__r11 | complete | 5 | 4 | 0 |  |
| scripted-mc-02__C__s63862__r12 | complete | 4 | 5 | 0 |  |
| scripted-mc-02__C__s63863__r13 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63864__r14 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63865__r15 | complete | 5 | 7 | 0 |  |
| scripted-mc-02__C__s63866__r16 | complete | 3 | 5 | 0 |  |
| scripted-mc-02__C__s63867__r17 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__C__s63868__r18 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63869__r19 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63870__r20 | complete | 5 | 5 | 0 |  |
| scripted-mc-02__C__s63871__r21 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63872__r22 | complete | 5 | 5 | 0 |  |
| scripted-mc-02__C__s63873__r23 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__C__s63874__r24 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63875__r25 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63876__r26 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63877__r27 | complete | 5 | 7 | 0 |  |
| scripted-mc-02__C__s63878__r28 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63879__r29 | complete | 3 | 6 | 0 |  |
| scripted-mc-02__C__s63880__r30 | complete | 4 | 7 | 0 |  |
| scripted-mc-02__C__s63881__r31 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63882__r32 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63883__r33 | complete | 4 | 6 | 0 |  |
| scripted-mc-02__C__s63884__r34 | complete | 5 | 4 | 0 |  |
| scripted-mc-02__C__s63885__r35 | complete | 5 | 4 | 0 |  |
| scripted-mc-02__C__s63886__r36 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__C__s63887__r37 | complete | 4 | 5 | 0 |  |
| scripted-mc-02__C__s63888__r38 | complete | 5 | 6 | 0 |  |
| scripted-mc-02__C__s63889__r39 | complete | 4 | 7 | 0 |  |
