# Sim report batch_0042

## 1. Header

| field | value |
|---|---|
| rules | 1.7.0 |
| roster | 1.6.0 |
| ai | 1.4.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 480 |
| seed | 4201 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 12531.4s |
| engine tests | not run |
| generated | 2026-09-24 02:58:25 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 7 FAIL / 18 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 50/58 abilities outside the band; roster mean 19.7%; 10 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 50.0% [45.5, 54.5] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 15.0 [15.0, 16.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 99.4% [98.2, 99.8] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.18 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 49.6% [45.1, 54.0] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 76.6 [70.5, 81.8] | 214 | 5.01 | 2.30 | 4% | 82% | 0% | 8% | 0.19 | 0.58 | 1.6 | 0.0 | 29% | bootsx214, longbowx214, ruby_crystalx214 |
| bastion | 75.0 [68.4, 80.6] | 192 | 2.34 | 1.08 | 89% | 0% | 0% | 2% | 0.33 | 0.24 | 0.7 | 0.3 | 16% | cloth_armorx192, long_swordx192, ruby_crystalx192 |
| ashwyn | 60.8 [53.6, 67.5] | 186 | 4.66 | 2.14 | 3% | 68% | 0% | 20% | 0.18 | 0.81 | 2.2 | 0.0 | 29% | ionian_charmx186, longbowx186, ruby_crystalx186 |
| sylphine | 58.9 [51.8, 65.6] | 192 | 1.34 | 0.62 | 13% | 1% | 0% | 14% | 0.30 | 0.28 | 0.9 | 0.0 | 9% | long_swordx192, ruby_crystalx192, vampiric_bladex190 |
| sable | 58.3 [50.5, 65.8] | 156 | 5.53 | 2.54 | 3% | 50% | 0% | 38% | 0.22 | 0.25 | 0.7 | 1.2 | 33% | ionian_charmx156, long_swordx156, longbowx156 |
| pallas | 57.9 [50.5, 64.9] | 178 | 3.66 | 1.68 | 4% | 0% | 1% | 89% | 0.10 | 0.57 | 1.6 | 4.7 | 23% | bootsx178, longbowx178, ruby_crystalx178 |
| veyra | 57.8 [50.9, 64.3] | 206 | 1.41 | 0.65 | 3% | 69% | 0% | 8% | 0.26 | 0.55 | 1.6 | 1.4 | 10% | long_swordx206, longbowx206, vampiric_bladex204 |
| thornjaw | 54.0 [46.6, 61.2] | 176 | 1.30 | 0.60 | 13% | 8% | 2% | 3% | 0.22 | 0.36 | 1.1 | 0.2 | 9% | long_swordx176, ruby_crystalx176, vampiric_bladex168 |
| noctis | 53.8 [47.1, 60.5] | 208 | 1.47 | 0.67 | 66% | 1% | 21% | 1% | 0.31 | 0.81 | 2.3 | 0.2 | 12% | longbowx208, ionian_charmx207, ruby_crystalx202 |
| kestrel | 53.6 [46.0, 60.9] | 168 | 1.74 | 0.80 | 55% | 15% | 0% | 19% | 0.33 | 0.27 | 0.8 | 3.3 | 12% | long_swordx168, longbowx168, vampiric_bladex166 |
| bramblehide | 51.3 [43.4, 59.1] | 152 | 1.73 | 0.79 | 4% | 28% | 1% | 23% | 0.24 | 0.32 | 0.9 | 3.6 | 12% | long_swordx152, ruby_crystalx152, vampiric_bladex152 |
| rictus | 50.5 [43.9, 57.0] | 220 | 1.14 | 0.52 | 13% | 6% | 30% | 2% | 0.27 | 0.76 | 2.1 | 2.3 | 8% | long_swordx220, ruby_crystalx220, vampiric_bladex217 |
| dax | 50.0 [43.1, 56.9] | 196 | 1.36 | 0.62 | 10% | 43% | 3% | 15% | 0.28 | 0.48 | 1.4 | 1.7 | 9% | long_swordx196, longbowx196, vampiric_bladex194 |
| brixa | 48.5 [41.5, 55.4] | 194 | 1.40 | 0.65 | 41% | 4% | 7% | 2% | 0.30 | 0.52 | 1.5 | 0.7 | 10% | long_swordx194, longbowx194, vampiric_bladex193 |
| marrow | 48.3 [41.1, 55.6] | 180 | 2.30 | 1.05 | 9% | 1% | 0% | 38% | 0.17 | 0.19 | 0.6 | 0.0 | 16% | long_swordx180, ruby_crystalx180, cloth_armorx179 |
| ossuar | 45.3 [38.3, 52.4] | 190 | 1.97 | 0.91 | 11% | 3% | 0% | 50% | 0.14 | 0.22 | 0.7 | 4.0 | 13% | long_swordx190, ruby_crystalx190, cloth_armorx189 |
| quillan | 45.1 [38.4, 52.0] | 204 | 4.52 | 2.08 | 8% | 9% | 0% | 72% | 0.19 | 0.71 | 2.1 | 0.0 | 29% | ionian_charmx204, longbowx204, ruby_crystalx204 |
| vurmak | 44.3 [37.7, 51.0] | 210 | 1.40 | 0.64 | 16% | 2% | 1% | 56% | 0.19 | 0.60 | 1.8 | 4.1 | 10% | long_swordx210, ruby_crystalx210, cloth_armorx201 |
| grivven | 40.8 [34.3, 47.6] | 206 | 2.35 | 1.08 | 5% | 1% | 2% | 66% | 0.08 | 0.41 | 1.3 | 7.5 | 16% | longbowx206, ruby_crystalx206, bootsx205 |
| orrin | 40.3 [33.7, 47.3] | 196 | 1.61 | 0.74 | 9% | 31% | 1% | 1% | 0.24 | 0.45 | 1.3 | 0.1 | 11% | long_swordx196, longbowx194, vampiric_bladex192 |
| mossgrove | 37.7 [31.6, 44.3] | 220 | 1.14 | 0.52 | 34% | 2% | 1% | 8% | 0.22 | 0.47 | 1.4 | 3.6 | 8% | long_swordx220, ruby_crystalx220, vampiric_bladex217 |
| kaelis | 37.2 [30.6, 44.3] | 188 | 1.19 | 0.55 | 23% | 6% | 2% | 14% | 0.19 | 0.53 | 1.5 | 1.4 | 9% | ruby_crystalx188, long_swordx187, cloth_armorx185 |
| lumen | 36.1 [29.0, 43.8] | 158 | 0.82 | 0.38 | 70% | 0% | 0% | 1% | 0.19 | 0.30 | 0.9 | 0.1 | 6% | longbowx158, ruby_crystalx158, bootsx155 |
| corvane | 35.3 [29.1, 42.1] | 204 | 0.49 | 0.22 | 45% | 0% | 1% | 4% | 0.24 | 0.64 | 2.0 | 3.7 | 4% | longbowx204, ruby_crystalx204, bootsx203 |
| vellum | 35.0 [28.8, 41.7] | 206 | 2.53 | 1.16 | 5% | 0% | 1% | 80% | 0.17 | 0.62 | 1.9 | 3.1 | 19% | longbowx206, ionian_charmx202, ruby_crystalx200 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [46.8, 53.2] | 1.50 |
| Jungle | 50.0 [46.8, 53.2] | 1.30 |
| Mid | 50.0 [46.8, 53.2] | 3.62 |
| Support | 50.0 [46.8, 53.2] | 2.54 |
| Top | 50.0 [46.8, 53.2] | 1.83 |

## 5. Games

- length: median 15.0, p10 12, p90 18
- end reasons: {'nexus': 477, 'round_limit_towers': 2, 'round_limit_hp': 1} (draws 0)
- priority win rate: 50.0% [45.5, 54.5]
- north win rate: 49.6% [45.1, 54.0]
- length histogram: {8: 2, 9: 2, 10: 10, 11: 18, 12: 27, 13: 56, 14: 68, 15: 77, 16: 75, 17: 64, 18: 39, 19: 30, 20: 12}

## 6. Objectives

- takes per game: {'dragon': 1.6, 'baron': 0.55}
- median round taken: dragon 8.0, baron 12.0
- win rate when secured: {'dragon': 46.875, 'baron': 40.15151515151515}
- camp clears per game: {'red_buff': 3.3291666666666666, 'krugs': 5.660416666666666, 'blue_buff': 3.347916666666667, 'wolves': 5.835416666666666, 'raptors': 5.966666666666667, 'dragon': 1.6, 'baron': 0.55}

## 7. Structures

- first tower falls: median round 7.0, p10 5, p90 9
- games with at least one tower down: 100.0%
- first-tower win rate: 73.8%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 4.25 |
| chips_monster | 3.55 |
| base | 3.35 |
| chips_wave | 2.80 |
| champion_kill | 0.46 |
| blue_buff | 0.22 |
| red_buff | 0.15 |

| use | AP |
|---|---|
| shop | 11.17 |
| abilities | 2.32 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.99 | 54.4% | 22.5% | +31.9 |
| cloth_armor | 5 | 1.97 | 55.6% | 40.5% | +15.1 |
| control_ward | 2 | 0.97 | - | 50.0% | - |
| frost_charm | 2 | 0.75 | - | 50.0% | - |
| health_potion | 2 | 1.94 | - | 50.0% | - |
| ionian_charm | 8 | 1.99 | 56.3% | 24.9% | +31.5 |
| long_sword | 6 | 2.00 | 50.7% | 47.3% | +3.5 |
| longbow | 6 | 2.00 | 50.0% | 49.9% | +0.1 |
| ruby_crystal | 4 | 2.00 | 50.4% | 11.1% | +39.3 |
| stopwatch | 3 | 1.94 | - | 50.0% | - |
| swift_tonic | 1 | 1.98 | - | 50.0% | - |
| vampiric_blade | 5 | 1.98 | 52.9% | 43.1% | +9.8 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 | 62 | 64.5 [52.1, 75.3] |
| SM_g2_clock3_short | 78 | 64.1 [53.0, 73.9] |
| SM_g1_clock2 | 80 | 61.3 [50.3, 71.2] |
| SM_g1_clock3 | 74 | 60.8 [49.4, 71.1] |
| SM_g2_lane_map | 56 | 57.1 [44.1, 69.2] |
| SM_g2_lane5 | 56 | 53.6 [40.7, 66.0] |
| T2_sieger | 128 | 50.0 [41.5, 58.5] |
| SM_g2_lane_ap | 80 | 48.8 [38.1, 59.5] |
| SM_g2_lane3 | 70 | 47.1 [35.9, 58.7] |
| SM_g2_siege_guard | 82 | 43.9 [33.7, 54.7] |
| T2_search | 118 | 35.6 [27.5, 44.6] |
| SM_g2_brawl_open | 76 | 26.3 [17.7, 37.2] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] | vs T2_sieger | vs T2_search | state occupancy | switches/game |
|---|---|---|---|---|---|---|
| SM_g2_clock3_short | 78 | 64.1 [53.0, 73.9] | 67% (18) | 86% (14) | sieger 60%, laner 26%, objective 13% | 2.0 |
| SM_g2_lane6 | 62 | 64.5 [52.1, 75.3] | 25% (12) | 70% (10) | sieger 66%, laner 34% | 1.0 |
| SM_g1_clock2 | 80 | 61.3 [50.3, 71.2] | 45% (20) | 100% (14) | sieger 79%, laner 21% | 1.0 |
| SM_g1_clock3 | 74 | 60.8 [49.4, 71.1] | 40% (10) | 73% (22) | sieger 48%, laner 26%, objective 26% | 2.0 |
| SM_g2_lane_map | 56 | 57.1 [44.1, 69.2] | 83% (6) | 42% (12) | sieger 60%, laner 20%, warder 20% | 1.8 |
| T2_sieger | 128 | 50.0 [41.5, 58.5] | - | - | - | - |
| SM_g2_lane5 | 56 | 53.6 [40.7, 66.0] | 100% (2) | 75% (8) | sieger 74%, laner 26% | 1.0 |
| SM_g2_lane_ap | 80 | 48.8 [38.1, 59.5] | 80% (10) | 21% (14) | sieger 50%, objective 31%, laner 20% | 2.2 |
| SM_g2_lane3 | 70 | 47.1 [35.9, 58.7] | 67% (12) | 88% (8) | sieger 87%, laner 13% | 1.0 |
| SM_g2_siege_guard | 82 | 43.9 [33.7, 54.7] | 45% (22) | 67% (6) | sieger 87%, warder 13% | 1.5 |
| T2_search | 118 | 35.6 [27.5, 44.6] | - | - | - | - |
| SM_g2_brawl_open | 76 | 26.3 [17.7, 37.2] | 19% (16) | 20% (10) | sieger 60%, brawler 40% | 2.4 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 46.49 per game
- that is 41.0% of all ability uses
- of which true snipes (from cover, two or more hexes away): 37.7% of all uses
- snipes aimed at a champion: 7.6 per game
- activations ending beside an enemy-held hexgroup (looking in): 64.6%


## 10. Anomalies

- ILLEGAL[activation r13]: stacking: n_mid_T2 and w23 on: 1 games
- ILLEGAL[world r13]: stacking: n_mid_T2 and w23 on: 1 games
- ILLEGAL[upkeep r14]: stacking: n_mid_T2 and w23 on: 1 games
- ILLEGAL[activation r14]: stacking: n_mid_T2 and w23 on: 1 games
- ILLEGAL[world r14]: stacking: n_mid_T2 and w23 on: 1 games
- ILLEGAL[upkeep r15]: stacking: n_mid_T2 and w23 on: 1 games
- ILLEGAL[activation r15]: stacking: n_mid_T2 and w23 on: 1 games

## 11. Top 5 flags (evidence only)

1. **anomaly: ILLEGAL[activation r13]: stacking: n_mid_T2 and w23 on** - 1 games
2. **anomaly: ILLEGAL[world r13]: stacking: n_mid_T2 and w23 on** - 1 games
3. **anomaly: ILLEGAL[upkeep r14]: stacking: n_mid_T2 and w23 on** - 1 games
4. **anomaly: ILLEGAL[activation r14]: stacking: n_mid_T2 and w23 on** - 1 games
5. **anomaly: ILLEGAL[world r14]: stacking: n_mid_T2 and w23 on** - 1 games
