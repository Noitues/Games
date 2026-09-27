# Sim report batch_0054

## 1. Header

| field | value |
|---|---|
| rules | 1.8.0 |
| roster | 1.7.0 |
| ai | 1.3.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 120 |
| seed | 3801 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 3664.4s |
| engine tests | not run |
| generated | 2026-09-27 04:20:58 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 25 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 49/58 abilities outside the band; roster mean 15.4%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 52.5% [43.6, 61.2] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 17.0 [16.0, 19.0] | **INCONCLUSIVE** |
| >=95% of games end by Nexus kill before round 20 | 69.2% [60.4, 76.7] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | marrow, quillan, sable, vellum (roster mean 1.40 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 50.8% [42.0, 59.6] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 65.9 [51.1, 78.1] | 44 | 2.18 | 1.56 | 10% | 6% | 0% | 67% | 0.07 | 0.59 | 1.8 | 3.0 | 20% | longbowx44, ionian_charmx43, ruby_crystalx41 |
| grivven | 63.0 [48.6, 75.5] | 46 | 1.24 | 0.88 | 4% | 2% | 6% | 50% | 0.11 | 0.33 | 0.9 | 7.3 | 11% | longbowx46, ruby_crystalx46, bootsx45 |
| ashwyn | 59.1 [47.0, 70.1] | 66 | 2.09 | 1.49 | 6% | 57% | 0% | 20% | 0.14 | 0.71 | 2.0 | 2.0 | 19% | longbowx66, ruby_crystalx64, ionian_charmx64 |
| dax | 57.1 [44.1, 69.2] | 56 | 1.07 | 0.76 | 14% | 32% | 4% | 2% | 0.32 | 0.41 | 1.2 | 0.7 | 10% | long_swordx56, longbowx56, vampiric_bladex51 |
| ossuar | 57.1 [42.2, 70.9] | 42 | 1.77 | 1.26 | 10% | 1% | 0% | 59% | 0.10 | 0.19 | 0.5 | 4.9 | 15% | long_swordx42, ruby_crystalx42, cloth_armorx40 |
| sylphine | 56.5 [42.2, 69.8] | 46 | 0.90 | 0.65 | 11% | 2% | 1% | 8% | 0.22 | 0.33 | 1.0 | 0.1 | 8% | long_swordx46, ruby_crystalx46, vampiric_bladex42 |
| brixa | 54.3 [40.2, 67.8] | 46 | 1.00 | 0.71 | 25% | 2% | 8% | 1% | 0.24 | 0.37 | 1.0 | 0.9 | 9% | long_swordx46, longbowx46, vampiric_bladex43 |
| rictus | 54.2 [40.3, 67.4] | 48 | 0.88 | 0.63 | 16% | 2% | 23% | 0% | 0.17 | 0.75 | 2.3 | 2.1 | 8% | long_swordx48, ruby_crystalx48, vampiric_bladex43 |
| orrin | 54.0 [40.4, 67.0] | 50 | 1.19 | 0.85 | 4% | 20% | 1% | 0% | 0.20 | 0.52 | 1.6 | 0.0 | 10% | long_swordx50, longbowx50, vampiric_bladex50 |
| pallas | 54.0 [40.4, 67.0] | 50 | 1.51 | 1.08 | 9% | 0% | 1% | 72% | 0.06 | 0.46 | 1.3 | 5.2 | 13% | longbowx50, ruby_crystalx50, bootsx49 |
| vellum | 53.1 [36.4, 69.1] | 32 | 2.11 | 1.51 | 5% | 0% | 0% | 65% | 0.28 | 0.50 | 1.5 | 3.1 | 19% | ionian_charmx32, longbowx32, ruby_crystalx30 |
| kaelis | 52.1 [38.3, 65.5] | 48 | 0.81 | 0.58 | 19% | 2% | 6% | 4% | 0.08 | 0.25 | 0.8 | 0.6 | 8% | long_swordx48, ruby_crystalx48, cloth_armorx46 |
| mossgrove | 51.9 [38.7, 64.9] | 52 | 0.96 | 0.69 | 24% | 3% | 1% | 3% | 0.15 | 0.21 | 0.6 | 3.1 | 9% | long_swordx52, ruby_crystalx52, vampiric_bladex47 |
| lumen | 50.0 [35.2, 64.8] | 40 | 0.63 | 0.45 | 51% | 0% | 0% | 1% | 0.12 | 0.23 | 0.6 | 0.1 | 6% | longbowx40, ruby_crystalx40, bootsx37 |
| marrow | 50.0 [36.6, 63.4] | 50 | 2.35 | 1.68 | 4% | 0% | 0% | 57% | 0.24 | 0.14 | 0.4 | 0.0 | 20% | long_swordx50, ruby_crystalx50, cloth_armorx43 |
| vurmak | 46.8 [34.9, 59.0] | 62 | 1.07 | 0.77 | 17% | 6% | 1% | 23% | 0.35 | 0.29 | 0.9 | 2.7 | 10% | ruby_crystalx62, long_swordx60, cloth_armorx51 |
| thornjaw | 45.2 [31.2, 60.1] | 42 | 0.97 | 0.70 | 13% | 3% | 1% | 2% | 0.26 | 0.17 | 0.6 | 0.1 | 8% | long_swordx42, ruby_crystalx42, vampiric_bladex39 |
| bastion | 44.7 [30.1, 60.3] | 38 | 2.07 | 1.48 | 75% | 0% | 0% | 5% | 0.45 | 0.13 | 0.4 | 1.1 | 18% | cloth_armorx38, long_swordx38, ruby_crystalx38 |
| wisp | 42.9 [30.8, 55.9] | 56 | 1.76 | 1.26 | 7% | 68% | 1% | 8% | 0.11 | 0.50 | 1.4 | 5.3 | 15% | longbowx56, ruby_crystalx55, bootsx49 |
| veyra | 42.6 [30.3, 55.8] | 54 | 1.20 | 0.86 | 1% | 68% | 0% | 1% | 0.52 | 0.37 | 1.1 | 0.3 | 11% | long_swordx54, longbowx51, vampiric_bladex46 |
| bramblehide | 42.3 [29.9, 55.8] | 52 | 1.55 | 1.10 | 2% | 14% | 1% | 29% | 0.10 | 0.25 | 0.8 | 3.4 | 13% | long_swordx52, ruby_crystalx52, vampiric_bladex49 |
| corvane | 41.7 [28.8, 55.7] | 48 | 0.30 | 0.21 | 29% | 0% | 0% | 3% | 0.25 | 0.62 | 1.9 | 2.9 | 3% | longbowx48, ruby_crystalx48, bootsx46 |
| kestrel | 38.2 [23.9, 55.0] | 34 | 1.57 | 1.12 | 73% | 5% | 0% | 6% | 0.15 | 0.12 | 0.3 | 1.5 | 13% | long_swordx34, longbowx34, vampiric_bladex34 |
| sable | 36.0 [24.1, 49.9] | 50 | 2.38 | 1.70 | 2% | 47% | 0% | 35% | 0.12 | 0.10 | 0.3 | 3.8 | 22% | longbowx50, ionian_charmx49, ruby_crystalx45 |
| noctis | 35.4 [23.4, 49.6] | 48 | 1.46 | 1.04 | 79% | 0% | 8% | 1% | 0.35 | 0.27 | 0.7 | 0.1 | 14% | longbowx48, ionian_charmx47, ruby_crystalx45 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.18 |
| Jungle | 50.0 [43.7, 56.3] | 1.06 |
| Mid | 50.0 [43.7, 56.3] | 2.04 |
| Support | 50.0 [43.7, 56.3] | 1.13 |
| Top | 50.0 [43.7, 56.3] | 1.57 |

## 5. Games

- length: median 17.0, p10 12, p90 20
- end reasons: {'nexus': 83, 'round_limit_towers': 33, 'round_limit_kills': 1, 'round_limit_hp': 3} (draws 0)
- priority win rate: 52.5% [43.6, 61.2]
- north win rate: 50.8% [42.0, 59.6]
- length histogram: {8: 1, 9: 4, 10: 2, 11: 4, 12: 10, 13: 10, 14: 10, 15: 4, 16: 13, 17: 8, 18: 5, 19: 9, 20: 40}

## 6. Objectives

- takes per game: {'dragon': 2.3833333333333333, 'baron': 1.075}
- median round taken: dragon 10.0, baron 12
- win rate when secured: {'dragon': 46.85314685314685, 'baron': 42.63565891472868}
- camp clears per game: {'wolves': 6.766666666666667, 'raptors': 7.025, 'krugs': 6.691666666666666, 'dragon': 2.3833333333333333, 'red_buff': 3.8833333333333333, 'blue_buff': 4.1, 'baron': 1.075}

## 7. Structures

- first tower falls: median round 5.0, p10 3, p90 8
- games with at least one tower down: 100.0%
- first-tower win rate: 84.2%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.84 |
| base | 3.00 |
| chips_wave | 2.92 |
| tower_kill | 0.48 |
| champion_kill | 0.32 |
| dragon | 0.28 |
| blue_buff | 0.25 |
| red_buff | 0.14 |

| use | AP |
|---|---|
| shop | 8.98 |
| abilities | 1.78 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.88 | 46.5% | 57.1% | -10.6 |
| cloth_armor | 5 | 1.82 | 49.4% | 50.6% | -1.2 |
| control_ward | 2 | 0.78 | - | 50.0% | - |
| frost_charm | 2 | 0.47 | - | 50.0% | - |
| health_potion | 2 | 1.73 | - | 50.0% | - |
| ionian_charm | 8 | 1.96 | 47.5% | 53.3% | -5.8 |
| long_sword | 6 | 2.00 | 49.3% | 52.1% | -2.9 |
| longbow | 6 | 2.00 | 49.9% | 50.1% | -0.2 |
| ruby_crystal | 4 | 2.00 | 49.3% | 62.5% | -13.2 |
| stopwatch | 3 | 1.73 | - | 50.0% | - |
| swift_tonic | 1 | 1.95 | - | 50.0% | - |
| vampiric_blade | 5 | 1.91 | 48.3% | 52.5% | -4.1 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 93.1 [83.6, 97.3] |
| T2_laner | 54 | 57.4 [44.2, 69.7] |
| T2_objective | 42 | 40.5 [27.0, 55.5] |
| T2_warder | 38 | 23.7 [13.0, 39.2] |
| T2_brawler | 48 | 18.8 [10.2, 31.9] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 55.20 per game
- that is 46.4% of all ability uses
- of which true snipes (from cover, two or more hexes away): 41.8% of all uses
- snipes aimed at a champion: 7.0 per game
- activations ending beside an enemy-held hexgroup (looking in): 44.1%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **>=95% of games end by Nexus kill before round 20** - 69.2% [60.4, 76.7]
2. **ability usage: ashwyn.R** - used in 20.5% of affordable rounds with a legal target
3. **ability usage: bastion.W** - used in 0.2% of affordable rounds with a legal target
4. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
5. **ability usage: bastion.R** - used in 4.5% of affordable rounds with a legal target

## 12. Delta vs batch_0051

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -5.5 | -0.32 | no |
| bastion | +4.2 | +0.07 | no |
| bramblehide | +0.0 | +0.05 | no |
| brixa | +6.5 | -0.04 | no |
| corvane | -4.2 | -0.05 | no |
| dax | -3.6 | +0.12 | no |
| grivven | +10.9 | +0.14 | no |
| kaelis | -11.7 | +0.10 | no |
| kestrel | -13.3 | +0.06 | no |
| lumen | +2.5 | +0.01 | no |
| marrow | +2.0 | +0.11 | no |
| mossgrove | +6.8 | +0.01 | no |
| noctis | +0.0 | +0.07 | no |
| orrin | +10.0 | +0.07 | no |
| ossuar | +16.7 | -0.08 | no |
| pallas | +0.9 | +0.03 | no |
| quillan | +5.4 | -0.48 | no |
| rictus | +0.0 | -0.00 | no |
| sable | -2.0 | -0.40 | no |
| sylphine | -8.7 | +0.07 | no |
| thornjaw | +1.3 | +0.00 | no |
| vellum | +6.2 | +0.09 | no |
| veyra | -2.7 | +0.02 | no |
| vurmak | -6.5 | +0.01 | no |
| wisp | -8.1 | -0.83 | no |

- median length delta: +1.0
- nexus-kill rate delta: -5.8 pts
