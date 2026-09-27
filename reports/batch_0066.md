# Sim report batch_0066

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
| runtime | 0.4s |
| engine tests | not run |
| generated | 2026-09-27 21:41:07 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 1 FAIL / 24 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 14.5%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 50.3% [46.3, 54.3] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 15.0 [14.0, 15.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 100.0% [99.4, 100.0] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, vellum (roster mean 1.17 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 49.7% [45.7, 53.7] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pallas | 58.6 [52.2, 64.8] | 232 | 1.42 | 1.21 | 6% | 1% | 2% | 72% | 0.08 | 0.57 | 1.6 | 5.0 | 12% | longbowx232, ruby_crystalx232, bootsx230 |
| sylphine | 57.2 [51.0, 63.2] | 250 | 0.77 | 0.65 | 11% | 3% | 0% | 10% | 0.24 | 0.34 | 1.1 | 0.0 | 7% | long_swordx250, ruby_crystalx250, vampiric_bladex226 |
| wisp | 55.0 [48.4, 61.5] | 218 | 1.53 | 1.30 | 8% | 63% | 2% | 3% | 0.14 | 0.78 | 2.2 | 4.8 | 14% | longbowx218, ruby_crystalx217, bootsx202 |
| kestrel | 54.7 [48.6, 60.7] | 256 | 1.32 | 1.12 | 54% | 7% | 1% | 8% | 0.42 | 0.32 | 1.0 | 1.7 | 12% | long_swordx256, longbowx256, vampiric_bladex253 |
| rictus | 54.3 [47.9, 60.5] | 234 | 0.73 | 0.62 | 13% | 3% | 19% | 2% | 0.36 | 0.76 | 2.2 | 2.1 | 7% | long_swordx234, ruby_crystalx234, vampiric_bladex219 |
| bastion | 53.7 [47.8, 59.6] | 268 | 1.14 | 0.97 | 48% | 0% | 0% | 7% | 0.18 | 0.23 | 0.8 | 1.6 | 11% | long_swordx268, ruby_crystalx268, cloth_armorx267 |
| noctis | 52.8 [46.1, 59.4] | 212 | 1.21 | 1.03 | 69% | 0% | 11% | 2% | 0.49 | 0.56 | 1.6 | 0.3 | 12% | longbowx212, ionian_charmx210, ruby_crystalx206 |
| vellum | 52.8 [46.6, 58.9] | 248 | 1.80 | 1.53 | 3% | 0% | 3% | 64% | 0.25 | 0.61 | 1.8 | 3.1 | 17% | longbowx248, ionian_charmx238, ruby_crystalx227 |
| lumen | 51.7 [45.3, 58.0] | 236 | 0.56 | 0.48 | 50% | 1% | 0% | 1% | 0.23 | 0.31 | 1.0 | 0.1 | 5% | longbowx236, ruby_crystalx236, bootsx230 |
| kaelis | 51.5 [44.6, 58.3] | 202 | 0.62 | 0.53 | 24% | 3% | 6% | 6% | 0.37 | 0.37 | 1.1 | 0.7 | 6% | ruby_crystalx202, long_swordx199, cloth_armorx191 |
| veyra | 51.4 [44.7, 58.1] | 210 | 1.10 | 0.94 | 2% | 61% | 0% | 2% | 0.41 | 0.51 | 1.5 | 0.5 | 10% | long_swordx210, longbowx208, vampiric_bladex205 |
| sable | 50.9 [44.4, 57.3] | 226 | 2.26 | 1.92 | 3% | 39% | 0% | 40% | 0.14 | 0.28 | 0.8 | 3.8 | 20% | longbowx226, ionian_charmx221, ruby_crystalx216 |
| quillan | 50.4 [44.5, 56.2] | 280 | 1.95 | 1.66 | 8% | 8% | 0% | 62% | 0.15 | 0.74 | 2.1 | 2.8 | 18% | longbowx280, ionian_charmx276, ruby_crystalx267 |
| orrin | 49.2 [43.2, 55.3] | 262 | 0.93 | 0.79 | 3% | 18% | 1% | 0% | 0.32 | 0.68 | 2.0 | 0.0 | 9% | long_swordx262, longbowx258, vampiric_bladex244 |
| vurmak | 49.2 [42.9, 55.5] | 238 | 0.91 | 0.77 | 20% | 6% | 1% | 24% | 0.53 | 0.28 | 0.8 | 2.7 | 9% | ruby_crystalx238, long_swordx235, cloth_armorx216 |
| bramblehide | 48.9 [42.9, 54.9] | 262 | 1.25 | 1.06 | 1% | 13% | 1% | 25% | 0.23 | 0.40 | 1.2 | 3.3 | 11% | long_swordx262, ruby_crystalx262, vampiric_bladex258 |
| dax | 48.7 [42.2, 55.2] | 226 | 0.93 | 0.79 | 13% | 25% | 3% | 4% | 0.39 | 0.51 | 1.5 | 0.8 | 9% | long_swordx226, longbowx226, vampiric_bladex223 |
| grivven | 48.4 [42.3, 54.6] | 252 | 1.03 | 0.88 | 5% | 3% | 5% | 37% | 0.10 | 0.42 | 1.3 | 5.8 | 10% | longbowx252, ruby_crystalx252, bootsx251 |
| ossuar | 48.0 [41.9, 54.2] | 252 | 1.67 | 1.42 | 36% | 1% | 0% | 36% | 0.22 | 0.23 | 0.8 | 3.4 | 15% | long_swordx252, ruby_crystalx252, cloth_armorx246 |
| marrow | 47.5 [41.3, 53.8] | 240 | 1.43 | 1.22 | 5% | 0% | 0% | 45% | 0.13 | 0.23 | 0.8 | 4.1 | 13% | ruby_crystalx240, long_swordx239, cloth_armorx232 |
| brixa | 45.9 [39.8, 52.2] | 246 | 0.84 | 0.71 | 21% | 2% | 6% | 1% | 0.38 | 0.55 | 1.7 | 0.7 | 8% | long_swordx246, longbowx245, vampiric_bladex243 |
| thornjaw | 44.7 [38.0, 51.5] | 206 | 0.81 | 0.69 | 12% | 4% | 1% | 3% | 0.28 | 0.41 | 1.3 | 0.1 | 7% | long_swordx206, ruby_crystalx206, vampiric_bladex194 |
| mossgrove | 44.4 [38.3, 50.6] | 248 | 0.77 | 0.65 | 22% | 1% | 1% | 5% | 0.23 | 0.39 | 1.2 | 3.0 | 7% | long_swordx248, ruby_crystalx248, vampiric_bladex235 |
| ashwyn | 43.2 [37.0, 49.6] | 234 | 1.91 | 1.63 | 4% | 54% | 1% | 20% | 0.29 | 0.86 | 2.4 | 2.1 | 18% | ionian_charmx234, longbowx234, ruby_crystalx232 |
| corvane | 38.2 [32.5, 44.2] | 262 | 0.46 | 0.39 | 53% | 0% | 0% | 4% | 0.35 | 0.52 | 1.5 | 1.0 | 4% | longbowx262, ruby_crystalx262, bootsx259 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [47.2, 52.8] | 1.02 |
| Jungle | 50.0 [47.2, 52.8] | 0.87 |
| Mid | 50.0 [47.2, 52.8] | 1.84 |
| Support | 50.0 [47.2, 52.8] | 0.98 |
| Top | 50.0 [47.2, 52.8] | 1.18 |

## 5. Games

- length: median 15.0, p10 12, p90 17
- end reasons: {'nexus': 600} (draws 0)
- priority win rate: 50.3% [46.3, 54.3]
- north win rate: 49.7% [45.7, 53.7]
- length histogram: {10: 7, 11: 27, 12: 54, 13: 81, 14: 126, 15: 93, 16: 97, 17: 65, 18: 27, 19: 18, 20: 5}

## 6. Objectives

- takes per game: {'dragon': 1.7, 'baron': 0.6216666666666667}
- median round taken: dragon 7.0, baron 12
- win rate when secured: {'dragon': 46.470588235294116, 'baron': 43.16353887399464}
- camp clears per game: {'raptors': 5.486666666666666, 'krugs': 5.048333333333333, 'blue_buff': 2.9633333333333334, 'wolves': 5.306666666666667, 'dragon': 1.7, 'red_buff': 2.7816666666666667, 'baron': 0.6216666666666667}

## 7. Structures

- first tower falls: median round 7.0, p10 5, p90 10
- games with at least one tower down: 100.0%
- first-tower win rate: 65.2%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.32 |
| base | 3.00 |
| chips_wave | 2.28 |
| champion_kill | 1.15 |
| tower_kill | 0.59 |
| dragon | 0.21 |
| blue_buff | 0.20 |
| red_buff | 0.10 |

| use | AP |
|---|---|
| shop | 8.83 |
| abilities | 1.62 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.95 | 48.3% | 52.4% | -4.0 |
| cloth_armor | 5 | 1.92 | 48.5% | 51.0% | -2.6 |
| control_ward | 2 | 0.17 | - | 50.0% | - |
| frost_charm | 2 | 0.10 | - | 50.0% | - |
| health_potion | 2 | 1.93 | - | 50.0% | - |
| ionian_charm | 8 | 1.97 | 46.3% | 52.7% | -6.4 |
| long_sword | 6 | 2.00 | 49.9% | 50.4% | -0.6 |
| longbow | 6 | 2.00 | 50.0% | 50.1% | -0.1 |
| ruby_crystal | 4 | 2.00 | 49.9% | 52.1% | -2.2 |
| stopwatch | 3 | 1.87 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.96 | 49.6% | 50.5% | -1.0 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 | 384 | 63.3 [58.4, 67.9] |
| T2_sieger | 426 | 59.2 [54.4, 63.7] |
| SM_g3_phase | 390 | 26.9 [22.8, 31.5] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| SM_g2_lane6 | 384 | 63.3 [58.4, 67.9] |  | sieger 65%, laner 35% | 1.0 |
| T2_sieger | 426 | 59.2 [54.4, 63.7] |  | - | - |
| SM_g3_phase | 390 | 26.9 [22.8, 31.5] |  | objective 38%, sieger 31%, laner 27%, brawler 4% | 5.1 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 39.27 per game
- that is 37.7% of all ability uses
- of which true snipes (from cover, two or more hexes away): 33.4% of all uses
- snipes aimed at a champion: 5.1 per game
- activations ending beside an enemy-held hexgroup (looking in): 60.3%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **ability usage: ashwyn.R** - used in 20.3% of affordable rounds with a legal target
2. **ability usage: bastion.W** - used in 0.4% of affordable rounds with a legal target
3. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
4. **ability usage: bastion.R** - used in 7.5% of affordable rounds with a legal target
5. **ability usage: bramblehide.Q** - used in 1.3% of affordable rounds with a legal target
