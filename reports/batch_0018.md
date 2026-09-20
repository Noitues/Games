# Sim report batch_0018

## 1. Header

| field | value |
|---|---|
| rules | 1.1.0 |
| roster | 1.2.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 1801 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 464.7s |
| engine tests | not run |
| generated | 2026-09-20 17:42:34 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 6 FAIL / 19 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 53/56 abilities outside the band; roster mean 18.3%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 50.0% [42.1, 57.9] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 14.0 [13.0, 14.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 92.7% [87.3, 95.9] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.61 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 45.3% [37.6, 53.3] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 82.8 [71.1, 90.4] | 58 | 6.70 | 2.57 | 9% | 74% | 1% | 7% | 0.03 | 0.02 | 0.0 | 0.0 | 35% | bootsx58, cloth_armorx58, longbowx58 |
| ashwyn | 74.0 [60.4, 84.1] | 50 | 10.12 | 3.88 | 2% | 88% | 0% | 5% | 0.02 | 0.00 | 0.0 | 0.0 | 50% | bootsx50, cloth_armorx50, ionian_charmx50 |
| bramblehide | 62.5 [50.3, 73.3] | 64 | 2.13 | 0.82 | 3% | 26% | 1% | 35% | 0.00 | 0.00 | 0.0 | 3.9 | 14% | long_swordx64, ruby_crystalx64, vampiric_bladex63 |
| ossuar | 62.5 [48.4, 74.8] | 48 | 2.09 | 0.80 | 13% | 9% | 3% | 41% | 0.02 | 0.00 | 0.0 | 3.4 | 13% | cloth_armorx48, long_swordx48, ruby_crystalx48 |
| thornjaw | 62.1 [49.2, 73.4] | 58 | 1.05 | 0.40 | 12% | 19% | 8% | 5% | 0.02 | 0.02 | 0.0 | 0.8 | 7% | long_swordx58, ruby_crystalx58, vampiric_bladex56 |
| pallas | 60.8 [49.4, 71.1] | 74 | 5.05 | 1.94 | 6% | 1% | 0% | 86% | 0.00 | 0.01 | 0.0 | 4.6 | 30% | bootsx74, longbowx74, ruby_crystalx74 |
| marrow | 57.8 [45.6, 69.1] | 64 | 1.74 | 0.67 | 13% | 2% | 9% | 22% | 0.00 | 0.00 | 0.0 | 0.8 | 11% | cloth_armorx64, long_swordx64, ruby_crystalx64 |
| kestrel | 57.1 [45.5, 68.1] | 70 | 1.83 | 0.70 | 38% | 18% | 4% | 22% | 0.00 | 0.03 | 0.1 | 3.2 | 11% | long_swordx70, longbowx70, ruby_crystalx70 |
| vurmak | 56.0 [42.3, 68.8] | 50 | 1.41 | 0.54 | 18% | 5% | 3% | 44% | 0.04 | 0.00 | 0.0 | 3.5 | 9% | ruby_crystalx50, long_swordx49, cloth_armorx46 |
| quillan | 55.8 [42.3, 68.4] | 52 | 7.95 | 3.05 | 4% | 3% | 2% | 84% | 0.02 | 0.02 | 0.0 | 2.5 | 43% | ionian_charmx52, long_swordx52, longbowx52 |
| veyra | 55.0 [42.5, 66.9] | 60 | 1.04 | 0.40 | 13% | 34% | 6% | 14% | 0.03 | 0.05 | 0.1 | 2.8 | 7% | long_swordx60, longbowx58, vampiric_bladex56 |
| rictus | 52.2 [38.1, 65.9] | 46 | 1.07 | 0.41 | 20% | 19% | 21% | 1% | 0.00 | 0.02 | 0.1 | 1.7 | 6% | long_swordx46, ruby_crystalx46, vampiric_bladex46 |
| brixa | 51.9 [38.9, 64.6] | 54 | 1.19 | 0.46 | 29% | 11% | 10% | 8% | 0.02 | 0.00 | 0.0 | 1.1 | 8% | long_swordx54, longbowx54, vampiric_bladex53 |
| orrin | 51.7 [39.2, 64.1] | 58 | 0.98 | 0.38 | 18% | 20% | 10% | 6% | 0.02 | 0.03 | 0.1 | 2.0 | 6% | long_swordx58, longbowx57, vampiric_bladex55 |
| bastion | 50.0 [38.4, 61.6] | 68 | 1.69 | 0.65 | 42% | 3% | 1% | 11% | 0.00 | 0.00 | 0.0 | 2.3 | 11% | cloth_armorx68, long_swordx68, ruby_crystalx68 |
| sable | 50.0 [37.5, 62.5] | 58 | 6.40 | 2.46 | 5% | 59% | 0% | 24% | 0.00 | 0.00 | 0.0 | 2.7 | 38% | ionian_charmx58, longbowx58, ruby_crystalx58 |
| vellum | 47.2 [36.1, 58.6] | 72 | 3.09 | 1.18 | 11% | 1% | 8% | 70% | 0.01 | 0.04 | 0.1 | 2.7 | 22% | ionian_charmx72, longbowx72, ruby_crystalx71 |
| sylphine | 45.8 [34.8, 57.3] | 72 | 0.82 | 0.32 | 12% | 2% | 10% | 16% | 0.03 | 0.00 | 0.0 | 1.0 | 5% | long_swordx72, ruby_crystalx72, vampiric_bladex67 |
| grivven | 43.8 [30.7, 57.7] | 48 | 3.27 | 1.25 | 15% | 2% | 0% | 61% | 0.06 | 0.04 | 0.1 | 8.0 | 22% | bootsx48, longbowx48, ruby_crystalx48 |
| corvane | 37.1 [26.2, 49.5] | 62 | 0.46 | 0.18 | 39% | 2% | 10% | 1% | 0.00 | 0.08 | 0.2 | 3.5 | 3% | bootsx62, longbowx62, ruby_crystalx62 |
| dax | 32.8 [22.1, 45.6] | 58 | 1.16 | 0.45 | 20% | 28% | 4% | 16% | 0.00 | 0.02 | 0.0 | 1.9 | 8% | long_swordx58, longbowx58, vampiric_bladex57 |
| noctis | 30.9 [21.2, 42.6] | 68 | 1.41 | 0.54 | 49% | 5% | 21% | 2% | 0.00 | 0.06 | 0.2 | 0.4 | 11% | longbowx68, ionian_charmx65, ruby_crystalx64 |
| kaelis | 30.0 [20.5, 41.5] | 70 | 0.95 | 0.36 | 21% | 16% | 4% | 11% | 0.00 | 0.00 | 0.0 | 1.0 | 6% | long_swordx70, ruby_crystalx70, cloth_armorx68 |
| mossgrove | 28.3 [18.5, 40.8] | 60 | 0.86 | 0.33 | 25% | 16% | 1% | 7% | 0.00 | 0.02 | 0.0 | 3.4 | 6% | long_swordx60, ruby_crystalx60, vampiric_bladex59 |
| lumen | 22.4 [13.6, 34.7] | 58 | 0.66 | 0.25 | 36% | 3% | 1% | 2% | 0.00 | 0.05 | 0.1 | 0.3 | 5% | longbowx58, ruby_crystalx58, bootsx57 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 1.27 |
| Jungle | 50.0 [44.4, 55.6] | 1.19 |
| Mid | 50.0 [44.4, 55.6] | 5.36 |
| Support | 50.0 [44.4, 55.6] | 3.29 |
| Top | 50.0 [44.4, 55.6] | 1.54 |

## 5. Games

- length: median 14.0, p10 11, p90 19
- end reasons: {'nexus': 139, 'round_limit_towers': 10, 'round_limit_hp': 1} (draws 0)
- priority win rate: 50.0% [42.1, 57.9]
- north win rate: 45.3% [37.6, 53.3]
- length histogram: {9: 1, 10: 5, 11: 24, 12: 25, 13: 12, 14: 24, 15: 15, 16: 12, 17: 12, 18: 3, 19: 5, 20: 12}

## 6. Objectives

- takes per game: {'dragon': 1.88, 'baron': 0.8333333333333334}
- median round taken: dragon 9.0, baron 11
- win rate when secured: {'dragon': 48.93617021276596, 'baron': 43.2}
- camp clears per game: {'raptors': 6.78, 'blue_buff': 4.073333333333333, 'krugs': 6.873333333333333, 'wolves': 6.1466666666666665, 'red_buff': 4.1866666666666665, 'dragon': 1.88, 'baron': 0.8333333333333334}

## 7. Structures

- first tower falls: median round 5.0, p10 3, p90 7
- games with at least one tower down: 100.0%
- first-tower win rate: 72.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.26 |
| chips_wave | 4.01 |
| chips_structure | 3.92 |
| base | 3.37 |
| blue_buff | 0.28 |
| red_buff | 0.21 |
| champion_kill | 0.01 |

| use | AP |
|---|---|
| shop | 11.83 |
| abilities | 2.23 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.99 | 57.6% | 2.0% | +55.6 |
| cloth_armor | 5 | 1.96 | 59.9% | 32.5% | +27.3 |
| control_ward | 2 | 1.21 | - | 50.0% | - |
| frost_charm | 2 | 1.05 | - | 50.0% | - |
| health_potion | 2 | 1.95 | - | 50.0% | - |
| ionian_charm | 8 | 1.98 | 60.7% | 5.2% | +55.6 |
| long_sword | 6 | 2.00 | 51.3% | 45.3% | +6.0 |
| longbow | 6 | 2.00 | 50.2% | 49.8% | +0.4 |
| ruby_crystal | 4 | 2.00 | 51.0% | 0.0% | +51.0 |
| stopwatch | 3 | 1.92 | - | 50.0% | - |
| swift_tonic | 1 | 1.97 | - | 50.0% | - |
| vampiric_blade | 5 | 1.95 | 55.4% | 37.0% | +18.4 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 82.55 per game
- that is 84.4% of all ability uses


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 10.12 AP/round = 3.88x roster mean
2. **champion win rate: wisp** - WR 82.8% [71.1, 90.4]
3. **economy outlier: quillan** - 7.95 AP/round = 3.05x roster mean
4. **champion win rate: lumen** - WR 22.4% [13.6, 34.7]
5. **champion win rate: ashwyn** - WR 74.0% [60.4, 84.1]

## 12. Delta vs batch_0016

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -13.5 | +0.61 | no |
| bastion | -1.8 | +0.17 | no |
| bramblehide | +12.5 | +0.14 | no |
| brixa | +17.2 | +0.06 | no |
| corvane | +15.4 | +0.09 | no |
| dax | -20.0 | -0.04 | no |
| grivven | +12.2 | +0.56 | no |
| kaelis | -0.6 | +0.09 | no |
| kestrel | -11.8 | -0.03 | no |
| lumen | -27.6 | -0.02 | no |
| marrow | +9.2 | +0.16 | no |
| mossgrove | -18.7 | +0.09 | no |
| noctis | +4.8 | +0.15 | no |
| orrin | +15.5 | +0.12 | no |
| ossuar | +4.2 | +0.15 | no |
| pallas | -11.2 | +0.46 | no |
| quillan | -6.7 | +0.14 | no |
| rictus | -1.4 | +0.03 | no |
| sable | +12.1 | +0.57 | no |
| sylphine | -5.7 | +0.04 | no |
| thornjaw | +13.8 | +0.08 | no |
| vellum | +11.5 | +0.48 | no |
| veyra | +0.0 | +0.05 | no |
| vurmak | +4.4 | +0.14 | no |
| wisp | -0.6 | +0.50 | no |

- median length delta: +3.0
- nexus-kill rate delta: -4.7 pts
