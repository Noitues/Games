# Sim report batch_0070

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
| generated | 2026-09-28 03:13:22 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 25 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 14.5%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 47.3% [43.4, 51.3] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 17.0 [17.0, 17.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 96.3% [94.5, 97.6] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, vellum (roster mean 1.18 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 51.3% [47.3, 55.3] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pallas | 59.1 [52.6, 65.2] | 232 | 1.47 | 1.24 | 6% | 1% | 2% | 73% | 0.11 | 0.64 | 2.5 | 5.4 | 13% | longbowx232, ruby_crystalx232, bootsx229 |
| bastion | 57.5 [51.5, 63.2] | 268 | 1.11 | 0.94 | 45% | 1% | 0% | 8% | 0.24 | 0.24 | 1.0 | 2.0 | 10% | cloth_armorx268, long_swordx268, ruby_crystalx268 |
| thornjaw | 56.3 [49.5, 62.9] | 206 | 0.83 | 0.70 | 13% | 4% | 1% | 2% | 0.26 | 0.39 | 1.6 | 0.1 | 7% | long_swordx206, ruby_crystalx206, vampiric_bladex200 |
| quillan | 55.7 [49.9, 61.4] | 280 | 1.94 | 1.64 | 7% | 7% | 0% | 61% | 0.17 | 0.77 | 2.9 | 2.8 | 18% | longbowx280, ionian_charmx279, ruby_crystalx277 |
| veyra | 55.2 [48.5, 61.8] | 210 | 1.06 | 0.89 | 1% | 59% | 0% | 2% | 0.52 | 0.53 | 2.2 | 0.6 | 9% | long_swordx210, longbowx210, vampiric_bladex206 |
| vurmak | 54.2 [47.9, 60.4] | 238 | 0.95 | 0.80 | 19% | 5% | 1% | 22% | 0.45 | 0.26 | 1.1 | 2.8 | 9% | ruby_crystalx238, long_swordx237, cloth_armorx229 |
| noctis | 52.8 [46.1, 59.4] | 212 | 1.13 | 0.95 | 66% | 0% | 11% | 2% | 0.53 | 0.62 | 2.4 | 0.2 | 11% | longbowx212, ionian_charmx211, ruby_crystalx210 |
| wisp | 52.8 [46.1, 59.3] | 218 | 1.52 | 1.29 | 8% | 64% | 2% | 3% | 0.17 | 0.83 | 3.2 | 5.1 | 14% | longbowx218, ruby_crystalx218, bootsx217 |
| dax | 52.2 [45.7, 58.6] | 226 | 0.93 | 0.79 | 11% | 26% | 3% | 4% | 0.45 | 0.52 | 2.1 | 1.0 | 9% | long_swordx226, longbowx226, vampiric_bladex226 |
| sable | 51.8 [45.3, 58.2] | 226 | 2.31 | 1.95 | 3% | 39% | 0% | 39% | 0.17 | 0.34 | 1.3 | 3.8 | 21% | longbowx226, ruby_crystalx226, ionian_charmx223 |
| bramblehide | 51.5 [45.5, 57.5] | 262 | 1.30 | 1.10 | 1% | 13% | 1% | 26% | 0.26 | 0.44 | 1.7 | 3.5 | 12% | long_swordx262, ruby_crystalx262, vampiric_bladex262 |
| rictus | 51.3 [44.9, 57.6] | 234 | 0.76 | 0.64 | 12% | 4% | 18% | 2% | 0.37 | 0.80 | 3.2 | 2.1 | 7% | long_swordx234, ruby_crystalx234, vampiric_bladex233 |
| kaelis | 49.0 [42.2, 55.9] | 202 | 0.63 | 0.53 | 23% | 2% | 6% | 4% | 0.32 | 0.40 | 1.7 | 0.6 | 6% | ruby_crystalx202, long_swordx201, cloth_armorx196 |
| orrin | 48.9 [42.9, 54.9] | 262 | 0.90 | 0.76 | 3% | 18% | 1% | 0% | 0.31 | 0.71 | 2.9 | 0.0 | 8% | long_swordx262, longbowx260, vampiric_bladex259 |
| grivven | 48.8 [42.7, 55.0] | 252 | 1.06 | 0.89 | 4% | 3% | 5% | 40% | 0.10 | 0.55 | 2.3 | 6.5 | 10% | bootsx252, longbowx252, ruby_crystalx252 |
| sylphine | 48.8 [42.7, 55.0] | 250 | 0.77 | 0.65 | 12% | 3% | 0% | 9% | 0.26 | 0.45 | 1.9 | 0.0 | 7% | long_swordx250, ruby_crystalx250, vampiric_bladex245 |
| kestrel | 48.0 [42.0, 54.2] | 256 | 1.34 | 1.13 | 53% | 7% | 0% | 10% | 0.48 | 0.40 | 1.7 | 2.1 | 12% | long_swordx256, longbowx256, vampiric_bladex255 |
| vellum | 47.6 [41.4, 53.8] | 248 | 1.94 | 1.64 | 3% | 0% | 3% | 65% | 0.31 | 0.65 | 2.5 | 3.1 | 18% | longbowx248, ionian_charmx242, ruby_crystalx242 |
| brixa | 46.7 [40.6, 53.0] | 246 | 0.88 | 0.75 | 22% | 3% | 6% | 1% | 0.41 | 0.59 | 2.3 | 0.7 | 8% | long_swordx246, longbowx246, vampiric_bladex246 |
| corvane | 45.4 [39.5, 51.5] | 262 | 0.43 | 0.36 | 51% | 0% | 0% | 5% | 0.50 | 0.59 | 2.4 | 1.2 | 4% | bootsx262, longbowx262, ruby_crystalx262 |
| lumen | 44.9 [38.7, 51.3] | 236 | 0.56 | 0.47 | 48% | 1% | 0% | 1% | 0.28 | 0.33 | 1.2 | 0.1 | 5% | longbowx236, ruby_crystalx236, bootsx235 |
| ossuar | 44.4 [38.4, 50.6] | 252 | 1.67 | 1.41 | 33% | 1% | 0% | 38% | 0.24 | 0.27 | 1.1 | 3.8 | 15% | cloth_armorx252, long_swordx252, ruby_crystalx252 |
| marrow | 44.2 [38.0, 50.5] | 240 | 1.44 | 1.22 | 5% | 0% | 0% | 44% | 0.13 | 0.29 | 1.3 | 4.4 | 13% | cloth_armorx240, long_swordx240, ruby_crystalx240 |
| mossgrove | 43.1 [37.1, 49.4] | 248 | 0.77 | 0.65 | 21% | 1% | 1% | 4% | 0.28 | 0.40 | 1.7 | 3.1 | 7% | long_swordx248, ruby_crystalx248, vampiric_bladex247 |
| ashwyn | 41.5 [35.3, 47.9] | 234 | 1.87 | 1.58 | 4% | 54% | 1% | 18% | 0.31 | 0.97 | 3.6 | 2.0 | 17% | longbowx234, ruby_crystalx234, ionian_charmx233 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [47.2, 52.8] | 1.02 |
| Jungle | 50.0 [47.2, 52.8] | 0.89 |
| Mid | 50.0 [47.2, 52.8] | 1.85 |
| Support | 50.0 [47.2, 52.8] | 0.99 |
| Top | 50.0 [47.2, 52.8] | 1.18 |

## 5. Games

- length: median 17.0, p10 15, p90 19
- end reasons: {'nexus': 578, 'round_limit_towers': 19, 'round_limit_hp': 2, 'round_limit_kills': 1} (draws 0)
- priority win rate: 47.3% [43.4, 51.3]
- north win rate: 51.3% [47.3, 55.3]
- length histogram: {10: 1, 11: 1, 12: 6, 13: 13, 14: 31, 15: 65, 16: 109, 17: 144, 18: 115, 19: 66, 20: 49}

## 6. Objectives

- takes per game: {'dragon': 1.9433333333333334, 'baron': 0.8383333333333334}
- median round taken: dragon 9.0, baron 12
- win rate when secured: {'dragon': 49.056603773584904, 'baron': 49.70178926441352}
- camp clears per game: {'raptors': 6.125, 'krugs': 5.681666666666667, 'blue_buff': 3.37, 'wolves': 6.05, 'dragon': 1.9433333333333334, 'red_buff': 3.125, 'baron': 0.8383333333333334}

## 7. Structures

- first tower falls: median round 9.0, p10 6, p90 12
- games with at least one tower down: 100.0%
- first-tower win rate: 58.2%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.25 |
| base | 3.00 |
| chips_wave | 2.36 |
| champion_kill | 1.13 |
| tower_kill | 0.55 |
| dragon | 0.25 |
| blue_buff | 0.20 |
| red_buff | 0.10 |

| use | AP |
|---|---|
| shop | 8.79 |
| abilities | 1.61 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.99 | 51.3% | 46.1% | +5.2 |
| cloth_armor | 5 | 1.98 | 51.1% | 48.9% | +2.1 |
| control_ward | 2 | 0.31 | - | 50.0% | - |
| frost_charm | 2 | 0.20 | - | 50.0% | - |
| health_potion | 2 | 1.96 | - | 50.0% | - |
| ionian_charm | 8 | 1.98 | 50.7% | 49.1% | +1.6 |
| long_sword | 6 | 2.00 | 50.4% | 48.5% | +2.0 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.1 |
| ruby_crystal | 4 | 2.00 | 50.2% | 33.7% | +16.5 |
| stopwatch | 3 | 1.94 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 50.4% | 49.2% | +1.2 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 | 384 | 65.4 [60.5, 70.0] |
| T2_sieger | 426 | 46.5 [41.8, 51.2] |
| SM_g3_phase | 390 | 38.7 [34.0, 43.6] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| SM_g2_lane6 | 384 | 65.4 [60.5, 70.0] |  | sieger 70%, laner 30% | 1.0 |
| T2_sieger | 426 | 46.5 [41.8, 51.2] |  | - | - |
| SM_g3_phase | 390 | 38.7 [34.0, 43.6] |  | sieger 37%, objective 36%, laner 23%, brawler 4% | 5.3 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 43.98 per game
- that is 37.0% of all ability uses
- of which true snipes (from cover, two or more hexes away): 32.9% of all uses
- snipes aimed at a champion: 5.5 per game
- activations ending beside an enemy-held hexgroup (looking in): 61.7%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **ability usage: ashwyn.R** - used in 18.1% of affordable rounds with a legal target
2. **ability usage: bastion.W** - used in 0.5% of affordable rounds with a legal target
3. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
4. **ability usage: bastion.R** - used in 8.2% of affordable rounds with a legal target
5. **ability usage: bramblehide.Q** - used in 1.4% of affordable rounds with a legal target
