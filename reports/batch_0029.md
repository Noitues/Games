# Sim report batch_0029

## 1. Header

| field | value |
|---|---|
| rules | 1.2.0 |
| roster | 1.3.0 |
| ai | 1.2.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 80 |
| seed | 2901 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 1440.3s |
| engine tests | not run |
| generated | 2026-09-20 23:34:18 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 5 FAIL / 20 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 53/56 abilities outside the band; roster mean 20.3%; 13 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 53.8% [42.9, 64.3] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 12.0 [12.0, 13.0] | **INCONCLUSIVE** |
| >=95% of games end by Nexus kill before round 20 | 97.5% [91.3, 99.3] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, wisp (roster mean 2.75 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 51.2% [40.5, 61.9] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 90.0 [74.4, 96.5] | 30 | 10.95 | 3.97 | 0% | 98% | 0% | 0% | 0.03 | 0.13 | 0.2 | 0.0 | 51% | bootsx30, cloth_armorx30, ionian_charmx30 |
| wisp | 81.2 [64.7, 91.1] | 32 | 7.32 | 2.66 | 0% | 95% | 0% | 4% | 0.03 | 0.41 | 0.5 | 0.0 | 36% | bootsx32, cloth_armorx32, longbowx32 |
| veyra | 71.4 [56.4, 82.8] | 42 | 1.68 | 0.61 | 2% | 81% | 0% | 4% | 0.31 | 0.05 | 0.1 | 0.7 | 9% | long_swordx42, longbowx42, vampiric_bladex40 |
| vurmak | 66.7 [46.7, 82.0] | 24 | 1.67 | 0.61 | 55% | 0% | 0% | 30% | 0.46 | 0.00 | 0.0 | 2.0 | 9% | cloth_armorx24, long_swordx24, ruby_crystalx24 |
| bastion | 63.3 [45.5, 78.1] | 30 | 1.64 | 0.60 | 83% | 0% | 0% | 1% | 0.07 | 0.10 | 0.2 | 0.2 | 10% | long_swordx30, ruby_crystalx30, cloth_armorx29 |
| quillan | 58.3 [42.2, 72.9] | 36 | 8.55 | 3.10 | 0% | 1% | 0% | 97% | 0.03 | 0.31 | 0.5 | 2.5 | 44% | bootsx36, ionian_charmx36, long_swordx36 |
| lumen | 57.7 [38.9, 74.5] | 26 | 0.94 | 0.34 | 82% | 0% | 0% | 0% | 0.00 | 0.00 | 0.0 | 0.0 | 6% | bootsx26, longbowx26, ruby_crystalx26 |
| sylphine | 56.7 [39.2, 72.6] | 30 | 1.20 | 0.43 | 35% | 1% | 0% | 16% | 0.37 | 0.00 | 0.0 | 0.0 | 7% | long_swordx30, ruby_crystalx30, vampiric_bladex30 |
| pallas | 50.0 [34.5, 65.5] | 36 | 3.33 | 1.21 | 16% | 0% | 0% | 78% | 0.03 | 0.25 | 0.5 | 4.0 | 18% | longbowx36, ruby_crystalx36, bootsx34 |
| rictus | 50.0 [35.5, 64.5] | 42 | 1.23 | 0.45 | 14% | 20% | 21% | 1% | 0.19 | 0.26 | 0.4 | 1.7 | 7% | long_swordx42, ruby_crystalx42, vampiric_bladex41 |
| thornjaw | 50.0 [30.7, 69.3] | 22 | 1.32 | 0.48 | 36% | 10% | 2% | 1% | 0.00 | 0.00 | 0.0 | 0.0 | 8% | long_swordx22, ruby_crystalx22, bootsx20 |
| mossgrove | 47.5 [32.9, 62.5] | 40 | 1.07 | 0.39 | 60% | 0% | 0% | 10% | 0.12 | 0.10 | 0.1 | 4.5 | 7% | long_swordx40, ruby_crystalx40, vampiric_bladex39 |
| sable | 47.1 [31.5, 63.3] | 34 | 6.45 | 2.34 | 1% | 86% | 0% | 12% | 0.03 | 0.18 | 0.4 | 3.0 | 36% | ionian_charmx34, long_swordx34, longbowx34 |
| dax | 46.9 [30.9, 63.6] | 32 | 1.49 | 0.54 | 30% | 37% | 0% | 11% | 0.06 | 0.06 | 0.1 | 0.6 | 8% | long_swordx32, longbowx32, vampiric_bladex32 |
| bramblehide | 46.2 [28.8, 64.5] | 26 | 2.29 | 0.83 | 0% | 36% | 0% | 48% | 0.04 | 0.04 | 0.0 | 4.4 | 14% | long_swordx26, ruby_crystalx26, vampiric_bladex26 |
| orrin | 44.4 [29.5, 60.4] | 36 | 1.18 | 0.43 | 4% | 51% | 1% | 3% | 0.17 | 0.31 | 0.5 | 3.7 | 7% | long_swordx36, longbowx36, vampiric_bladex35 |
| kaelis | 43.8 [28.2, 60.7] | 32 | 1.15 | 0.42 | 58% | 2% | 2% | 5% | 0.09 | 0.00 | 0.0 | 0.5 | 7% | cloth_armorx32, long_swordx32, ruby_crystalx32 |
| marrow | 43.3 [27.4, 60.8] | 30 | 1.38 | 0.50 | 43% | 0% | 0% | 23% | 0.13 | 0.03 | 0.1 | 0.0 | 8% | long_swordx30, ruby_crystalx30, cloth_armorx29 |
| brixa | 40.9 [23.3, 61.3] | 22 | 1.34 | 0.49 | 35% | 18% | 7% | 0% | 0.09 | 0.18 | 0.4 | 0.5 | 9% | long_swordx22, longbowx22, vampiric_bladex21 |
| ossuar | 40.9 [27.7, 55.6] | 44 | 2.73 | 0.99 | 1% | 5% | 0% | 83% | 0.02 | 0.05 | 0.1 | 4.6 | 17% | long_swordx44, ruby_crystalx44, cloth_armorx43 |
| vellum | 39.3 [23.6, 57.6] | 28 | 2.97 | 1.08 | 2% | 0% | 0% | 90% | 0.07 | 0.43 | 1.1 | 3.1 | 21% | longbowx28, ionian_charmx27, ruby_crystalx26 |
| grivven | 37.5 [22.9, 54.7] | 32 | 2.98 | 1.08 | 5% | 0% | 0% | 76% | 0.03 | 0.12 | 0.3 | 6.8 | 18% | bootsx32, longbowx32, ruby_crystalx32 |
| kestrel | 35.7 [20.7, 54.2] | 28 | 1.89 | 0.69 | 25% | 48% | 0% | 26% | 0.18 | 0.18 | 0.4 | 3.4 | 12% | long_swordx28, longbowx28, vampiric_bladex28 |
| corvane | 26.5 [14.6, 43.1] | 34 | 0.58 | 0.21 | 43% | 0% | 0% | 1% | 0.09 | 0.26 | 0.5 | 2.6 | 4% | longbowx34, ruby_crystalx34, bootsx33 |
| noctis | 15.6 [6.9, 31.8] | 32 | 1.54 | 0.56 | 75% | 0% | 12% | 0% | 0.09 | 0.56 | 1.1 | 0.1 | 12% | longbowx32, ionian_charmx30, ruby_crystalx30 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [42.3, 57.7] | 1.52 |
| Jungle | 50.0 [42.3, 57.7] | 1.37 |
| Mid | 50.0 [42.3, 57.7] | 6.17 |
| Support | 50.0 [42.3, 57.7] | 3.09 |
| Top | 50.0 [42.3, 57.7] | 1.80 |

## 5. Games

- length: median 12.0, p10 10, p90 15
- end reasons: {'nexus': 78, 'round_limit_towers': 2} (draws 0)
- priority win rate: 53.8% [42.9, 64.3]
- north win rate: 51.2% [40.5, 61.9]
- length histogram: {9: 6, 10: 8, 11: 11, 12: 16, 13: 13, 14: 12, 15: 6, 16: 3, 17: 1, 18: 2, 20: 2}

## 6. Objectives

- takes per game: {'dragon': 1.6625, 'baron': 0.75}
- median round taken: dragon 7, baron 10.0
- win rate when secured: {'dragon': 42.10526315789474, 'baron': 31.666666666666668}
- camp clears per game: {'raptors': 6.1875, 'wolves': 5.7625, 'krugs': 6.0625, 'blue_buff': 3.7375, 'red_buff': 3.6875, 'dragon': 1.6625, 'baron': 0.75}

## 7. Structures

- first tower falls: median round 4.0, p10 3, p90 5
- games with at least one tower down: 100.0%
- first-tower win rate: 66.2%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 5.16 |
| chips_monster | 4.41 |
| chips_wave | 4.06 |
| base | 3.34 |
| blue_buff | 0.29 |
| red_buff | 0.15 |
| champion_kill | 0.06 |

| use | AP |
|---|---|
| shop | 13.02 |
| abilities | 2.19 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.96 | 58.5% | 5.5% | +53.0 |
| cloth_armor | 5 | 1.96 | 59.2% | 34.2% | +25.0 |
| control_ward | 2 | 0.99 | - | 50.0% | - |
| frost_charm | 2 | 0.90 | - | 50.0% | - |
| health_potion | 2 | 1.96 | - | 50.0% | - |
| ionian_charm | 8 | 1.96 | 60.6% | 11.1% | +49.5 |
| long_sword | 6 | 2.00 | 51.2% | 45.7% | +5.5 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 51.2% | 0.0% | +51.2 |
| stopwatch | 3 | 1.90 | - | 50.0% | - |
| swift_tonic | 1 | 1.96 | - | 50.0% | - |
| vampiric_blade | 5 | 1.98 | 54.9% | 38.7% | +16.3 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 45.04 per game
- that is 46.4% of all ability uses


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 10.95 AP/round = 3.97x roster mean
2. **champion win rate: ashwyn** - WR 90.0% [74.4, 96.5]
3. **champion win rate: noctis** - WR 15.6% [6.9, 31.8]
4. **economy outlier: quillan** - 8.55 AP/round = 3.10x roster mean
5. **champion win rate: wisp** - WR 81.2% [64.7, 91.1]

## 12. Delta vs batch_0028

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -0.5 | +0.61 | no |
| bastion | +1.6 | -0.06 | no |
| bramblehide | -17.2 | +0.21 | no |
| brixa | +8.8 | +0.00 | no |
| corvane | +1.5 | +0.07 | no |
| dax | -6.7 | +0.11 | no |
| grivven | +3.1 | -0.02 | no |
| kaelis | +10.4 | +0.07 | no |
| kestrel | -33.0 | -0.04 | no |
| lumen | +13.9 | +0.02 | no |
| marrow | +7.0 | +0.08 | no |
| mossgrove | +15.9 | +0.05 | no |
| noctis | -23.3 | -0.06 | no |
| orrin | -2.2 | -0.10 | no |
| ossuar | -27.3 | +0.20 | no |
| pallas | -5.3 | +0.52 | no |
| quillan | +8.3 | +0.71 | no |
| rictus | +3.3 | +0.06 | no |
| sable | +15.5 | +0.14 | no |
| sylphine | +3.5 | +0.05 | no |
| thornjaw | -10.0 | +0.14 | no |
| vellum | +14.3 | +0.47 | no |
| veyra | +23.8 | -0.00 | no |
| vurmak | +29.2 | +0.06 | no |
| wisp | -8.8 | +0.81 | no |

- median length delta: +2.0
- nexus-kill rate delta: -2.5 pts
