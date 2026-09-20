# Sim report batch_0015

## 1. Header

| field | value |
|---|---|
| rules | 1.1.0 |
| roster | 1.1.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 1402 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 243.6s |
| engine tests | not run |
| generated | 2026-09-20 10:51:37 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 4 FAIL / 21 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 50/58 abilities outside the band; roster mean 24.7%; 7 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 48.7% [40.8, 56.6] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 9.0 [9.0, 9.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 100.0% [97.5, 100.0] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, ossuar, quillan, sable, wisp (roster mean 2.81 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 45.3% [37.6, 53.3] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 82.0 [69.2, 90.2] | 50 | 11.74 | 4.18 | 1% | 5% | 1% | 89% | 0.04 | 0.00 | 0.0 | 2.3 | 53% | ionian_charmx50, longbowx50, ruby_crystalx50 |
| ashwyn | 73.4 [61.5, 82.7] | 64 | 8.02 | 2.85 | 1% | 68% | 0% | 25% | 0.03 | 0.00 | 0.0 | 0.3 | 42% | longbowx64, ionian_charmx63, ruby_crystalx61 |
| bramblehide | 66.7 [51.6, 79.0] | 42 | 3.99 | 1.42 | 1% | 11% | 0% | 82% | 0.02 | 0.00 | 0.0 | 3.5 | 23% | long_swordx42, ruby_crystalx42, vampiric_bladex41 |
| veyra | 62.9 [50.5, 73.8] | 62 | 1.29 | 0.46 | 6% | 15% | 2% | 58% | 0.00 | 0.03 | 0.0 | 4.8 | 8% | long_swordx62, longbowx58, vampiric_bladex54 |
| wisp | 62.1 [50.1, 72.9] | 66 | 4.39 | 1.56 | 10% | 50% | 0% | 34% | 0.00 | 0.00 | 0.0 | 1.7 | 25% | longbowx66, ruby_crystalx65, bootsx58 |
| ossuar | 61.1 [47.8, 73.0] | 54 | 5.32 | 1.89 | 0% | 0% | 0% | 90% | 0.00 | 0.00 | 0.0 | 3.9 | 29% | long_swordx54, ruby_crystalx54, cloth_armorx51 |
| kestrel | 59.4 [47.1, 70.5] | 64 | 1.76 | 0.62 | 15% | 30% | 4% | 33% | 0.00 | 0.02 | 0.0 | 3.0 | 11% | long_swordx64, longbowx61, vampiric_bladex55 |
| pallas | 58.9 [45.9, 70.8] | 56 | 3.83 | 1.36 | 13% | 1% | 2% | 75% | 0.04 | 0.00 | 0.0 | 3.2 | 22% | longbowx56, ruby_crystalx55, bootsx53 |
| sable | 57.6 [45.6, 68.8] | 66 | 9.08 | 3.23 | 3% | 15% | 0% | 76% | 0.00 | 0.02 | 0.0 | 2.5 | 47% | longbowx66, ionian_charmx62, ruby_crystalx59 |
| vurmak | 53.7 [40.6, 66.3] | 54 | 1.66 | 0.59 | 11% | 3% | 1% | 62% | 0.02 | 0.02 | 0.0 | 3.4 | 12% | ruby_crystalx54, long_swordx43, cloth_armorx33 |
| brixa | 53.3 [40.9, 65.4] | 60 | 1.26 | 0.45 | 14% | 7% | 8% | 43% | 0.00 | 0.03 | 0.1 | 3.0 | 8% | long_swordx60, longbowx56, vampiric_bladex48 |
| bastion | 51.5 [39.8, 62.9] | 68 | 2.46 | 0.88 | 12% | 3% | 2% | 43% | 0.00 | 0.00 | 0.0 | 3.8 | 15% | ruby_crystalx68, long_swordx66, cloth_armorx65 |
| mossgrove | 51.4 [40.1, 62.6] | 72 | 0.88 | 0.31 | 20% | 15% | 1% | 26% | 0.01 | 0.00 | 0.0 | 3.7 | 6% | long_swordx72, ruby_crystalx70, vampiric_bladex58 |
| rictus | 50.0 [37.9, 62.1] | 62 | 1.02 | 0.36 | 19% | 15% | 21% | 3% | 0.02 | 0.02 | 0.0 | 1.6 | 6% | ruby_crystalx62, long_swordx61, vampiric_bladex48 |
| kaelis | 48.4 [36.4, 60.6] | 62 | 1.11 | 0.39 | 14% | 12% | 3% | 34% | 0.00 | 0.00 | 0.0 | 2.3 | 7% | ruby_crystalx62, long_swordx57, cloth_armorx51 |
| grivven | 45.5 [31.7, 59.9] | 44 | 2.35 | 0.84 | 13% | 3% | 1% | 54% | 0.00 | 0.00 | 0.0 | 4.6 | 14% | longbowx44, ruby_crystalx44, bootsx39 |
| sylphine | 44.4 [33.5, 55.9] | 72 | 0.84 | 0.30 | 23% | 2% | 7% | 25% | 0.00 | 0.00 | 0.0 | 2.1 | 5% | ruby_crystalx72, long_swordx71, vampiric_bladex54 |
| corvane | 43.6 [33.1, 54.6] | 78 | 0.37 | 0.13 | 35% | 2% | 12% | 3% | 0.01 | 0.03 | 0.1 | 2.9 | 3% | longbowx78, ruby_crystalx78, bootsx70 |
| thornjaw | 42.3 [29.9, 55.8] | 52 | 0.96 | 0.34 | 19% | 13% | 17% | 9% | 0.00 | 0.00 | 0.0 | 1.7 | 6% | ruby_crystalx52, long_swordx51, vampiric_bladex39 |
| dax | 40.0 [28.6, 52.6] | 60 | 1.28 | 0.46 | 17% | 13% | 3% | 43% | 0.00 | 0.05 | 0.1 | 2.6 | 8% | long_swordx60, longbowx59, vampiric_bladex54 |
| lumen | 39.3 [27.6, 52.4] | 56 | 0.73 | 0.26 | 40% | 2% | 1% | 1% | 0.00 | 0.00 | 0.0 | 0.2 | 5% | longbowx56, ruby_crystalx55, bootsx45 |
| marrow | 37.1 [26.2, 49.5] | 62 | 1.24 | 0.44 | 14% | 2% | 11% | 19% | 0.00 | 0.00 | 0.0 | 2.1 | 9% | ruby_crystalx62, long_swordx60, cloth_armorx52 |
| vellum | 35.4 [23.4, 49.6] | 48 | 2.88 | 1.03 | 11% | 1% | 2% | 74% | 0.00 | 0.02 | 0.0 | 2.7 | 21% | longbowx47, ionian_charmx41, ruby_crystalx32 |
| orrin | 31.5 [20.7, 44.7] | 54 | 0.84 | 0.30 | 18% | 22% | 6% | 8% | 0.02 | 0.00 | 0.0 | 2.1 | 5% | long_swordx54, longbowx50, vampiric_bladex39 |
| noctis | 9.7 [4.8, 18.7] | 72 | 0.91 | 0.33 | 24% | 6% | 34% | 6% | 0.01 | 0.06 | 0.1 | 0.7 | 8% | longbowx68, ionian_charmx50, ruby_crystalx41 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 1.30 |
| Jungle | 50.0 [44.4, 55.6] | 1.35 |
| Mid | 50.0 [44.4, 55.6] | 6.34 |
| Support | 50.0 [44.4, 55.6] | 2.26 |
| Top | 50.0 [44.4, 55.6] | 2.30 |

## 5. Games

- length: median 9.0, p10 7, p90 12
- end reasons: {'nexus': 150} (draws 0)
- priority win rate: 48.7% [40.8, 56.6]
- north win rate: 45.3% [37.6, 53.3]
- length histogram: {6: 8, 7: 13, 8: 37, 9: 34, 10: 29, 11: 13, 12: 10, 13: 5, 14: 1}

## 6. Objectives

- takes per game: {'dragon': 1.14, 'baron': 0.18666666666666668}
- median round taken: dragon 5, baron 9.5
- win rate when secured: {'dragon': 43.85964912280702, 'baron': 39.285714285714285}
- camp clears per game: {'krugs': 4.806666666666667, 'wolves': 4.486666666666666, 'raptors': 4.913333333333333, 'blue_buff': 2.9266666666666667, 'red_buff': 2.84, 'dragon': 1.14, 'baron': 0.18666666666666668}

## 7. Structures

- first tower falls: median round 3.0, p10 2, p90 3
- games with at least one tower down: 100.0%
- first-tower win rate: 78.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 4.82 |
| chips_monster | 4.62 |
| chips_wave | 3.71 |
| base | 3.24 |
| blue_buff | 0.31 |
| red_buff | 0.21 |
| champion_kill | 0.01 |

| use | AP |
|---|---|
| shop | 12.29 |
| abilities | 3.08 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.77 | 70.9% | 28.5% | +42.4 |
| cloth_armor | 5 | 1.68 | 67.1% | 41.4% | +25.7 |
| control_ward | 2 | 0.19 | - | 50.0% | - |
| frost_charm | 2 | 0.03 | - | 50.0% | - |
| health_potion | 2 | 1.61 | - | 50.0% | - |
| ionian_charm | 8 | 1.77 | 71.5% | 35.8% | +35.6 |
| long_sword | 6 | 2.00 | 55.2% | 37.7% | +17.6 |
| longbow | 6 | 2.00 | 51.2% | 48.3% | +2.9 |
| ruby_crystal | 4 | 2.00 | 54.8% | 10.0% | +44.8 |
| stopwatch | 3 | 1.51 | - | 50.0% | - |
| swift_tonic | 1 | 1.90 | - | 50.0% | - |
| vampiric_blade | 5 | 1.69 | 64.3% | 36.8% | +27.5 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: quillan** - 11.74 AP/round = 4.18x roster mean
2. **champion win rate: noctis** - WR 9.7% [4.8, 18.7]
3. **economy outlier: sable** - 9.08 AP/round = 3.23x roster mean
4. **champion win rate: quillan** - WR 82.0% [69.2, 90.2]
5. **economy outlier: ashwyn** - 8.02 AP/round = 2.85x roster mean

## 12. Delta vs batch_0014

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -11.6 | -1.76 | no |
| bastion | -15.2 | +0.94 | no |
| bramblehide | -7.6 | +2.02 | no |
| brixa | +1.8 | +0.13 | no |
| corvane | +22.2 | -0.03 | no |
| dax | -14.7 | +0.15 | no |
| grivven | +9.1 | -0.47 | no |
| kaelis | +19.6 | +0.24 | no |
| kestrel | +5.9 | -0.04 | no |
| lumen | +6.8 | +0.09 | no |
| marrow | -6.8 | -0.32 | no |
| mossgrove | +17.1 | +0.04 | no |
| noctis | -15.3 | -0.46 | no |
| orrin | -4.5 | -0.04 | no |
| ossuar | -9.9 | +3.38 | no |
| pallas | -5.1 | -0.67 | no |
| quillan | +19.9 | +4.26 | no |
| rictus | +15.6 | +0.07 | no |
| sable | +20.1 | +3.32 | no |
| sylphine | -15.2 | +0.04 | no |
| thornjaw | -5.4 | +0.00 | no |
| vellum | -2.5 | +0.30 | no |
| veyra | +6.9 | +0.25 | no |
| vurmak | +8.9 | +0.39 | no |
| wisp | -20.7 | -1.83 | no |

- median length delta: -2.0
- nexus-kill rate delta: +0.7 pts
