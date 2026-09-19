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
