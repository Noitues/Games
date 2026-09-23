# Sim report batch_0037

## 1. Header

| field | value |
|---|---|
| rules | 1.6.0 |
| roster | 1.6.0 |
| ai | 1.3.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 120 |
| seed | 3701 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 5347.5s |
| engine tests | not run |
| generated | 2026-09-23 05:17:42 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 2 FAIL / 23 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 51/58 abilities outside the band; roster mean 19.2%; 9 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 48.3% [39.6, 57.2] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 15.0 [14.0, 16.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 93.3% [87.4, 96.6] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.46 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 55.0% [46.1, 63.6] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 82.6 [69.3, 90.9] | 46 | 5.88 | 2.39 | 2% | 85% | 0% | 8% | 0.04 | 0.30 | 0.6 | 0.0 | 30% | bootsx46, cloth_armorx46, longbowx46 |
| ashwyn | 67.5 [52.0, 79.9] | 40 | 5.61 | 2.28 | 4% | 73% | 0% | 15% | 0.10 | 0.72 | 1.3 | 0.0 | 33% | ionian_charmx40, long_swordx40, longbowx40 |
| veyra | 65.0 [52.4, 75.8] | 60 | 1.67 | 0.68 | 2% | 72% | 0% | 7% | 0.12 | 0.18 | 0.4 | 1.3 | 10% | long_swordx60, longbowx60, ruby_crystalx60 |
| sable | 62.1 [49.2, 73.4] | 58 | 6.33 | 2.57 | 3% | 53% | 0% | 35% | 0.12 | 0.12 | 0.2 | 1.2 | 36% | longbowx58, ruby_crystalx57, ionian_charmx56 |
| pallas | 60.4 [46.3, 73.0] | 48 | 4.26 | 1.73 | 3% | 0% | 0% | 90% | 0.04 | 0.48 | 0.9 | 4.3 | 25% | bootsx48, longbowx48, ruby_crystalx48 |
| kestrel | 60.0 [44.6, 73.7] | 40 | 1.90 | 0.77 | 57% | 14% | 0% | 20% | 0.10 | 0.12 | 0.3 | 3.4 | 12% | long_swordx40, longbowx39, vampiric_bladex39 |
| bramblehide | 57.9 [42.2, 72.1] | 38 | 1.86 | 0.76 | 4% | 24% | 0% | 25% | 0.11 | 0.16 | 0.3 | 3.1 | 11% | long_swordx38, ruby_crystalx38, vampiric_bladex38 |
| bastion | 54.8 [39.9, 68.8] | 42 | 2.40 | 0.97 | 81% | 0% | 0% | 4% | 0.21 | 0.05 | 0.1 | 0.9 | 15% | cloth_armorx42, long_swordx42, ruby_crystalx42 |
| thornjaw | 54.7 [42.6, 66.3] | 64 | 1.42 | 0.58 | 11% | 6% | 3% | 2% | 0.16 | 0.17 | 0.3 | 0.2 | 9% | ruby_crystalx64, long_swordx63, vampiric_bladex62 |
| marrow | 54.0 [40.4, 67.0] | 50 | 2.49 | 1.01 | 6% | 1% | 0% | 41% | 0.08 | 0.06 | 0.1 | 0.0 | 16% | ruby_crystalx50, cloth_armorx49, long_swordx49 |
| orrin | 50.0 [33.6, 66.4] | 32 | 1.76 | 0.71 | 9% | 33% | 2% | 1% | 0.03 | 0.38 | 0.7 | 0.1 | 11% | long_swordx32, longbowx31, vampiric_bladex30 |
| quillan | 50.0 [36.1, 63.9] | 46 | 5.34 | 2.17 | 8% | 8% | 0% | 75% | 0.09 | 0.50 | 1.0 | 0.0 | 32% | ionian_charmx46, long_swordx46, longbowx46 |
| vurmak | 50.0 [35.8, 64.2] | 44 | 1.42 | 0.58 | 14% | 2% | 1% | 52% | 0.09 | 0.36 | 0.8 | 3.8 | 9% | ruby_crystalx44, long_swordx41, cloth_armorx39 |
| mossgrove | 48.2 [35.7, 61.0] | 56 | 1.30 | 0.53 | 36% | 3% | 0% | 4% | 0.04 | 0.27 | 0.5 | 3.1 | 9% | long_swordx56, ruby_crystalx56, vampiric_bladex54 |
| kaelis | 48.1 [35.1, 61.3] | 52 | 1.29 | 0.52 | 20% | 4% | 2% | 14% | 0.15 | 0.19 | 0.3 | 1.4 | 9% | ruby_crystalx52, cloth_armorx51, long_swordx51 |
| ossuar | 44.2 [31.6, 57.7] | 52 | 2.53 | 1.03 | 5% | 4% | 0% | 63% | 0.00 | 0.04 | 0.1 | 4.3 | 15% | cloth_armorx52, long_swordx52, ruby_crystalx52 |
| sylphine | 44.1 [28.9, 60.5] | 34 | 1.39 | 0.56 | 11% | 1% | 1% | 8% | 0.12 | 0.06 | 0.2 | 0.1 | 9% | ruby_crystalx34, long_swordx33, vampiric_bladex33 |
| rictus | 43.8 [30.7, 57.7] | 48 | 1.21 | 0.49 | 15% | 3% | 30% | 1% | 0.19 | 0.27 | 0.6 | 2.6 | 8% | long_swordx48, ruby_crystalx48, vampiric_bladex47 |
| noctis | 42.5 [28.5, 57.8] | 40 | 1.68 | 0.68 | 77% | 0% | 12% | 1% | 0.15 | 0.25 | 0.5 | 0.1 | 13% | ionian_charmx40, longbowx40, ruby_crystalx40 |
| dax | 38.3 [27.1, 51.0] | 60 | 1.54 | 0.63 | 10% | 43% | 2% | 9% | 0.13 | 0.12 | 0.3 | 1.1 | 10% | long_swordx60, longbowx60, vampiric_bladex60 |
| brixa | 37.5 [25.2, 51.6] | 48 | 1.37 | 0.56 | 36% | 2% | 8% | 1% | 0.17 | 0.06 | 0.1 | 0.8 | 9% | long_swordx48, longbowx47, vampiric_bladex47 |
| corvane | 37.5 [25.2, 51.6] | 48 | 0.57 | 0.23 | 50% | 0% | 0% | 1% | 0.10 | 0.35 | 0.7 | 3.4 | 4% | bootsx48, longbowx48, ruby_crystalx48 |
| lumen | 36.0 [24.1, 49.9] | 50 | 0.80 | 0.33 | 61% | 0% | 0% | 1% | 0.00 | 0.18 | 0.4 | 0.1 | 6% | bootsx50, longbowx50, ruby_crystalx50 |
| grivven | 35.4 [23.4, 49.6] | 48 | 2.79 | 1.13 | 2% | 1% | 2% | 70% | 0.04 | 0.25 | 0.6 | 7.9 | 18% | bootsx48, ruby_crystalx48, longbowx47 |
| vellum | 30.4 [19.9, 43.3] | 56 | 2.77 | 1.12 | 7% | 0% | 0% | 81% | 0.14 | 0.46 | 0.9 | 3.0 | 19% | longbowx54, ionian_charmx52, ruby_crystalx49 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.63 |
| Jungle | 50.0 [43.7, 56.3] | 1.42 |
| Mid | 50.0 [43.7, 56.3] | 4.41 |
| Support | 50.0 [43.7, 56.3] | 2.82 |
| Top | 50.0 [43.7, 56.3] | 2.03 |

## 5. Games

- length: median 15.0, p10 11, p90 19
- end reasons: {'nexus': 112, 'round_limit_towers': 6, 'round_limit_hp': 2} (draws 0)
- priority win rate: 48.3% [39.6, 57.2]
- north win rate: 55.0% [46.1, 63.6]
- length histogram: {9: 2, 10: 4, 11: 7, 12: 9, 13: 5, 14: 28, 15: 14, 16: 14, 17: 9, 18: 11, 19: 7, 20: 10}

## 6. Objectives

- takes per game: {'dragon': 2.0083333333333333, 'baron': 0.9166666666666666}
- median round taken: dragon 9, baron 11.0
- win rate when secured: {'dragon': 53.941908713692946, 'baron': 44.54545454545455}
- camp clears per game: {'wolves': 6.208333333333333, 'krugs': 6.433333333333334, 'raptors': 6.458333333333333, 'red_buff': 3.658333333333333, 'blue_buff': 3.625, 'dragon': 2.0083333333333333, 'baron': 0.9166666666666666}

## 7. Structures

- first tower falls: median round 6.0, p10 4, p90 8
- games with at least one tower down: 100.0%
- first-tower win rate: 75.8%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 4.59 |
| chips_monster | 3.96 |
| chips_wave | 3.48 |
| base | 3.44 |
| blue_buff | 0.24 |
| red_buff | 0.17 |
| champion_kill | 0.07 |

| use | AP |
|---|---|
| shop | 11.71 |
| abilities | 2.38 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 54.4% | 15.6% | +38.8 |
| cloth_armor | 5 | 1.94 | 55.3% | 39.2% | +16.0 |
| control_ward | 2 | 1.38 | - | 50.0% | - |
| frost_charm | 2 | 1.06 | - | 50.0% | - |
| health_potion | 2 | 1.87 | - | 50.0% | - |
| ionian_charm | 8 | 1.95 | 55.7% | 19.3% | +36.4 |
| long_sword | 6 | 2.00 | 51.3% | 45.3% | +6.1 |
| longbow | 6 | 1.99 | 50.4% | 49.4% | +1.0 |
| ruby_crystal | 4 | 2.00 | 50.8% | 0.0% | +50.8 |
| stopwatch | 3 | 1.82 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.98 | 53.0% | 42.1% | +10.9 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 52 | 86.5 [74.7, 93.3] |
| T2_objective | 44 | 68.2 [53.4, 80.0] |
| T2_laner | 46 | 52.2 [38.1, 65.9] |
| T2_warder | 46 | 21.7 [12.3, 35.6] |
| T2_brawler | 52 | 21.2 [12.2, 34.0] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 66.33 per game
- that is 56.1% of all ability uses
- activations ending beside an enemy-held hexgroup (looking in): 56.4%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **champion win rate: wisp** - WR 82.6% [69.3, 90.9]
2. **economy outlier: sable** - 6.33 AP/round = 2.57x roster mean
3. **champion win rate: vellum** - WR 30.4% [19.9, 43.3]
4. **economy outlier: wisp** - 5.88 AP/round = 2.39x roster mean
5. **economy outlier: ashwyn** - 5.61 AP/round = 2.28x roster mean

## 12. Delta vs batch_0035

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -3.3 | -0.15 | no |
| bastion | -26.2 | -0.10 | no |
| bramblehide | -0.4 | -0.19 | no |
| brixa | -10.3 | -0.21 | no |
| corvane | +4.9 | -0.03 | no |
| dax | -23.0 | +0.02 | no |
| grivven | -1.5 | +0.17 | no |
| kaelis | +2.1 | -0.04 | no |
| kestrel | +10.0 | +0.00 | no |
| lumen | +12.1 | -0.08 | no |
| marrow | -2.0 | -0.31 | no |
| mossgrove | -1.8 | +0.00 | no |
| noctis | +9.8 | -0.02 | no |
| orrin | +1.8 | -0.11 | no |
| ossuar | +17.7 | +0.12 | no |
| pallas | -7.4 | -0.24 | no |
| quillan | +7.1 | -0.05 | no |
| rictus | -4.5 | -0.11 | no |
| sable | -10.2 | +0.03 | no |
| sylphine | +7.3 | -0.10 | no |
| thornjaw | +1.7 | -0.05 | no |
| vellum | +3.1 | -0.04 | no |
| veyra | +21.2 | +0.14 | no |
| vurmak | -2.9 | -0.17 | no |
| wisp | -2.2 | -0.01 | no |

- median length delta: -1.0
- nexus-kill rate delta: -4.2 pts
