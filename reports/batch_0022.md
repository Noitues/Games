# Sim report batch_0022

## 1. Header

| field | value |
|---|---|
| rules | 1.1.1 |
| roster | 1.2.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 300 |
| seed | 2201 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 961.1s |
| engine tests | 105 passed in 70.76s (0:01:10) |
| generated | 2026-09-20 18:27:27 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 9 FAIL / 16 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 54/56 abilities outside the band; roster mean 18.3%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 49.0% [43.4, 54.6] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 14.0 [13.0, 14.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 97.3% [94.8, 98.6] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.58 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 47.0% [41.4, 52.6] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 76.9 [68.0, 84.0] | 104 | 6.44 | 2.49 | 10% | 71% | 0% | 7% | 0.00 | 0.02 | 0.0 | 0.0 | 34% | bootsx104, cloth_armorx104, longbowx104 |
| ashwyn | 72.5 [63.9, 79.7] | 120 | 10.08 | 3.90 | 1% | 89% | 0% | 5% | 0.00 | 0.00 | 0.0 | 0.1 | 50% | bootsx120, ionian_charmx120, long_swordx120 |
| pallas | 71.1 [63.2, 77.9] | 142 | 5.12 | 1.98 | 7% | 1% | 0% | 86% | 0.01 | 0.01 | 0.0 | 4.2 | 28% | longbowx142, ruby_crystalx142, bootsx140 |
| bramblehide | 67.9 [58.7, 75.8] | 112 | 2.20 | 0.85 | 5% | 24% | 1% | 35% | 0.02 | 0.00 | 0.0 | 3.5 | 13% | long_swordx112, ruby_crystalx112, vampiric_bladex112 |
| quillan | 67.3 [58.1, 75.3] | 110 | 8.18 | 3.17 | 3% | 3% | 1% | 86% | 0.01 | 0.01 | 0.0 | 2.5 | 43% | bootsx110, ionian_charmx110, long_swordx110 |
| kestrel | 61.5 [53.0, 69.5] | 130 | 1.87 | 0.72 | 42% | 18% | 4% | 23% | 0.00 | 0.02 | 0.1 | 3.3 | 11% | long_swordx130, longbowx130, vampiric_bladex128 |
| vurmak | 58.6 [49.5, 67.2] | 116 | 1.45 | 0.56 | 20% | 5% | 2% | 39% | 0.03 | 0.01 | 0.0 | 3.1 | 9% | ruby_crystalx116, long_swordx113, cloth_armorx109 |
| bastion | 55.5 [46.8, 63.8] | 128 | 1.59 | 0.62 | 38% | 3% | 1% | 11% | 0.02 | 0.01 | 0.0 | 2.2 | 10% | ruby_crystalx128, long_swordx127, cloth_armorx126 |
| sable | 55.3 [46.1, 64.1] | 114 | 6.33 | 2.45 | 5% | 57% | 0% | 26% | 0.00 | 0.01 | 0.0 | 2.8 | 37% | ionian_charmx114, longbowx114, ruby_crystalx113 |
| ossuar | 53.7 [45.3, 62.0] | 134 | 2.09 | 0.81 | 13% | 8% | 5% | 43% | 0.00 | 0.01 | 0.0 | 3.5 | 13% | long_swordx134, ruby_crystalx134, cloth_armorx133 |
| veyra | 53.4 [44.4, 62.3] | 116 | 1.06 | 0.41 | 11% | 35% | 6% | 14% | 0.01 | 0.03 | 0.1 | 2.5 | 7% | long_swordx116, longbowx115, vampiric_bladex109 |
| dax | 47.5 [38.8, 56.4] | 120 | 1.16 | 0.45 | 18% | 30% | 6% | 18% | 0.01 | 0.04 | 0.1 | 2.0 | 7% | long_swordx120, longbowx120, vampiric_bladex117 |
| orrin | 46.4 [37.5, 55.6] | 112 | 0.93 | 0.36 | 17% | 19% | 12% | 6% | 0.04 | 0.04 | 0.1 | 1.9 | 6% | long_swordx112, longbowx110, vampiric_bladex109 |
| rictus | 46.4 [38.3, 54.7] | 138 | 1.05 | 0.41 | 20% | 19% | 19% | 1% | 0.01 | 0.01 | 0.0 | 1.7 | 7% | long_swordx138, ruby_crystalx138, vampiric_bladex132 |
| mossgrove | 46.3 [37.2, 55.7] | 108 | 0.84 | 0.33 | 24% | 19% | 2% | 8% | 0.03 | 0.01 | 0.0 | 3.1 | 6% | long_swordx108, ruby_crystalx108, vampiric_bladex99 |
| thornjaw | 46.2 [37.8, 54.7] | 130 | 1.01 | 0.39 | 13% | 17% | 8% | 5% | 0.00 | 0.02 | 0.1 | 0.7 | 7% | long_swordx130, ruby_crystalx130, vampiric_bladex120 |
| sylphine | 44.6 [35.8, 53.9] | 112 | 0.81 | 0.31 | 13% | 1% | 11% | 14% | 0.01 | 0.01 | 0.0 | 1.2 | 5% | long_swordx112, ruby_crystalx112, vampiric_bladex108 |
| grivven | 44.5 [36.2, 53.2] | 128 | 3.08 | 1.19 | 14% | 2% | 1% | 60% | 0.01 | 0.02 | 0.0 | 7.6 | 20% | longbowx128, ruby_crystalx128, bootsx127 |
| marrow | 41.4 [33.2, 50.1] | 128 | 1.70 | 0.66 | 13% | 2% | 11% | 23% | 0.01 | 0.00 | 0.0 | 1.0 | 12% | ruby_crystalx128, long_swordx127, cloth_armorx126 |
| brixa | 40.2 [31.9, 49.0] | 122 | 1.12 | 0.43 | 28% | 11% | 12% | 8% | 0.01 | 0.02 | 0.0 | 1.2 | 8% | long_swordx122, longbowx121, vampiric_bladex118 |
| kaelis | 38.3 [29.1, 48.4] | 94 | 0.99 | 0.38 | 22% | 17% | 4% | 12% | 0.00 | 0.00 | 0.0 | 1.0 | 7% | ruby_crystalx94, long_swordx93, cloth_armorx87 |
| corvane | 30.5 [22.9, 39.3] | 118 | 0.42 | 0.16 | 37% | 2% | 13% | 1% | 0.01 | 0.04 | 0.1 | 3.8 | 3% | longbowx118, ruby_crystalx118, bootsx114 |
| vellum | 30.3 [23.1, 38.6] | 132 | 3.05 | 1.18 | 11% | 0% | 8% | 70% | 0.01 | 0.02 | 0.0 | 2.6 | 23% | longbowx132, ionian_charmx127, ruby_crystalx121 |
| noctis | 29.0 [21.8, 37.6] | 124 | 1.36 | 0.53 | 48% | 5% | 21% | 3% | 0.01 | 0.02 | 0.1 | 0.6 | 11% | longbowx124, ionian_charmx117, ruby_crystalx109 |
| lumen | 24.1 [17.0, 32.9] | 108 | 0.66 | 0.25 | 34% | 4% | 1% | 2% | 0.01 | 0.01 | 0.0 | 0.3 | 5% | longbowx108, ruby_crystalx108, bootsx104 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [46.0, 54.0] | 1.24 |
| Jungle | 50.0 [46.0, 54.0] | 1.17 |
| Mid | 50.0 [46.0, 54.0] | 5.67 |
| Support | 50.0 [46.0, 54.0] | 3.18 |
| Top | 50.0 [46.0, 54.0] | 1.61 |

## 5. Games

- length: median 14.0, p10 11, p90 18
- end reasons: {'nexus': 292, 'round_limit_kills': 1, 'round_limit_towers': 6, 'round_limit_hp': 1} (draws 0)
- priority win rate: 49.0% [43.4, 54.6]
- north win rate: 47.0% [41.4, 52.6]
- length histogram: {9: 6, 10: 19, 11: 35, 12: 52, 13: 35, 14: 47, 15: 33, 16: 20, 17: 16, 18: 11, 19: 13, 20: 13}

## 6. Objectives

- takes per game: {'dragon': 1.84, 'baron': 0.8566666666666667}
- median round taken: dragon 8.0, baron 11
- win rate when secured: {'dragon': 44.02173913043478, 'baron': 50.97276264591439}
- camp clears per game: {'raptors': 6.93, 'krugs': 6.886666666666667, 'wolves': 6.2, 'blue_buff': 4.08, 'red_buff': 4.18, 'dragon': 1.84, 'baron': 0.8566666666666667}

## 7. Structures

- first tower falls: median round 5.0, p10 4, p90 7
- games with at least one tower down: 100.0%
- first-tower win rate: 74.7%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.38 |
| chips_wave | 4.07 |
| chips_structure | 4.00 |
| base | 3.38 |
| blue_buff | 0.29 |
| red_buff | 0.22 |
| champion_kill | 0.01 |

| use | AP |
|---|---|
| shop | 11.88 |
| abilities | 2.22 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.96 | 58.4% | 6.2% | +52.2 |
| cloth_armor | 5 | 1.94 | 61.0% | 31.2% | +29.8 |
| control_ward | 2 | 1.17 | - | 50.0% | - |
| frost_charm | 2 | 1.03 | - | 50.0% | - |
| health_potion | 2 | 1.93 | - | 50.0% | - |
| ionian_charm | 8 | 1.96 | 62.2% | 5.2% | +57.0 |
| long_sword | 6 | 2.00 | 51.6% | 44.4% | +7.2 |
| longbow | 6 | 2.00 | 50.1% | 49.8% | +0.3 |
| ruby_crystal | 4 | 2.00 | 51.4% | 1.2% | +50.2 |
| stopwatch | 3 | 1.92 | - | 50.0% | - |
| swift_tonic | 1 | 1.98 | - | 50.0% | - |
| vampiric_blade | 5 | 1.95 | 56.3% | 35.7% | +20.7 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 81.59 per game
- that is 85.5% of all ability uses


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 10.08 AP/round = 3.90x roster mean
2. **economy outlier: quillan** - 8.18 AP/round = 3.17x roster mean
3. **champion win rate: wisp** - WR 76.9% [68.0, 84.0]
4. **champion win rate: lumen** - WR 24.1% [17.0, 32.9]
5. **champion win rate: ashwyn** - WR 72.5% [63.9, 79.7]

## 12. Delta vs batch_0016

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -15.0 | +0.58 | no |
| bastion | +3.7 | +0.07 | no |
| bramblehide | +17.9 | +0.21 | no |
| brixa | +5.5 | -0.01 | no |
| corvane | +8.8 | +0.05 | no |
| dax | -5.3 | -0.05 | no |
| grivven | +13.0 | +0.36 | no |
| kaelis | +7.7 | +0.13 | no |
| kestrel | -7.4 | +0.01 | no |
| lumen | -25.9 | -0.02 | yes |
| marrow | -7.2 | +0.12 | no |
| mossgrove | -0.8 | +0.07 | no |
| noctis | +2.9 | +0.10 | no |
| orrin | +10.2 | +0.07 | no |
| ossuar | -4.6 | +0.15 | no |
| pallas | -0.9 | +0.53 | no |
| quillan | +4.8 | +0.38 | no |
| rictus | -7.2 | +0.02 | no |
| sable | +17.3 | +0.50 | no |
| sylphine | -6.9 | +0.03 | no |
| thornjaw | -2.1 | +0.03 | no |
| vellum | -5.4 | +0.45 | no |
| veyra | -1.6 | +0.07 | no |
| vurmak | +7.1 | +0.18 | no |
| wisp | -6.4 | +0.24 | no |

- median length delta: +3.0
- nexus-kill rate delta: +0.0 pts
