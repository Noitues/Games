# Sim report batch_0004

## 1. Header

| field | value |
|---|---|
| rules | 1.0.0 |
| roster | 1.1.0 |
| ai | 1.0.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 400 |
| seed | 525252 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 457.3s |
| engine tests | 78 passed in 25.32s |
| generated | 2026-09-19 06:12:18 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 8 FAIL / 17 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 47/58 abilities outside the band; roster mean 27.1%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 47.5% [42.7, 52.4] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 12.0 [12.0, 12.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 98.8% [97.1, 99.5] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, ossuar, quillan, sable (roster mean 2.16 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.5% [43.6, 53.4] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 91.1 [85.8, 94.5] | 168 | 10.95 | 5.07 | 0% | 4% | 0% | 94% | 2.59 | 1.45 | 2.1 | 2.0 | 51% | ionian_charmx168, longbowx168, ruby_crystalx168 |
| ossuar | 68.4 [60.7, 75.1] | 158 | 4.58 | 2.12 | 1% | 0% | 0% | 90% | 0.99 | 0.80 | 1.4 | 4.2 | 26% | long_swordx158, ruby_crystalx158, cloth_armorx154 |
| pallas | 64.1 [56.7, 70.9] | 170 | 2.60 | 1.21 | 6% | 8% | 4% | 63% | 0.75 | 1.60 | 2.7 | 2.9 | 16% | ruby_crystalx167, longbowx153, bootsx150 |
| kestrel | 63.8 [55.9, 71.0] | 152 | 1.62 | 0.75 | 8% | 18% | 1% | 61% | 0.54 | 1.07 | 1.9 | 5.3 | 11% | long_swordx147, longbowx128, vampiric_bladex125 |
| sable | 61.4 [53.9, 68.5] | 166 | 7.01 | 3.25 | 5% | 9% | 0% | 78% | 1.82 | 1.61 | 2.6 | 2.6 | 41% | longbowx161, ionian_charmx150, ruby_crystalx150 |
| ashwyn | 60.0 [52.0, 67.5] | 150 | 6.81 | 3.15 | 2% | 80% | 0% | 14% | 1.31 | 1.71 | 3.0 | 0.4 | 42% | longbowx150, ruby_crystalx148, ionian_charmx147 |
| grivven | 59.7 [51.8, 67.2] | 154 | 1.82 | 0.84 | 25% | 4% | 1% | 52% | 0.57 | 1.25 | 2.4 | 5.3 | 12% | ruby_crystalx154, longbowx150, bootsx148 |
| mossgrove | 58.5 [50.2, 66.2] | 142 | 0.55 | 0.25 | 16% | 17% | 7% | 28% | 0.36 | 1.15 | 2.1 | 3.8 | 4% | ruby_crystalx138, long_swordx136, vampiric_bladex117 |
| brixa | 55.4 [47.4, 63.2] | 148 | 0.91 | 0.42 | 12% | 10% | 9% | 46% | 0.36 | 1.22 | 2.1 | 3.4 | 6% | long_swordx147, longbowx128, vampiric_bladex127 |
| sylphine | 54.1 [46.0, 61.9] | 148 | 0.58 | 0.27 | 23% | 10% | 10% | 29% | 0.35 | 1.01 | 1.8 | 2.6 | 4% | ruby_crystalx143, long_swordx128, vampiric_bladex109 |
| bastion | 53.0 [45.4, 60.4] | 168 | 1.62 | 0.75 | 13% | 16% | 1% | 42% | 0.69 | 1.10 | 1.9 | 4.2 | 11% | ruby_crystalx168, cloth_armorx151, long_swordx151 |
| bramblehide | 51.6 [44.5, 58.5] | 192 | 2.87 | 1.33 | 3% | 7% | 1% | 74% | 1.05 | 1.80 | 2.8 | 3.2 | 19% | long_swordx192, ruby_crystalx189, vampiric_bladex166 |
| thornjaw | 51.3 [43.5, 59.1] | 154 | 0.65 | 0.30 | 26% | 15% | 11% | 10% | 0.46 | 1.27 | 2.0 | 1.4 | 5% | ruby_crystalx150, long_swordx140, vampiric_bladex111 |
| dax | 48.1 [40.6, 55.8] | 162 | 0.97 | 0.45 | 12% | 19% | 3% | 45% | 0.29 | 1.13 | 1.9 | 3.0 | 7% | long_swordx156, vampiric_bladex132, longbowx126 |
| lumen | 46.4 [39.0, 54.0] | 166 | 0.35 | 0.16 | 47% | 5% | 3% | 19% | 0.30 | 0.64 | 1.2 | 2.0 | 3% | ruby_crystalx164, longbowx159, bootsx146 |
| marrow | 45.2 [37.8, 52.8] | 166 | 0.98 | 0.45 | 7% | 9% | 7% | 43% | 0.51 | 0.99 | 1.8 | 3.2 | 7% | ruby_crystalx165, long_swordx135, cloth_armorx128 |
| wisp | 45.0 [37.0, 53.3] | 140 | 2.63 | 1.22 | 10% | 32% | 3% | 45% | 0.72 | 1.76 | 2.8 | 2.5 | 19% | ruby_crystalx134, longbowx123, bootsx108 |
| vurmak | 42.9 [35.7, 50.5] | 170 | 0.96 | 0.45 | 16% | 6% | 5% | 47% | 0.44 | 1.24 | 2.1 | 3.3 | 8% | ruby_crystalx169, long_swordx117, cloth_armorx110 |
| veyra | 42.5 [35.1, 50.2] | 160 | 0.99 | 0.46 | 8% | 17% | 2% | 57% | 0.19 | 1.26 | 2.3 | 5.0 | 7% | long_swordx140, longbowx134, vampiric_bladex123 |
| orrin | 42.1 [35.1, 49.5] | 178 | 0.73 | 0.34 | 15% | 36% | 11% | 6% | 0.43 | 1.27 | 2.3 | 3.3 | 6% | long_swordx161, longbowx147, vampiric_bladex132 |
| kaelis | 39.9 [32.1, 48.2] | 138 | 0.73 | 0.34 | 23% | 15% | 4% | 27% | 0.33 | 1.23 | 2.1 | 1.9 | 6% | ruby_crystalx138, cloth_armorx99, long_swordx95 |
| rictus | 36.0 [29.0, 43.6] | 164 | 0.48 | 0.22 | 20% | 14% | 16% | 16% | 0.60 | 1.59 | 2.7 | 2.1 | 4% | ruby_crystalx160, long_swordx142, vampiric_bladex113 |
| corvane | 34.7 [28.0, 42.1] | 170 | 0.17 | 0.08 | 42% | 11% | 6% | 10% | 0.29 | 1.11 | 2.0 | 4.1 | 1% | longbowx166, ruby_crystalx164, bootsx149 |
| vellum | 30.1 [23.3, 38.0] | 146 | 2.12 | 0.98 | 7% | 1% | 2% | 79% | 0.76 | 1.72 | 3.1 | 3.0 | 18% | longbowx130, ruby_crystalx114, ionian_charmx94 |
| noctis | 6.5 [3.7, 11.2] | 170 | 0.35 | 0.16 | 23% | 4% | 26% | 20% | 0.62 | 1.51 | 2.7 | 2.4 | 4% | longbowx132, ruby_crystalx103, ionian_charmx77 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [46.5, 53.5] | 1.03 |
| Jungle | 50.0 [46.5, 53.5] | 1.12 |
| Mid | 50.0 [46.5, 53.5] | 5.49 |
| Support | 50.0 [46.5, 53.5] | 1.47 |
| Top | 50.0 [46.5, 53.5] | 1.78 |

## 5. Games

- length: median 12.0, p10 9, p90 16
- end reasons: {'nexus': 395, 'round_limit_towers': 3, 'round_limit_hp': 2} (draws 0)
- priority win rate: 47.5% [42.7, 52.4]
- north win rate: 48.5% [43.6, 53.4]
- length histogram: {7: 1, 8: 15, 9: 36, 10: 51, 11: 53, 12: 69, 13: 47, 14: 46, 15: 31, 16: 23, 17: 8, 18: 10, 19: 1, 20: 9}

## 6. Objectives

- takes per game: {'dragon': 1.785, 'baron': 0.835}
- median round taken: dragon 6.0, baron 10.0
- win rate when secured: {'dragon': 59.943977591036415, 'baron': 61.377245508982035}
- camp clears per game: {'krugs': 8.2775, 'wolves': 7.815, 'raptors': 8.2625, 'red_buff': 4.8075, 'blue_buff': 4.69, 'dragon': 1.785, 'baron': 0.835}

## 7. Structures

- first tower falls: median round 3.0, p10 2, p90 5
- games with at least one tower down: 100.0%
- first-tower win rate: 69.5%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.02 |
| chips_wave | 3.40 |
| base | 3.38 |
| chips_structure | 3.08 |
| champion_kill | 0.46 |
| blue_buff | 0.37 |
| red_buff | 0.22 |

| use | AP |
|---|---|
| shop | 10.62 |
| abilities | 3.11 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.75 | 71.4% | 8.8% | +62.7 |
| cloth_armor | 5 | 1.60 | 73.6% | 30.4% | +43.2 |
| control_ward | 2 | 0.33 | - | 50.0% | - |
| frost_charm | 2 | 0.23 | - | 50.0% | - |
| health_potion | 2 | 1.78 | - | 50.0% | - |
| ionian_charm | 8 | 1.59 | 77.7% | 12.9% | +64.8 |
| long_sword | 6 | 1.92 | 59.3% | 30.9% | +28.4 |
| longbow | 6 | 1.92 | 55.7% | 43.4% | +12.3 |
| ruby_crystal | 4 | 2.00 | 55.1% | 0.3% | +54.8 |
| stopwatch | 3 | 1.86 | - | 50.0% | - |
| swift_tonic | 1 | 1.89 | - | 50.0% | - |
| vampiric_blade | 5 | 1.63 | 69.0% | 28.1% | +40.9 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: quillan** - 10.95 AP/round = 5.07x roster mean
2. **champion win rate: noctis** - WR 6.5% [3.7, 11.2]
3. **champion win rate: quillan** - WR 91.1% [85.8, 94.5]
4. **economy outlier: sable** - 7.01 AP/round = 3.25x roster mean
5. **economy outlier: ashwyn** - 6.81 AP/round = 3.15x roster mean

## 12. Delta vs batch_0002

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -28.0 | -1.00 | yes |
| bastion | +4.0 | -0.33 | no |
| dax | -4.9 | -0.03 | no |
| grivven | +1.7 | -0.10 | no |
| kestrel | +16.8 | -0.15 | yes |
| lumen | +4.4 | +0.01 | no |
| mossgrove | +7.5 | -0.00 | no |
| thornjaw | +2.3 | -0.06 | no |
| vellum | +18.1 | -0.07 | yes |
| vurmak | -8.1 | +0.02 | no |

- median length delta: -3.0
- nexus-kill rate delta: -0.7 pts
