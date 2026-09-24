# Sim report batch_0046

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
| runtime | 4880.8s |
| engine tests | not run |
| generated | 2026-09-24 16:16:34 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 1 FAIL / 24 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 53/58 abilities outside the band; roster mean 16.0%; 7 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 47.5% [38.8, 56.4] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 20.0 [20.0, 20.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 0.8% [0.1, 4.6] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 1.71 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 52.5% [43.6, 61.2] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 70.5 [55.8, 81.8] | 44 | 3.29 | 1.93 | 9% | 6% | 0% | 71% | 0.27 | 1.23 | 3.9 | 0.0 | 25% | ionian_charmx44, longbowx44, ruby_crystalx44 |
| dax | 66.1 [53.0, 77.1] | 56 | 1.09 | 0.64 | 12% | 34% | 3% | 5% | 0.45 | 0.62 | 2.0 | 1.0 | 9% | long_swordx56, longbowx56, ruby_crystalx56 |
| grivven | 65.2 [50.8, 77.3] | 46 | 1.90 | 1.11 | 4% | 1% | 2% | 64% | 0.04 | 0.72 | 2.4 | 8.8 | 15% | bootsx46, cloth_armorx46, longbowx46 |
| bastion | 63.2 [47.3, 76.6] | 38 | 1.82 | 1.07 | 82% | 0% | 0% | 1% | 0.74 | 0.16 | 0.5 | 0.2 | 14% | bootsx38, cloth_armorx38, ionian_charmx38 |
| sylphine | 60.9 [46.5, 73.6] | 46 | 0.86 | 0.50 | 10% | 4% | 1% | 10% | 0.54 | 0.30 | 1.0 | 0.1 | 7% | long_swordx46, ruby_crystalx46, vampiric_bladex46 |
| wisp | 60.7 [47.6, 72.4] | 56 | 3.81 | 2.23 | 4% | 80% | 1% | 5% | 0.25 | 0.75 | 2.4 | 0.0 | 25% | bootsx56, longbowx56, ruby_crystalx56 |
| ashwyn | 57.6 [45.6, 68.8] | 66 | 3.50 | 2.05 | 4% | 71% | 0% | 15% | 0.24 | 1.15 | 3.7 | 0.0 | 25% | ionian_charmx66, long_swordx66, longbowx66 |
| kaelis | 52.1 [38.3, 65.5] | 48 | 0.78 | 0.46 | 16% | 3% | 5% | 4% | 0.42 | 0.40 | 1.3 | 0.6 | 6% | cloth_armorx48, long_swordx48, ruby_crystalx48 |
| bramblehide | 50.0 [36.9, 63.1] | 52 | 1.39 | 0.81 | 3% | 23% | 1% | 16% | 0.37 | 0.29 | 0.9 | 2.8 | 10% | bootsx52, long_swordx52, ruby_crystalx52 |
| brixa | 50.0 [36.1, 63.9] | 46 | 1.00 | 0.59 | 30% | 2% | 12% | 1% | 0.24 | 0.57 | 1.5 | 1.2 | 8% | long_swordx46, longbowx46, vampiric_bladex46 |
| vurmak | 48.4 [36.4, 60.6] | 62 | 1.10 | 0.64 | 18% | 6% | 2% | 25% | 0.55 | 0.40 | 1.4 | 2.8 | 9% | ruby_crystalx62, long_swordx61, cloth_armorx60 |
| mossgrove | 48.1 [35.1, 61.3] | 52 | 1.02 | 0.60 | 27% | 3% | 1% | 2% | 0.19 | 0.48 | 1.6 | 2.9 | 8% | long_swordx52, ruby_crystalx52, vampiric_bladex52 |
| rictus | 47.9 [34.5, 61.7] | 48 | 1.01 | 0.59 | 14% | 4% | 26% | 2% | 0.44 | 0.83 | 2.5 | 2.3 | 8% | bootsx48, long_swordx48, ruby_crystalx48 |
| ossuar | 45.2 [31.2, 60.1] | 42 | 1.75 | 1.02 | 13% | 1% | 0% | 47% | 0.31 | 0.29 | 0.9 | 4.0 | 13% | cloth_armorx42, long_swordx42, ruby_crystalx42 |
| kestrel | 44.1 [28.9, 60.5] | 34 | 1.57 | 0.92 | 74% | 6% | 0% | 7% | 0.68 | 0.15 | 0.5 | 1.9 | 11% | bootsx34, long_swordx34, longbowx34 |
| marrow | 44.0 [31.2, 57.7] | 50 | 1.63 | 0.95 | 7% | 1% | 0% | 31% | 0.34 | 0.20 | 0.7 | 0.0 | 12% | cloth_armorx50, long_swordx50, ruby_crystalx50 |
| orrin | 44.0 [31.2, 57.7] | 50 | 1.20 | 0.70 | 7% | 18% | 0% | 0% | 0.38 | 0.60 | 1.8 | 0.0 | 9% | long_swordx50, longbowx50, vampiric_bladex50 |
| thornjaw | 42.9 [29.1, 57.8] | 42 | 1.02 | 0.60 | 8% | 5% | 3% | 3% | 0.69 | 0.26 | 0.9 | 0.2 | 8% | bootsx42, long_swordx42, ruby_crystalx42 |
| veyra | 42.6 [30.3, 55.8] | 54 | 1.23 | 0.72 | 3% | 73% | 0% | 1% | 0.56 | 0.48 | 1.5 | 0.2 | 10% | long_swordx54, longbowx54, vampiric_bladex54 |
| pallas | 42.0 [29.4, 55.8] | 50 | 2.90 | 1.70 | 3% | 0% | 1% | 84% | 0.14 | 0.78 | 2.6 | 5.0 | 21% | bootsx50, longbowx50, ruby_crystalx50 |
| sable | 42.0 [29.4, 55.8] | 50 | 4.51 | 2.64 | 3% | 49% | 0% | 35% | 0.26 | 0.18 | 0.5 | 1.3 | 32% | bootsx50, ionian_charmx50, long_swordx50 |
| lumen | 40.0 [26.3, 55.4] | 40 | 0.65 | 0.38 | 61% | 0% | 0% | 1% | 0.30 | 0.42 | 1.4 | 0.1 | 6% | bootsx40, longbowx40, ruby_crystalx40 |
| corvane | 39.6 [27.0, 53.7] | 48 | 0.34 | 0.20 | 36% | 0% | 0% | 2% | 0.21 | 0.92 | 2.8 | 3.1 | 3% | bootsx48, longbowx48, ruby_crystalx48 |
| noctis | 37.5 [25.2, 51.6] | 48 | 1.34 | 0.79 | 79% | 0% | 8% | 0% | 0.40 | 0.67 | 2.0 | 0.0 | 12% | ionian_charmx48, longbowx48, ruby_crystalx48 |
| vellum | 37.5 [22.9, 54.7] | 32 | 1.96 | 1.15 | 4% | 1% | 2% | 67% | 0.28 | 1.06 | 3.5 | 3.1 | 17% | ionian_charmx32, longbowx32, ruby_crystalx32 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.19 |
| Jungle | 50.0 [43.7, 56.3] | 1.07 |
| Mid | 50.0 [43.7, 56.3] | 3.04 |
| Support | 50.0 [43.7, 56.3] | 2.03 |
| Top | 50.0 [43.7, 56.3] | 1.37 |

## 5. Games

- length: median 20.0, p10 20, p90 20
- end reasons: {'round_limit_towers': 59, 'round_limit_hp': 60, 'nexus': 1} (draws 0)
- priority win rate: 47.5% [38.8, 56.4]
- north win rate: 52.5% [43.6, 61.2]
- length histogram: {19: 1, 20: 119}

## 6. Objectives

- takes per game: {'dragon': 3.375, 'baron': 1.8333333333333333}
- median round taken: dragon 11, baron 13.5
- win rate when secured: {'dragon': 51.358024691358025, 'baron': 50.0}
- camp clears per game: {'krugs': 9.316666666666666, 'wolves': 9.5, 'raptors': 9.616666666666667, 'red_buff': 5.958333333333333, 'blue_buff': 5.883333333333334, 'dragon': 3.375, 'baron': 1.8333333333333333}

## 7. Structures

- first tower falls: median round 16.0, p10 12, p90 19
- games with at least one tower down: 50.0%
- first-tower win rate: 100.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.60 |
| chips_wave | 3.95 |
| base | 3.69 |
| champion_kill | 0.41 |
| blue_buff | 0.29 |
| red_buff | 0.16 |
| tower_kill | 0.06 |

| use | AP |
|---|---|
| shop | 9.81 |
| abilities | 1.93 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 50.2% | 46.0% | +4.2 |
| cloth_armor | 5 | 1.98 | 49.1% | 52.3% | -3.1 |
| control_ward | 2 | 1.57 | - | 50.0% | - |
| frost_charm | 2 | 1.33 | - | 50.0% | - |
| health_potion | 2 | 1.93 | - | 50.0% | - |
| ionian_charm | 8 | 2.00 | 50.0% | 50.5% | -0.5 |
| long_sword | 6 | 2.00 | 50.2% | 49.4% | +0.8 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 50.0% | 33.3% | +16.7 |
| stopwatch | 3 | 1.94 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 49.9% | 50.4% | -0.5 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 93.1 [83.6, 97.3] |
| T2_laner | 54 | 50.0 [37.1, 62.9] |
| T2_objective | 42 | 38.1 [25.0, 53.2] |
| T2_warder | 38 | 34.2 [21.2, 50.1] |
| T2_brawler | 48 | 20.8 [11.7, 34.3] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 71.46 per game
- that is 45.8% of all ability uses
- of which true snipes (from cover, two or more hexes away): 41.2% of all uses
- snipes aimed at a champion: 14.7 per game
- activations ending beside an enemy-held hexgroup (looking in): 50.6%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **Median game length 13-18 rounds** - 20.0 [20.0, 20.0]
2. **>=95% of games end by Nexus kill before round 20** - 0.8% [0.1, 4.6]
3. **economy outlier: sable** - 4.51 AP/round = 2.64x roster mean
4. **champion win rate: quillan** - WR 70.5% [55.8, 81.8]
5. **ability usage: ashwyn.R** - used in 15.5% of affordable rounds with a legal target

## 12. Delta vs batch_0039

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +0.0 | -0.92 | no |
| bastion | +10.5 | -0.44 | no |
| bramblehide | -1.9 | -0.34 | no |
| brixa | +8.7 | -0.34 | no |
| corvane | +10.4 | -0.17 | no |
| dax | +5.4 | -0.22 | no |
| grivven | +21.7 | -0.40 | no |
| kaelis | +0.0 | -0.43 | no |
| kestrel | -8.8 | -0.22 | no |
| lumen | +2.5 | -0.16 | no |
| marrow | +6.0 | -0.61 | no |
| mossgrove | +3.8 | -0.15 | no |
| noctis | +4.2 | -0.18 | no |
| orrin | -6.0 | -0.52 | no |
| ossuar | -11.9 | -0.45 | no |
| pallas | -14.0 | -0.95 | no |
| quillan | +4.5 | -0.81 | no |
| rictus | +2.1 | -0.15 | no |
| sable | -10.0 | -1.13 | no |
| sylphine | +0.0 | -0.46 | no |
| thornjaw | -4.8 | -0.23 | no |
| vellum | +3.1 | -0.69 | no |
| veyra | -1.9 | -0.15 | no |
| vurmak | -3.2 | -0.34 | no |
| wisp | -16.1 | -1.25 | no |

- median length delta: +2.0
- nexus-kill rate delta: -77.5 pts
