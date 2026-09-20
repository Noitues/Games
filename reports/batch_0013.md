# Sim report batch_0013

## 1. Header

| field | value |
|---|---|
| rules | 1.1.0 |
| roster | 1.2.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 1202 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 825.5s |
| engine tests | not run |
| generated | 2026-09-20 10:38:30 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 3 FAIL / 22 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 56/56 abilities outside the band; roster mean 11.5%; 0 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 59.1% [51.0, 66.6] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 20.0 [20.0, 20.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 0.7% [0.1, 3.7] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan (roster mean 0.74 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 32.2% [25.2, 40.1] | **FAIL** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 84.4 [73.6, 91.3] | 64 | 3.18 | 4.30 | 12% | 50% | 7% | 11% | 0.16 | 0.69 | 1.7 | 1.5 | 35% | longbowx64, ruby_crystalx64, ionian_charmx62 |
| mossgrove | 67.5 [52.0, 79.9] | 40 | 0.39 | 0.53 | 12% | 37% | 3% | 5% | 0.07 | 0.10 | 0.2 | 3.2 | 6% | ruby_crystalx40, long_swordx38, vampiric_bladex37 |
| kestrel | 67.3 [54.1, 78.2] | 55 | 1.05 | 1.42 | 39% | 14% | 17% | 4% | 0.25 | 0.05 | 0.1 | 1.3 | 14% | long_swordx56, vampiric_bladex55, longbowx49 |
| wisp | 64.8 [51.5, 76.2] | 54 | 1.03 | 1.40 | 30% | 15% | 7% | 14% | 0.13 | 0.43 | 1.0 | 0.0 | 13% | ruby_crystalx54, bootsx53, longbowx52 |
| bastion | 58.6 [45.8, 70.4] | 58 | 0.69 | 0.94 | 31% | 14% | 1% | 2% | 0.17 | 0.05 | 0.2 | 0.7 | 10% | ruby_crystalx58, cloth_armorx56, long_swordx49 |
| veyra | 56.2 [42.3, 69.3] | 48 | 0.58 | 0.79 | 18% | 15% | 18% | 9% | 0.04 | 0.21 | 0.4 | 2.8 | 9% | long_swordx39, longbowx33, ruby_crystalx33 |
| quillan | 56.0 [42.3, 68.8] | 50 | 1.67 | 2.26 | 25% | 7% | 13% | 25% | 0.08 | 0.52 | 1.4 | 2.4 | 22% | ruby_crystalx49, longbowx44, ionian_charmx38 |
| corvane | 55.1 [43.4, 66.2] | 69 | 0.21 | 0.29 | 23% | 4% | 22% | 3% | 0.12 | 0.30 | 0.6 | 6.3 | 3% | bootsx70, ruby_crystalx70, longbowx68 |
| dax | 52.2 [40.5, 63.7] | 67 | 0.83 | 1.12 | 29% | 17% | 4% | 12% | 0.13 | 0.19 | 0.5 | 2.6 | 12% | long_swordx67, vampiric_bladex64, ruby_crystalx63 |
| kaelis | 51.6 [39.4, 63.6] | 62 | 0.49 | 0.66 | 26% | 14% | 12% | 4% | 0.16 | 0.13 | 0.3 | 0.8 | 7% | ruby_crystalx62, cloth_armorx57, long_swordx44 |
| marrow | 50.9 [38.3, 63.4] | 57 | 0.26 | 0.35 | 11% | 7% | 24% | 4% | 0.02 | 0.07 | 0.2 | 3.6 | 4% | ruby_crystalx58, cloth_armorx47, long_swordx34 |
| thornjaw | 50.8 [38.6, 62.9] | 61 | 0.57 | 0.78 | 11% | 25% | 7% | 4% | 0.07 | 0.36 | 0.9 | 1.2 | 8% | ruby_crystalx62, long_swordx56, bootsx46 |
| ossuar | 49.2 [37.1, 61.4] | 61 | 0.45 | 0.61 | 20% | 11% | 16% | 10% | 0.05 | 0.07 | 0.2 | 4.0 | 7% | ruby_crystalx62, cloth_armorx56, long_swordx39 |
| bramblehide | 47.3 [34.7, 60.2] | 55 | 0.76 | 1.03 | 12% | 22% | 4% | 2% | 0.11 | 0.07 | 0.2 | 4.0 | 11% | long_swordx56, ruby_crystalx56, vampiric_bladex55 |
| sylphine | 47.1 [35.9, 58.7] | 70 | 0.29 | 0.40 | 6% | 6% | 21% | 16% | 0.04 | 0.09 | 0.2 | 3.4 | 4% | ruby_crystalx69, long_swordx54, vampiric_bladex48 |
| grivven | 46.6 [34.3, 59.2] | 58 | 0.44 | 0.60 | 32% | 11% | 3% | 7% | 0.10 | 0.14 | 0.4 | 6.9 | 7% | ruby_crystalx58, bootsx57, longbowx56 |
| noctis | 45.5 [34.0, 57.4] | 66 | 0.78 | 1.06 | 38% | 15% | 12% | 3% | 0.17 | 0.26 | 0.6 | 2.5 | 12% | ruby_crystalx65, longbowx64, ionian_charmx41 |
| rictus | 44.4 [33.5, 55.9] | 72 | 0.64 | 0.87 | 19% | 29% | 9% | 3% | 0.18 | 0.28 | 0.6 | 1.8 | 9% | ruby_crystalx72, long_swordx67, vampiric_bladex58 |
| brixa | 44.1 [32.9, 55.9] | 68 | 0.64 | 0.87 | 11% | 13% | 14% | 14% | 0.19 | 0.18 | 0.4 | 2.2 | 9% | long_swordx68, vampiric_bladex64, ruby_crystalx56 |
| lumen | 42.6 [30.3, 55.8] | 54 | 0.41 | 0.56 | 33% | 6% | 3% | 6% | 0.17 | 0.15 | 0.3 | 1.4 | 6% | bootsx54, ruby_crystalx54, longbowx51 |
| pallas | 41.3 [30.0, 53.6] | 63 | 0.68 | 0.92 | 20% | 10% | 6% | 16% | 0.16 | 0.35 | 0.8 | 2.5 | 10% | ruby_crystalx64, bootsx63, longbowx57 |
| vurmak | 40.0 [28.6, 52.6] | 60 | 0.61 | 0.83 | 15% | 22% | 5% | 16% | 0.27 | 0.07 | 0.1 | 3.2 | 9% | ruby_crystalx60, cloth_armorx46, long_swordx38 |
| orrin | 33.3 [22.7, 45.9] | 60 | 0.37 | 0.50 | 19% | 7% | 26% | 4% | 0.10 | 0.32 | 0.7 | 1.8 | 6% | long_swordx54, vampiric_bladex48, ruby_crystalx42 |
| vellum | 32.2 [21.7, 44.9] | 59 | 0.62 | 0.84 | 21% | 0% | 27% | 18% | 0.08 | 0.27 | 0.7 | 2.4 | 10% | ruby_crystalx55, longbowx42, ionian_charmx22 |
| sable | 30.5 [20.3, 43.1] | 59 | 0.79 | 1.07 | 32% | 11% | 2% | 8% | 0.12 | 0.08 | 0.3 | 2.9 | 12% | ruby_crystalx58, longbowx46, ionian_charmx20 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 0.70 |
| Jungle | 50.0 [44.4, 55.6] | 0.54 |
| Mid | 50.0 [44.4, 55.6] | 1.41 |
| Support | 50.0 [44.4, 55.6] | 0.54 |
| Top | 50.0 [44.4, 55.6] | 0.50 |

## 5. Games

- length: median 20.0, p10 20, p90 20
- end reasons: {'round_limit_towers': 110, 'round_limit_hp': 38, 'round_limit_draw': 1, 'nexus': 1} (draws 1)
- priority win rate: 59.1% [51.0, 66.6]
- north win rate: 32.2% [25.2, 40.1]
- length histogram: {18: 1, 20: 149}

## 6. Objectives

- takes per game: {'dragon': 0.9733333333333334, 'baron': 0.4666666666666667}
- median round taken: dragon 14.5, baron 17.0
- win rate when secured: {'dragon': 55.172413793103445, 'baron': 50.72463768115942}
- camp clears per game: {'raptors': 4.78, 'wolves': 4.3133333333333335, 'red_buff': 2.8333333333333335, 'krugs': 4.633333333333334, 'blue_buff': 3.06, 'dragon': 0.9733333333333334, 'baron': 0.4666666666666667}

## 7. Structures

- first tower falls: median round 15.0, p10 8, p90 19
- games with at least one tower down: 81.3%
- first-tower win rate: 93.4%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| base | 3.15 |
| chips_monster | 2.17 |
| chips_wave | 1.00 |
| chips_structure | 0.42 |
| blue_buff | 0.15 |
| red_buff | 0.10 |
| champion_kill | 0.04 |

| use | AP |
|---|---|
| shop | 5.66 |
| abilities | 1.35 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.98 | 57.7% | 41.3% | +16.4 |
| cloth_armor | 5 | 1.75 | 64.1% | 43.7% | +20.3 |
| control_ward | 2 | 0.11 | - | 50.0% | - |
| frost_charm | 2 | 0.04 | - | 50.0% | - |
| health_potion | 2 | 1.97 | - | 50.0% | - |
| ionian_charm | 8 | 1.22 | 79.6% | 41.3% | +38.4 |
| long_sword | 6 | 1.95 | 58.9% | 37.8% | +21.1 |
| longbow | 6 | 1.91 | 55.9% | 43.9% | +11.9 |
| ruby_crystal | 4 | 2.00 | 50.9% | 30.8% | +20.1 |
| stopwatch | 3 | 1.98 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 1.81 | 60.1% | 42.0% | +18.1 |

## 10. Anomalies

- ILLEGAL[activation r18]: stacking: n_rictus and n_ossuar on: 1 games
- ILLEGAL[world r18]: stacking: n_rictus and n_ossuar on: 1 games
- ILLEGAL[upkeep r19]: stacking: n_rictus and n_ossuar on: 1 games
- ILLEGAL[activation r19]: stacking: n_rictus and n_ossuar on: 1 games
- ILLEGAL[activation r8]: stacking: n_pallas and n_kaelis on: 1 games
- ILLEGAL[world r8]: stacking: n_pallas and n_kaelis on: 1 games
- ILLEGAL[activation r11]: stacking: s_corvane and s_ossuar on: 1 games
- ILLEGAL[activation r16]: stacking: s_vellum and s_bastion on: 1 games
- ILLEGAL[activation r17]: stacking: n_dax and n_rictus on: 1 games
- ILLEGAL[activation r13]: stacking: s_ashwyn and s_bramblehide on: 1 games
- ILLEGAL[world r13]: stacking: s_ashwyn and s_bramblehide on: 1 games
- ILLEGAL[activation r16]: stacking: s_brixa and s_thornjaw on: 1 games
- ILLEGAL[activation r18]: stacking: n_corvane and n_ashwyn on: 1 games
- ILLEGAL[world r18]: stacking: n_corvane and n_ashwyn on: 1 games

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 3.18 AP/round = 4.30x roster mean
2. **anomaly: ILLEGAL[activation r18]: stacking: n_rictus and n_ossuar on** - 1 games
3. **anomaly: ILLEGAL[world r18]: stacking: n_rictus and n_ossuar on** - 1 games
4. **anomaly: ILLEGAL[upkeep r19]: stacking: n_rictus and n_ossuar on** - 1 games
5. **anomaly: ILLEGAL[activation r19]: stacking: n_rictus and n_ossuar on** - 1 games

## 12. Delta vs batch_0012

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -0.2 | -0.03 | no |
| bastion | +14.0 | -0.03 | no |
| bramblehide | -10.3 | +0.01 | no |
| brixa | +3.1 | -0.02 | no |
| corvane | +8.4 | -0.03 | no |
| dax | -13.8 | -0.02 | no |
| grivven | -8.4 | -0.01 | no |
| kaelis | -0.3 | -0.09 | no |
| kestrel | +14.3 | -0.03 | no |
| lumen | -4.9 | -0.02 | no |
| marrow | -2.0 | +0.01 | no |
| mossgrove | +25.1 | +0.04 | no |
| noctis | +8.2 | -0.06 | no |
| orrin | -0.6 | +0.01 | no |
| ossuar | +2.0 | +0.06 | no |
| pallas | -12.2 | +0.03 | no |
| quillan | -6.1 | -0.17 | no |
| rictus | -8.2 | -0.06 | no |
| sable | -2.8 | -0.09 | no |
| sylphine | -0.0 | -0.02 | no |
| thornjaw | +2.9 | -0.04 | no |
| vellum | -1.8 | +0.03 | no |
| veyra | -0.1 | -0.09 | no |
| vurmak | -14.4 | -0.04 | no |
| wisp | +17.6 | +0.03 | no |

- median length delta: +0.0
- nexus-kill rate delta: +0.0 pts
