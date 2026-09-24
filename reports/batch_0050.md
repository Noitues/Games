# Sim report batch_0050

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
| runtime | 5094.0s |
| engine tests | not run |
| generated | 2026-09-24 18:11:24 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 1 FAIL / 24 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 51/58 abilities outside the band; roster mean 16.3%; 7 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 58.0% [49.0, 66.5] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 20.0 [20.0, 20.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 15.0% [9.7, 22.5] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, wisp (roster mean 1.60 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 49.6% [40.8, 58.4] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 72.7 [58.2, 83.7] | 44 | 2.77 | 1.73 | 7% | 4% | 0% | 74% | 0.16 | 0.80 | 2.6 | 0.0 | 23% | ionian_charmx44, longbowx44, ruby_crystalx44 |
| ashwyn | 60.0 [47.9, 71.0] | 65 | 2.55 | 1.59 | 5% | 65% | 0% | 18% | 0.18 | 0.97 | 2.9 | 0.0 | 22% | ionian_charmx66, long_swordx66, longbowx66 |
| orrin | 59.2 [45.2, 71.8] | 49 | 1.26 | 0.78 | 5% | 19% | 1% | 0% | 0.27 | 0.63 | 1.9 | 0.0 | 11% | long_swordx50, longbowx50, vampiric_bladex50 |
| wisp | 58.9 [45.9, 70.8] | 56 | 2.97 | 1.85 | 3% | 81% | 1% | 6% | 0.21 | 0.46 | 1.6 | 0.0 | 22% | bootsx56, cloth_armorx56, longbowx56 |
| kaelis | 58.3 [44.3, 71.2] | 48 | 0.91 | 0.57 | 17% | 2% | 5% | 3% | 0.19 | 0.50 | 1.5 | 0.4 | 8% | cloth_armorx48, long_swordx48, ruby_crystalx48 |
| sylphine | 56.5 [42.2, 69.8] | 46 | 1.01 | 0.63 | 10% | 2% | 0% | 7% | 0.33 | 0.50 | 1.5 | 0.1 | 9% | bootsx46, long_swordx46, ruby_crystalx46 |
| dax | 55.4 [42.4, 67.6] | 56 | 1.07 | 0.67 | 14% | 31% | 3% | 3% | 0.36 | 0.59 | 1.8 | 0.9 | 9% | long_swordx56, longbowx56, vampiric_bladex56 |
| vurmak | 54.1 [41.7, 66.0] | 61 | 1.25 | 0.78 | 18% | 5% | 1% | 22% | 0.61 | 0.33 | 1.1 | 2.7 | 11% | cloth_armorx62, long_swordx62, ruby_crystalx62 |
| brixa | 53.3 [39.1, 67.1] | 45 | 1.14 | 0.71 | 29% | 3% | 6% | 1% | 0.51 | 0.53 | 1.6 | 0.8 | 10% | long_swordx46, longbowx46, ruby_crystalx46 |
| bramblehide | 52.9 [39.5, 65.9] | 51 | 1.72 | 1.08 | 3% | 18% | 0% | 30% | 0.22 | 0.33 | 1.1 | 3.7 | 14% | bootsx52, long_swordx52, ruby_crystalx52 |
| rictus | 52.1 [38.3, 65.5] | 48 | 1.07 | 0.67 | 14% | 3% | 24% | 2% | 0.38 | 0.75 | 2.2 | 2.4 | 9% | long_swordx48, ruby_crystalx48, vampiric_bladex48 |
| grivven | 51.1 [37.0, 65.0] | 45 | 1.22 | 0.76 | 7% | 2% | 6% | 45% | 0.09 | 0.51 | 1.8 | 8.2 | 11% | bootsx46, longbowx46, ruby_crystalx46 |
| mossgrove | 51.0 [37.7, 64.1] | 51 | 1.03 | 0.64 | 28% | 3% | 0% | 3% | 0.16 | 0.55 | 1.8 | 3.4 | 9% | long_swordx52, ruby_crystalx52, vampiric_bladex52 |
| corvane | 48.9 [35.3, 62.8] | 47 | 0.39 | 0.24 | 33% | 0% | 0% | 2% | 0.28 | 0.89 | 2.8 | 2.9 | 4% | bootsx48, cloth_armorx48, longbowx48 |
| bastion | 48.6 [33.4, 64.1] | 37 | 2.06 | 1.28 | 77% | 0% | 0% | 3% | 0.76 | 0.11 | 0.4 | 0.9 | 17% | cloth_armorx38, long_swordx38, ruby_crystalx38 |
| ossuar | 47.6 [33.4, 62.3] | 42 | 2.12 | 1.32 | 7% | 1% | 0% | 66% | 0.14 | 0.24 | 0.9 | 5.6 | 17% | cloth_armorx42, long_swordx42, ruby_crystalx42 |
| lumen | 47.5 [32.9, 62.5] | 40 | 0.71 | 0.44 | 54% | 0% | 0% | 1% | 0.20 | 0.30 | 0.8 | 0.1 | 7% | bootsx40, longbowx40, ruby_crystalx40 |
| pallas | 42.0 [29.4, 55.8] | 50 | 1.61 | 1.01 | 8% | 1% | 1% | 78% | 0.06 | 0.72 | 2.4 | 5.9 | 13% | bootsx50, cloth_armorx50, longbowx50 |
| veyra | 40.7 [28.7, 54.0] | 54 | 1.27 | 0.79 | 2% | 70% | 0% | 2% | 0.48 | 0.63 | 2.0 | 0.6 | 11% | long_swordx54, longbowx54, ruby_crystalx54 |
| noctis | 40.4 [27.6, 54.7] | 47 | 1.48 | 0.93 | 79% | 0% | 8% | 1% | 0.55 | 0.51 | 1.6 | 0.1 | 14% | ionian_charmx48, longbowx48, ruby_crystalx48 |
| marrow | 40.0 [27.6, 53.8] | 50 | 2.35 | 1.47 | 4% | 0% | 0% | 58% | 0.38 | 0.14 | 0.5 | 0.0 | 19% | cloth_armorx50, long_swordx50, ruby_crystalx50 |
| kestrel | 38.2 [23.9, 55.0] | 34 | 1.67 | 1.04 | 77% | 6% | 0% | 6% | 0.47 | 0.21 | 0.7 | 1.6 | 13% | long_swordx34, longbowx34, vampiric_bladex34 |
| sable | 36.0 [24.1, 49.9] | 50 | 3.00 | 1.87 | 1% | 52% | 0% | 34% | 0.22 | 0.30 | 1.0 | 1.6 | 25% | ionian_charmx50, longbowx50, ruby_crystalx50 |
| thornjaw | 35.7 [23.0, 50.8] | 42 | 1.18 | 0.74 | 12% | 2% | 1% | 2% | 0.21 | 0.21 | 0.7 | 0.2 | 10% | bootsx42, long_swordx42, ruby_crystalx42 |
| vellum | 34.4 [20.4, 51.7] | 32 | 2.27 | 1.41 | 3% | 0% | 2% | 68% | 0.31 | 0.59 | 1.9 | 3.2 | 19% | ionian_charmx32, longbowx32, ruby_crystalx32 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.25 |
| Jungle | 50.0 [43.7, 56.3] | 1.21 |
| Mid | 50.0 [43.7, 56.3] | 2.43 |
| Support | 50.0 [43.7, 56.3] | 1.46 |
| Top | 50.0 [43.7, 56.3] | 1.69 |

## 5. Games

- length: median 20.0, p10 19, p90 20
- end reasons: {'round_limit_hp': 22, 'round_limit_towers': 79, 'nexus': 18, 'round_limit_draw': 1} (draws 1)
- priority win rate: 58.0% [49.0, 66.5]
- north win rate: 49.6% [40.8, 58.4]
- length histogram: {16: 3, 17: 2, 18: 5, 19: 4, 20: 106}

## 6. Objectives

- takes per game: {'dragon': 3.275, 'baron': 1.6833333333333333}
- median round taken: dragon 11, baron 12.0
- win rate when secured: {'dragon': 44.73007712082262, 'baron': 51.0}
- camp clears per game: {'wolves': 8.791666666666666, 'raptors': 9.033333333333333, 'krugs': 8.766666666666667, 'blue_buff': 5.425, 'dragon': 3.275, 'red_buff': 5.275, 'baron': 1.6833333333333333}

## 7. Structures

- first tower falls: median round 12, p10 6, p90 17
- games with at least one tower down: 92.5%
- first-tower win rate: 92.8%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.16 |
| chips_wave | 3.39 |
| base | 3.00 |
| champion_kill | 0.37 |
| dragon | 0.35 |
| blue_buff | 0.27 |
| tower_kill | 0.19 |
| red_buff | 0.15 |

| use | AP |
|---|---|
| shop | 9.21 |
| abilities | 2.03 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 48.3% | 68.3% | -20.0 |
| cloth_armor | 5 | 2.00 | 46.8% | 56.2% | -9.4 |
| control_ward | 2 | 1.27 | - | 50.0% | - |
| frost_charm | 2 | 0.90 | - | 50.0% | - |
| health_potion | 2 | 1.84 | - | 50.0% | - |
| ionian_charm | 8 | 2.00 | 45.3% | 73.7% | -28.5 |
| long_sword | 6 | 2.00 | 49.6% | 51.4% | -1.8 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 49.9% | 100.0% | -50.1 |
| stopwatch | 3 | 1.88 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 48.6% | 53.9% | -5.4 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 96.6 [88.3, 99.0] |
| T2_laner | 53 | 50.9 [37.9, 63.9] |
| T2_objective | 42 | 38.1 [25.0, 53.2] |
| T2_warder | 37 | 35.1 [21.8, 51.2] |
| T2_brawler | 48 | 14.6 [7.2, 27.2] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 71.72 per game
- that is 46.6% of all ability uses
- of which true snipes (from cover, two or more hexes away): 42.3% of all uses
- snipes aimed at a champion: 10.3 per game
- activations ending beside an enemy-held hexgroup (looking in): 45.2%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **Median game length 13-18 rounds** - 20.0 [20.0, 20.0]
2. **>=95% of games end by Nexus kill before round 20** - 15.0% [9.7, 22.5]
3. **champion win rate: quillan** - WR 72.7% [58.2, 83.7]
4. **ability usage: ashwyn.R** - used in 18.0% of affordable rounds with a legal target
5. **ability usage: bastion.W** - used in 0.1% of affordable rounds with a legal target

## 12. Delta vs batch_0039

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +2.4 | -1.87 | no |
| bastion | -4.0 | -0.20 | no |
| bramblehide | +1.0 | -0.01 | no |
| brixa | +12.0 | -0.20 | no |
| corvane | +19.8 | -0.13 | no |
| dax | -5.4 | -0.25 | no |
| grivven | +7.6 | -1.09 | no |
| kaelis | +6.2 | -0.30 | no |
| kestrel | -14.7 | -0.12 | no |
| lumen | +10.0 | -0.10 | no |
| marrow | +2.0 | +0.11 | no |
| mossgrove | +6.7 | -0.14 | no |
| noctis | +7.1 | -0.04 | no |
| orrin | +9.2 | -0.46 | no |
| ossuar | -9.5 | -0.08 | no |
| pallas | -14.0 | -2.24 | no |
| quillan | +6.8 | -1.33 | no |
| rictus | +6.3 | -0.10 | no |
| sable | -16.0 | -2.64 | no |
| sylphine | -4.3 | -0.32 | no |
| thornjaw | -11.9 | -0.07 | no |
| vellum | +0.0 | -0.39 | no |
| veyra | -3.7 | -0.11 | no |
| vurmak | +2.5 | -0.19 | no |
| wisp | -17.9 | -2.09 | no |

- median length delta: +2.0
- nexus-kill rate delta: -63.3 pts
