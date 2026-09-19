# Sim report batch_0006

## 1. Header

| field | value |
|---|---|
| rules | 1.0.0 |
| roster | 1.1.0 |
| ai | 1.1.0 |
| matchup | T2_search vs T1_greedy (temperature 0.3) |
| games | 200 |
| seed | 777002 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 405.8s |
| engine tests | not run |
| generated | 2026-09-19 17:14:37 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 4 FAIL / 21 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 47/58 abilities outside the band; roster mean 27.8%; 8 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 55.5% [48.6, 62.2] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 12.0 [11.0, 12.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 99.0% [96.4, 99.7] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, ossuar, quillan, sable (roster mean 2.21 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.5% [41.7, 55.4] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 88.2 [79.0, 93.6] | 76 | 10.98 | 4.96 | 1% | 4% | 0% | 94% | 2.00 | 1.50 | 2.1 | 1.9 | 51% | longbowx76, ruby_crystalx76, ionian_charmx75 |
| ossuar | 71.6 [61.4, 80.0] | 88 | 4.54 | 2.05 | 1% | 1% | 1% | 92% | 0.83 | 0.72 | 1.2 | 4.2 | 26% | ruby_crystalx88, long_swordx87, cloth_armorx84 |
| thornjaw | 64.7 [52.8, 75.0] | 68 | 0.70 | 0.31 | 34% | 7% | 14% | 11% | 0.47 | 1.25 | 1.9 | 1.7 | 5% | ruby_crystalx66, long_swordx60, bootsx54 |
| wisp | 63.3 [53.4, 72.1] | 98 | 3.11 | 1.41 | 7% | 39% | 1% | 47% | 0.69 | 1.67 | 2.8 | 2.6 | 19% | longbowx95, ruby_crystalx95, bootsx90 |
| veyra | 61.4 [49.7, 72.0] | 70 | 1.11 | 0.50 | 5% | 15% | 1% | 66% | 0.14 | 1.17 | 1.9 | 4.9 | 7% | long_swordx65, longbowx58, vampiric_bladex54 |
| sable | 58.8 [47.8, 68.9] | 80 | 6.98 | 3.15 | 2% | 9% | 0% | 84% | 1.55 | 1.73 | 2.6 | 2.6 | 41% | longbowx78, ionian_charmx72, ruby_crystalx67 |
| bramblehide | 57.5 [46.6, 67.7] | 80 | 2.81 | 1.27 | 2% | 6% | 2% | 77% | 1.16 | 1.84 | 2.9 | 3.5 | 18% | long_swordx80, ruby_crystalx80, vampiric_bladex73 |
| ashwyn | 57.3 [46.5, 67.5] | 82 | 6.60 | 2.98 | 1% | 76% | 0% | 18% | 1.07 | 1.73 | 2.8 | 0.5 | 39% | longbowx82, ionian_charmx80, ruby_crystalx79 |
| kestrel | 54.7 [44.2, 64.7] | 86 | 1.67 | 0.75 | 7% | 20% | 1% | 62% | 0.42 | 1.13 | 2.0 | 5.5 | 12% | long_swordx85, longbowx80, vampiric_bladex78 |
| kaelis | 52.6 [41.6, 63.3] | 78 | 0.82 | 0.37 | 21% | 10% | 3% | 35% | 0.54 | 1.03 | 1.8 | 2.4 | 6% | ruby_crystalx78, cloth_armorx69, long_swordx69 |
| grivven | 52.4 [41.8, 62.7] | 84 | 1.73 | 0.78 | 28% | 5% | 1% | 51% | 0.43 | 1.18 | 2.2 | 5.3 | 12% | longbowx84, ruby_crystalx84, bootsx78 |
| rictus | 50.0 [38.7, 61.3] | 72 | 0.52 | 0.24 | 23% | 7% | 18% | 19% | 0.92 | 1.54 | 2.7 | 2.4 | 4% | long_swordx70, ruby_crystalx70, vampiric_bladex59 |
| pallas | 48.7 [37.8, 59.7] | 76 | 2.59 | 1.17 | 4% | 7% | 4% | 67% | 0.72 | 1.72 | 3.0 | 3.3 | 17% | ruby_crystalx74, longbowx72, bootsx64 |
| corvane | 46.9 [35.2, 58.9] | 64 | 0.20 | 0.09 | 56% | 6% | 2% | 7% | 0.22 | 0.78 | 1.5 | 4.1 | 1% | longbowx64, ruby_crystalx64, bootsx58 |
| orrin | 46.4 [36.2, 57.0] | 84 | 0.75 | 0.34 | 10% | 41% | 10% | 4% | 0.33 | 1.32 | 2.3 | 3.2 | 5% | long_swordx78, longbowx68, vampiric_bladex60 |
| brixa | 45.5 [35.5, 55.8] | 88 | 1.04 | 0.47 | 15% | 7% | 8% | 47% | 0.38 | 1.18 | 2.0 | 3.4 | 7% | long_swordx88, longbowx74, vampiric_bladex71 |
| bastion | 44.0 [33.9, 54.7] | 84 | 1.71 | 0.77 | 11% | 10% | 1% | 49% | 0.58 | 1.15 | 1.9 | 4.4 | 12% | ruby_crystalx84, long_swordx70, cloth_armorx69 |
| mossgrove | 44.0 [34.7, 53.8] | 100 | 0.59 | 0.26 | 15% | 16% | 3% | 32% | 0.33 | 1.16 | 1.9 | 4.1 | 4% | ruby_crystalx98, long_swordx97, vampiric_bladex74 |
| vurmak | 43.8 [33.4, 54.7] | 80 | 1.02 | 0.46 | 16% | 4% | 5% | 53% | 0.46 | 1.39 | 2.4 | 3.4 | 8% | ruby_crystalx80, long_swordx61, cloth_armorx55 |
| dax | 43.1 [32.3, 54.6] | 72 | 1.07 | 0.48 | 10% | 19% | 2% | 54% | 0.35 | 1.10 | 1.9 | 3.5 | 7% | long_swordx72, longbowx65, vampiric_bladex65 |
| sylphine | 37.5 [27.7, 48.5] | 80 | 0.56 | 0.25 | 27% | 8% | 7% | 30% | 0.40 | 1.10 | 1.8 | 2.3 | 4% | ruby_crystalx78, long_swordx71, vampiric_bladex61 |
| lumen | 34.6 [25.0, 45.7] | 78 | 0.44 | 0.20 | 59% | 3% | 1% | 16% | 0.36 | 0.71 | 1.3 | 1.5 | 4% | longbowx77, ruby_crystalx76, bootsx64 |
| marrow | 34.3 [24.2, 46.0] | 70 | 0.96 | 0.43 | 7% | 9% | 3% | 48% | 0.41 | 1.10 | 2.0 | 3.3 | 7% | ruby_crystalx70, long_swordx56, cloth_armorx48 |
| vellum | 26.1 [18.1, 36.2] | 88 | 2.37 | 1.07 | 6% | 1% | 2% | 81% | 0.74 | 1.69 | 2.9 | 3.2 | 20% | longbowx81, ionian_charmx64, ruby_crystalx62 |
| noctis | 21.6 [13.8, 32.3] | 74 | 0.46 | 0.21 | 25% | 3% | 33% | 20% | 0.77 | 1.38 | 2.5 | 2.6 | 5% | longbowx66, ruby_crystalx46, ionian_charmx45 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [45.1, 54.9] | 1.13 |
| Jungle | 50.0 [45.1, 54.9] | 1.03 |
| Mid | 50.0 [45.1, 54.9] | 5.44 |
| Support | 50.0 [45.1, 54.9] | 1.73 |
| Top | 50.0 [45.1, 54.9] | 1.89 |

## 5. Games

- length: median 12.0, p10 9, p90 16
- end reasons: {'nexus': 198, 'round_limit_towers': 2} (draws 0)
- priority win rate: 55.5% [48.6, 62.2]
- north win rate: 48.5% [41.7, 55.4]
- length histogram: {7: 1, 8: 7, 9: 26, 10: 24, 11: 30, 12: 30, 13: 23, 14: 19, 15: 12, 16: 13, 17: 4, 18: 6, 19: 1, 20: 4}

## 6. Objectives

- takes per game: {'dragon': 1.86, 'baron': 0.84}
- median round taken: dragon 6.0, baron 10.0
- win rate when secured: {'dragon': 54.30107526881721, 'baron': 63.69047619047619}
- camp clears per game: {'krugs': 8.215, 'wolves': 7.66, 'raptors': 8.19, 'blue_buff': 4.62, 'red_buff': 4.69, 'dragon': 1.86, 'baron': 0.84}

## 7. Structures

- first tower falls: median round 3.0, p10 1, p90 5
- games with at least one tower down: 100.0%
- first-tower win rate: 73.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.06 |
| chips_wave | 3.45 |
| base | 3.40 |
| chips_structure | 3.22 |
| champion_kill | 0.45 |
| blue_buff | 0.37 |
| red_buff | 0.21 |

| use | AP |
|---|---|
| shop | 10.81 |
| abilities | 3.22 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.77 | 70.4% | 11.3% | +59.1 |
| cloth_armor | 5 | 1.62 | 72.4% | 31.8% | +40.5 |
| control_ward | 2 | 0.28 | - | 50.0% | - |
| frost_charm | 2 | 0.17 | - | 50.0% | - |
| health_potion | 2 | 1.89 | - | 50.0% | - |
| ionian_charm | 8 | 1.68 | 75.6% | 16.1% | +59.4 |
| long_sword | 6 | 1.96 | 57.5% | 33.0% | +24.6 |
| longbow | 6 | 1.99 | 53.6% | 45.5% | +8.1 |
| ruby_crystal | 4 | 2.00 | 55.0% | 0.0% | +55.0 |
| stopwatch | 3 | 1.83 | - | 50.0% | - |
| swift_tonic | 1 | 1.89 | - | 50.0% | - |
| vampiric_blade | 5 | 1.68 | 67.1% | 30.0% | +37.1 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: quillan** - 10.98 AP/round = 4.96x roster mean
2. **champion win rate: quillan** - WR 88.2% [79.0, 93.6]
3. **economy outlier: sable** - 6.98 AP/round = 3.15x roster mean
4. **economy outlier: ashwyn** - 6.60 AP/round = 2.98x roster mean
5. **champion win rate: noctis** - WR 21.6% [13.8, 32.3]
