# Sim report batch_0045

## 1. Header

| field | value |
|---|---|
| rules | 1.7.0 |
| roster | 1.6.0 |
| ai | 1.4.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 560 |
| seed | 4501 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 0.1s |
| engine tests | not run |
| generated | 2026-09-24 14:07:45 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 25 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 50/58 abilities outside the band; roster mean 18.4%; 6 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 48.8% [44.6, 52.9] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 16.0 [16.0, 16.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 89.6% [86.8, 91.9] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 1.82 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 50.2% [46.1, 54.3] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rictus | 60.3 [53.9, 66.4] | 232 | 0.96 | 0.53 | 15% | 11% | 26% | 2% | 0.29 | 0.87 | 2.6 | 2.4 | 7% | ruby_crystalx231, long_swordx228, vampiric_bladex213 |
| wisp | 58.5 [51.9, 64.7] | 224 | 4.47 | 2.45 | 5% | 72% | 2% | 9% | 0.25 | 0.67 | 1.9 | 0.0 | 29% | longbowx224, ruby_crystalx224, bootsx222 |
| marrow | 57.4 [50.9, 63.6] | 230 | 1.70 | 0.94 | 10% | 3% | 4% | 29% | 0.24 | 0.29 | 0.9 | 0.5 | 13% | ruby_crystalx230, long_swordx218, cloth_armorx210 |
| ashwyn | 56.2 [49.9, 62.4] | 240 | 4.28 | 2.35 | 6% | 61% | 2% | 20% | 0.27 | 0.74 | 2.2 | 0.0 | 29% | ruby_crystalx240, longbowx238, ionian_charmx237 |
| sylphine | 56.0 [49.6, 62.3] | 232 | 1.06 | 0.58 | 12% | 3% | 3% | 15% | 0.27 | 0.37 | 1.1 | 0.5 | 8% | ruby_crystalx231, long_swordx226, vampiric_bladex210 |
| bastion | 55.4 [48.6, 62.1] | 202 | 2.04 | 1.12 | 79% | 2% | 1% | 2% | 0.47 | 0.37 | 1.1 | 0.4 | 15% | ruby_crystalx202, long_swordx199, cloth_armorx198 |
| brixa | 53.7 [47.0, 60.2] | 216 | 1.10 | 0.60 | 34% | 8% | 9% | 5% | 0.28 | 0.62 | 1.7 | 1.0 | 9% | long_swordx214, vampiric_bladex205, longbowx196 |
| quillan | 52.4 [45.6, 59.1] | 208 | 4.01 | 2.20 | 11% | 8% | 3% | 61% | 0.26 | 0.73 | 2.2 | 0.0 | 29% | longbowx205, ruby_crystalx203, ionian_charmx201 |
| pallas | 52.2 [45.7, 58.6] | 226 | 3.18 | 1.74 | 9% | 2% | 2% | 75% | 0.14 | 0.67 | 2.0 | 4.5 | 22% | ruby_crystalx225, bootsx222, longbowx222 |
| kestrel | 51.3 [44.9, 57.7] | 232 | 1.46 | 0.80 | 51% | 18% | 3% | 15% | 0.34 | 0.35 | 1.1 | 2.9 | 11% | long_swordx232, longbowx221, vampiric_bladex219 |
| lumen | 50.0 [43.9, 56.1] | 256 | 0.62 | 0.34 | 56% | 3% | 1% | 3% | 0.16 | 0.50 | 1.6 | 0.5 | 6% | ruby_crystalx255, longbowx249, bootsx245 |
| bramblehide | 49.5 [42.9, 56.2] | 212 | 1.46 | 0.80 | 8% | 28% | 2% | 16% | 0.24 | 0.29 | 0.9 | 3.4 | 11% | long_swordx211, ruby_crystalx211, vampiric_bladex207 |
| veyra | 49.1 [42.8, 55.5] | 232 | 1.11 | 0.61 | 7% | 58% | 3% | 10% | 0.37 | 0.54 | 1.6 | 2.0 | 8% | long_swordx225, longbowx221, vampiric_bladex207 |
| orrin | 49.1 [42.6, 55.6] | 224 | 1.19 | 0.65 | 12% | 25% | 6% | 2% | 0.30 | 0.60 | 1.8 | 0.3 | 9% | long_swordx220, vampiric_bladex207, longbowx206 |
| vurmak | 48.6 [42.1, 55.2] | 220 | 1.12 | 0.61 | 18% | 5% | 2% | 42% | 0.39 | 0.52 | 1.7 | 3.8 | 9% | ruby_crystalx220, long_swordx199, cloth_armorx185 |
| vellum | 47.6 [41.0, 54.3] | 212 | 1.89 | 1.04 | 10% | 2% | 8% | 63% | 0.22 | 0.73 | 2.3 | 3.0 | 16% | longbowx188, ruby_crystalx186, ionian_charmx172 |
| sable | 46.8 [40.3, 53.4] | 218 | 4.79 | 2.63 | 8% | 45% | 1% | 33% | 0.20 | 0.26 | 0.8 | 1.3 | 33% | longbowx207, ruby_crystalx204, ionian_charmx201 |
| dax | 46.8 [40.2, 53.4] | 216 | 1.10 | 0.61 | 15% | 36% | 4% | 15% | 0.31 | 0.52 | 1.5 | 2.0 | 9% | long_swordx208, vampiric_bladex206, longbowx199 |
| noctis | 46.7 [40.5, 53.0] | 242 | 1.13 | 0.62 | 60% | 2% | 18% | 3% | 0.37 | 0.74 | 2.2 | 0.7 | 10% | longbowx234, ruby_crystalx227, ionian_charmx206 |
| kaelis | 46.2 [39.9, 52.6] | 236 | 0.90 | 0.50 | 21% | 11% | 4% | 12% | 0.26 | 0.61 | 1.9 | 1.2 | 7% | ruby_crystalx236, cloth_armorx221, long_swordx214 |
| grivven | 46.1 [39.8, 52.5] | 230 | 2.14 | 1.17 | 11% | 7% | 2% | 56% | 0.12 | 0.50 | 1.6 | 7.4 | 17% | longbowx230, ruby_crystalx229, bootsx226 |
| mossgrove | 43.8 [37.5, 50.3] | 226 | 0.82 | 0.45 | 28% | 10% | 2% | 9% | 0.19 | 0.43 | 1.4 | 3.8 | 6% | ruby_crystalx225, long_swordx216, vampiric_bladex190 |
| ossuar | 43.1 [36.9, 49.5] | 232 | 1.63 | 0.90 | 13% | 5% | 3% | 41% | 0.15 | 0.26 | 0.8 | 4.0 | 13% | ruby_crystalx232, long_swordx213, cloth_armorx208 |
| corvane | 41.8 [35.0, 49.1] | 184 | 0.35 | 0.19 | 40% | 2% | 5% | 4% | 0.17 | 0.85 | 2.4 | 4.1 | 3% | ruby_crystalx184, longbowx180, bootsx178 |
| thornjaw | 39.4 [33.2, 46.1] | 218 | 0.99 | 0.54 | 13% | 14% | 5% | 4% | 0.25 | 0.49 | 1.5 | 0.6 | 8% | ruby_crystalx217, long_swordx203, vampiric_bladex194 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [47.1, 52.9] | 1.20 |
| Jungle | 50.0 [47.1, 52.9] | 1.05 |
| Mid | 50.0 [47.1, 52.9] | 3.20 |
| Support | 50.0 [47.1, 52.9] | 2.17 |
| Top | 50.0 [47.1, 52.9] | 1.47 |

## 5. Games

- length: median 16.0, p10 13, p90 20
- end reasons: {'nexus': 502, 'round_limit_towers': 56, 'round_limit_hp': 2} (draws 0)
- priority win rate: 48.8% [44.6, 52.9]
- north win rate: 50.2% [46.1, 54.3]
- length histogram: {9: 2, 10: 5, 11: 16, 12: 23, 13: 48, 14: 75, 15: 77, 16: 60, 17: 60, 18: 54, 19: 52, 20: 88}

## 6. Objectives

- takes per game: {'dragon': 1.6214285714285714, 'baron': 0.6357142857142857}
- median round taken: dragon 9.0, baron 13.0
- win rate when secured: {'dragon': 60.13215859030837, 'baron': 43.82022471910113}
- camp clears per game: {'raptors': 6.007142857142857, 'red_buff': 3.414285714285714, 'wolves': 5.858928571428572, 'krugs': 5.7, 'blue_buff': 3.4571428571428573, 'dragon': 1.6214285714285714, 'baron': 0.6357142857142857}

## 7. Structures

- first tower falls: median round 7.0, p10 5, p90 9
- games with at least one tower down: 100.0%
- first-tower win rate: 94.8%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.40 |
| base | 3.35 |
| chips_structure | 3.03 |
| chips_wave | 2.47 |
| champion_kill | 0.46 |
| blue_buff | 0.21 |
| red_buff | 0.13 |

| use | AP |
|---|---|
| shop | 9.83 |
| abilities | 2.17 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.95 | 58.9% | 14.8% | +44.1 |
| cloth_armor | 5 | 1.82 | 60.4% | 36.7% | +23.6 |
| control_ward | 2 | 0.76 | - | 50.0% | - |
| frost_charm | 2 | 0.64 | - | 50.0% | - |
| health_potion | 2 | 1.96 | - | 50.0% | - |
| ionian_charm | 8 | 1.82 | 62.0% | 21.1% | +41.0 |
| long_sword | 6 | 1.97 | 54.0% | 38.8% | +15.2 |
| longbow | 6 | 1.98 | 52.2% | 47.1% | +5.1 |
| ruby_crystal | 4 | 2.00 | 51.8% | 2.0% | +49.9 |
| stopwatch | 3 | 1.93 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.90 | 57.8% | 35.9% | +21.9 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 | 296 | 97.6 [95.2, 98.8] |
| T2_sieger | 264 | 93.9 [90.4, 96.2] |
| X_exploit_splitpush | 96 | 21.9 [14.8, 31.1] |
| X_exploit_farm | 84 | 2.4 [0.7, 8.3] |
| X_exploit_cdlock | 84 | 0.0 [0.0, 4.4] |
| X_exploit_dive | 72 | 0.0 [0.0, 5.1] |
| X_exploit_fogsnipe | 84 | 0.0 [0.0, 4.4] |
| X_exploit_objectives | 64 | 0.0 [0.0, 5.7] |
| X_exploit_turtle | 76 | 0.0 [0.0, 4.8] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] | vs T2_sieger | vs SM_g2_lane6 | state occupancy | switches/game |
|---|---|---|---|---|---|---|
| SM_g2_lane6 | 296 | 97.6 [95.2, 98.8] | - | - | sieger 69%, laner 31% | 1.0 |
| T2_sieger | 264 | 93.9 [90.4, 96.2] | - | - | - | - |
| X_exploit_splitpush | 96 | 21.9 [14.8, 31.1] | 25% (56) | 18% (40) | - | - |
| X_exploit_farm | 84 | 2.4 [0.7, 8.3] | 5% (40) | 0% (44) | - | - |
| X_exploit_cdlock | 84 | 0.0 [0.0, 4.4] | 0% (48) | 0% (36) | - | - |
| X_exploit_dive | 72 | 0.0 [0.0, 5.1] | 0% (20) | 0% (52) | - | - |
| X_exploit_fogsnipe | 84 | 0.0 [0.0, 4.4] | 0% (46) | 0% (38) | - | - |
| X_exploit_objectives | 64 | 0.0 [0.0, 5.7] | 0% (20) | 0% (44) | - | - |
| X_exploit_turtle | 76 | 0.0 [0.0, 4.8] | 0% (34) | 0% (42) | - | - |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 42.02 per game
- that is 37.3% of all ability uses
- of which true snipes (from cover, two or more hexes away): 34.3% of all uses
- snipes aimed at a champion: 7.4 per game
- activations ending beside an enemy-held hexgroup (looking in): 61.7%


## 10. Anomalies

- ILLEGAL[activation r9]: stacking: w9 and w0 on: 1 games
- ILLEGAL[world r9]: stacking: w9 and w0 on: 1 games
- ILLEGAL[activation r8]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[world r8]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[upkeep r9]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[activation r9]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[world r9]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[upkeep r10]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[activation r10]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[world r10]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[upkeep r11]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[activation r11]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[world r11]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[upkeep r12]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[activation r12]: stacking: n_mid_T2 and w7 on: 1 games
- ILLEGAL[activation r16]: stacking: n_ashwyn and n_kaelis on: 1 games
- ILLEGAL[activation r19]: stacking: w40 and w35 on: 1 games
- ILLEGAL[world r19]: stacking: w40 and w35 on: 1 games

## 11. Top 5 flags (evidence only)

1. **anomaly: ILLEGAL[activation r9]: stacking: w9 and w0 on** - 1 games
2. **anomaly: ILLEGAL[world r9]: stacking: w9 and w0 on** - 1 games
3. **anomaly: ILLEGAL[activation r8]: stacking: n_mid_T2 and w7 on** - 1 games
4. **anomaly: ILLEGAL[world r8]: stacking: n_mid_T2 and w7 on** - 1 games
5. **anomaly: ILLEGAL[upkeep r9]: stacking: n_mid_T2 and w7 on** - 1 games
