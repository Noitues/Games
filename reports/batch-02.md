# Batch report: batch-02

Runs: 12 ({'complete': 12}). Spec version(s): ['0.3.1']. Backend(s): ['claude_cli']. Tokens: 18,884,649 (≈ $46.17).

## Blind per-session judge (compiled after unblinding)

_Each session was scored alone by a judge that saw only the story (no mechanics lines, and no deck, card or tension vocabulary or card IDs) under a random session ID. Scores were joined to arms only afterwards._

| Score (1–10) | A (10 sessions) | B (1 sessions) | C (1 sessions) |
| --- | --- | --- | --- |
| overall | 6.70 [6.40, 7.00] (n=10) | 6.00 (n=1) | 5.00 (n=1) |
| engagement | 6.80 [6.50, 7.00] (n=10) | 6.00 (n=1) | 5.00 (n=1) |
| coherence | 7.10 [6.30, 7.70] (n=10) | 7.00 (n=1) | 7.00 (n=1) |
| spotlight_fairness | 7.30 [6.60, 8.00] (n=10) | 6.00 (n=1) | 8.00 (n=1) |
| player_agency | 6.10 [5.70, 6.50] (n=10) | 5.00 (n=1) | 4.00 (n=1) |
| complication_quality | 6.60 [6.00, 7.10] (n=10) | 7.00 (n=1) | 5.00 (n=1) |
| backstory_score | 7.70 [7.33, 8.00] (n=40) | 8.00 [7.25, 8.75] (n=4) | 7.25 [7.00, 7.75] (n=4) |
| backstory_used_rate | 1.00 [1.00, 1.00] (n=40) | 1.00 [1.00, 1.00] (n=4) | 1.00 [1.00, 1.00] (n=4) |
| all_players_backstory_used | 1.00 [1.00, 1.00] (n=10) | 1.00 (n=1) | 1.00 (n=1) |
| lurker_backstory_score | 6.00 [4.80, 7.20] (n=5) | — | — |


## Structural metrics (per session, mean [95% bootstrap CI])

| Metric | A | B | C |
| --- | --- | --- | --- |
| Every player's backstory drove an event | 1.00 [1.00, 1.00] (n=10) | 0.00 (n=1) | 0.00 (n=1) |
| Every player's own card surfaced from the deck | 1.00 [1.00, 1.00] (n=10) | — | — |
| Deck draws / session (target 5–8) | 4.60 [3.60, 5.50] (n=10) | 0.00 (n=1) | 6.00 (n=1) |
| Draw costs using the drawn card: engine tag check | 0.99 [0.97, 1.00] (n=10) | — | 1.00 (n=1) |
| Draw costs whose text uses the tag (after rewrite) | 0.96 [0.91, 1.00] (n=10) | — | 1.00 (n=1) |
| Draw costs that needed a GM rewrite | 4.50 [3.60, 5.50] (n=10) | 0.00 (n=1) | 4.00 (n=1) |
| Draw costs using the drawn card: referee judgment | 0.90 [0.82, 0.97] (n=10) | 0.00 (n=1) | 0.92 (n=1) |
| Minutes per session | 32.41 [28.93, 37.18] (n=10) | 23.50 (n=1) | 29.00 (n=1) |
| Cost per session (USD) | 4.00 [3.71, 4.33] (n=10) | 2.92 (n=1) | 3.29 (n=1) |
| Mean player FP at session end (target 1–5) | 2.92 [2.62, 3.17] (n=10) | 3.25 (n=1) | 2.00 (n=1) |
| Spotlight Gini: turns | 0.03 [0.01, 0.07] (n=10) | 0.00 (n=1) | 0.00 (n=1) |
| Spotlight Gini: invokes | 0.38 [0.29, 0.47] (n=10) | 0.34 (n=1) | 0.25 (n=1) |
| Scenes / session | 5.00 [5.00, 5.00] (n=10) | 5.00 (n=1) | 5.00 (n=1) |
| Clock marks | 1.90 [1.00, 2.80] (n=10) | 0.00 (n=1) | 3.00 (n=1) |
| Compels accepted | 5.30 [4.30, 6.20] (n=10) | 8.00 (n=1) | 4.00 (n=1) |
| Compels refused | 1.10 [0.50, 1.70] (n=10) | 0.00 (n=1) | 1.00 (n=1) |
| GM-improvised complications | 2.40 [1.40, 3.40] (n=10) | 9.00 (n=1) | 1.00 (n=1) |
| Card-supplied complications | 9.70 [9.00, 10.40] (n=10) | 0.00 (n=1) | 11.00 (n=1) |
| Improvisation share | 0.19 [0.12, 0.26] (n=10) | 1.00 (n=1) | 0.08 (n=1) |
| Rule violations (engine + referee) | 4.80 [3.80, 6.10] (n=10) | 2.00 (n=1) | 3.00 (n=1) |
|   — engine refusals | 2.50 [1.50, 3.70] (n=10) | 2.00 (n=1) | 3.00 (n=1) |
|   — referee | 2.30 [1.50, 3.00] (n=10) | 0.00 (n=1) | 0.00 (n=1) |
| Ambiguity records | 10.60 [9.40, 11.60] (n=10) | 3.00 (n=1) | 15.00 (n=1) |
| Backstory guarantee failures | 0.00 [0.00, 0.00] (n=10) | 0.00 (n=1) | 0.00 (n=1) |
| Within-session variance of involvement | 0.33 [0.18, 0.48] (n=10) | 0.25 (n=1) | 0.19 (n=1) |
| Compel accept ratio | 0.828 | 1.0 | 0.8 |
| Tension values seen | {2: 8, 3: 24, 4: 16, 5: 9, 6: 3} | {} | {2: 1, 3: 4, 4: 1} |

## Experiential (LLM player self-reports, 1–7; weak evidence)

| Score | A | B | C |
| --- | --- | --- | --- |
| fun | 6.25 [6.08, 6.42] (n=40) | 6.25 [6.00, 6.75] (n=4) | 6.50 [6.00, 7.00] (n=4) |
| involvement | 6.40 [6.20, 6.60] (n=40) | 6.50 [6.00, 7.00] (n=4) | 6.75 [6.25, 7.00] (n=4) |
| connection | 6.60 [6.38, 6.80] (n=40) | 6.00 [5.00, 7.00] (n=4) | 7.00 [7.00, 7.00] (n=4) |
| control | 5.50 [5.33, 5.67] (n=40) | 5.25 [5.00, 5.75] (n=4) | 6.00 [5.25, 6.75] (n=4) |
| play_again | 6.90 [6.80, 6.97] (n=40) | 7.00 [7.00, 7.00] (n=4) | 7.00 [7.00, 7.00] (n=4) |

### Paired differences (same seed, same character and personality)

- **A-B**: involvement 0.25 [0.00, 0.75] (n=4); connection 0.75 [0.00, 1.75] (n=4); fun 0.25 [0.00, 0.75] (n=4); control 0.50 [0.00, 1.00] (n=4)
- **A-C**: involvement 0.00 [-0.75, 0.75] (n=4); connection -0.25 [-0.75, 0.00] (n=4); fun 0.00 [-0.75, 0.75] (n=4); control -0.25 [-1.00, 0.50] (n=4)
- **C-B**: involvement 0.25 [-0.50, 1.00] (n=4); connection 1.00 [0.00, 2.00] (n=4); fun 0.25 [0.00, 0.75] (n=4); control 0.75 [0.25, 1.00] (n=4)

Lurker involvement by arm: A 5.40 [5.00, 5.80] (n=5)

### Survey means by personality

| Personality | A involvement | B involvement | C involvement | A connection | B connection | C connection |
| --- | --- | --- | --- | --- | --- | --- |
| instigator | 6.80 [6.40, 7.00] (n=5) | 7.00 (n=1) | 7.00 (n=1) | 6.80 [6.40, 7.00] (n=5) | 7.00 (n=1) | 7.00 (n=1) |
| lurker | 5.40 [5.00, 5.80] (n=5) | — | — | 5.80 [5.20, 6.40] (n=5) | — | — |
| method_actor | 6.60 [6.20, 7.00] (n=5) | — | — | 6.80 [6.40, 7.00] (n=5) | — | — |
| optimizer | 6.60 [6.20, 7.00] (n=5) | 7.00 (n=1) | 6.00 (n=1) | 6.80 [6.40, 7.00] (n=5) | 7.00 (n=1) | 7.00 (n=1) |
| protector | 6.60 [6.20, 7.00] (n=5) | 6.00 (n=1) | 7.00 (n=1) | 6.60 [5.80, 7.00] (n=5) | 5.00 (n=1) | 7.00 (n=1) |
| rules_lawyer | 6.40 [6.00, 6.80] (n=5) | — | — | 6.80 [6.40, 7.00] (n=5) | — | — |
| storyteller | 6.60 [6.20, 7.00] (n=5) | — | — | 7.00 [7.00, 7.00] (n=5) | — | — |
| tactician | 6.20 [6.00, 6.60] (n=5) | 6.00 (n=1) | 7.00 (n=1) | 6.20 [5.60, 6.80] (n=5) | 5.00 (n=1) | 7.00 (n=1) |

### Paired transcript preference (blinded, same cohort and seed)

- not run

### Fate point flow by personality (mean per session: earned / spent / end)

- **A**: instigator 1.6/2.6/2; lurker 1.4/1.4/3; method_actor 1.8/1.8/3; optimizer 1.2/0.2/4; protector 2.2/1.2/4; rules_lawyer 0.8/2.4/1.4; storyteller 2.2/1.2/4; tactician 0.8/1.8/2
- **B**: instigator 5/4/4; optimizer 5/1/7; protector 0/3/0; tactician 0/1/2
- **C**: instigator 1/3/1; optimizer 2/0/5; protector 1/4/0; tactician 1/2/2

### Complaint clusters (keyword buckets over 'most frustrating')

- **A**: {'other': 18, 'agency/control': 11, 'rules/confusion': 6, 'dice/luck': 4, 'spotlight/ignored': 3, 'pacing': 1}
- **B**: {'agency/control': 2, 'rules/confusion': 1, 'other': 1}
- **C**: {'rules/confusion': 1, 'dice/luck': 1, 'agency/control': 1, 'other': 1, 'pacing': 1}

## Ambiguities

| Count | ID / section | Issue | Interim ruling |
| --- | --- | --- | --- |
| 37 | AMB-27 | Success with style on create advantage: the aspect's 2 free invokes AND the deck peek, or one of them? | Both: the aspect keeps 2 free invokes and the player may also peek. |
| 12 | AMB-12 | Stress box values are unspecified. | Fate Core: boxes 1 and 2; Physique/Will +1/+2 adds a 3 box, +3 or more adds 3 and 4. |
| 11 | AMB-01 | Arm A lists 'Attention', which the spec never defines. | Not modelled. |
| 11 | AMB-22 | Does a GLOBAL anchor give the GM a free invoke like a GM card? | Yes, GLOBAL cards placed on the rail give the GM 1 free invoke that scene. |
| 9 | AMB-20 | §6 Altered scene draws a card, but §4's closed list of draw triggers omits it. | §6 is more specific: Altered scenes draw. |
| 4 | AMB-26 | Several Beat Frames are queued for the same scene. | One per scene; the guarantee frame first, the rest carry to later scenes. |
| 3 | AMB-03 | Does the session end after the climax scene? | Yes: the climax scene is the last scene of the session. |
| 2 | AMB-10 | Growth from 'roll fails after one of its tags was invoked' — invoked by whom? | Owner's own invokes only. |
| 2 | AMB-23 | Success at major cost on an attack: how much harm lands? | The attack lands for 1 shift. |
| 1 | §4 Backstory guarantee | The guarantee text says 'The GM pulls a player's card' (singular) when 'the deck is down to 2 cards.' In scene 4, the deck hit 2 cards while | When the deck-down-to-2 threshold is reached and more than one player still has an unsurfaced card among the remaining cards, all such remai |
| 1 | §5 step 2 vs §4 Backstory guarantee | The BAD NEWS Beat Frame (scene 4) has two open blanks (◆WHO, ◆WHY) and per §5 step 2 should draw 1 card per open blank (2 draws). Only one c | The guarantee check is evaluated after each individual card draw, including mid-Beat-Frame; if it empties the deck, remaining open blanks in |
| 1 | §3 outcome table / §4 climax rule | Several success_with_style results in the climax scene (events 102, 104, 107) had no peek/boost logged. The climax rule (§4) only states tha | With the deck empty during the climax, the success-with-style deck-peek option is unavailable and treated as an automatic boost with no card |
| 1 | §3 (outcome table) vs §4 (Resolving a drawn player card) | When a tie or major-cost draw (§3) turns up a card that happens to be a player card, it's unclear whether the 'minor/major cost must use one | The table treated the offered compel (using the drawn card's weakness tag) as satisfying the tie's minor-cost requirement, deferring to §4's |
| 1 | §5/§6 vs §4 | When an Altered-scene draw (§6) turns up a card owned by a player, the table applied BOTH the §6 scene-alteration effect (using one power ta | The table let one draw do double duty: the weakness tag drove the compel/surface procedure and a separate power tag drove the scene alterati |
| 1 | §6A (Resolving a story draw, step 3) vs §7 (rail limit) | Story-pile draws PE-06 (event 12, scene 1) and SPE-01 (event 35, scene 2, first appearance on rail) are never shown leaving the rail with an | Assumed the story cards were returned to their pile per §6A step 3 even though the log omits the corresponding rail_remove rows; treated as  |
| 1 | §5 | In the scene-3 PLEA FOR HELP beat frame, open blanks were WHO and WHERE. The first drawn card (C-03, CULTURE) has no matching open-blank typ | The table placed CA-01 into the remaining open blank (WHERE), using the ROOTS card as a 'place' per §5 step 4's ROOTS-can-be-a-place allowan |
| 1 | §6A | The 'compel that did not come from a deck draw is accepted' trigger draws from the player's Story Pile only after the compel has already bee | The table treated the trigger as satisfied by placing the card face-up on the rail with a free invoke for later use, without retroactively r |
| 1 | §5 | In the PLEA FOR HELP beat (event 26), both drawn cards' types (ROOTS→WHO and FACTION→WHO) nominally map to the same single 'WHO' blank, sinc | The table resolved cards in draw order: the first card drawn (AN-02, ROOTS) took the matching WHO blank; the second (F-04, FACTION), finding |
| 1 | §6 | Altered scene text is defined as changing 'who is there, the location, or the weather.' The F-03 draw (event 108) instead introduced a new o | The table treated 'element' broadly enough to include a new complicating action tied to the drawn tag, rather than restricting Altered scene |
| 1 | §3/§7 | The GM anchor card F-02 (non-GLOBAL) is placed face-up during pre-session prep (event 3, scene 0), before any scene formally begins, and is  | The free invoke from the scene-0 anchor placement was treated as usable during the session's first scene (Scene 1). |
| 1 | AMB-06 | Interrupt with no unused prepared Beat Frame. | Engine picks an unused starter-library frame by seeded RNG. |
| 1 | §5/§6/§7 | Scene 2 has no scene_test event even though it is not the session's first scene. Instead the Beat Frame trigger B-04 (fired at Scene 1 clean | The table treated a triggered (non-guarantee) Beat Frame deployment as replacing that scene's scene test, by analogy with the guarantee rule |
| 1 | §10 GM step B | T-04 ('The Drowned Priest') was taken out in conflict in Scene 4 (events 119-120), which per §8/§10 should trigger a post-session evaluation | Not modelled in this compact log; assumed to occur off-log during the 10-minute post-session procedure, but the log gives no confirmation ei |
| 1 | §3 / §4 / §11 (live tags vs. compels) | The engine refused a compel formally tied to EI-02 while that card sat unsurfaced in the Session Deck (not live). The GM then issued an equi | Treated as valid: since the compel was not formally attached to the card (no draw_id, no surfacing, no free invoke granted), it was ruled an |
| 1 | §6A / §7 (rail limit vs. repeated story draws) | When a Story Pile card is drawn again while an earlier, uncleared copy of the same card is still face-up on the rail (EI-06 recurring at eve | The table treated each draw as a fresh rail_add, compounding the rail count rather than deduplicating the existing card. |
| 1 | §5 step 3 (Beat Frame blank-filling fallback) | For frames where none of the drawn cards' native types match any open blank (RIVAL CLAIM: ROOTS/LOCATION vs. open WHERE/HOW; PLEA FOR HELP:  | Cards were resolved strictly in draw order, each filling the first still-open blank when its native type didn't match, producing internally  |
| 1 | §4 (Resolving a drawn player card, step 4) / §5 step 6 | When a surfacing compel is refused, the rule says 'the GM builds the cost from a face-up GM tag instead,' but the log only shows the owner p | Table treated the fate-point payment plus ordinary scene framing as satisfying the requirement, without a distinct logged face-up-tag cost. |
| 1 | §7 (Scene loop / rail triggers) | Scene 4 has no scene_test event even though it is not the session's first scene. It appears a Beat Frame trigger (B-04) fired during scene 3 | Table treated the cleanup-triggered Beat Frame deployment (B-04 -> RIVAL CLAIM) as replacing scene 4's scene test, by analogy with the Inter |
| 1 | §8 / §10 GM step B | L-05 (a LOCATION card) left play via 'overcome with success with style' and was later mutated into L-05v2 at session end. §10 step B's mutat | Table applied the mutation rule broadly to any GM card (including LOCATION) that left play and remained fictionally 'alive' in the story. |
| 1 | §3 | The paragraph 'The cost must use the tag' first says it governs 'a cost, compel, twist or Beat Frame blank,' then immediately narrows itself | The engine applied the strict tag-use check broadly, to compels (§4), Beat Frame blanks (§5) and Altered-scene twists (§6) as well as §3 cos |
| 1 | §6A / §7 | §6A step 3 requires a drawn story card to be 'returned to its pile and reshuffled' at scene end unless retired, but §7's five-step fixed cle | The table let drawn story cards (FE-06, EI-05, SMA-02) remain face-up on the rail past the end of the scene in which they were drawn, with n |
| 1 | §7 | The rail-limit rule only provides a resolution mechanism for overflow — 'the GM removes the oldest non-GLOBAL GM card' — but does not say wh | After the sole removable non-GLOBAL GM card (L-04) was discarded once, the rail was allowed to exceed 5 cards again (6 cards after event 132 |
| 1 | §7 (rail limit) / §6A (pile cleanup) | The rail-overflow rule only says to remove 'the oldest non-GLOBAL GM card' when the 5-card limit is exceeded. It does not say what to do whe | No eviction occurred for the overflow; the log shows the rail exceeding 5 cards at several points (events 29, 53, 58, 85) with only sporadic |
| 1 | §10 Step B ('Evaluate threats that left play') | Step B is written for 'threats' that left play, and its procedure (mutate with a version suffix, or retire) most naturally reads as covering | The table applied Step B to the LOCATION card L-05 as if it were a 'threat', mutating it into L-05v2. |
| 1 | §4 step 4 (refusal cost) / engine refusal follow-up | The engine refused the GM's attempted refusal-cost for Fenwick's declined compel at event 104 (it tried to use FE-01's own 'Warden watchtowe | Not recorded; the refused cost attempt has no visible replacement in the log. |
| 1 | §5 step 3 (Beat Frame blank-fill) | The rule only defines a fallback ('fills the first open blank still empty') for when a card's type matches NO open blank. It doesn't say wha | The table treated 'natural slot already occupied' the same as 'type matches no open blank': the card fell through to the first still-empty b |
| 1 | §6 / §7 scene loop | Scenes 2 and 3 have no scene_test event logged at all, even though §7 step 1 says to run the scene test 'except in the session's first scene | The table treated a cleanup-triggered Beat Frame/module deployment at the top of a scene as superseding that scene's scene test, running the |
| 1 | Outcomes / Conflict (defend rolls) | The Outcomes rule states 'tie = success at a minor cost' but does not say how a tie applies to a defend roll (where the defender is not taki | The table treated a tied defense as a clean, cost-free successful defense rather than invoking the generic 'minor cost' language. |
| 1 | Outcomes ('success at a major cost') vs. Conflict (stress/consequence tracks) | The rules describe 'success at a major cost' as an option on a failed roll and separately define a stress/consequence system for Conflict. I | The GM resolved the major cost (event 81) as a freeform narrative consequence (being swept into the flood) without marking any boxes on Anse |
| 1 | §4 vs §6 (Altered scene) | §6.4 says an Altered-scene draw's tags 'change one element of the planned scene' (flavor only), while §4's enumerated draw triggers do not l | Table treated any Session Deck draw of a player card, regardless of which trigger caused it, as running the full §4 player-card resolution ( |

## Referee friction points (all runs)

- (1×) The GM's proposed fictional trigger 'the party enters a settlement' was rejected twice by the engine (scenes 1 and 2) as not a valid unused §7 trigger, indicati
- (1×) The GM attempted a compel citing PE-01 against Petra in scene 2 while that card was not in play (still in the Session Deck / not owned-live), and the engine ref
- (1×) Resolving the BAD NEWS Beat Frame's second open blank required an ad hoc ruling when the backstory-guarantee pull emptied the deck mid-frame, forcing an unplann
- (1×) Two cost narrations (YA-04's compel at event 57 and CA-01's Beat Frame compel at event 120) needed to be 'repaired' before they satisfied the §3 'the cost must 
- (1×) Story-pile draws (PE-06, SPE-01) never get an explicit rail_remove logged at scene cleanup the way every other rail card does, forcing rail-limit compliance to 
- (1×) The same Session Deck draw was pressed into double duty twice this session (YA-04 in scene 3, PE-03 in scene 4) — one tag for the §4 compel/surface procedure an
- (1×) Story cards AN-06, PE-06, PE-05 and CA-06 (all placed face-up on the rail during scene 4 via §6A story draws) have no corresponding pile-return event at scene 4
- (1×) The §6A trigger fires only after a compel is already accepted, which puts the 'complication must involve the drawn card' requirement structurally after the fact
- (1×) GM anchor L-01 (the ford location) stayed face-up across scenes 2-4 until removed purely for rail-space reasons (event 70), even as play moved on to Hollowmoot 
- (1×) GM fate point fields (gm_fp, gm_fp_spent) are never populated anywhere in the log, making it impossible to verify the §3 rule that the GM receives 1 fate point 

## Player one-sentence verdicts on backstory use

- [A s44982] optimizer: Petra's entire backstory—her home, her gift, her debts—was woven directly into the story's heart, making each discovery and loss feel personally urgent rather than incidental.
- [A s44982] protector: Anselm's backstory felt earned and central, not forced against him—the drowning became a real obstacle to overcome, not a penalty for existing.
- [A s44982] instigator: Both my roots mattered and drove real stakes—Marrowreed's burning wasn't just flavor, and Sella's bond wasn't background decoration; they were the emotional spine of what happened to Caddock.
- [A s44982] tactician: My backstory was honored perfectly—the tragedy of lost weir-keeping became real and personal through recognizing what it cost Moss and what still survives, making both the loss and the knowledge matter thematically.
- [A s44983] storyteller: Petra's entire character concept was the literal solution to the session's mystery, which made playing her feel essential, even when the swarm-song's pull on her vow stripped away some agency in how she responded.
- [A s44983] rules_lawyer: My obsessions and expertise were honored, my rites and knowledge mattered in life-death ways, but the session bypassed Anselm's defining doubt—whether saving people from the hive is even possible, or just prolonging something darker.
- [A s44983] lurker: My background was used well and meaningfully—but only in the final section, leaving the first half feeling disconnected from Caddock's story.
- [A s44983] method_actor: The background was used well—all four cards touched the story naturally without feeling forced or unfair.
- [A s44984] protector: Petra's backstory was used well—it generated meaningful complications that tested her character without feeling unfair or arbitrary.
- [A s44984] instigator: Anselm's background was used to create real complications and stakes—his past made him vulnerable in ways that directly shaped what happened, and his expertise made his choices tactically different from the others' in ways that mattered.
- [A s44984] tactician: Caddock's backstory wasn't flavor—it was the session's spine, and the GM used it with real weight and care.
- [A s44984] optimizer: Yarrow's core identity as someone who steadies others and reads the land was woven through the whole session without ever feeling like it was used *against* me — strong session for that character's specific story.
- [A s44985] rules_lawyer: Petra's backstory felt integrated naturally into the story's stakes without being weaponized unfairly—her abilities and history were the engine, not the obstacle.
- [A s44985] lurker: My background was engaged directly through compel and thematic echo, but I ended up playing support in other people's big moments rather than driving my own character arc.
- [A s44985] method_actor: My character's core flaw was weaponized against me in the best way—it created genuine conflict and didn't feel arbitrary or punitive, just inevitable.
- [A s44985] storyteller: Yarrow's Weir-Keeper background felt genuinely central to the story and used with respect, though the compel from Ossa bound him to a choice his character would probably have refused if given the chance.
- [A s44986] instigator: Petra's backstory felt like the backbone of the entire session—it drove plot points, created emotional stakes, and gave her the specific skills and vulnerabilities that made her the natural choice to solve each problem.
- [A s44986] tactician: Anselm's expertise and immediate backstory hooks (bell-tongue, liturgy) worked well, but the deeper personal stakes haven't been engaged yet—his sister's drowning, his moral crisis about souls, the old mill-roads—which will matter more as the story continues.
- [A s44986] optimizer: Caddock's most important relationship got earned, complex screen time that complicated rather than resolved her core conflict, while other background elements stay in reserve—that's the right call.
- [A s44986] protector: Yarrow's family legacy and weir-keeper knowledge were used well and felt earned, but his disgrace remained unexplored and he stayed more in a support role than a driver of the main mystery.
- [A s44987] lurker: The core concept worked perfectly when it mattered; the disgrace and militia past exist but stayed at the surface.
- [A s44987] method_actor: Hask's family background wasn't just acknowledged—it was woven into every major scene in ways that made his expertise matter mechanically and emotionally.
- [A s44987] storyteller: My character's core cards became major plot hooks at exactly the right moment and created real vulnerability, but I'm sharing the narrative focus with equally strong backgrounds and sometimes feel like I'm supporting others' storylines rather than driving my own.
- [A s44987] rules_lawyer: Fenwick's background was woven expertly into the narrative—each of his cards touched the story organically, making his choices feel genuinely costly without being unfair.
- [A s44988] tactician: Maud's militia background and Hollowmoot roots powered every key moment, making her essential to the story's turning points without ever feeling forced into those positions.
- [A s44988] optimizer: My character's hooks felt genuinely important to the story—the GM wove them in naturally where they mattered rather than forcing them.
- [A s44988] protector: Eira's willingness to help the vulnerable was used as the very thing that creates her deepest debt—and that feels precisely right, not unfair.
- [A s44988] instigator: Fenwick's character concept and backstory felt used well—the escalation impulse, the enmity with the Order, and the Cartel debt all became the heart of the action without feeling forced or wasted, and I'd absolutely play another session to see what comes next.
- [A s44989] method_actor: Maud's oath and debt were used as complementary pressures creating genuine stakes and real tension—the game used her history to constrain choices in ways that made sense, not as arbitrary punishment.
- [A s44989] storyteller: My ferry-family roots weren't color—they were the reason I could help.
- [A s44989] rules_lawyer: My knowledge and skills were absolutely essential and well-woven in, but the major story complications felt more like predetermined consequences of my character cards than genuine emergent challenges.
- [A s44989] lurker: Your enmity with the Order and Bren's location felt woven in meaningfully—threatening but fair, integrated rather than forced.
- [A s44990] optimizer: Maud's past felt honored and active in play—the GM made her the anchor point for other characters' trust, leaning hard into "still holds the line" as her core, and that landed exactly right.
- [A s44990] protector: My backstory was weaponized perfectly—not unfairly, but as the specific blade that would wound Hask most because it came from someone he chose to trust and taught to survive.
- [A s44990] instigator: My background got used skillfully—three of my four cards came alive in ways that mattered—but "The Massacre at Three Elms" felt present only as atmosphere, not as the weight Eira actually carries, and I left the session with Sella still a ghost I'm hunting instead of a confrontation I can close.
- [A s44990] tactician: Bren's ghost and the forbidden oath made Fenwick essential to this story, and refusing to break it for the Cartel felt like the truest thing he could do.
- [A s44991] storyteller: My backstory created meaningful moral weight and genuinely difficult choices—the compels were challenging without being unfair, and the silver debt made events feel personally stakes-heavy in exactly the right way.
- [A s44991] rules_lawyer: My background was woven in skillfully and created real personal weight, but too many story complications felt imposed on me rather than driven by my choices — I was reactive more than proactive.
- [A s44991] lurker: Eira's backstory was used well—personal elements created meaningful moments—though mostly through mechanical compels rather than through opportunities for her to seize initiative.
- [A s44991] method_actor: My backstory with Bren was integrated beautifully and earned, but I'm narrowing into the role of "mapmaker who navigates around problems" instead of one who drives forward into stakes for personal reasons.
- [B s44982] optimizer: My background was used well and woven in organically, but the central vow—Ring Everyone Home Before the Flood—is still waiting to become a real mechanical/narrative weight on Petra's shoulders.
- [B s44982] protector: My drowned-mill background was threaded throughout via the drowning imagery and directly invoked in the ending—used well overall, but I wish the finale had forced explicit confrontation with that trauma rather than just thematic resonance.
- [B s44982] instigator: Backstory used well—my Marrowreed trauma with the Wardens made this confrontation feel personal and earned.
- [B s44982] tactician: Yarrow's practical expertise (weir-keeper, militia) was well-integrated and felt earned, but his personal stakes (disgrace, the promise, bond with Brack) remained mostly dormant.
- [C s44982] optimizer: Petra's background—the bell-work, the swamp-sense, the debt history, the swarm-song attunement—was woven into the actual story beats rather than just character flavor, and it felt like central to why she mattered.
- [C s44982] protector: Used well—the Mireth compel especially cut right to my character's core uncertainty, and all the background integration felt earned rather than forced.
- [C s44982] instigator: Caddock's backstory was woven through every scene—it created stakes, complications, and reasons to act, and never once felt ignored or used unfairly.
- [C s44982] tactician: My backstory was central to nearly every major scene and felt earned rather than inflicted—especially the burial-ground defense, which gave Yarrow exactly the kind of personal, high-stakes moment his character needed.

## Run status

| Run | Status | Scenes | Draws | Tokens | Error |
| --- | --- | --- | --- | --- | --- |
| batch-02__A__s44982__r0 | complete | 5 | 5 | 1,230,420 |  |
| batch-02__A__s44983__r1 | complete | 5 | 5 | 1,712,345 |  |
| batch-02__A__s44984__r2 | complete | 5 | 2 | 1,377,196 |  |
| batch-02__A__s44985__r3 | complete | 5 | 6 | 1,874,168 |  |
| batch-02__A__s44986__r4 | complete | 5 | 6 | 1,556,890 |  |
| batch-02__A__s44987__r5 | complete | 5 | 4 | 1,761,622 |  |
| batch-02__A__s44988__r6 | complete | 5 | 5 | 1,482,254 |  |
| batch-02__A__s44989__r7 | complete | 5 | 4 | 2,148,446 |  |
| batch-02__A__s44990__r8 | complete | 5 | 2 | 1,750,777 |  |
| batch-02__A__s44991__r9 | complete | 5 | 7 | 1,590,271 |  |
| batch-02__B__s44982__r0 | complete | 5 | 0 | 920,335 |  |
| batch-02__C__s44982__r0 | complete | 5 | 6 | 1,479,925 |  |
