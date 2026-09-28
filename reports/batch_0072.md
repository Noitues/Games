# Sim report batch_0072

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
| generated | 2026-09-28 03:13:25 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 25 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 14.5%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 47.2% [43.2, 51.2] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 17.0 [17.0, 17.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 96.3% [94.5, 97.6] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, vellum (roster mean 1.18 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 51.5% [47.5, 55.5] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pallas | 58.6 [52.2, 64.8] | 232 | 1.47 | 1.24 | 6% | 1% | 2% | 72% | 0.10 | 0.65 | 2.5 | 5.3 | 13% | longbowx232, ruby_crystalx232, bootsx229 |
| quillan | 57.1 [51.3, 62.8] | 280 | 1.94 | 1.64 | 7% | 7% | 0% | 60% | 0.17 | 0.76 | 2.9 | 2.8 | 18% | longbowx280, ionian_charmx279, ruby_crystalx277 |
| bastion | 56.7 [50.7, 62.5] | 268 | 1.12 | 0.95 | 45% | 1% | 0% | 8% | 0.24 | 0.24 | 1.0 | 2.0 | 10% | cloth_armorx268, long_swordx268, ruby_crystalx268 |
| thornjaw | 56.3 [49.5, 62.9] | 206 | 0.83 | 0.70 | 12% | 4% | 1% | 2% | 0.26 | 0.39 | 1.6 | 0.1 | 7% | long_swordx206, ruby_crystalx206, vampiric_bladex200 |
| vurmak | 55.9 [49.5, 62.0] | 238 | 0.95 | 0.80 | 19% | 5% | 1% | 22% | 0.45 | 0.27 | 1.1 | 2.8 | 9% | ruby_crystalx238, long_swordx237, cloth_armorx229 |
| veyra | 55.2 [48.5, 61.8] | 210 | 1.06 | 0.90 | 1% | 59% | 0% | 2% | 0.52 | 0.53 | 2.2 | 0.5 | 10% | long_swordx210, longbowx210, vampiric_bladex206 |
| dax | 52.7 [46.2, 59.1] | 226 | 0.93 | 0.79 | 11% | 26% | 3% | 4% | 0.45 | 0.52 | 2.1 | 1.0 | 9% | long_swordx226, longbowx226, vampiric_bladex226 |
| noctis | 52.4 [45.7, 59.0] | 212 | 1.13 | 0.96 | 66% | 0% | 11% | 2% | 0.54 | 0.62 | 2.4 | 0.3 | 11% | longbowx212, ionian_charmx211, ruby_crystalx210 |
| bramblehide | 52.3 [46.3, 58.3] | 262 | 1.30 | 1.10 | 1% | 13% | 1% | 26% | 0.26 | 0.44 | 1.7 | 3.5 | 12% | long_swordx262, ruby_crystalx262, vampiric_bladex262 |
| wisp | 51.8 [45.2, 58.4] | 218 | 1.52 | 1.28 | 8% | 64% | 1% | 3% | 0.17 | 0.84 | 3.2 | 5.1 | 14% | longbowx218, ruby_crystalx218, bootsx217 |
| rictus | 51.7 [45.3, 58.0] | 234 | 0.76 | 0.64 | 12% | 4% | 18% | 2% | 0.37 | 0.82 | 3.2 | 2.1 | 7% | long_swordx234, ruby_crystalx234, vampiric_bladex233 |
| grivven | 49.6 [43.5, 55.7] | 252 | 1.05 | 0.89 | 5% | 3% | 5% | 40% | 0.10 | 0.54 | 2.3 | 6.5 | 10% | bootsx252, longbowx252, ruby_crystalx252 |
| sable | 49.6 [43.1, 56.0] | 226 | 2.31 | 1.95 | 3% | 39% | 0% | 39% | 0.16 | 0.34 | 1.3 | 3.8 | 21% | longbowx226, ruby_crystalx226, ionian_charmx223 |
| kaelis | 48.5 [41.7, 55.4] | 202 | 0.63 | 0.53 | 23% | 2% | 6% | 5% | 0.32 | 0.40 | 1.7 | 0.6 | 6% | ruby_crystalx202, long_swordx200, cloth_armorx196 |
| orrin | 48.1 [42.1, 54.1] | 262 | 0.90 | 0.76 | 3% | 18% | 1% | 0% | 0.31 | 0.71 | 2.9 | 0.0 | 8% | long_swordx262, longbowx260, vampiric_bladex259 |
| kestrel | 48.0 [42.0, 54.2] | 256 | 1.34 | 1.13 | 53% | 7% | 0% | 10% | 0.48 | 0.40 | 1.7 | 2.1 | 12% | long_swordx256, longbowx256, vampiric_bladex255 |
| sylphine | 47.6 [41.5, 53.8] | 250 | 0.77 | 0.65 | 12% | 3% | 0% | 9% | 0.26 | 0.45 | 1.9 | 0.0 | 7% | long_swordx250, ruby_crystalx250, vampiric_bladex245 |
| vellum | 47.2 [41.1, 53.4] | 248 | 1.94 | 1.64 | 3% | 0% | 3% | 65% | 0.32 | 0.66 | 2.6 | 3.1 | 18% | longbowx248, ionian_charmx242, ruby_crystalx242 |
| brixa | 47.2 [41.0, 53.4] | 246 | 0.88 | 0.75 | 22% | 3% | 6% | 1% | 0.41 | 0.58 | 2.3 | 0.7 | 8% | long_swordx246, longbowx246, vampiric_bladex246 |
| corvane | 46.2 [40.2, 52.2] | 262 | 0.43 | 0.36 | 51% | 0% | 0% | 5% | 0.50 | 0.58 | 2.3 | 1.2 | 4% | bootsx262, longbowx262, ruby_crystalx262 |
| ossuar | 45.2 [39.2, 51.4] | 252 | 1.67 | 1.41 | 33% | 1% | 0% | 38% | 0.23 | 0.27 | 1.1 | 3.8 | 15% | cloth_armorx252, long_swordx252, ruby_crystalx252 |
| lumen | 44.5 [38.3, 50.9] | 236 | 0.56 | 0.48 | 49% | 1% | 0% | 1% | 0.28 | 0.32 | 1.2 | 0.2 | 5% | longbowx236, ruby_crystalx236, bootsx235 |
| mossgrove | 43.1 [37.1, 49.4] | 248 | 0.77 | 0.66 | 21% | 1% | 1% | 4% | 0.29 | 0.40 | 1.7 | 3.2 | 7% | long_swordx248, ruby_crystalx248, vampiric_bladex247 |
| marrow | 42.9 [36.8, 49.2] | 240 | 1.44 | 1.21 | 5% | 0% | 0% | 44% | 0.14 | 0.29 | 1.3 | 4.4 | 13% | cloth_armorx240, long_swordx240, ruby_crystalx240 |
| ashwyn | 42.7 [36.6, 49.1] | 234 | 1.87 | 1.58 | 4% | 54% | 1% | 18% | 0.31 | 0.97 | 3.6 | 2.0 | 17% | longbowx234, ruby_crystalx234, ionian_charmx233 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [47.2, 52.8] | 1.02 |
| Jungle | 50.0 [47.2, 52.8] | 0.89 |
| Mid | 50.0 [47.2, 52.8] | 1.85 |
| Support | 50.0 [47.2, 52.8] | 0.98 |
| Top | 50.0 [47.2, 52.8] | 1.18 |

## 5. Games

- length: median 17.0, p10 15, p90 19
- end reasons: {'nexus': 578, 'round_limit_towers': 21, 'round_limit_hp': 1} (draws 0)
- priority win rate: 47.2% [43.2, 51.2]
- north win rate: 51.5% [47.5, 55.5]
- length histogram: {10: 1, 11: 1, 12: 6, 13: 13, 14: 31, 15: 65, 16: 109, 17: 144, 18: 112, 19: 67, 20: 51}

## 6. Objectives

- takes per game: {'dragon': 1.9366666666666668, 'baron': 0.835}
- median round taken: dragon 9.0, baron 12
- win rate when secured: {'dragon': 49.82788296041308, 'baron': 49.70059880239521}
- camp clears per game: {'raptors': 6.111666666666666, 'krugs': 5.668333333333333, 'blue_buff': 3.3633333333333333, 'wolves': 6.043333333333333, 'dragon': 1.9366666666666668, 'red_buff': 3.1366666666666667, 'baron': 0.835}

## 7. Structures

- first tower falls: median round 9.0, p10 6, p90 12
- games with at least one tower down: 100.0%
- first-tower win rate: 58.3%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.24 |
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
| abilities | 1.60 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.99 | 51.4% | 45.7% | +5.7 |
| cloth_armor | 5 | 1.98 | 51.3% | 48.7% | +2.7 |
| control_ward | 2 | 0.30 | - | 50.0% | - |
| frost_charm | 2 | 0.20 | - | 50.0% | - |
| health_potion | 2 | 1.96 | - | 50.0% | - |
| ionian_charm | 8 | 1.98 | 50.9% | 48.8% | +2.0 |
| long_sword | 6 | 2.00 | 50.4% | 48.5% | +2.0 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.1 |
| ruby_crystal | 4 | 2.00 | 50.2% | 33.7% | +16.5 |
| stopwatch | 3 | 1.94 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 50.5% | 49.2% | +1.3 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 | 384 | 66.7 [61.8, 71.2] |
| T2_sieger | 426 | 45.8 [41.1, 50.5] |
| SM_g3_phase | 390 | 38.2 [33.5, 43.1] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| SM_g2_lane6 | 384 | 66.7 [61.8, 71.2] |  | sieger 70%, laner 30% | 1.0 |
| T2_sieger | 426 | 45.8 [41.1, 50.5] |  | - | - |
| SM_g3_phase | 390 | 38.2 [33.5, 43.1] |  | sieger 37%, objective 36%, laner 23%, brawler 4% | 5.3 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 44.03 per game
- that is 37.0% of all ability uses
- of which true snipes (from cover, two or more hexes away): 33.0% of all uses
- snipes aimed at a champion: 5.6 per game
- activations ending beside an enemy-held hexgroup (looking in): 61.8%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **ability usage: ashwyn.R** - used in 18.0% of affordable rounds with a legal target
2. **ability usage: bastion.W** - used in 0.5% of affordable rounds with a legal target
3. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
4. **ability usage: bastion.R** - used in 8.4% of affordable rounds with a legal target
5. **ability usage: bramblehide.Q** - used in 1.5% of affordable rounds with a legal target
