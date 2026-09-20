# Sim report batch_0010

## 1. Header

| field | value |
|---|---|
| rules | 1.1.0 |
| roster | 1.1.0 |
| ai | 1.2.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 300 |
| seed | 990010 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 9962.1s |
| engine tests | 102 passed in 114.38s (0:01:54) |
| generated | 2026-09-20 10:02:56 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 3 FAIL / 22 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 18.5%; 11 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 49.3% [43.7, 55.0] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 20.0 [20.0, 20.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 20.3% [16.2, 25.2] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable (roster mean 1.57 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 31.9% [26.8, 37.4] | **FAIL** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 73.9 [65.4, 81.0] | 119 | 5.43 | 3.46 | 13% | 13% | 0% | 72% | 0.07 | 0.17 | 0.3 | 3.9 | 39% | ionian_charmx120, long_swordx120, longbowx120 |
| ossuar | 64.9 [55.8, 73.1] | 114 | 1.90 | 1.21 | 7% | 3% | 0% | 77% | 0.03 | 0.08 | 0.2 | 7.2 | 16% | cloth_armorx116, long_swordx116, ruby_crystalx116 |
| ashwyn | 64.4 [54.9, 73.0] | 104 | 3.92 | 2.50 | 3% | 59% | 0% | 31% | 0.10 | 0.25 | 0.5 | 1.7 | 32% | longbowx106, ionian_charmx105, long_swordx105 |
| wisp | 62.5 [53.9, 70.4] | 128 | 2.00 | 1.28 | 23% | 32% | 0% | 40% | 0.05 | 0.19 | 0.4 | 4.4 | 16% | longbowx128, ruby_crystalx128, bootsx126 |
| kestrel | 57.8 [48.1, 67.0] | 102 | 1.49 | 0.95 | 9% | 43% | 0% | 29% | 0.07 | 0.21 | 0.4 | 6.0 | 13% | long_swordx102, longbowx101, vampiric_bladex100 |
| sylphine | 55.0 [44.1, 65.4] | 80 | 1.01 | 0.65 | 39% | 2% | 0% | 13% | 0.09 | 0.17 | 0.4 | 1.9 | 9% | long_swordx82, ruby_crystalx82, vampiric_bladex81 |
| pallas | 54.7 [45.7, 63.4] | 117 | 1.18 | 0.75 | 24% | 0% | 0% | 50% | 0.08 | 0.19 | 0.4 | 3.9 | 10% | longbowx118, ruby_crystalx118, bootsx117 |
| kaelis | 53.1 [44.5, 61.4] | 130 | 1.20 | 0.77 | 30% | 0% | 2% | 14% | 0.10 | 0.07 | 0.2 | 2.0 | 10% | long_swordx132, ruby_crystalx132, cloth_armorx131 |
| sable | 50.8 [42.2, 59.4] | 126 | 3.36 | 2.14 | 7% | 15% | 0% | 62% | 0.05 | 0.08 | 0.2 | 4.2 | 28% | longbowx126, ruby_crystalx125, ionian_charmx123 |
| brixa | 50.4 [42.0, 58.7] | 135 | 1.21 | 0.77 | 16% | 2% | 3% | 32% | 0.22 | 0.19 | 0.3 | 4.6 | 11% | long_swordx136, longbowx136, vampiric_bladex136 |
| bramblehide | 50.0 [41.3, 58.7] | 122 | 1.44 | 0.92 | 0% | 15% | 0% | 23% | 0.15 | 0.15 | 0.4 | 2.3 | 12% | bootsx122, long_swordx122, ruby_crystalx122 |
| rictus | 50.0 [42.0, 58.0] | 148 | 1.12 | 0.72 | 31% | 1% | 15% | 6% | 0.17 | 0.24 | 0.4 | 1.9 | 10% | long_swordx148, ruby_crystalx148, vampiric_bladex144 |
| thornjaw | 50.0 [41.3, 58.7] | 122 | 1.15 | 0.73 | 38% | 0% | 3% | 1% | 0.13 | 0.10 | 0.2 | 0.6 | 10% | ruby_crystalx122, long_swordx121, vampiric_bladex120 |
| dax | 48.9 [40.6, 57.2] | 135 | 1.37 | 0.87 | 16% | 20% | 0% | 35% | 0.19 | 0.16 | 0.3 | 4.2 | 12% | long_swordx136, longbowx135, ruby_crystalx135 |
| veyra | 48.7 [39.8, 57.7] | 115 | 1.16 | 0.74 | 8% | 22% | 0% | 34% | 0.18 | 0.36 | 0.7 | 7.2 | 10% | long_swordx116, longbowx115, vampiric_bladex112 |
| lumen | 48.7 [39.7, 57.8] | 113 | 0.61 | 0.39 | 50% | 0% | 0% | 1% | 0.08 | 0.02 | 0.0 | 0.2 | 5% | bootsx114, longbowx114, ruby_crystalx114 |
| vurmak | 48.0 [38.6, 57.6] | 102 | 1.55 | 0.99 | 6% | 2% | 0% | 53% | 0.26 | 0.02 | 0.1 | 6.0 | 13% | long_swordx102, ruby_crystalx102, cloth_armorx101 |
| vellum | 47.7 [38.4, 57.0] | 107 | 2.04 | 1.30 | 8% | 0% | 0% | 75% | 0.06 | 0.16 | 0.3 | 4.7 | 20% | longbowx108, ionian_charmx106, ruby_crystalx106 |
| mossgrove | 46.8 [38.2, 55.5] | 124 | 1.00 | 0.64 | 15% | 1% | 0% | 13% | 0.16 | 0.06 | 0.2 | 5.0 | 9% | long_swordx126, ruby_crystalx126, vampiric_bladex122 |
| orrin | 45.0 [35.9, 54.3] | 109 | 0.85 | 0.54 | 16% | 31% | 0% | 2% | 0.08 | 0.28 | 0.5 | 3.9 | 8% | long_swordx110, longbowx110, vampiric_bladex109 |
| bastion | 43.2 [35.0, 51.7] | 132 | 0.91 | 0.58 | 10% | 0% | 0% | 6% | 0.04 | 0.08 | 0.2 | 1.9 | 8% | cloth_armorx132, ruby_crystalx132, long_swordx130 |
| corvane | 43.1 [34.5, 52.2] | 116 | 0.40 | 0.25 | 36% | 0% | 0% | 1% | 0.09 | 0.19 | 0.4 | 3.6 | 4% | longbowx116, ruby_crystalx116, bootsx115 |
| marrow | 41.5 [33.0, 50.5] | 118 | 0.81 | 0.51 | 9% | 0% | 0% | 5% | 0.03 | 0.02 | 0.0 | 0.6 | 7% | ruby_crystalx118, long_swordx117, cloth_armorx115 |
| grivven | 40.2 [31.9, 49.0] | 122 | 0.97 | 0.62 | 14% | 0% | 0% | 33% | 0.03 | 0.17 | 0.4 | 7.8 | 9% | bootsx124, longbowx124, ruby_crystalx124 |
| noctis | 20.0 [14.2, 27.4] | 140 | 1.11 | 0.71 | 39% | 0% | 36% | 2% | 0.20 | 0.13 | 0.3 | 0.4 | 12% | longbowx140, ruby_crystalx139, ionian_charmx138 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [46.0, 54.0] | 1.22 |
| Jungle | 50.0 [46.0, 54.0] | 1.15 |
| Mid | 50.0 [46.0, 54.0] | 3.11 |
| Support | 50.0 [46.0, 54.0] | 1.05 |
| Top | 50.0 [46.0, 54.0] | 1.25 |

## 5. Games

- length: median 20.0, p10 18, p90 20
- end reasons: {'round_limit_towers': 183, 'nexus': 61, 'round_limit_hp': 53, 'round_limit_kills': 1, 'round_limit_draw': 2} (draws 2)
- priority win rate: 49.3% [43.7, 55.0]
- north win rate: 31.9% [26.8, 37.4]
- length histogram: {10: 1, 14: 6, 15: 5, 16: 7, 17: 7, 18: 6, 19: 11, 20: 257}

## 6. Objectives

- takes per game: {'dragon': 2.96, 'baron': 1.6966666666666668}
- median round taken: dragon 12.0, baron 14
- win rate when secured: {'dragon': 54.42176870748299, 'baron': 52.76679841897233}
- camp clears per game: {'wolves': 5.626666666666667, 'raptors': 6.91, 'krugs': 6.15, 'dragon': 2.96, 'blue_buff': 5.056666666666667, 'red_buff': 5.236666666666666, 'baron': 1.6966666666666668}

## 7. Structures

- first tower falls: median round 6.0, p10 4, p90 10
- games with at least one tower down: 100.0%
- first-tower win rate: 66.4%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.67 |
| base | 3.58 |
| chips_wave | 2.44 |
| chips_structure | 1.51 |
| blue_buff | 0.25 |
| red_buff | 0.18 |
| champion_kill | 0.04 |

| use | AP |
|---|---|
| shop | 8.67 |
| abilities | 2.51 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.99 | 54.1% | 25.0% | +29.1 |
| cloth_armor | 5 | 1.98 | 55.7% | 41.4% | +14.3 |
| control_ward | 2 | 1.09 | - | 50.0% | - |
| frost_charm | 2 | 0.77 | - | 50.0% | - |
| health_potion | 2 | 1.98 | - | 50.0% | - |
| ionian_charm | 8 | 1.97 | 56.4% | 28.9% | +27.5 |
| long_sword | 6 | 2.00 | 50.9% | 46.8% | +4.1 |
| longbow | 6 | 2.00 | 50.1% | 49.9% | +0.2 |
| ruby_crystal | 4 | 2.00 | 50.4% | 7.4% | +43.0 |
| stopwatch | 3 | 1.97 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 1.97 | 53.0% | 43.2% | +9.8 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: quillan** - 5.43 AP/round = 3.46x roster mean
2. **champion win rate: noctis** - WR 20.0% [14.2, 27.4]
3. **Median game length 13-18 rounds** - 20.0 [20.0, 20.0]
4. **>=95% of games end by Nexus kill before round 20** - 20.3% [16.2, 25.2]
5. **North vs South win rate 48-52%** - north 31.9% [26.8, 37.4]

## 12. Delta vs batch_0009

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +3.6 | -2.54 | no |
| bastion | -5.4 | -0.90 | no |
| bramblehide | -10.4 | -1.68 | no |
| brixa | +2.8 | +0.11 | no |
| corvane | +9.5 | +0.21 | no |
| dax | -4.1 | +0.19 | no |
| grivven | -7.8 | -0.76 | no |
| kaelis | +6.3 | +0.23 | no |
| kestrel | +10.2 | -0.28 | no |
| lumen | +4.8 | +0.01 | no |
| marrow | -3.2 | -0.44 | no |
| mossgrove | -5.8 | +0.32 | no |
| noctis | +13.3 | +0.46 | yes |
| orrin | -1.1 | -0.06 | no |
| ossuar | -4.2 | -2.60 | no |
| pallas | -3.0 | -1.92 | no |
| quillan | -9.4 | -5.57 | no |
| rictus | -1.2 | +0.45 | no |
| sable | -17.3 | -4.49 | yes |
| sylphine | +0.7 | +0.23 | no |
| thornjaw | +17.3 | +0.40 | no |
| vellum | +21.1 | -0.54 | yes |
| veyra | -7.5 | -0.01 | no |
| vurmak | +7.1 | +0.40 | no |
| wisp | -1.5 | -1.02 | no |

- median length delta: +9.0
- nexus-kill rate delta: -79.7 pts
