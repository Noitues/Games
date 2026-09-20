# Sim report batch_0026

## 1. Header

| field | value |
|---|---|
| rules | 1.2.0 |
| roster | 1.3.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 2601 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 479.9s |
| engine tests | not run |
| generated | 2026-09-20 22:29:57 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 6 FAIL / 19 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 48/56 abilities outside the band; roster mean 18.6%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 42.7% [35.0, 50.7] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 14.0 [13.0, 15.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 92.0% [86.5, 95.4] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, wisp (roster mean 2.20 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.7% [40.8, 56.6] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 90.5 [81.7, 95.3] | 74 | 6.61 | 3.01 | 3% | 86% | 1% | 3% | 0.24 | 0.47 | 0.9 | 0.0 | 36% | bootsx74, longbowx74, ruby_crystalx74 |
| ashwyn | 87.9 [77.1, 94.0] | 58 | 10.74 | 4.88 | 0% | 96% | 0% | 1% | 0.26 | 0.24 | 0.4 | 0.1 | 54% | bootsx58, ionian_charmx58, long_swordx58 |
| quillan | 69.0 [56.2, 79.4] | 58 | 8.18 | 3.72 | 0% | 1% | 1% | 94% | 0.21 | 0.41 | 0.8 | 2.6 | 45% | ionian_charmx58, longbowx58, ruby_crystalx58 |
| dax | 62.1 [50.1, 72.9] | 66 | 0.89 | 0.40 | 37% | 18% | 3% | 14% | 0.23 | 0.17 | 0.3 | 1.5 | 6% | long_swordx66, longbowx64, ruby_crystalx60 |
| sylphine | 57.4 [45.5, 68.4] | 68 | 0.61 | 0.28 | 19% | 2% | 14% | 25% | 0.25 | 0.09 | 0.2 | 1.4 | 4% | ruby_crystalx68, long_swordx66, vampiric_bladex63 |
| marrow | 56.8 [45.4, 67.4] | 74 | 0.62 | 0.28 | 28% | 4% | 15% | 8% | 0.20 | 0.04 | 0.1 | 1.5 | 5% | ruby_crystalx74, cloth_armorx66, long_swordx63 |
| vurmak | 55.0 [42.5, 66.9] | 60 | 1.12 | 0.51 | 41% | 12% | 1% | 19% | 0.38 | 0.08 | 0.2 | 1.8 | 9% | ruby_crystalx60, long_swordx53, cloth_armorx46 |
| pallas | 54.7 [42.6, 66.3] | 64 | 2.55 | 1.16 | 23% | 4% | 1% | 56% | 0.12 | 0.41 | 1.0 | 3.2 | 18% | ruby_crystalx64, bootsx62, longbowx62 |
| bramblehide | 53.4 [40.8, 65.7] | 58 | 2.09 | 0.95 | 2% | 39% | 1% | 40% | 0.21 | 0.12 | 0.2 | 4.9 | 16% | long_swordx58, ruby_crystalx58, vampiric_bladex56 |
| rictus | 53.3 [40.9, 65.4] | 60 | 0.72 | 0.33 | 9% | 39% | 11% | 6% | 0.32 | 0.22 | 0.5 | 1.5 | 5% | ruby_crystalx59, long_swordx54, bootsx45 |
| ossuar | 51.9 [38.9, 64.6] | 54 | 1.90 | 0.86 | 5% | 6% | 8% | 59% | 0.07 | 0.06 | 0.1 | 4.8 | 15% | ruby_crystalx54, long_swordx50, cloth_armorx43 |
| kestrel | 50.0 [36.4, 63.6] | 48 | 1.46 | 0.66 | 13% | 46% | 9% | 17% | 0.17 | 0.19 | 0.3 | 2.4 | 10% | long_swordx48, vampiric_bladex45, longbowx44 |
| brixa | 48.6 [37.2, 60.0] | 70 | 0.85 | 0.38 | 19% | 27% | 7% | 7% | 0.21 | 0.37 | 0.7 | 0.8 | 6% | long_swordx70, longbowx66, vampiric_bladex65 |
| veyra | 48.5 [36.8, 60.3] | 66 | 1.04 | 0.47 | 6% | 54% | 11% | 5% | 0.14 | 0.27 | 0.7 | 1.0 | 8% | long_swordx61, longbowx57, vampiric_bladex51 |
| bastion | 48.2 [35.7, 61.0] | 56 | 1.25 | 0.57 | 66% | 5% | 1% | 1% | 0.21 | 0.07 | 0.2 | 0.2 | 10% | ruby_crystalx56, cloth_armorx55, long_swordx54 |
| sable | 45.2 [33.4, 57.5] | 62 | 5.94 | 2.70 | 2% | 80% | 0% | 10% | 0.13 | 0.27 | 0.6 | 3.5 | 40% | longbowx62, ionian_charmx61, ruby_crystalx57 |
| thornjaw | 42.9 [30.8, 55.9] | 56 | 0.77 | 0.35 | 22% | 30% | 5% | 2% | 0.12 | 0.16 | 0.3 | 0.4 | 6% | ruby_crystalx55, long_swordx51, vampiric_bladex43 |
| grivven | 42.5 [28.5, 57.8] | 40 | 2.80 | 1.27 | 5% | 6% | 1% | 66% | 0.12 | 0.10 | 0.1 | 7.2 | 19% | longbowx40, ruby_crystalx40, bootsx37 |
| mossgrove | 41.4 [29.6, 54.2] | 58 | 0.66 | 0.30 | 32% | 21% | 2% | 12% | 0.16 | 0.12 | 0.2 | 4.3 | 6% | ruby_crystalx58, long_swordx56, vampiric_bladex47 |
| orrin | 38.0 [25.9, 51.8] | 50 | 0.50 | 0.23 | 6% | 14% | 22% | 13% | 0.02 | 0.50 | 1.1 | 2.1 | 4% | long_swordx47, longbowx38, vampiric_bladex33 |
| vellum | 36.4 [25.8, 48.4] | 66 | 1.73 | 0.79 | 7% | 2% | 23% | 52% | 0.08 | 0.53 | 1.2 | 2.5 | 16% | longbowx58, ionian_charmx51, ruby_crystalx50 |
| kaelis | 35.7 [24.5, 48.8] | 56 | 0.68 | 0.31 | 41% | 10% | 9% | 6% | 0.11 | 0.12 | 0.2 | 0.5 | 6% | ruby_crystalx56, long_swordx50, cloth_armorx47 |
| corvane | 28.3 [18.5, 40.8] | 60 | 0.18 | 0.08 | 21% | 3% | 23% | 6% | 0.18 | 0.48 | 0.9 | 4.2 | 2% | longbowx60, ruby_crystalx60, bootsx58 |
| lumen | 22.6 [14.0, 34.4] | 62 | 0.54 | 0.25 | 59% | 3% | 1% | 2% | 0.11 | 0.27 | 0.5 | 0.3 | 5% | ruby_crystalx62, longbowx61, bootsx56 |
| noctis | 12.5 [6.2, 23.6] | 56 | 0.59 | 0.27 | 29% | 13% | 15% | 8% | 0.20 | 0.54 | 1.0 | 2.5 | 7% | longbowx52, ruby_crystalx38, ionian_charmx30 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 0.94 |
| Jungle | 50.0 [44.4, 55.6] | 0.96 |
| Mid | 50.0 [44.4, 55.6] | 5.38 |
| Support | 50.0 [44.4, 55.6] | 2.70 |
| Top | 50.0 [44.4, 55.6] | 1.08 |

## 5. Games

- length: median 14.0, p10 11, p90 20
- end reasons: {'nexus': 138, 'round_limit_towers': 11, 'round_limit_hp': 1} (draws 0)
- priority win rate: 42.7% [35.0, 50.7]
- north win rate: 48.7% [40.8, 56.6]
- length histogram: {8: 2, 9: 1, 10: 8, 11: 12, 12: 20, 13: 24, 14: 16, 15: 19, 16: 14, 17: 7, 18: 5, 19: 4, 20: 18}

## 6. Objectives

- takes per game: {'dragon': 1.62, 'baron': 0.7133333333333334}
- median round taken: dragon 8, baron 12
- win rate when secured: {'dragon': 43.62139917695473, 'baron': 51.401869158878505}
- camp clears per game: {'wolves': 6.266666666666667, 'krugs': 6.5, 'red_buff': 4.086666666666667, 'raptors': 6.526666666666666, 'blue_buff': 3.986666666666667, 'dragon': 1.62, 'baron': 0.7133333333333334}

## 7. Structures

- first tower falls: median round 5.0, p10 4, p90 8
- games with at least one tower down: 100.0%
- first-tower win rate: 86.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.12 |
| chips_wave | 3.56 |
| base | 3.33 |
| chips_structure | 3.07 |
| blue_buff | 0.27 |
| red_buff | 0.13 |
| champion_kill | 0.08 |

| use | AP |
|---|---|
| shop | 10.57 |
| abilities | 2.12 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.91 | 65.5% | 1.9% | +63.5 |
| cloth_armor | 5 | 1.71 | 68.8% | 26.6% | +42.2 |
| control_ward | 2 | 1.01 | - | 50.0% | - |
| frost_charm | 2 | 0.89 | - | 50.0% | - |
| health_potion | 2 | 1.90 | - | 50.0% | - |
| ionian_charm | 8 | 1.72 | 69.7% | 6.6% | +63.1 |
| long_sword | 6 | 1.97 | 56.3% | 34.7% | +21.6 |
| longbow | 6 | 1.99 | 52.6% | 46.6% | +6.0 |
| ruby_crystal | 4 | 2.00 | 53.9% | 0.0% | +53.9 |
| stopwatch | 3 | 1.91 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.78 | 64.4% | 28.3% | +36.2 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 43.71 per game
- that is 45.7% of all ability uses


## 10. Anomalies

- ILLEGAL[activation r2]: stacking: n_kestrel and n_quillan on: 1 games
- ILLEGAL[world r2]: stacking: n_kestrel and n_quillan on: 1 games

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 10.74 AP/round = 4.88x roster mean
2. **economy outlier: quillan** - 8.18 AP/round = 3.72x roster mean
3. **champion win rate: wisp** - WR 90.5% [81.7, 95.3]
4. **anomaly: ILLEGAL[activation r2]: stacking: n_kestrel and n_quillan on** - 1 games
5. **anomaly: ILLEGAL[world r2]: stacking: n_kestrel and n_quillan on** - 1 games

## 12. Delta vs batch_0023

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +3.6 | -0.17 | no |
| bastion | -1.8 | +0.01 | no |
| bramblehide | -15.6 | +0.03 | no |
| brixa | +6.9 | -0.01 | no |
| corvane | -9.2 | +0.00 | no |
| dax | +25.4 | +0.01 | yes |
| grivven | -14.2 | -0.15 | no |
| kaelis | -3.0 | -0.00 | no |
| kestrel | -26.4 | -0.04 | yes |
| lumen | -10.2 | -0.01 | no |
| marrow | +2.3 | +0.02 | no |
| mossgrove | -10.0 | -0.01 | no |
| noctis | -2.5 | -0.10 | no |
| orrin | -11.2 | -0.16 | no |
| ossuar | -6.2 | -0.13 | no |
| pallas | +7.3 | +0.04 | no |
| quillan | +9.9 | -0.10 | no |
| rictus | +14.9 | +0.07 | no |
| sable | -18.0 | -0.36 | no |
| sylphine | +16.6 | +0.06 | no |
| thornjaw | -9.0 | -0.02 | no |
| vellum | +5.6 | -0.15 | no |
| veyra | -0.7 | +0.00 | no |
| vurmak | +5.8 | -0.01 | no |
| wisp | +13.0 | -0.39 | no |

- median length delta: -1.0
- nexus-kill rate delta: +3.3 pts
