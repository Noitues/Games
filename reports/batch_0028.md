# Sim report batch_0028

## 1. Header

| field | value |
|---|---|
| rules | 1.2.0 |
| roster | 1.3.0 |
| ai | 1.2.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 80 |
| seed | 2801 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 1159.3s |
| engine tests | not run |
| generated | 2026-09-20 23:09:06 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 4 FAIL / 21 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 53/56 abilities outside the band; roster mean 19.9%; 12 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 53.8% [42.9, 64.3] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 10.0 [10.0, 11.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 100.0% [95.4, 100.0] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, wisp (roster mean 2.59 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 46.2% [35.7, 57.1] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 90.5 [77.9, 96.2] | 42 | 10.34 | 3.99 | 0% | 98% | 0% | 1% | 0.05 | 0.19 | 0.2 | 0.0 | 47% | bootsx42, ionian_charmx42, long_swordx42 |
| wisp | 90.0 [74.4, 96.5] | 30 | 6.51 | 2.51 | 0% | 93% | 0% | 4% | 0.03 | 0.27 | 0.3 | 0.0 | 30% | bootsx30, cloth_armorx30, longbowx30 |
| kestrel | 68.8 [51.4, 82.0] | 32 | 1.93 | 0.75 | 25% | 45% | 0% | 29% | 0.03 | 0.12 | 0.2 | 2.7 | 11% | long_swordx32, longbowx32, vampiric_bladex32 |
| ossuar | 68.2 [53.4, 80.0] | 44 | 2.53 | 0.98 | 3% | 6% | 0% | 79% | 0.07 | 0.00 | 0.0 | 4.1 | 14% | long_swordx44, ruby_crystalx44, cloth_armorx43 |
| bramblehide | 63.3 [45.5, 78.1] | 30 | 2.08 | 0.80 | 0% | 43% | 0% | 44% | 0.07 | 0.03 | 0.0 | 4.0 | 13% | long_swordx30, ruby_crystalx30, vampiric_bladex28 |
| bastion | 61.8 [45.0, 76.1] | 34 | 1.70 | 0.66 | 87% | 0% | 0% | 2% | 0.12 | 0.03 | 0.1 | 0.2 | 10% | long_swordx34, ruby_crystalx34, cloth_armorx33 |
| thornjaw | 60.0 [42.3, 75.4] | 30 | 1.18 | 0.46 | 36% | 12% | 1% | 0% | 0.30 | 0.13 | 0.2 | 0.1 | 7% | long_swordx30, ruby_crystalx30, vampiric_bladex27 |
| pallas | 55.3 [39.7, 69.9] | 38 | 2.81 | 1.08 | 25% | 0% | 0% | 70% | 0.05 | 0.13 | 0.2 | 3.6 | 17% | longbowx38, ruby_crystalx38, bootsx34 |
| dax | 53.6 [35.8, 70.5] | 28 | 1.38 | 0.53 | 28% | 37% | 0% | 9% | 0.14 | 0.14 | 0.3 | 0.8 | 9% | long_swordx28, longbowx28, vampiric_bladex26 |
| sylphine | 53.1 [36.4, 69.1] | 32 | 1.14 | 0.44 | 32% | 2% | 0% | 19% | 0.25 | 0.03 | 0.0 | 0.0 | 6% | long_swordx32, ruby_crystalx31, bootsx29 |
| quillan | 50.0 [33.2, 66.8] | 30 | 7.84 | 3.03 | 0% | 0% | 0% | 98% | 0.10 | 0.30 | 0.5 | 2.5 | 43% | ionian_charmx30, longbowx30, ruby_crystalx30 |
| veyra | 47.6 [33.4, 62.3] | 42 | 1.68 | 0.65 | 0% | 82% | 0% | 4% | 0.17 | 0.14 | 0.2 | 0.7 | 11% | long_swordx42, longbowx40, vampiric_bladex36 |
| orrin | 46.7 [30.2, 63.9] | 30 | 1.28 | 0.50 | 8% | 50% | 0% | 3% | 0.10 | 0.10 | 0.2 | 3.4 | 7% | long_swordx30, longbowx30, ruby_crystalx30 |
| rictus | 46.7 [30.2, 63.9] | 30 | 1.17 | 0.45 | 14% | 24% | 18% | 1% | 0.27 | 0.10 | 0.1 | 1.4 | 7% | long_swordx30, ruby_crystalx30, vampiric_bladex27 |
| lumen | 43.8 [28.2, 60.7] | 32 | 0.92 | 0.36 | 78% | 0% | 0% | 0% | 0.00 | 0.03 | 0.1 | 0.0 | 6% | longbowx32, ruby_crystalx32, bootsx30 |
| noctis | 38.9 [20.3, 61.4] | 18 | 1.60 | 0.62 | 72% | 0% | 18% | 2% | 0.17 | 0.33 | 0.6 | 0.3 | 13% | longbowx18, ionian_charmx16, ruby_crystalx15 |
| vurmak | 37.5 [21.2, 57.3] | 24 | 1.61 | 0.62 | 63% | 1% | 0% | 20% | 0.17 | 0.12 | 0.3 | 1.6 | 10% | ruby_crystalx24, long_swordx23, cloth_armorx19 |
| marrow | 36.4 [19.7, 57.0] | 22 | 1.30 | 0.50 | 48% | 0% | 0% | 23% | 0.18 | 0.05 | 0.0 | 0.0 | 9% | long_swordx22, ruby_crystalx22, cloth_armorx19 |
| grivven | 34.4 [20.4, 51.7] | 32 | 3.00 | 1.16 | 2% | 0% | 0% | 76% | 0.00 | 0.12 | 0.2 | 5.7 | 18% | longbowx32, ruby_crystalx32, bootsx31 |
| kaelis | 33.3 [20.2, 49.7] | 36 | 1.08 | 0.42 | 61% | 1% | 2% | 7% | 0.14 | 0.08 | 0.1 | 0.6 | 7% | ruby_crystalx36, long_swordx35, cloth_armorx32 |
| brixa | 32.1 [17.9, 50.7] | 28 | 1.34 | 0.52 | 29% | 16% | 3% | 2% | 0.14 | 0.21 | 0.3 | 0.2 | 9% | long_swordx28, longbowx28, vampiric_bladex24 |
| mossgrove | 31.6 [19.1, 47.5] | 38 | 1.02 | 0.39 | 63% | 0% | 0% | 11% | 0.05 | 0.00 | 0.0 | 4.7 | 7% | long_swordx38, ruby_crystalx38, vampiric_bladex36 |
| sable | 31.6 [19.1, 47.5] | 38 | 6.31 | 2.43 | 0% | 90% | 0% | 8% | 0.05 | 0.18 | 0.3 | 2.9 | 38% | ionian_charmx38, longbowx38, ruby_crystalx35 |
| corvane | 25.0 [12.7, 43.4] | 28 | 0.51 | 0.20 | 38% | 0% | 0% | 1% | 0.04 | 0.21 | 0.2 | 2.6 | 4% | longbowx28, ruby_crystalx27, bootsx25 |
| vellum | 25.0 [13.3, 42.1] | 32 | 2.49 | 0.96 | 2% | 0% | 0% | 86% | 0.00 | 0.34 | 0.7 | 3.4 | 20% | longbowx32, ionian_charmx30, ruby_crystalx20 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [42.3, 57.7] | 1.54 |
| Jungle | 50.0 [42.3, 57.7] | 1.30 |
| Mid | 50.0 [42.3, 57.7] | 6.36 |
| Support | 50.0 [42.3, 57.7] | 2.76 |
| Top | 50.0 [42.3, 57.7] | 1.72 |

## 5. Games

- length: median 10.0, p10 8, p90 14
- end reasons: {'nexus': 80} (draws 0)
- priority win rate: 53.8% [42.9, 64.3]
- north win rate: 46.2% [35.7, 57.1]
- length histogram: {7: 2, 8: 8, 9: 15, 10: 18, 11: 13, 12: 10, 13: 5, 14: 3, 15: 4, 17: 1, 19: 1}

## 6. Objectives

- takes per game: {'dragon': 1.2875, 'baron': 0.4625}
- median round taken: dragon 6, baron 10
- win rate when secured: {'dragon': 39.80582524271845, 'baron': 48.648648648648646}
- camp clears per game: {'krugs': 5.0625, 'wolves': 4.925, 'raptors': 5.2375, 'blue_buff': 3.2125, 'red_buff': 3.2, 'dragon': 1.2875, 'baron': 0.4625}

## 7. Structures

- first tower falls: median round 3.0, p10 3, p90 4
- games with at least one tower down: 100.0%
- first-tower win rate: 71.2%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 5.05 |
| chips_monster | 4.44 |
| chips_wave | 3.80 |
| base | 3.26 |
| blue_buff | 0.28 |
| red_buff | 0.14 |
| champion_kill | 0.06 |

| use | AP |
|---|---|
| shop | 13.34 |
| abilities | 2.17 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.88 | 64.2% | 14.8% | +49.4 |
| cloth_armor | 5 | 1.82 | 65.7% | 33.4% | +32.3 |
| control_ward | 2 | 0.55 | - | 50.0% | - |
| frost_charm | 2 | 0.35 | - | 50.0% | - |
| health_potion | 2 | 1.88 | - | 50.0% | - |
| ionian_charm | 8 | 1.95 | 66.4% | 18.1% | +48.3 |
| long_sword | 6 | 2.00 | 52.4% | 42.6% | +9.8 |
| longbow | 6 | 2.00 | 50.2% | 49.7% | +0.5 |
| ruby_crystal | 4 | 2.00 | 52.9% | 2.2% | +50.7 |
| stopwatch | 3 | 1.71 | - | 50.0% | - |
| swift_tonic | 1 | 1.86 | - | 50.0% | - |
| vampiric_blade | 5 | 1.88 | 58.7% | 36.0% | +22.7 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 39.51 per game
- that is 48.9% of all ability uses


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 10.34 AP/round = 3.99x roster mean
2. **champion win rate: ashwyn** - WR 90.5% [77.9, 96.2]
3. **champion win rate: wisp** - WR 90.0% [74.4, 96.5]
4. **economy outlier: quillan** - 7.84 AP/round = 3.03x roster mean
5. **champion win rate: corvane** - WR 25.0% [12.7, 43.4]

## 12. Delta vs batch_0026

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +2.5 | -0.40 | no |
| bastion | +13.6 | +0.45 | no |
| bramblehide | +9.9 | -0.01 | no |
| brixa | -16.4 | +0.49 | no |
| corvane | -3.3 | +0.33 | no |
| dax | -8.5 | +0.49 | no |
| grivven | -8.1 | +0.19 | no |
| kaelis | -2.4 | +0.41 | no |
| kestrel | +18.8 | +0.48 | no |
| lumen | +21.2 | +0.38 | no |
| marrow | -20.4 | +0.68 | no |
| mossgrove | -9.8 | +0.37 | no |
| noctis | +26.4 | +1.02 | no |
| orrin | +8.7 | +0.78 | no |
| ossuar | +16.3 | +0.63 | no |
| pallas | +0.6 | +0.26 | no |
| quillan | -19.0 | -0.34 | no |
| rictus | -6.7 | +0.46 | no |
| sable | -13.6 | +0.37 | no |
| sylphine | -4.2 | +0.53 | no |
| thornjaw | +17.1 | +0.41 | no |
| vellum | -11.4 | +0.77 | no |
| veyra | -0.9 | +0.64 | no |
| vurmak | -17.5 | +0.49 | no |
| wisp | -0.5 | -0.11 | no |

- median length delta: -4.0
- nexus-kill rate delta: +8.0 pts
