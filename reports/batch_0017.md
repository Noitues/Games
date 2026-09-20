# Sim report batch_0017

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
| runtime | 430.8s |
| engine tests | not run |
| generated | 2026-09-20 17:21:52 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 10 FAIL / 15 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 52/56 abilities outside the band; roster mean 18.0%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 52.7% [44.7, 60.5] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 12.0 [12.0, 13.0] | **INCONCLUSIVE** |
| >=95% of games end by Nexus kill before round 20 | 98.7% [95.3, 99.6] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.23 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.0% [40.2, 55.9] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 90.6 [81.0, 95.6] | 64 | 9.28 | 4.16 | 2% | 86% | 0% | 5% | 0.25 | 0.25 | 0.4 | 0.0 | 49% | bootsx64, ionian_charmx64, long_swordx64 |
| quillan | 75.0 [61.2, 85.1] | 48 | 7.59 | 3.40 | 4% | 2% | 1% | 84% | 0.19 | 0.25 | 0.5 | 2.4 | 44% | ionian_charmx48, longbowx48, ruby_crystalx47 |
| kestrel | 74.1 [61.6, 83.7] | 58 | 1.61 | 0.72 | 42% | 19% | 5% | 18% | 0.19 | 0.03 | 0.1 | 2.7 | 10% | long_swordx58, longbowx57, vampiric_bladex57 |
| wisp | 73.3 [61.0, 82.9] | 60 | 5.23 | 2.35 | 13% | 60% | 2% | 10% | 0.15 | 0.15 | 0.2 | 0.0 | 31% | longbowx60, ruby_crystalx60, bootsx56 |
| pallas | 70.0 [56.2, 80.9] | 50 | 4.24 | 1.90 | 9% | 2% | 1% | 74% | 0.08 | 0.12 | 0.2 | 3.9 | 26% | longbowx50, ruby_crystalx50, bootsx48 |
| ossuar | 66.7 [55.2, 76.5] | 72 | 1.67 | 0.75 | 16% | 11% | 3% | 34% | 0.17 | 0.04 | 0.1 | 2.9 | 11% | ruby_crystalx72, long_swordx70, cloth_armorx66 |
| veyra | 55.0 [42.5, 66.9] | 60 | 0.91 | 0.41 | 11% | 35% | 8% | 13% | 0.05 | 0.25 | 0.5 | 2.2 | 7% | long_swordx59, longbowx55, vampiric_bladex48 |
| sylphine | 53.1 [41.1, 64.8] | 64 | 0.74 | 0.33 | 12% | 3% | 9% | 19% | 0.17 | 0.05 | 0.1 | 0.9 | 5% | long_swordx63, ruby_crystalx63, vampiric_bladex55 |
| bramblehide | 51.9 [38.9, 64.6] | 54 | 1.90 | 0.85 | 3% | 21% | 3% | 34% | 0.11 | 0.13 | 0.2 | 3.8 | 14% | long_swordx54, ruby_crystalx54, vampiric_bladex52 |
| bastion | 51.8 [39.0, 64.3] | 56 | 1.25 | 0.56 | 43% | 6% | 3% | 6% | 0.07 | 0.05 | 0.1 | 1.3 | 9% | ruby_crystalx56, cloth_armorx53, long_swordx52 |
| thornjaw | 51.7 [39.2, 64.1] | 58 | 0.86 | 0.39 | 14% | 19% | 7% | 3% | 0.10 | 0.10 | 0.3 | 0.7 | 6% | ruby_crystalx57, long_swordx55, vampiric_bladex46 |
| mossgrove | 51.5 [39.8, 62.9] | 68 | 0.74 | 0.33 | 24% | 14% | 3% | 10% | 0.13 | 0.07 | 0.2 | 3.3 | 5% | long_swordx68, ruby_crystalx67, vampiric_bladex61 |
| dax | 50.0 [38.7, 61.3] | 72 | 1.05 | 0.47 | 19% | 30% | 4% | 15% | 0.01 | 0.18 | 0.3 | 1.7 | 8% | long_swordx72, longbowx67, vampiric_bladex65 |
| lumen | 50.0 [37.1, 62.9] | 54 | 0.53 | 0.24 | 44% | 4% | 2% | 6% | 0.15 | 0.17 | 0.4 | 0.9 | 4% | ruby_crystalx53, longbowx52, bootsx50 |
| marrow | 45.8 [34.8, 57.3] | 72 | 1.85 | 0.83 | 14% | 4% | 8% | 30% | 0.12 | 0.08 | 0.1 | 0.7 | 13% | ruby_crystalx72, long_swordx68, cloth_armorx64 |
| vurmak | 45.3 [33.7, 57.4] | 64 | 1.12 | 0.50 | 20% | 7% | 4% | 37% | 0.19 | 0.17 | 0.4 | 3.4 | 8% | ruby_crystalx64, long_swordx56, cloth_armorx49 |
| sable | 43.1 [31.2, 55.9] | 58 | 5.52 | 2.48 | 6% | 48% | 1% | 31% | 0.09 | 0.21 | 0.4 | 2.8 | 36% | longbowx57, ionian_charmx55, ruby_crystalx54 |
| rictus | 41.1 [29.2, 54.1] | 56 | 0.83 | 0.37 | 20% | 21% | 19% | 3% | 0.21 | 0.27 | 0.4 | 1.7 | 6% | long_swordx55, ruby_crystalx53, vampiric_bladex48 |
| grivven | 40.8 [30.4, 52.0] | 76 | 2.47 | 1.11 | 16% | 5% | 1% | 51% | 0.04 | 0.14 | 0.3 | 6.3 | 18% | longbowx76, ruby_crystalx76, bootsx71 |
| brixa | 38.5 [26.5, 52.0] | 52 | 0.98 | 0.44 | 26% | 12% | 11% | 9% | 0.10 | 0.21 | 0.3 | 1.2 | 7% | long_swordx52, longbowx49, vampiric_bladex48 |
| orrin | 31.0 [20.6, 43.8] | 58 | 0.74 | 0.33 | 16% | 19% | 10% | 5% | 0.02 | 0.33 | 0.7 | 2.1 | 6% | long_swordx58, longbowx52, vampiric_bladex48 |
| kaelis | 30.6 [18.0, 46.9] | 36 | 0.72 | 0.32 | 21% | 16% | 7% | 10% | 0.06 | 0.14 | 0.3 | 0.9 | 6% | ruby_crystalx36, long_swordx34, cloth_armorx30 |
| noctis | 23.9 [13.9, 37.9] | 46 | 1.06 | 0.47 | 47% | 3% | 18% | 3% | 0.13 | 0.28 | 0.6 | 0.7 | 11% | longbowx44, ruby_crystalx35, ionian_charmx31 |
| vellum | 23.8 [16.0, 33.9] | 84 | 2.55 | 1.15 | 12% | 0% | 8% | 65% | 0.06 | 0.26 | 0.5 | 3.1 | 22% | longbowx81, ionian_charmx71, ruby_crystalx67 |
| corvane | 21.7 [13.1, 33.6] | 60 | 0.28 | 0.13 | 31% | 5% | 11% | 3% | 0.08 | 0.30 | 0.6 | 4.0 | 3% | ruby_crystalx60, longbowx59, bootsx55 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 1.06 |
| Jungle | 50.0 [44.4, 55.6] | 0.99 |
| Mid | 50.0 [44.4, 55.6] | 5.14 |
| Support | 50.0 [44.4, 55.6] | 2.53 |
| Top | 50.0 [44.4, 55.6] | 1.40 |

## 5. Games

- length: median 12.0, p10 9, p90 17
- end reasons: {'nexus': 148, 'round_limit_towers': 2} (draws 0)
- priority win rate: 52.7% [44.7, 60.5]
- north win rate: 48.0% [40.2, 55.9]
- length histogram: {7: 1, 8: 2, 9: 16, 10: 14, 11: 22, 12: 30, 13: 17, 14: 15, 15: 7, 16: 9, 17: 6, 18: 7, 19: 2, 20: 2}

## 6. Objectives

- takes per game: {'dragon': 1.3333333333333333, 'baron': 0.47333333333333333}
- median round taken: dragon 7.0, baron 11
- win rate when secured: {'dragon': 52.5, 'baron': 42.25352112676056}
- camp clears per game: {'krugs': 5.533333333333333, 'wolves': 5.426666666666667, 'raptors': 5.54, 'red_buff': 3.4066666666666667, 'blue_buff': 3.38, 'dragon': 1.3333333333333333, 'baron': 0.47333333333333333}

## 7. Structures

- first tower falls: median round 4.0, p10 3, p90 6
- games with at least one tower down: 100.0%
- first-tower win rate: 73.3%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.00 |
| chips_wave | 3.53 |
| chips_structure | 3.28 |
| base | 3.26 |
| blue_buff | 0.26 |
| red_buff | 0.15 |
| champion_kill | 0.06 |

| use | AP |
|---|---|
| shop | 11.11 |
| abilities | 2.23 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.87 | 66.5% | 13.7% | +52.8 |
| cloth_armor | 5 | 1.75 | 68.8% | 32.5% | +36.3 |
| control_ward | 2 | 0.45 | - | 50.0% | - |
| frost_charm | 2 | 0.35 | - | 50.0% | - |
| health_potion | 2 | 1.84 | - | 50.0% | - |
| ionian_charm | 8 | 1.79 | 70.7% | 15.6% | +55.0 |
| long_sword | 6 | 1.99 | 54.7% | 37.6% | +17.1 |
| longbow | 6 | 1.98 | 51.7% | 47.7% | +4.0 |
| ruby_crystal | 4 | 2.00 | 53.7% | 1.9% | +51.8 |
| stopwatch | 3 | 1.89 | - | 50.0% | - |
| swift_tonic | 1 | 1.97 | - | 50.0% | - |
| vampiric_blade | 5 | 1.81 | 62.5% | 32.4% | +30.1 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 55.24 per game
- that is 66.6% of all ability uses


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 9.28 AP/round = 4.16x roster mean
2. **champion win rate: ashwyn** - WR 90.6% [81.0, 95.6]
3. **economy outlier: quillan** - 7.59 AP/round = 3.40x roster mean
4. **champion win rate: corvane** - WR 21.7% [13.1, 33.6]
5. **champion win rate: vellum** - WR 23.8% [16.0, 33.9]

## 12. Delta vs batch_0016

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +3.1 | -0.23 | no |
| bastion | +0.0 | -0.27 | no |
| bramblehide | +1.9 | -0.09 | no |
| brixa | +3.8 | -0.15 | no |
| corvane | +0.0 | -0.08 | no |
| dax | -2.8 | -0.16 | no |
| grivven | +9.2 | -0.24 | no |
| kaelis | +0.0 | -0.14 | no |
| kestrel | +5.2 | -0.25 | no |
| lumen | +0.0 | -0.15 | no |
| marrow | -2.8 | +0.27 | no |
| mossgrove | +4.4 | -0.04 | no |
| noctis | -2.2 | -0.20 | no |
| orrin | -5.2 | -0.12 | no |
| ossuar | +8.3 | -0.27 | no |
| pallas | -2.0 | -0.35 | no |
| quillan | +12.5 | -0.22 | no |
| rictus | -12.5 | -0.20 | no |
| sable | +5.2 | -0.31 | no |
| sylphine | +1.6 | -0.05 | no |
| thornjaw | +3.4 | -0.11 | no |
| vellum | -11.9 | -0.05 | no |
| veyra | +0.0 | -0.08 | no |
| vurmak | -6.2 | -0.15 | no |
| wisp | -10.0 | -0.97 | no |

- median length delta: +1.0
- nexus-kill rate delta: +1.3 pts
