# Sim report batch_0047

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
| runtime | 5788.8s |
| engine tests | not run |
| generated | 2026-09-24 16:31:55 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 25 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 53/58 abilities outside the band; roster mean 16.0%; 7 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 48.3% [39.6, 57.2] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 20.0 [20.0, 20.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 0.8% [0.1, 4.6] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 1.77 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 53.3% [44.4, 62.0] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 65.9 [51.1, 78.1] | 44 | 3.61 | 2.04 | 10% | 6% | 0% | 72% | 0.23 | 1.14 | 3.1 | 0.0 | 27% | longbowx44, ruby_crystalx44, ionian_charmx43 |
| kestrel | 64.7 [47.9, 78.5] | 34 | 1.61 | 0.91 | 74% | 8% | 0% | 8% | 0.82 | 0.12 | 0.4 | 2.2 | 12% | bootsx34, long_swordx34, longbowx34 |
| wisp | 62.5 [49.4, 74.0] | 56 | 4.04 | 2.29 | 3% | 81% | 1% | 4% | 0.30 | 0.75 | 2.4 | 0.0 | 27% | bootsx56, cloth_armorx56, longbowx56 |
| ashwyn | 62.1 [50.1, 72.9] | 66 | 3.59 | 2.03 | 4% | 71% | 0% | 14% | 0.39 | 1.23 | 4.0 | 0.0 | 27% | ionian_charmx66, long_swordx66, longbowx66 |
| grivven | 60.9 [46.5, 73.6] | 46 | 1.95 | 1.10 | 3% | 3% | 2% | 62% | 0.13 | 0.87 | 2.8 | 8.4 | 16% | bootsx46, longbowx46, ruby_crystalx46 |
| dax | 57.1 [44.1, 69.2] | 56 | 1.07 | 0.60 | 14% | 36% | 3% | 4% | 0.70 | 0.62 | 1.9 | 0.8 | 9% | long_swordx56, longbowx56, ruby_crystalx56 |
| sylphine | 56.5 [42.2, 69.8] | 46 | 0.92 | 0.52 | 10% | 3% | 1% | 8% | 0.61 | 0.41 | 1.2 | 0.2 | 7% | long_swordx46, ruby_crystalx46, vampiric_bladex45 |
| bramblehide | 55.8 [42.3, 68.4] | 52 | 1.48 | 0.84 | 3% | 23% | 1% | 15% | 0.33 | 0.38 | 1.2 | 2.7 | 11% | bootsx52, long_swordx52, ruby_crystalx52 |
| brixa | 54.3 [40.2, 67.8] | 46 | 1.11 | 0.63 | 31% | 2% | 8% | 0% | 0.46 | 0.61 | 1.7 | 0.8 | 9% | long_swordx46, longbowx46, vampiric_bladex46 |
| vurmak | 53.2 [41.0, 65.1] | 62 | 1.17 | 0.66 | 17% | 4% | 1% | 27% | 0.68 | 0.45 | 1.6 | 2.9 | 9% | long_swordx62, ruby_crystalx62, cloth_armorx61 |
| bastion | 52.6 [37.3, 67.5] | 38 | 1.97 | 1.12 | 84% | 0% | 0% | 0% | 0.76 | 0.26 | 0.9 | 0.1 | 15% | cloth_armorx38, long_swordx38, ruby_crystalx38 |
| kaelis | 52.1 [38.3, 65.5] | 48 | 0.86 | 0.49 | 18% | 3% | 5% | 4% | 0.42 | 0.48 | 1.5 | 0.6 | 7% | cloth_armorx48, long_swordx48, ruby_crystalx48 |
| mossgrove | 50.0 [36.9, 63.1] | 52 | 1.03 | 0.58 | 29% | 3% | 1% | 3% | 0.37 | 0.48 | 1.4 | 3.5 | 8% | bootsx52, long_swordx52, ruby_crystalx52 |
| rictus | 50.0 [36.4, 63.6] | 48 | 1.00 | 0.57 | 15% | 4% | 25% | 1% | 0.46 | 1.02 | 3.2 | 2.1 | 8% | bootsx48, long_swordx48, ruby_crystalx48 |
| marrow | 48.0 [34.8, 61.5] | 50 | 1.68 | 0.95 | 6% | 1% | 0% | 33% | 0.42 | 0.28 | 0.9 | 0.0 | 13% | cloth_armorx50, long_swordx50, ruby_crystalx50 |
| pallas | 48.0 [34.8, 61.5] | 50 | 2.93 | 1.66 | 4% | 0% | 1% | 84% | 0.18 | 0.90 | 3.1 | 5.0 | 21% | bootsx50, cloth_armorx50, longbowx50 |
| sable | 46.0 [33.0, 59.6] | 50 | 4.32 | 2.44 | 3% | 51% | 0% | 33% | 0.44 | 0.32 | 0.9 | 1.2 | 32% | ionian_charmx50, long_swordx50, longbowx50 |
| ossuar | 42.9 [29.1, 57.8] | 42 | 1.71 | 0.97 | 11% | 2% | 0% | 44% | 0.17 | 0.40 | 1.3 | 4.0 | 13% | cloth_armorx42, long_swordx42, ruby_crystalx42 |
| veyra | 40.7 [28.7, 54.0] | 54 | 1.24 | 0.70 | 3% | 73% | 0% | 1% | 0.57 | 0.48 | 1.5 | 0.3 | 11% | long_swordx54, longbowx54, ruby_crystalx54 |
| orrin | 38.0 [25.9, 51.8] | 50 | 1.20 | 0.68 | 6% | 19% | 0% | 0% | 0.44 | 0.76 | 2.4 | 0.0 | 9% | bootsx50, long_swordx50, longbowx50 |
| corvane | 37.5 [25.2, 51.6] | 48 | 0.41 | 0.23 | 36% | 0% | 0% | 1% | 0.21 | 0.88 | 2.9 | 2.9 | 4% | bootsx48, longbowx48, ruby_crystalx48 |
| lumen | 37.5 [24.2, 53.0] | 40 | 0.68 | 0.38 | 60% | 0% | 0% | 1% | 0.28 | 0.47 | 1.2 | 0.1 | 6% | bootsx40, longbowx40, ruby_crystalx40 |
| thornjaw | 35.7 [23.0, 50.8] | 42 | 1.10 | 0.62 | 9% | 4% | 3% | 4% | 0.52 | 0.31 | 1.0 | 0.3 | 8% | long_swordx42, ruby_crystalx42, vampiric_bladex42 |
| noctis | 35.4 [23.4, 49.6] | 48 | 1.42 | 0.81 | 79% | 0% | 9% | 1% | 0.54 | 0.71 | 2.2 | 0.1 | 13% | ionian_charmx48, long_swordx48, longbowx48 |
| vellum | 31.2 [18.0, 48.6] | 32 | 2.08 | 1.17 | 5% | 1% | 1% | 66% | 0.38 | 1.16 | 3.5 | 3.0 | 18% | ionian_charmx32, longbowx32, ruby_crystalx32 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.22 |
| Jungle | 50.0 [43.7, 56.3] | 1.11 |
| Mid | 50.0 [43.7, 56.3] | 3.11 |
| Support | 50.0 [43.7, 56.3] | 2.12 |
| Top | 50.0 [43.7, 56.3] | 1.44 |

## 5. Games

- length: median 20.0, p10 20, p90 20
- end reasons: {'round_limit_hp': 65, 'round_limit_towers': 54, 'nexus': 1} (draws 0)
- priority win rate: 48.3% [39.6, 57.2]
- north win rate: 53.3% [44.4, 62.0]
- length histogram: {20: 120}

## 6. Objectives

- takes per game: {'dragon': 3.466666666666667, 'baron': 1.8833333333333333}
- median round taken: dragon 11.0, baron 13.0
- win rate when secured: {'dragon': 55.04807692307692, 'baron': 52.21238938053097}
- camp clears per game: {'krugs': 9.5, 'wolves': 9.675, 'raptors': 9.933333333333334, 'red_buff': 6.208333333333333, 'blue_buff': 6.233333333333333, 'dragon': 3.466666666666667, 'baron': 1.8833333333333333}

## 7. Structures

- first tower falls: median round 16.0, p10 11, p90 20
- games with at least one tower down: 50.0%
- first-tower win rate: 98.3%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.52 |
| chips_wave | 3.98 |
| base | 3.00 |
| champion_kill | 0.46 |
| dragon | 0.34 |
| blue_buff | 0.31 |
| red_buff | 0.16 |
| tower_kill | 0.05 |

| use | AP |
|---|---|
| shop | 9.67 |
| abilities | 1.91 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 50.9% | 32.8% | +18.1 |
| cloth_armor | 5 | 1.99 | 51.0% | 47.4% | +3.5 |
| control_ward | 2 | 1.45 | - | 50.0% | - |
| frost_charm | 2 | 1.22 | - | 50.0% | - |
| health_potion | 2 | 1.92 | - | 50.0% | - |
| ionian_charm | 8 | 1.99 | 51.2% | 39.0% | +12.2 |
| long_sword | 6 | 2.00 | 50.2% | 49.4% | +0.8 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 50.0% | 0.0% | +50.0 |
| stopwatch | 3 | 1.94 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 50.7% | 47.9% | +2.8 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 87.9 [77.1, 94.0] |
| T2_laner | 54 | 55.6 [42.4, 68.0] |
| T2_objective | 42 | 42.9 [29.1, 57.8] |
| T2_warder | 38 | 26.3 [15.0, 42.0] |
| T2_brawler | 48 | 22.9 [13.3, 36.5] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 71.61 per game
- that is 46.4% of all ability uses
- of which true snipes (from cover, two or more hexes away): 41.8% of all uses
- snipes aimed at a champion: 14.7 per game
- activations ending beside an enemy-held hexgroup (looking in): 50.5%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **Median game length 13-18 rounds** - 20.0 [20.0, 20.0]
2. **>=95% of games end by Nexus kill before round 20** - 0.8% [0.1, 4.6]
3. **economy outlier: sable** - 4.32 AP/round = 2.44x roster mean
4. **economy outlier: wisp** - 4.04 AP/round = 2.29x roster mean
5. **ability usage: ashwyn.R** - used in 14.3% of affordable rounds with a legal target

## 12. Delta vs batch_0039

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +4.5 | -0.82 | no |
| bastion | +0.0 | -0.29 | no |
| bramblehide | +3.8 | -0.25 | no |
| brixa | +13.0 | -0.23 | no |
| corvane | +8.3 | -0.10 | no |
| dax | -3.6 | -0.25 | no |
| grivven | +17.4 | -0.35 | no |
| kaelis | +0.0 | -0.35 | no |
| kestrel | +11.8 | -0.18 | no |
| lumen | +0.0 | -0.13 | no |
| marrow | +10.0 | -0.56 | no |
| mossgrove | +5.8 | -0.14 | no |
| noctis | +2.1 | -0.10 | no |
| orrin | -12.0 | -0.52 | no |
| ossuar | -14.3 | -0.49 | no |
| pallas | -8.0 | -0.92 | no |
| quillan | +0.0 | -0.50 | no |
| rictus | +4.2 | -0.16 | no |
| sable | -6.0 | -1.32 | no |
| sylphine | -4.3 | -0.40 | no |
| thornjaw | -11.9 | -0.16 | no |
| vellum | -3.1 | -0.57 | no |
| veyra | -3.7 | -0.14 | no |
| vurmak | +1.6 | -0.26 | no |
| wisp | -14.3 | -1.01 | no |

- median length delta: +2.0
- nexus-kill rate delta: -77.5 pts
