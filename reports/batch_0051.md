# Sim report batch_0051

## 1. Header

| field | value |
|---|---|
| rules | 1.8.0 |
| roster | 1.6.0 |
| ai | 1.3.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 120 |
| seed | 3801 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 3325.8s |
| engine tests | not run |
| generated | 2026-09-24 19:05:19 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 25 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 51/58 abilities outside the band; roster mean 15.5%; 6 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 56.3% [47.3, 64.9] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 16.0 [15.5, 17.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 75.0% [66.6, 81.9] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, marrow, quillan, sable, wisp (roster mean 1.45 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 50.4% [41.6, 59.2] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sylphine | 65.2 [50.8, 77.3] | 46 | 0.84 | 0.58 | 10% | 3% | 1% | 7% | 0.33 | 0.33 | 1.0 | 0.2 | 7% | long_swordx46, ruby_crystalx46, vampiric_bladex39 |
| ashwyn | 64.6 [52.5, 75.1] | 65 | 2.41 | 1.66 | 5% | 60% | 0% | 18% | 0.17 | 0.68 | 1.8 | 0.0 | 21% | ionian_charmx66, longbowx66, ruby_crystalx62 |
| kaelis | 63.8 [49.5, 76.0] | 47 | 0.71 | 0.49 | 19% | 3% | 6% | 4% | 0.23 | 0.40 | 1.2 | 0.6 | 7% | ruby_crystalx48, long_swordx47, cloth_armorx44 |
| dax | 60.7 [47.6, 72.4] | 56 | 0.95 | 0.65 | 14% | 28% | 2% | 3% | 0.32 | 0.39 | 1.1 | 0.6 | 9% | long_swordx56, longbowx54, vampiric_bladex50 |
| quillan | 60.5 [45.6, 73.6] | 43 | 2.67 | 1.84 | 7% | 5% | 0% | 75% | 0.09 | 0.63 | 1.9 | 0.0 | 24% | longbowx44, ionian_charmx42, ruby_crystalx40 |
| rictus | 54.2 [40.3, 67.4] | 48 | 0.88 | 0.61 | 13% | 4% | 21% | 2% | 0.21 | 0.58 | 1.6 | 1.9 | 7% | long_swordx48, ruby_crystalx48, vampiric_bladex40 |
| vurmak | 53.2 [41.0, 65.1] | 62 | 1.06 | 0.73 | 18% | 4% | 1% | 23% | 0.48 | 0.27 | 0.8 | 2.5 | 10% | ruby_crystalx62, long_swordx60, cloth_armorx50 |
| pallas | 53.1 [39.4, 66.3] | 49 | 1.48 | 1.02 | 8% | 0% | 1% | 76% | 0.18 | 0.45 | 1.3 | 5.4 | 13% | longbowx50, ruby_crystalx50, bootsx47 |
| grivven | 52.2 [38.1, 65.9] | 46 | 1.09 | 0.76 | 4% | 2% | 6% | 41% | 0.04 | 0.28 | 0.8 | 6.3 | 10% | longbowx46, ruby_crystalx46, bootsx45 |
| kestrel | 51.5 [35.2, 67.5] | 33 | 1.51 | 1.04 | 71% | 6% | 0% | 5% | 0.27 | 0.15 | 0.4 | 1.1 | 13% | long_swordx34, longbowx33, vampiric_bladex33 |
| wisp | 50.9 [38.1, 63.6] | 55 | 2.59 | 1.79 | 3% | 77% | 1% | 5% | 0.25 | 0.56 | 1.5 | 0.0 | 21% | ruby_crystalx56, longbowx55, bootsx48 |
| marrow | 48.0 [34.8, 61.5] | 50 | 2.25 | 1.55 | 3% | 0% | 0% | 56% | 0.28 | 0.04 | 0.1 | 0.0 | 19% | ruby_crystalx50, long_swordx48, cloth_armorx43 |
| brixa | 47.8 [34.1, 61.9] | 46 | 1.04 | 0.72 | 28% | 3% | 7% | 0% | 0.33 | 0.28 | 0.8 | 0.9 | 9% | long_swordx46, longbowx46, vampiric_bladex45 |
| lumen | 47.5 [32.9, 62.5] | 40 | 0.62 | 0.43 | 52% | 0% | 0% | 0% | 0.15 | 0.28 | 0.8 | 0.1 | 6% | longbowx40, ruby_crystalx40, bootsx37 |
| vellum | 46.9 [30.9, 63.6] | 32 | 2.02 | 1.40 | 3% | 0% | 1% | 66% | 0.25 | 0.53 | 1.7 | 2.9 | 18% | longbowx32, ionian_charmx31, ruby_crystalx26 |
| corvane | 45.8 [32.6, 59.7] | 48 | 0.34 | 0.24 | 31% | 0% | 0% | 1% | 0.10 | 0.65 | 1.7 | 2.3 | 3% | longbowx48, ruby_crystalx48, bootsx42 |
| veyra | 45.3 [32.7, 58.5] | 53 | 1.17 | 0.81 | 2% | 69% | 0% | 1% | 0.40 | 0.42 | 1.2 | 0.3 | 11% | long_swordx54, longbowx52, vampiric_bladex46 |
| mossgrove | 45.1 [32.3, 58.6] | 51 | 0.95 | 0.66 | 25% | 4% | 0% | 4% | 0.14 | 0.35 | 1.1 | 2.9 | 9% | long_swordx52, ruby_crystalx51, vampiric_bladex46 |
| orrin | 44.0 [31.2, 57.7] | 50 | 1.12 | 0.78 | 3% | 17% | 1% | 0% | 0.18 | 0.60 | 1.8 | 0.0 | 10% | long_swordx50, longbowx50, vampiric_bladex44 |
| thornjaw | 43.9 [29.9, 59.0] | 41 | 0.97 | 0.67 | 12% | 4% | 1% | 2% | 0.15 | 0.10 | 0.2 | 0.1 | 9% | long_swordx42, ruby_crystalx42, vampiric_bladex38 |
| bramblehide | 42.3 [29.9, 55.8] | 52 | 1.50 | 1.03 | 2% | 16% | 0% | 26% | 0.12 | 0.19 | 0.6 | 3.1 | 12% | long_swordx52, ruby_crystalx52, vampiric_bladex50 |
| bastion | 40.5 [26.3, 56.5] | 37 | 2.00 | 1.38 | 74% | 0% | 0% | 3% | 0.49 | 0.14 | 0.4 | 0.7 | 17% | long_swordx38, ruby_crystalx38, cloth_armorx37 |
| ossuar | 40.5 [27.0, 55.5] | 42 | 1.85 | 1.28 | 7% | 1% | 0% | 62% | 0.17 | 0.14 | 0.5 | 4.9 | 15% | ruby_crystalx42, long_swordx41, cloth_armorx37 |
| sable | 38.0 [25.9, 51.8] | 50 | 2.78 | 1.92 | 2% | 55% | 0% | 27% | 0.14 | 0.20 | 0.5 | 1.2 | 24% | longbowx50, ionian_charmx46, ruby_crystalx42 |
| noctis | 35.4 [23.4, 49.6] | 48 | 1.38 | 0.95 | 78% | 0% | 7% | 1% | 0.33 | 0.35 | 1.1 | 0.1 | 13% | longbowx48, ionian_charmx46, ruby_crystalx45 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.13 |
| Jungle | 50.0 [43.7, 56.3] | 1.04 |
| Mid | 50.0 [43.7, 56.3] | 2.28 |
| Support | 50.0 [43.7, 56.3] | 1.30 |
| Top | 50.0 [43.7, 56.3] | 1.53 |

## 5. Games

- length: median 16.0, p10 11, p90 20
- end reasons: {'nexus': 90, 'round_limit_hp': 8, 'round_limit_kills': 3, 'round_limit_towers': 18, 'round_limit_draw': 1} (draws 1)
- priority win rate: 56.3% [47.3, 64.9]
- north win rate: 50.4% [41.6, 59.2]
- length histogram: {6: 2, 8: 1, 9: 3, 10: 6, 11: 8, 12: 8, 13: 8, 14: 10, 15: 4, 16: 15, 17: 12, 18: 6, 19: 4, 20: 33}

## 6. Objectives

- takes per game: {'dragon': 2.3916666666666666, 'baron': 1.0583333333333333}
- median round taken: dragon 9, baron 11
- win rate when secured: {'dragon': 43.81625441696113, 'baron': 43.2}
- camp clears per game: {'wolves': 6.925, 'raptors': 7.141666666666667, 'krugs': 6.691666666666666, 'blue_buff': 3.941666666666667, 'dragon': 2.3916666666666666, 'red_buff': 3.7916666666666665, 'baron': 1.0583333333333333}

## 7. Structures

- first tower falls: median round 4.0, p10 3, p90 7
- games with at least one tower down: 100.0%
- first-tower win rate: 74.8%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.00 |
| chips_wave | 3.01 |
| base | 3.00 |
| tower_kill | 0.50 |
| champion_kill | 0.33 |
| dragon | 0.29 |
| blue_buff | 0.25 |
| red_buff | 0.14 |

| use | AP |
|---|---|
| shop | 9.12 |
| abilities | 1.91 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.82 | 48.0% | 53.8% | -5.8 |
| cloth_armor | 5 | 1.76 | 48.9% | 50.9% | -2.0 |
| control_ward | 2 | 0.77 | - | 50.0% | - |
| frost_charm | 2 | 0.42 | - | 50.0% | - |
| health_potion | 2 | 1.72 | - | 50.0% | - |
| ionian_charm | 8 | 1.93 | 48.4% | 52.0% | -3.6 |
| long_sword | 6 | 2.00 | 49.4% | 51.7% | -2.4 |
| longbow | 6 | 2.00 | 49.9% | 50.2% | -0.3 |
| ruby_crystal | 4 | 2.00 | 49.2% | 60.2% | -11.0 |
| stopwatch | 3 | 1.68 | - | 50.0% | - |
| swift_tonic | 1 | 1.98 | - | 50.0% | - |
| vampiric_blade | 5 | 1.88 | 47.5% | 53.5% | -6.0 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 89.7 [79.2, 95.2] |
| T2_laner | 53 | 54.7 [41.5, 67.3] |
| T2_objective | 42 | 40.5 [27.0, 55.5] |
| T2_brawler | 47 | 25.5 [15.3, 39.5] |
| T2_warder | 38 | 23.7 [13.0, 39.2] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 55.86 per game
- that is 46.7% of all ability uses
- of which true snipes (from cover, two or more hexes away): 42.2% of all uses
- snipes aimed at a champion: 7.6 per game
- activations ending beside an enemy-held hexgroup (looking in): 45.0%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **>=95% of games end by Nexus kill before round 20** - 75.0% [66.6, 81.9]
2. **ability usage: ashwyn.R** - used in 17.8% of affordable rounds with a legal target
3. **ability usage: bastion.W** - used in 0.0% of affordable rounds with a legal target
4. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
5. **ability usage: bastion.R** - used in 3.4% of affordable rounds with a legal target

## 12. Delta vs batch_0039

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +7.0 | -2.01 | no |
| bastion | -12.1 | -0.26 | no |
| bramblehide | -9.6 | -0.24 | no |
| brixa | +6.5 | -0.30 | no |
| corvane | +16.7 | -0.17 | no |
| dax | +0.0 | -0.37 | no |
| grivven | +8.7 | -1.21 | no |
| kaelis | +11.7 | -0.50 | no |
| kestrel | -1.4 | -0.28 | no |
| lumen | +10.0 | -0.18 | no |
| marrow | +10.0 | +0.01 | no |
| mossgrove | +0.9 | -0.22 | no |
| noctis | +2.1 | -0.14 | no |
| orrin | -6.0 | -0.60 | no |
| ossuar | -16.7 | -0.35 | no |
| pallas | -2.9 | -2.37 | no |
| quillan | -5.4 | -1.43 | no |
| rictus | +8.3 | -0.29 | no |
| sable | -14.0 | -2.86 | no |
| sylphine | +4.3 | -0.49 | no |
| thornjaw | -3.7 | -0.28 | no |
| vellum | +12.5 | -0.63 | no |
| veyra | +0.8 | -0.20 | no |
| vurmak | +1.6 | -0.37 | no |
| wisp | -25.9 | -2.46 | no |

- median length delta: -2.0
- nexus-kill rate delta: -3.3 pts
