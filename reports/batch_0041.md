# Sim report batch_0041

## 1. Header

| field | value |
|---|---|
| rules | 1.7.0 |
| roster | 1.6.0 |
| ai | 1.4.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 400 |
| seed | 4101 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 11583.9s |
| engine tests | not run |
| generated | 2026-09-23 23:24:39 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 6 FAIL / 19 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 19.8%; 12 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 45.5% [40.7, 50.4] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 17.0 [16.0, 17.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 92.5% [89.5, 94.7] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.25 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 47.5% [42.7, 52.4] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 78.5 [70.6, 84.7] | 130 | 5.00 | 2.23 | 3% | 84% | 0% | 7% | 0.13 | 0.50 | 1.4 | 0.0 | 28% | bootsx130, cloth_armorx130, longbowx130 |
| bastion | 71.3 [64.0, 77.7] | 164 | 2.38 | 1.06 | 90% | 0% | 0% | 2% | 0.35 | 0.25 | 0.8 | 0.4 | 16% | cloth_armorx164, long_swordx164, ruby_crystalx164 |
| pallas | 62.9 [55.9, 69.4] | 194 | 3.82 | 1.70 | 5% | 0% | 1% | 90% | 0.10 | 0.57 | 1.7 | 4.8 | 24% | longbowx194, ruby_crystalx194, bootsx193 |
| marrow | 59.0 [51.1, 66.4] | 156 | 2.30 | 1.02 | 8% | 1% | 0% | 35% | 0.28 | 0.11 | 0.4 | 0.0 | 15% | cloth_armorx156, long_swordx156, ruby_crystalx156 |
| sable | 58.7 [50.0, 66.9] | 126 | 5.51 | 2.45 | 3% | 54% | 0% | 37% | 0.14 | 0.27 | 0.7 | 1.3 | 33% | ionian_charmx126, longbowx126, ruby_crystalx126 |
| rictus | 57.1 [49.5, 64.3] | 170 | 1.19 | 0.53 | 14% | 6% | 30% | 1% | 0.27 | 0.82 | 2.4 | 2.3 | 8% | long_swordx170, ruby_crystalx170, vampiric_bladex169 |
| kestrel | 56.8 [49.1, 64.2] | 162 | 1.76 | 0.78 | 56% | 13% | 0% | 23% | 0.20 | 0.31 | 1.0 | 4.2 | 12% | long_swordx162, longbowx162, vampiric_bladex162 |
| ashwyn | 54.0 [46.6, 61.2] | 176 | 4.70 | 2.09 | 2% | 72% | 0% | 18% | 0.20 | 0.82 | 2.5 | 0.0 | 29% | bootsx176, ionian_charmx176, long_swordx176 |
| veyra | 52.0 [44.1, 59.8] | 152 | 1.52 | 0.68 | 1% | 75% | 0% | 7% | 0.18 | 0.43 | 1.2 | 1.4 | 10% | long_swordx152, longbowx152, vampiric_bladex151 |
| quillan | 51.2 [43.6, 58.8] | 164 | 4.70 | 2.09 | 7% | 9% | 0% | 75% | 0.19 | 0.62 | 2.0 | 0.0 | 29% | ionian_charmx164, longbowx164, ruby_crystalx164 |
| thornjaw | 51.2 [43.7, 58.6] | 168 | 1.38 | 0.61 | 11% | 7% | 3% | 3% | 0.26 | 0.29 | 0.8 | 0.2 | 9% | long_swordx168, ruby_crystalx168, vampiric_bladex167 |
| noctis | 50.6 [43.0, 58.2] | 162 | 1.54 | 0.68 | 73% | 0% | 16% | 1% | 0.32 | 0.69 | 2.0 | 0.1 | 12% | ionian_charmx162, longbowx162, ruby_crystalx161 |
| grivven | 49.5 [42.4, 56.6] | 186 | 2.40 | 1.07 | 4% | 1% | 2% | 71% | 0.06 | 0.44 | 1.5 | 8.2 | 16% | bootsx186, longbowx186, ruby_crystalx186 |
| brixa | 49.4 [41.7, 57.1] | 158 | 1.44 | 0.64 | 41% | 3% | 8% | 2% | 0.29 | 0.37 | 1.0 | 0.8 | 10% | long_swordx158, longbowx158, vampiric_bladex158 |
| dax | 48.8 [41.4, 56.3] | 170 | 1.43 | 0.64 | 11% | 45% | 2% | 12% | 0.28 | 0.35 | 1.0 | 1.4 | 10% | long_swordx170, longbowx170, vampiric_bladex170 |
| mossgrove | 48.7 [40.9, 56.6] | 152 | 1.21 | 0.54 | 34% | 1% | 1% | 7% | 0.22 | 0.41 | 1.3 | 3.6 | 8% | long_swordx152, ruby_crystalx152, vampiric_bladex151 |
| bramblehide | 48.2 [40.8, 55.7] | 168 | 1.82 | 0.81 | 3% | 29% | 0% | 24% | 0.15 | 0.26 | 0.8 | 3.6 | 12% | long_swordx168, ruby_crystalx168, vampiric_bladex168 |
| vurmak | 47.9 [39.8, 56.1] | 142 | 1.50 | 0.67 | 15% | 3% | 1% | 57% | 0.32 | 0.44 | 1.4 | 4.3 | 10% | long_swordx142, ruby_crystalx142, cloth_armorx141 |
| sylphine | 43.7 [35.8, 51.9] | 142 | 1.38 | 0.62 | 14% | 1% | 0% | 9% | 0.24 | 0.20 | 0.6 | 0.0 | 9% | long_swordx142, ruby_crystalx142, vampiric_bladex141 |
| orrin | 43.0 [35.6, 50.8] | 158 | 1.68 | 0.75 | 9% | 36% | 1% | 1% | 0.28 | 0.37 | 1.1 | 0.1 | 11% | long_swordx158, longbowx158, vampiric_bladex157 |
| kaelis | 38.5 [31.9, 45.6] | 192 | 1.26 | 0.56 | 23% | 5% | 3% | 13% | 0.27 | 0.29 | 0.8 | 1.2 | 9% | long_swordx192, ruby_crystalx192, cloth_armorx191 |
| vellum | 37.8 [30.9, 45.2] | 172 | 2.72 | 1.21 | 3% | 0% | 1% | 83% | 0.13 | 0.66 | 2.0 | 3.1 | 20% | ionian_charmx172, longbowx172, ruby_crystalx170 |
| ossuar | 33.6 [26.4, 41.6] | 146 | 2.20 | 0.98 | 8% | 3% | 0% | 59% | 0.06 | 0.17 | 0.5 | 4.5 | 15% | long_swordx146, ruby_crystalx146, cloth_armorx144 |
| lumen | 31.8 [25.0, 39.5] | 154 | 0.83 | 0.37 | 70% | 0% | 0% | 1% | 0.16 | 0.23 | 0.8 | 0.1 | 6% | bootsx154, longbowx154, ruby_crystalx154 |
| corvane | 25.7 [19.1, 33.7] | 136 | 0.50 | 0.22 | 51% | 0% | 1% | 3% | 0.23 | 0.53 | 1.6 | 4.0 | 4% | bootsx136, longbowx136, ruby_crystalx136 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [46.5, 53.5] | 1.57 |
| Jungle | 50.0 [46.5, 53.5] | 1.40 |
| Mid | 50.0 [46.5, 53.5] | 3.76 |
| Support | 50.0 [46.5, 53.5] | 2.54 |
| Top | 50.0 [46.5, 53.5] | 1.91 |

## 5. Games

- length: median 17.0, p10 13, p90 20
- end reasons: {'nexus': 370, 'round_limit_towers': 21, 'round_limit_hp': 9} (draws 0)
- priority win rate: 45.5% [40.7, 50.4]
- north win rate: 47.5% [42.7, 52.4]
- length histogram: {10: 6, 11: 3, 12: 19, 13: 21, 14: 32, 15: 44, 16: 73, 17: 58, 18: 58, 19: 35, 20: 51}

## 6. Objectives

- takes per game: {'dragon': 2.1225, 'baron': 0.9425}
- median round taken: dragon 10, baron 12
- win rate when secured: {'dragon': 45.22968197879859, 'baron': 38.19628647214854}
- camp clears per game: {'wolves': 6.6625, 'blue_buff': 4.0675, 'raptors': 6.8875, 'dragon': 2.1225, 'krugs': 6.5175, 'red_buff': 4.0325, 'baron': 0.9425}

## 7. Structures

- first tower falls: median round 7.0, p10 5, p90 10
- games with at least one tower down: 100.0%
- first-tower win rate: 72.8%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 3.99 |
| chips_monster | 3.89 |
| base | 3.48 |
| chips_wave | 3.13 |
| champion_kill | 0.36 |
| blue_buff | 0.24 |
| red_buff | 0.17 |

| use | AP |
|---|---|
| shop | 11.05 |
| abilities | 2.38 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 52.4% | 23.4% | +29.0 |
| cloth_armor | 5 | 1.99 | 53.4% | 42.6% | +10.8 |
| control_ward | 2 | 1.31 | - | 50.0% | - |
| frost_charm | 2 | 1.12 | - | 50.0% | - |
| health_potion | 2 | 1.97 | - | 50.0% | - |
| ionian_charm | 8 | 2.00 | 53.1% | 28.9% | +24.2 |
| long_sword | 6 | 2.00 | 50.4% | 48.5% | +1.9 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 50.2% | 11.1% | +39.1 |
| stopwatch | 3 | 1.95 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 51.4% | 45.8% | +5.7 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g1_clock3 | 60 | 66.7 [54.1, 77.3] |
| SM_g1_clock2 | 82 | 61.0 [50.2, 70.8] |
| SM_g1_ap_lead | 72 | 59.7 [48.2, 70.3] |
| T2_sieger | 68 | 57.4 [45.5, 68.4] |
| SM_g1_map_commit | 78 | 52.6 [41.6, 63.3] |
| SM_g1_fight | 82 | 50.0 [39.4, 60.6] |
| SM_g1_map | 106 | 45.3 [36.1, 54.8] |
| SM_g1_objective_window | 86 | 40.7 [30.9, 51.3] |
| T2_search | 88 | 38.6 [29.1, 49.1] |
| SM_g1_full | 78 | 37.2 [27.3, 48.3] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] | vs T2_search | vs T2_sieger | state occupancy | switches/game |
|---|---|---|---|---|---|---|
| SM_g1_clock3 | 60 | 66.7 [54.1, 77.3] | 67% (6) | 50% (2) | sieger 48%, laner 26%, objective 26% | 2.0 |
| SM_g1_clock2 | 82 | 61.0 [50.2, 70.8] | 71% (14) | 25% (8) | sieger 81%, laner 19% | 1.0 |
| SM_g1_ap_lead | 72 | 59.7 [48.2, 70.3] | 50% (12) | 58% (12) | sieger 43%, objective 42%, laner 15% | 3.8 |
| T2_sieger | 68 | 57.4 [45.5, 68.4] | 62% (8) | - | - | - |
| SM_g1_map_commit | 78 | 52.6 [41.6, 63.3] | 80% (10) | 75% (4) | laner 59%, sieger 22%, warder 19% | 1.9 |
| SM_g1_fight | 82 | 50.0 [39.4, 60.6] | 80% (10) | 43% (14) | laner 60%, brawler 21%, sieger 17%, warder 2% | 3.0 |
| SM_g1_map | 106 | 45.3 [36.1, 54.8] | 25% (4) | 33% (12) | laner 59%, warder 23%, sieger 18% | 2.9 |
| SM_g1_objective_window | 86 | 40.7 [30.9, 51.3] | 50% (14) | - | objective 85%, sieger 15% | 3.2 |
| T2_search | 88 | 38.6 [29.1, 49.1] | - | 38% (8) | - | - |
| SM_g1_full | 78 | 37.2 [27.3, 48.3] | 50% (10) | 38% (8) | objective 74%, laner 16%, sieger 7%, warder 2% | 3.2 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 53.09 per game
- that is 41.7% of all ability uses
- of which true snipes (from cover, two or more hexes away): 38.4% of all uses
- snipes aimed at a champion: 9.7 per game
- activations ending beside an enemy-held hexgroup (looking in): 61.2%


## 10. Anomalies

- ILLEGAL[activation r14]: stacking: n_mid_T2 and w25 on: 1 games
- ILLEGAL[world r14]: stacking: n_mid_T2 and w25 on: 1 games
- ILLEGAL[upkeep r15]: stacking: n_mid_T2 and w25 on: 1 games
- ILLEGAL[activation r15]: stacking: n_mid_T2 and w25 on: 1 games
- ILLEGAL[activation r13]: stacking: s_mid_T2 and w28 on: 1 games
- ILLEGAL[world r13]: stacking: s_mid_T2 and w28 on: 1 games
- ILLEGAL[upkeep r14]: stacking: s_mid_T2 and w28 on: 1 games
- ILLEGAL[activation r14]: stacking: s_mid_T2 and w28 on: 1 games
- ILLEGAL[activation r12]: stacking: w19 and w13 on: 1 games
- ILLEGAL[world r12]: stacking: w19 and w13 on: 1 games

## 11. Top 5 flags (evidence only)

1. **anomaly: ILLEGAL[activation r14]: stacking: n_mid_T2 and w25 on** - 1 games
2. **anomaly: ILLEGAL[world r14]: stacking: n_mid_T2 and w25 on** - 1 games
3. **anomaly: ILLEGAL[upkeep r15]: stacking: n_mid_T2 and w25 on** - 1 games
4. **anomaly: ILLEGAL[activation r15]: stacking: n_mid_T2 and w25 on** - 1 games
5. **anomaly: ILLEGAL[activation r13]: stacking: s_mid_T2 and w28 on** - 1 games
