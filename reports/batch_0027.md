# Sim report batch_0027

## 1. Header

| field | value |
|---|---|
| rules | 1.2.0 |
| roster | 1.3.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 2602 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 548.9s |
| engine tests | not run |
| generated | 2026-09-20 22:39:06 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 4 FAIL / 21 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 48/56 abilities outside the band; roster mean 18.7%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 45.3% [37.6, 53.3] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 16.0 [16.0, 17.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 86.7% [80.3, 91.2] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, wisp (roster mean 2.32 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 42.0% [34.4, 50.0] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 75.0 [63.2, 84.0] | 64 | 7.15 | 3.08 | 3% | 85% | 1% | 5% | 0.27 | 0.53 | 0.9 | 0.0 | 41% | bootsx64, cloth_armorx64, longbowx64 |
| ashwyn | 72.2 [59.1, 82.4] | 54 | 11.17 | 4.82 | 0% | 97% | 0% | 1% | 0.26 | 0.24 | 0.4 | 0.0 | 57% | bootsx54, cloth_armorx54, ionian_charmx54 |
| ossuar | 67.3 [53.8, 78.5] | 52 | 2.18 | 0.94 | 6% | 6% | 6% | 58% | 0.25 | 0.10 | 0.3 | 4.6 | 14% | cloth_armorx52, long_swordx52, ruby_crystalx52 |
| quillan | 59.5 [48.1, 69.9] | 74 | 8.51 | 3.67 | 0% | 0% | 1% | 95% | 0.19 | 0.58 | 1.2 | 3.1 | 49% | ionian_charmx74, long_swordx74, longbowx74 |
| grivven | 59.1 [44.4, 72.3] | 44 | 3.32 | 1.43 | 2% | 4% | 0% | 74% | 0.11 | 0.14 | 0.3 | 8.8 | 22% | longbowx44, ruby_crystalx44, bootsx43 |
| dax | 58.9 [45.9, 70.8] | 56 | 1.00 | 0.43 | 42% | 16% | 2% | 13% | 0.14 | 0.16 | 0.3 | 1.3 | 7% | long_swordx56, ruby_crystalx55, vampiric_bladex55 |
| sable | 58.0 [44.2, 70.6] | 50 | 6.17 | 2.66 | 1% | 82% | 0% | 11% | 0.12 | 0.34 | 0.8 | 3.5 | 40% | longbowx50, ionian_charmx48, ruby_crystalx48 |
| thornjaw | 56.7 [44.1, 68.4] | 60 | 0.80 | 0.34 | 24% | 32% | 4% | 2% | 0.25 | 0.10 | 0.2 | 0.3 | 5% | long_swordx59, ruby_crystalx59, vampiric_bladex58 |
| pallas | 56.0 [42.3, 68.8] | 50 | 2.66 | 1.15 | 20% | 2% | 3% | 57% | 0.18 | 0.44 | 1.1 | 3.5 | 17% | longbowx50, ruby_crystalx50, bootsx48 |
| orrin | 52.9 [41.2, 64.3] | 68 | 0.68 | 0.29 | 8% | 20% | 21% | 11% | 0.13 | 0.28 | 0.6 | 2.5 | 5% | long_swordx67, longbowx65, vampiric_bladex65 |
| sylphine | 51.8 [39.0, 64.3] | 56 | 0.53 | 0.23 | 18% | 3% | 12% | 23% | 0.12 | 0.12 | 0.2 | 1.4 | 4% | ruby_crystalx56, long_swordx53, vampiric_bladex50 |
| vurmak | 51.6 [39.6, 63.4] | 64 | 1.11 | 0.48 | 43% | 11% | 1% | 17% | 0.34 | 0.09 | 0.2 | 1.6 | 8% | ruby_crystalx64, cloth_armorx57, long_swordx57 |
| mossgrove | 51.4 [40.1, 62.6] | 72 | 0.69 | 0.30 | 36% | 17% | 1% | 12% | 0.12 | 0.03 | 0.1 | 4.8 | 5% | long_swordx72, ruby_crystalx72, vampiric_bladex68 |
| kaelis | 48.3 [36.2, 60.7] | 60 | 0.71 | 0.31 | 39% | 9% | 8% | 6% | 0.20 | 0.18 | 0.4 | 0.3 | 5% | ruby_crystalx60, long_swordx58, cloth_armorx57 |
| brixa | 46.6 [34.3, 59.2] | 58 | 0.81 | 0.35 | 16% | 30% | 9% | 7% | 0.09 | 0.28 | 0.6 | 1.1 | 7% | long_swordx58, longbowx54, vampiric_bladex54 |
| rictus | 46.4 [34.0, 59.3] | 56 | 0.69 | 0.30 | 10% | 38% | 10% | 6% | 0.20 | 0.29 | 0.6 | 1.4 | 5% | ruby_crystalx56, long_swordx55, vampiric_bladex52 |
| veyra | 46.2 [33.3, 59.5] | 52 | 1.02 | 0.44 | 7% | 53% | 10% | 7% | 0.12 | 0.37 | 0.9 | 1.5 | 8% | long_swordx51, longbowx49, vampiric_bladex47 |
| kestrel | 45.5 [34.0, 57.4] | 66 | 1.54 | 0.66 | 15% | 45% | 9% | 18% | 0.17 | 0.12 | 0.3 | 2.8 | 10% | long_swordx66, vampiric_bladex66, longbowx63 |
| marrow | 43.9 [32.6, 55.9] | 66 | 0.65 | 0.28 | 28% | 3% | 16% | 10% | 0.15 | 0.15 | 0.4 | 1.7 | 5% | ruby_crystalx66, long_swordx64, cloth_armorx63 |
| bramblehide | 42.9 [30.8, 55.9] | 56 | 2.07 | 0.89 | 1% | 35% | 1% | 44% | 0.05 | 0.14 | 0.3 | 5.2 | 16% | long_swordx56, ruby_crystalx56, vampiric_bladex53 |
| bastion | 41.4 [29.6, 54.2] | 58 | 1.24 | 0.54 | 65% | 5% | 0% | 1% | 0.14 | 0.17 | 0.4 | 0.3 | 10% | ruby_crystalx58, cloth_armorx57, long_swordx55 |
| vellum | 39.4 [28.5, 51.5] | 66 | 1.88 | 0.81 | 7% | 1% | 22% | 54% | 0.12 | 0.61 | 1.4 | 2.6 | 17% | longbowx62, ruby_crystalx57, ionian_charmx53 |
| corvane | 39.2 [28.9, 50.6] | 74 | 0.20 | 0.09 | 19% | 4% | 23% | 6% | 0.18 | 0.34 | 0.9 | 4.5 | 2% | longbowx74, ruby_crystalx74, bootsx73 |
| lumen | 27.9 [18.7, 39.6] | 68 | 0.55 | 0.24 | 60% | 4% | 1% | 4% | 0.10 | 0.22 | 0.5 | 0.6 | 5% | longbowx68, ruby_crystalx68, bootsx62 |
| noctis | 21.4 [12.7, 33.8] | 56 | 0.63 | 0.27 | 30% | 14% | 14% | 6% | 0.12 | 0.41 | 0.9 | 2.4 | 6% | longbowx56, ruby_crystalx54, ionian_charmx46 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 1.01 |
| Jungle | 50.0 [44.4, 55.6] | 0.94 |
| Mid | 50.0 [44.4, 55.6] | 5.67 |
| Support | 50.0 [44.4, 55.6] | 2.63 |
| Top | 50.0 [44.4, 55.6] | 1.14 |

## 5. Games

- length: median 16.0, p10 13, p90 20
- end reasons: {'nexus': 130, 'round_limit_hp': 3, 'round_limit_towers': 17} (draws 0)
- priority win rate: 45.3% [37.6, 53.3]
- north win rate: 42.0% [34.4, 50.0]
- length histogram: {9: 1, 10: 1, 11: 7, 12: 5, 13: 13, 14: 16, 15: 18, 16: 24, 17: 15, 18: 15, 19: 10, 20: 25}

## 6. Objectives

- takes per game: {'dragon': 1.9266666666666667, 'baron': 0.9066666666666666}
- median round taken: dragon 10, baron 11.5
- win rate when secured: {'dragon': 43.944636678200695, 'baron': 44.85294117647059}
- camp clears per game: {'raptors': 7.2, 'krugs': 7.1866666666666665, 'blue_buff': 4.533333333333333, 'wolves': 6.866666666666666, 'red_buff': 4.546666666666667, 'dragon': 1.9266666666666667, 'baron': 0.9066666666666666}

## 7. Structures

- first tower falls: median round 6.0, p10 5, p90 9
- games with at least one tower down: 100.0%
- first-tower win rate: 76.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.11 |
| chips_wave | 3.87 |
| base | 3.39 |
| chips_structure | 3.09 |
| blue_buff | 0.28 |
| red_buff | 0.14 |
| champion_kill | 0.07 |

| use | AP |
|---|---|
| shop | 10.48 |
| abilities | 2.15 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.93 | 58.8% | 6.7% | +52.1 |
| cloth_armor | 5 | 1.91 | 60.8% | 31.7% | +29.1 |
| control_ward | 2 | 1.17 | - | 50.0% | - |
| frost_charm | 2 | 1.11 | - | 50.0% | - |
| health_potion | 2 | 1.97 | - | 50.0% | - |
| ionian_charm | 8 | 1.83 | 62.9% | 8.9% | +54.0 |
| long_sword | 6 | 1.99 | 52.9% | 41.2% | +11.7 |
| longbow | 6 | 2.00 | 51.1% | 48.5% | +2.6 |
| ruby_crystal | 4 | 2.00 | 51.5% | 0.0% | +51.5 |
| stopwatch | 3 | 1.97 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.95 | 57.0% | 34.9% | +22.0 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 49.04 per game
- that is 45.8% of all ability uses


## 10. Anomalies

- ILLEGAL[activation r6]: stacking: s_noctis and s_bastion on: 1 games
- ILLEGAL[activation r11]: stacking: n_lumen and n_marrow on: 1 games
- ILLEGAL[world r11]: stacking: n_lumen and n_marrow on: 1 games
- ILLEGAL[upkeep r12]: stacking: n_lumen and n_marrow on: 1 games
- ILLEGAL[activation r12]: stacking: n_lumen and n_marrow on: 1 games
- ILLEGAL[activation r11]: stacking: n_corvane and n_bastion on: 1 games

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 11.17 AP/round = 4.82x roster mean
2. **economy outlier: quillan** - 8.51 AP/round = 3.67x roster mean
3. **anomaly: ILLEGAL[activation r6]: stacking: s_noctis and s_bastion on** - 1 games
4. **anomaly: ILLEGAL[activation r11]: stacking: n_lumen and n_marrow on** - 1 games
5. **anomaly: ILLEGAL[world r11]: stacking: n_lumen and n_marrow on** - 1 games

## 12. Delta vs batch_0023

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -12.2 | +0.26 | no |
| bastion | -8.6 | -0.00 | no |
| bramblehide | -26.2 | +0.01 | yes |
| brixa | +4.9 | -0.05 | no |
| corvane | +1.7 | +0.02 | no |
| dax | +22.2 | +0.13 | no |
| grivven | +2.4 | +0.36 | no |
| kaelis | +9.6 | +0.04 | no |
| kestrel | -30.9 | +0.04 | yes |
| lumen | -4.9 | -0.00 | no |
| marrow | -10.5 | +0.04 | no |
| mossgrove | -0.0 | +0.02 | no |
| noctis | +6.4 | -0.05 | no |
| orrin | +3.7 | +0.02 | no |
| ossuar | +9.2 | +0.15 | no |
| pallas | +8.6 | +0.16 | no |
| quillan | +0.4 | +0.23 | no |
| rictus | +8.0 | +0.05 | no |
| sable | -5.2 | -0.14 | no |
| sylphine | +11.0 | -0.01 | no |
| thornjaw | +4.8 | +0.00 | no |
| vellum | +8.6 | +0.00 | no |
| veyra | -3.0 | -0.02 | no |
| vurmak | +2.3 | -0.02 | no |
| wisp | -2.6 | +0.14 | no |

- median length delta: +1.0
- nexus-kill rate delta: -2.0 pts
