# Batch report: scripted-v03

Runs: 22 ({'complete': 22}). Spec version(s): ['0.3.0']. Backend(s): ['scripted']. Tokens: 0 (≈ $0.00).

## Blind per-session judge (compiled after unblinding)

_Each session was scored alone by a judge that saw only the story (no mechanics lines, and no deck, card or tension vocabulary or card IDs) under a random session ID. Scores were joined to arms only afterwards._

| Score (1–10) | A (20 sessions) | B (1 sessions) | C (1 sessions) |
| --- | --- | --- | --- |
| overall | 5.55 [4.75, 6.35] (n=20) | 6.00 (n=1) | 5.00 (n=1) |
| engagement | 5.15 [4.40, 5.95] (n=20) | 4.00 (n=1) | 6.00 (n=1) |
| coherence | 5.55 [4.75, 6.35] (n=20) | 7.00 (n=1) | 5.00 (n=1) |
| spotlight_fairness | 5.75 [4.90, 6.55] (n=20) | 3.00 (n=1) | 4.00 (n=1) |
| player_agency | 5.90 [5.20, 6.55] (n=20) | 5.00 (n=1) | 4.00 (n=1) |
| complication_quality | 5.55 [4.80, 6.30] (n=20) | 5.00 (n=1) | 6.00 (n=1) |
| backstory_score | 5.44 [5.09, 5.80] (n=80) | 6.25 [4.75, 7.50] (n=4) | 4.50 [3.00, 6.75] (n=4) |
| backstory_used_rate | 0.69 [0.59, 0.79] (n=80) | 0.50 [0.00, 1.00] (n=4) | 0.00 [0.00, 0.00] (n=4) |
| all_players_backstory_used | 0.25 [0.10, 0.45] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| lurker_backstory_score | 4.90 [3.80, 6.10] (n=10) | — | — |

_Synthetic (scripted backend): these judge scores are random placeholders._


## Structural metrics (per session, mean [95% bootstrap CI])

| Metric | A | B | C |
| --- | --- | --- | --- |
| Every player's backstory drove an event | 1.00 [1.00, 1.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Every player's own card surfaced from the deck | 1.00 [1.00, 1.00] (n=20) | — | — |
| Deck draws / session (target 5–8) | 5.80 [5.55, 6.05] (n=20) | 0.00 (n=1) | 5.00 (n=1) |
| Draw costs using the drawn card: engine tag check | 1.00 [1.00, 1.00] (n=20) | — | 1.00 (n=1) |
| Draw costs whose text uses the tag (after rewrite) | 1.00 [1.00, 1.00] (n=20) | — | 1.00 (n=1) |
| Draw costs that needed a GM rewrite | 0.00 [0.00, 0.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Draw costs using the drawn card: referee judgment | 1.00 [1.00, 1.00] (n=20) | — | 1.00 (n=1) |
| Minutes per session | 0.00 [0.00, 0.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Cost per session (USD) | 0.00 [0.00, 0.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Mean player FP at session end (target 1–5) | 2.33 [1.94, 2.71] (n=20) | 2.50 (n=1) | 3.50 (n=1) |
| Spotlight Gini: turns | 0.09 [0.06, 0.11] (n=20) | 0.03 (n=1) | 0.06 (n=1) |
| Spotlight Gini: invokes | 0.34 [0.27, 0.42] (n=20) | 0.50 (n=1) | 0.25 (n=1) |
| Scenes / session | 4.65 [4.35, 4.85] (n=20) | 5.00 (n=1) | 4.00 (n=1) |
| Clock marks | 4.90 [3.80, 6.00] (n=20) | 0.00 (n=1) | 5.00 (n=1) |
| Compels accepted | 4.55 [3.90, 5.20] (n=20) | 4.00 (n=1) | 4.00 (n=1) |
| Compels refused | 1.85 [1.45, 2.25] (n=20) | 1.00 (n=1) | 2.00 (n=1) |
| GM-improvised complications | 2.40 [1.75, 3.10] (n=20) | 6.00 (n=1) | 2.00 (n=1) |
| Card-supplied complications | 9.70 [9.30, 10.05] (n=20) | 0.00 (n=1) | 10.00 (n=1) |
| Improvisation share | 0.18 [0.14, 0.23] (n=20) | 1.00 (n=1) | 0.17 (n=1) |
| Rule violations (engine + referee) | 1.25 [0.55, 2.10] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
|   — engine refusals | 1.25 [0.55, 2.10] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
|   — referee | 0.00 [0.00, 0.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Ambiguity records | 8.85 [7.40, 10.40] (n=20) | 1.00 (n=1) | 8.00 (n=1) |
| Backstory guarantee failures | 0.00 [0.00, 0.00] (n=20) | 0.00 (n=1) | 0.00 (n=1) |
| Within-session variance of involvement | — | — | — |
| Compel accept ratio | 0.711 | 0.8 | 0.667 |
| Tension values seen | {1: 43, 2: 34, 3: 32, 4: 4} | {} | {1: 3, 2: 1, 3: 1} |

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

- **A**: instigator 1.4/2.6/1.8; lurker 1.5/1.3/3.2; method_actor 2.3/1.3/4; optimizer 1.7/3.8/0.9; protector 2.3/2/3.3; rules_lawyer 1.3/3.7/0.6; storyteller 1.6/1.7/2.9; tactician 1.5/2.6/1.9
- **B**: instigator 1/2/2; optimizer 0/0/3; protector 2/1/4; tactician 2/4/1
- **C**: instigator 1/2/2; optimizer 2/3/2; protector 3/0/6; tactician 2/1/4

### Complaint clusters (keyword buckets over 'most frustrating')

- **A**: {}
- **B**: {}
- **C**: {}

## Ambiguities

| Count | ID / section | Issue | Interim ruling |
| --- | --- | --- | --- |
| 29 | AMB-27 | Success with style on create advantage: the aspect's 2 free invokes AND the deck peek, or one of them? | Both: the aspect keeps 2 free invokes and the player may also peek. |
| 22 | AMB-12 | Stress box values are unspecified. | Fate Core: boxes 1 and 2; Physique/Will +1/+2 adds a 3 box, +3 or more adds 3 and 4. |
| 21 | AMB-01 | Arm A lists 'Attention', which the spec never defines. | Not modelled. |
| 21 | AMB-22 | Does a GLOBAL anchor give the GM a free invoke like a GM card? | Yes, GLOBAL cards placed on the rail give the GM 1 free invoke that scene. |
| 16 | AMB-10 | Growth from 'roll fails after one of its tags was invoked' — invoked by whom? | Owner's own invokes only. |
| 14 | AMB-03 | Does the session end after the climax scene? | Yes: the climax scene is the last scene of the session. |
| 14 | AMB-26 | Several Beat Frames are queued for the same scene. | One per scene; the guarantee frame first, the rest carry to later scenes. |
| 13 | AMB-23 | Success at major cost on an attack: how much harm lands? | The attack lands for 1 shift. |
| 13 | AMB-16 | A draw is required but the deck is empty outside a climax. | The cost uses a face-up GM tag, as in a climax. |
| 9 | AMB-19 | Tie on an attack: 'success at minor cost' but 0 shifts of harm. | Attacker gets a boost (Fate Core) and the deck draw still happens. |
| 7 | AMB-14 | Who decides a beat 'went badly' for its stakes clock? | GM agent reports it at scene end; the Referee audits it. |
| 4 | AMB-20 | §6 Altered scene draws a card, but §4's closed list of draw triggers omits it. | §6 is more specific: Altered scenes draw. |
| 3 | AMB-05 | Rail overflow with no non-GLOBAL GM card on the rail. | Evict the oldest non-GLOBAL card of any kind. |

## Referee friction points (all runs)


## Player one-sentence verdicts on backstory use


## Run status

| Run | Status | Scenes | Draws | Tokens | Error |
| --- | --- | --- | --- | --- | --- |
| scripted-v03__A__s77806__r0 | complete | 3 | 6 | 0 |  |
| scripted-v03__A__s77807__r1 | complete | 5 | 6 | 0 |  |
| scripted-v03__A__s77808__r2 | complete | 4 | 5 | 0 |  |
| scripted-v03__A__s77809__r3 | complete | 4 | 6 | 0 |  |
| scripted-v03__A__s77810__r4 | complete | 5 | 6 | 0 |  |
| scripted-v03__A__s77811__r5 | complete | 4 | 5 | 0 |  |
| scripted-v03__A__s77812__r6 | complete | 5 | 6 | 0 |  |
| scripted-v03__A__s77813__r7 | complete | 5 | 6 | 0 |  |
| scripted-v03__A__s77814__r8 | complete | 5 | 5 | 0 |  |
| scripted-v03__A__s77815__r9 | complete | 5 | 6 | 0 |  |
| scripted-v03__A__s77816__r10 | complete | 5 | 6 | 0 |  |
| scripted-v03__A__s77817__r11 | complete | 5 | 6 | 0 |  |
| scripted-v03__A__s77818__r12 | complete | 5 | 6 | 0 |  |
| scripted-v03__A__s77819__r13 | complete | 5 | 5 | 0 |  |
| scripted-v03__A__s77820__r14 | complete | 4 | 7 | 0 |  |
| scripted-v03__A__s77821__r15 | complete | 5 | 5 | 0 |  |
| scripted-v03__A__s77822__r16 | complete | 5 | 6 | 0 |  |
| scripted-v03__A__s77823__r17 | complete | 4 | 5 | 0 |  |
| scripted-v03__A__s77824__r18 | complete | 5 | 6 | 0 |  |
| scripted-v03__A__s77825__r19 | complete | 5 | 7 | 0 |  |
| scripted-v03__B__s77806__r0 | complete | 5 | 0 | 0 |  |
| scripted-v03__C__s77806__r0 | complete | 4 | 5 | 0 |  |
