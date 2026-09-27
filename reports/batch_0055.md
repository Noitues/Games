# Sim report batch_0055

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
| runtime | 3194.0s |
| engine tests | not run |
| generated | 2026-09-27 04:14:29 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 25 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 15.6%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 61.7% [52.7, 69.9] | **FAIL** |
| Median game length 13-18 rounds | 16.0 [15.0, 17.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 75.8% [67.4, 82.6] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, marrow, quillan, sable, wisp (roster mean 1.43 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 50.0% [41.2, 58.8] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 68.2 [53.4, 80.0] | 44 | 2.57 | 1.80 | 8% | 6% | 0% | 75% | 0.07 | 0.64 | 2.0 | 0.0 | 22% | longbowx44, ionian_charmx39, ruby_crystalx38 |
| sylphine | 63.0 [48.6, 75.5] | 46 | 0.87 | 0.61 | 11% | 3% | 1% | 7% | 0.30 | 0.35 | 1.0 | 0.1 | 8% | long_swordx46, ruby_crystalx46, vampiric_bladex39 |
| dax | 62.5 [49.4, 74.0] | 56 | 0.98 | 0.68 | 15% | 28% | 2% | 3% | 0.27 | 0.36 | 1.0 | 0.6 | 9% | long_swordx56, longbowx53, vampiric_bladex49 |
| kaelis | 58.3 [44.3, 71.2] | 48 | 0.73 | 0.51 | 19% | 2% | 6% | 4% | 0.23 | 0.31 | 1.0 | 0.5 | 7% | ruby_crystalx48, long_swordx46, cloth_armorx41 |
| bastion | 57.9 [42.2, 72.1] | 38 | 1.95 | 1.36 | 74% | 0% | 0% | 3% | 0.39 | 0.08 | 0.2 | 0.6 | 17% | long_swordx38, ruby_crystalx38, cloth_armorx37 |
| lumen | 57.5 [42.2, 71.5] | 40 | 0.61 | 0.43 | 53% | 0% | 0% | 1% | 0.10 | 0.23 | 0.6 | 0.0 | 6% | longbowx40, ruby_crystalx40, bootsx34 |
| wisp | 55.4 [42.4, 67.6] | 56 | 2.68 | 1.87 | 4% | 77% | 1% | 6% | 0.18 | 0.45 | 1.2 | 0.0 | 22% | longbowx54, ruby_crystalx54, bootsx45 |
| ashwyn | 53.0 [41.2, 64.6] | 66 | 2.41 | 1.68 | 5% | 61% | 0% | 19% | 0.17 | 0.59 | 1.6 | 0.0 | 21% | longbowx66, ionian_charmx63, ruby_crystalx61 |
| orrin | 52.0 [38.5, 65.2] | 50 | 1.08 | 0.75 | 4% | 16% | 1% | 0% | 0.28 | 0.52 | 1.5 | 0.0 | 9% | long_swordx50, longbowx50, vampiric_bladex43 |
| grivven | 50.0 [36.1, 63.9] | 46 | 1.05 | 0.73 | 4% | 3% | 7% | 40% | 0.07 | 0.33 | 1.1 | 6.3 | 9% | longbowx46, ruby_crystalx46, bootsx44 |
| rictus | 50.0 [36.4, 63.6] | 48 | 0.87 | 0.60 | 13% | 4% | 22% | 2% | 0.27 | 0.65 | 1.9 | 2.0 | 7% | long_swordx48, ruby_crystalx48, vampiric_bladex41 |
| vurmak | 50.0 [37.9, 62.1] | 62 | 1.04 | 0.72 | 18% | 4% | 1% | 23% | 0.52 | 0.23 | 0.8 | 2.5 | 9% | ruby_crystalx62, long_swordx55, cloth_armorx50 |
| corvane | 47.9 [34.5, 61.7] | 48 | 0.31 | 0.21 | 32% | 1% | 0% | 1% | 0.12 | 0.65 | 1.9 | 2.7 | 3% | longbowx48, ruby_crystalx47, bootsx43 |
| brixa | 47.8 [34.1, 61.9] | 46 | 1.03 | 0.72 | 30% | 3% | 6% | 1% | 0.46 | 0.39 | 1.2 | 0.7 | 9% | long_swordx46, longbowx46, vampiric_bladex45 |
| ossuar | 47.6 [33.4, 62.3] | 42 | 1.78 | 1.24 | 8% | 1% | 0% | 61% | 0.14 | 0.14 | 0.5 | 4.9 | 15% | ruby_crystalx42, long_swordx41, cloth_armorx36 |
| thornjaw | 47.6 [33.4, 62.3] | 42 | 1.05 | 0.73 | 11% | 3% | 1% | 2% | 0.21 | 0.12 | 0.2 | 0.0 | 9% | long_swordx42, ruby_crystalx42, vampiric_bladex38 |
| vellum | 46.9 [30.9, 63.6] | 32 | 1.96 | 1.37 | 2% | 0% | 1% | 65% | 0.31 | 0.53 | 1.8 | 3.0 | 18% | longbowx32, ionian_charmx31, ruby_crystalx27 |
| veyra | 46.3 [33.7, 59.4] | 54 | 1.19 | 0.83 | 2% | 66% | 0% | 1% | 0.30 | 0.35 | 1.0 | 0.3 | 11% | long_swordx53, longbowx48, vampiric_bladex41 |
| bramblehide | 46.2 [33.3, 59.5] | 52 | 1.42 | 0.99 | 2% | 15% | 0% | 28% | 0.10 | 0.17 | 0.5 | 3.3 | 12% | long_swordx52, ruby_crystalx52, vampiric_bladex46 |
| mossgrove | 44.2 [31.6, 57.7] | 52 | 0.86 | 0.60 | 27% | 5% | 0% | 4% | 0.15 | 0.33 | 0.9 | 3.0 | 8% | long_swordx52, ruby_crystalx50, vampiric_bladex42 |
| noctis | 43.8 [30.7, 57.7] | 48 | 1.42 | 0.99 | 78% | 0% | 10% | 0% | 0.35 | 0.38 | 1.2 | 0.1 | 14% | longbowx48, ionian_charmx46, ruby_crystalx45 |
| pallas | 40.0 [27.6, 53.8] | 50 | 1.47 | 1.02 | 8% | 0% | 2% | 74% | 0.12 | 0.38 | 1.2 | 5.2 | 13% | longbowx50, ruby_crystalx49, bootsx47 |
| marrow | 38.0 [25.9, 51.8] | 50 | 2.26 | 1.58 | 3% | 0% | 0% | 56% | 0.16 | 0.04 | 0.1 | 0.0 | 19% | ruby_crystalx50, long_swordx47, cloth_armorx42 |
| sable | 38.0 [25.9, 51.8] | 50 | 2.69 | 1.88 | 2% | 52% | 0% | 29% | 0.10 | 0.16 | 0.4 | 1.5 | 23% | longbowx50, ionian_charmx42, ruby_crystalx42 |
| kestrel | 35.3 [21.5, 52.1] | 34 | 1.56 | 1.09 | 70% | 6% | 0% | 7% | 0.15 | 0.15 | 0.4 | 1.6 | 13% | long_swordx34, longbowx33, vampiric_bladex32 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.14 |
| Jungle | 50.0 [43.7, 56.3] | 1.02 |
| Mid | 50.0 [43.7, 56.3] | 2.24 |
| Support | 50.0 [43.7, 56.3] | 1.29 |
| Top | 50.0 [43.7, 56.3] | 1.51 |

## 5. Games

- length: median 16.0, p10 9, p90 20
- end reasons: {'nexus': 91, 'round_limit_towers': 24, 'round_limit_hp': 5} (draws 0)
- priority win rate: 61.7% [52.7, 69.9]
- north win rate: 50.0% [41.2, 58.8]
- length histogram: {5: 3, 8: 4, 9: 9, 10: 2, 11: 8, 12: 3, 13: 7, 14: 8, 15: 11, 16: 12, 17: 7, 18: 4, 19: 7, 20: 35}

## 6. Objectives

- takes per game: {'dragon': 2.2916666666666665, 'baron': 1.025}
- median round taken: dragon 9, baron 12
- win rate when secured: {'dragon': 47.27272727272727, 'baron': 49.59349593495935}
- camp clears per game: {'wolves': 6.816666666666666, 'raptors': 7.083333333333333, 'krugs': 6.533333333333333, 'blue_buff': 3.941666666666667, 'dragon': 2.2916666666666665, 'red_buff': 3.816666666666667, 'baron': 1.025}

## 7. Structures

- first tower falls: median round 4.0, p10 3, p90 7
- games with at least one tower down: 100.0%
- first-tower win rate: 74.2%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.00 |
| base | 3.00 |
| chips_wave | 2.96 |
| tower_kill | 0.49 |
| champion_kill | 0.32 |
| dragon | 0.29 |
| blue_buff | 0.25 |
| red_buff | 0.15 |

| use | AP |
|---|---|
| shop | 9.05 |
| abilities | 1.92 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.77 | 49.7% | 50.6% | -0.9 |
| cloth_armor | 5 | 1.72 | 50.0% | 50.0% | +0.0 |
| control_ward | 2 | 0.72 | - | 50.0% | - |
| frost_charm | 2 | 0.38 | - | 50.0% | - |
| health_potion | 2 | 1.69 | - | 50.0% | - |
| ionian_charm | 8 | 1.84 | 49.6% | 50.5% | -0.8 |
| long_sword | 6 | 2.00 | 49.3% | 51.8% | -2.5 |
| longbow | 6 | 2.00 | 49.7% | 50.4% | -0.7 |
| ruby_crystal | 4 | 2.00 | 49.2% | 59.6% | -10.4 |
| stopwatch | 3 | 1.64 | - | 50.0% | - |
| swift_tonic | 1 | 1.98 | - | 50.0% | - |
| vampiric_blade | 5 | 1.79 | 48.4% | 52.1% | -3.7 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 87.9 [77.1, 94.0] |
| T2_laner | 54 | 53.7 [40.6, 66.3] |
| T2_objective | 42 | 38.1 [25.0, 53.2] |
| T2_warder | 38 | 34.2 [21.2, 50.1] |
| T2_brawler | 48 | 22.9 [13.3, 36.5] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 54.89 per game
- that is 47.0% of all ability uses
- of which true snipes (from cover, two or more hexes away): 42.5% of all uses
- snipes aimed at a champion: 7.5 per game
- activations ending beside an enemy-held hexgroup (looking in): 44.9%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **Priority (first player) win rate 48-52%** - 61.7% [52.7, 69.9]
2. **>=95% of games end by Nexus kill before round 20** - 75.8% [67.4, 82.6]
3. **ability usage: ashwyn.R** - used in 18.6% of affordable rounds with a legal target
4. **ability usage: bastion.W** - used in 0.0% of affordable rounds with a legal target
5. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target

## 12. Delta vs batch_0051

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -11.6 | -0.00 | no |
| bastion | +17.4 | -0.05 | no |
| bramblehide | +3.8 | -0.07 | no |
| brixa | +0.0 | -0.01 | no |
| corvane | +2.1 | -0.04 | no |
| dax | +1.8 | +0.03 | no |
| grivven | -2.2 | -0.04 | no |
| kaelis | -5.5 | +0.02 | no |
| kestrel | -16.2 | +0.05 | no |
| lumen | +10.0 | -0.01 | no |
| marrow | -10.0 | +0.01 | no |
| mossgrove | -0.9 | -0.09 | no |
| noctis | +8.3 | +0.04 | no |
| orrin | +8.0 | -0.04 | no |
| ossuar | +7.1 | -0.07 | no |
| pallas | -13.1 | -0.02 | no |
| quillan | +7.7 | -0.09 | no |
| rictus | -4.2 | -0.01 | no |
| sable | +0.0 | -0.09 | no |
| sylphine | -2.2 | +0.03 | no |
| thornjaw | +3.7 | +0.08 | no |
| vellum | +0.0 | -0.06 | no |
| veyra | +1.0 | +0.02 | no |
| vurmak | -3.2 | -0.02 | no |
| wisp | +4.4 | +0.09 | no |

- median length delta: +0.0
- nexus-kill rate delta: +0.8 pts
