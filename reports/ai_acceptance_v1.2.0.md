# AI acceptance report - ai 1.2.0, roster 1.1.0

Generated 2026-09-19 20:11:59. Batches: batch_0005 (T1 vs T0), batch_0008 (T2 vs T1), batch_0009 (T2 mirror), plus a 40-game sweep per exploit policy against T2.

## Acceptance checks (Prompts 4.C)

| check | value | verdict | evidence |
|---|---|---|---|
| T1 beats T0 in >=90% of games | 97.0% [93.6, 98.6] | **PASS** | batch_0005 |
| T2 beats T1 in >=65% of games | 58.5% [53.6, 63.2] | **FAIL** | batch_0008 |
| Mirror T2 vs T2, seats swapped, lands at 50 +/- 2% | 48.8% [43.9, 53.6] | **INCONCLUSIVE** | batch_0009 |
| No illegal action is ever submitted | 0 illegal states | **PASS** | all batches |
| Every ability used >5% of the time under T2 | 47 of 100 below 5% | **FAIL** | batch_0009 |
| Decisions stay inside the time budget | 7.42s per game wall clock on 4 workers; a 2,000-game T2 batch projects to 247 min | **FAIL** | batch_0009 |
| No exploit policy beats T2 more than 60% (Phase 5 gate) | worst is X_exploit_splitpush at 32.5% [20.1, 48.0] | **PASS** | exploit sweep |

## Exploit sweep vs T2_search

| policy | games | win rate [95% CI] | median rounds | illegal states |
|---|---|---|---|---|
| X_exploit_dive | 40 | 20.0 [10.5, 34.8] | 12 | 0 |
| X_exploit_farm | 40 | 30.0 [18.1, 45.4] | 11 | 0 |
| X_exploit_splitpush | 40 | 32.5 [20.1, 48.0] | 11 | 0 |
| X_exploit_objectives | 40 | 27.5 [16.1, 42.8] | 12 | 0 |
| X_exploit_turtle | 40 | 20.0 [10.5, 34.8] | 12 | 0 |
| X_exploit_cdlock | 40 | 27.5 [16.1, 42.8] | 13 | 0 |

## Abilities under 5% use in the mirror batch

| champion | ability | cost | usage |
|---|---|---|---|
| bastion | E | 1 AP | 0.0% |
| kestrel | E | 0 AP | 0.0% |
| lumen | E | 1 AP | 0.0% |
| ossuar | E | 0 AP | 0.0% |
| quillan | E | 0 AP | 0.0% |
| ashwyn | E | 0 AP | 0.1% |
| vellum | E | 0 AP | 0.1% |
| vellum | W | 2 AP | 0.1% |
| veyra | E | 0 AP | 0.1% |
| marrow | E | 0 AP | 0.2% |
| wisp | E | 0 AP | 0.2% |
| quillan | Q | 0 AP | 0.2% |
| corvane | E | 0 AP | 0.2% |
| ossuar | W | 1 AP | 0.2% |
| noctis | W | 0 AP | 0.3% |
| sable | E | 0 AP | 0.4% |
| bramblehide | Q | 1 AP | 0.4% |
| ossuar | Q | 0 AP | 0.5% |
| ashwyn | Q | 0 AP | 0.7% |
| sable | Q | 1 AP | 1.4% |
| grivven | E | 0 AP | 1.5% |
| orrin | R | 2 AP | 1.6% |
| grivven | W | 0 AP | 1.6% |
| lumen | W | 1 AP | 1.7% |
| pallas | E | 0 AP | 1.8% |
| bramblehide | E | 0 AP | 2.0% |
| vellum | Q | 1 AP | 2.0% |
| kaelis | W | 1 AP | 2.1% |
| thornjaw | W | 1 AP | 2.1% |
| vurmak | W | 0 AP | 2.3% |
| kaelis | E | 0 AP | 2.3% |
| dax | E | 1 AP | 2.3% |
| rictus | W | 1 AP | 2.4% |
| quillan | W | 2 AP | 2.7% |
| marrow | W | 1 AP | 2.7% |
| veyra | Q | 1 AP | 2.8% |
| kestrel | Q | 0 AP | 3.0% |
| pallas | Q | 0 AP | 3.2% |
| mossgrove | E | 1 AP | 3.3% |
| marrow | Q | 0 AP | 3.3% |
| pallas | W | 1 AP | 3.3% |
| brixa | W | 1 AP | 3.6% |
| sylphine | W | 1 AP | 3.7% |
| bastion | W | 1 AP | 4.1% |
| bramblehide | W | 0 AP | 4.4% |
| sylphine | E | 0 AP | 4.8% |
| vurmak | E | 0 AP | 4.9% |
