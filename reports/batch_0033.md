# Sim report batch_0033

## 1. Header

| field | value |
|---|---|
| rules | 1.4.0 |
| roster | 1.4.1 |
| ai | 1.2.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 80 |
| seed | 3301 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 2658.7s |
| engine tests | not run |
| generated | 2026-09-23 01:23:04 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 4 FAIL / 21 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 51/59 abilities outside the band; roster mean 20.6%; 11 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 46.2% [35.7, 57.1] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 15.0 [14.0, 15.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 100.0% [95.4, 100.0] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.58 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 43.8% [33.4, 54.7] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 76.3 [60.8, 87.0] | 38 | 8.59 | 3.33 | 0% | 90% | 0% | 5% | 0.13 | 0.37 | 0.6 | 0.0 | 42% | bootsx38, cloth_armorx38, ionian_charmx38 |
| wisp | 75.0 [56.6, 87.3] | 28 | 5.63 | 2.18 | 2% | 83% | 0% | 10% | 0.07 | 0.54 | 1.0 | 0.0 | 30% | bootsx28, cloth_armorx28, ionian_charmx28 |
| marrow | 64.3 [45.8, 79.3] | 28 | 2.29 | 0.89 | 8% | 1% | 0% | 35% | 0.29 | 0.11 | 0.2 | 0.0 | 12% | bootsx28, cloth_armorx28, ionian_charmx28 |
| bastion | 61.5 [42.5, 77.6] | 26 | 2.41 | 0.94 | 88% | 1% | 0% | 2% | 0.19 | 0.08 | 0.2 | 0.4 | 15% | cloth_armorx26, long_swordx26, ruby_crystalx26 |
| kestrel | 60.0 [42.3, 75.4] | 30 | 1.76 | 0.68 | 63% | 11% | 0% | 15% | 0.23 | 0.13 | 0.3 | 2.7 | 11% | bootsx30, long_swordx30, longbowx30 |
| sable | 60.0 [42.3, 75.4] | 30 | 5.97 | 2.31 | 0% | 56% | 0% | 36% | 0.13 | 0.23 | 0.4 | 1.2 | 34% | bootsx30, ionian_charmx30, long_swordx30 |
| grivven | 58.3 [42.2, 72.9] | 36 | 2.32 | 0.90 | 7% | 0% | 2% | 69% | 0.06 | 0.19 | 0.5 | 7.8 | 13% | bootsx36, longbowx36, ruby_crystalx36 |
| pallas | 56.8 [42.2, 70.3] | 44 | 3.93 | 1.52 | 6% | 0% | 0% | 88% | 0.05 | 0.73 | 1.4 | 4.5 | 22% | bootsx44, cloth_armorx44, longbowx44 |
| thornjaw | 56.8 [42.2, 70.3] | 44 | 1.47 | 0.57 | 9% | 5% | 2% | 2% | 0.23 | 0.11 | 0.2 | 0.2 | 9% | long_swordx44, ruby_crystalx44, vampiric_bladex44 |
| brixa | 56.7 [39.2, 72.6] | 30 | 1.58 | 0.61 | 44% | 3% | 5% | 1% | 0.13 | 0.27 | 0.4 | 0.5 | 9% | bootsx30, long_swordx30, longbowx30 |
| mossgrove | 56.7 [39.2, 72.6] | 30 | 1.32 | 0.51 | 32% | 0% | 1% | 7% | 0.07 | 0.03 | 0.1 | 3.3 | 8% | long_swordx30, ruby_crystalx30, vampiric_bladex30 |
| quillan | 56.2 [39.3, 71.8] | 32 | 6.79 | 2.63 | 2% | 3% | 0% | 89% | 0.09 | 0.69 | 1.3 | 2.5 | 36% | bootsx32, ionian_charmx32, long_swordx32 |
| dax | 50.0 [34.8, 65.2] | 38 | 1.53 | 0.59 | 5% | 50% | 2% | 15% | 0.18 | 0.21 | 0.3 | 1.5 | 10% | long_swordx38, longbowx38, vampiric_bladex38 |
| sylphine | 50.0 [33.6, 66.4] | 32 | 1.42 | 0.55 | 10% | 3% | 0% | 11% | 0.28 | 0.00 | 0.0 | 0.0 | 8% | bootsx32, long_swordx32, ruby_crystalx32 |
| ossuar | 47.5 [32.9, 62.5] | 40 | 2.24 | 0.87 | 8% | 4% | 0% | 56% | 0.10 | 0.15 | 0.3 | 3.8 | 13% | cloth_armorx40, long_swordx40, ruby_crystalx40 |
| rictus | 45.5 [26.9, 65.3] | 22 | 1.30 | 0.50 | 14% | 4% | 28% | 0% | 0.14 | 0.41 | 0.7 | 2.3 | 9% | long_swordx22, ruby_crystalx22, vampiric_bladex21 |
| orrin | 42.9 [26.5, 60.9] | 28 | 1.78 | 0.69 | 8% | 35% | 0% | 1% | 0.25 | 0.29 | 0.8 | 0.1 | 11% | long_swordx28, longbowx28, vampiric_bladex28 |
| veyra | 41.2 [26.4, 57.8] | 34 | 1.53 | 0.59 | 4% | 57% | 0% | 6% | 0.44 | 0.21 | 0.5 | 1.3 | 10% | long_swordx34, longbowx34, ruby_crystalx33 |
| vurmak | 41.2 [26.4, 57.8] | 34 | 1.56 | 0.61 | 18% | 2% | 0% | 54% | 0.21 | 0.32 | 0.6 | 4.2 | 10% | cloth_armorx34, long_swordx34, ruby_crystalx34 |
| kaelis | 40.6 [25.5, 57.7] | 32 | 1.28 | 0.50 | 23% | 4% | 4% | 13% | 0.09 | 0.16 | 0.4 | 1.2 | 9% | long_swordx32, ruby_crystalx32, cloth_armorx31 |
| bramblehide | 37.5 [22.9, 54.7] | 32 | 2.09 | 0.81 | 3% | 26% | 1% | 30% | 0.12 | 0.12 | 0.2 | 3.5 | 13% | bootsx32, long_swordx32, ruby_crystalx32 |
| lumen | 30.0 [14.5, 51.9] | 20 | 0.84 | 0.33 | 64% | 0% | 0% | 1% | 0.20 | 0.00 | 0.0 | 0.1 | 6% | bootsx20, cloth_armorx20, longbowx20 |
| vellum | 28.1 [15.6, 45.4] | 32 | 2.59 | 1.01 | 9% | 0% | 0% | 84% | 0.00 | 0.62 | 1.3 | 3.2 | 20% | ionian_charmx32, longbowx32, ruby_crystalx32 |
| corvane | 21.9 [11.0, 38.8] | 32 | 0.53 | 0.21 | 45% | 0% | 0% | 1% | 0.06 | 0.28 | 0.6 | 3.5 | 4% | bootsx32, longbowx32, ruby_crystalx32 |
| noctis | 21.4 [10.2, 39.5] | 28 | 1.71 | 0.66 | 77% | 0% | 14% | 0% | 0.04 | 0.43 | 0.9 | 0.0 | 13% | ionian_charmx28, longbowx28, ruby_crystalx28 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [42.3, 57.7] | 1.63 |
| Jungle | 50.0 [42.3, 57.7] | 1.53 |
| Mid | 50.0 [42.3, 57.7] | 5.33 |
| Support | 50.0 [42.3, 57.7] | 2.80 |
| Top | 50.0 [42.3, 57.7] | 1.94 |

## 5. Games

- length: median 15.0, p10 13, p90 17
- end reasons: {'nexus': 80} (draws 0)
- priority win rate: 46.2% [35.7, 57.1]
- north win rate: 43.8% [33.4, 54.7]
- length histogram: {11: 2, 12: 2, 13: 11, 14: 17, 15: 20, 16: 16, 17: 5, 18: 4, 19: 3}

## 6. Objectives

- takes per game: {'dragon': 2.0, 'baron': 0.925}
- median round taken: dragon 9.0, baron 10.0
- win rate when secured: {'dragon': 40.0, 'baron': 54.054054054054056}
- camp clears per game: {'blue_buff': 4.175, 'krugs': 6.425, 'wolves': 6.5625, 'raptors': 6.9375, 'dragon': 2.0, 'red_buff': 4.2, 'baron': 0.925}

## 7. Structures

- first tower falls: median round 6.0, p10 4, p90 7
- games with at least one tower down: 100.0%
- first-tower win rate: 66.2%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 5.11 |
| chips_monster | 4.21 |
| chips_wave | 3.72 |
| base | 3.43 |
| blue_buff | 0.27 |
| red_buff | 0.15 |
| champion_kill | 0.09 |

| use | AP |
|---|---|
| shop | 11.97 |
| abilities | 2.60 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 54.5% | 4.2% | +50.4 |
| cloth_armor | 5 | 1.99 | 56.8% | 34.8% | +22.0 |
| control_ward | 2 | 1.34 | - | 50.0% | - |
| frost_charm | 2 | 1.23 | - | 50.0% | - |
| health_potion | 2 | 1.99 | - | 50.0% | - |
| ionian_charm | 8 | 2.00 | 57.0% | 2.9% | +54.0 |
| long_sword | 6 | 2.00 | 50.6% | 47.9% | +2.6 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 50.3% | 0.0% | +50.3 |
| stopwatch | 3 | 1.94 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 53.5% | 40.1% | +13.4 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 66.17 per game
- that is 56.0% of all ability uses
- activations ending on a hexgroup edge: 98.3%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 8.59 AP/round = 3.33x roster mean
2. **champion win rate: noctis** - WR 21.4% [10.2, 39.5]
3. **champion win rate: corvane** - WR 21.9% [11.0, 38.8]
4. **champion win rate: ashwyn** - WR 76.3% [60.8, 87.0]
5. **champion win rate: wisp** - WR 75.0% [56.6, 87.3]

## 12. Delta vs batch_0032

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -1.5 | -2.28 | no |
| bastion | -5.1 | -0.23 | no |
| bramblehide | -2.0 | -0.26 | no |
| brixa | +9.4 | +0.09 | no |
| corvane | -5.6 | -0.04 | no |
| dax | -7.9 | +0.11 | no |
| grivven | +5.0 | -1.17 | no |
| kaelis | +21.9 | +0.12 | no |
| kestrel | +11.9 | -0.14 | no |
| lumen | -6.4 | -0.07 | no |
| marrow | +16.1 | +0.73 | no |
| mossgrove | +16.3 | +0.27 | no |
| noctis | -4.6 | +0.15 | no |
| orrin | +17.9 | +0.04 | no |
| ossuar | +1.7 | -0.55 | no |
| pallas | +18.8 | +0.71 | no |
| quillan | -13.8 | -1.47 | no |
| rictus | -17.6 | +0.07 | no |
| sable | -0.5 | -1.86 | no |
| sylphine | +0.0 | +0.20 | no |
| thornjaw | +1.5 | +0.14 | no |
| vellum | +4.0 | -0.02 | no |
| veyra | -31.2 | -0.21 | no |
| vurmak | -15.3 | -0.15 | no |
| wisp | -16.3 | -1.76 | no |

- median length delta: +2.0
- nexus-kill rate delta: +7.5 pts
