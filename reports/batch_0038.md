# Sim report batch_0038

## 1. Header

| field | value |
|---|---|
| rules | 1.6.0 |
| roster | 1.6.0 |
| ai | 1.3.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 120 |
| seed | 3801 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 4123.0s |
| engine tests | not run |
| generated | 2026-09-23 06:33:07 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 1 FAIL / 24 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 50/58 abilities outside the band; roster mean 19.5%; 13 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 48.3% [39.6, 57.2] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 15.0 [14.0, 15.5] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 96.7% [91.7, 98.7] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.45 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 60.0% [51.1, 68.3] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 76.8 [64.2, 85.9] | 56 | 5.76 | 2.35 | 3% | 83% | 1% | 7% | 0.05 | 0.27 | 0.7 | 0.0 | 30% | bootsx56, longbowx56, ruby_crystalx56 |
| dax | 64.3 [51.2, 75.5] | 56 | 1.42 | 0.58 | 10% | 41% | 2% | 12% | 0.16 | 0.34 | 1.0 | 1.2 | 9% | long_swordx56, longbowx56, vampiric_bladex56 |
| sylphine | 63.0 [48.6, 75.5] | 46 | 1.41 | 0.57 | 14% | 1% | 0% | 8% | 0.15 | 0.17 | 0.5 | 0.1 | 9% | long_swordx46, ruby_crystalx46, vampiric_bladex46 |
| ashwyn | 60.6 [48.5, 71.5] | 66 | 5.40 | 2.21 | 4% | 72% | 0% | 17% | 0.06 | 0.52 | 1.5 | 0.0 | 31% | ionian_charmx66, long_swordx66, longbowx66 |
| quillan | 59.1 [44.4, 72.3] | 44 | 5.23 | 2.14 | 7% | 9% | 0% | 75% | 0.02 | 0.48 | 1.4 | 0.0 | 30% | ionian_charmx44, longbowx44, ruby_crystalx44 |
| vurmak | 58.1 [45.7, 69.5] | 62 | 1.56 | 0.64 | 17% | 1% | 1% | 58% | 0.15 | 0.31 | 0.9 | 4.1 | 10% | long_swordx62, ruby_crystalx62, cloth_armorx61 |
| bastion | 57.9 [42.2, 72.1] | 38 | 2.32 | 0.95 | 82% | 0% | 0% | 4% | 0.26 | 0.16 | 0.5 | 0.9 | 15% | cloth_armorx38, long_swordx38, ruby_crystalx38 |
| kestrel | 55.9 [39.5, 71.1] | 34 | 1.92 | 0.79 | 60% | 13% | 0% | 21% | 0.12 | 0.12 | 0.3 | 3.4 | 11% | long_swordx34, longbowx34, ruby_crystalx34 |
| rictus | 54.2 [40.3, 67.4] | 48 | 1.36 | 0.55 | 12% | 3% | 30% | 1% | 0.19 | 0.29 | 0.9 | 2.2 | 8% | long_swordx48, ruby_crystalx48, bootsx47 |
| brixa | 50.0 [36.1, 63.9] | 46 | 1.56 | 0.64 | 44% | 4% | 7% | 1% | 0.13 | 0.17 | 0.5 | 0.7 | 10% | long_swordx46, longbowx46, ruby_crystalx46 |
| thornjaw | 50.0 [35.5, 64.5] | 42 | 1.34 | 0.55 | 12% | 5% | 2% | 1% | 0.26 | 0.10 | 0.3 | 0.1 | 8% | long_swordx42, ruby_crystalx42, vampiric_bladex41 |
| bramblehide | 48.1 [35.1, 61.3] | 52 | 1.99 | 0.81 | 3% | 26% | 1% | 30% | 0.15 | 0.12 | 0.3 | 3.5 | 12% | long_swordx52, ruby_crystalx52, vampiric_bladex52 |
| marrow | 48.0 [34.8, 61.5] | 50 | 2.59 | 1.06 | 7% | 0% | 0% | 41% | 0.06 | 0.06 | 0.2 | 0.0 | 16% | cloth_armorx50, long_swordx50, ruby_crystalx50 |
| pallas | 48.0 [34.8, 61.5] | 50 | 4.32 | 1.77 | 3% | 0% | 1% | 87% | 0.08 | 0.28 | 0.7 | 4.4 | 25% | bootsx50, cloth_armorx50, longbowx50 |
| sable | 46.0 [33.0, 59.6] | 50 | 6.28 | 2.57 | 3% | 53% | 0% | 32% | 0.10 | 0.10 | 0.3 | 1.0 | 36% | ionian_charmx50, longbowx50, ruby_crystalx50 |
| grivven | 45.7 [32.2, 59.8] | 46 | 2.70 | 1.11 | 7% | 1% | 2% | 69% | 0.00 | 0.28 | 0.9 | 7.7 | 17% | bootsx46, longbowx46, ruby_crystalx46 |
| ossuar | 42.9 [29.1, 57.8] | 42 | 2.31 | 0.94 | 10% | 2% | 0% | 60% | 0.10 | 0.10 | 0.4 | 3.8 | 13% | cloth_armorx42, long_swordx42, ruby_crystalx42 |
| orrin | 42.0 [29.4, 55.8] | 50 | 1.88 | 0.77 | 7% | 39% | 1% | 0% | 0.12 | 0.24 | 0.6 | 0.0 | 12% | long_swordx50, longbowx50, ruby_crystalx50 |
| kaelis | 41.7 [28.8, 55.7] | 48 | 1.24 | 0.51 | 20% | 4% | 2% | 15% | 0.15 | 0.29 | 0.8 | 1.3 | 8% | cloth_armorx48, long_swordx48, ruby_crystalx48 |
| vellum | 40.6 [25.5, 57.7] | 32 | 2.78 | 1.14 | 6% | 0% | 1% | 80% | 0.12 | 0.44 | 1.3 | 2.7 | 19% | ionian_charmx32, longbowx32, ruby_crystalx32 |
| veyra | 38.9 [27.0, 52.2] | 54 | 1.45 | 0.59 | 2% | 69% | 0% | 7% | 0.17 | 0.30 | 0.9 | 1.4 | 10% | long_swordx54, longbowx54, vampiric_bladex53 |
| corvane | 37.5 [25.2, 51.6] | 48 | 0.55 | 0.23 | 49% | 0% | 0% | 2% | 0.04 | 0.48 | 1.4 | 3.5 | 4% | bootsx48, cloth_armorx48, longbowx48 |
| noctis | 37.5 [25.2, 51.6] | 48 | 1.65 | 0.68 | 73% | 0% | 17% | 1% | 0.12 | 0.35 | 1.0 | 0.1 | 13% | ionian_charmx48, longbowx48, ruby_crystalx48 |
| mossgrove | 36.5 [24.8, 50.1] | 52 | 1.22 | 0.50 | 35% | 5% | 0% | 5% | 0.19 | 0.23 | 0.8 | 3.4 | 8% | bootsx52, long_swordx52, ruby_crystalx52 |
| lumen | 35.0 [22.1, 50.5] | 40 | 0.89 | 0.36 | 61% | 0% | 0% | 0% | 0.05 | 0.12 | 0.3 | 0.0 | 6% | bootsx40, longbowx40, ruby_crystalx40 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.62 |
| Jungle | 50.0 [43.7, 56.3] | 1.47 |
| Mid | 50.0 [43.7, 56.3] | 4.46 |
| Support | 50.0 [43.7, 56.3] | 3.02 |
| Top | 50.0 [43.7, 56.3] | 1.96 |

## 5. Games

- length: median 15.0, p10 12, p90 18
- end reasons: {'nexus': 116, 'round_limit_towers': 3, 'round_limit_kills': 1} (draws 0)
- priority win rate: 48.3% [39.6, 57.2]
- north win rate: 60.0% [51.1, 68.3]
- length histogram: {11: 8, 12: 8, 13: 17, 14: 20, 15: 18, 16: 10, 17: 15, 18: 12, 19: 5, 20: 7}

## 6. Objectives

- takes per game: {'dragon': 2.058333333333333, 'baron': 0.9083333333333333}
- median round taken: dragon 9, baron 11
- win rate when secured: {'dragon': 42.51012145748988, 'baron': 52.293577981651374}
- camp clears per game: {'krugs': 6.366666666666666, 'wolves': 6.491666666666666, 'raptors': 6.733333333333333, 'blue_buff': 3.8333333333333335, 'red_buff': 3.841666666666667, 'dragon': 2.058333333333333, 'baron': 0.9083333333333333}

## 7. Structures

- first tower falls: median round 6.0, p10 4, p90 8
- games with at least one tower down: 100.0%
- first-tower win rate: 78.3%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 4.64 |
| chips_monster | 4.03 |
| chips_wave | 3.58 |
| base | 3.45 |
| blue_buff | 0.25 |
| champion_kill | 0.24 |
| red_buff | 0.17 |

| use | AP |
|---|---|
| shop | 11.94 |
| abilities | 2.42 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 52.3% | 23.4% | +28.9 |
| cloth_armor | 5 | 1.99 | 52.8% | 43.6% | +9.2 |
| control_ward | 2 | 1.32 | - | 50.0% | - |
| frost_charm | 2 | 1.03 | - | 50.0% | - |
| health_potion | 2 | 1.87 | - | 50.0% | - |
| ionian_charm | 8 | 2.00 | 52.4% | 30.6% | +21.8 |
| long_sword | 6 | 2.00 | 50.3% | 49.0% | +1.3 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 50.1% | 0.0% | +50.1 |
| stopwatch | 3 | 1.83 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.99 | 51.2% | 46.5% | +4.6 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 70.7 [58.0, 80.8] |
| T2_laner | 54 | 55.6 [42.4, 68.0] |
| T2_objective | 42 | 45.2 [31.2, 60.1] |
| T2_brawler | 48 | 35.4 [23.4, 49.6] |
| T2_warder | 38 | 34.2 [21.2, 50.1] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 67.81 per game
- that is 57.6% of all ability uses
- of which true snipes (from cover, two or more hexes away): 54.4% of all uses
- snipes aimed at a champion: 9.4 per game
- activations ending beside an enemy-held hexgroup (looking in): 57.0%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **champion win rate: wisp** - WR 76.8% [64.2, 85.9]
2. **economy outlier: sable** - 6.28 AP/round = 2.57x roster mean
3. **economy outlier: wisp** - 5.76 AP/round = 2.35x roster mean
4. **ability usage: ashwyn.R** - used in 16.5% of affordable rounds with a legal target
5. **ability usage: bastion.W** - used in 0.0% of affordable rounds with a legal target

## 12. Delta vs batch_0037

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -6.9 | -0.21 | no |
| bastion | +3.1 | -0.08 | no |
| bramblehide | -9.8 | +0.13 | no |
| brixa | +12.5 | +0.19 | no |
| corvane | +0.0 | -0.01 | no |
| dax | +26.0 | -0.12 | no |
| grivven | +10.2 | -0.09 | no |
| kaelis | -6.4 | -0.06 | no |
| kestrel | -4.1 | +0.02 | no |
| lumen | -1.0 | +0.08 | no |
| marrow | -6.0 | +0.10 | no |
| mossgrove | -11.7 | -0.08 | no |
| noctis | -5.0 | -0.03 | no |
| orrin | -8.0 | +0.12 | no |
| ossuar | -1.4 | -0.23 | no |
| pallas | -12.4 | +0.06 | no |
| quillan | +9.1 | -0.10 | no |
| rictus | +10.4 | +0.15 | no |
| sable | -16.1 | -0.05 | no |
| sylphine | +18.9 | +0.02 | no |
| thornjaw | -4.7 | -0.08 | no |
| vellum | +10.3 | +0.01 | no |
| veyra | -26.1 | -0.22 | no |
| vurmak | +8.1 | +0.14 | no |
| wisp | -5.8 | -0.12 | no |

- median length delta: +0.0
- nexus-kill rate delta: +3.3 pts
