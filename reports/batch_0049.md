# Sim report batch_0049

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
| runtime | 3364.1s |
| engine tests | not run |
| generated | 2026-09-24 17:22:45 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 25 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 15.2%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 51.7% [42.8, 60.4] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 20.0 [19.0, 20.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 49.2% [40.4, 58.0] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 1.66 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 55.0% [46.1, 63.6] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 68.2 [53.4, 80.0] | 44 | 3.25 | 1.96 | 9% | 5% | 0% | 71% | 0.39 | 0.98 | 3.0 | 0.0 | 26% | ionian_charmx44, longbowx44, ruby_crystalx44 |
| dax | 58.9 [45.9, 70.8] | 56 | 0.96 | 0.58 | 14% | 32% | 3% | 3% | 0.59 | 0.57 | 1.7 | 0.6 | 8% | long_swordx56, longbowx56, vampiric_bladex56 |
| grivven | 58.7 [44.3, 71.7] | 46 | 1.82 | 1.09 | 5% | 2% | 3% | 56% | 0.04 | 0.65 | 2.0 | 7.6 | 15% | longbowx46, ruby_crystalx46, bootsx45 |
| sylphine | 58.7 [44.3, 71.7] | 46 | 0.86 | 0.52 | 10% | 4% | 1% | 8% | 0.46 | 0.37 | 1.1 | 0.2 | 7% | long_swordx46, ruby_crystalx46, vampiric_bladex45 |
| ashwyn | 57.6 [45.6, 68.8] | 66 | 3.50 | 2.10 | 4% | 68% | 0% | 14% | 0.21 | 1.21 | 3.7 | 0.0 | 27% | ionian_charmx66, long_swordx66, longbowx66 |
| wisp | 57.1 [44.1, 69.2] | 56 | 3.55 | 2.14 | 4% | 73% | 1% | 5% | 0.29 | 0.68 | 2.2 | 0.0 | 25% | bootsx56, longbowx56, ruby_crystalx56 |
| mossgrove | 55.8 [42.3, 68.4] | 52 | 0.99 | 0.60 | 27% | 4% | 1% | 3% | 0.44 | 0.42 | 1.4 | 3.0 | 8% | long_swordx52, ruby_crystalx52, vampiric_bladex51 |
| kaelis | 54.2 [40.3, 67.4] | 48 | 0.84 | 0.50 | 20% | 2% | 5% | 4% | 0.27 | 0.58 | 1.7 | 0.5 | 7% | cloth_armorx48, long_swordx48, ruby_crystalx48 |
| vurmak | 53.2 [41.0, 65.1] | 62 | 1.10 | 0.66 | 18% | 5% | 1% | 22% | 0.77 | 0.34 | 1.2 | 2.5 | 9% | cloth_armorx62, long_swordx62, ruby_crystalx62 |
| bastion | 50.0 [34.8, 65.2] | 38 | 1.87 | 1.12 | 79% | 0% | 0% | 1% | 0.82 | 0.21 | 0.6 | 0.2 | 15% | cloth_armorx38, long_swordx38, ruby_crystalx38 |
| orrin | 50.0 [36.6, 63.4] | 50 | 1.12 | 0.67 | 5% | 19% | 1% | 0% | 0.34 | 0.64 | 1.8 | 0.0 | 9% | long_swordx50, longbowx50, vampiric_bladex50 |
| rictus | 47.9 [34.5, 61.7] | 48 | 0.89 | 0.53 | 15% | 4% | 23% | 1% | 0.42 | 0.85 | 2.7 | 2.2 | 7% | long_swordx48, ruby_crystalx48, vampiric_bladex48 |
| brixa | 47.8 [34.1, 61.9] | 46 | 1.03 | 0.62 | 30% | 3% | 7% | 1% | 0.43 | 0.59 | 1.7 | 0.7 | 8% | long_swordx46, longbowx46, vampiric_bladex45 |
| ossuar | 47.6 [33.4, 62.3] | 42 | 1.62 | 0.97 | 12% | 2% | 0% | 47% | 0.19 | 0.29 | 1.0 | 3.9 | 12% | cloth_armorx42, long_swordx42, ruby_crystalx42 |
| kestrel | 47.1 [31.5, 63.3] | 34 | 1.55 | 0.93 | 73% | 8% | 0% | 8% | 0.65 | 0.18 | 0.5 | 1.9 | 12% | long_swordx34, longbowx34, vampiric_bladex34 |
| bramblehide | 46.2 [33.3, 59.5] | 52 | 1.40 | 0.84 | 4% | 24% | 1% | 13% | 0.37 | 0.21 | 0.6 | 2.8 | 11% | long_swordx52, ruby_crystalx52, vampiric_bladex52 |
| pallas | 46.0 [33.0, 59.6] | 50 | 2.64 | 1.59 | 5% | 0% | 1% | 80% | 0.14 | 0.84 | 2.9 | 4.9 | 20% | bootsx50, longbowx50, ruby_crystalx50 |
| lumen | 45.0 [30.7, 60.2] | 40 | 0.64 | 0.38 | 54% | 0% | 0% | 1% | 0.17 | 0.50 | 1.6 | 0.1 | 6% | bootsx40, longbowx40, ruby_crystalx40 |
| veyra | 44.4 [32.0, 57.6] | 54 | 1.21 | 0.73 | 3% | 69% | 0% | 1% | 0.48 | 0.46 | 1.5 | 0.3 | 10% | long_swordx54, longbowx54, vampiric_bladex54 |
| marrow | 44.0 [31.2, 57.7] | 50 | 1.68 | 1.01 | 6% | 1% | 0% | 32% | 0.28 | 0.18 | 0.6 | 0.0 | 13% | cloth_armorx50, long_swordx50, ruby_crystalx50 |
| corvane | 41.7 [28.8, 55.7] | 48 | 0.35 | 0.21 | 32% | 0% | 0% | 4% | 0.44 | 0.79 | 2.5 | 3.1 | 3% | bootsx48, longbowx48, ruby_crystalx48 |
| vellum | 40.6 [25.5, 57.7] | 32 | 1.95 | 1.17 | 4% | 1% | 2% | 65% | 0.34 | 0.91 | 2.8 | 3.1 | 17% | ionian_charmx32, longbowx32, ruby_crystalx32 |
| thornjaw | 40.5 [27.0, 55.5] | 42 | 1.06 | 0.64 | 9% | 4% | 1% | 4% | 0.36 | 0.17 | 0.5 | 0.1 | 8% | long_swordx42, ruby_crystalx42, bootsx41 |
| sable | 40.0 [27.6, 53.8] | 50 | 4.34 | 2.61 | 4% | 46% | 0% | 32% | 0.26 | 0.14 | 0.4 | 1.2 | 32% | ionian_charmx50, longbowx50, ruby_crystalx50 |
| noctis | 39.6 [27.0, 53.7] | 48 | 1.38 | 0.83 | 80% | 0% | 7% | 1% | 0.42 | 0.58 | 1.7 | 0.1 | 13% | ionian_charmx48, longbowx48, ruby_crystalx47 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.15 |
| Jungle | 50.0 [43.7, 56.3] | 1.04 |
| Mid | 50.0 [43.7, 56.3] | 3.00 |
| Support | 50.0 [43.7, 56.3] | 1.90 |
| Top | 50.0 [43.7, 56.3] | 1.38 |

## 5. Games

- length: median 20.0, p10 15, p90 20
- end reasons: {'nexus': 59, 'round_limit_towers': 52, 'round_limit_kills': 3, 'round_limit_hp': 6} (draws 0)
- priority win rate: 51.7% [42.8, 60.4]
- north win rate: 55.0% [46.1, 63.6]
- length histogram: {9: 1, 12: 3, 13: 1, 14: 4, 15: 7, 16: 9, 17: 10, 18: 3, 19: 13, 20: 69}

## 6. Objectives

- takes per game: {'dragon': 3.0416666666666665, 'baron': 1.5666666666666667}
- median round taken: dragon 10, baron 12.0
- win rate when secured: {'dragon': 49.58904109589041, 'baron': 45.744680851063826}
- camp clears per game: {'krugs': 8.575, 'wolves': 8.658333333333333, 'raptors': 8.866666666666667, 'red_buff': 5.383333333333334, 'dragon': 3.0416666666666665, 'blue_buff': 5.383333333333334, 'baron': 1.5666666666666667}

## 7. Structures

- first tower falls: median round 8.0, p10 4, p90 14
- games with at least one tower down: 100.0%
- first-tower win rate: 90.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.37 |
| chips_wave | 3.71 |
| base | 3.00 |
| champion_kill | 0.42 |
| tower_kill | 0.32 |
| dragon | 0.31 |
| blue_buff | 0.29 |
| red_buff | 0.15 |

| use | AP |
|---|---|
| shop | 9.65 |
| abilities | 1.81 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.99 | 49.6% | 53.0% | -3.4 |
| cloth_armor | 5 | 2.00 | 49.6% | 50.7% | -1.1 |
| control_ward | 2 | 1.17 | - | 50.0% | - |
| frost_charm | 2 | 0.88 | - | 50.0% | - |
| health_potion | 2 | 1.82 | - | 50.0% | - |
| ionian_charm | 8 | 2.00 | 47.8% | 59.1% | -11.4 |
| long_sword | 6 | 2.00 | 50.1% | 49.8% | +0.2 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 49.9% | 60.0% | -10.1 |
| stopwatch | 3 | 1.83 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.99 | 49.4% | 51.5% | -2.1 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 94.8 [85.9, 98.2] |
| T2_laner | 54 | 57.4 [44.2, 69.7] |
| T2_objective | 42 | 42.9 [29.1, 57.8] |
| T2_warder | 38 | 23.7 [13.0, 39.2] |
| T2_brawler | 48 | 14.6 [7.2, 27.2] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 65.20 per game
- that is 46.4% of all ability uses
- of which true snipes (from cover, two or more hexes away): 42.1% of all uses
- snipes aimed at a champion: 13.0 per game
- activations ending beside an enemy-held hexgroup (looking in): 48.9%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **Median game length 13-18 rounds** - 20.0 [19.0, 20.0]
2. **>=95% of games end by Nexus kill before round 20** - 49.2% [40.4, 58.0]
3. **economy outlier: sable** - 4.34 AP/round = 2.61x roster mean
4. **ability usage: ashwyn.R** - used in 13.7% of affordable rounds with a legal target
5. **ability usage: bastion.W** - used in 0.1% of affordable rounds with a legal target

## 12. Delta vs batch_0039

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +0.0 | -0.92 | no |
| bastion | -2.6 | -0.39 | no |
| bramblehide | -5.8 | -0.34 | no |
| brixa | +6.5 | -0.31 | no |
| corvane | +12.5 | -0.17 | no |
| dax | -1.8 | -0.35 | no |
| grivven | +15.2 | -0.48 | no |
| kaelis | +2.1 | -0.38 | no |
| kestrel | -5.9 | -0.24 | no |
| lumen | +7.5 | -0.17 | no |
| marrow | +6.0 | -0.56 | no |
| mossgrove | +11.5 | -0.18 | no |
| noctis | +6.2 | -0.14 | no |
| orrin | +0.0 | -0.60 | no |
| ossuar | -9.5 | -0.58 | no |
| pallas | -10.0 | -1.21 | no |
| quillan | +2.3 | -0.85 | no |
| rictus | +2.1 | -0.28 | no |
| sable | -12.0 | -1.30 | no |
| sylphine | -2.2 | -0.47 | no |
| thornjaw | -7.1 | -0.19 | no |
| vellum | +6.2 | -0.70 | no |
| veyra | +0.0 | -0.16 | no |
| vurmak | +1.6 | -0.34 | no |
| wisp | -19.6 | -1.50 | no |

- median length delta: +2.0
- nexus-kill rate delta: -29.2 pts
