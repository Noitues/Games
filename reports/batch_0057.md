# Sim report batch_0057

## 1. Header

| field | value |
|---|---|
| rules | 1.8.0 |
| roster | 1.7.0 |
| ai | 1.5.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 4000 |
| seed | 5701 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 1.7s |
| engine tests | not run |
| generated | 2026-09-27 10:35:38 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 5 FAIL / 9 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 50/58 abilities outside the band; roster mean 14.2%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 49.2% [47.7, 50.8] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 12.0 [11.0, 12.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 100.0% [99.9, 100.0] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, marrow, quillan, sable (roster mean 1.10 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 46.9% [45.3, 48.4] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bastion | 62.2 [59.7, 64.6] | 1504 | 1.55 | 1.41 | 67% | 0% | 0% | 3% | 0.34 | 0.14 | 0.4 | 0.5 | 15% | ruby_crystalx1504, long_swordx1494, cloth_armorx1362 |
| marrow | 59.4 [57.0, 61.8] | 1616 | 2.06 | 1.87 | 3% | 1% | 0% | 57% | 0.14 | 0.11 | 0.3 | 0.0 | 19% | ruby_crystalx1615, long_swordx1520, cloth_armorx1124 |
| wisp | 59.2 [56.8, 61.6] | 1590 | 1.53 | 1.39 | 7% | 57% | 1% | 8% | 0.12 | 0.55 | 1.3 | 3.5 | 14% | longbowx1579, ruby_crystalx1525, bootsx1004 |
| pallas | 54.1 [51.7, 56.5] | 1652 | 1.31 | 1.19 | 7% | 1% | 2% | 67% | 0.09 | 0.44 | 1.1 | 4.1 | 13% | longbowx1651, ruby_crystalx1622, bootsx1280 |
| noctis | 54.0 [51.6, 56.4] | 1664 | 1.15 | 1.04 | 68% | 0% | 11% | 2% | 0.38 | 0.43 | 1.1 | 0.2 | 12% | longbowx1664, ionian_charmx1461, ruby_crystalx1160 |
| thornjaw | 54.0 [51.5, 56.4] | 1560 | 0.61 | 0.55 | 13% | 4% | 1% | 3% | 0.18 | 0.34 | 0.9 | 0.1 | 6% | long_swordx1549, ruby_crystalx1496, vampiric_bladex826 |
| veyra | 52.3 [49.8, 54.7] | 1544 | 1.02 | 0.93 | 1% | 60% | 0% | 2% | 0.32 | 0.45 | 1.2 | 0.3 | 10% | long_swordx1540, longbowx1400, vampiric_bladex914 |
| bramblehide | 51.9 [49.5, 54.4] | 1610 | 1.07 | 0.97 | 1% | 12% | 1% | 21% | 0.16 | 0.29 | 0.8 | 2.5 | 10% | long_swordx1610, ruby_crystalx1599, vampiric_bladex1321 |
| vellum | 51.1 [48.6, 53.6] | 1522 | 1.63 | 1.48 | 3% | 0% | 4% | 63% | 0.24 | 0.41 | 1.1 | 3.1 | 16% | longbowx1507, ionian_charmx1207, ruby_crystalx853 |
| kestrel | 51.1 [48.7, 53.5] | 1638 | 1.20 | 1.09 | 53% | 7% | 1% | 6% | 0.33 | 0.27 | 0.7 | 0.9 | 12% | long_swordx1638, longbowx1584, vampiric_bladex1260 |
| brixa | 50.4 [48.0, 52.8] | 1664 | 0.71 | 0.65 | 18% | 3% | 7% | 1% | 0.22 | 0.53 | 1.4 | 0.6 | 7% | long_swordx1664, longbowx1602, vampiric_bladex1293 |
| sable | 49.9 [47.4, 52.3] | 1588 | 1.98 | 1.80 | 3% | 39% | 0% | 39% | 0.13 | 0.20 | 0.5 | 3.7 | 19% | longbowx1583, ionian_charmx1341, ruby_crystalx1038 |
| sylphine | 49.6 [47.1, 52.1] | 1540 | 0.65 | 0.59 | 13% | 4% | 0% | 10% | 0.19 | 0.28 | 0.7 | 0.0 | 6% | long_swordx1530, ruby_crystalx1485, vampiric_bladex807 |
| mossgrove | 49.6 [47.1, 52.0] | 1618 | 0.66 | 0.60 | 21% | 1% | 1% | 3% | 0.20 | 0.30 | 0.8 | 2.3 | 7% | long_swordx1618, ruby_crystalx1589, vampiric_bladex1072 |
| quillan | 49.2 [46.8, 51.6] | 1668 | 1.73 | 1.57 | 10% | 9% | 1% | 57% | 0.13 | 0.56 | 1.4 | 2.7 | 17% | longbowx1663, ionian_charmx1402, ruby_crystalx1137 |
| dax | 48.9 [46.5, 51.4] | 1610 | 0.83 | 0.75 | 13% | 24% | 3% | 3% | 0.27 | 0.47 | 1.2 | 0.5 | 8% | long_swordx1610, longbowx1549, vampiric_bladex1240 |
| lumen | 48.6 [46.1, 51.1] | 1568 | 0.49 | 0.45 | 43% | 1% | 0% | 1% | 0.16 | 0.32 | 0.8 | 0.1 | 5% | longbowx1567, ruby_crystalx1546, bootsx1150 |
| orrin | 47.3 [44.8, 49.8] | 1544 | 0.76 | 0.70 | 4% | 15% | 1% | 0% | 0.18 | 0.62 | 1.6 | 0.0 | 8% | long_swordx1543, longbowx1412, vampiric_bladex944 |
| grivven | 46.8 [44.4, 49.3] | 1592 | 0.95 | 0.86 | 5% | 4% | 5% | 31% | 0.08 | 0.32 | 0.8 | 4.4 | 10% | longbowx1591, ruby_crystalx1578, bootsx1332 |
| ashwyn | 45.6 [43.2, 48.1] | 1558 | 1.75 | 1.59 | 5% | 50% | 1% | 23% | 0.22 | 0.70 | 1.8 | 2.0 | 17% | longbowx1558, ionian_charmx1497, ruby_crystalx1382 |
| kaelis | 45.3 [42.9, 47.8] | 1578 | 0.55 | 0.50 | 28% | 3% | 7% | 5% | 0.16 | 0.26 | 0.7 | 0.5 | 6% | ruby_crystalx1578, long_swordx1444, cloth_armorx1081 |
| rictus | 45.2 [42.8, 47.6] | 1672 | 0.66 | 0.60 | 13% | 4% | 20% | 2% | 0.24 | 0.62 | 1.6 | 1.8 | 7% | long_swordx1670, ruby_crystalx1636, vampiric_bladex989 |
| vurmak | 43.0 [40.7, 45.4] | 1700 | 0.90 | 0.82 | 23% | 6% | 1% | 24% | 0.33 | 0.21 | 0.5 | 2.2 | 10% | ruby_crystalx1700, long_swordx1381, cloth_armorx716 |
| ossuar | 41.1 [38.8, 43.6] | 1602 | 1.49 | 1.36 | 9% | 1% | 0% | 52% | 0.09 | 0.17 | 0.5 | 3.7 | 15% | ruby_crystalx1602, long_swordx1514, cloth_armorx1052 |
| corvane | 41.1 [38.7, 43.5] | 1598 | 0.27 | 0.25 | 17% | 0% | 1% | 3% | 0.23 | 0.59 | 1.4 | 1.9 | 3% | longbowx1598, ruby_crystalx1589, bootsx1307 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [48.9, 51.1] | 0.91 |
| Jungle | 50.0 [48.9, 51.1] | 0.73 |
| Mid | 50.0 [48.9, 51.1] | 1.64 |
| Support | 50.0 [48.9, 51.1] | 0.91 |
| Top | 50.0 [48.9, 51.1] | 1.31 |

## 5. Games

- length: median 12.0, p10 9, p90 14
- end reasons: {'nexus': 4000} (draws 0)
- priority win rate: 49.2% [47.7, 50.8]
- north win rate: 46.9% [45.3, 48.4]
- length histogram: {5: 4, 6: 35, 7: 112, 8: 229, 9: 375, 10: 586, 11: 658, 12: 691, 13: 554, 14: 371, 15: 227, 16: 99, 17: 29, 18: 23, 19: 5, 20: 2}

## 6. Objectives

- takes per game: {'dragon': 1.063, 'baron': 0.124}
- median round taken: dragon 6.0, baron 12.0
- win rate when secured: {'dragon': 46.284101599247414, 'baron': 42.13709677419355}
- camp clears per game: {'krugs': 3.851, 'wolves': 4.12175, 'raptors': 4.18575, 'blue_buff': 2.1615, 'red_buff': 2.02975, 'dragon': 1.063, 'baron': 0.124}

## 7. Structures

- first tower falls: median round 4.0, p10 3, p90 7
- games with at least one tower down: 100.0%
- first-tower win rate: 64.8%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.15 |
| base | 3.00 |
| chips_wave | 2.13 |
| tower_kill | 0.79 |
| champion_kill | 0.47 |
| blue_buff | 0.19 |
| dragon | 0.14 |
| red_buff | 0.09 |

| use | AP |
|---|---|
| shop | 7.93 |
| abilities | 1.60 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.52 | 50.1% | 50.0% | +0.2 |
| cloth_armor | 5 | 1.33 | 50.9% | 49.8% | +1.2 |
| control_ward | 2 | 0.01 | - | 50.0% | - |
| frost_charm | 2 | 0.00 | - | 50.0% | - |
| health_potion | 2 | 1.79 | - | 50.0% | - |
| ionian_charm | 8 | 1.73 | 48.6% | 50.3% | -1.7 |
| long_sword | 6 | 2.00 | 50.2% | 49.7% | +0.5 |
| longbow | 6 | 2.00 | 49.8% | 50.3% | -0.6 |
| ruby_crystal | 4 | 2.00 | 49.7% | 51.2% | -1.5 |
| stopwatch | 3 | 1.73 | - | 50.0% | - |
| swift_tonic | 1 | 1.95 | - | 50.0% | - |
| vampiric_blade | 5 | 1.54 | 50.2% | 49.9% | +0.2 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 4000 | 59.8 [58.3, 61.3] |
| SM_g2_lane6 | 4000 | 40.2 [38.7, 41.7] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| T2_sieger | 4000 | 59.8 [58.3, 61.3] |  | - | - |
| SM_g2_lane6 | 4000 | 40.2 [38.7, 41.7] |  | sieger 56%, laner 44% | 1.0 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 29.87 per game
- that is 36.7% of all ability uses
- of which true snipes (from cover, two or more hexes away): 32.6% of all uses
- snipes aimed at a champion: 3.7 per game
- activations ending beside an enemy-held hexgroup (looking in): 62.9%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **Median game length 13-18 rounds** - 12.0 [11.0, 12.0]
2. **ability usage: ashwyn.R** - used in 22.9% of affordable rounds with a legal target
3. **ability usage: bastion.W** - used in 0.4% of affordable rounds with a legal target
4. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
5. **ability usage: bastion.R** - used in 2.6% of affordable rounds with a legal target
