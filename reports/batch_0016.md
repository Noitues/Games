# Sim report batch_0016

## 1. Header

| field | value |
|---|---|
| rules | 1.1.0 |
| roster | 1.2.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 1601 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 388.4s |
| engine tests | 105 passed in 60.57s (0:01:00) |
| generated | 2026-09-20 17:14:41 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 7 FAIL / 18 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 53/56 abilities outside the band; roster mean 18.0%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 46.7% [38.9, 54.6] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 11.0 [11.0, 11.5] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 97.3% [93.3, 99.0] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.41 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 47.3% [39.5, 55.3] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 87.5 [77.2, 93.5] | 64 | 9.51 | 3.94 | 2% | 84% | 0% | 7% | 0.02 | 0.00 | 0.0 | 0.1 | 48% | bootsx64, ionian_charmx64, long_swordx64 |
| wisp | 83.3 [72.0, 90.7] | 60 | 6.20 | 2.57 | 11% | 68% | 1% | 9% | 0.02 | 0.03 | 0.1 | 0.0 | 34% | longbowx60, ruby_crystalx60, bootsx59 |
| pallas | 72.0 [58.3, 82.5] | 50 | 4.59 | 1.90 | 7% | 1% | 1% | 83% | 0.00 | 0.02 | 0.0 | 3.8 | 26% | longbowx50, ruby_crystalx50, bootsx49 |
| kestrel | 69.0 [56.2, 79.4] | 58 | 1.86 | 0.77 | 47% | 16% | 4% | 21% | 0.00 | 0.00 | 0.0 | 2.4 | 11% | long_swordx58, longbowx58, vampiric_bladex57 |
| quillan | 62.5 [48.4, 74.8] | 48 | 7.81 | 3.23 | 5% | 5% | 1% | 82% | 0.04 | 0.00 | 0.0 | 2.5 | 43% | ionian_charmx48, longbowx48, ruby_crystalx48 |
| ossuar | 58.3 [46.8, 69.0] | 72 | 1.94 | 0.80 | 18% | 9% | 4% | 37% | 0.00 | 0.00 | 0.0 | 3.0 | 12% | ruby_crystalx72, long_swordx71, cloth_armorx65 |
| veyra | 55.0 [42.5, 66.9] | 60 | 0.99 | 0.41 | 12% | 32% | 6% | 16% | 0.00 | 0.03 | 0.1 | 2.5 | 7% | long_swordx60, longbowx56, vampiric_bladex48 |
| rictus | 53.6 [40.7, 66.0] | 56 | 1.03 | 0.43 | 17% | 19% | 20% | 4% | 0.00 | 0.05 | 0.1 | 1.6 | 7% | long_swordx56, ruby_crystalx54, vampiric_bladex46 |
| dax | 52.8 [41.4, 63.9] | 72 | 1.21 | 0.50 | 17% | 30% | 4% | 19% | 0.00 | 0.01 | 0.0 | 1.9 | 8% | long_swordx72, longbowx71, vampiric_bladex65 |
| bastion | 51.8 [39.0, 64.3] | 56 | 1.52 | 0.63 | 40% | 3% | 2% | 10% | 0.02 | 0.00 | 0.0 | 1.6 | 10% | ruby_crystalx56, long_swordx55, cloth_armorx53 |
| sylphine | 51.6 [39.6, 63.4] | 64 | 0.78 | 0.33 | 12% | 1% | 13% | 16% | 0.00 | 0.00 | 0.0 | 1.2 | 5% | long_swordx64, ruby_crystalx64, vampiric_bladex55 |
| vurmak | 51.6 [39.6, 63.4] | 64 | 1.27 | 0.53 | 20% | 6% | 3% | 35% | 0.03 | 0.05 | 0.1 | 3.1 | 9% | ruby_crystalx64, long_swordx61, cloth_armorx54 |
| bramblehide | 50.0 [37.1, 62.9] | 54 | 1.99 | 0.83 | 6% | 23% | 2% | 38% | 0.04 | 0.00 | 0.0 | 3.7 | 14% | long_swordx54, ruby_crystalx54, vampiric_bladex54 |
| lumen | 50.0 [37.1, 62.9] | 54 | 0.68 | 0.28 | 35% | 3% | 1% | 3% | 0.00 | 0.02 | 0.1 | 0.3 | 5% | longbowx54, ruby_crystalx54, bootsx49 |
| marrow | 48.6 [37.4, 59.9] | 72 | 1.58 | 0.65 | 15% | 2% | 10% | 20% | 0.01 | 0.00 | 0.0 | 0.9 | 12% | ruby_crystalx72, long_swordx71, cloth_armorx65 |
| thornjaw | 48.3 [35.9, 60.8] | 58 | 0.97 | 0.40 | 12% | 16% | 9% | 5% | 0.02 | 0.00 | 0.0 | 0.8 | 7% | long_swordx58, ruby_crystalx55, vampiric_bladex49 |
| mossgrove | 47.1 [35.7, 58.8] | 68 | 0.78 | 0.32 | 24% | 18% | 1% | 9% | 0.00 | 0.01 | 0.0 | 3.0 | 5% | long_swordx68, ruby_crystalx68, vampiric_bladex57 |
| sable | 37.9 [26.6, 50.8] | 58 | 5.83 | 2.42 | 8% | 57% | 0% | 23% | 0.00 | 0.00 | 0.0 | 2.6 | 37% | longbowx58, ionian_charmx55, ruby_crystalx53 |
| orrin | 36.2 [25.1, 49.1] | 58 | 0.86 | 0.35 | 19% | 18% | 12% | 4% | 0.00 | 0.05 | 0.1 | 1.8 | 6% | long_swordx58, longbowx54, vampiric_bladex48 |
| vellum | 35.7 [26.3, 46.4] | 84 | 2.61 | 1.08 | 16% | 0% | 8% | 66% | 0.00 | 0.04 | 0.1 | 2.6 | 21% | longbowx84, ionian_charmx74, ruby_crystalx67 |
| brixa | 34.6 [23.2, 48.2] | 52 | 1.13 | 0.47 | 29% | 10% | 9% | 9% | 0.00 | 0.00 | 0.0 | 0.9 | 8% | long_swordx52, longbowx51, vampiric_bladex47 |
| grivven | 31.6 [22.2, 42.7] | 76 | 2.71 | 1.12 | 17% | 3% | 1% | 53% | 0.01 | 0.00 | 0.0 | 6.0 | 19% | longbowx76, ruby_crystalx76, bootsx71 |
| kaelis | 30.6 [18.0, 46.9] | 36 | 0.86 | 0.36 | 25% | 17% | 4% | 11% | 0.00 | 0.00 | 0.0 | 1.1 | 6% | long_swordx36, ruby_crystalx36, cloth_armorx33 |
| noctis | 26.1 [15.6, 40.3] | 46 | 1.26 | 0.52 | 42% | 6% | 22% | 2% | 0.00 | 0.07 | 0.1 | 0.5 | 12% | longbowx46, ionian_charmx37, ruby_crystalx31 |
| corvane | 21.7 [13.1, 33.6] | 60 | 0.37 | 0.15 | 31% | 1% | 12% | 2% | 0.00 | 0.03 | 0.1 | 3.4 | 3% | longbowx60, ruby_crystalx60, bootsx55 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 1.21 |
| Jungle | 50.0 [44.4, 55.6] | 1.08 |
| Mid | 50.0 [44.4, 55.6] | 5.33 |
| Support | 50.0 [44.4, 55.6] | 2.89 |
| Top | 50.0 [44.4, 55.6] | 1.50 |

## 5. Games

- length: median 11.0, p10 9, p90 16
- end reasons: {'nexus': 146, 'round_limit_hp': 2, 'round_limit_towers': 2} (draws 0)
- priority win rate: 46.7% [38.9, 54.6]
- north win rate: 47.3% [39.5, 55.3]
- length histogram: {7: 3, 8: 8, 9: 20, 10: 28, 11: 29, 12: 17, 13: 16, 14: 7, 15: 6, 16: 4, 17: 3, 18: 3, 19: 1, 20: 5}

## 6. Objectives

- takes per game: {'dragon': 1.4066666666666667, 'baron': 0.42}
- median round taken: dragon 6, baron 11
- win rate when secured: {'dragon': 41.70616113744076, 'baron': 41.26984126984127}
- camp clears per game: {'krugs': 5.6466666666666665, 'red_buff': 3.3733333333333335, 'raptors': 5.626666666666667, 'wolves': 5.02, 'blue_buff': 3.2533333333333334, 'dragon': 1.4066666666666667, 'baron': 0.42}

## 7. Structures

- first tower falls: median round 4.0, p10 3, p90 5
- games with at least one tower down: 100.0%
- first-tower win rate: 73.3%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.20 |
| chips_structure | 3.71 |
| chips_wave | 3.63 |
| base | 3.29 |
| blue_buff | 0.27 |
| red_buff | 0.21 |
| champion_kill | 0.01 |

| use | AP |
|---|---|
| shop | 11.82 |
| abilities | 2.17 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.89 | 65.4% | 17.9% | +47.5 |
| cloth_armor | 5 | 1.80 | 64.4% | 36.2% | +28.3 |
| control_ward | 2 | 0.51 | - | 50.0% | - |
| frost_charm | 2 | 0.35 | - | 50.0% | - |
| health_potion | 2 | 1.83 | - | 50.0% | - |
| ionian_charm | 8 | 1.85 | 67.6% | 23.6% | +44.0 |
| long_sword | 6 | 2.00 | 53.6% | 39.8% | +13.7 |
| longbow | 6 | 2.00 | 50.6% | 49.2% | +1.4 |
| ruby_crystal | 4 | 2.00 | 53.6% | 2.8% | +50.8 |
| stopwatch | 3 | 1.81 | - | 50.0% | - |
| swift_tonic | 1 | 1.95 | - | 50.0% | - |
| vampiric_blade | 5 | 1.81 | 60.8% | 35.1% | +25.7 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 65.82 per game
- that is 85.0% of all ability uses


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 9.51 AP/round = 3.94x roster mean
2. **champion win rate: ashwyn** - WR 87.5% [77.2, 93.5]
3. **economy outlier: quillan** - 7.81 AP/round = 3.23x roster mean
4. **champion win rate: wisp** - WR 83.3% [72.0, 90.7]
5. **champion win rate: corvane** - WR 21.7% [13.1, 33.6]
