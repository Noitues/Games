# Sim report batch_0009

## 1. Header

| field | value |
|---|---|
| rules | 1.0.0 |
| roster | 1.1.0 |
| ai | 1.2.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 400 |
| seed | 991002 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 2966.5s |
| engine tests | not run |
| generated | 2026-09-19 19:53:49 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 8 FAIL / 17 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 49/58 abilities outside the band; roster mean 28.8%; 10 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 48.8% [43.9, 53.6] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 11.0 [11.0, 11.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 100.0% [99.0, 100.0] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, ossuar, quillan, sable (roster mean 2.36 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.8% [43.9, 53.6] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 83.3 [76.7, 88.4] | 156 | 11.00 | 4.66 | 0% | 3% | 0% | 96% | 1.65 | 1.43 | 2.0 | 1.8 | 50% | ionian_charmx156, longbowx156, ruby_crystalx155 |
| ossuar | 69.1 [61.6, 75.7] | 162 | 4.51 | 1.91 | 1% | 0% | 0% | 93% | 0.70 | 0.72 | 1.2 | 3.9 | 24% | ruby_crystalx162, long_swordx161, cloth_armorx155 |
| sable | 68.1 [61.1, 74.3] | 188 | 7.85 | 3.32 | 1% | 9% | 0% | 87% | 1.35 | 1.63 | 2.3 | 2.4 | 42% | longbowx181, ionian_charmx177, ruby_crystalx177 |
| wisp | 64.0 [56.4, 71.0] | 164 | 3.02 | 1.28 | 5% | 36% | 0% | 54% | 0.77 | 1.66 | 2.6 | 2.7 | 18% | ruby_crystalx163, longbowx161, bootsx151 |
| ashwyn | 60.8 [52.8, 68.3] | 148 | 6.46 | 2.74 | 1% | 79% | 0% | 17% | 0.85 | 1.68 | 2.7 | 0.6 | 39% | longbowx148, ionian_charmx145, ruby_crystalx145 |
| bramblehide | 60.4 [52.5, 67.8] | 154 | 3.12 | 1.32 | 0% | 4% | 2% | 81% | 0.72 | 1.77 | 2.6 | 3.3 | 19% | long_swordx154, ruby_crystalx154, vampiric_bladex141 |
| pallas | 57.7 [50.4, 64.6] | 182 | 3.10 | 1.31 | 3% | 3% | 2% | 81% | 0.47 | 1.65 | 2.5 | 3.1 | 18% | ruby_crystalx181, longbowx178, bootsx166 |
| veyra | 56.2 [48.1, 64.0] | 146 | 1.18 | 0.50 | 3% | 15% | 0% | 71% | 0.21 | 1.07 | 1.8 | 5.2 | 8% | long_swordx132, longbowx119, vampiric_bladex109 |
| sylphine | 54.3 [46.6, 61.8] | 162 | 0.78 | 0.33 | 30% | 4% | 5% | 33% | 0.35 | 0.81 | 1.4 | 2.6 | 5% | ruby_crystalx159, long_swordx155, vampiric_bladex132 |
| dax | 52.9 [45.5, 60.3] | 170 | 1.18 | 0.50 | 7% | 17% | 2% | 60% | 0.31 | 1.09 | 1.8 | 3.4 | 8% | long_swordx169, longbowx150, vampiric_bladex145 |
| mossgrove | 52.6 [44.8, 60.2] | 156 | 0.69 | 0.29 | 16% | 10% | 3% | 36% | 0.35 | 1.17 | 1.8 | 4.0 | 5% | ruby_crystalx156, long_swordx153, vampiric_bladex130 |
| rictus | 51.2 [43.6, 58.9] | 160 | 0.68 | 0.29 | 32% | 2% | 15% | 15% | 0.72 | 1.25 | 2.1 | 1.9 | 5% | ruby_crystalx157, long_swordx153, vampiric_bladex122 |
| bastion | 48.6 [40.7, 56.7] | 146 | 1.80 | 0.76 | 10% | 4% | 0% | 54% | 0.36 | 1.04 | 1.8 | 4.6 | 13% | ruby_crystalx146, long_swordx132, cloth_armorx124 |
| grivven | 47.9 [39.9, 56.0] | 144 | 1.73 | 0.73 | 32% | 2% | 1% | 54% | 0.38 | 1.28 | 2.3 | 5.0 | 11% | ruby_crystalx144, longbowx141, bootsx133 |
| kestrel | 47.6 [40.3, 55.1] | 170 | 1.77 | 0.75 | 3% | 18% | 0% | 73% | 0.41 | 1.05 | 1.7 | 5.2 | 12% | long_swordx169, longbowx149, vampiric_bladex139 |
| brixa | 47.5 [40.0, 55.2] | 162 | 1.10 | 0.47 | 10% | 4% | 6% | 60% | 0.29 | 1.23 | 2.0 | 3.5 | 7% | long_swordx162, longbowx147, vampiric_bladex140 |
| kaelis | 46.8 [39.1, 54.6] | 156 | 0.97 | 0.41 | 21% | 2% | 2% | 48% | 0.31 | 1.21 | 1.9 | 2.8 | 7% | ruby_crystalx156, long_swordx127, cloth_armorx125 |
| orrin | 46.1 [38.3, 54.0] | 152 | 0.91 | 0.39 | 7% | 55% | 6% | 2% | 0.34 | 1.27 | 2.0 | 3.4 | 6% | long_swordx147, longbowx137, vampiric_bladex126 |
| marrow | 44.7 [37.4, 52.2] | 170 | 1.25 | 0.53 | 3% | 3% | 0% | 62% | 0.36 | 1.12 | 1.8 | 3.3 | 8% | ruby_crystalx170, long_swordx145, cloth_armorx137 |
| lumen | 43.9 [36.5, 51.6] | 164 | 0.60 | 0.25 | 73% | 2% | 0% | 11% | 0.25 | 0.33 | 0.6 | 1.0 | 5% | ruby_crystalx162, longbowx160, bootsx126 |
| vurmak | 41.0 [33.8, 48.6] | 166 | 1.15 | 0.49 | 11% | 2% | 5% | 61% | 0.48 | 1.17 | 1.9 | 3.4 | 8% | ruby_crystalx166, long_swordx133, cloth_armorx112 |
| corvane | 33.6 [26.4, 41.6] | 146 | 0.19 | 0.08 | 64% | 5% | 0% | 6% | 0.23 | 0.79 | 1.3 | 4.2 | 1% | longbowx146, ruby_crystalx145, bootsx130 |
| thornjaw | 32.7 [26.1, 40.2] | 168 | 0.75 | 0.32 | 36% | 2% | 11% | 9% | 0.33 | 1.08 | 1.8 | 1.4 | 6% | ruby_crystalx157, long_swordx151, vampiric_bladex110 |
| vellum | 26.6 [20.3, 34.0] | 158 | 2.58 | 1.09 | 2% | 0% | 0% | 91% | 0.60 | 1.75 | 2.8 | 3.0 | 20% | longbowx149, ionian_charmx120, ruby_crystalx118 |
| noctis | 6.7 [3.7, 11.8] | 150 | 0.65 | 0.28 | 29% | 0% | 41% | 15% | 0.61 | 1.03 | 1.7 | 1.9 | 7% | longbowx134, ruby_crystalx89, ionian_charmx72 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [46.5, 53.5] | 1.24 |
| Jungle | 50.0 [46.5, 53.5] | 1.19 |
| Mid | 50.0 [46.5, 53.5] | 5.82 |
| Support | 50.0 [46.5, 53.5] | 1.79 |
| Top | 50.0 [46.5, 53.5] | 1.93 |

## 5. Games

- length: median 11.0, p10 9, p90 15
- end reasons: {'nexus': 400} (draws 0)
- priority win rate: 48.8% [43.9, 53.6]
- north win rate: 48.8% [43.9, 53.6]
- length histogram: {5: 1, 7: 7, 8: 28, 9: 44, 10: 76, 11: 69, 12: 65, 13: 32, 14: 33, 15: 21, 16: 15, 17: 7, 18: 1, 19: 1}

## 6. Objectives

- takes per game: {'dragon': 1.7575, 'baron': 0.79}
- median round taken: dragon 6, baron 10.0
- win rate when secured: {'dragon': 49.786628733997155, 'baron': 53.48101265822785}
- camp clears per game: {'krugs': 7.6475, 'wolves': 7.2125, 'raptors': 7.635, 'blue_buff': 4.3225, 'red_buff': 4.4775, 'dragon': 1.7575, 'baron': 0.79}

## 7. Structures

- first tower falls: median round 2.0, p10 1, p90 3
- games with at least one tower down: 100.0%
- first-tower win rate: 60.2%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.25 |
| chips_structure | 3.68 |
| chips_wave | 3.60 |
| base | 3.37 |
| champion_kill | 0.46 |
| blue_buff | 0.37 |
| red_buff | 0.22 |

| use | AP |
|---|---|
| shop | 11.32 |
| abilities | 3.35 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.76 | 69.4% | 15.7% | +53.7 |
| cloth_armor | 5 | 1.63 | 71.3% | 33.8% | +37.5 |
| control_ward | 2 | 0.20 | - | 50.0% | - |
| frost_charm | 2 | 0.12 | - | 50.0% | - |
| health_potion | 2 | 1.72 | - | 50.0% | - |
| ionian_charm | 8 | 1.68 | 75.6% | 19.5% | +56.1 |
| long_sword | 6 | 1.97 | 57.0% | 33.8% | +23.2 |
| longbow | 6 | 1.98 | 53.2% | 45.9% | +7.3 |
| ruby_crystal | 4 | 2.00 | 54.5% | 2.0% | +52.5 |
| stopwatch | 3 | 1.83 | - | 50.0% | - |
| swift_tonic | 1 | 1.90 | - | 50.0% | - |
| vampiric_blade | 5 | 1.68 | 66.8% | 31.2% | +35.6 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: quillan** - 11.00 AP/round = 4.66x roster mean
2. **champion win rate: noctis** - WR 6.7% [3.7, 11.8]
3. **economy outlier: sable** - 7.85 AP/round = 3.32x roster mean
4. **champion win rate: quillan** - WR 83.3% [76.7, 88.4]
5. **Median game length 13-18 rounds** - 11.0 [11.0, 11.0]

## 12. Delta vs batch_0007

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -0.9 | -0.50 | no |
| bastion | +0.2 | +0.08 | no |
| bramblehide | +7.0 | +0.18 | no |
| brixa | -11.3 | -0.01 | no |
| corvane | -4.8 | -0.02 | no |
| dax | +0.7 | +0.07 | no |
| grivven | -12.8 | -0.20 | no |
| kaelis | +6.3 | +0.08 | no |
| kestrel | +0.9 | +0.06 | no |
| lumen | +0.5 | +0.04 | no |
| marrow | +0.9 | +0.02 | no |
| mossgrove | +9.3 | +0.08 | no |
| noctis | -1.7 | +0.08 | no |
| orrin | +9.1 | +0.08 | no |
| ossuar | -3.5 | -0.05 | no |
| pallas | +9.7 | +0.41 | no |
| quillan | -5.8 | +0.12 | no |
| rictus | -2.8 | +0.05 | no |
| sable | +6.4 | +0.18 | no |
| sylphine | +7.4 | +0.09 | no |
| thornjaw | -19.1 | -0.03 | yes |
| vellum | -5.9 | -0.12 | no |
| veyra | +2.0 | +0.02 | no |
| vurmak | -6.7 | +0.03 | no |
| wisp | +2.9 | -0.07 | no |

- median length delta: -1.0
- nexus-kill rate delta: +0.5 pts
