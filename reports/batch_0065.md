# Sim report batch_0065

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
| runtime | 0.3s |
| engine tests | not run |
| generated | 2026-09-27 19:37:23 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 1 FAIL / 24 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 51/58 abilities outside the band; roster mean 14.6%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 48.0% [44.0, 52.0] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 15.0 [15.0, 15.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 98.8% [97.6, 99.4] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, vellum (roster mean 1.18 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 50.0% [46.0, 54.0] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pallas | 62.1 [55.7, 68.1] | 232 | 1.38 | 1.17 | 6% | 1% | 2% | 72% | 0.09 | 0.58 | 1.7 | 5.3 | 13% | longbowx232, ruby_crystalx232, bootsx226 |
| sylphine | 57.6 [51.4, 63.6] | 250 | 0.75 | 0.63 | 12% | 3% | 0% | 10% | 0.29 | 0.38 | 1.1 | 0.0 | 7% | long_swordx250, ruby_crystalx250, vampiric_bladex217 |
| noctis | 55.7 [48.9, 62.2] | 212 | 1.24 | 1.05 | 70% | 0% | 11% | 1% | 0.48 | 0.52 | 1.5 | 0.2 | 13% | longbowx212, ionian_charmx209, ruby_crystalx202 |
| veyra | 55.2 [48.5, 61.8] | 210 | 1.10 | 0.93 | 1% | 62% | 0% | 2% | 0.48 | 0.60 | 1.9 | 0.4 | 10% | long_swordx210, longbowx210, vampiric_bladex193 |
| bastion | 55.2 [49.2, 61.1] | 268 | 1.15 | 0.98 | 48% | 1% | 0% | 9% | 0.20 | 0.24 | 0.7 | 1.9 | 11% | long_swordx268, ruby_crystalx268, cloth_armorx266 |
| kaelis | 53.5 [46.6, 60.2] | 202 | 0.62 | 0.52 | 23% | 3% | 7% | 5% | 0.31 | 0.42 | 1.3 | 0.7 | 6% | ruby_crystalx202, long_swordx200, cloth_armorx187 |
| orrin | 52.7 [46.6, 58.6] | 262 | 0.90 | 0.76 | 4% | 18% | 1% | 0% | 0.29 | 0.73 | 2.2 | 0.0 | 9% | long_swordx262, longbowx258, vampiric_bladex247 |
| ashwyn | 51.7 [45.3, 58.0] | 234 | 1.98 | 1.67 | 4% | 56% | 1% | 20% | 0.31 | 0.84 | 2.3 | 2.1 | 19% | ionian_charmx234, longbowx234, ruby_crystalx233 |
| rictus | 51.7 [45.3, 58.0] | 234 | 0.76 | 0.64 | 13% | 4% | 20% | 2% | 0.35 | 0.79 | 2.4 | 2.2 | 7% | long_swordx234, ruby_crystalx234, vampiric_bladex221 |
| wisp | 51.4 [44.8, 57.9] | 218 | 1.49 | 1.26 | 8% | 62% | 2% | 3% | 0.13 | 0.72 | 2.0 | 4.9 | 14% | longbowx218, ruby_crystalx217, bootsx201 |
| bramblehide | 50.0 [44.0, 56.0] | 262 | 1.28 | 1.08 | 1% | 12% | 1% | 25% | 0.20 | 0.47 | 1.4 | 3.3 | 12% | long_swordx262, ruby_crystalx262, vampiric_bladex260 |
| grivven | 49.6 [43.5, 55.7] | 252 | 1.02 | 0.86 | 5% | 4% | 6% | 37% | 0.13 | 0.47 | 1.5 | 6.0 | 10% | longbowx252, ruby_crystalx252, bootsx251 |
| brixa | 49.6 [43.4, 55.8] | 246 | 0.87 | 0.74 | 22% | 3% | 6% | 1% | 0.30 | 0.56 | 1.7 | 0.7 | 9% | long_swordx246, longbowx245, vampiric_bladex236 |
| vurmak | 49.6 [43.3, 55.9] | 238 | 0.96 | 0.81 | 20% | 6% | 1% | 24% | 0.36 | 0.29 | 0.9 | 2.8 | 10% | ruby_crystalx238, long_swordx232, cloth_armorx203 |
| quillan | 49.3 [43.5, 55.1] | 280 | 1.96 | 1.65 | 8% | 8% | 1% | 63% | 0.16 | 0.75 | 2.1 | 3.0 | 19% | longbowx280, ionian_charmx277, ruby_crystalx270 |
| kestrel | 48.4 [42.4, 54.5] | 256 | 1.32 | 1.12 | 54% | 7% | 0% | 8% | 0.36 | 0.34 | 1.0 | 1.7 | 13% | long_swordx256, longbowx256, vampiric_bladex249 |
| lumen | 48.3 [42.0, 54.7] | 236 | 0.57 | 0.49 | 50% | 1% | 0% | 1% | 0.27 | 0.31 | 0.9 | 0.1 | 6% | longbowx236, ruby_crystalx236, bootsx225 |
| sable | 47.8 [41.4, 54.3] | 226 | 2.23 | 1.89 | 3% | 42% | 0% | 38% | 0.23 | 0.35 | 1.0 | 3.9 | 21% | longbowx226, ionian_charmx223, ruby_crystalx208 |
| ossuar | 47.2 [41.1, 53.4] | 252 | 1.64 | 1.39 | 36% | 1% | 0% | 36% | 0.26 | 0.21 | 0.7 | 3.5 | 15% | long_swordx252, ruby_crystalx252, cloth_armorx245 |
| vellum | 46.4 [40.3, 52.6] | 248 | 1.92 | 1.62 | 3% | 0% | 3% | 68% | 0.27 | 0.60 | 1.8 | 3.3 | 19% | longbowx247, ionian_charmx237, ruby_crystalx225 |
| thornjaw | 46.1 [39.4, 52.9] | 206 | 0.81 | 0.69 | 13% | 4% | 1% | 3% | 0.28 | 0.46 | 1.4 | 0.1 | 8% | long_swordx206, ruby_crystalx206, vampiric_bladex187 |
| marrow | 44.6 [38.4, 50.9] | 240 | 1.43 | 1.21 | 6% | 0% | 0% | 46% | 0.17 | 0.25 | 0.8 | 4.3 | 13% | ruby_crystalx240, long_swordx239, cloth_armorx231 |
| dax | 44.2 [37.9, 50.8] | 226 | 0.94 | 0.79 | 12% | 25% | 4% | 4% | 0.29 | 0.51 | 1.6 | 0.9 | 9% | long_swordx226, longbowx226, vampiric_bladex221 |
| mossgrove | 44.0 [37.9, 50.2] | 248 | 0.78 | 0.66 | 22% | 1% | 1% | 4% | 0.31 | 0.42 | 1.3 | 3.1 | 8% | long_swordx248, ruby_crystalx248, vampiric_bladex241 |
| corvane | 40.1 [34.3, 46.1] | 262 | 0.46 | 0.39 | 54% | 0% | 0% | 4% | 0.31 | 0.53 | 1.7 | 0.8 | 5% | longbowx262, ruby_crystalx262, bootsx260 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [47.2, 52.8] | 1.03 |
| Jungle | 50.0 [47.2, 52.8] | 0.88 |
| Mid | 50.0 [47.2, 52.8] | 1.88 |
| Support | 50.0 [47.2, 52.8] | 0.96 |
| Top | 50.0 [47.2, 52.8] | 1.18 |

## 5. Games

- length: median 15.0, p10 12, p90 18
- end reasons: {'nexus': 593, 'round_limit_hp': 2, 'round_limit_kills': 1, 'round_limit_towers': 4} (draws 0)
- priority win rate: 48.0% [44.0, 52.0]
- north win rate: 50.0% [46.0, 54.0]
- length histogram: {10: 6, 11: 17, 12: 61, 13: 71, 14: 91, 15: 104, 16: 94, 17: 76, 18: 47, 19: 18, 20: 15}

## 6. Objectives

- takes per game: {'dragon': 1.7466666666666666, 'baron': 0.6733333333333333}
- median round taken: dragon 7.0, baron 12.0
- win rate when secured: {'dragon': 47.32824427480916, 'baron': 41.08910891089109}
- camp clears per game: {'raptors': 5.588333333333333, 'krugs': 5.18, 'blue_buff': 3.033333333333333, 'wolves': 5.491666666666666, 'dragon': 1.7466666666666666, 'red_buff': 2.8733333333333335, 'baron': 0.6733333333333333}

## 7. Structures

- first tower falls: median round 7.0, p10 5, p90 10
- games with at least one tower down: 100.0%
- first-tower win rate: 64.7%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.32 |
| base | 3.00 |
| chips_wave | 2.32 |
| champion_kill | 0.59 |
| tower_kill | 0.58 |
| dragon | 0.22 |
| blue_buff | 0.20 |
| red_buff | 0.10 |

| use | AP |
|---|---|
| shop | 8.33 |
| abilities | 1.63 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.94 | 47.7% | 52.8% | -5.1 |
| cloth_armor | 5 | 1.89 | 48.1% | 51.1% | -3.0 |
| control_ward | 2 | 0.10 | - | 50.0% | - |
| frost_charm | 2 | 0.04 | - | 50.0% | - |
| health_potion | 2 | 1.92 | - | 50.0% | - |
| ionian_charm | 8 | 1.97 | 46.9% | 51.8% | -4.9 |
| long_sword | 6 | 2.00 | 49.8% | 50.6% | -0.9 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.1 |
| ruby_crystal | 4 | 2.00 | 49.7% | 55.5% | -5.8 |
| stopwatch | 3 | 1.85 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.96 | 49.1% | 51.1% | -2.1 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 | 384 | 66.1 [61.3, 70.7] |
| T2_sieger | 426 | 58.2 [53.5, 62.8] |
| SM_g3_phase | 390 | 25.1 [21.1, 29.7] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| SM_g2_lane6 | 384 | 66.1 [61.3, 70.7] |  | sieger 66%, laner 34% | 1.0 |
| T2_sieger | 426 | 58.2 [53.5, 62.8] |  | - | - |
| SM_g3_phase | 390 | 25.1 [21.1, 29.7] |  | objective 38%, sieger 31%, laner 26%, brawler 5% | 5.1 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 40.34 per game
- that is 38.0% of all ability uses
- of which true snipes (from cover, two or more hexes away): 34.0% of all uses
- snipes aimed at a champion: 5.1 per game
- activations ending beside an enemy-held hexgroup (looking in): 60.4%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **ability usage: ashwyn.R** - used in 19.8% of affordable rounds with a legal target
2. **ability usage: bastion.W** - used in 0.7% of affordable rounds with a legal target
3. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
4. **ability usage: bastion.R** - used in 8.6% of affordable rounds with a legal target
5. **ability usage: bramblehide.Q** - used in 1.2% of affordable rounds with a legal target
