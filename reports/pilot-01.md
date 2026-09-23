# Batch report: pilot-01

Runs: 9 ({'complete': 9}). Spec version(s): ['0.1.0']. Backend(s): ['claude_cli']. Tokens: 16,308,917 (≈ $48.44).

## Blinded analyst conclusions

_Written by the Analyst agent from blinded labels **before** unblinding._

"With only 3 sessions per arm and 12 paired survey judgments per comparison, this dataset supports mainly directional, low-confidence observations rather than firm conclusions. The clearest and most defensible finding is a null result: self-reported fun, involvement, connection, and play-again intent do not meaningfully distinguish the three rule variants -- all cluster near the top of the 1-7 scale with overlapping intervals. Paired forced-choice preferences produce an intransitive cycle among the three arms, suggesting either that each variant has genuinely different, non-dominating strengths that surface differently depending on the direct comparison, or (equally plausible given n=12 per pair) that this cycle is sampling noise. Behavioral/log-based metrics are more informative and point to a consistent structural contrast: the arm with no card-deck subsystem relies entirely on GM improvisation and has the highest compel-acceptance and fate-point accumulation, while the two deck-using arms trade off against each other -- one (lower deck-draw volume) achieves more consistent backstory surfacing and fewer rule violations, while the other (higher deck-draw volume) achieves more even spotlight distribution and slightly higher involvement/play-again scores at the cost of more rule violations, more unresolved ambiguities, and more player pushback against card-driven compels. None of these behavioral contrasts should be treated as decisive given the small number of runs and the wide variance seen within several arms (especially violation counts). A larger sample, particularly more paired preference judgments and more sessions per arm, would be needed before recommending one rule variant over another."

- Overall self-reported enjoyment (fun, involvement, connection, control, play-again) does not clearly differentiate the three arms: all means fall in a narrow 6.3-6.9 band (control slightly lower, 5.5-5.75) with heavily overlapping confidence intervals and paired within-comparison deltas of at most ~0.33 points on a 7-point scale. This is a genuine null result on the self-report measure, not just insufficient power to detect a real gap of interest.
- Paired forced-choice preferences show a non-transitive (rock-paper-scissors) pattern across the three arms: Arm 1 was preferred over Arm 2 (7 vs 5 of 12), Arm 2 was preferred over Arm 3 (8 vs 4), and Arm 3 was preferred over Arm 1 (8 vs 4). No single arm dominates in pairwise preference, and the margins (7-5, 8-4, 8-4 out of only 12 judgments) are modest enough that this cycle may reflect sampling noise as much as a real multi-dimensional trade-off between arms.
- One arm (apparently the label 'Arm 1') never draws from a card deck (deck_draws=0, card_supplied_complications=0, improvisation_share=1.0, clock_marks=0 by construction) and instead relies entirely on GM-improvised complications (mean 11.3 per session) and a high compel-accept regime (8 compels accepted, 0.96 accept ratio, highest ending fate points at 2.33). This arm also shows the highest total rule violations among the three (6.7 mean) despite having no card subsystem to misapply, and rules/confusion did not appear as a top complaint category for it.
- The two deck-using arms (labelled Arm 2 and Arm 3) differ from each other in draw intensity and downstream effects: Arm 2 draws fewer cards (mean 4, tight range) and shows the highest 'all players got a backstory beat' rate (0.667) plus the lowest violation count (4) and highest self-reported connection (6.83); Arm 3 draws more cards (mean 5.67) but never achieves full backstory coverage (0.0), has the highest violation count and most run-to-run variance (7.3, range 3-15), the most ambiguity mentions (19), and more refused compels with a lower compel-accept ratio (0.80 vs 0.90-0.96 in the other arms) -- suggesting friction between card-driven compels and player acceptance -- while simultaneously having the most even spotlight distribution (lowest involvement variance, 0.125) and the highest self-reported involvement (6.83) and play-again intent (6.92) of the three arms.
- Rules/confusion appears as a named complaint category only in the two card-deck arms (Arm 2: 3 mentions, Arm 3: 2 mentions), not as a listed category for the no-deck arm, consistent with (but not proof of) the deck subsystem introducing additional rules ambiguity -- also reflected in generally higher raw ambiguity counts in the deck arms (16.7 and 19.0) versus the non-deck arm (15.7), though these ranges overlap substantially.
- Behavioral equity metrics (turn-taking gini 0.008-0.023, invoke gini 0.22-0.25) are similar and low across all three arms, indicating no meaningful difference in turn-taking or spotlight-invoke balance attributable to the rule variant at this sample size.

Caveats:
- Extremely small sample: aggregates are built from only 3 sessions per arm, and many metrics (violations, clock_marks, fp_end, tension) show very wide lo-hi ranges relative to their means (e.g., Arm 3 violations ranges 3-15 around a mean of 7.3), so single outlier sessions can be driving arm-level differences.
- Self-report survey scales (1-7) are compressed near ceiling in all three arms (means 6.3-6.9 on fun/involvement/connection/play_again); differences between arms are ≤0.33 points and confidence intervals overlap heavily, so these should be read as null/no-detectable-difference results, not as evidence of a 'better' arm.
- The paired forced-choice preference results are based on only n=12 judgments per pairwise comparison, and the observed intransitive cycle (Arm1 beats Arm2, Arm2 beats Arm3, Arm3 beats Arm1) could easily be sampling noise rather than a genuine non-transitive preference structure; it should not be over-interpreted without a larger sample.
- Some fields are structurally undefined or missing for certain arms (e.g., deck_surfaced_all_players_rate has n=0 for Arm 3 and no field at all for Arm 1 since it appears to lack a deck subsystem; draw_cost_used_card_rate_engine is n=0 for Arm 1), so direct three-way comparisons on those metrics are not possible.
- Arm identities are blinded; any inference about 'why' one arm behaves differently (e.g., presence/absence of a card-deck mechanic) is a pattern-based inference from the data, not confirmed knowledge of the underlying rules, and could be wrong.
- No multiple-comparison correction was applied across the many metrics examined; with this many comparisons at small n, some apparent patterns are expected to arise by chance.
- Personality-subgroup breakdowns (e.g., lurker, method_actor) often have n=1-2 per arm, so those splits are illustrative only and not statistically meaningful.

## Unblinding

| Blinded label | Arm |
| --- | --- |
| Arm 1 | B |
| Arm 2 | A |
| Arm 3 | C |

## Structural metrics (per session, mean [95% bootstrap CI])

| Metric | A | B | C |
| --- | --- | --- | --- |
| Every player's backstory drove an event | 0.67 [0.00, 1.00] (n=3) | 0.33 [0.00, 1.00] (n=3) | 0.00 [0.00, 0.00] (n=3) |
| Every player's own card surfaced from the deck | 0.00 [0.00, 0.00] (n=3) | — | — |
| Deck draws / session (target 5–8) | 4.00 [4.00, 4.00] (n=3) | 0.00 [0.00, 0.00] (n=3) | 5.67 [4.00, 7.00] (n=3) |
| Draw costs using the drawn card: engine tag check | 0.94 [0.83, 1.00] (n=3) | — | 0.93 [0.80, 1.00] (n=3) |
| Draw costs using the drawn card: referee judgment | 0.61 [0.50, 0.67] (n=3) | 0.05 [0.00, 0.14] (n=3) | 0.51 [0.42, 0.59] (n=3) |
| Mean player FP at session end (target 1–5) | 1.42 [0.75, 2.25] (n=3) | 2.33 [1.75, 3.25] (n=3) | 1.58 [0.00, 3.00] (n=3) |
| Spotlight Gini: turns | 0.02 [0.00, 0.07] (n=3) | 0.01 [0.00, 0.03] (n=3) | 0.01 [0.00, 0.02] (n=3) |
| Spotlight Gini: invokes | 0.25 [0.25, 0.25] (n=3) | 0.24 [0.14, 0.30] (n=3) | 0.22 [0.17, 0.30] (n=3) |
| Scenes / session | 5.00 [5.00, 5.00] (n=3) | 5.00 [5.00, 5.00] (n=3) | 5.00 [5.00, 5.00] (n=3) |
| Clock marks | 1.67 [0.00, 4.00] (n=3) | 0.00 [0.00, 0.00] (n=3) | 2.33 [0.00, 4.00] (n=3) |
| Compels accepted | 6.00 [5.00, 7.00] (n=3) | 8.00 [6.00, 12.00] (n=3) | 5.33 [5.00, 6.00] (n=3) |
| Compels refused | 0.67 [0.00, 2.00] (n=3) | 0.33 [0.00, 1.00] (n=3) | 1.33 [0.00, 2.00] (n=3) |
| GM-improvised complications | 5.00 [3.00, 8.00] (n=3) | 11.33 [7.00, 19.00] (n=3) | 3.67 [3.00, 5.00] (n=3) |
| Card-supplied complications | 5.33 [5.00, 6.00] (n=3) | 0.00 [0.00, 0.00] (n=3) | 8.00 [5.00, 10.00] (n=3) |
| Improvisation share | 0.46 [0.38, 0.61] (n=3) | 1.00 [1.00, 1.00] (n=3) | 0.33 [0.23, 0.50] (n=3) |
| Rule violations (engine + referee) | 4.00 [2.00, 6.00] (n=3) | 6.67 [5.00, 9.00] (n=3) | 7.33 [3.00, 15.00] (n=3) |
|   — engine refusals | 3.00 [1.00, 4.00] (n=3) | 4.00 [4.00, 4.00] (n=3) | 3.67 [0.00, 10.00] (n=3) |
|   — referee | 1.00 [0.00, 2.00] (n=3) | 2.67 [1.00, 5.00] (n=3) | 3.67 [2.00, 5.00] (n=3) |
| Ambiguity records | 16.67 [15.00, 18.00] (n=3) | 15.67 [13.00, 18.00] (n=3) | 19.00 [15.00, 21.00] (n=3) |
| Backstory guarantee failures | 0.00 [0.00, 0.00] (n=3) | 0.00 [0.00, 0.00] (n=3) | 0.00 [0.00, 0.00] (n=3) |
| Within-session variance of involvement | 0.38 [0.19, 0.69] (n=3) | 0.38 [0.19, 0.69] (n=3) | 0.12 [0.00, 0.19] (n=3) |
| Compel accept ratio | 0.9 | 0.96 | 0.8 |
| Tension values seen | {1: 11, 2: 3, 3: 4} | {} | {1: 6, 2: 8, 3: 4} |

## Experiential (LLM player self-reports, 1–7; weak evidence)

| Score | A | B | C |
| --- | --- | --- | --- |
| fun | 6.33 [6.08, 6.58] (n=12) | 6.58 [6.17, 6.92] (n=12) | 6.33 [6.08, 6.58] (n=12) |
| involvement | 6.50 [6.08, 6.83] (n=12) | 6.50 [6.08, 6.83] (n=12) | 6.83 [6.58, 7.00] (n=12) |
| connection | 6.83 [6.58, 7.00] (n=12) | 6.50 [6.00, 6.92] (n=12) | 6.50 [6.08, 6.92] (n=12) |
| control | 5.50 [5.25, 5.75] (n=12) | 5.75 [5.50, 6.00] (n=12) | 5.75 [5.42, 6.08] (n=12) |
| play_again | 6.75 [6.50, 7.00] (n=12) | 6.83 [6.58, 7.00] (n=12) | 6.92 [6.75, 7.00] (n=12) |

### Paired differences (same seed, same character and personality)

- **A-B**: involvement 0.00 [-0.33, 0.33] (n=12); connection 0.33 [0.00, 0.83] (n=12); fun -0.25 [-0.67, 0.17] (n=12); control -0.25 [-0.67, 0.17] (n=12)
- **A-C**: involvement -0.33 [-0.58, -0.08] (n=12); connection 0.33 [-0.17, 0.92] (n=12); fun 0.00 [-0.42, 0.42] (n=12); control -0.25 [-0.75, 0.17] (n=12)
- **C-B**: involvement 0.33 [0.00, 0.67] (n=12); connection 0.00 [-0.67, 0.67] (n=12); fun -0.25 [-0.67, 0.17] (n=12); control 0.00 [-0.42, 0.33] (n=12)

Lurker involvement by arm: A 5.00 (n=1); B 5.00 (n=1); C 6.00 (n=1)

### Survey means by personality

| Personality | A involvement | B involvement | C involvement | A connection | B connection | C connection |
| --- | --- | --- | --- | --- | --- | --- |
| instigator | 7.00 [7.00, 7.00] (n=2) | 7.00 [7.00, 7.00] (n=2) | 7.00 [7.00, 7.00] (n=2) | 7.00 [7.00, 7.00] (n=2) | 7.00 [7.00, 7.00] (n=2) | 7.00 [7.00, 7.00] (n=2) |
| lurker | 5.00 (n=1) | 5.00 (n=1) | 6.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 5.00 (n=1) |
| method_actor | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 5.00 (n=1) |
| optimizer | 6.50 [6.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 7.00 [7.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 5.50 [5.00, 6.00] (n=2) | 6.50 [6.00, 7.00] (n=2) |
| protector | 6.50 [6.00, 7.00] (n=2) | 7.00 [7.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 7.00 [7.00, 7.00] (n=2) | 7.00 [7.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) |
| rules_lawyer | 6.00 (n=1) | 6.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) |
| storyteller | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) |
| tactician | 6.50 [6.00, 7.00] (n=2) | 6.00 [6.00, 6.00] (n=2) | 7.00 [7.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 5.50 [5.00, 6.00] (n=2) | 7.00 [7.00, 7.00] (n=2) |

### Paired transcript preference (blinded, same cohort and seed)

- A-B: {'B': 7, 'A': 5}
- A-C: {'C': 4, 'A': 8}
- B-C: {'B': 4, 'C': 8}

### Fate point flow by personality (mean per session: earned / spent / end)

- **A**: instigator 1.5/4.5/0; lurker 1/2/2; method_actor 4/1/6; optimizer 1.5/3.5/1; protector 2.5/3.5/2; rules_lawyer 1/4/0; storyteller 1/3/1; tactician 0.5/2.5/1
- **B**: instigator 3.5/6/0.5; lurker 1/2/2; method_actor 5/4/4; optimizer 2/2.5/2.5; protector 1.5/2/2.5; rules_lawyer 1/3/1; storyteller 0/3/0; tactician 4/2/5
- **C**: instigator 2.5/3/2.5; lurker 1/0/4; method_actor 1/4/0; optimizer 1/3/1; protector 0.5/2.5/1; rules_lawyer 2/4/1; storyteller 1/2/2; tactician 1.5/3/1.5

### Complaint clusters (keyword buckets over 'most frustrating')

- **A**: {'dice/luck': 5, 'rules/confusion': 3, 'pacing': 3, 'other': 3, 'agency/control': 2}
- **B**: {'other': 7, 'pacing': 2, 'dice/luck': 1, 'spotlight/ignored': 1, 'agency/control': 1}
- **C**: {'other': 5, 'dice/luck': 3, 'rules/confusion': 2, 'pacing': 1, 'agency/control': 1, 'unfair/punishing': 1, 'spotlight/ignored': 1}

## Ambiguities

| Count | ID / section | Issue | Interim ruling |
| --- | --- | --- | --- |
| 9 | AMB-12 | Stress box values are unspecified. | Fate Core: boxes 1 and 2; Physique/Will +1/+2 adds a 3 box, +3 or more adds 3 and 4. |
| 6 | AMB-01 | Arm A lists 'Attention', which the spec never defines. | Not modelled. |
| 6 | AMB-22 | Does a GLOBAL anchor give the GM a free invoke like a GM card? | Yes, GLOBAL cards placed on the rail give the GM 1 free invoke that scene. |
| 5 | AMB-19 | Tie on an attack: 'success at minor cost' but 0 shifts of harm. | Attacker gets a boost (Fate Core) and the deck draw still happens. |
| 3 | AMB-23 | Success at major cost on an attack: how much harm lands? | The attack lands for 1 shift. |
| 2 | AMB-20 | §6 Altered scene draws a card, but §4's closed list of draw triggers omits it. | §6 is more specific: Altered scenes draw. |
| 2 | AMB-10 | Growth from 'roll fails after one of its tags was invoked' — invoked by whom? | Owner's own invokes only. |
| 2 | AMB-04 | Do tension adjustment rows stack? | All applicable rows are summed, then clamped to 1-6. |
| 1 | §3 Outcomes and deck draws table (interaction with Create Advantage's native success-with-style bonus) | Events 11-12, 13-14, and 16-17 show players getting success-with-style on Create Advantage rolls. Standard Fate CA success-with-style alread | Table ruling: on Create Advantage rolls, the deck peek is additive to the CA's native success-with-style bonus (both the 2 free invokes and  |
| 1 | §3 (Which tags are live) / §4 (When the GM draws / Resolving a drawn player card) | The rules state a player card sitting in the Session Deck is 'not live' and 'its owner cannot invoke it until it surfaces,' but this languag | The table treated the tag as usable for a compel without running it through the §4 draw procedure, and awarded the story-pile draw (§6A row  |
| 1 | §6A (Pile maintenance, scene cleanup) | The scene-end cleanup log (events 41-46) shows Tension adjustment, a rail discard, and one new story card added (SN-02), but never logs the  | Treated as an unlogged/implicit engine action rather than an omission, since the event log format may not surface every housekeeping step; n |
| 1 | §5 (Beat Frame procedure, step 5) | Step 5 requires the GM to ask the surfacing card's owner one specific question about the filled blank and treat the answer as canon (worked  | Treated Aldous's own declared narration in his 'overcome' action (event 57, 'the weight of their shared history and his sworn vow') as satis |
| 1 | §3 (Invokes) / §4 (Resolving a drawn player card) | The GM invokes AL-02's weakness tag ('Verrick now commands the Wardens') against its own owner (Aldous) while it sits face-up on the rail (e | Assumed the GM silently paid 1 fate point from its per-scene budget for the invoke, with only the compensating payout to the target logged e |
| 1 | §4 (When the GM draws) | The Session Deck draw attributed to the tie (event 60, YS-02) is logged with a lower event_id than the roll that produced the tie result (ev | Treated as a display/log-ordering artifact of the engine rather than an actual causality violation, since the engine is stated to already en |
| 1 | §6A (Pile maintenance — Weight) | Cards drawn or featured this scene (F-02, AL-02, YS-02) should each gain +1 Weight (max 3) at cleanup per §6A, but no Weight-change events a | Assumed Weight tracking occurs but is simply not itemized in this event log schema. |
| 1 | §6 (Adjusting Tension at scene end) | Tension dropped 2→1 with note 'resolved -1' (event 67), but the FACTION card F-02 that opposed the party remains face-up on the rail with it | Accepted the GM's judgment that winning the social conflict against Verrick/the Order (events 61-63) counted as 'filled a player's goal' for |
| 1 | §6A (Draw triggers / Resolving a story draw) | Event 81 is a compel accepted on Mire's own card (MI-02) that did not come from a deck draw, which correctly triggers a Player Story Pile dr | Treated as satisfied by assumption that the GM applied MI-06 off-log (e.g., folded it into the unlogged prose of the compel's fallout); flag |
| 1 | §7 (Scene loop cleanup step 5 / Backup modules) | Trigger M-1 fires at cleanup (event 89) but scene 4 ends immediately after (event 90) with no card-add or scene-change event showing the mod | Interim ruling used: deployment of a module that fires at cleanup is deferred to the start of the next scene's framing rather than requiring |
| 1 | §6A (Pile maintenance – Add) / §3 (active opposition) | The NPC 'Anxious Hollowmoot Neighbor' is used as active/named opposition for Morwen's roll (event 85) without ever having been drawn from a  | Interim ruling used: the card was filed in the pile of the player to whom the NPC is fictionally tied (Mire, whose neighbor it is), not the  |
| 1 | §6 (Tension adjustment table) | T-03 (a face-up THREAT) was overcome with success with style and left play this scene (events 100-101), which fits the table row 'The party  | Treated the outcome as consistent with the rules (assume -1 was computed and clamped to the floor of 1) since the numeric result matches eit |
| 1 | §6 tension table / §7 cleanup step 3 | F-02 (FACTION) and C-02 (a module GM card) were removed from the rail at cleanup with the note 'discard: no longer present' (events 108-109) | Assumed neither card was actively bypassed/ignored in the fiction (they simply were not narratively relevant this scene and exited via norma |
| 1 | §3 (GM free invoke from a rail card) | T-03 was placed face-up via module M-1 (event 92), which per §3 grants the GM 1 free invoke on its tags to be used within that scene. The on | Treated the free invoke as unused/expired at scene end per the 'Unused free invokes expire' cleanup rule, since no successful GM invoke on a |
| 1 | §3 (Outcomes and deck draws table) | Event 22 was a Create Advantage roll with success with style (shifts=4), which per standard Fate already grants the create-advantage aspect  | The table let Ysolde keep both the create-advantage aspect's 2 free invokes (noted 'aspect A-1.1.2 (2 free)') AND take the top-card peek (ev |
| 1 | §6A (Draw triggers table — compel not from a deck draw) | The rules don't cap how many times the same weakness tag on the same card can be freely compelled within one scene, or whether each such com | The table allowed repeated free compels on the identical tag within the same scene, each treated as a distinct Fate event and each drawing a |
| 1 | §6 (Adjusting Tension at scene end table) | It's unclear whether talking/negotiating past a face-up FACTION checkpoint (Warden Sergeant Coss) without ever marking its clock or taking i | The GM treated the successful social overcome of the checkpoint (event 24) as resolving the FACTION for tension purposes, applying -1 (event |
| 1 | §3 (Outcomes and deck draws table, success-with-style row) and standard Fate Create Advantage rules | Event 38 (Aldous, Create Advantage, success with style) grants 2 free invokes on the new aspect per baseline Fate CA rules ('2 free' in note | The table allowed both benefits: Aldous kept the 2 free invokes on the created aspect and also took the deck peek (moved AL-04 to the bottom |
| 1 | §6A (Draw triggers table, row: 'A player accepts a compel that did not come from a deck draw') | The compel (event 35, tag 'Every stranger knows her face') was fully narrated and accepted before the triggered Story Pile draw occurred (ev | The GM treated the draw as supplying supplementary narrative material after the fact: two new story cards (SN-02 'Old Bettony' and SMO-01 'T |
| 1 | §6 (Adjusting Tension at scene end table) | Tension dropped 2→1 at event 40 with notes 'resolved -1,' implying the 'party resolved a THREAT or filled a player's goal' row. No THREAT/FA | The GM applied the -1 based on narrative judgment (the scene's central question of finding shelter/aid in Hollowmoot was resolved favorably) |
| 1 | §7 (Scene loop, cleanup step 5: 'Check every unused module and Beat Frame trigger. Deploy each one that fired.') | Events 43-44 log 'Trigger fired: M-1' and 'Trigger fired: B-01' during scene 2 cleanup, but no deployment (card draws, frame sentence, frame | Deployment was treated as deferred to the start of the next scene rather than executed within scene 2's own log. |
| 1 | §6 Tension track / §7 Scene loop step 1 | Scene 3 is not the session's first scene, so a scene test (1d6 roll) should have been run before framing the scene. No scene_test event appe | Treated as compliant on the assumption the AMBUSH Beat Frame fired from its own prepared trigger (a valid independent §4 draw trigger) rathe |
| 1 | §3 Free invokes from cards / §7 Backup modules | Module M-1's two GM cards (C-01, T-05) are placed face-up on the rail (events 46-47) with no accompanying 'GM gains 1 free invoke' event, ev | Treated module placement as outside the free-invoke grant (i.e., only deck-drawn GM cards trigger the free invoke), since §7 describes modul |
| 1 | §3 Free invokes from cards / §4 Resolving a drawn GM card | H-05 surfaces once (event 52) and is granted exactly 1 free invoke, yet the GM is shown invoking its tag 'weakens the strongest fighter' on  | Assumed the second invoke (event 75) was paid out of the GM's per-scene fate point budget off-log, since the log format provides no field to |
| 1 | §3 (Opposition) / §5 (Beat Frame fills) | Events 94 and 95 show a 'Named NPC' (Mag) rolling active opposition (4dF + rating) while also listing a face-up GM card tag (H-05 'brings fe | Treated H-05's contribution as a passive, no-invoke-cost situational bonus (not a spent free invoke) layered onto the GM's ad-hoc rating for |
| 1 | §6A (Story Pile draws) | Three Story Pile draws occurred this scene (AL-05, MI-05, MI-06) from compels not sourced from a deck draw. §6A requires 'the complication m | Treated the ongoing Warden-cordon standoff narration as satisfying the 'involve the drawn card' requirement in the absence of contrary evide |
| 1 | §5 / §7 (Beat Frame trigger) | The Beat Frame 'PLEA FOR HELP' draws (events 83-85) begin at the very start of Scene 4 with no logged 'WHEN...THEN' trigger event in this sc | Assumed the trigger was evaluated and fired during the prior scene's cleanup step 4.5 ('Check every unused module and Beat Frame trigger') a |
| 1 | §7 Writing triggers / §12 Event log format | Module M-2's trigger (the 'WHEN [event]' condition) is never logged as its own event before the rail_add rows for H-06 and T-02. The spec re | Treated the module deployment as valid on the assumption the trigger fired off-log; no violation charged, but the log is incomplete for audi |
| 1 | §7 The rail / §6A pile maintenance | T-02 is added to the rail this scene but never removed or discarded by scene end, and it is not a GLOBAL card, so its persistence rule is un | Assumed T-02 remains fictionally present at scene end and so legitimately carries to scene 6 under cleanup step 3 ('move GM cards that are n |
| 1 | §6 (Adjusting Tension at scene end) | Tension was reduced by 1 (event 24, 'resolved -1') on the grounds that something was 'resolved,' but the log shows no face-up THREAT/FACTION | Treated the checkpoint NPC as a stand-in for a THREAT that was effectively neutralized through social resolution, applying the -1 'resolved  |
| 1 | §3 (live tags) / §4 (Session Deck) | Event 11's compel invokes tag 'Verrick now commands the Wardens' on card AL-02 as a normal (non-deck-draw) compel. The log does not show whe | Assumed AL-02 remained in Aldous's binder (live) since only one of his four cards enters the deck and the GM/engine allowed the compel to pr |
| 1 | §5/§7 (Beat Frame triggers) | The engine refused a Beat Frame deployment because the stated trigger ('the party enters a settlement') was 'not an unused fictional trigger | Treated the engine's refusal as authoritative: the trigger was considered already spent/invalid, so no Beat Frame drew cards for this scene; |

## Referee friction points (all runs)

- (1×) Six fate points were spent by players in the very first scene (four Create Advantage rolls, all against the same two GM anchor cards H-03 and T-01), which front
- (1×) The ambiguous interaction between Create Advantage's native success-with-style bonus and the §3 deck-peek option (see ambiguity above) let all three peeking pla
- (1×) All four PCs converged on create_advantage against the same two face-up anchor cards in immediate succession; the rules give no guidance on pacing or diminishin
- (1×) The AL-02 card appears simultaneously as a compellable live-tag source (event 28) and as an undrawn card sitting on top of the Session Deck (event 39 peek) — th
- (1×) Story Pile draw IDs (AL-06, MO-06) share the same prefix/numbering convention as Session Deck binder cards (AL-01..04) and GM cards (L-01), with no type marker 
- (1×) Scene-end cleanup events don't explicitly log the §6A step 3 return of story-drawn cards (AL-06, MO-06) to their piles, so compliance with full pile-maintenance
- (1×) The tie-draw (event 60) is logged before the roll that produced the tie (event 61), obscuring whether draw-trigger causality (§4) was actually respected or is j
- (1×) GM fate-point expenditure for invoking a player's weakness tag as hostile opposition (event 62) is never itemized separately from the compensating scene-end pay
- (1×) The Beat Frame's mandatory 'owner answers one question, answer is canon' beat (§5 step 5) is not clearly represented as its own event, blurring the line between
- (1×) The Story Pile draw (MI-06) triggered by Mire's accepted compel is added to the rail but never visibly used in fiction or invoked before the scene ends, undercu

## Player one-sentence verdicts on backstory use

- [A s87940] optimizer: Your hunted heretic background was used effectively with real narrative stakes, but some other characters' stronger rolls meant your mechanical moments got sidelined in key confrontations.
- [A s87940] protector: My background felt genuinely integrated, not used *at* me but used *for* me—Verrick especially—though I wish we'd gotten to see the full consequence of Aldous's final empathy roll before the session ended.
- [A s87940] instigator: My reputation worked perfectly for every scenario, but I would've valued more chances to use active exorcism skills that aren't just "be known by name."
- [A s87940] tactician: Mire's disgraced militia background was authentically used to create meaningful stakes and character moments, but it also meant she paid the physical price where other characters found social solutions — fitting for her position, but it left me wanting more agency in how it resolved.
- [A s87941] storyteller: The GM didn't just reference the exile—they made it the whole emotional architecture of the session, and let Ysolde turn that specific pain into saving others, which felt earned and true.
- [A s87941] rules_lawyer: Aldous's backstory was woven through every beat—his vow gave him moral direction, his fear created real stakes, and his old discipline made his choice to defy Verrick at the checkpoint genuinely meaningful.
- [A s87941] lurker: The backstory was used well—invoked naturally as essential to the plot, not padding.
- [A s87941] method_actor: The GM centered Mire's disgracement and gave her a real chance to stand against the man who cast her out, which felt like earned narrative rather than punitive use of her past.
- [A s87942] protector: Ysolde's backstory felt woven through every major beat—not ornamental, but necessary to the solution and to why she's willing to burn her safety for strangers—so it landed very well.
- [A s87942] instigator: Aldous's backstory wasn't just used—it was load-bearing; every major obstacle required something specific from his history, and none of it ever felt artificial or punitive.
- [A s87942] tactician: Morwen's exorcist clarity and willingness to lead were central to the crisis, but the session's emotional weight and personal stakes tilted toward Mire's oath-debt and Ysolde's teacher-legacy, leaving Morwen's own deeper drive less explored.
- [A s87942] optimizer: Mire's backstory was central to the plot and her specific skills (militia training, Notice) made visible differences in key moments, but rapid pacing left less room for personal emotional beats to land.
- [B s87940] optimizer: My backstory as the exiled cook who reads secrets was core to how I solved every problem this session, though the specific oath against the traitor I swore remained unexplored.
- [B s87940] protector: My backstory wasn't just present but mechanically central to the story—the rain-reading was how we won, the soul-saving vow was the entire mission, and the ghost-marks manifested as perception that mattered in real moments.
- [B s87940] instigator: The backstory was used well—woven in organically, central to every major choice, feeling like an expression of who Morwen is rather than a trap set to punish her.
- [B s87940] tactician: My training and debt-obligations shaped key moments well and mattered when they came up, but my core conflict with the Wardens and my vengeful nature remained backgrounded rather than central to the story.
- [B s87941] storyteller: My character's core identity was the literal key to solving this scenario—the GM built the entire encounter around what she *hears* and who she *understands*, and that felt like being seen perfectly.
- [B s87941] rules_lawyer: My aspects weren't just invoked as flavor—they became the actual mechanism of why Aldous was valuable and what made him vulnerable, which felt earned rather than arbitrary.
- [B s87941] lurker: My exorcist's central doubt about the hive's soul was perfectly the heart of this story, and I had the key moment of understanding—but I wish I'd been braver about claiming more of that investigation for myself instead of letting it happen around me.
- [B s87941] method_actor: Mire's disgraced warden status and Order training were used effectively as the emotional spine of her arc, though the stilt-folk community angle and her specific history with Verrick could have been woven in deeper.
- [B s87942] protector: Ysolde's backstory as someone who listens people back to themselves felt built into the scenario's DNA—not ignored, not weaponized, just *used well*.
- [B s87942] instigator: His drowning survival was woven perfectly as the mechanical and narrative core throughout; the Hive-Suspect consequence is earned rather than unfair, though it now blocks progress on his larger vow to cross souls before the flood.
- [B s87942] tactician: The Order training and exorcist expertise were well-used, but the philosophical doubt at Morwen's core—questioning whether the Hive has souls—got overshadowed by narrative urgency and rescue momentum.
- [B s87942] optimizer: My warden background and Order training felt central and well-used throughout, though the personal conflicts with Verrick and the Wardens — and the mortgage hanging over Wick Lane — are clearly being saved for later rather than tested now.
- [C s87940] optimizer: The mill connection and exile complications with Ess and Sela felt organic and excellent, creating real stakes that mattered to Ysolde personally; the heretic and scholar aspects stayed dormant, but this was the right story to spotlight Ysolde the river-wise outsider.
- [C s87940] protector: The backstory was used as real constraint and complication rather than just flavor, which made every choice matter—panic near water, duty to carry souls, inability to lie to the Order—these were tested, not just acknowledged.
- [C s87940] instigator: My backstory felt used well—the oath to Thom, my untouched status, my exorcist role—all became central to the drama instead of window-dressing.
- [C s87940] tactician: Used well—my past wasn't wielded against me unfairly, but it was wielded directly and often, leaving me constantly choosing between my old debts and new loyalties, which is exactly what Mire's character needed.
- [C s87941] storyteller: My backstory wasn't just consulted—it was *the story*, woven through every major scene in ways that gave Ysolde real stakes, real knowledge, and real reasons to be the one doing this, which made me feel like the session was built for this character specifically.
- [C s87941] rules_lawyer: Aldous's backstory felt earned and organic — the rain-reading and Corvus trauma emerged naturally from his concept and skills without being forced or overshadowing others' arcs.
- [C s87941] lurker: My background was respected and my abilities mattered in key moments, but the narrative spotlight went more to other characters' personal stakes (Ysolde's sister, Mire's temple) than to Morwen's own story.
- [C s87941] method_actor: Your temple background made the rescue meaningful and earned, but my past as a disgraced Warden never really caught up with me.
- [C s87942] protector: Ysolde's exile, her Order-marking, her crew-loyalty and protective drive were all threaded through the story without being weaponized against her; that felt right.
- [C s87942] instigator: My backstory felt deeply woven into the session's core mystery in a way that made Aldous feel competent and necessary rather than defined solely by his trauma—he mattered because of what he knew, not just because he'd survived.
- [C s87942] tactician: Morwen's practical expertise as an exorcist was perfectly centered in this story, but her defining philosophical uncertainty about whether the hive has souls remained embedded in action rather than explored through choice.
- [C s87942] optimizer: My background was consistently woven in and made tactically relevant without feeling forced, but the session's structure—social challenges, magical workings, tactical avoidance—never let me do what I trained my whole life to do: actually fight.

## Run status

| Run | Status | Scenes | Draws | Tokens | Error |
| --- | --- | --- | --- | --- | --- |
| pilot-01__A__s87940__r0 | complete | 5 | 4 | 1,540,610 |  |
| pilot-01__A__s87941__r1 | complete | 5 | 4 | 2,088,785 |  |
| pilot-01__A__s87942__r2 | complete | 5 | 4 | 2,122,827 |  |
| pilot-01__B__s87940__r0 | complete | 5 | 0 | 2,246,592 |  |
| pilot-01__B__s87941__r1 | complete | 5 | 0 | 1,064,212 |  |
| pilot-01__B__s87942__r2 | complete | 5 | 0 | 1,124,706 |  |
| pilot-01__C__s87940__r0 | complete | 5 | 7 | 2,252,967 |  |
| pilot-01__C__s87941__r1 | complete | 5 | 6 | 2,040,240 |  |
| pilot-01__C__s87942__r2 | complete | 5 | 4 | 1,827,978 |  |
