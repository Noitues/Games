# Sim report batch_0034

## 1. Header

| field | value |
|---|---|
| rules | 1.5.0 |
| roster | 1.5.0 |
| ai | 1.2.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 120 |
| seed | 3401 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 4535.3s |
| engine tests | not run |
| generated | 2026-09-23 02:39:33 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 6 FAIL / 19 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 50/59 abilities outside the band; roster mean 20.9%; 10 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 55.0% [46.1, 63.6] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 16.0 [15.0, 16.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 98.3% [94.1, 99.5] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.51 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.3% [39.6, 57.2] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 84.0 [71.5, 91.7] | 50 | 5.99 | 2.38 | 2% | 82% | 0% | 12% | 0.10 | 0.24 | 0.4 | 0.0 | 31% | bootsx50, cloth_armorx50, ionian_charmx50 |
| ashwyn | 75.0 [61.8, 84.8] | 52 | 5.65 | 2.25 | 4% | 75% | 0% | 16% | 0.04 | 0.46 | 0.9 | 0.0 | 32% | ionian_charmx52, long_swordx52, longbowx52 |
| pallas | 65.0 [49.5, 77.9] | 40 | 4.49 | 1.79 | 3% | 0% | 0% | 92% | 0.07 | 0.42 | 0.7 | 4.7 | 25% | bootsx40, cloth_armorx40, ionian_charmx40 |
| sable | 64.3 [49.2, 77.0] | 42 | 6.40 | 2.54 | 1% | 55% | 0% | 37% | 0.10 | 0.10 | 0.1 | 1.1 | 34% | bootsx42, ionian_charmx42, long_swordx42 |
| sylphine | 64.3 [51.2, 75.5] | 56 | 1.44 | 0.57 | 13% | 2% | 0% | 11% | 0.23 | 0.07 | 0.1 | 0.0 | 9% | long_swordx56, ruby_crystalx56, vampiric_bladex56 |
| vurmak | 61.8 [45.0, 76.1] | 34 | 1.61 | 0.64 | 16% | 3% | 0% | 55% | 0.21 | 0.24 | 0.4 | 4.4 | 10% | cloth_armorx34, long_swordx34, ruby_crystalx34 |
| grivven | 61.1 [47.8, 73.0] | 54 | 2.73 | 1.09 | 4% | 0% | 0% | 73% | 0.00 | 0.19 | 0.5 | 8.4 | 17% | bootsx54, longbowx54, ruby_crystalx54 |
| bastion | 59.4 [47.1, 70.5] | 64 | 2.43 | 0.97 | 90% | 0% | 0% | 3% | 0.23 | 0.12 | 0.2 | 0.7 | 15% | cloth_armorx64, long_swordx64, ruby_crystalx64 |
| marrow | 56.5 [42.2, 69.8] | 46 | 2.74 | 1.09 | 8% | 0% | 0% | 46% | 0.09 | 0.15 | 0.3 | 0.0 | 17% | cloth_armorx46, long_swordx46, ruby_crystalx46 |
| dax | 53.4 [40.8, 65.7] | 58 | 1.55 | 0.62 | 8% | 45% | 1% | 13% | 0.19 | 0.12 | 0.2 | 1.3 | 10% | long_swordx58, longbowx58, vampiric_bladex58 |
| kestrel | 52.6 [37.3, 67.5] | 38 | 1.94 | 0.77 | 63% | 9% | 0% | 21% | 0.13 | 0.16 | 0.3 | 3.6 | 13% | long_swordx38, longbowx38, ruby_crystalx38 |
| brixa | 52.0 [38.5, 65.2] | 50 | 1.56 | 0.62 | 41% | 3% | 7% | 1% | 0.14 | 0.30 | 0.6 | 0.5 | 10% | long_swordx50, longbowx50, ruby_crystalx50 |
| orrin | 50.0 [35.5, 64.5] | 42 | 1.80 | 0.71 | 8% | 38% | 0% | 1% | 0.17 | 0.21 | 0.4 | 0.1 | 11% | long_swordx42, longbowx42, ruby_crystalx42 |
| bramblehide | 47.9 [34.5, 61.7] | 48 | 2.14 | 0.85 | 3% | 23% | 0% | 32% | 0.02 | 0.12 | 0.2 | 3.5 | 13% | bootsx48, long_swordx48, ruby_crystalx48 |
| thornjaw | 46.8 [34.9, 59.0] | 62 | 1.43 | 0.57 | 12% | 7% | 3% | 2% | 0.13 | 0.15 | 0.3 | 0.3 | 9% | bootsx62, long_swordx62, ruby_crystalx62 |
| kaelis | 45.5 [31.7, 59.9] | 44 | 1.28 | 0.51 | 23% | 3% | 3% | 13% | 0.16 | 0.11 | 0.2 | 1.4 | 8% | cloth_armorx44, long_swordx44, ruby_crystalx44 |
| rictus | 44.1 [28.9, 60.5] | 34 | 1.30 | 0.52 | 15% | 5% | 32% | 0% | 0.06 | 0.56 | 0.9 | 2.6 | 9% | long_swordx34, ruby_crystalx34, vampiric_bladex33 |
| mossgrove | 42.5 [28.5, 57.8] | 40 | 1.30 | 0.52 | 35% | 0% | 1% | 6% | 0.23 | 0.17 | 0.4 | 3.4 | 8% | long_swordx40, ruby_crystalx40, vampiric_bladex40 |
| veyra | 42.3 [29.9, 55.8] | 52 | 1.45 | 0.58 | 5% | 56% | 0% | 8% | 0.21 | 0.25 | 0.5 | 1.8 | 9% | long_swordx52, longbowx52, ruby_crystalx52 |
| quillan | 41.3 [28.3, 55.7] | 46 | 5.24 | 2.08 | 8% | 15% | 0% | 70% | 0.11 | 0.59 | 1.2 | 0.0 | 31% | ionian_charmx46, long_swordx46, longbowx46 |
| noctis | 40.7 [28.7, 54.0] | 54 | 1.65 | 0.66 | 75% | 0% | 16% | 0% | 0.17 | 0.39 | 0.8 | 0.1 | 13% | ionian_charmx54, longbowx54, ruby_crystalx54 |
| ossuar | 28.8 [18.3, 42.3] | 52 | 2.45 | 0.97 | 8% | 3% | 0% | 68% | 0.06 | 0.06 | 0.1 | 4.8 | 16% | cloth_armorx52, long_swordx52, ruby_crystalx52 |
| vellum | 28.3 [17.3, 42.5] | 46 | 2.90 | 1.15 | 7% | 0% | 0% | 81% | 0.09 | 0.41 | 1.0 | 3.3 | 21% | ionian_charmx46, longbowx46, ruby_crystalx46 |
| lumen | 25.0 [15.5, 37.7] | 56 | 0.88 | 0.35 | 67% | 0% | 0% | 0% | 0.09 | 0.07 | 0.2 | 0.1 | 7% | bootsx56, longbowx56, ruby_crystalx56 |
| corvane | 12.5 [5.5, 26.1] | 40 | 0.53 | 0.21 | 52% | 0% | 0% | 1% | 0.05 | 0.35 | 0.7 | 3.9 | 4% | bootsx40, cloth_armorx40, longbowx40 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.64 |
| Jungle | 50.0 [43.7, 56.3] | 1.54 |
| Mid | 50.0 [43.7, 56.3] | 4.27 |
| Support | 50.0 [43.7, 56.3] | 2.90 |
| Top | 50.0 [43.7, 56.3] | 2.17 |

## 5. Games

- length: median 16.0, p10 12, p90 19
- end reasons: {'nexus': 118, 'round_limit_towers': 1, 'round_limit_hp': 1} (draws 0)
- priority win rate: 55.0% [46.1, 63.6]
- north win rate: 48.3% [39.6, 57.2]
- length histogram: {9: 1, 10: 2, 11: 5, 12: 7, 13: 10, 14: 16, 15: 18, 16: 20, 17: 12, 18: 10, 19: 9, 20: 10}

## 6. Objectives

- takes per game: {'dragon': 1.95, 'baron': 0.8666666666666667}
- median round taken: dragon 9.0, baron 11.0
- win rate when secured: {'dragon': 46.15384615384615, 'baron': 51.92307692307692}
- camp clears per game: {'wolves': 6.25, 'krugs': 6.108333333333333, 'raptors': 6.55, 'blue_buff': 3.683333333333333, 'red_buff': 3.7333333333333334, 'dragon': 1.95, 'baron': 0.8666666666666667}

## 7. Structures

- first tower falls: median round 6.0, p10 4, p90 8
- games with at least one tower down: 100.0%
- first-tower win rate: 66.7%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 4.85 |
| chips_monster | 3.84 |
| chips_wave | 3.56 |
| base | 3.44 |
| blue_buff | 0.23 |
| red_buff | 0.14 |
| champion_kill | 0.07 |

| use | AP |
|---|---|
| shop | 11.44 |
| abilities | 2.62 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 53.7% | 11.3% | +42.4 |
| cloth_armor | 5 | 2.00 | 55.6% | 38.0% | +17.6 |
| control_ward | 2 | 1.22 | - | 50.0% | - |
| frost_charm | 2 | 1.12 | - | 50.0% | - |
| health_potion | 2 | 1.98 | - | 50.0% | - |
| ionian_charm | 8 | 2.00 | 56.0% | 13.1% | +42.9 |
| long_sword | 6 | 2.00 | 50.6% | 47.8% | +2.8 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 50.0% | 0.0% | +50.0 |
| stopwatch | 3 | 1.96 | - | 50.0% | - |
| swift_tonic | 1 | 1.98 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 52.2% | 43.7% | +8.5 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 68.28 per game
- that is 53.9% of all ability uses
- activations ending on a hexgroup edge: 98.3%


## 10. Anomalies

- ILLEGAL[activation r13]: stacking: n_mid_T2 and w36 on: 1 games

## 11. Top 5 flags (evidence only)

1. **anomaly: ILLEGAL[activation r13]: stacking: n_mid_T2 and w36 on** - 1 games
2. **champion win rate: corvane** - WR 12.5% [5.5, 26.1]
3. **champion win rate: wisp** - WR 84.0% [71.5, 91.7]
4. **champion win rate: ashwyn** - WR 75.0% [61.8, 84.8]
5. **champion win rate: lumen** - WR 25.0% [15.5, 37.7]

## 12. Delta vs batch_0033

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -1.3 | -2.94 | no |
| bastion | -2.2 | +0.02 | no |
| bramblehide | +10.4 | +0.05 | no |
| brixa | -4.7 | -0.01 | no |
| corvane | -9.4 | -0.00 | no |
| dax | +3.4 | +0.02 | no |
| grivven | +2.8 | +0.41 | no |
| kaelis | +4.8 | -0.00 | no |
| kestrel | -7.4 | +0.17 | no |
| lumen | -5.0 | +0.04 | no |
| marrow | -7.8 | +0.44 | no |
| mossgrove | -14.2 | -0.03 | no |
| noctis | +19.3 | -0.06 | no |
| orrin | +7.1 | +0.02 | no |
| ossuar | -18.7 | +0.20 | no |
| pallas | +8.2 | +0.56 | no |
| quillan | -14.9 | -1.55 | no |
| rictus | -1.3 | +0.00 | no |
| sable | +4.3 | +0.43 | no |
| sylphine | +14.3 | +0.02 | no |
| thornjaw | -10.0 | -0.03 | no |
| vellum | +0.1 | +0.30 | no |
| veyra | +1.1 | -0.09 | no |
| vurmak | +20.6 | +0.05 | no |
| wisp | +9.0 | +0.36 | no |

- median length delta: +1.0
- nexus-kill rate delta: -1.7 pts
