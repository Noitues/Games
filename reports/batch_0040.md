# Sim report batch_0040

## 1. Header

| field | value |
|---|---|
| rules | 1.7.0 |
| roster | 1.6.0 |
| ai | 1.3.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 120 |
| seed | 3801 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 3911.7s |
| engine tests | not run |
| generated | 2026-09-23 19:11:44 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 1 FAIL / 24 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 50/58 abilities outside the band; roster mean 19.5%; 10 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 46.7% [38.0, 55.6] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 17.0 [17.0, 18.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 79.2% [71.1, 85.5] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.19 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 50.0% [41.2, 58.8] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 75.0 [62.3, 84.5] | 56 | 4.93 | 2.26 | 4% | 80% | 0% | 10% | 0.30 | 0.54 | 1.6 | 0.0 | 27% | bootsx56, cloth_armorx56, longbowx56 |
| quillan | 63.6 [48.9, 76.2] | 44 | 4.31 | 1.97 | 8% | 9% | 0% | 74% | 0.14 | 1.00 | 2.9 | 0.0 | 28% | ionian_charmx44, longbowx44, ruby_crystalx44 |
| sylphine | 63.0 [48.6, 75.5] | 46 | 1.31 | 0.60 | 10% | 2% | 1% | 12% | 0.33 | 0.35 | 1.0 | 0.2 | 8% | long_swordx46, ruby_crystalx46, vampiric_bladex46 |
| kestrel | 61.8 [45.0, 76.1] | 34 | 1.81 | 0.83 | 65% | 12% | 0% | 18% | 0.38 | 0.15 | 0.4 | 3.3 | 11% | long_swordx34, longbowx34, vampiric_bladex34 |
| dax | 58.9 [45.9, 70.8] | 56 | 1.33 | 0.61 | 11% | 43% | 3% | 13% | 0.25 | 0.55 | 1.6 | 1.6 | 9% | long_swordx56, longbowx56, ruby_crystalx56 |
| vurmak | 56.5 [44.1, 68.1] | 62 | 1.47 | 0.67 | 14% | 2% | 1% | 55% | 0.48 | 0.55 | 1.7 | 4.2 | 10% | long_swordx62, ruby_crystalx62, cloth_armorx61 |
| ashwyn | 56.1 [44.1, 67.4] | 66 | 4.41 | 2.02 | 4% | 69% | 0% | 19% | 0.21 | 0.97 | 2.9 | 0.0 | 27% | bootsx66, ionian_charmx66, long_swordx66 |
| sable | 56.0 [42.3, 68.8] | 50 | 5.75 | 2.63 | 4% | 51% | 0% | 38% | 0.16 | 0.18 | 0.5 | 1.4 | 33% | bootsx50, ionian_charmx50, long_swordx50 |
| grivven | 54.3 [40.2, 67.8] | 46 | 2.27 | 1.04 | 5% | 1% | 0% | 70% | 0.02 | 0.57 | 1.8 | 8.2 | 15% | bootsx46, cloth_armorx46, longbowx46 |
| bastion | 52.6 [37.3, 67.5] | 38 | 2.30 | 1.05 | 86% | 0% | 0% | 2% | 0.26 | 0.24 | 0.8 | 0.4 | 15% | cloth_armorx38, long_swordx38, ruby_crystalx38 |
| mossgrove | 51.9 [38.7, 64.9] | 52 | 1.15 | 0.52 | 33% | 4% | 2% | 7% | 0.15 | 0.52 | 1.6 | 3.7 | 8% | long_swordx52, ruby_crystalx52, vampiric_bladex52 |
| ossuar | 50.0 [35.5, 64.5] | 42 | 2.24 | 1.02 | 8% | 4% | 0% | 58% | 0.10 | 0.14 | 0.5 | 4.0 | 13% | cloth_armorx42, long_swordx42, ruby_crystalx42 |
| pallas | 48.0 [34.8, 61.5] | 50 | 3.78 | 1.73 | 4% | 0% | 0% | 87% | 0.14 | 0.58 | 1.7 | 4.7 | 23% | bootsx50, cloth_armorx50, longbowx50 |
| veyra | 46.3 [33.7, 59.4] | 54 | 1.38 | 0.63 | 2% | 73% | 0% | 7% | 0.61 | 0.43 | 1.3 | 1.4 | 9% | long_swordx54, longbowx54, vampiric_bladex54 |
| bramblehide | 46.2 [33.3, 59.5] | 52 | 1.76 | 0.80 | 4% | 31% | 1% | 24% | 0.15 | 0.33 | 1.0 | 3.5 | 11% | bootsx52, long_swordx52, ruby_crystalx52 |
| kaelis | 45.8 [32.6, 59.7] | 48 | 1.24 | 0.57 | 19% | 4% | 3% | 12% | 0.23 | 0.50 | 1.5 | 1.2 | 9% | cloth_armorx48, long_swordx48, ruby_crystalx48 |
| rictus | 45.8 [32.6, 59.7] | 48 | 1.20 | 0.55 | 14% | 4% | 34% | 2% | 0.27 | 0.67 | 1.9 | 2.6 | 8% | bootsx48, long_swordx48, ruby_crystalx48 |
| brixa | 45.7 [32.2, 59.8] | 46 | 1.29 | 0.59 | 41% | 4% | 9% | 2% | 0.35 | 0.50 | 1.5 | 1.0 | 9% | long_swordx46, longbowx46, vampiric_bladex46 |
| marrow | 44.0 [31.2, 57.7] | 50 | 2.21 | 1.01 | 7% | 2% | 0% | 38% | 0.22 | 0.22 | 0.7 | 0.0 | 14% | cloth_armorx50, long_swordx50, ruby_crystalx50 |
| thornjaw | 42.9 [29.1, 57.8] | 42 | 1.24 | 0.57 | 10% | 7% | 4% | 3% | 0.38 | 0.19 | 0.6 | 0.3 | 8% | bootsx42, long_swordx42, ruby_crystalx42 |
| orrin | 40.0 [27.6, 53.8] | 50 | 1.73 | 0.79 | 8% | 36% | 1% | 1% | 0.24 | 0.58 | 1.7 | 0.0 | 11% | long_swordx50, longbowx50, vampiric_bladex50 |
| noctis | 37.5 [25.2, 51.6] | 48 | 1.54 | 0.70 | 76% | 0% | 16% | 0% | 0.31 | 0.54 | 1.7 | 0.1 | 12% | ionian_charmx48, longbowx48, ruby_crystalx48 |
| corvane | 33.3 [21.7, 47.5] | 48 | 0.51 | 0.23 | 55% | 0% | 0% | 3% | 0.25 | 0.67 | 2.0 | 4.0 | 4% | bootsx48, longbowx48, ruby_crystalx48 |
| lumen | 32.5 [20.1, 48.0] | 40 | 0.78 | 0.36 | 67% | 0% | 0% | 2% | 0.20 | 0.28 | 0.9 | 0.2 | 6% | bootsx40, longbowx40, ruby_crystalx40 |
| vellum | 28.1 [15.6, 45.4] | 32 | 2.69 | 1.23 | 5% | 0% | 1% | 80% | 0.16 | 0.78 | 2.5 | 2.8 | 18% | longbowx32, ruby_crystalx32, ionian_charmx31 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.48 |
| Jungle | 50.0 [43.7, 56.3] | 1.34 |
| Mid | 50.0 [43.7, 56.3] | 3.87 |
| Support | 50.0 [43.7, 56.3] | 2.60 |
| Top | 50.0 [43.7, 56.3] | 1.84 |

## 5. Games

- length: median 17.0, p10 15, p90 20
- end reasons: {'nexus': 95, 'round_limit_towers': 16, 'round_limit_hp': 9} (draws 0)
- priority win rate: 46.7% [38.0, 55.6]
- north win rate: 50.0% [41.2, 58.8]
- length histogram: {12: 1, 14: 9, 15: 18, 16: 15, 17: 20, 18: 15, 19: 10, 20: 32}

## 6. Objectives

- takes per game: {'dragon': 2.3666666666666667, 'baron': 1.0666666666666667}
- median round taken: dragon 10.0, baron 11.5
- win rate when secured: {'dragon': 45.42253521126761, 'baron': 47.65625}
- camp clears per game: {'wolves': 7.083333333333333, 'raptors': 7.366666666666666, 'krugs': 7.033333333333333, 'blue_buff': 4.316666666666666, 'dragon': 2.3666666666666667, 'red_buff': 4.283333333333333, 'baron': 1.0666666666666667}

## 7. Structures

- first tower falls: median round 8.0, p10 5, p90 11
- games with at least one tower down: 100.0%
- first-tower win rate: 73.3%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| base | 4.02 |
| chips_monster | 3.94 |
| chips_structure | 3.74 |
| chips_wave | 3.26 |
| champion_kill | 0.40 |
| blue_buff | 0.24 |
| red_buff | 0.17 |

| use | AP |
|---|---|
| shop | 11.01 |
| abilities | 2.38 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 51.1% | 28.8% | +22.3 |
| cloth_armor | 5 | 1.99 | 51.7% | 45.5% | +6.3 |
| control_ward | 2 | 1.47 | - | 50.0% | - |
| frost_charm | 2 | 1.31 | - | 50.0% | - |
| health_potion | 2 | 1.92 | - | 50.0% | - |
| ionian_charm | 8 | 1.99 | 51.3% | 36.0% | +15.3 |
| long_sword | 6 | 2.00 | 50.3% | 49.0% | +1.3 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 50.2% | 0.0% | +50.2 |
| stopwatch | 3 | 1.93 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 50.6% | 48.0% | +2.6 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 74.1 [61.6, 83.7] |
| T2_laner | 54 | 59.3 [46.0, 71.3] |
| T2_objective | 42 | 40.5 [27.0, 55.5] |
| T2_brawler | 48 | 33.3 [21.7, 47.5] |
| T2_warder | 38 | 31.6 [19.1, 47.5] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 57.21 per game
- that is 43.1% of all ability uses
- of which true snipes (from cover, two or more hexes away): 40.0% of all uses
- snipes aimed at a champion: 11.0 per game
- activations ending beside an enemy-held hexgroup (looking in): 57.4%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **champion win rate: wisp** - WR 75.0% [62.3, 84.5]
2. **>=95% of games end by Nexus kill before round 20** - 79.2% [71.1, 85.5]
3. **economy outlier: sable** - 5.75 AP/round = 2.63x roster mean
4. **economy outlier: wisp** - 4.93 AP/round = 2.26x roster mean
5. **ability usage: ashwyn.R** - used in 18.7% of affordable rounds with a legal target

## 12. Delta vs batch_0039

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -1.5 | -0.01 | no |
| bastion | +0.0 | +0.04 | no |
| bramblehide | -5.8 | +0.02 | no |
| brixa | +4.3 | -0.05 | no |
| corvane | +4.2 | -0.01 | no |
| dax | -1.8 | +0.02 | no |
| grivven | +10.9 | -0.04 | no |
| kaelis | -6.3 | +0.03 | no |
| kestrel | +8.8 | +0.02 | no |
| lumen | -5.0 | -0.03 | no |
| marrow | +6.0 | -0.03 | no |
| mossgrove | +7.7 | -0.02 | no |
| noctis | +4.2 | +0.02 | no |
| orrin | -10.0 | +0.01 | no |
| ossuar | -7.1 | +0.04 | no |
| pallas | -8.0 | -0.07 | no |
| quillan | -2.3 | +0.21 | no |
| rictus | +0.0 | +0.04 | no |
| sable | +4.0 | +0.12 | no |
| sylphine | +2.2 | -0.01 | no |
| thornjaw | -4.8 | -0.01 | no |
| vellum | -6.2 | +0.04 | no |
| veyra | +1.9 | +0.00 | no |
| vurmak | +4.8 | +0.04 | no |
| wisp | -1.8 | -0.13 | no |

- median length delta: -1.0
- nexus-kill rate delta: +0.8 pts
