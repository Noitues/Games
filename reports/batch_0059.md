# Sim report batch_0059

## 1. Header

| field | value |
|---|---|
| rules | 1.8.0 |
| roster | 1.8.0 |
| ai | 1.5.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 1600 |
| seed | 5901 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 0.9s |
| engine tests | not run |
| generated | 2026-09-27 18:03:52 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 2 FAIL / 18 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 50/58 abilities outside the band; roster mean 14.3%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 50.2% [47.8, 52.7] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 13.0 [12.0, 13.0] | **INCONCLUSIVE** |
| >=95% of games end by Nexus kill before round 20 | 100.0% [99.8, 100.0] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, vellum (roster mean 1.14 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 46.1% [43.7, 48.6] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 59.5 [55.6, 63.2] | 624 | 1.50 | 1.31 | 8% | 63% | 1% | 3% | 0.10 | 0.60 | 1.5 | 4.1 | 15% | longbowx622, ruby_crystalx602, bootsx432 |
| pallas | 56.4 [52.6, 60.2] | 654 | 1.36 | 1.19 | 7% | 1% | 2% | 70% | 0.10 | 0.50 | 1.3 | 4.5 | 13% | longbowx654, ruby_crystalx652, bootsx562 |
| sable | 54.5 [50.5, 58.4] | 600 | 2.09 | 1.82 | 4% | 41% | 0% | 38% | 0.13 | 0.25 | 0.7 | 3.7 | 20% | longbowx597, ionian_charmx529, ruby_crystalx451 |
| veyra | 54.4 [50.5, 58.2] | 638 | 1.08 | 0.94 | 1% | 61% | 0% | 1% | 0.30 | 0.48 | 1.3 | 0.3 | 10% | long_swordx638, longbowx607, vampiric_bladex471 |
| bastion | 53.2 [49.4, 57.0] | 658 | 1.14 | 1.00 | 52% | 1% | 0% | 7% | 0.14 | 0.20 | 0.6 | 1.4 | 11% | ruby_crystalx658, long_swordx649, cloth_armorx596 |
| bramblehide | 53.0 [49.1, 56.9] | 628 | 1.18 | 1.03 | 1% | 13% | 1% | 24% | 0.14 | 0.32 | 0.9 | 2.9 | 11% | long_swordx628, ruby_crystalx626, vampiric_bladex547 |
| kaelis | 52.7 [48.7, 56.6] | 598 | 0.59 | 0.52 | 25% | 3% | 6% | 5% | 0.19 | 0.31 | 0.8 | 0.5 | 6% | ruby_crystalx598, long_swordx565, cloth_armorx457 |
| thornjaw | 52.6 [48.8, 56.5] | 646 | 0.73 | 0.64 | 14% | 4% | 1% | 2% | 0.17 | 0.35 | 1.0 | 0.1 | 7% | long_swordx646, ruby_crystalx630, vampiric_bladex436 |
| ossuar | 52.3 [48.3, 56.2] | 620 | 1.62 | 1.41 | 36% | 1% | 0% | 36% | 0.18 | 0.16 | 0.5 | 3.0 | 15% | ruby_crystalx620, long_swordx599, cloth_armorx505 |
| kestrel | 51.5 [47.7, 55.3] | 664 | 1.31 | 1.14 | 56% | 7% | 1% | 7% | 0.33 | 0.28 | 0.8 | 1.2 | 13% | long_swordx664, longbowx650, vampiric_bladex566 |
| noctis | 51.1 [47.2, 55.0] | 624 | 1.23 | 1.07 | 71% | 0% | 11% | 2% | 0.38 | 0.41 | 1.0 | 0.2 | 13% | longbowx624, ionian_charmx578, ruby_crystalx500 |
| quillan | 50.8 [47.0, 54.6] | 660 | 1.90 | 1.66 | 9% | 9% | 1% | 61% | 0.12 | 0.59 | 1.5 | 2.8 | 19% | longbowx660, ionian_charmx580, ruby_crystalx496 |
| sylphine | 49.8 [45.9, 53.7] | 628 | 0.72 | 0.63 | 13% | 3% | 0% | 10% | 0.18 | 0.28 | 0.8 | 0.0 | 7% | long_swordx624, ruby_crystalx615, vampiric_bladex407 |
| vurmak | 49.6 [45.8, 53.3] | 680 | 0.95 | 0.83 | 23% | 5% | 1% | 24% | 0.35 | 0.21 | 0.6 | 2.3 | 10% | ruby_crystalx679, long_swordx603, cloth_armorx408 |
| brixa | 49.2 [45.4, 53.1] | 650 | 0.81 | 0.70 | 20% | 3% | 6% | 1% | 0.22 | 0.49 | 1.4 | 0.6 | 8% | long_swordx650, longbowx637, vampiric_bladex569 |
| rictus | 49.2 [45.3, 53.1] | 620 | 0.72 | 0.63 | 13% | 3% | 19% | 2% | 0.25 | 0.63 | 1.7 | 1.8 | 7% | long_swordx620, ruby_crystalx609, vampiric_bladex441 |
| vellum | 48.8 [45.0, 52.6] | 652 | 1.80 | 1.57 | 3% | 0% | 3% | 66% | 0.25 | 0.44 | 1.3 | 3.1 | 18% | longbowx646, ionian_charmx552, ruby_crystalx468 |
| orrin | 48.0 [44.2, 51.8] | 654 | 0.86 | 0.75 | 4% | 16% | 1% | 0% | 0.20 | 0.58 | 1.6 | 0.0 | 8% | long_swordx653, longbowx618, vampiric_bladex458 |
| corvane | 48.0 [44.1, 51.8] | 640 | 0.44 | 0.39 | 52% | 0% | 0% | 3% | 0.32 | 0.44 | 1.2 | 0.6 | 5% | longbowx640, ruby_crystalx637, bootsx571 |
| dax | 46.6 [42.7, 50.7] | 594 | 0.92 | 0.80 | 13% | 25% | 3% | 3% | 0.23 | 0.44 | 1.2 | 0.6 | 9% | long_swordx594, longbowx579, vampiric_bladex494 |
| grivven | 46.4 [42.6, 50.3] | 640 | 1.03 | 0.90 | 5% | 3% | 4% | 37% | 0.08 | 0.36 | 1.0 | 5.0 | 10% | longbowx640, ruby_crystalx640, bootsx559 |
| mossgrove | 45.6 [41.9, 49.3] | 678 | 0.77 | 0.68 | 22% | 1% | 1% | 4% | 0.18 | 0.28 | 0.8 | 2.6 | 8% | long_swordx678, ruby_crystalx671, vampiric_bladex508 |
| ashwyn | 45.3 [41.6, 49.1] | 664 | 1.94 | 1.69 | 5% | 56% | 0% | 21% | 0.21 | 0.67 | 1.7 | 2.1 | 19% | longbowx664, ionian_charmx646, ruby_crystalx613 |
| marrow | 42.5 [38.8, 46.4] | 644 | 1.39 | 1.21 | 7% | 1% | 0% | 45% | 0.10 | 0.21 | 0.6 | 3.6 | 13% | ruby_crystalx644, long_swordx622, cloth_armorx511 |
| lumen | 39.9 [36.2, 43.7] | 642 | 0.55 | 0.48 | 47% | 0% | 0% | 1% | 0.20 | 0.25 | 0.6 | 0.1 | 6% | longbowx642, ruby_crystalx634, bootsx523 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [48.3, 51.7] | 1.00 |
| Jungle | 50.0 [48.3, 51.7] | 0.82 |
| Mid | 50.0 [48.3, 51.7] | 1.79 |
| Support | 50.0 [48.3, 51.7] | 0.98 |
| Top | 50.0 [48.3, 51.7] | 1.14 |

## 5. Games

- length: median 13.0, p10 9, p90 16
- end reasons: {'nexus': 1600} (draws 0)
- priority win rate: 50.2% [47.8, 52.7]
- north win rate: 46.1% [43.7, 48.6]
- length histogram: {5: 1, 6: 10, 7: 31, 8: 55, 9: 100, 10: 177, 11: 203, 12: 211, 13: 222, 14: 182, 15: 169, 16: 112, 17: 70, 18: 40, 19: 15, 20: 2}

## 6. Objectives

- takes per game: {'dragon': 1.37125, 'baron': 0.409375}
- median round taken: dragon 6.0, baron 12
- win rate when secured: {'dragon': 44.12032816773017, 'baron': 34.19847328244275}
- camp clears per game: {'raptors': 4.665625, 'krugs': 4.3825, 'red_buff': 2.385625, 'wolves': 4.589375, 'dragon': 1.37125, 'blue_buff': 2.5225, 'baron': 0.409375}

## 7. Structures

- first tower falls: median round 4.0, p10 3, p90 7
- games with at least one tower down: 100.0%
- first-tower win rate: 66.1%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.32 |
| base | 3.00 |
| chips_wave | 2.19 |
| tower_kill | 0.71 |
| champion_kill | 0.44 |
| blue_buff | 0.20 |
| dragon | 0.18 |
| red_buff | 0.10 |

| use | AP |
|---|---|
| shop | 8.16 |
| abilities | 1.56 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.65 | 46.6% | 51.9% | -5.3 |
| cloth_armor | 5 | 1.55 | 46.4% | 51.2% | -4.8 |
| control_ward | 2 | 0.03 | - | 50.0% | - |
| frost_charm | 2 | 0.01 | - | 50.0% | - |
| health_potion | 2 | 1.85 | - | 50.0% | - |
| ionian_charm | 8 | 1.80 | 46.4% | 51.2% | -4.8 |
| long_sword | 6 | 2.00 | 49.4% | 51.3% | -1.9 |
| longbow | 6 | 2.00 | 49.9% | 50.2% | -0.4 |
| ruby_crystal | 4 | 2.00 | 49.3% | 54.1% | -4.8 |
| stopwatch | 3 | 1.80 | - | 50.0% | - |
| swift_tonic | 1 | 1.95 | - | 50.0% | - |
| vampiric_blade | 5 | 1.68 | 47.6% | 51.6% | -4.0 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 1088 | 69.6 [66.8, 72.2] |
| SM_g2_lane6 | 1044 | 57.9 [54.8, 60.8] |
| SM_g3_phase | 1068 | 22.4 [20.0, 25.0] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| T2_sieger | 1088 | 69.6 [66.8, 72.2] |  | - | - |
| SM_g2_lane6 | 1044 | 57.9 [54.8, 60.8] |  | sieger 60%, laner 40% | 1.0 |
| SM_g3_phase | 1068 | 22.4 [20.0, 25.0] |  | objective 37%, laner 31%, sieger 28%, brawler 4% | 4.5 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 34.60 per game
- that is 38.7% of all ability uses
- of which true snipes (from cover, two or more hexes away): 34.4% of all uses
- snipes aimed at a champion: 4.1 per game
- activations ending beside an enemy-held hexgroup (looking in): 58.8%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **ability usage: ashwyn.R** - used in 20.5% of affordable rounds with a legal target
2. **ability usage: bastion.W** - used in 0.6% of affordable rounds with a legal target
3. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
4. **ability usage: bastion.R** - used in 7.2% of affordable rounds with a legal target
5. **ability usage: bramblehide.Q** - used in 1.4% of affordable rounds with a legal target
