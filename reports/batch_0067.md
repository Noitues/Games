# Sim report batch_0067

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
| runtime | 0.2s |
| engine tests | not run |
| generated | 2026-09-27 21:41:08 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 2 FAIL / 23 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 14.4%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 48.3% [44.4, 52.3] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 17.0 [17.0, 17.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 96.2% [94.3, 97.4] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, vellum (roster mean 1.19 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 46.7% [42.7, 50.7] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| veyra | 64.3 [57.6, 70.5] | 210 | 1.10 | 0.92 | 1% | 60% | 0% | 2% | 0.39 | 0.60 | 2.0 | 0.5 | 10% | long_swordx210, longbowx210, vampiric_bladex208 |
| sylphine | 62.4 [56.3, 68.2] | 250 | 0.78 | 0.65 | 11% | 3% | 0% | 10% | 0.29 | 0.45 | 1.5 | 0.0 | 8% | long_swordx250, ruby_crystalx250, vampiric_bladex240 |
| wisp | 58.7 [52.1, 65.0] | 218 | 1.48 | 1.24 | 9% | 62% | 2% | 3% | 0.16 | 0.90 | 2.7 | 5.3 | 14% | longbowx218, ruby_crystalx218, bootsx213 |
| bastion | 57.1 [51.1, 62.9] | 268 | 1.12 | 0.93 | 46% | 1% | 0% | 8% | 0.21 | 0.29 | 1.0 | 1.9 | 11% | long_swordx268, ruby_crystalx268, cloth_armorx267 |
| sable | 54.9 [48.4, 61.2] | 226 | 2.32 | 1.94 | 2% | 38% | 0% | 39% | 0.19 | 0.35 | 1.0 | 4.0 | 22% | longbowx226, ruby_crystalx224, ionian_charmx223 |
| pallas | 54.3 [47.9, 60.6] | 232 | 1.45 | 1.21 | 6% | 1% | 1% | 72% | 0.14 | 0.64 | 2.1 | 5.8 | 13% | bootsx232, longbowx232, ruby_crystalx232 |
| ashwyn | 53.8 [47.4, 60.1] | 234 | 1.95 | 1.63 | 4% | 55% | 0% | 19% | 0.29 | 0.98 | 2.9 | 2.2 | 19% | longbowx234, ruby_crystalx234, ionian_charmx233 |
| noctis | 53.3 [46.6, 59.9] | 212 | 1.19 | 1.00 | 67% | 0% | 12% | 1% | 0.58 | 0.64 | 1.9 | 0.2 | 12% | ionian_charmx212, longbowx212, ruby_crystalx212 |
| ossuar | 50.0 [43.9, 56.1] | 252 | 1.68 | 1.41 | 34% | 1% | 0% | 37% | 0.28 | 0.26 | 0.9 | 3.9 | 15% | long_swordx252, ruby_crystalx252, cloth_armorx250 |
| kestrel | 49.6 [43.5, 55.7] | 256 | 1.36 | 1.13 | 52% | 7% | 0% | 9% | 0.43 | 0.40 | 1.3 | 2.1 | 13% | long_swordx256, longbowx256, vampiric_bladex254 |
| vurmak | 49.6 [43.3, 55.9] | 238 | 0.91 | 0.76 | 20% | 5% | 1% | 22% | 0.48 | 0.36 | 1.3 | 2.8 | 9% | ruby_crystalx238, long_swordx235, cloth_armorx234 |
| orrin | 49.2 [43.2, 55.3] | 262 | 0.93 | 0.78 | 3% | 18% | 1% | 0% | 0.25 | 0.81 | 2.6 | 0.0 | 9% | long_swordx262, longbowx261, vampiric_bladex260 |
| lumen | 48.7 [42.4, 55.1] | 236 | 0.54 | 0.45 | 49% | 1% | 0% | 1% | 0.25 | 0.38 | 1.2 | 0.2 | 5% | longbowx236, ruby_crystalx236, bootsx232 |
| kaelis | 48.5 [41.7, 55.4] | 202 | 0.65 | 0.54 | 22% | 3% | 6% | 5% | 0.39 | 0.41 | 1.4 | 0.7 | 7% | long_swordx202, ruby_crystalx202, cloth_armorx196 |
| bramblehide | 48.1 [42.1, 54.1] | 262 | 1.33 | 1.11 | 1% | 13% | 1% | 26% | 0.28 | 0.45 | 1.3 | 3.7 | 12% | long_swordx262, ruby_crystalx262, vampiric_bladex262 |
| mossgrove | 47.6 [41.4, 53.8] | 248 | 0.79 | 0.66 | 20% | 1% | 1% | 4% | 0.33 | 0.42 | 1.4 | 3.1 | 8% | long_swordx248, ruby_crystalx248, vampiric_bladex244 |
| dax | 47.3 [40.9, 53.8] | 226 | 0.94 | 0.79 | 12% | 25% | 4% | 3% | 0.40 | 0.56 | 1.7 | 1.0 | 9% | long_swordx226, longbowx226, vampiric_bladex224 |
| quillan | 47.1 [41.4, 53.0] | 280 | 1.98 | 1.66 | 7% | 8% | 0% | 62% | 0.21 | 0.86 | 2.6 | 3.1 | 19% | longbowx280, ionian_charmx276, ruby_crystalx274 |
| rictus | 45.7 [39.5, 52.1] | 234 | 0.77 | 0.64 | 12% | 4% | 19% | 2% | 0.33 | 0.82 | 2.5 | 2.3 | 7% | long_swordx234, ruby_crystalx234, vampiric_bladex229 |
| corvane | 45.4 [39.5, 51.5] | 262 | 0.46 | 0.38 | 53% | 0% | 0% | 3% | 0.37 | 0.59 | 1.8 | 0.9 | 5% | bootsx262, longbowx262, ruby_crystalx262 |
| thornjaw | 45.1 [38.5, 52.0] | 206 | 0.82 | 0.69 | 13% | 4% | 1% | 3% | 0.30 | 0.46 | 1.5 | 0.2 | 8% | long_swordx206, ruby_crystalx206, vampiric_bladex200 |
| grivven | 44.4 [38.4, 50.6] | 252 | 1.05 | 0.88 | 5% | 3% | 6% | 38% | 0.11 | 0.55 | 1.9 | 6.7 | 10% | bootsx252, longbowx252, ruby_crystalx252 |
| marrow | 43.8 [37.6, 50.1] | 240 | 1.45 | 1.22 | 5% | 0% | 0% | 44% | 0.17 | 0.29 | 1.0 | 4.7 | 14% | cloth_armorx240, long_swordx240, ruby_crystalx240 |
| vellum | 42.3 [36.4, 48.6] | 248 | 1.95 | 1.63 | 3% | 0% | 3% | 66% | 0.33 | 0.66 | 2.2 | 3.4 | 19% | longbowx248, ionian_charmx246, ruby_crystalx245 |
| brixa | 41.5 [35.5, 47.7] | 246 | 0.88 | 0.74 | 20% | 3% | 7% | 1% | 0.36 | 0.66 | 2.0 | 0.9 | 9% | long_swordx246, longbowx246, vampiric_bladex245 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [47.2, 52.8] | 1.04 |
| Jungle | 50.0 [47.2, 52.8] | 0.91 |
| Mid | 50.0 [47.2, 52.8] | 1.89 |
| Support | 50.0 [47.2, 52.8] | 0.98 |
| Top | 50.0 [47.2, 52.8] | 1.18 |

## 5. Games

- length: median 17.0, p10 15, p90 19
- end reasons: {'nexus': 577, 'round_limit_hp': 3, 'round_limit_towers': 20} (draws 0)
- priority win rate: 48.3% [44.4, 52.3]
- north win rate: 46.7% [42.7, 50.7]
- length histogram: {11: 1, 12: 4, 13: 9, 14: 41, 15: 65, 16: 110, 17: 130, 18: 101, 19: 79, 20: 60}

## 6. Objectives

- takes per game: {'dragon': 1.985, 'baron': 0.8533333333333334}
- median round taken: dragon 9, baron 12.0
- win rate when secured: {'dragon': 49.45424013434089, 'baron': 47.65625}
- camp clears per game: {'raptors': 6.225, 'krugs': 5.825, 'blue_buff': 3.395, 'wolves': 6.095, 'dragon': 1.985, 'red_buff': 3.2216666666666667, 'baron': 0.8533333333333334}

## 7. Structures

- first tower falls: median round 9.0, p10 6, p90 12
- games with at least one tower down: 100.0%
- first-tower win rate: 64.5%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.28 |
| base | 3.00 |
| chips_wave | 2.39 |
| champion_kill | 0.59 |
| tower_kill | 0.56 |
| dragon | 0.25 |
| blue_buff | 0.20 |
| red_buff | 0.10 |

| use | AP |
|---|---|
| shop | 8.40 |
| abilities | 1.61 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.99 | 50.2% | 49.4% | +0.9 |
| cloth_armor | 5 | 1.98 | 49.7% | 50.2% | -0.5 |
| control_ward | 2 | 0.17 | - | 50.0% | - |
| frost_charm | 2 | 0.10 | - | 50.0% | - |
| health_potion | 2 | 1.95 | - | 50.0% | - |
| ionian_charm | 8 | 1.98 | 48.7% | 51.3% | -2.6 |
| long_sword | 6 | 2.00 | 50.1% | 49.7% | +0.4 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 49.9% | 55.2% | -5.2 |
| stopwatch | 3 | 1.93 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 1.99 | 49.9% | 50.1% | -0.1 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 | 384 | 59.9 [54.9, 64.7] |
| T2_sieger | 426 | 56.1 [51.4, 60.7] |
| SM_g3_phase | 390 | 33.6 [29.1, 38.4] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| SM_g2_lane6 | 384 | 59.9 [54.9, 64.7] |  | sieger 70%, laner 30% | 1.0 |
| T2_sieger | 426 | 56.1 [51.4, 60.7] |  | - | - |
| SM_g3_phase | 390 | 33.6 [29.1, 38.4] |  | sieger 37%, objective 36%, laner 23%, brawler 4% | 5.3 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 44.61 per game
- that is 36.6% of all ability uses
- of which true snipes (from cover, two or more hexes away): 32.6% of all uses
- snipes aimed at a champion: 5.8 per game
- activations ending beside an enemy-held hexgroup (looking in): 62.1%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **ability usage: ashwyn.R** - used in 18.5% of affordable rounds with a legal target
2. **ability usage: bastion.W** - used in 0.7% of affordable rounds with a legal target
3. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
4. **ability usage: bastion.R** - used in 7.6% of affordable rounds with a legal target
5. **ability usage: bramblehide.Q** - used in 1.2% of affordable rounds with a legal target
