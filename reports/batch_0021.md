# Sim report batch_0021

## 1. Header

| field | value |
|---|---|
| rules | 1.1.0 |
| roster | 1.2.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 2101 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 446.9s |
| engine tests | not run |
| generated | 2026-09-20 18:05:55 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 8 FAIL / 17 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 53/56 abilities outside the band; roster mean 18.3%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 43.3% [35.7, 51.3] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 14.0 [13.0, 14.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 98.7% [95.3, 99.6] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.57 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 49.3% [41.4, 57.3] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 90.7 [80.1, 96.0] | 54 | 9.70 | 3.78 | 2% | 87% | 0% | 6% | 0.00 | 0.00 | 0.0 | 0.1 | 47% | bootsx54, cloth_armorx54, ionian_charmx54 |
| wisp | 80.6 [69.1, 88.6] | 62 | 6.64 | 2.58 | 9% | 73% | 1% | 5% | 0.02 | 0.02 | 0.0 | 0.0 | 35% | bootsx62, longbowx62, ruby_crystalx62 |
| bramblehide | 71.7 [59.2, 81.5] | 60 | 2.27 | 0.88 | 5% | 24% | 1% | 37% | 0.02 | 0.02 | 0.0 | 3.6 | 13% | long_swordx60, ruby_crystalx60, vampiric_bladex60 |
| vurmak | 71.7 [59.2, 81.5] | 60 | 1.42 | 0.55 | 21% | 5% | 3% | 39% | 0.05 | 0.00 | 0.0 | 2.9 | 9% | ruby_crystalx60, long_swordx58, cloth_armorx56 |
| pallas | 67.9 [54.8, 78.6] | 56 | 5.09 | 1.98 | 7% | 1% | 0% | 84% | 0.00 | 0.02 | 0.1 | 4.3 | 29% | bootsx56, longbowx56, ruby_crystalx56 |
| kestrel | 62.0 [48.2, 74.1] | 50 | 1.83 | 0.71 | 40% | 19% | 5% | 21% | 0.00 | 0.00 | 0.0 | 2.9 | 11% | long_swordx50, longbowx50, vampiric_bladex49 |
| rictus | 57.1 [45.5, 68.1] | 70 | 1.03 | 0.40 | 19% | 19% | 19% | 1% | 0.00 | 0.06 | 0.1 | 1.5 | 6% | long_swordx70, ruby_crystalx70, vampiric_bladex69 |
| ossuar | 53.7 [40.6, 66.3] | 54 | 2.21 | 0.86 | 11% | 7% | 5% | 46% | 0.00 | 0.00 | 0.0 | 3.6 | 14% | long_swordx54, ruby_crystalx54, cloth_armorx53 |
| quillan | 53.4 [40.8, 65.7] | 58 | 8.31 | 3.24 | 3% | 3% | 0% | 85% | 0.03 | 0.03 | 0.1 | 2.6 | 46% | ionian_charmx58, longbowx58, ruby_crystalx58 |
| dax | 50.0 [37.5, 62.5] | 58 | 1.14 | 0.44 | 18% | 29% | 5% | 18% | 0.00 | 0.02 | 0.0 | 1.9 | 7% | long_swordx58, longbowx58, vampiric_bladex57 |
| mossgrove | 50.0 [38.4, 61.6] | 68 | 0.87 | 0.34 | 29% | 16% | 1% | 8% | 0.00 | 0.00 | 0.0 | 3.5 | 6% | long_swordx68, ruby_crystalx67, vampiric_bladex64 |
| orrin | 50.0 [38.3, 61.7] | 66 | 0.93 | 0.36 | 17% | 19% | 10% | 7% | 0.00 | 0.08 | 0.2 | 2.1 | 6% | long_swordx66, longbowx64, vampiric_bladex62 |
| veyra | 50.0 [37.3, 62.7] | 56 | 1.09 | 0.42 | 15% | 34% | 7% | 13% | 0.02 | 0.00 | 0.0 | 2.4 | 6% | long_swordx56, longbowx56, vampiric_bladex55 |
| sable | 48.6 [37.6, 59.8] | 74 | 6.48 | 2.52 | 6% | 57% | 0% | 26% | 0.00 | 0.03 | 0.0 | 2.7 | 38% | ionian_charmx74, longbowx74, ruby_crystalx73 |
| marrow | 47.0 [35.4, 58.8] | 66 | 1.78 | 0.69 | 14% | 2% | 11% | 23% | 0.02 | 0.02 | 0.0 | 0.9 | 12% | long_swordx66, ruby_crystalx66, cloth_armorx63 |
| bastion | 45.2 [33.4, 57.5] | 62 | 1.55 | 0.61 | 40% | 3% | 2% | 10% | 0.00 | 0.00 | 0.0 | 1.9 | 11% | ruby_crystalx62, long_swordx61, cloth_armorx59 |
| grivven | 41.9 [30.5, 54.3] | 62 | 2.96 | 1.15 | 15% | 1% | 1% | 61% | 0.02 | 0.03 | 0.1 | 7.2 | 18% | longbowx62, ruby_crystalx62, bootsx61 |
| brixa | 41.4 [30.6, 53.1] | 70 | 1.10 | 0.43 | 29% | 12% | 12% | 8% | 0.00 | 0.01 | 0.0 | 1.3 | 7% | long_swordx70, longbowx69, vampiric_bladex65 |
| corvane | 34.5 [23.6, 47.3] | 58 | 0.41 | 0.16 | 38% | 1% | 10% | 2% | 0.03 | 0.02 | 0.0 | 3.7 | 3% | longbowx58, ruby_crystalx58, bootsx55 |
| sylphine | 34.1 [21.9, 48.9] | 44 | 0.81 | 0.31 | 12% | 2% | 13% | 16% | 0.00 | 0.02 | 0.0 | 1.2 | 5% | long_swordx44, ruby_crystalx44, vampiric_bladex41 |
| kaelis | 32.8 [22.1, 45.6] | 58 | 0.95 | 0.37 | 22% | 16% | 3% | 10% | 0.02 | 0.02 | 0.0 | 0.9 | 6% | cloth_armorx58, ruby_crystalx58, long_swordx57 |
| thornjaw | 31.0 [20.6, 43.8] | 58 | 0.93 | 0.36 | 15% | 17% | 7% | 4% | 0.02 | 0.03 | 0.1 | 0.7 | 7% | ruby_crystalx58, long_swordx57, vampiric_bladex50 |
| vellum | 31.0 [20.6, 43.8] | 58 | 2.74 | 1.07 | 11% | 0% | 10% | 66% | 0.00 | 0.05 | 0.1 | 2.7 | 22% | longbowx58, ionian_charmx56, ruby_crystalx54 |
| noctis | 28.6 [18.4, 41.5] | 56 | 1.37 | 0.53 | 50% | 6% | 17% | 4% | 0.00 | 0.04 | 0.1 | 0.6 | 11% | longbowx56, ionian_charmx52, ruby_crystalx47 |
| lumen | 25.8 [16.6, 37.9] | 62 | 0.63 | 0.24 | 31% | 4% | 1% | 3% | 0.02 | 0.02 | 0.0 | 0.4 | 5% | longbowx62, ruby_crystalx62, bootsx58 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 1.19 |
| Jungle | 50.0 [44.4, 55.6] | 1.19 |
| Mid | 50.0 [44.4, 55.6] | 5.74 |
| Support | 50.0 [44.4, 55.6] | 3.14 |
| Top | 50.0 [44.4, 55.6] | 1.58 |

## 5. Games

- length: median 14.0, p10 11, p90 17
- end reasons: {'nexus': 148, 'round_limit_towers': 2} (draws 0)
- priority win rate: 43.3% [35.7, 51.3]
- north win rate: 49.3% [41.4, 57.3]
- length histogram: {8: 1, 9: 6, 10: 5, 11: 17, 12: 28, 13: 17, 14: 30, 15: 21, 16: 6, 17: 7, 18: 5, 19: 1, 20: 6}

## 6. Objectives

- takes per game: {'dragon': 1.8066666666666666, 'baron': 0.88}
- median round taken: dragon 8, baron 10.0
- win rate when secured: {'dragon': 41.69741697416974, 'baron': 41.666666666666664}
- camp clears per game: {'krugs': 6.906666666666666, 'red_buff': 4.093333333333334, 'wolves': 6.093333333333334, 'raptors': 6.76, 'blue_buff': 4.1066666666666665, 'dragon': 1.8066666666666666, 'baron': 0.88}

## 7. Structures

- first tower falls: median round 5.0, p10 4, p90 7
- games with at least one tower down: 100.0%
- first-tower win rate: 83.3%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.40 |
| chips_wave | 4.12 |
| chips_structure | 3.98 |
| base | 3.37 |
| blue_buff | 0.30 |
| red_buff | 0.22 |
| champion_kill | 0.01 |

| use | AP |
|---|---|
| shop | 12.04 |
| abilities | 2.20 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.95 | 58.8% | 8.0% | +50.8 |
| cloth_armor | 5 | 1.93 | 61.8% | 30.6% | +31.2 |
| control_ward | 2 | 1.14 | - | 50.0% | - |
| frost_charm | 2 | 0.97 | - | 50.0% | - |
| health_potion | 2 | 1.95 | - | 50.0% | - |
| ionian_charm | 8 | 1.96 | 61.7% | 7.7% | +54.0 |
| long_sword | 6 | 2.00 | 52.0% | 43.4% | +8.6 |
| longbow | 6 | 2.00 | 50.2% | 49.8% | +0.4 |
| ruby_crystal | 4 | 2.00 | 51.5% | 0.0% | +51.5 |
| stopwatch | 3 | 1.91 | - | 50.0% | - |
| swift_tonic | 1 | 1.98 | - | 50.0% | - |
| vampiric_blade | 5 | 1.93 | 56.4% | 35.7% | +20.6 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 79.60 per game
- that is 85.6% of all ability uses


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 9.70 AP/round = 3.78x roster mean
2. **champion win rate: ashwyn** - WR 90.7% [80.1, 96.0]
3. **economy outlier: quillan** - 8.31 AP/round = 3.24x roster mean
4. **champion win rate: wisp** - WR 80.6% [69.1, 88.6]
5. **champion win rate: lumen** - WR 25.8% [16.6, 37.9]

## 12. Delta vs batch_0020

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +8.0 | +0.11 | no |
| bastion | -0.7 | +0.01 | no |
| bramblehide | +10.0 | +0.15 | no |
| brixa | -6.9 | +0.02 | no |
| corvane | +4.5 | -0.00 | no |
| dax | -8.6 | -0.07 | no |
| grivven | -5.4 | +0.11 | no |
| kaelis | -14.1 | -0.05 | no |
| kestrel | +20.3 | +0.00 | no |
| lumen | -14.2 | -0.02 | no |
| marrow | -1.1 | -0.04 | no |
| mossgrove | +21.0 | -0.03 | no |
| noctis | +16.6 | +0.01 | no |
| orrin | +6.7 | +0.00 | no |
| ossuar | +12.0 | +0.20 | no |
| pallas | +13.4 | +0.37 | no |
| quillan | -19.3 | +0.27 | no |
| rictus | +5.4 | +0.03 | no |
| sable | +5.8 | +0.17 | no |
| sylphine | -17.7 | -0.03 | no |
| thornjaw | -25.0 | -0.17 | no |
| vellum | -6.1 | -0.24 | no |
| veyra | -8.0 | +0.04 | no |
| vurmak | +6.0 | -0.02 | no |
| wisp | +4.8 | +0.29 | no |

- median length delta: +1.0
- nexus-kill rate delta: +0.7 pts
