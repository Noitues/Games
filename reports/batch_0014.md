# Sim report batch_0014

## 1. Header

| field | value |
|---|---|
| rules | 1.1.0 |
| roster | 1.2.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 1401 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 363.2s |
| engine tests | 104 passed in 60.18s (0:01:00) |
| generated | 2026-09-20 10:47:34 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 8 FAIL / 17 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 52/56 abilities outside the band; roster mean 17.7%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 44.0% [36.3, 52.0] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 11.0 [11.0, 11.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 99.3% [96.3, 99.9] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.41 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.7% [40.8, 56.6] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 85.0 [73.9, 91.9] | 60 | 9.78 | 4.06 | 2% | 86% | 0% | 6% | 0.02 | 0.00 | 0.0 | 0.1 | 49% | ionian_charmx60, long_swordx60, longbowx60 |
| wisp | 82.9 [72.4, 89.9] | 70 | 6.22 | 2.58 | 11% | 69% | 0% | 8% | 0.00 | 0.00 | 0.0 | 0.0 | 33% | longbowx70, ruby_crystalx70, bootsx69 |
| bramblehide | 74.3 [63.0, 83.1] | 70 | 1.98 | 0.82 | 4% | 23% | 1% | 29% | 0.00 | 0.00 | 0.0 | 3.1 | 13% | long_swordx70, ruby_crystalx70, vampiric_bladex68 |
| ossuar | 71.0 [58.7, 80.8] | 62 | 1.93 | 0.80 | 17% | 8% | 4% | 38% | 0.00 | 0.02 | 0.0 | 3.1 | 12% | long_swordx62, ruby_crystalx62, cloth_armorx60 |
| bastion | 66.7 [52.5, 78.3] | 48 | 1.52 | 0.63 | 43% | 4% | 3% | 8% | 0.02 | 0.00 | 0.0 | 1.2 | 9% | long_swordx48, ruby_crystalx48, cloth_armorx46 |
| pallas | 64.1 [51.8, 74.7] | 64 | 4.50 | 1.87 | 8% | 1% | 1% | 83% | 0.00 | 0.03 | 0.1 | 4.0 | 27% | longbowx64, ruby_crystalx64, bootsx63 |
| quillan | 62.1 [50.1, 72.9] | 66 | 7.48 | 3.11 | 4% | 3% | 1% | 83% | 0.00 | 0.05 | 0.1 | 2.5 | 41% | longbowx66, ionian_charmx65, ruby_crystalx63 |
| sylphine | 59.6 [46.1, 71.8] | 52 | 0.81 | 0.33 | 11% | 1% | 11% | 17% | 0.00 | 0.00 | 0.0 | 1.1 | 5% | long_swordx52, ruby_crystalx52, vampiric_bladex49 |
| veyra | 56.0 [42.3, 68.8] | 50 | 1.04 | 0.43 | 11% | 34% | 6% | 16% | 0.00 | 0.00 | 0.0 | 2.6 | 7% | long_swordx50, longbowx50, vampiric_bladex46 |
| dax | 54.7 [42.6, 66.3] | 64 | 1.13 | 0.47 | 18% | 28% | 4% | 19% | 0.00 | 0.02 | 0.0 | 2.1 | 8% | long_swordx64, longbowx62, vampiric_bladex61 |
| kestrel | 53.4 [40.8, 65.7] | 58 | 1.79 | 0.75 | 44% | 17% | 5% | 23% | 0.00 | 0.00 | 0.0 | 2.5 | 12% | long_swordx58, longbowx58, vampiric_bladex55 |
| brixa | 51.6 [39.6, 63.4] | 64 | 1.14 | 0.47 | 27% | 10% | 10% | 11% | 0.00 | 0.00 | 0.0 | 1.0 | 8% | long_swordx64, longbowx64, vampiric_bladex57 |
| thornjaw | 47.7 [33.8, 62.1] | 44 | 0.95 | 0.40 | 12% | 17% | 7% | 5% | 0.00 | 0.02 | 0.0 | 0.6 | 7% | long_swordx44, ruby_crystalx43, vampiric_bladex37 |
| vurmak | 44.8 [32.7, 57.5] | 58 | 1.28 | 0.53 | 16% | 6% | 3% | 40% | 0.00 | 0.00 | 0.0 | 3.2 | 9% | ruby_crystalx58, long_swordx52, cloth_armorx48 |
| marrow | 43.9 [32.6, 55.9] | 66 | 1.55 | 0.64 | 15% | 3% | 9% | 21% | 0.03 | 0.00 | 0.0 | 0.9 | 11% | long_swordx66, ruby_crystalx66, cloth_armorx61 |
| vellum | 37.9 [26.6, 50.8] | 58 | 2.58 | 1.07 | 17% | 1% | 7% | 63% | 0.00 | 0.02 | 0.0 | 2.5 | 20% | longbowx58, ionian_charmx56, ruby_crystalx49 |
| sable | 37.5 [26.0, 50.6] | 56 | 5.75 | 2.39 | 3% | 56% | 0% | 27% | 0.00 | 0.04 | 0.1 | 2.9 | 38% | longbowx56, ionian_charmx53, ruby_crystalx48 |
| grivven | 36.4 [23.8, 51.1] | 44 | 2.82 | 1.17 | 14% | 3% | 0% | 55% | 0.02 | 0.00 | 0.0 | 6.3 | 20% | longbowx44, ruby_crystalx44, bootsx43 |
| orrin | 35.9 [25.3, 48.2] | 64 | 0.88 | 0.37 | 17% | 19% | 10% | 5% | 0.00 | 0.03 | 0.1 | 1.8 | 6% | long_swordx64, longbowx60, vampiric_bladex53 |
| rictus | 34.4 [23.9, 46.6] | 64 | 0.95 | 0.40 | 21% | 19% | 20% | 2% | 0.02 | 0.05 | 0.1 | 1.8 | 7% | long_swordx64, ruby_crystalx64, vampiric_bladex49 |
| mossgrove | 34.3 [24.2, 46.0] | 70 | 0.84 | 0.35 | 24% | 17% | 1% | 8% | 0.00 | 0.00 | 0.0 | 2.8 | 6% | long_swordx70, ruby_crystalx70, vampiric_bladex61 |
| lumen | 32.5 [23.2, 43.4] | 80 | 0.63 | 0.26 | 35% | 3% | 1% | 3% | 0.01 | 0.01 | 0.0 | 0.4 | 5% | longbowx80, ruby_crystalx80, bootsx70 |
| kaelis | 28.8 [19.3, 40.6] | 66 | 0.87 | 0.36 | 23% | 16% | 5% | 10% | 0.00 | 0.03 | 0.1 | 0.8 | 6% | ruby_crystalx66, long_swordx62, cloth_armorx59 |
| noctis | 25.0 [15.8, 37.2] | 60 | 1.37 | 0.57 | 51% | 3% | 22% | 1% | 0.03 | 0.02 | 0.1 | 0.3 | 13% | longbowx60, ionian_charmx50, ruby_crystalx45 |
| corvane | 21.4 [11.7, 35.9] | 42 | 0.40 | 0.17 | 32% | 2% | 11% | 0% | 0.00 | 0.05 | 0.1 | 3.4 | 3% | longbowx42, ruby_crystalx42, bootsx38 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 1.19 |
| Jungle | 50.0 [44.4, 55.6] | 1.14 |
| Mid | 50.0 [44.4, 55.6] | 5.45 |
| Support | 50.0 [44.4, 55.6] | 3.05 |
| Top | 50.0 [44.4, 55.6] | 1.42 |

## 5. Games

- length: median 11.0, p10 9, p90 14
- end reasons: {'nexus': 149, 'round_limit_towers': 1} (draws 0)
- priority win rate: 44.0% [36.3, 52.0]
- north win rate: 48.7% [40.8, 56.6]
- length histogram: {7: 3, 8: 11, 9: 16, 10: 24, 11: 38, 12: 24, 13: 12, 14: 7, 15: 3, 16: 8, 18: 3, 20: 1}

## 6. Objectives

- takes per game: {'dragon': 1.34, 'baron': 0.4666666666666667}
- median round taken: dragon 6, baron 10.0
- win rate when secured: {'dragon': 48.25870646766169, 'baron': 37.142857142857146}
- camp clears per game: {'krugs': 5.44, 'raptors': 5.44, 'red_buff': 3.3533333333333335, 'wolves': 4.98, 'blue_buff': 3.2533333333333334, 'dragon': 1.34, 'baron': 0.4666666666666667}

## 7. Structures

- first tower falls: median round 4.0, p10 3, p90 5
- games with at least one tower down: 100.0%
- first-tower win rate: 71.3%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.29 |
| chips_structure | 3.80 |
| chips_wave | 3.71 |
| base | 3.27 |
| blue_buff | 0.28 |
| red_buff | 0.21 |
| champion_kill | 0.01 |

| use | AP |
|---|---|
| shop | 12.09 |
| abilities | 2.10 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.89 | 65.9% | 17.4% | +48.5 |
| cloth_armor | 5 | 1.83 | 65.4% | 35.6% | +29.8 |
| control_ward | 2 | 0.47 | - | 50.0% | - |
| frost_charm | 2 | 0.27 | - | 50.0% | - |
| health_potion | 2 | 1.83 | - | 50.0% | - |
| ionian_charm | 8 | 1.89 | 68.8% | 22.4% | +46.4 |
| long_sword | 6 | 2.00 | 53.4% | 40.4% | +13.1 |
| longbow | 6 | 2.00 | 50.3% | 49.5% | +0.8 |
| ruby_crystal | 4 | 2.00 | 53.1% | 7.8% | +45.3 |
| stopwatch | 3 | 1.77 | - | 50.0% | - |
| swift_tonic | 1 | 1.97 | - | 50.0% | - |
| vampiric_blade | 5 | 1.85 | 60.8% | 34.9% | +25.9 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 9.78 AP/round = 4.06x roster mean
2. **champion win rate: ashwyn** - WR 85.0% [73.9, 91.9]
3. **champion win rate: wisp** - WR 82.9% [72.4, 89.9]
4. **economy outlier: quillan** - 7.48 AP/round = 3.11x roster mean
5. **champion win rate: corvane** - WR 21.4% [11.7, 35.9]
