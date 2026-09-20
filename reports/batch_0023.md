# Sim report batch_0023

## 1. Header

| field | value |
|---|---|
| rules | 1.2.0 |
| roster | 1.3.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 300 |
| seed | 2301 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 1005.6s |
| engine tests | 107 passed in 63.79s (0:01:03) |
| generated | 2026-09-20 22:03:10 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 7 FAIL / 18 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 48/56 abilities outside the band; roster mean 18.4%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 55.3% [49.7, 60.9] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 15.0 [15.0, 16.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 88.7% [84.6, 91.8] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, wisp (roster mean 2.26 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 47.3% [41.8, 53.0] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 84.4 [77.1, 89.7] | 128 | 10.91 | 4.82 | 0% | 97% | 0% | 1% | 0.30 | 0.20 | 0.3 | 0.0 | 54% | bootsx128, ionian_charmx128, long_swordx128 |
| wisp | 77.6 [69.2, 84.2] | 116 | 7.00 | 3.09 | 3% | 86% | 1% | 4% | 0.19 | 0.42 | 0.8 | 0.0 | 39% | longbowx116, ruby_crystalx116, bootsx115 |
| kestrel | 76.4 [67.6, 83.3] | 110 | 1.50 | 0.66 | 13% | 47% | 9% | 17% | 0.36 | 0.13 | 0.3 | 2.4 | 10% | long_swordx110, vampiric_bladex106, longbowx105 |
| bramblehide | 69.1 [59.9, 77.0] | 110 | 2.06 | 0.91 | 2% | 37% | 1% | 39% | 0.13 | 0.15 | 0.3 | 4.4 | 14% | long_swordx110, ruby_crystalx110, vampiric_bladex110 |
| sable | 63.2 [53.7, 71.8] | 106 | 6.30 | 2.78 | 2% | 82% | 0% | 9% | 0.20 | 0.34 | 0.7 | 3.3 | 41% | longbowx106, ionian_charmx105, ruby_crystalx103 |
| quillan | 59.0 [50.1, 67.3] | 122 | 8.28 | 3.66 | 0% | 0% | 1% | 95% | 0.16 | 0.48 | 1.0 | 3.0 | 48% | ionian_charmx122, longbowx122, ruby_crystalx122 |
| ossuar | 58.1 [49.3, 66.4] | 124 | 2.02 | 0.89 | 5% | 6% | 8% | 55% | 0.16 | 0.06 | 0.1 | 4.6 | 15% | ruby_crystalx124, long_swordx121, cloth_armorx117 |
| grivven | 56.7 [47.7, 65.2] | 120 | 2.96 | 1.31 | 4% | 6% | 1% | 69% | 0.12 | 0.17 | 0.4 | 8.0 | 20% | ruby_crystalx120, longbowx119, bootsx118 |
| marrow | 54.5 [45.2, 63.4] | 112 | 0.61 | 0.27 | 27% | 4% | 17% | 9% | 0.17 | 0.12 | 0.2 | 1.6 | 4% | ruby_crystalx112, long_swordx107, cloth_armorx105 |
| thornjaw | 51.8 [42.6, 60.9] | 110 | 0.79 | 0.35 | 23% | 29% | 5% | 2% | 0.24 | 0.14 | 0.3 | 0.5 | 6% | ruby_crystalx110, long_swordx105, vampiric_bladex96 |
| mossgrove | 51.4 [43.3, 59.5] | 142 | 0.67 | 0.29 | 32% | 20% | 2% | 15% | 0.14 | 0.10 | 0.3 | 4.6 | 5% | ruby_crystalx142, long_swordx141, vampiric_bladex129 |
| bastion | 50.0 [40.7, 59.3] | 108 | 1.25 | 0.55 | 65% | 4% | 1% | 1% | 0.16 | 0.09 | 0.2 | 0.4 | 10% | ruby_crystalx108, cloth_armorx102, long_swordx102 |
| vurmak | 49.2 [40.9, 57.7] | 132 | 1.13 | 0.50 | 43% | 11% | 3% | 17% | 0.27 | 0.15 | 0.3 | 1.5 | 9% | ruby_crystalx132, long_swordx109, cloth_armorx103 |
| orrin | 49.2 [40.6, 57.9] | 124 | 0.66 | 0.29 | 7% | 19% | 22% | 10% | 0.15 | 0.23 | 0.5 | 2.6 | 5% | long_swordx119, vampiric_bladex113, longbowx110 |
| veyra | 49.2 [40.5, 57.9] | 122 | 1.04 | 0.46 | 5% | 54% | 10% | 5% | 0.17 | 0.26 | 0.6 | 1.1 | 7% | long_swordx119, longbowx112, vampiric_bladex104 |
| pallas | 47.4 [38.6, 56.4] | 116 | 2.51 | 1.11 | 27% | 3% | 3% | 53% | 0.14 | 0.51 | 1.2 | 3.3 | 19% | longbowx116, ruby_crystalx116, bootsx109 |
| brixa | 41.7 [32.8, 51.1] | 108 | 0.86 | 0.38 | 18% | 31% | 6% | 8% | 0.20 | 0.35 | 0.7 | 0.7 | 6% | long_swordx107, vampiric_bladex107, longbowx104 |
| sylphine | 40.7 [31.9, 50.2] | 108 | 0.54 | 0.24 | 18% | 3% | 14% | 24% | 0.14 | 0.09 | 0.2 | 1.5 | 4% | ruby_crystalx108, long_swordx107, vampiric_bladex96 |
| kaelis | 38.7 [30.6, 47.5] | 124 | 0.68 | 0.30 | 41% | 8% | 9% | 6% | 0.18 | 0.15 | 0.3 | 0.5 | 5% | ruby_crystalx124, cloth_armorx121, long_swordx119 |
| rictus | 38.5 [30.5, 47.0] | 130 | 0.65 | 0.29 | 10% | 39% | 8% | 5% | 0.23 | 0.31 | 0.6 | 1.3 | 5% | ruby_crystalx129, long_swordx124, vampiric_bladex105 |
| corvane | 37.5 [29.4, 46.4] | 120 | 0.18 | 0.08 | 19% | 4% | 23% | 6% | 0.17 | 0.42 | 0.9 | 4.0 | 1% | ruby_crystalx120, longbowx119, bootsx118 |
| dax | 36.8 [29.1, 45.1] | 136 | 0.88 | 0.39 | 43% | 15% | 3% | 12% | 0.15 | 0.21 | 0.4 | 1.2 | 7% | long_swordx135, longbowx127, vampiric_bladex124 |
| lumen | 32.8 [25.3, 41.3] | 128 | 0.55 | 0.24 | 58% | 3% | 2% | 4% | 0.10 | 0.20 | 0.4 | 0.7 | 5% | longbowx128, ruby_crystalx128, bootsx123 |
| vellum | 30.8 [22.7, 40.2] | 104 | 1.88 | 0.83 | 6% | 2% | 25% | 53% | 0.10 | 0.47 | 1.1 | 2.5 | 17% | longbowx95, ruby_crystalx89, ionian_charmx81 |
| noctis | 15.0 [10.0, 21.8] | 140 | 0.69 | 0.30 | 32% | 13% | 14% | 8% | 0.16 | 0.61 | 1.3 | 2.3 | 7% | longbowx139, ruby_crystalx122, ionian_charmx104 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [46.0, 54.0] | 0.98 |
| Jungle | 50.0 [46.0, 54.0] | 0.92 |
| Mid | 50.0 [46.0, 54.0] | 5.61 |
| Support | 50.0 [46.0, 54.0] | 2.58 |
| Top | 50.0 [46.0, 54.0] | 1.14 |

## 5. Games

- length: median 15.0, p10 12, p90 20
- end reasons: {'nexus': 266, 'round_limit_towers': 34} (draws 0)
- priority win rate: 55.3% [49.7, 60.9]
- north win rate: 47.3% [41.8, 53.0]
- length histogram: {8: 1, 9: 5, 10: 6, 11: 16, 12: 27, 13: 33, 14: 42, 15: 36, 16: 30, 17: 27, 18: 20, 19: 13, 20: 44}

## 6. Objectives

- takes per game: {'dragon': 1.77, 'baron': 0.8366666666666667}
- median round taken: dragon 9, baron 12
- win rate when secured: {'dragon': 45.5743879472693, 'baron': 46.21513944223108}
- camp clears per game: {'raptors': 6.913333333333333, 'wolves': 6.65, 'krugs': 6.916666666666667, 'blue_buff': 4.3133333333333335, 'red_buff': 4.346666666666667, 'dragon': 1.77, 'baron': 0.8366666666666667}

## 7. Structures

- first tower falls: median round 6.0, p10 4, p90 9
- games with at least one tower down: 100.0%
- first-tower win rate: 86.3%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.14 |
| chips_wave | 3.69 |
| base | 3.36 |
| chips_structure | 3.09 |
| blue_buff | 0.28 |
| red_buff | 0.14 |
| champion_kill | 0.07 |

| use | AP |
|---|---|
| shop | 10.52 |
| abilities | 2.09 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.94 | 62.4% | 2.7% | +59.7 |
| cloth_armor | 5 | 1.83 | 65.9% | 27.0% | +39.0 |
| control_ward | 2 | 1.10 | - | 50.0% | - |
| frost_charm | 2 | 1.04 | - | 50.0% | - |
| health_potion | 2 | 1.94 | - | 50.0% | - |
| ionian_charm | 8 | 1.80 | 67.9% | 4.4% | +63.5 |
| long_sword | 6 | 1.97 | 54.3% | 38.0% | +16.3 |
| longbow | 6 | 1.99 | 51.5% | 47.8% | +3.7 |
| ruby_crystal | 4 | 2.00 | 52.2% | 0.0% | +52.2 |
| stopwatch | 3 | 1.94 | - | 50.0% | - |
| swift_tonic | 1 | 1.98 | - | 50.0% | - |
| vampiric_blade | 5 | 1.87 | 60.5% | 30.4% | +30.1 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 46.75 per game
- that is 46.0% of all ability uses


## 10. Anomalies

- ILLEGAL[activation r12]: stacking: s_thornjaw and n_bastion on: 1 games

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 10.91 AP/round = 4.82x roster mean
2. **economy outlier: quillan** - 8.28 AP/round = 3.66x roster mean
3. **anomaly: ILLEGAL[activation r12]: stacking: s_thornjaw and n_bastion on** - 1 games
4. **champion win rate: noctis** - WR 15.0% [10.0, 21.8]
5. **champion win rate: ashwyn** - WR 84.4% [77.1, 89.7]

## 12. Delta vs batch_0022

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +11.9 | +0.82 | no |
| bastion | -5.5 | -0.35 | no |
| bramblehide | +1.2 | -0.14 | no |
| brixa | +1.5 | -0.26 | no |
| corvane | +7.0 | -0.24 | no |
| dax | -10.7 | -0.28 | no |
| grivven | +12.1 | -0.12 | no |
| kaelis | +0.4 | -0.31 | no |
| kestrel | +14.8 | -0.37 | no |
| lumen | +8.7 | -0.10 | no |
| marrow | +13.1 | -1.10 | no |
| mossgrove | +5.1 | -0.18 | no |
| noctis | -14.0 | -0.67 | no |
| orrin | +2.8 | -0.27 | no |
| ossuar | +4.3 | -0.07 | no |
| pallas | -23.7 | -2.61 | yes |
| quillan | -8.3 | +0.10 | no |
| rictus | -7.9 | -0.40 | no |
| sable | +7.9 | -0.03 | no |
| sylphine | -3.9 | -0.27 | no |
| thornjaw | +5.7 | -0.21 | no |
| vellum | +0.5 | -1.17 | no |
| veyra | -4.3 | -0.02 | no |
| vurmak | -9.4 | -0.31 | no |
| wisp | +0.7 | +0.56 | no |

- median length delta: +1.0
- nexus-kill rate delta: -8.7 pts
