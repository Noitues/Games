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
| batch_0009, exploit sweep, acceptance report | - | - | Ordered but not run: work paused. Commands are in docs/HANDOFF.md. |

### Calibration

Ten T2 variants over 890 games (`reports/calibration/plan_a..d`) all landed
between 52% and 62% against T1. `tools/search_agreement.py` measured the
searched move differing from the greedy move 45.4% of 399 decisions, at an
average cost of 4.1 points of immediate value, for a few points of win rate.
Recorded as a finding about the game's decision structure rather than an AI
backlog item; escalated to the lead designer.
