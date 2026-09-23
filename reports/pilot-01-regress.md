# Batch report: pilot-01-regress

Runs: 9 ({'complete': 9}). Spec version(s): ['0.2.0']. Backend(s): ['claude_cli']. Tokens: 17,167,751 (≈ $51.32).

## Blinded analyst conclusions

_Written by the Analyst agent from blinded labels **before** unblinding._

Across three variants tested with only 3 sessions each, self-reported enjoyment (fun/involvement/connection/control/play-again) is essentially indistinguishable between arms — scores are compressed near the top of the 1-7 scale and several means are identical to three decimal places across arms. The more diagnostic signals — paired head-to-head preferences and behavioural/mechanical counts — do show a consistent pattern: the arm with zero deck draws and 100% GM improvisation (structurally, Arm 1) produced the fewest rule violations and was clearly preferred over the arm with the heaviest, mandatory-seeming deck integration (Arm 2, 100% engine draw-usage, highest draw count) by 9-3 in paired comparison, and mildly preferred over the third, referee-mediated deck arm (Arm 3) by 7-5. Arm 2 mildly beat Arm 3 in preference (7-5) despite Arm 2 generating the most rule violations (mean 10 vs. 5.3 for Arm 1 and 7.7 for Arm 3) and the most GM/engine ambiguities encountered (19 vs. 12.7 and 18.3). Arm 2 was the only variant that reliably surfaced backstory content to all players and hit the deck-guarantee metric every run (100%/100%), whereas Arm 3 never did so in any of its three runs (0%) despite drawing cards, and Arm 1 (no deck) did so unevenly (33% average, ranging 0-100% across its three runs). Net: the deck/engine mechanic that most reliably delivers its structural promise (Arm 2) comes with a measurable cost in rule violations and is the least-preferred option head-to-head, while the simplest, deck-free condition (Arm 1) is cleanest mechanically and most preferred by players, but at the cost of unreliable backstory coverage. Arm 3 sits in between on most measures — a plausible middle-ground design — but its complete failure to surface backstory to all players in any session is a concrete negative finding worth investigating regardless of overall preference standing.

- Structural fingerprint: Arm 1 has zero deck draws, zero card-supplied complications, 100% improvisation share, and 0% engine card-usage rate — it appears to be a deck-free/pure-improv condition. Arm 2 and Arm 3 both use the deck (draws 6.0 vs 3.3 per session respectively) but differ sharply in reliability and referee card-usage rate (Arm 2: engine 100%/referee 57.6%; Arm 3: engine 100%/referee 80.7%).
- Paired head-to-head preference (most trustworthy metric given ceiling-compressed surveys): Arm 1 beats Arm 2 decisively (9-3), Arm 1 beats Arm 3 narrowly (7-5), and Arm 2 beats Arm 3 narrowly (7-5). Net ranking by direct preference: Arm 1 > Arm 2 ≈ Arm 3 (Arm 2 slightly ahead of Arm 3), all on very small comparison counts.
- 1-7 self-report survey scores show negligible, likely-noise-level differences between arms (e.g., 'involvement' mean is 6.417 in all three arms; 'fun' ranges only 6.17-6.42; 'play_again' ranges only 6.83-6.92) — the surveys do not discriminate the arms and should not be used alone to judge quality.
- Rule violations scale with deck/engine complexity: Arm 1 (no deck) mean 5.3 violations, Arm 3 (deck, referee-heavier) mean 7.7, Arm 2 (deck, engine-heavy, most draws) mean 10.0 — driven mainly by engine-side violations in Arm 2 (5.7) vs. referee-side violations dominating in Arm 3 (4.7) and Arm 1 having the fewest of both types.
- Ambiguity/rules-confusion counts follow the same pattern: Arm 1 encountered fewer distinct ambiguous rulings (mean 12.7) than Arm 2 (19.0) or Arm 3 (18.3); Arm 2 and Arm 3 share heavy overlap in specific flagged sections (deck/Beat-Frame procedure, §6A draw-trigger table), while Arm 1's ambiguities cluster on core mechanics (compels, invokes, passive/active opposition) rather than deck rules.
- Backstory/content-guarantee delivery differs starkly: Arm 2 achieved 100% 'all players get backstory' and 100% 'deck surfaced to all players' in every run; Arm 1 achieved this only 33% of the time on average (0-100% range, highly inconsistent); Arm 3 achieved 0% in all three runs — despite drawing cards, it never delivered this guarantee to all players in any session tested.
- Fate-point economy and compel activity are highest in Arm 2 (most FP earned/spent, most compels accepted at 7.7, highest compel-accept ratio 0.885, most clock progression at 2.0 marks) and lowest/least active in Arm 1 (fewest compels accepted 4.7, zero clock marks in every run), with Arm 3 intermediate on most of these.
- Complaint categories are low-count and long-tailed in all arms (n≈15-20 total complaints per arm across many sub-categories); no complaint category stands out as a robust between-arm difference given the small sample.

Caveats:
- Only n=3 sessions per arm (12 player-level survey observations, but those are clustered within 3 runs, not independent) — nearly every point estimate has a wide lo-hi range, so most numeric differences below are directional/suggestive, not statistically established.
- Self-report survey scores (1-7) are heavily ceiling-compressed (most means 5.5-7, many identical to 3 decimal places across arms, e.g. involvement=6.417 in all three arms), so they have almost no power to discriminate the arms here — paired-preference and behavioural-count data are more informative and were weighted accordingly.
- The paired-preference totals (12 comparisons per pairing) are themselves generated from the same small set of sessions/players, so they are not independent replications either; a 9-3 or 7-5 split with n=12 is a modest signal, not proof.
- I do not know which rule variant each 'Arm' label corresponds to (deck-optional vs. mandatory, engine- vs. referee-triggered draws, etc.); all interpretation below is inferred structurally from the metrics themselves (e.g., zero deck_draws in Arm 1) and should be checked against the actual condition manifest before drawing design conclusions.
- The 'guarantee_failed' flag is 0 for all arms even though 'backstory_all_players_rate' is 0.0 for Arm 3 in every run — these two metrics appear to measure different things (an explicit hard-fail check vs. an observed outcome rate), and the discrepancy should be reconciled before treating Arm 3's 0% rate as a confirmed design failure.
- Complaint tallies and ambiguity-ID lists are long-tailed with many singleton categories across only 3 runs; treat any single complaint or ambiguity-ID count as anecdotal, not a reliable frequency estimate.
- No formal significance testing was performed (none is really warranted at n=3); all comparisons should be read as 'consistent with a difference' at best, pending more runs.

## Unblinding

| Blinded label | Arm |
| --- | --- |
| Arm 1 | B |
| Arm 2 | A |
| Arm 3 | C |

## Structural metrics (per session, mean [95% bootstrap CI])

| Metric | A | B | C |
| --- | --- | --- | --- |
| Every player's backstory drove an event | 1.00 [1.00, 1.00] (n=3) | 0.33 [0.00, 1.00] (n=3) | 0.00 [0.00, 0.00] (n=3) |
| Every player's own card surfaced from the deck | 1.00 [1.00, 1.00] (n=3) | — | — |
| Deck draws / session (target 5–8) | 6.00 [6.00, 6.00] (n=3) | 0.00 [0.00, 0.00] (n=3) | 3.33 [2.00, 5.00] (n=3) |
| Draw costs using the drawn card: engine tag check | 1.00 [1.00, 1.00] (n=3) | — | 1.00 [1.00, 1.00] (n=3) |
| Draw costs using the drawn card: referee judgment | 0.58 [0.47, 0.65] (n=3) | 0.00 [0.00, 0.00] (n=3) | 0.81 [0.77, 0.83] (n=3) |
| Mean player FP at session end (target 1–5) | 2.33 [2.00, 3.00] (n=3) | 1.50 [0.50, 2.00] (n=3) | 1.83 [1.25, 2.25] (n=3) |
| Spotlight Gini: turns | 0.01 [0.00, 0.02] (n=3) | 0.02 [0.00, 0.06] (n=3) | 0.02 [0.00, 0.07] (n=3) |
| Spotlight Gini: invokes | 0.29 [0.13, 0.52] (n=3) | 0.27 [0.09, 0.47] (n=3) | 0.16 [0.12, 0.19] (n=3) |
| Scenes / session | 4.33 [4.00, 5.00] (n=3) | 5.00 [5.00, 5.00] (n=3) | 5.00 [5.00, 5.00] (n=3) |
| Clock marks | 2.00 [0.00, 3.00] (n=3) | 0.00 [0.00, 0.00] (n=3) | 1.00 [1.00, 1.00] (n=3) |
| Compels accepted | 7.67 [7.00, 8.00] (n=3) | 4.67 [3.00, 6.00] (n=3) | 5.67 [5.00, 6.00] (n=3) |
| Compels refused | 1.00 [0.00, 3.00] (n=3) | 1.00 [0.00, 2.00] (n=3) | 1.00 [0.00, 2.00] (n=3) |
| GM-improvised complications | 4.67 [4.00, 6.00] (n=3) | 7.33 [7.00, 8.00] (n=3) | 2.67 [2.00, 3.00] (n=3) |
| Card-supplied complications | 9.33 [9.00, 10.00] (n=3) | 0.00 [0.00, 0.00] (n=3) | 8.33 [8.00, 9.00] (n=3) |
| Improvisation share | 0.33 [0.29, 0.40] (n=3) | 1.00 [1.00, 1.00] (n=3) | 0.24 [0.20, 0.27] (n=3) |
| Rule violations (engine + referee) | 10.00 [5.00, 18.00] (n=3) | 5.33 [2.00, 10.00] (n=3) | 7.67 [6.00, 9.00] (n=3) |
|   — engine refusals | 5.67 [2.00, 12.00] (n=3) | 4.00 [1.00, 10.00] (n=3) | 3.00 [0.00, 6.00] (n=3) |
|   — referee | 4.33 [2.00, 6.00] (n=3) | 1.33 [0.00, 3.00] (n=3) | 4.67 [3.00, 6.00] (n=3) |
| Ambiguity records | 19.00 [18.00, 20.00] (n=3) | 12.67 [11.00, 14.00] (n=3) | 18.33 [16.00, 21.00] (n=3) |
| Backstory guarantee failures | 0.00 [0.00, 0.00] (n=3) | 0.00 [0.00, 0.00] (n=3) | 0.00 [0.00, 0.00] (n=3) |
| Within-session variance of involvement | 0.35 [0.19, 0.69] (n=3) | 0.23 [0.19, 0.25] (n=3) | 0.31 [0.00, 0.75] (n=3) |
| Compel accept ratio | 0.885 | 0.824 | 0.85 |
| Tension values seen | {1: 9, 2: 4, 3: 3} | {} | {1: 9, 2: 4, 3: 5} |

## Experiential (LLM player self-reports, 1–7; weak evidence)

| Score | A | B | C |
| --- | --- | --- | --- |
| fun | 6.42 [6.17, 6.67] (n=12) | 6.33 [6.08, 6.58] (n=12) | 6.17 [5.83, 6.50] (n=12) |
| involvement | 6.42 [6.08, 6.75] (n=12) | 6.42 [6.17, 6.75] (n=12) | 6.42 [6.00, 6.75] (n=12) |
| connection | 6.50 [6.08, 6.83] (n=12) | 6.25 [5.83, 6.58] (n=12) | 6.67 [6.42, 6.92] (n=12) |
| control | 5.67 [5.25, 6.00] (n=12) | 5.67 [5.25, 6.00] (n=12) | 5.50 [5.17, 5.92] (n=12) |
| play_again | 6.92 [6.75, 7.00] (n=12) | 6.92 [6.75, 7.00] (n=12) | 6.83 [6.58, 7.00] (n=12) |

### Paired differences (same seed, same character and personality)

- **A-B**: involvement 0.00 [-0.33, 0.33] (n=12); connection 0.25 [-0.17, 0.67] (n=12); fun 0.08 [-0.25, 0.42] (n=12); control 0.00 [-0.58, 0.58] (n=12)
- **A-C**: involvement 0.00 [-0.25, 0.25] (n=12); connection -0.17 [-0.58, 0.17] (n=12); fun 0.25 [-0.17, 0.58] (n=12); control 0.17 [-0.25, 0.58] (n=12)
- **C-B**: involvement 0.00 [-0.42, 0.42] (n=12); connection 0.42 [-0.08, 0.92] (n=12); fun -0.17 [-0.50, 0.08] (n=12); control -0.17 [-0.67, 0.42] (n=12)

Lurker involvement by arm: A 5.00 (n=1); B 6.00 (n=1); C 5.00 (n=1)

### Survey means by personality

| Personality | A involvement | B involvement | C involvement | A connection | B connection | C connection |
| --- | --- | --- | --- | --- | --- | --- |
| instigator | 6.50 [6.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 5.50 [5.00, 6.00] (n=2) | 6.50 [6.00, 7.00] (n=2) |
| lurker | 5.00 (n=1) | 6.00 (n=1) | 5.00 (n=1) | 6.00 (n=1) | 7.00 (n=1) | 6.00 (n=1) |
| method_actor | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 6.00 (n=1) | 7.00 (n=1) |
| optimizer | 6.50 [6.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 6.00 [6.00, 6.00] (n=2) | 6.00 [5.00, 7.00] (n=2) | 5.50 [5.00, 6.00] (n=2) | 7.00 [7.00, 7.00] (n=2) |
| protector | 6.50 [6.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 7.00 [7.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) |
| rules_lawyer | 7.00 (n=1) | 6.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) | 7.00 (n=1) |
| storyteller | 6.00 (n=1) | 6.00 (n=1) | 7.00 (n=1) | 6.00 (n=1) | 6.00 (n=1) | 7.00 (n=1) |
| tactician | 6.50 [6.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) | 7.00 [7.00, 7.00] (n=2) | 6.50 [6.00, 7.00] (n=2) |

### Paired transcript preference (blinded, same cohort and seed)

- A-B: {'B': 9, 'A': 3}
- A-C: {'A': 7, 'C': 5}
- B-C: {'C': 5, 'B': 7}

### Fate point flow by personality (mean per session: earned / spent / end)

- **A**: instigator 2/5/0.5; lurker 3/2/4; method_actor 3/2/4; optimizer 3.5/2/4.5; protector 1.5/2.5/2.5; rules_lawyer 0/3/0; storyteller 1/4/0; tactician 2.5/3/2.5
- **B**: instigator 1/3.5/0.5; lurker 1/4/0; method_actor 2/4/1; optimizer 3/3/3.5; protector 0.5/1/2.5; rules_lawyer 0/3/0; storyteller 0/2/1; tactician 1/2.5/1.5
- **C**: instigator 1.5/3.5/1; lurker 1/1/3; method_actor 2/2/3; optimizer 1.5/2.5/2.5; protector 2/3/2; rules_lawyer 1/3/1; storyteller 1/2/2; tactician 1/3/1

### Complaint clusters (keyword buckets over 'most frustrating')

- **A**: {'other': 6, 'dice/luck': 2, 'agency/control': 2, 'spotlight/ignored': 2, 'pacing': 1, 'rules/confusion': 1}
- **B**: {'other': 7, 'spotlight/ignored': 3, 'rules/confusion': 2, 'agency/control': 1, 'unfair/punishing': 1}
- **C**: {'other': 6, 'dice/luck': 3, 'agency/control': 3, 'rules/confusion': 2, 'pacing': 1}

## Ambiguities

| Count | ID / section | Issue | Interim ruling |
| --- | --- | --- | --- |
| 16 | AMB-27 | Success with style on create advantage: the aspect's 2 free invokes AND the deck peek, or one of them? | Both: the aspect keeps 2 free invokes and the player may also peek. |
| 9 | AMB-12 | Stress box values are unspecified. | Fate Core: boxes 1 and 2; Physique/Will +1/+2 adds a 3 box, +3 or more adds 3 and 4. |
| 6 | AMB-01 | Arm A lists 'Attention', which the spec never defines. | Not modelled. |
| 6 | AMB-22 | Does a GLOBAL anchor give the GM a free invoke like a GM card? | Yes, GLOBAL cards placed on the rail give the GM 1 free invoke that scene. |
| 4 | AMB-19 | Tie on an attack: 'success at minor cost' but 0 shifts of harm. | Attacker gets a boost (Fate Core) and the deck draw still happens. |
| 3 | AMB-03 | Does the session end after the climax scene? | Yes: the climax scene is the last scene of the session. |
| 3 | AMB-10 | Growth from 'roll fails after one of its tags was invoked' — invoked by whom? | Owner's own invokes only. |
| 3 | AMB-04 | Do tension adjustment rows stack? | All applicable rows are summed, then clamped to 1-6. |
| 2 | AMB-23 | Success at major cost on an attack: how much harm lands? | The attack lands for 1 shift. |
| 1 | §3 (Opposition, passive / Invokes) | Event 20: Morwen's Overcome vs THREAT T-01 shows opposition +3, built (per the note 'GM invokes: ignores pain entirely [T-01]') from Average | Treated as legal: the GM's free invoke on a face-up GM card may be spent to add a flat +2 to passive opposition instead of counting that sam |
| 1 | §6 Adjusting Tension | Event 46 applies a -1 Tension adjustment ('resolved -1') at scene end, but the table only grants -1 for 'The party resolved a THREAT or fill | Treated the successful social overcome of Sergeant Colm (tied to the Causeway Wardens checkpoint) as equivalent to resolving the scene's obs |
| 1 | §4 step 2 (Resolving a drawn player card) | The compel built from MO-03 (event 37) uses the power tag 'Stands against the Wardens' torches' rather than the card's weakness tag 'Risks e | GM judged the power tag as directly causing the trouble (it names the exact provocation — torches — driving the compel) and used it instead  |
| 1 | §3 Outcomes and deck draws (Tie row) | The tie occurred on Ysolde's create-advantage roll, but the drawn card (MO-03) belongs to Morwen, and the resulting 'minor cost' compel is n | Allowed the minor cost to manifest as a scene-wide complication involving a different player (Morwen) than the one who rolled, consistent wi |
| 1 | §5 | Beat Frame BETRAYAL has open blanks WHO and WHY. The first drawn card, L-01 (LOCATION, whose table-type is WHERE), matches no open blank and | A card whose natural type-blank is already filled by another card is treated as if its type matched no open blank, and it falls through to t |
| 1 | §3 | On event 80 (Morwen's Overcome vs the Order Patrol, opposition +3), the GM used a free invoke on F-02's tag 'commands pilgrim loyalty' on th | Treated as compliant absent contrary evidence; the table should log which named tags set passive-opposition +1 increments going forward so t |
| 1 | §6A | Two story cards were added at scene cleanup (SN-02 'Pell, the Bought Guide' and SN-03 'Order Patrol Still Watching'), but neither event reco | Assumed Pell was filed to Aldous's Player Story Pile (ties to his card) and the Order Patrol to the GM Story Pile (ties to no single charact |
| 1 | §5 (Beat Frame procedure, step 5) | The rule requires the GM to ask the card owner one question about the filled blank and treat their answer as canon. For YS-02's WHO fill (ev | Treated the compel narration in event 105 as satisfying the step-5 question/answer requirement, since it names what Ysolde promised Elara. |
| 1 | §6A (pile maintenance — Add) | The rule says a newly-added NPC 'goes to a player's pile if it ties to one character, otherwise to the GM Story Pile,' but does not say what | Assigned Toma (SMO-02) to Morwen's Story Pile, on the basis that she was the acting character in the scene's culminating beat toward the NPC |
| 1 | §6A (Draw triggers table) | The trigger table requires that a compel-triggered or concede-triggered story draw's card 'must involve' or 'must feature' in the complicati | The table treated the initiating compel/concede's own narration (using the original live card) as sufficient, and let the freshly drawn stor |
| 1 | §4 (Outcomes and deck draws) / climax override in §4 ('When the deck runs out') | During the climax, ties and major costs draw from face-up GM tags instead of the Session Deck. The spec does not say whether the chosen face | The table allowed any currently face-up GM tag (from any card on the rail) to source a climax-mode cost, regardless of which specific roll t |
| 1 | §8 (Consequences strain cards / Card destruction) | Ysolde's card YS-03 was Strained by a Mild consequence at event 153, then sacrificed via concession at event 156-157 in the very same scene, | The table allowed the Strained card to be sacrificed, treating concession/sacrifice as independent of the ordinary invoke-liveness restricti |
| 1 | AMB-16 | A draw is required but the deck is empty outside a climax. | The cost uses a face-up GM tag, as in a climax. |
| 1 | §4 (Resolving a drawn player card, step 4) / §3 outcomes table | The spec doesn't say whether the deck draws for the major-cost roll (event 16) and the two tie rolls (events 19, 21) must be resolved in ord | Allowed deferred/batched resolution; each cost/compel event was matched to its triggering roll via the for_event/caused_by fields rather tha |
| 1 | §4 step 4 | The rule says that when a drawn player card's compel is refused, 'the GM builds the cost from a face-up GM tag instead,' but the spec doesn' | None was applied at the table for event 24; no discrete cost event was produced, which is logged below as a violation rather than resolved b |
| 1 | §5 (Beat Frame procedure, step 4) | Step 4 only specifies how ROOTS/REACH (player) cards should be interpreted when filling a blank (person/place or motive). It gives no guidan | GM was allowed to freely personify/narrate the GM card's tags to satisfy the mismatched blank, as long as one of its tags (here 'brings feve |
| 1 | §5 (Beat Frame procedure, step 4) | MO-04 is a REACH card, which step 4 says 'becomes the motive,' but the type-mismatch resolution (step 3) forced it to fill the WHERE blank i | GM blended the REACH tag into a location description (a shrine tied to the Priest who seeks Morwen) rather than a pure motive, treating the  |
| 1 | §5 (Beat Frame procedure, steps 5–6) | The written procedure has the card owner answer the GM's question (step 5) before the card's compel/surfacing (step 6). In the log, compel a | Table treated the step order as non-binding; surfacing/compel happened first, GM's question followed once the card was live. |
| 1 | §6 (Tension adjustment table) | The table's -1 row applies only when 'the party resolved a THREAT or filled a player's goal.' Event 62-64 applied -1 tension for successfull | HAZARD cards were treated as equivalent to THREAT/FACTION for the -1 tension row. |
| 1 | §6A | The spec doesn't state whether a Story Pile draw triggered by an accepted compel must occur before the compel's complication is narrated (so | The table treated the draw as happening after the compel was already fixed, and did not go back to weave the drawn card's tags into the comp |
| 1 | §3 (Opposition, active NPC) | The rules cap passive opposition at Great (+4) but say nothing about a ceiling for active Named-NPC opposition (here the Hive Mother rolls t | Treated as unbounded, per 'Named NPCs roll 4dF + their rating as active opposition, as in Fate' with no stated cap. |
| 1 | §6A (draw triggers table, row 1) | For both compel-triggered Story Pile draws in this scene (event 11 → AL-06; event 22 → MI-05), the compel's complication was fully narrated  | Treated the drawn card (AL-06 / MI-05) as informing the ongoing narration and any follow-up beats rather than requiring the compel's origina |
| 1 | §6A (draw triggers table, GM free invoke column) | The rule states the GM gains 1 free invoke on the pile card drawn from a non-deck compel, but the log shows no explicit 'GM +1 free invoke'  | Assumed the grant occurred silently at the same moment as the rail_add row and simply wasn't given its own line; treated the free invoke as  |
| 1 | §5.4 | The rule for filling Beat Frame blanks with a card's tag only spells out the procedure for player ROOTS/REACH cards ("becomes a specific per | Treated the same as the worked example: the GM narrated the blank directly from the drawn card's power tag content (the hostage-camp describ |
| 1 | §7 | The log records 'Trigger fired: M-2' with note 'scene_start:3' during scene 2's cleanup (event 52), before Scene 2 End (event 53). The spec' | Treated the trigger's underlying in-fiction condition as having been satisfied during scene 2, logged the firing at cleanup per the checklis |
| 1 | §5 | In the FALSE SANCTUARY beat frame (open blanks WHERE/HOW), neither drawn card's table type (F-01=FACTION→WHO, MO-03=REACH→WHY) matched an op | GM narrated MO-03's chosen power tag ('Can calm a hive-touched victim') as the method the shelter's danger/relief works ('hides ◆HOW'), repu |
| 1 | §6A | For a compel that did not come from a deck draw (events 73 and 77), the rule says 'the complication must involve the drawn NPC or move the d | The table drew the card immediately after logging the accepted compel, placed it face-up with its free invoke, and did not retroactively rew |
| 1 | §4 Cleanup at scene end / §7 Backup modules | L-05 was placed face-up via module deployment (not a Session Deck draw), was never invoked in scene 4, and has no rail_remove/discard event  | Treated as if the GM implicitly 'kept' L-05 on the rail for the next scene, since no discard event was logged and nothing in §7 forbids a mo |
| 1 | §7 The rail / §2 card provenance | Event 139 targets card H-03 (a HAZARD card, per its prefix) but no rail_add event for H-03 appears anywhere in the scene-4 log, so it's unve | Assumed H-03 was already face-up on the rail from a prior scene (outside this excerpt) and simply persisted, since no rail_add for it was ex |
| 1 | §5 Beat Frame procedure, step 5 | The spec requires the GM to ask the card owner 'one question about the filled blank' whose answer becomes canon, as a distinct step before t | Treated the compel's own narrative text as satisfying the answer-the-question step, since no separate declare/answer event was logged. |
| 1 | §3 Invokes / Free invokes from cards | Event 139's GM invoke list includes 'aspect A-1.4.5 (1 free)', a free invoke on an aspect not tied to any listed card, module, or prior succ | Treated as a fiction-made temporary aspect (permitted under §3's 'temporary situation and character aspects are still made up at the table') |

## Referee friction points (all runs)

- (1×) §3: No explicit rule for whether a face-up GM card's free invoke can be spent to boost a passive (non-rolled) opposition value by +2, versus the flat +1-per-tag
- (1×) Engine refusal on the trigger 'WHEN the party leaves the road or causeway' as 'not an unused fictional trigger' sits awkwardly next to §7's own worked example '
- (1×) Engine refusal for 'active opposition from unknown NPC Hive-Touched Pack' highlights that §3 says 'Named NPCs roll 4dF + their rating as active opposition' but 
- (1×) Tension adjustments cite a terse 'resolved' justification that doesn't map cleanly onto the four listed §6 conditions, making it hard to audit whether -1 was ea
- (1×) Choosing between a drawn card's default weakness tag and an allowed power tag for a compel (§4 step 2) relies on a subjective 'causes trouble directly' test wit
- (1×) Free-invoke accounting on face-up GM cards (e.g., paying 1 fp to invoke H-03 in event 34) depends on knowing whether that card's one-time scene free invoke was 
- (1×) The engine had to refuse three separate attempts to set active opposition from an unnamed/unrated 'Order Patrol' NPC before the GM landed on a valid passive-opp
- (1×) The Beat Frame type-mismatch fallback rule (§5) doesn't anticipate a card whose natural type-blank is already occupied by an earlier mismatched card, forcing an
- (1×) Passive-opposition math is logged only as a final number (e.g., '+3') without recording which face-up tags contributed the increments, making it impossible to v
- (1×) Story Pile draw MO-06 (events 128-129) is missing its mandated GM free-invoke grant (§6A), and no logged text shows the draw's tags actually shaping the complic

## Player one-sentence verdicts on backstory use

- [A s87940] optimizer: Ysolde's backstory was woven expertly into the narrative through Tamsin and the Cartel, making her essential to solving multiple problems, though the specifics of her exile from the Reed-Kin clans remain a mystery waiting to be told.
- [A s87940] protector: My backstory was woven through completely and the rain-reading gained real mechanical weight, but I wish the ending had let me guide the party to safety rather than watch someone else sacrifice herself to end the crisis.
- [A s87940] instigator: My powers and concept were used brilliantly and at the center of everything, but the deeper story of who I am—orphan, survivor, pilgrim guide—stayed as backdrop instead of becoming active.
- [A s87940] tactician: The background felt integrated—it provided meaningful competencies (reading ground, holding formations, knowing Cartel culture) and thematic constraints without being used against me unfairly.
- [A s87941] storyteller: Used well, especially the heretical knowledge as my signature ability, though the exile felt like a complication imposed rather than an asset I brought, and the climax was shaped by my reaching but resolved by Mire's final strike.
- [A s87941] rules_lawyer: Aldous's identity as a survivor and reader of omens was genuinely central to how challenges were built, making each obstacle feel personally tailored to my character rather than generic.
- [A s87941] lurker: My background was used well and felt like real consequences, but mostly in ways that pulled me into situations rather than letting me choose my path.
- [A s87941] method_actor: Your orphanage background was the emotional core of this session, used to create real moral conflict and personal stakes, and it was used thoughtfully — not against you, even when the outcome wasn't the redemption you hoped for.
- [A s87942] protector: My backstory felt woven in really well—the Order connection, Tamsin's teaching, Ysolde's crew-protector role all came together naturally and made her the logical center of multiple scenes.
- [A s87942] instigator: My past wasn't just background texture—it was the shape of everything that happened, and the GM deployed it with respect and precision.
- [A s87942] tactician: Your backstory as the first outbreak's survivor who refuses to let people burn felt deeply essential—especially at the cellar and when bringing Aldous back—though the relentless pacing didn't leave room for the cautious, methodical planning approach you described wanting to play.
- [A s87942] optimizer: My background with the Cartel and guard training made me tactically essential to the mission, which felt earned and good, but the session's relentless pacing meant I didn't get breathing room to sit with the emotional complexity of my disgrace or what it costs to still fight like I'm badged.
- [B s87940] optimizer: Ysolde's defining trait—that she hears everything—was treated not as a passive flavor point but as the story's solution, and that felt like being truly seen.
- [B s87940] protector: Your vow to cross every soul felt genuinely vital to this story's resolution, and your connection to drowned things shaped not just how you won but why you were the one who could.
- [B s87940] instigator: Morwen got to be effective and central, but the actual complexity of her doubt was left on the table.
- [B s87940] tactician: Mire's backstory was woven through the whole session and made her central to it—her history wasn't just flavor, it shaped what she could and couldn't do, and what she had to stand firm on.
- [B s87941] storyteller: Her listening ability was woven into every major moment and felt vital, not incidental, which was satisfying—but everything cost her blood, and she ended the session badly wounded with her other aspects untouched.
- [B s87941] rules_lawyer: My fortune-teller's gifts were the key to reading the swarm's weakness, right up until they made me the hive's marked target.
- [B s87941] lurker: My backstory wasn't just acknowledged—it was the foundation of every scene, and the GM created situations specifically designed to test the contradictions in my vows and doubts.
- [B s87941] method_actor: The tension between "still holds the line" and "disgraced outcast" was executed really well—it gave Mire genuine weight and made every choice feel costly.
- [B s87942] protector: My exile and protective core felt well-used thematically throughout, but it could have had more teeth and more personal consequences.
- [B s87942] instigator: Used well—Aldous's survival and ghostly communion felt mechanically real, not just decorative. He could *perceive* and *do* things other characters couldn't because of who he was.
- [B s87942] tactician: My Order-trained background was used exceptionally well and made Morwen's expertise genuinely matter in ways that affected the outcome; my trouble was invoked fairly but heavily, which limited my agency more than I'd have liked.
- [B s87942] optimizer: My aspects were used mechanically for bonuses, but the deeper threads - why I'm disgraced, what I owe, who I am beyond the wall - were left unexplored.
- [C s87940] optimizer: Ysolde's exile and heresy were threaded through the session with real sophistication, turning her marked status from a liability into the core of her character's arc toward redemption.
- [C s87940] protector: My backstory was used well and drove meaningful, character-defining choices, though much of it felt like pieces being placed for future consequences rather than arcs finding resolution.
- [C s87940] instigator: My background was actively used to create moral weight rather than just color, especially around the Order and the nets, which made my uncertainty about the hive-touched feel like a real tension instead of just a concept.
- [C s87940] tactician: Mire's orphanage training was integrated throughout and felt great, but her Cartel obligations and Verrick disgrace haven't surfaced yet, leaving her deepest complications still waiting to be ignited.
- [C s87941] storyteller: Ysolde's background—the exile, the water-reading, the forbidden knowledge—was woven through the entire session as both plot points and active solution paths, which felt genuinely excellent.
- [C s87941] rules_lawyer: My background wasn't ignored or used unfairly—it was central to every scene—but it kept turning into genuine moral complications that sometimes felt inescapable.
- [C s87941] lurker: Her background was used well in specific, earned moments (the compel, the vow's thematic relevance) but her deliberate quietness meant not everything on her sheet got showcased—not ignored or unfair, just selective by design.
- [C s87941] method_actor: My character's core drive to hold the line despite disgrace and cost became the whole session—which is exactly right for Mire, even though it means every choice bleeds her a little more.
- [C s87942] protector: Ysolde's background felt genuinely integrated, particularly the ferryman and exile threads, which gave real weight and texture to her choices throughout.
- [C s87942] instigator: Aldous's backstory wasn't texture or flavor text—it was the foundation the entire narrative was built on, with vulnerabilities transformed into assets exactly when the story needed them most.
- [C s87942] tactician: Morwen's backstory—the trauma, the exorcism, the Sallowmere knowledge, the refusal to burn victims—was central to the session's shape, not grafted on or used against her, and every scene let her live into those themes.
- [C s87942] optimizer: Mire's background made her the natural tactical leader in crisis moments, but her Cartel debt and personal vendetta didn't get enough activation to feel like they mattered to this story.

## Run status

| Run | Status | Scenes | Draws | Tokens | Error |
| --- | --- | --- | --- | --- | --- |
| pilot-01-regress__A__s87940__r0 | complete | 5 | 6 | 2,771,027 |  |
| pilot-01-regress__A__s87941__r1 | complete | 4 | 6 | 2,385,063 |  |
| pilot-01-regress__A__s87942__r2 | complete | 4 | 6 | 2,012,065 |  |
| pilot-01-regress__B__s87940__r0 | complete | 5 | 0 | 989,255 |  |
| pilot-01-regress__B__s87941__r1 | complete | 5 | 0 | 1,614,280 |  |
| pilot-01-regress__B__s87942__r2 | complete | 5 | 0 | 1,255,309 |  |
| pilot-01-regress__C__s87940__r0 | complete | 5 | 5 | 2,030,824 |  |
| pilot-01-regress__C__s87941__r1 | complete | 5 | 2 | 2,013,663 |  |
| pilot-01-regress__C__s87942__r2 | complete | 5 | 3 | 2,096,265 |  |
