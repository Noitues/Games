# Sim report batch_0044

## 1. Header

| field | value |
|---|---|
| rules | 1.7.0 |
| roster | 1.6.0 |
| ai | 1.4.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 4000 |
| seed | 4401 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 1.4s |
| engine tests | not run |
| generated | 2026-09-24 13:12:51 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 10 FAIL / 7 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 50/58 abilities outside the band; roster mean 19.8%; 9 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 51.0% [49.5, 52.5] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 14.0 [14.0, 14.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 99.4% [99.1, 99.6] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.15 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 46.8% [45.2, 48.3] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 77.4 [75.3, 79.3] | 1612 | 4.94 | 2.29 | 4% | 81% | 1% | 9% | 0.22 | 0.57 | 1.5 | 0.0 | 29% | bootsx1612, longbowx1612, ruby_crystalx1612 |
| bastion | 74.9 [72.7, 77.0] | 1630 | 2.36 | 1.09 | 90% | 0% | 0% | 1% | 0.32 | 0.26 | 0.8 | 0.3 | 16% | cloth_armorx1630, long_swordx1630, ruby_crystalx1630 |
| sable | 58.6 [56.2, 60.9] | 1654 | 5.60 | 2.60 | 4% | 51% | 0% | 38% | 0.20 | 0.23 | 0.6 | 1.3 | 34% | longbowx1654, ionian_charmx1652, ruby_crystalx1648 |
| ashwyn | 58.4 [55.9, 60.8] | 1516 | 4.71 | 2.19 | 3% | 68% | 0% | 21% | 0.24 | 0.74 | 2.0 | 0.0 | 30% | longbowx1516, ruby_crystalx1516, ionian_charmx1514 |
| pallas | 57.5 [55.1, 59.9] | 1606 | 3.54 | 1.64 | 5% | 0% | 1% | 86% | 0.12 | 0.59 | 1.6 | 4.6 | 22% | longbowx1606, ruby_crystalx1606, bootsx1601 |
| veyra | 54.8 [52.3, 57.2] | 1586 | 1.37 | 0.63 | 3% | 68% | 0% | 9% | 0.28 | 0.56 | 1.6 | 1.7 | 9% | long_swordx1586, longbowx1583, vampiric_bladex1554 |
| quillan | 53.5 [51.1, 55.9] | 1622 | 4.70 | 2.18 | 8% | 9% | 0% | 72% | 0.19 | 0.63 | 1.8 | 0.0 | 30% | longbowx1622, ionian_charmx1619, ruby_crystalx1615 |
| thornjaw | 52.6 [50.1, 55.0] | 1568 | 1.30 | 0.61 | 13% | 9% | 3% | 3% | 0.25 | 0.48 | 1.3 | 0.2 | 9% | long_swordx1568, ruby_crystalx1568, vampiric_bladex1538 |
| kestrel | 52.5 [50.0, 55.0] | 1540 | 1.72 | 0.80 | 54% | 15% | 0% | 20% | 0.29 | 0.31 | 0.9 | 3.3 | 12% | long_swordx1540, longbowx1537, vampiric_bladex1526 |
| sylphine | 52.3 [49.9, 54.7] | 1668 | 1.32 | 0.61 | 13% | 2% | 0% | 16% | 0.29 | 0.31 | 0.9 | 0.0 | 9% | ruby_crystalx1667, long_swordx1666, vampiric_bladex1602 |
| bramblehide | 50.6 [48.1, 53.0] | 1582 | 1.64 | 0.76 | 4% | 30% | 1% | 19% | 0.20 | 0.39 | 1.1 | 3.2 | 11% | long_swordx1582, ruby_crystalx1582, vampiric_bladex1580 |
| marrow | 50.5 [48.0, 53.0] | 1560 | 2.22 | 1.03 | 9% | 1% | 1% | 38% | 0.18 | 0.26 | 0.8 | 0.1 | 15% | ruby_crystalx1560, long_swordx1559, cloth_armorx1551 |
| rictus | 49.3 [46.8, 51.8] | 1572 | 1.09 | 0.51 | 13% | 7% | 31% | 2% | 0.28 | 0.84 | 2.2 | 2.5 | 8% | long_swordx1572, ruby_crystalx1572, vampiric_bladex1532 |
| dax | 48.9 [46.5, 51.3] | 1654 | 1.34 | 0.62 | 9% | 42% | 2% | 15% | 0.26 | 0.51 | 1.4 | 1.7 | 10% | long_swordx1654, longbowx1649, vampiric_bladex1642 |
| brixa | 48.7 [46.3, 51.1] | 1640 | 1.38 | 0.64 | 41% | 5% | 7% | 2% | 0.30 | 0.58 | 1.5 | 0.7 | 10% | long_swordx1640, longbowx1640, vampiric_bladex1634 |
| grivven | 48.3 [45.8, 50.7] | 1604 | 2.31 | 1.07 | 6% | 2% | 2% | 66% | 0.08 | 0.45 | 1.4 | 7.2 | 16% | longbowx1604, ruby_crystalx1604, bootsx1601 |
| vurmak | 45.7 [43.3, 48.1] | 1602 | 1.37 | 0.64 | 17% | 1% | 2% | 60% | 0.23 | 0.60 | 1.8 | 4.2 | 10% | ruby_crystalx1602, long_swordx1590, cloth_armorx1508 |
| orrin | 45.3 [42.8, 47.7] | 1580 | 1.55 | 0.72 | 10% | 29% | 1% | 1% | 0.26 | 0.58 | 1.6 | 0.1 | 11% | long_swordx1580, longbowx1574, vampiric_bladex1564 |
| mossgrove | 45.2 [42.8, 47.7] | 1610 | 1.10 | 0.51 | 34% | 2% | 1% | 9% | 0.21 | 0.51 | 1.5 | 3.8 | 8% | long_swordx1610, ruby_crystalx1610, vampiric_bladex1593 |
| noctis | 44.4 [42.0, 46.8] | 1650 | 1.46 | 0.68 | 68% | 1% | 21% | 1% | 0.27 | 0.80 | 2.3 | 0.1 | 12% | longbowx1650, ionian_charmx1625, ruby_crystalx1601 |
| kaelis | 40.3 [37.9, 42.7] | 1562 | 1.16 | 0.54 | 22% | 6% | 2% | 17% | 0.21 | 0.62 | 1.7 | 1.6 | 8% | ruby_crystalx1562, long_swordx1551, cloth_armorx1532 |
| lumen | 38.6 [36.3, 41.0] | 1646 | 0.80 | 0.37 | 67% | 1% | 0% | 2% | 0.18 | 0.37 | 1.0 | 0.2 | 6% | longbowx1646, ruby_crystalx1646, bootsx1626 |
| ossuar | 38.3 [36.0, 40.6] | 1646 | 1.94 | 0.90 | 9% | 4% | 0% | 51% | 0.14 | 0.25 | 0.8 | 4.1 | 13% | ruby_crystalx1646, long_swordx1645, cloth_armorx1631 |
| vellum | 35.0 [32.7, 37.4] | 1558 | 2.44 | 1.13 | 4% | 0% | 3% | 80% | 0.21 | 0.69 | 2.0 | 3.2 | 19% | longbowx1558, ionian_charmx1530, ruby_crystalx1501 |
| corvane | 27.4 [25.2, 29.7] | 1532 | 0.48 | 0.22 | 46% | 0% | 1% | 4% | 0.22 | 0.71 | 2.0 | 3.8 | 4% | longbowx1532, ruby_crystalx1532, bootsx1524 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [48.9, 51.1] | 1.47 |
| Jungle | 50.0 [48.9, 51.1] | 1.29 |
| Mid | 50.0 [48.9, 51.1] | 3.78 |
| Support | 50.0 [48.9, 51.1] | 2.43 |
| Top | 50.0 [48.9, 51.1] | 1.81 |

## 5. Games

- length: median 14.0, p10 12, p90 17
- end reasons: {'nexus': 3976, 'round_limit_hp': 10, 'round_limit_towers': 14} (draws 0)
- priority win rate: 51.0% [49.5, 52.5]
- north win rate: 46.8% [45.2, 48.3]
- length histogram: {8: 4, 9: 14, 10: 55, 11: 177, 12: 395, 13: 656, 14: 786, 15: 716, 16: 564, 17: 330, 18: 167, 19: 87, 20: 49}

## 6. Objectives

- takes per game: {'dragon': 1.35625, 'baron': 0.3955}
- median round taken: dragon 8, baron 13.0
- win rate when secured: {'dragon': 47.963133640552996, 'baron': 39.823008849557525}
- camp clears per game: {'blue_buff': 3.095, 'raptors': 5.553, 'krugs': 5.20575, 'wolves': 5.387, 'red_buff': 3.0815, 'dragon': 1.35625, 'baron': 0.3955}

## 7. Structures

- first tower falls: median round 7.0, p10 5, p90 9
- games with at least one tower down: 100.0%
- first-tower win rate: 69.5%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 4.42 |
| chips_monster | 3.44 |
| base | 3.29 |
| chips_wave | 2.70 |
| champion_kill | 0.50 |
| blue_buff | 0.21 |
| red_buff | 0.16 |

| use | AP |
|---|---|
| shop | 11.26 |
| abilities | 2.33 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.99 | 55.4% | 22.9% | +32.5 |
| cloth_armor | 5 | 1.96 | 56.5% | 40.4% | +16.1 |
| control_ward | 2 | 0.70 | - | 50.0% | - |
| frost_charm | 2 | 0.59 | - | 50.0% | - |
| health_potion | 2 | 1.95 | - | 50.0% | - |
| ionian_charm | 8 | 1.99 | 57.7% | 26.5% | +31.2 |
| long_sword | 6 | 2.00 | 50.9% | 46.6% | +4.3 |
| longbow | 6 | 2.00 | 50.0% | 49.9% | +0.1 |
| ruby_crystal | 4 | 2.00 | 50.6% | 12.5% | +38.0 |
| stopwatch | 3 | 1.93 | - | 50.0% | - |
| swift_tonic | 1 | 1.98 | - | 50.0% | - |
| vampiric_blade | 5 | 1.99 | 53.4% | 42.6% | +10.8 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 4000 | 50.8 [49.3, 52.3] |
| SM_g2_lane6 | 4000 | 49.2 [47.7, 50.7] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| T2_sieger | 4000 | 50.8 [49.3, 52.3] |  | - | - |
| SM_g2_lane6 | 4000 | 49.2 [47.7, 50.7] |  | sieger 65%, laner 35% | 1.0 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 42.06 per game
- that is 39.2% of all ability uses
- of which true snipes (from cover, two or more hexes away): 35.9% of all uses
- snipes aimed at a champion: 6.8 per game
- activations ending beside an enemy-held hexgroup (looking in): 68.5%


## 10. Anomalies

- ILLEGAL[activation r17]: stacking: w48 and w30 on: 1 games
- ILLEGAL[world r17]: stacking: w48 and w30 on: 1 games
- ILLEGAL[activation r6]: stacking: w6 and w0 on: 1 games
- ILLEGAL[world r6]: stacking: w6 and w0 on: 1 games
- ILLEGAL[upkeep r7]: stacking: w6 and w0 on: 1 games
- ILLEGAL[activation r7]: stacking: w6 and w0 on: 1 games
- ILLEGAL[world r7]: stacking: w6 and w0 on: 1 games
- ILLEGAL[activation r7]: stacking: w6 and w2 on: 1 games
- ILLEGAL[world r7]: stacking: w6 and w2 on: 1 games
- ILLEGAL[activation r13]: stacking: n_mid_T2 and w30 on: 1 games
- ILLEGAL[world r13]: stacking: n_mid_T2 and w30 on: 1 games

## 11. Top 5 flags (evidence only)

1. **anomaly: ILLEGAL[activation r17]: stacking: w48 and w30 on** - 1 games
2. **anomaly: ILLEGAL[world r17]: stacking: w48 and w30 on** - 1 games
3. **anomaly: ILLEGAL[activation r6]: stacking: w6 and w0 on** - 1 games
4. **anomaly: ILLEGAL[world r6]: stacking: w6 and w0 on** - 1 games
5. **anomaly: ILLEGAL[upkeep r7]: stacking: w6 and w0 on** - 1 games
