# Sim report batch_0043

## 1. Header

| field | value |
|---|---|
| rules | 1.7.0 |
| roster | 1.6.0 |
| ai | 1.4.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 160 |
| seed | 4301 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 4019.7s |
| engine tests | not run |
| generated | 2026-09-24 04:07:38 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 5 FAIL / 20 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 19.7%; 9 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 60.0% [52.3, 67.3] | **FAIL** |
| Median game length 13-18 rounds | 15.0 [14.0, 15.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 100.0% [97.7, 100.0] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.16 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 43.8% [36.3, 51.5] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bastion | 78.0 [64.8, 87.2] | 50 | 2.41 | 1.12 | 93% | 0% | 0% | 0% | 0.24 | 0.22 | 0.7 | 0.0 | 15% | cloth_armorx50, long_swordx50, ruby_crystalx50 |
| wisp | 73.3 [61.0, 82.9] | 60 | 4.87 | 2.26 | 3% | 82% | 1% | 7% | 0.15 | 0.63 | 1.7 | 0.0 | 28% | bootsx60, cloth_armorx60, longbowx60 |
| veyra | 71.0 [58.7, 80.8] | 62 | 1.42 | 0.66 | 2% | 67% | 0% | 9% | 0.27 | 0.50 | 1.3 | 1.6 | 10% | long_swordx62, longbowx62, vampiric_bladex62 |
| grivven | 59.4 [47.1, 70.5] | 64 | 2.31 | 1.07 | 6% | 1% | 1% | 68% | 0.12 | 0.41 | 1.2 | 7.3 | 16% | bootsx64, longbowx64, ruby_crystalx64 |
| bramblehide | 57.6 [45.6, 68.8] | 66 | 1.72 | 0.80 | 4% | 30% | 0% | 20% | 0.14 | 0.35 | 1.0 | 3.1 | 11% | long_swordx66, ruby_crystalx66, vampiric_bladex66 |
| kestrel | 57.4 [45.5, 68.4] | 68 | 1.67 | 0.77 | 52% | 16% | 0% | 20% | 0.25 | 0.37 | 1.1 | 3.5 | 11% | long_swordx68, longbowx68, ruby_crystalx66 |
| ashwyn | 55.6 [44.1, 66.5] | 72 | 4.51 | 2.09 | 2% | 64% | 0% | 24% | 0.17 | 0.89 | 2.4 | 0.0 | 30% | ionian_charmx72, longbowx72, ruby_crystalx72 |
| sable | 55.1 [44.1, 65.7] | 78 | 5.51 | 2.55 | 4% | 51% | 0% | 37% | 0.22 | 0.26 | 0.7 | 1.3 | 33% | ionian_charmx78, longbowx78, long_swordx77 |
| pallas | 54.4 [42.7, 65.7] | 68 | 3.68 | 1.71 | 6% | 0% | 1% | 86% | 0.12 | 0.56 | 1.5 | 4.7 | 23% | bootsx68, longbowx68, ruby_crystalx68 |
| thornjaw | 54.3 [40.2, 67.8] | 46 | 1.36 | 0.63 | 14% | 8% | 2% | 3% | 0.24 | 0.48 | 1.3 | 0.1 | 9% | long_swordx46, ruby_crystalx46, vampiric_bladex46 |
| quillan | 54.3 [42.7, 65.4] | 70 | 4.66 | 2.16 | 8% | 8% | 0% | 74% | 0.29 | 0.64 | 1.8 | 0.0 | 30% | ionian_charmx70, long_swordx70, longbowx70 |
| rictus | 53.7 [40.6, 66.3] | 54 | 1.11 | 0.51 | 14% | 6% | 30% | 1% | 0.19 | 0.74 | 1.9 | 2.5 | 7% | long_swordx54, ruby_crystalx54, vampiric_bladex52 |
| vurmak | 51.5 [39.8, 62.9] | 68 | 1.38 | 0.64 | 15% | 2% | 2% | 62% | 0.35 | 0.62 | 1.8 | 4.3 | 9% | long_swordx68, ruby_crystalx68, cloth_armorx67 |
| kaelis | 46.9 [35.2, 58.9] | 64 | 1.23 | 0.57 | 21% | 5% | 2% | 19% | 0.19 | 0.50 | 1.3 | 1.8 | 9% | cloth_armorx64, long_swordx64, ruby_crystalx64 |
| mossgrove | 45.2 [35.0, 55.9] | 84 | 1.15 | 0.53 | 32% | 1% | 0% | 10% | 0.21 | 0.46 | 1.3 | 3.9 | 8% | long_swordx84, ruby_crystalx84, vampiric_bladex83 |
| sylphine | 42.9 [31.9, 54.5] | 70 | 1.36 | 0.63 | 13% | 2% | 0% | 15% | 0.23 | 0.31 | 0.8 | 0.0 | 9% | long_swordx70, ruby_crystalx70, vampiric_bladex68 |
| orrin | 42.4 [31.2, 54.4] | 66 | 1.60 | 0.74 | 8% | 30% | 1% | 1% | 0.32 | 0.44 | 1.3 | 0.1 | 11% | long_swordx66, longbowx66, vampiric_bladex65 |
| brixa | 42.2 [30.9, 54.4] | 64 | 1.37 | 0.63 | 40% | 6% | 6% | 2% | 0.30 | 0.69 | 1.7 | 0.6 | 10% | long_swordx64, longbowx64, vampiric_bladex64 |
| vellum | 41.4 [29.6, 54.2] | 58 | 2.41 | 1.12 | 2% | 0% | 3% | 79% | 0.36 | 0.66 | 2.0 | 3.2 | 18% | longbowx58, ionian_charmx57, ruby_crystalx57 |
| ossuar | 40.6 [29.5, 52.9] | 64 | 1.99 | 0.93 | 8% | 5% | 0% | 50% | 0.14 | 0.14 | 0.4 | 4.2 | 14% | ruby_crystalx64, cloth_armorx63, long_swordx63 |
| marrow | 40.5 [30.1, 51.9] | 74 | 2.15 | 1.00 | 9% | 1% | 1% | 37% | 0.23 | 0.34 | 1.0 | 0.1 | 15% | long_swordx74, ruby_crystalx74, cloth_armorx73 |
| dax | 36.7 [25.6, 49.3] | 60 | 1.31 | 0.61 | 10% | 38% | 3% | 15% | 0.28 | 0.43 | 1.2 | 1.8 | 9% | long_swordx60, longbowx60, vampiric_bladex60 |
| noctis | 35.7 [23.0, 50.8] | 42 | 1.50 | 0.69 | 71% | 0% | 19% | 1% | 0.21 | 0.60 | 1.6 | 0.1 | 12% | ionian_charmx42, longbowx42, ruby_crystalx40 |
| lumen | 33.3 [23.5, 44.8] | 72 | 0.79 | 0.37 | 68% | 1% | 0% | 2% | 0.06 | 0.49 | 1.4 | 0.2 | 6% | longbowx72, ruby_crystalx72, bootsx71 |
| corvane | 30.4 [19.9, 43.3] | 56 | 0.47 | 0.22 | 44% | 0% | 1% | 4% | 0.21 | 0.64 | 1.9 | 3.8 | 4% | bootsx56, longbowx56, ruby_crystalx56 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.6, 55.4] | 1.48 |
| Jungle | 50.0 [44.6, 55.4] | 1.33 |
| Mid | 50.0 [44.6, 55.4] | 4.01 |
| Support | 50.0 [44.6, 55.4] | 2.41 |
| Top | 50.0 [44.6, 55.4] | 1.81 |

## 5. Games

- length: median 15.0, p10 12, p90 17
- end reasons: {'nexus': 160} (draws 0)
- priority win rate: 60.0% [52.3, 67.3]
- north win rate: 43.8% [36.3, 51.5]
- length histogram: {10: 1, 11: 4, 12: 14, 13: 23, 14: 33, 15: 37, 16: 24, 17: 17, 18: 5, 19: 2}

## 6. Objectives

- takes per game: {'dragon': 1.4125, 'baron': 0.49375}
- median round taken: dragon 8.0, baron 13
- win rate when secured: {'dragon': 47.78761061946903, 'baron': 43.037974683544306}
- camp clears per game: {'wolves': 5.5625, 'raptors': 5.73125, 'krugs': 5.48125, 'blue_buff': 3.30625, 'red_buff': 3.23125, 'dragon': 1.4125, 'baron': 0.49375}

## 7. Structures

- first tower falls: median round 7.0, p10 5, p90 9
- games with at least one tower down: 100.0%
- first-tower win rate: 71.2%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 4.46 |
| chips_monster | 3.55 |
| base | 3.30 |
| chips_wave | 2.81 |
| champion_kill | 0.47 |
| blue_buff | 0.22 |
| red_buff | 0.16 |

| use | AP |
|---|---|
| shop | 11.47 |
| abilities | 2.42 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.99 | 54.4% | 22.1% | +32.3 |
| cloth_armor | 5 | 1.98 | 55.8% | 40.3% | +15.5 |
| control_ward | 2 | 0.76 | - | 50.0% | - |
| frost_charm | 2 | 0.64 | - | 50.0% | - |
| health_potion | 2 | 1.96 | - | 50.0% | - |
| ionian_charm | 8 | 1.99 | 55.8% | 26.6% | +29.2 |
| long_sword | 6 | 2.00 | 50.7% | 47.5% | +3.2 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 50.4% | 12.5% | +37.9 |
| stopwatch | 3 | 1.91 | - | 50.0% | - |
| swift_tonic | 1 | 1.98 | - | 50.0% | - |
| vampiric_blade | 5 | 1.98 | 52.8% | 43.1% | +9.7 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 160 | 51.2 [43.6, 58.9] |
| SM_g2_lane6 | 92 | 51.1 [41.0, 61.1] |
| SM_g2_clock3_short | 68 | 45.6 [34.3, 57.3] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] | vs T2_sieger | state occupancy | switches/game |
|---|---|---|---|---|---|
| T2_sieger | 160 | 51.2 [43.6, 58.9] | - | - | - |
| SM_g2_lane6 | 92 | 51.1 [41.0, 61.1] | 51% (92) | sieger 66%, laner 34% | 1.0 |
| SM_g2_clock3_short | 68 | 45.6 [34.3, 57.3] | 46% (68) | sieger 59%, laner 27%, objective 14% | 2.0 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 43.21 per game
- that is 39.7% of all ability uses
- of which true snipes (from cover, two or more hexes away): 36.5% of all uses
- snipes aimed at a champion: 7.3 per game
- activations ending beside an enemy-held hexgroup (looking in): 68.9%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **champion win rate: bastion** - WR 78.0% [64.8, 87.2]
2. **Priority (first player) win rate 48-52%** - 60.0% [52.3, 67.3]
3. **champion win rate: wisp** - WR 73.3% [61.0, 82.9]
4. **economy outlier: sable** - 5.51 AP/round = 2.55x roster mean
5. **champion win rate: veyra** - WR 71.0% [58.7, 80.8]
