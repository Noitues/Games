# Sim report batch_0071

## 1. Header

| field | value |
|---|---|
| rules | 1.8.0 |
| roster | 1.8.0 |
| ai | 1.5.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 600 |
| seed | 5901 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 0.1s |
| engine tests | not run |
| generated | 2026-09-28 03:13:23 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 1 FAIL / 24 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 14.3%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 47.5% [43.5, 51.5] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 17.0 [17.0, 17.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 96.7% [94.9, 97.8] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, vellum (roster mean 1.19 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.2% [44.2, 52.2] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| veyra | 61.9 [55.2, 68.2] | 210 | 1.09 | 0.91 | 1% | 59% | 0% | 2% | 0.49 | 0.57 | 1.8 | 0.4 | 10% | long_swordx210, longbowx210, vampiric_bladex208 |
| pallas | 59.9 [53.5, 66.0] | 232 | 1.48 | 1.24 | 6% | 1% | 1% | 71% | 0.11 | 0.64 | 1.9 | 5.4 | 13% | longbowx232, ruby_crystalx232, bootsx231 |
| wisp | 58.3 [51.6, 64.6] | 218 | 1.55 | 1.30 | 7% | 64% | 1% | 3% | 0.16 | 0.87 | 2.6 | 5.2 | 14% | longbowx218, ruby_crystalx218, bootsx216 |
| quillan | 56.8 [50.9, 62.5] | 280 | 1.96 | 1.64 | 7% | 7% | 0% | 61% | 0.17 | 0.84 | 2.5 | 2.9 | 18% | longbowx280, ionian_charmx279, ruby_crystalx278 |
| rictus | 55.1 [48.7, 61.4] | 234 | 0.75 | 0.63 | 13% | 3% | 20% | 3% | 0.43 | 0.80 | 2.4 | 2.4 | 7% | long_swordx234, ruby_crystalx234, vampiric_bladex230 |
| kaelis | 55.0 [48.1, 61.7] | 202 | 0.63 | 0.53 | 22% | 3% | 6% | 5% | 0.36 | 0.41 | 1.3 | 0.7 | 6% | ruby_crystalx202, long_swordx201, cloth_armorx199 |
| noctis | 54.7 [48.0, 61.3] | 212 | 1.17 | 0.98 | 65% | 0% | 11% | 2% | 0.58 | 0.62 | 1.9 | 0.3 | 12% | longbowx212, ionian_charmx211, ruby_crystalx211 |
| sylphine | 53.2 [47.0, 59.3] | 250 | 0.78 | 0.65 | 11% | 3% | 0% | 9% | 0.32 | 0.40 | 1.3 | 0.0 | 7% | long_swordx250, ruby_crystalx250, vampiric_bladex241 |
| bastion | 53.0 [47.0, 58.9] | 268 | 1.14 | 0.95 | 46% | 1% | 0% | 8% | 0.20 | 0.25 | 0.8 | 2.0 | 10% | cloth_armorx268, long_swordx268, ruby_crystalx268 |
| brixa | 52.4 [46.2, 58.6] | 246 | 0.88 | 0.73 | 21% | 3% | 6% | 1% | 0.33 | 0.62 | 1.9 | 0.8 | 8% | long_swordx246, longbowx246, vampiric_bladex245 |
| vurmak | 50.4 [44.1, 56.7] | 238 | 0.95 | 0.79 | 19% | 5% | 1% | 22% | 0.52 | 0.26 | 0.8 | 2.8 | 9% | ruby_crystalx238, long_swordx236, cloth_armorx234 |
| bramblehide | 48.9 [42.9, 54.9] | 262 | 1.30 | 1.09 | 1% | 13% | 0% | 25% | 0.23 | 0.46 | 1.4 | 3.5 | 12% | long_swordx262, ruby_crystalx262, vampiric_bladex262 |
| orrin | 48.9 [42.9, 54.9] | 262 | 0.93 | 0.78 | 3% | 19% | 1% | 0% | 0.32 | 0.77 | 2.4 | 0.0 | 9% | long_swordx262, longbowx261, vampiric_bladex256 |
| mossgrove | 48.8 [42.6, 55.0] | 248 | 0.79 | 0.66 | 20% | 1% | 1% | 4% | 0.27 | 0.43 | 1.4 | 3.1 | 7% | long_swordx248, ruby_crystalx248, vampiric_bladex246 |
| ossuar | 48.4 [42.3, 54.6] | 252 | 1.67 | 1.40 | 34% | 1% | 0% | 36% | 0.23 | 0.29 | 1.0 | 3.7 | 15% | long_swordx252, ruby_crystalx252, cloth_armorx251 |
| sable | 48.2 [41.8, 54.7] | 226 | 2.31 | 1.93 | 3% | 39% | 0% | 38% | 0.17 | 0.37 | 1.1 | 3.8 | 21% | longbowx226, ionian_charmx224, ruby_crystalx223 |
| kestrel | 48.0 [42.0, 54.2] | 256 | 1.35 | 1.13 | 53% | 7% | 0% | 9% | 0.54 | 0.41 | 1.3 | 2.1 | 12% | long_swordx256, longbowx256, vampiric_bladex255 |
| grivven | 47.2 [41.1, 53.4] | 252 | 1.06 | 0.89 | 4% | 3% | 4% | 38% | 0.12 | 0.55 | 1.9 | 6.5 | 10% | longbowx252, ruby_crystalx252, bootsx251 |
| vellum | 45.2 [39.1, 51.4] | 248 | 1.96 | 1.64 | 3% | 0% | 3% | 65% | 0.33 | 0.67 | 2.1 | 3.2 | 18% | longbowx248, ionian_charmx245, ruby_crystalx244 |
| ashwyn | 44.4 [38.2, 50.8] | 234 | 1.93 | 1.61 | 4% | 53% | 0% | 20% | 0.33 | 1.00 | 2.9 | 2.1 | 18% | longbowx234, ruby_crystalx234, ionian_charmx233 |
| lumen | 44.1 [37.9, 50.4] | 236 | 0.56 | 0.47 | 49% | 1% | 0% | 1% | 0.25 | 0.32 | 1.0 | 0.1 | 5% | longbowx236, ruby_crystalx236, bootsx234 |
| marrow | 43.8 [37.6, 50.1] | 240 | 1.42 | 1.19 | 5% | 1% | 0% | 43% | 0.14 | 0.25 | 0.8 | 4.5 | 13% | cloth_armorx240, long_swordx240, ruby_crystalx240 |
| thornjaw | 43.2 [36.6, 50.0] | 206 | 0.84 | 0.70 | 13% | 4% | 1% | 3% | 0.26 | 0.42 | 1.4 | 0.1 | 7% | long_swordx206, ruby_crystalx206, vampiric_bladex202 |
| corvane | 42.4 [36.5, 48.4] | 262 | 0.44 | 0.37 | 52% | 0% | 0% | 4% | 0.52 | 0.57 | 1.8 | 1.0 | 4% | longbowx262, ruby_crystalx262, bootsx261 |
| dax | 39.8 [33.7, 46.3] | 226 | 0.93 | 0.78 | 12% | 26% | 3% | 4% | 0.58 | 0.54 | 1.6 | 1.0 | 9% | long_swordx226, longbowx226, vampiric_bladex226 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [47.2, 52.8] | 1.04 |
| Jungle | 50.0 [47.2, 52.8] | 0.90 |
| Mid | 50.0 [47.2, 52.8] | 1.88 |
| Support | 50.0 [47.2, 52.8] | 1.00 |
| Top | 50.0 [47.2, 52.8] | 1.18 |

## 5. Games

- length: median 17.0, p10 15, p90 19
- end reasons: {'nexus': 580, 'round_limit_towers': 18, 'round_limit_hp': 2} (draws 0)
- priority win rate: 47.5% [43.5, 51.5]
- north win rate: 48.2% [44.2, 52.2]
- length histogram: {10: 1, 12: 4, 13: 16, 14: 38, 15: 82, 16: 121, 17: 141, 18: 103, 19: 44, 20: 50}

## 6. Objectives

- takes per game: {'dragon': 1.9366666666666668, 'baron': 0.8366666666666667}
- median round taken: dragon 9.0, baron 12.0
- win rate when secured: {'dragon': 46.98795180722892, 'baron': 48.20717131474104}
- camp clears per game: {'raptors': 6.138333333333334, 'krugs': 5.695, 'blue_buff': 3.361666666666667, 'wolves': 6.011666666666667, 'dragon': 1.9366666666666668, 'red_buff': 3.155, 'baron': 0.8366666666666667}

## 7. Structures

- first tower falls: median round 9.0, p10 6, p90 12
- games with at least one tower down: 100.0%
- first-tower win rate: 63.8%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.28 |
| base | 3.00 |
| chips_wave | 2.39 |
| champion_kill | 1.17 |
| tower_kill | 0.57 |
| dragon | 0.25 |
| blue_buff | 0.20 |
| red_buff | 0.10 |

| use | AP |
|---|---|
| shop | 8.88 |
| abilities | 1.63 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.99 | 50.7% | 47.9% | +2.8 |
| cloth_armor | 5 | 1.99 | 50.3% | 49.7% | +0.5 |
| control_ward | 2 | 0.27 | - | 50.0% | - |
| frost_charm | 2 | 0.21 | - | 50.0% | - |
| health_potion | 2 | 1.95 | - | 50.0% | - |
| ionian_charm | 8 | 1.99 | 49.3% | 51.0% | -1.7 |
| long_sword | 6 | 2.00 | 50.1% | 49.6% | +0.5 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 50.0% | 47.9% | +2.1 |
| stopwatch | 3 | 1.94 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 1.99 | 50.1% | 49.9% | +0.2 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 | 384 | 69.3 [64.5, 73.7] |
| T2_sieger | 426 | 49.3 [44.6, 54.0] |
| SM_g3_phase | 390 | 31.8 [27.4, 36.6] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| SM_g2_lane6 | 384 | 69.3 [64.5, 73.7] |  | sieger 69%, laner 31% | 1.0 |
| T2_sieger | 426 | 49.3 [44.6, 54.0] |  | - | - |
| SM_g3_phase | 390 | 31.8 [27.4, 36.6] |  | sieger 38%, objective 35%, laner 23%, brawler 4% | 5.4 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 43.76 per game
- that is 36.2% of all ability uses
- of which true snipes (from cover, two or more hexes away): 32.2% of all uses
- snipes aimed at a champion: 5.6 per game
- activations ending beside an enemy-held hexgroup (looking in): 62.1%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **ability usage: ashwyn.R** - used in 19.8% of affordable rounds with a legal target
2. **ability usage: bastion.W** - used in 0.5% of affordable rounds with a legal target
3. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
4. **ability usage: bastion.R** - used in 8.3% of affordable rounds with a legal target
5. **ability usage: bramblehide.Q** - used in 1.1% of affordable rounds with a legal target
