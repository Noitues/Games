# Sim report batch_0025

## 1. Header

| field | value |
|---|---|
| rules | 1.2.0 |
| roster | 1.3.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 2402 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 456.9s |
| engine tests | not run |
| generated | 2026-09-20 22:19:33 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 5 FAIL / 20 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 48/56 abilities outside the band; roster mean 18.6%; 6 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 48.7% [40.8, 56.6] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 13.0 [12.5, 14.0] | **INCONCLUSIVE** |
| >=95% of games end by Nexus kill before round 20 | 91.3% [85.7, 94.9] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, wisp (roster mean 2.23 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 46.7% [38.9, 54.6] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 86.5 [74.7, 93.3] | 52 | 10.62 | 4.77 | 0% | 97% | 0% | 1% | 0.33 | 0.29 | 0.5 | 0.0 | 53% | bootsx52, ionian_charmx52, long_swordx52 |
| wisp | 80.0 [68.2, 88.2] | 60 | 6.24 | 2.80 | 3% | 82% | 1% | 5% | 0.25 | 0.47 | 0.8 | 0.0 | 36% | longbowx60, ruby_crystalx60, bootsx59 |
| quillan | 67.3 [53.8, 78.5] | 52 | 8.50 | 3.82 | 0% | 1% | 2% | 93% | 0.25 | 0.38 | 0.7 | 2.8 | 49% | ionian_charmx52, longbowx52, ruby_crystalx52 |
| sable | 64.3 [51.2, 75.5] | 56 | 6.36 | 2.86 | 2% | 81% | 0% | 9% | 0.12 | 0.30 | 0.6 | 3.1 | 40% | ionian_charmx56, longbowx56, ruby_crystalx54 |
| mossgrove | 63.2 [51.4, 73.7] | 68 | 0.67 | 0.30 | 31% | 21% | 1% | 15% | 0.10 | 0.09 | 0.1 | 4.2 | 5% | long_swordx68, ruby_crystalx68, vampiric_bladex59 |
| bramblehide | 61.8 [49.9, 72.4] | 68 | 1.95 | 0.88 | 2% | 38% | 2% | 40% | 0.07 | 0.16 | 0.3 | 4.8 | 15% | long_swordx68, ruby_crystalx68, vampiric_bladex61 |
| kestrel | 61.3 [48.8, 72.4] | 62 | 1.49 | 0.67 | 11% | 51% | 10% | 17% | 0.16 | 0.16 | 0.4 | 2.3 | 10% | long_swordx62, longbowx62, vampiric_bladex59 |
| ossuar | 58.9 [45.9, 70.8] | 56 | 2.05 | 0.92 | 5% | 6% | 7% | 59% | 0.20 | 0.02 | 0.1 | 4.8 | 15% | long_swordx56, ruby_crystalx56, cloth_armorx52 |
| brixa | 56.5 [44.1, 68.1] | 62 | 0.91 | 0.41 | 18% | 33% | 7% | 7% | 0.18 | 0.19 | 0.4 | 0.8 | 7% | long_swordx61, vampiric_bladex59, longbowx58 |
| pallas | 55.7 [44.1, 66.8] | 70 | 2.66 | 1.19 | 26% | 2% | 2% | 56% | 0.24 | 0.27 | 0.6 | 3.4 | 19% | longbowx70, ruby_crystalx70, bootsx67 |
| vurmak | 51.7 [39.3, 63.8] | 60 | 1.07 | 0.48 | 43% | 12% | 1% | 17% | 0.35 | 0.18 | 0.4 | 1.6 | 8% | ruby_crystalx60, long_swordx52, cloth_armorx49 |
| thornjaw | 50.0 [35.5, 64.5] | 42 | 0.76 | 0.34 | 24% | 32% | 4% | 2% | 0.24 | 0.24 | 0.5 | 0.4 | 6% | ruby_crystalx42, long_swordx41, vampiric_bladex36 |
| veyra | 50.0 [38.1, 61.9] | 64 | 1.07 | 0.48 | 4% | 54% | 11% | 4% | 0.06 | 0.23 | 0.5 | 0.8 | 8% | long_swordx58, longbowx52, vampiric_bladex49 |
| bastion | 48.4 [36.4, 60.6] | 62 | 1.26 | 0.56 | 68% | 4% | 1% | 1% | 0.27 | 0.11 | 0.3 | 0.2 | 11% | ruby_crystalx62, long_swordx61, cloth_armorx57 |
| sylphine | 48.3 [35.9, 60.8] | 58 | 0.53 | 0.24 | 17% | 3% | 14% | 26% | 0.07 | 0.05 | 0.1 | 1.5 | 4% | ruby_crystalx58, long_swordx54, vampiric_bladex46 |
| kaelis | 48.1 [35.4, 61.1] | 54 | 0.72 | 0.32 | 40% | 11% | 5% | 6% | 0.15 | 0.09 | 0.1 | 0.5 | 6% | ruby_crystalx54, long_swordx50, cloth_armorx48 |
| marrow | 44.1 [32.9, 55.9] | 68 | 0.59 | 0.26 | 29% | 3% | 16% | 9% | 0.22 | 0.06 | 0.1 | 1.5 | 4% | ruby_crystalx68, long_swordx60, cloth_armorx57 |
| dax | 43.3 [31.6, 55.9] | 60 | 0.90 | 0.40 | 43% | 15% | 2% | 10% | 0.20 | 0.20 | 0.4 | 1.1 | 7% | long_swordx60, longbowx56, vampiric_bladex54 |
| grivven | 41.4 [29.6, 54.2] | 58 | 3.04 | 1.37 | 5% | 9% | 1% | 64% | 0.07 | 0.24 | 0.6 | 7.6 | 23% | ruby_crystalx58, bootsx57, longbowx57 |
| corvane | 37.9 [26.6, 50.8] | 58 | 0.17 | 0.08 | 17% | 4% | 24% | 7% | 0.17 | 0.38 | 0.7 | 4.1 | 2% | ruby_crystalx58, longbowx57, bootsx53 |
| vellum | 37.5 [26.0, 50.6] | 56 | 1.77 | 0.79 | 5% | 2% | 26% | 54% | 0.12 | 0.45 | 0.9 | 2.6 | 17% | longbowx51, ionian_charmx42, ruby_crystalx42 |
| orrin | 36.5 [24.8, 50.1] | 52 | 0.58 | 0.26 | 7% | 18% | 23% | 12% | 0.04 | 0.37 | 0.8 | 2.7 | 5% | long_swordx48, longbowx46, vampiric_bladex43 |
| lumen | 31.5 [20.7, 44.7] | 54 | 0.54 | 0.24 | 59% | 3% | 1% | 4% | 0.04 | 0.22 | 0.5 | 0.5 | 6% | ruby_crystalx53, longbowx52, bootsx48 |
| rictus | 25.0 [16.0, 36.8] | 64 | 0.65 | 0.29 | 10% | 39% | 9% | 6% | 0.12 | 0.39 | 0.7 | 1.4 | 6% | ruby_crystalx63, long_swordx58, vampiric_bladex47 |
| noctis | 15.5 [9.3, 24.7] | 84 | 0.61 | 0.27 | 29% | 14% | 14% | 8% | 0.14 | 0.58 | 1.3 | 2.4 | 7% | longbowx77, ruby_crystalx66, ionian_charmx62 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 1.00 |
| Jungle | 50.0 [44.4, 55.6] | 0.94 |
| Mid | 50.0 [44.4, 55.6] | 5.00 |
| Support | 50.0 [44.4, 55.6] | 2.59 |
| Top | 50.0 [44.4, 55.6] | 1.12 |

## 5. Games

- length: median 13.0, p10 10, p90 19
- end reasons: {'nexus': 137, 'round_limit_hp': 3, 'round_limit_towers': 10} (draws 0)
- priority win rate: 48.7% [40.8, 56.6]
- north win rate: 46.7% [38.9, 54.6]
- length histogram: {7: 1, 8: 1, 9: 3, 10: 13, 11: 19, 12: 27, 13: 18, 14: 11, 15: 9, 16: 6, 17: 14, 18: 5, 19: 9, 20: 14}

## 6. Objectives

- takes per game: {'dragon': 1.4666666666666666, 'baron': 0.6066666666666667}
- median round taken: dragon 8.0, baron 11
- win rate when secured: {'dragon': 34.09090909090909, 'baron': 52.747252747252745}
- camp clears per game: {'wolves': 5.833333333333333, 'krugs': 5.973333333333334, 'raptors': 6.1, 'blue_buff': 3.7066666666666666, 'red_buff': 3.7533333333333334, 'dragon': 1.4666666666666666, 'baron': 0.6066666666666667}

## 7. Structures

- first tower falls: median round 5.0, p10 4, p90 8
- games with at least one tower down: 100.0%
- first-tower win rate: 86.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.92 |
| chips_wave | 3.41 |
| base | 3.28 |
| chips_structure | 2.89 |
| blue_buff | 0.26 |
| red_buff | 0.14 |
| champion_kill | 0.08 |

| use | AP |
|---|---|
| shop | 10.53 |
| abilities | 2.08 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.89 | 66.7% | 6.3% | +60.5 |
| cloth_armor | 5 | 1.75 | 68.5% | 28.7% | +39.8 |
| control_ward | 2 | 0.72 | - | 50.0% | - |
| frost_charm | 2 | 0.60 | - | 50.0% | - |
| health_potion | 2 | 1.88 | - | 50.0% | - |
| ionian_charm | 8 | 1.76 | 70.6% | 11.0% | +59.6 |
| long_sword | 6 | 1.95 | 55.5% | 35.9% | +19.6 |
| longbow | 6 | 1.97 | 52.4% | 46.7% | +5.7 |
| ruby_crystal | 4 | 2.00 | 53.4% | 0.0% | +53.4 |
| stopwatch | 3 | 1.89 | - | 50.0% | - |
| swift_tonic | 1 | 1.97 | - | 50.0% | - |
| vampiric_blade | 5 | 1.79 | 63.4% | 30.7% | +32.7 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 42.08 per game
- that is 46.2% of all ability uses


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 10.62 AP/round = 4.77x roster mean
2. **economy outlier: quillan** - 8.50 AP/round = 3.82x roster mean
3. **champion win rate: ashwyn** - WR 86.5% [74.7, 93.3]
4. **champion win rate: noctis** - WR 15.5% [9.3, 24.7]
5. **champion win rate: wisp** - WR 80.0% [68.2, 88.2]

## 12. Delta vs batch_0023

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +2.2 | -0.29 | no |
| bastion | -1.6 | +0.01 | no |
| bramblehide | -7.3 | -0.11 | no |
| brixa | +14.8 | +0.05 | no |
| corvane | +0.4 | -0.01 | no |
| dax | +6.6 | +0.02 | no |
| grivven | -15.3 | +0.09 | no |
| kaelis | +9.4 | +0.04 | no |
| kestrel | -15.1 | -0.01 | no |
| lumen | -1.3 | -0.01 | no |
| marrow | -10.3 | -0.02 | no |
| mossgrove | +11.8 | -0.00 | no |
| noctis | +0.5 | -0.08 | no |
| orrin | -12.7 | -0.09 | no |
| ossuar | +0.9 | +0.02 | no |
| pallas | +8.3 | +0.15 | no |
| quillan | +8.3 | +0.22 | no |
| rictus | -13.5 | +0.00 | no |
| sable | +1.1 | +0.06 | no |
| sylphine | +7.5 | -0.02 | no |
| thornjaw | -1.8 | -0.04 | no |
| vellum | +6.7 | -0.12 | no |
| veyra | +0.8 | +0.03 | no |
| vurmak | +2.4 | -0.07 | no |
| wisp | +2.4 | -0.76 | no |

- median length delta: -2.0
- nexus-kill rate delta: +2.7 pts
