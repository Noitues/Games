# Sim report batch_0048

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
| runtime | 4492.7s |
| engine tests | not run |
| generated | 2026-09-24 17:41:28 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 25 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 51/58 abilities outside the band; roster mean 15.5%; 6 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 43.3% [34.8, 52.3] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 20.0 [20.0, 20.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 30.0% [22.5, 38.7] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 1.72 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 51.7% [42.8, 60.4] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 65.9 [51.1, 78.1] | 44 | 3.29 | 1.91 | 9% | 5% | 1% | 67% | 0.25 | 1.00 | 3.0 | 0.0 | 26% | longbowx44, ruby_crystalx44, ionian_charmx43 |
| sylphine | 65.2 [50.8, 77.3] | 46 | 0.94 | 0.55 | 10% | 3% | 1% | 9% | 0.46 | 0.30 | 0.9 | 0.2 | 7% | long_swordx46, ruby_crystalx46, vampiric_bladex46 |
| dax | 62.5 [49.4, 74.0] | 56 | 1.03 | 0.60 | 13% | 31% | 3% | 4% | 0.71 | 0.54 | 1.7 | 0.9 | 8% | long_swordx56, longbowx56, ruby_crystalx56 |
| ashwyn | 62.1 [50.1, 72.9] | 66 | 3.46 | 2.02 | 5% | 68% | 0% | 14% | 0.26 | 1.20 | 3.9 | 0.0 | 26% | ionian_charmx66, long_swordx66, longbowx66 |
| grivven | 60.9 [46.5, 73.6] | 46 | 1.82 | 1.06 | 3% | 1% | 4% | 59% | 0.04 | 0.91 | 2.9 | 7.8 | 15% | bootsx46, longbowx46, ruby_crystalx46 |
| wisp | 58.9 [45.9, 70.8] | 56 | 3.80 | 2.21 | 4% | 77% | 1% | 5% | 0.25 | 0.54 | 1.7 | 0.0 | 26% | bootsx56, cloth_armorx56, longbowx56 |
| kaelis | 58.3 [44.3, 71.2] | 48 | 0.82 | 0.48 | 20% | 3% | 5% | 3% | 0.50 | 0.42 | 1.2 | 0.5 | 7% | cloth_armorx48, long_swordx48, ruby_crystalx48 |
| bastion | 52.6 [37.3, 67.5] | 38 | 1.89 | 1.10 | 81% | 0% | 0% | 0% | 0.79 | 0.18 | 0.6 | 0.0 | 15% | cloth_armorx38, long_swordx38, ruby_crystalx38 |
| brixa | 52.2 [38.1, 65.9] | 46 | 1.02 | 0.59 | 29% | 2% | 9% | 1% | 0.46 | 0.63 | 1.9 | 0.8 | 8% | long_swordx46, longbowx45, vampiric_bladex45 |
| vurmak | 51.6 [39.4, 63.6] | 62 | 1.17 | 0.68 | 18% | 6% | 1% | 23% | 0.61 | 0.34 | 1.0 | 2.5 | 9% | cloth_armorx62, long_swordx62, ruby_crystalx62 |
| mossgrove | 50.0 [36.9, 63.1] | 52 | 1.01 | 0.59 | 29% | 3% | 1% | 3% | 0.27 | 0.50 | 1.6 | 3.3 | 8% | long_swordx52, ruby_crystalx52, vampiric_bladex52 |
| orrin | 48.0 [34.8, 61.5] | 50 | 1.19 | 0.69 | 7% | 19% | 1% | 0% | 0.38 | 0.56 | 1.6 | 0.0 | 10% | long_swordx50, longbowx50, vampiric_bladex50 |
| pallas | 48.0 [34.8, 61.5] | 50 | 2.86 | 1.66 | 4% | 0% | 1% | 84% | 0.12 | 0.94 | 3.0 | 4.9 | 21% | bootsx50, cloth_armorx50, longbowx50 |
| rictus | 47.9 [34.5, 61.7] | 48 | 1.03 | 0.60 | 15% | 4% | 26% | 1% | 0.52 | 0.71 | 2.2 | 2.2 | 8% | bootsx48, long_swordx48, ruby_crystalx48 |
| bramblehide | 46.2 [33.3, 59.5] | 52 | 1.41 | 0.82 | 3% | 22% | 1% | 14% | 0.25 | 0.35 | 1.1 | 2.7 | 11% | long_swordx52, ruby_crystalx52, vampiric_bladex52 |
| ossuar | 45.2 [31.2, 60.1] | 42 | 1.66 | 0.97 | 11% | 2% | 0% | 44% | 0.19 | 0.33 | 1.1 | 4.0 | 12% | cloth_armorx42, long_swordx42, ruby_crystalx42 |
| corvane | 43.8 [30.7, 57.7] | 48 | 0.37 | 0.21 | 37% | 0% | 0% | 2% | 0.27 | 0.90 | 2.9 | 3.2 | 3% | bootsx48, longbowx48, ruby_crystalx48 |
| veyra | 42.6 [30.3, 55.8] | 54 | 1.28 | 0.75 | 3% | 71% | 0% | 2% | 0.59 | 0.50 | 1.5 | 0.4 | 11% | long_swordx54, longbowx54, ruby_crystalx54 |
| marrow | 42.0 [29.4, 55.8] | 50 | 1.72 | 1.00 | 7% | 1% | 0% | 34% | 0.28 | 0.26 | 0.9 | 0.0 | 14% | ruby_crystalx50, cloth_armorx49, long_swordx49 |
| sable | 42.0 [29.4, 55.8] | 50 | 4.36 | 2.54 | 3% | 50% | 0% | 32% | 0.32 | 0.20 | 0.6 | 1.0 | 32% | ionian_charmx50, long_swordx50, longbowx50 |
| kestrel | 41.2 [26.4, 57.8] | 34 | 1.62 | 0.94 | 76% | 7% | 0% | 5% | 0.82 | 0.12 | 0.3 | 1.4 | 12% | bootsx34, long_swordx34, longbowx34 |
| vellum | 40.6 [25.5, 57.7] | 32 | 2.03 | 1.18 | 4% | 0% | 2% | 66% | 0.34 | 0.91 | 3.0 | 2.9 | 18% | longbowx32, ruby_crystalx32, ionian_charmx31 |
| thornjaw | 40.5 [27.0, 55.5] | 42 | 1.08 | 0.63 | 10% | 4% | 2% | 3% | 0.48 | 0.31 | 1.0 | 0.1 | 8% | bootsx42, long_swordx42, ruby_crystalx42 |
| lumen | 35.0 [22.1, 50.5] | 40 | 0.68 | 0.39 | 59% | 0% | 0% | 0% | 0.20 | 0.45 | 1.5 | 0.0 | 6% | bootsx40, longbowx40, ruby_crystalx40 |
| noctis | 33.3 [21.7, 47.5] | 48 | 1.41 | 0.82 | 78% | 0% | 8% | 1% | 0.52 | 0.46 | 1.5 | 0.1 | 13% | ionian_charmx48, longbowx48, ruby_crystalx48 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.20 |
| Jungle | 50.0 [43.7, 56.3] | 1.10 |
| Mid | 50.0 [43.7, 56.3] | 3.02 |
| Support | 50.0 [43.7, 56.3] | 2.02 |
| Top | 50.0 [43.7, 56.3] | 1.41 |

## 5. Games

- length: median 20.0, p10 17, p90 20
- end reasons: {'round_limit_towers': 63, 'nexus': 36, 'round_limit_hp': 21} (draws 0)
- priority win rate: 43.3% [34.8, 52.3]
- north win rate: 51.7% [42.8, 60.4]
- length histogram: {11: 1, 12: 1, 13: 2, 14: 3, 15: 3, 16: 2, 17: 8, 18: 3, 19: 4, 20: 93}

## 6. Objectives

- takes per game: {'dragon': 3.2333333333333334, 'baron': 1.6833333333333333}
- median round taken: dragon 11.0, baron 12.0
- win rate when secured: {'dragon': 51.54639175257732, 'baron': 48.51485148514851}
- camp clears per game: {'krugs': 9.091666666666667, 'wolves': 9.1, 'raptors': 9.566666666666666, 'red_buff': 5.725, 'blue_buff': 5.883333333333334, 'dragon': 3.2333333333333334, 'baron': 1.6833333333333333}

## 7. Structures

- first tower falls: median round 11.0, p10 6, p90 17
- games with at least one tower down: 96.7%
- first-tower win rate: 90.5%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.47 |
| chips_wave | 3.84 |
| base | 3.00 |
| champion_kill | 0.42 |
| dragon | 0.34 |
| blue_buff | 0.30 |
| tower_kill | 0.23 |
| red_buff | 0.16 |

| use | AP |
|---|---|
| shop | 9.65 |
| abilities | 1.85 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 48.9% | 63.2% | -14.3 |
| cloth_armor | 5 | 1.99 | 49.4% | 51.3% | -1.9 |
| control_ward | 2 | 1.29 | - | 50.0% | - |
| frost_charm | 2 | 1.07 | - | 50.0% | - |
| health_potion | 2 | 1.88 | - | 50.0% | - |
| ionian_charm | 8 | 1.98 | 48.1% | 60.2% | -12.1 |
| long_sword | 6 | 2.00 | 49.7% | 51.0% | -1.3 |
| longbow | 6 | 2.00 | 49.9% | 50.1% | -0.2 |
| ruby_crystal | 4 | 2.00 | 50.0% | 66.7% | -16.7 |
| stopwatch | 3 | 1.90 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 49.8% | 50.6% | -0.9 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 91.4 [81.4, 96.3] |
| T2_laner | 54 | 53.7 [40.6, 66.3] |
| T2_objective | 42 | 38.1 [25.0, 53.2] |
| T2_warder | 38 | 34.2 [21.2, 50.1] |
| T2_brawler | 48 | 18.8 [10.2, 31.9] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 68.83 per game
- that is 46.5% of all ability uses
- of which true snipes (from cover, two or more hexes away): 41.9% of all uses
- snipes aimed at a champion: 13.7 per game
- activations ending beside an enemy-held hexgroup (looking in): 49.3%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **Median game length 13-18 rounds** - 20.0 [20.0, 20.0]
2. **>=95% of games end by Nexus kill before round 20** - 30.0% [22.5, 38.7]
3. **economy outlier: sable** - 4.36 AP/round = 2.54x roster mean
4. **ability usage: ashwyn.R** - used in 13.7% of affordable rounds with a legal target
5. **ability usage: bastion.W** - used in 0.0% of affordable rounds with a legal target

## 12. Delta vs batch_0039

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +4.5 | -0.95 | no |
| bastion | +0.0 | -0.37 | no |
| bramblehide | -5.8 | -0.32 | no |
| brixa | +10.9 | -0.32 | no |
| corvane | +14.6 | -0.15 | no |
| dax | +1.8 | -0.29 | no |
| grivven | +17.4 | -0.48 | no |
| kaelis | +6.2 | -0.40 | no |
| kestrel | -11.8 | -0.17 | no |
| lumen | -2.5 | -0.13 | no |
| marrow | +4.0 | -0.51 | no |
| mossgrove | +5.8 | -0.15 | no |
| noctis | +0.0 | -0.11 | no |
| orrin | -2.0 | -0.53 | no |
| ossuar | -11.9 | -0.54 | no |
| pallas | -8.0 | -0.99 | no |
| quillan | +0.0 | -0.82 | no |
| rictus | +2.1 | -0.14 | no |
| sable | -10.0 | -1.28 | no |
| sylphine | +4.3 | -0.38 | no |
| thornjaw | -7.1 | -0.17 | no |
| vellum | +6.2 | -0.62 | no |
| veyra | -1.9 | -0.10 | no |
| vurmak | +0.0 | -0.27 | no |
| wisp | -17.9 | -1.26 | no |

- median length delta: +2.0
- nexus-kill rate delta: -48.3 pts
