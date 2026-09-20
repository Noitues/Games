# Sim report batch_0020

## 1. Header

| field | value |
|---|---|
| rules | 1.1.0 |
| roster | 1.2.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 2001 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 426.5s |
| engine tests | not run |
| generated | 2026-09-20 17:57:50 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 6 FAIL / 19 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 53/56 abilities outside the band; roster mean 18.5%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 44.7% [36.9, 52.7] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 13.0 [12.0, 13.0] | **INCONCLUSIVE** |
| >=95% of games end by Nexus kill before round 20 | 98.0% [94.3, 99.3] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.52 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 42.7% [35.0, 50.7] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 82.7 [70.3, 90.6] | 52 | 9.59 | 3.80 | 2% | 87% | 1% | 6% | 0.00 | 0.02 | 0.0 | 0.1 | 46% | ionian_charmx52, long_swordx52, longbowx52 |
| wisp | 75.9 [63.5, 85.0] | 58 | 6.35 | 2.51 | 10% | 73% | 0% | 5% | 0.02 | 0.00 | 0.0 | 0.0 | 33% | bootsx58, longbowx58, ruby_crystalx58 |
| quillan | 72.7 [61.0, 82.0] | 66 | 8.04 | 3.19 | 2% | 3% | 1% | 85% | 0.02 | 0.02 | 0.0 | 2.4 | 43% | ionian_charmx66, long_swordx66, longbowx66 |
| vurmak | 65.6 [53.4, 76.1] | 64 | 1.44 | 0.57 | 21% | 3% | 2% | 42% | 0.00 | 0.02 | 0.0 | 3.1 | 9% | long_swordx64, ruby_crystalx64, cloth_armorx62 |
| bramblehide | 61.7 [49.0, 72.9] | 60 | 2.12 | 0.84 | 6% | 21% | 1% | 37% | 0.00 | 0.00 | 0.0 | 3.6 | 14% | long_swordx60, ruby_crystalx60, vampiric_bladex60 |
| dax | 58.6 [46.9, 69.4] | 70 | 1.21 | 0.48 | 16% | 30% | 4% | 17% | 0.01 | 0.01 | 0.0 | 1.7 | 7% | long_swordx70, longbowx69, vampiric_bladex67 |
| veyra | 58.0 [44.2, 70.6] | 50 | 1.06 | 0.42 | 12% | 36% | 7% | 13% | 0.04 | 0.00 | 0.0 | 2.5 | 7% | long_swordx50, longbowx49, ruby_crystalx46 |
| thornjaw | 56.1 [44.1, 67.4] | 66 | 1.10 | 0.43 | 12% | 16% | 7% | 5% | 0.02 | 0.02 | 0.0 | 0.7 | 7% | long_swordx66, ruby_crystalx66, vampiric_bladex61 |
| pallas | 54.4 [42.7, 65.7] | 68 | 4.73 | 1.87 | 6% | 1% | 1% | 87% | 0.00 | 0.03 | 0.1 | 4.2 | 26% | longbowx68, ruby_crystalx68, bootsx67 |
| rictus | 51.8 [39.0, 64.3] | 56 | 1.00 | 0.40 | 15% | 22% | 19% | 3% | 0.00 | 0.00 | 0.0 | 1.6 | 6% | long_swordx56, ruby_crystalx55, vampiric_bladex53 |
| sylphine | 51.8 [39.0, 64.3] | 56 | 0.83 | 0.33 | 13% | 1% | 11% | 16% | 0.00 | 0.00 | 0.0 | 1.1 | 5% | long_swordx56, ruby_crystalx56, vampiric_bladex49 |
| brixa | 48.3 [36.2, 60.7] | 60 | 1.08 | 0.43 | 25% | 11% | 11% | 10% | 0.00 | 0.08 | 0.1 | 1.1 | 7% | long_swordx60, vampiric_bladex60, longbowx59 |
| marrow | 48.1 [35.1, 61.3] | 52 | 1.82 | 0.72 | 17% | 2% | 9% | 25% | 0.00 | 0.00 | 0.0 | 0.9 | 13% | ruby_crystalx52, long_swordx51, cloth_armorx48 |
| grivven | 47.3 [36.3, 58.5] | 74 | 2.85 | 1.13 | 17% | 4% | 1% | 56% | 0.00 | 0.01 | 0.0 | 7.0 | 19% | bootsx74, longbowx74, ruby_crystalx74 |
| kaelis | 46.9 [35.2, 58.9] | 64 | 0.99 | 0.39 | 23% | 17% | 2% | 10% | 0.00 | 0.05 | 0.1 | 0.8 | 6% | long_swordx64, ruby_crystalx64, cloth_armorx62 |
| bastion | 45.8 [34.8, 57.3] | 72 | 1.54 | 0.61 | 42% | 3% | 1% | 10% | 0.01 | 0.01 | 0.0 | 2.0 | 11% | long_swordx72, ruby_crystalx72, cloth_armorx69 |
| orrin | 43.3 [31.6, 55.9] | 60 | 0.93 | 0.37 | 18% | 19% | 12% | 5% | 0.03 | 0.08 | 0.2 | 1.9 | 6% | long_swordx60, longbowx60, vampiric_bladex56 |
| sable | 42.9 [31.9, 54.5] | 70 | 6.31 | 2.50 | 5% | 57% | 0% | 27% | 0.03 | 0.01 | 0.0 | 2.7 | 37% | ionian_charmx70, longbowx70, ruby_crystalx70 |
| kestrel | 41.7 [30.1, 54.3] | 60 | 1.82 | 0.72 | 41% | 17% | 4% | 23% | 0.00 | 0.00 | 0.0 | 2.9 | 12% | long_swordx60, longbowx59, vampiric_bladex55 |
| ossuar | 41.7 [28.8, 55.7] | 48 | 2.01 | 0.80 | 13% | 9% | 3% | 44% | 0.00 | 0.02 | 0.1 | 3.5 | 12% | cloth_armorx48, long_swordx48, ruby_crystalx48 |
| lumen | 40.0 [26.3, 55.4] | 40 | 0.65 | 0.26 | 34% | 3% | 1% | 2% | 0.03 | 0.03 | 0.0 | 0.4 | 5% | longbowx40, ruby_crystalx40, bootsx37 |
| vellum | 37.1 [26.2, 49.5] | 62 | 2.98 | 1.18 | 11% | 0% | 7% | 71% | 0.00 | 0.02 | 0.0 | 2.9 | 23% | longbowx62, ruby_crystalx61, ionian_charmx59 |
| corvane | 30.0 [19.9, 42.5] | 60 | 0.41 | 0.16 | 36% | 1% | 13% | 1% | 0.00 | 0.00 | 0.0 | 4.0 | 3% | longbowx60, ruby_crystalx60, bootsx59 |
| mossgrove | 29.0 [19.2, 41.3] | 62 | 0.90 | 0.35 | 26% | 17% | 1% | 7% | 0.00 | 0.03 | 0.1 | 2.9 | 6% | long_swordx62, ruby_crystalx62, vampiric_bladex56 |
| noctis | 12.0 [5.6, 23.8] | 50 | 1.36 | 0.54 | 49% | 5% | 22% | 1% | 0.02 | 0.08 | 0.2 | 0.6 | 12% | longbowx50, ionian_charmx45, ruby_crystalx37 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 1.23 |
| Jungle | 50.0 [44.4, 55.6] | 1.19 |
| Mid | 50.0 [44.4, 55.6] | 5.75 |
| Support | 50.0 [44.4, 55.6] | 3.17 |
| Top | 50.0 [44.4, 55.6] | 1.53 |

## 5. Games

- length: median 13.0, p10 10, p90 17
- end reasons: {'nexus': 147, 'round_limit_towers': 3} (draws 0)
- priority win rate: 44.7% [36.9, 52.7]
- north win rate: 42.7% [35.0, 50.7]
- length histogram: {8: 3, 9: 5, 10: 17, 11: 28, 12: 21, 13: 20, 14: 17, 15: 11, 16: 10, 17: 6, 18: 5, 19: 3, 20: 4}

## 6. Objectives

- takes per game: {'dragon': 1.7333333333333334, 'baron': 0.78}
- median round taken: dragon 7.5, baron 10
- win rate when secured: {'dragon': 46.92307692307692, 'baron': 42.73504273504273}
- camp clears per game: {'krugs': 6.46, 'wolves': 5.886666666666667, 'raptors': 6.42, 'red_buff': 3.993333333333333, 'blue_buff': 3.9266666666666667, 'dragon': 1.7333333333333334, 'baron': 0.78}

## 7. Structures

- first tower falls: median round 5.0, p10 3, p90 7
- games with at least one tower down: 100.0%
- first-tower win rate: 80.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.37 |
| chips_structure | 4.01 |
| chips_wave | 3.98 |
| base | 3.34 |
| blue_buff | 0.30 |
| red_buff | 0.22 |
| champion_kill | 0.01 |

| use | AP |
|---|---|
| shop | 12.15 |
| abilities | 2.23 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.97 | 58.9% | 12.8% | +46.1 |
| cloth_armor | 5 | 1.93 | 61.8% | 32.9% | +28.9 |
| control_ward | 2 | 0.97 | - | 50.0% | - |
| frost_charm | 2 | 0.78 | - | 50.0% | - |
| health_potion | 2 | 1.93 | - | 50.0% | - |
| ionian_charm | 8 | 1.95 | 62.4% | 13.8% | +48.6 |
| long_sword | 6 | 2.00 | 51.9% | 43.6% | +8.3 |
| longbow | 6 | 2.00 | 50.2% | 49.7% | +0.6 |
| ruby_crystal | 4 | 2.00 | 51.6% | 0.0% | +51.6 |
| stopwatch | 3 | 1.91 | - | 50.0% | - |
| swift_tonic | 1 | 1.96 | - | 50.0% | - |
| vampiric_blade | 5 | 1.90 | 57.3% | 35.4% | +21.9 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 75.91 per game
- that is 85.9% of all ability uses


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 9.59 AP/round = 3.80x roster mean
2. **champion win rate: noctis** - WR 12.0% [5.6, 23.8]
3. **economy outlier: quillan** - 8.04 AP/round = 3.19x roster mean
4. **champion win rate: ashwyn** - WR 82.7% [70.3, 90.6]
5. **champion win rate: wisp** - WR 75.9% [63.5, 85.0]

## 12. Delta vs batch_0016

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -4.8 | +0.08 | no |
| bastion | -6.0 | +0.02 | no |
| bramblehide | +11.7 | +0.13 | no |
| brixa | +13.7 | -0.06 | no |
| corvane | +8.3 | +0.05 | no |
| dax | +5.8 | +0.01 | no |
| grivven | +15.7 | +0.14 | no |
| kaelis | +16.3 | +0.13 | no |
| kestrel | -27.3 | -0.04 | no |
| lumen | -10.0 | -0.03 | no |
| marrow | -0.5 | +0.24 | no |
| mossgrove | -18.0 | +0.12 | no |
| noctis | -14.1 | +0.10 | no |
| orrin | +7.1 | +0.08 | no |
| ossuar | -16.7 | +0.07 | no |
| pallas | -17.6 | +0.14 | no |
| quillan | +10.2 | +0.23 | no |
| rictus | -1.8 | -0.04 | no |
| sable | +4.9 | +0.48 | no |
| sylphine | +0.2 | +0.05 | no |
| thornjaw | +7.8 | +0.12 | no |
| vellum | +1.4 | +0.38 | no |
| veyra | +3.0 | +0.06 | no |
| vurmak | +14.1 | +0.17 | no |
| wisp | -7.5 | +0.15 | no |

- median length delta: +2.0
- nexus-kill rate delta: +0.7 pts
