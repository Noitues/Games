# Sim report batch_0005

## 1. Header

| field | value |
|---|---|
| rules | 1.0.0 |
| roster | 1.1.0 |
| ai | 1.1.0 |
| matchup | T1_greedy vs T0_random (temperature 0.3) |
| games | 200 |
| seed | 777001 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 231.1s |
| engine tests | 78 passed in 30.49s |
| generated | 2026-09-19 17:07:51 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 1 FAIL / 24 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 54/58 abilities outside the band; roster mean 15.8%; 0 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 97.0% [93.6, 98.6] | **FAIL** |
| Median game length 13-18 rounds | 14.0 [12.0, 16.0] | **INCONCLUSIVE** |
| >=95% of games end by Nexus kill before round 20 | 78.5% [72.3, 83.6] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, ossuar, quillan, sable (roster mean 1.63 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.0% [41.2, 54.9] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| grivven | 69.7 [58.7, 78.9] | 76 | 1.74 | 1.06 | 13% | 5% | 0% | 33% | 0.39 | 1.24 | 2.4 | 4.8 | 12% | bootsx69, ruby_crystalx68, cloth_armorx65 |
| orrin | 58.7 [48.5, 68.2] | 92 | 0.73 | 0.45 | 11% | 22% | 9% | 5% | 0.10 | 1.48 | 2.6 | 2.7 | 6% | ruby_crystalx76, bootsx74, vampiric_bladex68 |
| marrow | 57.1 [45.5, 68.1] | 70 | 1.06 | 0.65 | 6% | 5% | 4% | 30% | 0.17 | 1.34 | 2.5 | 2.8 | 10% | long_swordx54, ruby_crystalx54, cloth_armorx51 |
| thornjaw | 57.1 [46.5, 67.2] | 84 | 0.76 | 0.46 | 17% | 10% | 10% | 8% | 0.14 | 1.50 | 2.5 | 1.4 | 7% | bootsx70, ruby_crystalx68, vampiric_bladex64 |
| bramblehide | 55.9 [44.1, 67.1] | 68 | 2.39 | 1.46 | 4% | 4% | 2% | 41% | 0.41 | 2.13 | 3.6 | 2.3 | 16% | bootsx52, vampiric_bladex51, ruby_crystalx49 |
| sable | 54.5 [44.2, 64.5] | 88 | 5.12 | 3.14 | 5% | 6% | 0% | 40% | 0.93 | 1.70 | 2.9 | 1.4 | 27% | ruby_crystalx68, bootsx65, longbowx64 |
| kestrel | 53.3 [43.1, 63.1] | 92 | 1.27 | 0.78 | 7% | 11% | 3% | 27% | 0.17 | 1.58 | 2.9 | 3.9 | 11% | bootsx72, vampiric_bladex67, ruby_crystalx65 |
| bastion | 52.3 [41.9, 62.6] | 86 | 1.37 | 0.84 | 7% | 14% | 3% | 21% | 0.31 | 1.45 | 2.7 | 3.3 | 11% | ruby_crystalx63, cloth_armorx59, long_swordx59 |
| ashwyn | 51.9 [38.9, 64.6] | 54 | 4.61 | 2.82 | 3% | 43% | 3% | 13% | 0.67 | 1.80 | 3.2 | 0.7 | 26% | ruby_crystalx43, bootsx40, longbowx39 |
| ossuar | 51.4 [40.0, 62.8] | 70 | 2.81 | 1.72 | 4% | 2% | 5% | 38% | 0.51 | 1.49 | 2.9 | 2.7 | 16% | ruby_crystalx59, bootsx56, vampiric_bladex53 |
| vellum | 51.1 [41.0, 61.1] | 92 | 2.00 | 1.23 | 5% | 2% | 3% | 50% | 0.41 | 1.78 | 3.2 | 2.3 | 17% | ruby_crystalx72, long_swordx64, bootsx63 |
| corvane | 50.0 [40.1, 59.9] | 94 | 0.35 | 0.22 | 26% | 9% | 5% | 6% | 0.17 | 1.77 | 3.1 | 3.5 | 5% | ruby_crystalx74, bootsx72, cloth_armorx65 |
| vurmak | 48.9 [38.7, 59.1] | 88 | 0.93 | 0.57 | 10% | 4% | 4% | 27% | 0.14 | 1.74 | 3.0 | 2.5 | 9% | ruby_crystalx64, cloth_armorx63, vampiric_bladex56 |
| mossgrove | 48.4 [36.6, 60.4] | 64 | 0.59 | 0.36 | 9% | 14% | 6% | 17% | 0.12 | 1.56 | 2.7 | 3.0 | 6% | ruby_crystalx48, bootsx47, vampiric_bladex44 |
| veyra | 48.4 [36.6, 60.4] | 64 | 0.82 | 0.50 | 8% | 12% | 5% | 32% | 0.12 | 1.69 | 3.0 | 4.5 | 8% | ruby_crystalx49, vampiric_bladex44, long_swordx42 |
| wisp | 47.1 [35.7, 58.8] | 68 | 2.08 | 1.27 | 7% | 21% | 1% | 18% | 0.26 | 2.21 | 3.8 | 1.3 | 14% | bootsx52, cloth_armorx46, ruby_crystalx44 |
| noctis | 47.0 [37.5, 56.7] | 100 | 0.50 | 0.31 | 18% | 7% | 20% | 15% | 0.32 | 1.68 | 2.6 | 2.6 | 6% | ruby_crystalx67, longbowx58, long_swordx56 |
| sylphine | 47.0 [37.5, 56.7] | 100 | 0.62 | 0.38 | 13% | 7% | 6% | 17% | 0.06 | 2.03 | 3.7 | 1.9 | 7% | ruby_crystalx83, bootsx79, vampiric_bladex67 |
| brixa | 46.6 [36.5, 56.9] | 88 | 0.82 | 0.50 | 8% | 10% | 8% | 24% | 0.10 | 2.01 | 3.4 | 2.4 | 8% | bootsx66, ruby_crystalx64, vampiric_bladex56 |
| quillan | 45.5 [34.0, 57.4] | 66 | 5.69 | 3.49 | 4% | 4% | 4% | 36% | 0.82 | 2.21 | 4.0 | 1.4 | 28% | ruby_crystalx55, bootsx49, longbowx40 |
| lumen | 45.1 [34.8, 55.9] | 82 | 0.49 | 0.30 | 27% | 4% | 3% | 15% | 0.06 | 1.80 | 3.0 | 1.6 | 6% | bootsx63, ruby_crystalx61, cloth_armorx54 |
| rictus | 42.9 [32.8, 53.5] | 84 | 0.62 | 0.38 | 14% | 9% | 9% | 7% | 0.21 | 2.46 | 4.1 | 1.1 | 7% | bootsx61, ruby_crystalx55, vampiric_bladex49 |
| kaelis | 41.9 [32.0, 52.4] | 86 | 0.77 | 0.47 | 12% | 12% | 3% | 16% | 0.07 | 2.05 | 3.4 | 1.4 | 8% | ruby_crystalx61, cloth_armorx59, vampiric_bladex52 |
| dax | 39.1 [28.1, 51.3] | 64 | 0.84 | 0.51 | 10% | 11% | 5% | 21% | 0.16 | 2.02 | 3.6 | 2.2 | 9% | ruby_crystalx45, bootsx43, vampiric_bladex40 |
| pallas | 38.8 [28.8, 49.7] | 80 | 1.82 | 1.12 | 5% | 7% | 3% | 29% | 0.33 | 2.20 | 3.9 | 2.0 | 15% | bootsx60, ruby_crystalx53, cloth_armorx48 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [45.1, 54.9] | 0.90 |
| Jungle | 50.0 [45.1, 54.9] | 0.95 |
| Mid | 50.0 [45.1, 54.9] | 3.27 |
| Support | 50.0 [45.1, 54.9] | 1.23 |
| Top | 50.0 [45.1, 54.9] | 1.34 |

## 5. Games

- length: median 14.0, p10 9, p90 20
- end reasons: {'nexus': 157, 'round_limit_towers': 37, 'round_limit_hp': 5, 'round_limit_kills': 1} (draws 0)
- priority win rate: 97.0% [93.6, 98.6]
- north win rate: 48.0% [41.2, 54.9]
- length histogram: {7: 1, 8: 6, 9: 17, 10: 24, 11: 18, 12: 22, 13: 10, 14: 6, 15: 9, 16: 12, 17: 4, 18: 6, 19: 12, 20: 53}

## 6. Objectives

- takes per game: {'dragon': 1.645, 'baron': 0.765}
- median round taken: dragon 8, baron 12
- win rate when secured: {'dragon': 90.88145896656535, 'baron': 90.19607843137256}
- camp clears per game: {'krugs': 9.555, 'wolves': 9.035, 'raptors': 9.465, 'blue_buff': 4.9, 'red_buff': 5.01, 'dragon': 1.645, 'baron': 0.765}

## 7. Structures

- first tower falls: median round 5.0, p10 3, p90 9
- games with at least one tower down: 100.0%
- first-tower win rate: 96.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| base | 3.34 |
| chips_wave | 2.84 |
| chips_monster | 2.32 |
| chips_structure | 1.67 |
| champion_kill | 0.56 |
| blue_buff | 0.29 |
| red_buff | 0.20 |

| use | AP |
|---|---|
| shop | 8.50 |
| abilities | 1.92 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.98 | 63.6% | 16.8% | +46.8 |
| cloth_armor | 5 | 1.88 | 63.3% | 36.0% | +27.3 |
| control_ward | 2 | 1.26 | - | 50.0% | - |
| frost_charm | 2 | 1.12 | - | 50.0% | - |
| health_potion | 2 | 1.84 | - | 50.0% | - |
| ionian_charm | 8 | 1.30 | 90.7% | 15.5% | +75.2 |
| long_sword | 6 | 1.67 | 75.9% | 22.2% | +53.7 |
| longbow | 6 | 1.70 | 70.4% | 35.0% | +35.4 |
| ruby_crystal | 4 | 1.95 | 65.8% | 1.6% | +64.2 |
| stopwatch | 3 | 1.72 | - | 50.0% | - |
| swift_tonic | 1 | 1.96 | - | 50.0% | - |
| vampiric_blade | 5 | 1.82 | 66.7% | 29.5% | +37.2 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: quillan** - 5.69 AP/round = 3.49x roster mean
2. **economy outlier: sable** - 5.12 AP/round = 3.14x roster mean
3. **economy outlier: ashwyn** - 4.61 AP/round = 2.82x roster mean
4. **Priority (first player) win rate 48-52%** - 97.0% [93.6, 98.6]
5. **>=95% of games end by Nexus kill before round 20** - 78.5% [72.3, 83.6]
