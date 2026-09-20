# Sim report batch_0024

## 1. Header

| field | value |
|---|---|
| rules | 1.2.0 |
| roster | 1.3.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 2401 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 481.4s |
| engine tests | not run |
| generated | 2026-09-20 22:11:56 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 5 FAIL / 20 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 47/56 abilities outside the band; roster mean 18.7%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 49.3% [41.4, 57.3] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 14.5 [14.0, 15.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 92.7% [87.3, 95.9] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, wisp (roster mean 2.24 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 47.3% [39.5, 55.3] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 85.5 [74.7, 92.2] | 62 | 11.01 | 4.92 | 0% | 98% | 0% | 0% | 0.31 | 0.23 | 0.4 | 0.0 | 56% | bootsx62, cloth_armorx62, ionian_charmx62 |
| wisp | 72.7 [61.0, 82.0] | 66 | 6.58 | 2.94 | 4% | 83% | 2% | 4% | 0.15 | 0.41 | 0.8 | 0.0 | 37% | bootsx66, longbowx66, ruby_crystalx66 |
| bramblehide | 66.7 [52.5, 78.3] | 48 | 2.17 | 0.97 | 3% | 31% | 1% | 48% | 0.17 | 0.10 | 0.2 | 5.2 | 16% | long_swordx48, ruby_crystalx48, bootsx47 |
| quillan | 66.7 [53.4, 77.8] | 54 | 8.09 | 3.61 | 0% | 0% | 1% | 94% | 0.15 | 0.50 | 1.0 | 2.6 | 44% | ionian_charmx54, longbowx54, ruby_crystalx54 |
| veyra | 64.3 [53.6, 73.7] | 84 | 1.11 | 0.50 | 4% | 55% | 12% | 6% | 0.19 | 0.21 | 0.5 | 1.1 | 7% | long_swordx82, longbowx82, vampiric_bladex79 |
| pallas | 62.1 [50.1, 72.9] | 66 | 2.75 | 1.23 | 28% | 2% | 2% | 57% | 0.18 | 0.47 | 1.1 | 3.5 | 18% | bootsx66, ruby_crystalx66, longbowx65 |
| kaelis | 62.0 [48.2, 74.1] | 50 | 0.76 | 0.34 | 43% | 9% | 8% | 5% | 0.10 | 0.12 | 0.2 | 0.4 | 5% | ruby_crystalx50, cloth_armorx49, long_swordx48 |
| bastion | 61.3 [48.8, 72.4] | 62 | 1.18 | 0.53 | 65% | 5% | 1% | 1% | 0.24 | 0.11 | 0.3 | 0.2 | 8% | ruby_crystalx62, cloth_armorx61, long_swordx59 |
| sable | 59.6 [46.1, 71.8] | 52 | 5.95 | 2.66 | 3% | 81% | 0% | 9% | 0.13 | 0.54 | 1.2 | 3.1 | 39% | longbowx52, ionian_charmx51, ruby_crystalx50 |
| ossuar | 58.6 [46.9, 69.4] | 70 | 2.07 | 0.92 | 6% | 7% | 6% | 58% | 0.10 | 0.06 | 0.1 | 4.7 | 15% | ruby_crystalx70, long_swordx67, cloth_armorx66 |
| sylphine | 56.8 [42.2, 70.3] | 44 | 0.57 | 0.26 | 16% | 3% | 13% | 28% | 0.18 | 0.05 | 0.1 | 1.2 | 4% | ruby_crystalx43, long_swordx42, vampiric_bladex37 |
| thornjaw | 50.0 [38.6, 61.4] | 70 | 0.80 | 0.36 | 22% | 31% | 2% | 2% | 0.31 | 0.14 | 0.3 | 0.2 | 6% | ruby_crystalx69, long_swordx67, vampiric_bladex64 |
| corvane | 48.0 [34.8, 61.5] | 50 | 0.20 | 0.09 | 21% | 4% | 25% | 5% | 0.14 | 0.40 | 0.8 | 4.3 | 2% | longbowx50, ruby_crystalx50, bootsx46 |
| brixa | 46.8 [34.9, 59.0] | 62 | 0.90 | 0.40 | 17% | 29% | 7% | 9% | 0.16 | 0.23 | 0.5 | 0.8 | 7% | long_swordx62, vampiric_bladex58, longbowx54 |
| mossgrove | 46.8 [34.9, 59.0] | 62 | 0.63 | 0.28 | 30% | 19% | 1% | 15% | 0.10 | 0.19 | 0.5 | 4.3 | 5% | long_swordx62, ruby_crystalx61, vampiric_bladex59 |
| orrin | 46.6 [34.3, 59.2] | 58 | 0.62 | 0.28 | 9% | 16% | 21% | 11% | 0.14 | 0.34 | 0.7 | 2.2 | 5% | long_swordx55, longbowx53, vampiric_bladex51 |
| kestrel | 45.5 [31.7, 59.9] | 44 | 1.48 | 0.66 | 12% | 47% | 10% | 18% | 0.30 | 0.23 | 0.5 | 2.7 | 12% | long_swordx43, longbowx41, vampiric_bladex40 |
| dax | 38.5 [26.5, 52.0] | 52 | 0.93 | 0.41 | 41% | 17% | 3% | 13% | 0.17 | 0.15 | 0.3 | 1.4 | 7% | long_swordx52, longbowx50, vampiric_bladex50 |
| rictus | 38.2 [28.1, 49.4] | 76 | 0.66 | 0.30 | 10% | 39% | 11% | 7% | 0.34 | 0.28 | 0.6 | 1.6 | 5% | ruby_crystalx75, long_swordx72, vampiric_bladex59 |
| grivven | 37.9 [26.6, 50.8] | 58 | 2.90 | 1.30 | 5% | 6% | 0% | 66% | 0.07 | 0.38 | 0.9 | 7.3 | 22% | longbowx58, ruby_crystalx58, bootsx57 |
| vurmak | 33.9 [22.9, 47.0] | 56 | 1.04 | 0.46 | 42% | 13% | 2% | 16% | 0.18 | 0.18 | 0.4 | 1.6 | 8% | ruby_crystalx56, long_swordx50, cloth_armorx38 |
| marrow | 33.9 [23.3, 46.3] | 62 | 0.51 | 0.23 | 30% | 3% | 15% | 9% | 0.24 | 0.10 | 0.3 | 1.5 | 4% | ruby_crystalx62, cloth_armorx53, long_swordx51 |
| lumen | 25.0 [15.8, 37.2] | 60 | 0.53 | 0.24 | 58% | 5% | 1% | 3% | 0.22 | 0.17 | 0.3 | 0.5 | 5% | longbowx59, ruby_crystalx58, bootsx56 |
| noctis | 24.3 [15.8, 35.5] | 70 | 0.67 | 0.30 | 31% | 15% | 15% | 5% | 0.26 | 0.44 | 0.9 | 2.0 | 7% | longbowx66, ruby_crystalx59, ionian_charmx50 |
| vellum | 21.0 [12.7, 32.6] | 62 | 1.82 | 0.81 | 6% | 2% | 25% | 52% | 0.16 | 0.60 | 1.3 | 2.7 | 17% | longbowx59, ruby_crystalx51, ionian_charmx46 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 0.99 |
| Jungle | 50.0 [44.4, 55.6] | 0.92 |
| Mid | 50.0 [44.4, 55.6] | 5.30 |
| Support | 50.0 [44.4, 55.6] | 2.75 |
| Top | 50.0 [44.4, 55.6] | 1.15 |

## 5. Games

- length: median 14.5, p10 11, p90 20
- end reasons: {'nexus': 139, 'round_limit_hp': 2, 'round_limit_towers': 9} (draws 0)
- priority win rate: 49.3% [41.4, 57.3]
- north win rate: 47.3% [39.5, 55.3]
- length histogram: {9: 3, 10: 6, 11: 21, 12: 9, 13: 16, 14: 20, 15: 17, 16: 17, 17: 10, 18: 7, 19: 6, 20: 18}

## 6. Objectives

- takes per game: {'dragon': 1.6733333333333333, 'baron': 0.7733333333333333}
- median round taken: dragon 9, baron 12.0
- win rate when secured: {'dragon': 45.81673306772908, 'baron': 44.827586206896555}
- camp clears per game: {'wolves': 6.366666666666666, 'raptors': 6.5, 'red_buff': 4.12, 'blue_buff': 4.16, 'krugs': 6.62, 'dragon': 1.6733333333333333, 'baron': 0.7733333333333333}

## 7. Structures

- first tower falls: median round 6.0, p10 4, p90 8
- games with at least one tower down: 100.0%
- first-tower win rate: 86.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.08 |
| chips_wave | 3.60 |
| base | 3.33 |
| chips_structure | 3.05 |
| blue_buff | 0.28 |
| red_buff | 0.13 |
| champion_kill | 0.08 |

| use | AP |
|---|---|
| shop | 10.57 |
| abilities | 2.12 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.94 | 63.2% | 4.7% | +58.4 |
| cloth_armor | 5 | 1.78 | 67.2% | 27.4% | +39.8 |
| control_ward | 2 | 0.93 | - | 50.0% | - |
| frost_charm | 2 | 0.87 | - | 50.0% | - |
| health_potion | 2 | 1.93 | - | 50.0% | - |
| ionian_charm | 8 | 1.75 | 69.2% | 6.7% | +62.5 |
| long_sword | 6 | 1.97 | 55.1% | 36.6% | +18.5 |
| longbow | 6 | 1.99 | 51.7% | 47.7% | +4.0 |
| ruby_crystal | 4 | 2.00 | 52.7% | 1.2% | +51.5 |
| stopwatch | 3 | 1.96 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.89 | 61.6% | 29.9% | +31.7 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 45.27 per game
- that is 46.2% of all ability uses


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 11.01 AP/round = 4.92x roster mean
2. **economy outlier: quillan** - 8.09 AP/round = 3.61x roster mean
3. **champion win rate: ashwyn** - WR 85.5% [74.7, 92.2]
4. **champion win rate: vellum** - WR 21.0% [12.7, 32.6]
5. **economy outlier: wisp** - 6.58 AP/round = 2.94x roster mean

## 12. Delta vs batch_0023

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +1.1 | +0.10 | no |
| bastion | +11.3 | -0.06 | no |
| bramblehide | -2.4 | +0.11 | no |
| brixa | +5.1 | +0.04 | no |
| corvane | +10.5 | +0.02 | no |
| dax | +1.7 | +0.05 | no |
| grivven | -18.7 | -0.05 | no |
| kaelis | +23.3 | +0.08 | no |
| kestrel | -30.9 | -0.02 | yes |
| lumen | -7.8 | -0.02 | no |
| marrow | -20.6 | -0.09 | no |
| mossgrove | -4.6 | -0.04 | no |
| noctis | +9.3 | -0.01 | no |
| orrin | -2.6 | -0.04 | no |
| ossuar | +0.5 | +0.05 | no |
| pallas | +14.7 | +0.24 | no |
| quillan | +7.7 | -0.19 | no |
| rictus | -0.3 | +0.02 | no |
| sable | -3.6 | -0.35 | no |
| sylphine | +16.1 | +0.03 | no |
| thornjaw | -1.8 | +0.00 | no |
| vellum | -9.8 | -0.06 | no |
| veyra | +15.1 | +0.07 | no |
| vurmak | -15.3 | -0.10 | no |
| wisp | -4.9 | -0.43 | no |

- median length delta: -0.5
- nexus-kill rate delta: +4.0 pts
