# Changelog — Hex-Nexus Balance Lab

Version numbers are X.Y.Z: Z for number changes, Y for ability or rule changes,
X for pillar changes (Prompts 2.4).

## Iteration 0 — Phase 0 bootstrap

| artefact | version | change |
|---|---|---|
| rules | 1.0.0 | Imported `Hex-Nexus_Rules_v1.0.md` unchanged. Appendix A extracted to `rules/map_v1.json`. |
| roster | 1.0.0 | Initial 10-champion roster, 2 per role, every kit on budget (20-24 by Rules 14.2). |
| engine | 0.1.0 | Full rulebook implementation: map and tile graph, hidden-tile movement and range, flips and flip-back, recall, whole-card cooldown, snake order, chip=AP economy, World Phase, Shop Phase, buff and item cards, Dragon and Baron, protection order, death timers, round-20 tiebreak. 73 unit tests. |
| ai | 1.0.0 | T0_random and T1_greedy against the Policy interface. |

No balance patches yet: Phase 0 produces the baseline, not fixes.

### Iteration 0 batches

| batch | matchup | games | result |
|---|---|---|---|
| batch_0001 | T0 vs T0 | 200 | Baseline. Random play never closes a game: 0% Nexus kills, all 20 rounds. Caught two engine bugs (see below). |
| batch_0002 | T1 vs T1 | 200 | Phase 0 exit batch: 0 anomalies, median 15 rounds, 99.5% Nexus kills. |
| batch_0003 | T1 vs T0 | 100 | AI acceptance: T1 wins 100% (target >=90%). |

### Engine fixes found by the assertions (before the baseline was taken)

| bug | symptom | fix |
|---|---|---|
| Monster respawn onto an occupied hex | monster and champion stacked on one visible hex | a monster reappears only when its own hex is clear (RQ-018) |
| Wave spawning under a friendly champion | wave and champion stacked on the spawn hex | any unit other than a mergeable friendly wave skips that spawn (RQ-027) |
| Tile turning face up inside an ability (REVEAL then MOVE) | movement target node went stale, two champions stacked | a stale tile node resolves to a legal hex inside that tile |

## Iteration 1 — roster expansion to 25 (lead designer instruction)

| artefact | version | change |
|---|---|---|
| roster | 1.0.0 -> 1.1.0 | 15 new champions, 3 per role, taking the roster to 25 (5 per role). Every kit is inside the 22 +/- 2 band on its first pass and uses only Rules 6.3 icons. No existing champion was touched. |
| tests | - | The roster test now asserts an even, arbitrary number of champions per role, plus a new check that no two kits are identical. The fixture roster follows `HEXNEXUS_ROSTER` so older rosters can still be tested. |

New champions: Marrow, Kaelis, Ossuar (Top); Rictus, Bramblehide, Sylphine
(Jungle); Noctis, Quillan, Sable (Mid); Veyra, Brixa, Orrin (ADC); Pallas, Wisp,
Corvane (Support).

**Sampling consequence (RQ-028).** With 5 champions per role,
`random_by_role_no_duplicates` puts each champion in 40% of games. A 2,000-game
batch now gives about 800 games per champion (+/-3.5 pts), and the Rules 14.3
precision of +/-2.2 pts needs roughly 5,000 games. `batch_0004` (400 games) is a
smoke batch for the new kits, not a balance read.

### Iteration 1 batches

| batch | matchup | games | result |
|---|---|---|---|
| batch_0004 | T1 vs T1, roster 1.1.0 | 400 | 0 anomalies. Median 12 rounds, 98.8% Nexus kills, priority 47.5% [42.7, 52.4]. Economy outliers: quillan 5.07x, sable 3.25x, ashwyn 3.15x, ossuar 2.12x the roster mean. |

Batches 0001-0003 were re-run on the fixed engine and report code, so every
report in `reports/` comes from one build. All four now carry 0 anomalies.

### Further fixes in this iteration

| bug | symptom | fix |
|---|---|---|
| Destination hex taken between enumeration and execution | two friendly champions stacked (1 game in 400) | a move onto an occupied hex is refused and the unit stays put; movement is optional |
| Report clobbered the priority win rate | section 5 printed the last role's win rate instead of the first player's | separate variables; the role table now also states that role win rate is 50% by construction under `random_by_role_no_duplicates` |

## Iteration 2 - Phase 1: AI calibration (paused mid-phase)

| artefact | version | change |
|---|---|---|
| ai | 1.0.0 -> 1.1.0 | T2_search (depth-limited look-ahead over the snake order, T1 as the opponent model, per-decision time budget, macro weights) and the six required X_exploit_* policies as weight profiles over the shared evaluator. Evaluation now takes a weight profile; terms added for macro play default to 0 so T1 is unchanged. |
| ai | 1.1.0 -> 1.2.0 | T2 retuned from calibration: World Phase resolved at the leaf, sharper softmax over searched values, full-fidelity opponent model. 1.1.0 is frozen so batches 0005-0007 stay reproducible. |
| engine | 0.1.0 -> 0.2.0 | Publishes the snake order on the state; tracks assists; logs round and activation events; accepts per-policy config in a sim request. Closes two gaps against Prompts 4.D (assists, a compact text replay viewer). |
| tests | - | 94 tests (16 new for the policy contract, T2 behaviour, assists and the 1.2.0 package). |

### Iteration 2 batches

| batch | matchup | games | result |
|---|---|---|---|
| batch_0005 | T1 vs T0 | 200 | T1 wins 97.0% [93.6, 98.6]. Acceptance gate >=90%: PASS. |
| batch_0006 | T2 vs T1 (ai 1.1.0) | 200 | T2 wins 55.5% [48.6, 62.2]. |
| batch_0007 | T2 mirror (ai 1.1.0) | 600 | 0 anomalies. Priority 55.0% [51.0, 58.9], against 47.5% under T1: the first-player advantage grows with stronger play. |
| batch_0008 | T2 vs T1 (ai 1.2.0) | 400 | T2 wins 58.5% [53.6, 63.2]. Acceptance gate >=65%: FAIL, on a tight interval. |
| batch_0009 | T2 mirror (ai 1.2.0) | 400 | 0 anomalies. Priority 48.8% [43.9, 53.6] - the 55.0% of batch_0007 does not reproduce on the calibrated T2, so seat balance is unresolved rather than failing. Median length falls to 11 rounds; 100% Nexus kills. |
| exploit sweep | each exploit vs T2 | 40 each | dive 20.0%, farm 30.0%, split-push 32.5%, objectives 27.5%, turtle 20.0%, cooldown-lock 27.5%; 0 anomalies. No exploit beats T2: the Phase 5 gate is already met. |

Acceptance report: `reports/ai_acceptance_v1.2.0.md`. Three checks pass (T1 vs
T0, no illegal actions, no exploit beats T2), one is inconclusive at this
sample size (the mirror), and three fail: T2 vs T1 at 58.5%, 47 of 100
abilities used in under 5% of their affordable rounds, and a 2,000-game T2
batch projecting to about 4 hours on 4 cores.

### Calibration

Ten T2 variants over 890 games (`reports/calibration/plan_a..d`) all landed
between 52% and 62% against T1. `tools/search_agreement.py` measured the
searched move differing from the greedy move 45.4% of 399 decisions, at an
average cost of 4.1 points of immediate value, for a few points of win rate.
Recorded as a finding about the game's decision structure rather than an AI
backlog item; escalated to the lead designer.

## Iteration 3 - the lead designer's rulings

| artefact | version | change |
|---|---|---|
| rules | 1.0.0 -> 1.1.0 | RQ-001/RQ-002: hidden hexgroups become a refuge. Movement distance and effect distance are now separate - a hidden hexgroup is a shortcut for walking, not for shooting. Champions inside one cannot be reached from outside; minions, structures and monsters keep their own hex, so a tower inside a hidden hexgroup covers its own hex's neighbours. RQ-016: the rulebook's bump-and-continue is implemented rather than simplified. RQ-030: 14.2 credits cut to -2 per AP and -1.5 per cooldown round, ability floor raised to 3, and R capped at 1.75x the Q/W/E mean. |
| roster | 1.1.0 -> 1.2.0 | Refit to the new table: 48 of 100 abilities changed, 10 single-step stat changes, no ability made more expensive. Mean R gross 13.1 -> 9.9. |
| engine | 0.2.0 -> 0.3.0 | Effect geometry separated from movement geometry; bump-and-continue; canonical activation options (stand still, recall home) can no longer be sampled away by the enumeration cap. |
| ai | 1.2.0 | Unchanged. |
| tests | - | 102 tests. |

### Rulings recorded

| id | ruling |
|---|---|
| RQ-031 | The T2-vs-T1 acceptance gate drops from 65% to 60%: ten calibration variants over 890 games all landed between 52% and 62%, and the search-agreement diagnostic shows depth is not the bottleneck. At 58.5% [53.6, 63.2] the check is INCONCLUSIVE against the new gate rather than a pass - the interval straddles it. |
| RQ-032 | Open. Concealment is one-way as ruled, so a champion can shoot out of a hidden hexgroup without being reachable. Watching the exploit sweep for a sniper-in-the-fog strategy. |

## Iteration 4 - RQ-032 retest and the pacing patch

| artefact | version | change |
|---|---|---|
| rules | 1.1.0 -> 1.1.1 | P-0002: tower HP 8 -> 11. One number, the gentlest lever that lands the target. |
| engine | 0.3.0 -> 0.3.1 | Counts attacks made from inside a hidden hexgroup on something outside it, and reports them (Part 9b). Calibration tool takes config_overrides so rules variants can run head to head. |
| ai | 1.2.0 | Adds X_exploit_fogsnipe, the policy RQ-032 is actually about. |
| tests | - | 105, with the tower-HP assertions made config-relative. |

### RQ-032 retested on the corrected rules

The narrow question is clean. X_exploit_fogsnipe - a policy that values standing
in a hidden hexgroup and shooting out of it - loses to T2 at 12.5% [5.5, 26.1]
with concealment one-way as ruled, and at 2.5% with the reveal remedy on. Hiding
and poking is not degenerate, so RQ-032 needs no rule change on its own account.

Measuring it found something larger, logged as RQ-034: 85% of all ability uses
are already made from inside a hidden hexgroup at a target outside it, because a
champion's tile is hidden whenever no enemy stands in it. Champion kills per
game: 17.31 under the literal reading (batch_0004), 0.20 under the refuge as
ruled (batch_0016), 2.92 with the reveal remedy (batch_0017). A 5v5 skirmish is
now settled almost entirely by structures.

### P-0002 pacing sweep (150-game T1 mirrors)

| towers / Nexus | median | p10 | p90 | Nexus kills |
|---|---|---|---|---|
| 8 / 12 (before) | 11 | 9 | 16 | 97.3% |
| 9 / 14 | 13 | 10 | 17 | 96.7% |
| 10 / 12 | 13 | 10 | 17 | 98.0% |
| 10 / 16 | 14 | 11 | 19 | 92.7% |
| **11 / 12 (chosen)** | **14** | 11 | 17 | **98.7%** |

Raising the Nexus as well pushes the tail past the round limit and fails the 95%
floor. Raising tower HP alone lengthens the siege - the phase that actually fills
the rounds - and leaves the close-out decisive.

## Iteration 5 - ai 1.3.0: flank awareness and personalities

| artefact | version | change |
|---|---|---|
| ai | 1.2.0 -> 1.3.0 | Flank terms in the shared evaluation, and five personality profiles built on the T2 macro weights. 1.2.0 stays frozen, so batches 0008-0035 remain reproducible. |
| engine | 0.3.x | `personality_pool` in a sim request: each side draws an appetite per game. Reports read per personality (Part 9c). |
| tests | - | 117. |

### Flank awareness

A hidden hexgroup beside a lane is a gank avenue, and under RQ-036 walking up
to one reveals it. The evaluation now prices both halves of that: `flank_risk`
penalises standing beside a hexgroup that holds enemies, `flank_watch` rewards
standing beside an empty one, which denies it as an approach. The visible
effect is a laner favouring the side of its lane away from the dangerous
hexgroup rather than walking down the middle - which matters most in mid, where
both river hexgroups are in reach. `group_bias` was added alongside for the
personalities that want to fight together.

### Personalities

| name | wants |
|---|---|
| warder | vision and safety: buys Control Wards eagerly, spends them on sight, keeps out of reach |
| brawler | the five-on-five: stays grouped, hunts kills |
| sieger | the map: towers, wave state, the Nexus behind them |
| objective | the clock: Dragon, Baron, and the camps that buy them |
| laner | the lane: farms, keeps its distance, punishes a mistake |

These are not the exploit policies. Each is meant to be a reasonable way to
play, so a batch of mixed match-ups reads more like a play-test evening than a
mirror does: a mirror measures the game against one taste, a spread measures it
against several, which is what a balance number should survive.

Buying a card and holding it turned out to be opposite appetites - a warder
wants a hand full of Control Wards *and* wants to spend them immediately - so
the policy now prices them separately.

`batch_0036` is a plumbing check only (8 games). A real personality read needs
a proper batch; 8 games says nothing about which personality is strongest.

## Iteration 7 - P-0009 and the T2 read at reveal radius 2

| artefact | version | change |
|---|---|---|
| rules | 1.7.0 | unchanged. Rules 1.7.0 (reveal radius 2) read on T2 for the first time: `batch_0039`. |
| config | - | `dragon_ap_each` tried at 2 (P-0009) and left at 1. |
| ai | 1.3.0 -> 1.4.0 | A state machine over the personalities (Handoff §9): a machine is data (default state, commit timer, ordered rules over flat game-state signals), re-evaluated once per round at the first decision after Upkeep, swapping the whole personality profile. Eight generation-1 candidates in `ai/policy_v1_4_0/machines/gen1.json`. 1.3.0 frozen. |
| engine | 0.3.x | `--shard K/N` and `--merge` run one batch across containers; `anchor_share` draws a fixed anchor into one seat of a share of games. Batch results carry each machine's per-round state; the report gains 9d (field ranked by lower confidence bound, record against the anchors, occupancy). `run_batch` checkpoints each finished game to `reports/raw/<batch>.partial.jsonl` and resumes from it. |
| engine | 0.3.x | Two placement fixes from RQ-043: a non-champion entering a hidden tile takes a free hex or stays put; a respawn into a full base overflows to the ring or waits a round. |
| tests | - | 157, all passing. |

### Iteration 7 batches

| batch | matchup | games | result |
|---|---|---|---|
| batch_0039 | T2 personality pool, P-0008 values, rules 1.7.0 | 120 | The T2 read at reveal radius 2 (RQ-038), paired with batch_0038 by seed. Snipes down as the T1 probes said (true snipes 54.4% -> 40.2% of uses), champion-kill AP up 70%, but median length 15 -> 18 and Nexus kills 96.7% -> 78.3%. Personality field unchanged: sieger 69.0%, spread 40. |
| batch_0040 | as batch_0039 with `dragon_ap_each` 2 | 120 | **P-0009, FAIL.** Sieger 74.1%, objective 40.5%, spread 42.5. Dragon takes unchanged, 97 of 120 paired games had the same winner. The AP landed and did nothing: teams are not short of AP (RQ-039). Not adopted. |
| batch_0041 | ai 1.4.0: eight state machines + T2_search + T2_sieger, drawn per game | 400 | **State-machine generation 1 (RQ-040).** Ranked on the lower bound: clock3 66.7%, clock2 61.0%, ap_lead 59.7%, then the pure sieger 57.4%. The winners sit in sieger 43-81% of rounds; machines living in the objective state finish last with T2_search. Nothing beats sieging; a laning opening might. Survivors: the two clocks. |
| batch_0042 | ai 1.4.0 generation 2: ten machines, anchors drawn into half the games | 480 | **RQ-040, generation 2.** Bradley-Terry over all pairings puts the pure sieger mid-field: lane-then-siege machines +0.3 to +0.5 log-odds above it, siege-from-round-1 machines below, a brawl opening far below. Direct records vs the sieger too thin and confounded to confirm. Pacing passes in a sieging field (median 15, 99.4% Nexus). Survivors lane6, clock3_short. |
| batch_0043 | each generation-2 survivor vs T2_sieger, nothing else | 160 | **RQ-040 closed.** lane6 51.1% [41.0, 61.1] over 92, clock3_short 45.6% [34.3, 57.3] over 68. Neither beats sieging from round 1; the generation-2 edge was opposition mix. The state machine is unnecessary; RQ-037 is confirmed from three directions. Field for champion balance: T2_sieger + SM_g2_lane6. |
| batch_0044 | Phase 4 champion read: T2_sieger + SM_g2_lane6 drawn per game, four shards on four cloud sessions | 4000 | **RQ-041.** 10 of 25 champions clear of 45-55: Support and Top broken (wisp 77%, bastion 75%; corvane 27%), Mid split, Jungle and ADC balanced. Income and win rate correlate at 0.6; the Phase 3 AREA engines are the HIGH champions. **RQ-042**: South wins 53.2% [51.7, 54.8]. Pacing in band (median 14, 99.4% Nexus). |
| batch_0045 | Phase 5 exploit sweep: seven exploits vs the settled field, four shards | 560 | **RQ-043, gate met.** Best exploit split-push 21.9% [14.8, 31.1]; five exploits win nothing. Fog-snipe 0% under reveal radius 2. Found two placement bugs (hidden-tile entry, respawn into a full base), both fixed; caveat: exploits are T1 profiles. |

## Iteration 9 - rules 1.8.0: the lead designer's rulings on RQ-039, RQ-041 and RQ-042

| artefact | version | change |
|---|---|---|
| rules | 1.7.0 -> 1.8.0 | **P-0010 (pillar):** structures are never ability targets - only L0 and minion waves damage towers and the Nexus - and structure chips go to the supply, not the pool. **P-0011:** the Dragon card is a reusable Red Buff (2 hits adjacent, cooldown track position 3, at most 2 held, no AP); the Baron is Empowered waves for the rest of the game. Dragon and Baron stay where they are. |
| engine | 0.4.0 | Config knobs for each ruling (`abilities_hit_structures`, `structure_chips_pay`, `dragon_card`, `dragon_ap_each`, `baron_permanent`), defaults on the 1.8.0 side; the 1.7.0 economy stays reachable for old requests. `dragon_track` on the team state. |
| rules | 1.8.0 | **P-0012 (RQ-045):** AREA is a radius-1 disc around a centre placed within range; Longbow moves the centre, not the blast. Config `area_center`. |
| roster | 1.6.0 -> 1.7.0 | **P-0013:** cooldown 2 on the four AREA engines (sable W, wisp W, ashwyn W, quillan R); nothing bought back; exceptions declared. `validate_kit` honours a named `ability_exception`. |
| tests | - | 165. |

The designer's reading of RQ-041: income was meant to come from minions and
monsters and towers were meant to fall to basic attacks; an untagged AREA
that could hit a tower for AP was never the intent, and that is where the
engines' income and the sieger's double payoff came from. RQ-038 (pacing) and
the wider objective question stay open for later.

### Iteration 9 batches

| batch | matchup | games | result |
|---|---|---|---|
| batch_0046 | personality pool, P-0010 alone (1.7.0 rewards kept) | 120 | **Pacing collapses:** 1 Nexus kill in 120, every game to round 20, sieger 93.1% on the tiebreak. Tower HP 16 cannot fall to L0 and waves. The five AREA engines remain (sable 2.64x): AREA is a disc, radius 2 with Longbow. Dragon/Baron secured WR up to 51/50%. |
| batch_0047 | personality pool, P-0010 + P-0011 | 120 | Same pacing collapse as 0046 (tower HP 16). Objectives move the right way: Dragon secured 51 -> 55%, Baron 50 -> 52%, objective personality 38 -> 43%. Verdict deferred to a field where games end. |
| batch_0048 | as batch_0047, tower HP 8 | 120 | Nexus kills 30%, median 20, first tower round 11, 97% of games see a tower fall. Sieger 91% on the tiebreak - unreadable. |
| batch_0049 | as batch_0047, tower HP 6 | 120 | Nexus kills 49%, median 20 (p10 15), first tower round 8. Halfway; the Nexus at 12 is the next wall. |
| batch_0051 | 1.8.0 full, tower HP 4, Nexus HP 8 | 120 | Median 16, Nexus kills 75%, first tower round 4. The first 1.8.0 read where most games end; the sieger is 89.7% on roster 1.6.0. |
| batch_0052 | 1.8.0 full, tower HP 4, Nexus HP 12 | 120 | pending |
| batch_0053 | 1.8.0 full, tower HP 6, Nexus HP 8 | 120 | pending |
| batch_0054 | roster 1.7.0 (P-0013) on the chosen HP pair | 120 | pending |
| batch_0050 | as batch_0048 with P-0012 (centred AREA) | 120 | **P-0012 partial.** Engines down a third (sable 2.54x -> 1.87x, pallas to 1.01x) but four remain above 1.5x. Nexus kills 15% at tower HP 8 - pacing still the wall. |

