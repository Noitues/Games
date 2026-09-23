# Sim report batch_0032

## 1. Header

| field | value |
|---|---|
| rules | 1.3.0 |
| roster | 1.4.1 |
| ai | 1.2.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 120 |
| seed | 3201 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 3259.7s |
| engine tests | 1 failed, 109 passed in 70.10s (0:01:10) |
| generated | 2026-09-23 00:38:38 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 8 FAIL / 17 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 55/59 abilities outside the band; roster mean 23.0%; 13 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 53.3% [44.4, 62.0] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 13.0 [12.0, 13.5] | **INCONCLUSIVE** |
| >=95% of games end by Nexus kill before round 20 | 92.5% [86.4, 96.0] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, wisp (roster mean 2.88 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 50.0% [41.2, 58.8] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 91.3 [79.7, 96.6] | 46 | 7.39 | 2.56 | 0% | 97% | 0% | 1% | 0.09 | 0.28 | 0.4 | 0.0 | 33% | bootsx46, cloth_armorx46, longbowx46 |
| ashwyn | 77.8 [65.1, 86.8] | 54 | 10.87 | 3.77 | 0% | 98% | 0% | 0% | 0.04 | 0.19 | 0.3 | 0.0 | 48% | bootsx54, ionian_charmx54, long_swordx54 |
| veyra | 72.4 [59.8, 82.2] | 58 | 1.74 | 0.60 | 1% | 82% | 0% | 2% | 0.26 | 0.12 | 0.3 | 0.4 | 10% | long_swordx58, longbowx58, vampiric_bladex58 |
| quillan | 70.0 [54.6, 81.9] | 40 | 8.26 | 2.86 | 0% | 1% | 0% | 96% | 0.07 | 0.30 | 0.5 | 2.5 | 39% | bootsx40, ionian_charmx40, long_swordx40 |
| bastion | 66.7 [54.1, 77.3] | 60 | 2.65 | 0.92 | 97% | 0% | 0% | 0% | 0.25 | 0.03 | 0.1 | 0.1 | 15% | cloth_armorx60, long_swordx60, ruby_crystalx60 |
| rictus | 63.0 [48.6, 75.5] | 46 | 1.22 | 0.42 | 15% | 18% | 21% | 1% | 0.17 | 0.26 | 0.4 | 1.5 | 7% | bootsx46, long_swordx46, ruby_crystalx46 |
| sable | 60.5 [44.7, 74.4] | 38 | 7.82 | 2.71 | 0% | 86% | 0% | 11% | 0.03 | 0.18 | 0.3 | 0.3 | 39% | ionian_charmx38, long_swordx38, longbowx38 |
| dax | 57.9 [42.2, 72.1] | 38 | 1.42 | 0.49 | 32% | 31% | 0% | 11% | 0.21 | 0.16 | 0.3 | 0.9 | 8% | long_swordx38, longbowx38, ruby_crystalx38 |
| vurmak | 56.5 [42.2, 69.8] | 46 | 1.71 | 0.59 | 57% | 2% | 0% | 32% | 0.24 | 0.09 | 0.2 | 2.0 | 9% | long_swordx46, ruby_crystalx46, cloth_armorx40 |
| thornjaw | 55.4 [42.4, 67.6] | 56 | 1.33 | 0.46 | 30% | 11% | 1% | 0% | 0.14 | 0.04 | 0.1 | 0.0 | 8% | long_swordx56, ruby_crystalx56, vampiric_bladex55 |
| grivven | 53.3 [40.9, 65.4] | 60 | 3.49 | 1.21 | 1% | 0% | 0% | 76% | 0.02 | 0.17 | 0.4 | 7.0 | 20% | bootsx60, longbowx60, ruby_crystalx60 |
| sylphine | 50.0 [36.4, 63.6] | 48 | 1.23 | 0.43 | 35% | 1% | 0% | 13% | 0.19 | 0.04 | 0.1 | 0.0 | 8% | long_swordx48, ruby_crystalx48, vampiric_bladex44 |
| marrow | 48.1 [35.4, 61.1] | 54 | 1.56 | 0.54 | 39% | 0% | 0% | 24% | 0.17 | 0.06 | 0.1 | 0.0 | 10% | long_swordx54, ruby_crystalx54, cloth_armorx51 |
| kestrel | 48.1 [35.1, 61.3] | 52 | 1.90 | 0.66 | 28% | 49% | 0% | 21% | 0.10 | 0.15 | 0.3 | 2.8 | 12% | long_swordx52, longbowx52, vampiric_bladex51 |
| brixa | 47.2 [32.0, 63.0] | 36 | 1.49 | 0.52 | 39% | 11% | 4% | 0% | 0.08 | 0.25 | 0.4 | 0.3 | 9% | long_swordx36, longbowx36, vampiric_bladex36 |
| ossuar | 45.8 [32.6, 59.7] | 48 | 2.80 | 0.97 | 3% | 4% | 0% | 81% | 0.10 | 0.02 | 0.0 | 4.4 | 16% | long_swordx48, ruby_crystalx48, cloth_armorx47 |
| mossgrove | 40.4 [28.2, 53.9] | 52 | 1.05 | 0.36 | 61% | 0% | 0% | 12% | 0.06 | 0.00 | 0.0 | 5.0 | 7% | long_swordx52, ruby_crystalx52, vampiric_bladex50 |
| bramblehide | 39.5 [25.6, 55.3] | 38 | 2.35 | 0.82 | 3% | 33% | 0% | 54% | 0.11 | 0.13 | 0.3 | 4.5 | 13% | bootsx38, long_swordx38, ruby_crystalx38 |
| pallas | 38.0 [25.9, 51.8] | 50 | 3.22 | 1.12 | 19% | 0% | 0% | 77% | 0.10 | 0.38 | 0.8 | 4.0 | 19% | bootsx50, longbowx50, ruby_crystalx50 |
| lumen | 36.4 [23.8, 51.1] | 44 | 0.92 | 0.32 | 83% | 0% | 0% | 0% | 0.05 | 0.02 | 0.0 | 0.0 | 6% | longbowx44, ruby_crystalx44, bootsx43 |
| corvane | 27.5 [16.1, 42.8] | 40 | 0.57 | 0.20 | 44% | 0% | 0% | 1% | 0.10 | 0.33 | 0.6 | 2.9 | 4% | bootsx40, longbowx40, ruby_crystalx40 |
| noctis | 26.0 [15.9, 39.6] | 50 | 1.56 | 0.54 | 71% | 0% | 16% | 0% | 0.06 | 0.54 | 1.2 | 0.1 | 12% | longbowx50, ionian_charmx49, ruby_crystalx49 |
| orrin | 25.0 [15.5, 37.7] | 56 | 1.74 | 0.60 | 6% | 47% | 0% | 3% | 0.14 | 0.25 | 0.4 | 0.1 | 11% | long_swordx56, longbowx55, vampiric_bladex52 |
| vellum | 24.1 [15.0, 36.5] | 58 | 2.62 | 0.91 | 3% | 0% | 1% | 82% | 0.10 | 0.36 | 0.7 | 2.9 | 18% | longbowx58, ionian_charmx55, ruby_crystalx53 |
| kaelis | 18.8 [8.9, 35.3] | 32 | 1.16 | 0.40 | 54% | 2% | 3% | 6% | 0.22 | 0.09 | 0.2 | 0.6 | 8% | cloth_armorx32, long_swordx32, ruby_crystalx32 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.69 |
| Jungle | 50.0 [43.7, 56.3] | 1.39 |
| Mid | 50.0 [43.7, 56.3] | 6.02 |
| Support | 50.0 [43.7, 56.3] | 3.22 |
| Top | 50.0 [43.7, 56.3] | 2.06 |

## 5. Games

- length: median 13.0, p10 10, p90 18
- end reasons: {'nexus': 111, 'round_limit_towers': 9} (draws 0)
- priority win rate: 53.3% [44.4, 62.0]
- north win rate: 50.0% [41.2, 58.8]
- length histogram: {8: 1, 9: 6, 10: 7, 11: 25, 12: 16, 13: 15, 14: 11, 15: 14, 16: 6, 17: 3, 18: 6, 19: 1, 20: 9}

## 6. Objectives

- takes per game: {'dragon': 1.825, 'baron': 0.8166666666666667}
- median round taken: dragon 7, baron 10.0
- win rate when secured: {'dragon': 47.945205479452056, 'baron': 50.0}
- camp clears per game: {'krugs': 6.1, 'raptors': 6.425, 'wolves': 6.066666666666666, 'red_buff': 4.0, 'dragon': 1.825, 'blue_buff': 3.966666666666667, 'baron': 0.8166666666666667}

## 7. Structures

- first tower falls: median round 5.0, p10 4, p90 6
- games with at least one tower down: 100.0%
- first-tower win rate: 80.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 5.56 |
| chips_monster | 4.38 |
| chips_wave | 4.03 |
| base | 3.38 |
| blue_buff | 0.29 |
| red_buff | 0.13 |
| champion_kill | 0.06 |

| use | AP |
|---|---|
| shop | 12.49 |
| abilities | 2.71 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.99 | 58.3% | 2.2% | +56.1 |
| cloth_armor | 5 | 1.92 | 61.0% | 30.7% | +30.3 |
| control_ward | 2 | 1.13 | - | 50.0% | - |
| frost_charm | 2 | 1.06 | - | 50.0% | - |
| health_potion | 2 | 1.97 | - | 50.0% | - |
| ionian_charm | 8 | 1.97 | 61.5% | 4.5% | +57.0 |
| long_sword | 6 | 2.00 | 51.6% | 44.4% | +7.2 |
| longbow | 6 | 2.00 | 50.1% | 49.9% | +0.2 |
| ruby_crystal | 4 | 2.00 | 51.0% | 0.0% | +51.0 |
| stopwatch | 3 | 1.92 | - | 50.0% | - |
| swift_tonic | 1 | 1.98 | - | 50.0% | - |
| vampiric_blade | 5 | 1.98 | 55.6% | 36.5% | +19.1 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 48.22 per game
- that is 44.8% of all ability uses


## 10. Anomalies

- ILLEGAL[activation r3]: stacking: n_dax and n_mossgrove on: 1 games

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 10.87 AP/round = 3.77x roster mean
2. **champion win rate: wisp** - WR 91.3% [79.7, 96.6]
3. **anomaly: ILLEGAL[activation r3]: stacking: n_dax and n_mossgrove on** - 1 games
4. **champion win rate: kaelis** - WR 18.8% [8.9, 35.3]
5. **champion win rate: ashwyn** - WR 77.8% [65.1, 86.8]

## 12. Delta vs batch_0028

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -12.7 | +0.54 | no |
| bastion | +4.9 | +0.94 | no |
| bramblehide | -23.9 | +0.28 | no |
| brixa | +15.1 | +0.15 | no |
| corvane | +2.5 | +0.06 | no |
| dax | +4.3 | +0.04 | no |
| grivven | +19.0 | +0.49 | no |
| kaelis | -14.6 | +0.08 | no |
| kestrel | -20.7 | -0.03 | no |
| lumen | -7.4 | -0.00 | no |
| marrow | +11.8 | +0.26 | no |
| mossgrove | +8.8 | +0.03 | no |
| noctis | -12.9 | -0.04 | no |
| orrin | -21.7 | +0.46 | no |
| ossuar | -22.3 | +0.27 | no |
| pallas | -17.3 | +0.41 | no |
| quillan | +20.0 | +0.42 | no |
| rictus | +16.4 | +0.05 | no |
| sable | +28.9 | +1.52 | no |
| sylphine | -3.1 | +0.08 | no |
| thornjaw | -4.6 | +0.15 | no |
| vellum | -0.9 | +0.12 | no |
| veyra | +24.8 | +0.06 | no |
| vurmak | +19.0 | +0.10 | no |
| wisp | +1.3 | +0.89 | no |

- median length delta: +3.0
- nexus-kill rate delta: -7.5 pts
