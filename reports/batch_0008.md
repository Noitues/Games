# Sim report batch_0008

## 1. Header

| field | value |
|---|---|
| rules | 1.0.0 |
| roster | 1.1.0 |
| ai | 1.2.0 |
| matchup | T2_search vs T1_greedy (temperature 0.3) |
| games | 400 |
| seed | 991001 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 1891.9s |
| engine tests | 93 passed in 39.84s |
| generated | 2026-09-19 19:04:23 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 5 FAIL / 20 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 47/58 abilities outside the band; roster mean 27.8%; 7 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 58.5% [53.6, 63.2] | **FAIL** |
| Median game length 13-18 rounds | 12.0 [11.0, 12.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 98.8% [97.1, 99.5] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, ossuar, quillan, sable (roster mean 2.26 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 50.5% [45.6, 55.4] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 90.6 [85.3, 94.1] | 170 | 11.03 | 4.89 | 0% | 3% | 0% | 95% | 2.11 | 1.46 | 2.1 | 2.0 | 51% | ionian_charmx170, longbowx170, ruby_crystalx169 |
| ossuar | 72.2 [63.8, 79.3] | 126 | 4.47 | 1.98 | 1% | 0% | 0% | 92% | 0.75 | 0.74 | 1.2 | 4.1 | 24% | ruby_crystalx126, long_swordx123, cloth_armorx120 |
| wisp | 64.2 [56.6, 71.2] | 162 | 2.96 | 1.31 | 7% | 37% | 2% | 47% | 0.80 | 1.67 | 2.8 | 2.4 | 19% | ruby_crystalx160, longbowx154, bootsx134 |
| sable | 62.0 [54.5, 69.1] | 166 | 7.11 | 3.15 | 3% | 9% | 0% | 82% | 1.46 | 1.61 | 2.5 | 2.4 | 40% | longbowx165, ruby_crystalx153, ionian_charmx152 |
| ashwyn | 57.0 [48.8, 64.9] | 142 | 6.67 | 2.96 | 2% | 80% | 0% | 16% | 1.17 | 1.70 | 2.9 | 0.5 | 40% | longbowx142, ionian_charmx140, ruby_crystalx135 |
| grivven | 56.8 [49.1, 64.2] | 162 | 1.88 | 0.84 | 28% | 4% | 1% | 54% | 0.43 | 1.22 | 2.4 | 5.4 | 12% | ruby_crystalx162, longbowx160, bootsx156 |
| bramblehide | 55.1 [46.7, 63.1] | 138 | 2.90 | 1.29 | 2% | 7% | 2% | 75% | 0.96 | 1.71 | 2.7 | 3.2 | 18% | long_swordx137, ruby_crystalx137, vampiric_bladex118 |
| brixa | 54.5 [47.2, 61.7] | 176 | 1.01 | 0.45 | 12% | 7% | 8% | 51% | 0.22 | 1.20 | 2.1 | 3.5 | 7% | long_swordx174, longbowx156, vampiric_bladex147 |
| kaelis | 54.0 [46.6, 61.2] | 176 | 0.88 | 0.39 | 21% | 8% | 3% | 34% | 0.34 | 1.16 | 1.9 | 2.4 | 6% | ruby_crystalx176, long_swordx148, cloth_armorx143 |
| kestrel | 53.9 [46.0, 61.6] | 154 | 1.76 | 0.78 | 6% | 18% | 1% | 67% | 0.63 | 1.08 | 1.8 | 5.4 | 12% | long_swordx153, longbowx140, vampiric_bladex131 |
| rictus | 50.7 [42.7, 58.7] | 146 | 0.61 | 0.27 | 27% | 6% | 15% | 15% | 0.66 | 1.36 | 2.3 | 2.0 | 4% | ruby_crystalx142, long_swordx136, vampiric_bladex107 |
| veyra | 50.5 [43.3, 57.7] | 182 | 1.11 | 0.49 | 6% | 15% | 1% | 66% | 0.22 | 1.15 | 2.0 | 5.0 | 8% | long_swordx162, longbowx144, vampiric_bladex125 |
| sylphine | 50.0 [42.8, 57.2] | 180 | 0.65 | 0.29 | 24% | 7% | 7% | 32% | 0.37 | 1.05 | 1.8 | 2.6 | 5% | ruby_crystalx171, long_swordx168, vampiric_bladex141 |
| thornjaw | 49.4 [42.1, 56.8] | 174 | 0.75 | 0.33 | 31% | 6% | 11% | 10% | 0.36 | 1.15 | 1.8 | 1.5 | 5% | ruby_crystalx170, long_swordx168, vampiric_bladex128 |
| mossgrove | 45.7 [38.2, 53.4] | 162 | 0.58 | 0.26 | 15% | 16% | 5% | 32% | 0.30 | 1.13 | 2.1 | 4.1 | 4% | ruby_crystalx156, long_swordx154, vampiric_bladex118 |
| pallas | 45.7 [38.2, 53.4] | 162 | 2.78 | 1.23 | 4% | 7% | 3% | 70% | 0.54 | 1.78 | 3.0 | 3.1 | 18% | ruby_crystalx161, longbowx160, bootsx146 |
| dax | 45.6 [37.5, 54.0] | 136 | 1.04 | 0.46 | 9% | 18% | 3% | 52% | 0.35 | 1.15 | 1.9 | 3.4 | 8% | long_swordx132, longbowx113, vampiric_bladex111 |
| marrow | 45.5 [37.8, 53.3] | 154 | 1.16 | 0.51 | 5% | 6% | 3% | 54% | 0.45 | 1.13 | 2.0 | 3.3 | 9% | ruby_crystalx154, long_swordx127, cloth_armorx118 |
| orrin | 44.1 [36.4, 52.0] | 152 | 0.80 | 0.35 | 12% | 42% | 9% | 4% | 0.30 | 1.32 | 2.2 | 3.2 | 6% | long_swordx145, longbowx131, vampiric_bladex115 |
| corvane | 43.8 [36.4, 51.5] | 162 | 0.21 | 0.09 | 53% | 7% | 3% | 7% | 0.21 | 0.84 | 1.4 | 4.3 | 2% | longbowx160, ruby_crystalx156, bootsx138 |
| vurmak | 42.6 [35.2, 50.3] | 162 | 1.07 | 0.47 | 13% | 3% | 4% | 54% | 0.43 | 1.20 | 2.0 | 3.5 | 8% | ruby_crystalx162, long_swordx131, cloth_armorx109 |
| bastion | 41.2 [34.3, 48.5] | 182 | 1.61 | 0.72 | 10% | 12% | 1% | 46% | 0.52 | 0.99 | 1.7 | 4.3 | 12% | ruby_crystalx182, long_swordx152, cloth_armorx146 |
| lumen | 38.8 [31.4, 46.7] | 152 | 0.45 | 0.20 | 62% | 3% | 1% | 16% | 0.32 | 0.57 | 1.0 | 1.5 | 4% | ruby_crystalx149, longbowx145, bootsx118 |
| vellum | 28.4 [22.0, 35.8] | 162 | 2.35 | 1.04 | 5% | 0% | 1% | 84% | 0.53 | 1.77 | 3.1 | 3.2 | 21% | longbowx144, ruby_crystalx108, ionian_charmx102 |
| noctis | 10.0 [6.2, 15.6] | 160 | 0.53 | 0.24 | 29% | 2% | 34% | 17% | 0.62 | 1.28 | 2.2 | 2.4 | 6% | longbowx138, ruby_crystalx99, ionian_charmx88 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [46.5, 53.5] | 1.14 |
| Jungle | 50.0 [46.5, 53.5] | 1.04 |
| Mid | 50.0 [46.5, 53.5] | 5.58 |
| Support | 50.0 [46.5, 53.5] | 1.67 |
| Top | 50.0 [46.5, 53.5] | 1.70 |

## 5. Games

- length: median 12.0, p10 9, p90 16
- end reasons: {'nexus': 395, 'round_limit_towers': 2, 'round_limit_hp': 3} (draws 0)
- priority win rate: 58.5% [53.6, 63.2]
- north win rate: 50.5% [45.6, 55.4]
- length histogram: {7: 3, 8: 19, 9: 45, 10: 76, 11: 52, 12: 52, 13: 41, 14: 35, 15: 23, 16: 16, 17: 15, 18: 10, 19: 4, 20: 9}

## 6. Objectives

- takes per game: {'dragon': 1.785, 'baron': 0.815}
- median round taken: dragon 6.0, baron 10.0
- win rate when secured: {'dragon': 55.04201680672269, 'baron': 62.576687116564415}
- camp clears per game: {'wolves': 7.5475, 'raptors': 7.985, 'krugs': 8.0925, 'red_buff': 4.65, 'blue_buff': 4.56, 'dragon': 1.785, 'baron': 0.815}

## 7. Structures

- first tower falls: median round 3.0, p10 1, p90 4
- games with at least one tower down: 100.0%
- first-tower win rate: 68.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.99 |
| base | 3.39 |
| chips_wave | 3.37 |
| chips_structure | 3.26 |
| champion_kill | 0.45 |
| blue_buff | 0.37 |
| red_buff | 0.22 |

| use | AP |
|---|---|
| shop | 10.69 |
| abilities | 3.20 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.73 | 73.0% | 10.5% | +62.6 |
| cloth_armor | 5 | 1.59 | 73.7% | 31.9% | +41.8 |
| control_ward | 2 | 0.31 | - | 50.0% | - |
| frost_charm | 2 | 0.18 | - | 50.0% | - |
| health_potion | 2 | 1.80 | - | 50.0% | - |
| ionian_charm | 8 | 1.63 | 77.2% | 16.9% | +60.3 |
| long_sword | 6 | 1.96 | 58.3% | 32.0% | +26.3 |
| longbow | 6 | 1.96 | 54.0% | 45.0% | +9.0 |
| ruby_crystal | 4 | 2.00 | 55.7% | 0.2% | +55.4 |
| stopwatch | 3 | 1.84 | - | 50.0% | - |
| swift_tonic | 1 | 1.90 | - | 50.0% | - |
| vampiric_blade | 5 | 1.62 | 69.9% | 28.5% | +41.4 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: quillan** - 11.03 AP/round = 4.89x roster mean
2. **champion win rate: quillan** - WR 90.6% [85.3, 94.1]
3. **champion win rate: noctis** - WR 10.0% [6.2, 15.6]
4. **economy outlier: sable** - 7.11 AP/round = 3.15x roster mean
5. **economy outlier: ashwyn** - 6.67 AP/round = 2.96x roster mean
