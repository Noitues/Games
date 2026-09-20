# Sim report batch_0012

## 1. Header

| field | value |
|---|---|
| rules | 1.1.0 |
| roster | 1.2.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 1201 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 836.5s |
| engine tests | 104 passed in 107.21s (0:01:47) |
| generated | 2026-09-20 10:24:44 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 1 FAIL / 24 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 56/56 abilities outside the band; roster mean 11.1%; 0 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 59.3% [51.2, 67.0] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 20.0 [20.0, 20.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 0.7% [0.1, 3.7] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan (roster mean 0.76 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 35.9% [28.5, 43.9] | **FAIL** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 84.6 [72.5, 92.0] | 52 | 3.20 | 4.19 | 11% | 49% | 6% | 11% | 0.15 | 0.19 | 0.4 | 1.5 | 37% | ionian_charmx54, longbowx54, ruby_crystalx54 |
| dax | 66.0 [52.6, 77.3] | 53 | 0.85 | 1.11 | 29% | 17% | 4% | 13% | 0.02 | 0.08 | 0.2 | 2.8 | 11% | long_swordx54, vampiric_bladex54, longbowx52 |
| quillan | 62.1 [50.1, 72.9] | 66 | 1.84 | 2.41 | 25% | 6% | 12% | 27% | 0.05 | 0.11 | 0.3 | 2.7 | 24% | longbowx66, ruby_crystalx66, ionian_charmx59 |
| bramblehide | 57.5 [46.1, 68.2] | 73 | 0.75 | 0.98 | 11% | 21% | 3% | 2% | 0.07 | 0.10 | 0.2 | 3.7 | 11% | ruby_crystalx76, long_swordx75, vampiric_bladex75 |
| veyra | 56.4 [43.3, 68.6] | 55 | 0.67 | 0.88 | 20% | 20% | 16% | 6% | 0.04 | 0.04 | 0.1 | 2.1 | 11% | ruby_crystalx41, long_swordx38, vampiric_bladex37 |
| grivven | 55.0 [42.5, 66.9] | 60 | 0.45 | 0.59 | 31% | 8% | 3% | 7% | 0.02 | 0.08 | 0.2 | 6.6 | 7% | bootsx60, ruby_crystalx60, longbowx59 |
| vurmak | 54.4 [41.6, 66.6] | 57 | 0.66 | 0.86 | 14% | 22% | 4% | 15% | 0.04 | 0.04 | 0.1 | 2.7 | 9% | ruby_crystalx58, cloth_armorx47, long_swordx45 |
| pallas | 53.4 [40.8, 65.7] | 58 | 0.65 | 0.85 | 25% | 8% | 7% | 14% | 0.00 | 0.05 | 0.2 | 2.1 | 10% | bootsx62, ruby_crystalx62, longbowx59 |
| kestrel | 52.9 [41.2, 64.3] | 68 | 1.08 | 1.41 | 39% | 14% | 16% | 4% | 0.06 | 0.03 | 0.1 | 1.0 | 15% | vampiric_bladex70, long_swordx69, longbowx68 |
| marrow | 52.8 [39.7, 65.6] | 53 | 0.25 | 0.32 | 12% | 5% | 27% | 3% | 0.02 | 0.00 | 0.0 | 4.5 | 4% | ruby_crystalx58, cloth_armorx50, long_swordx46 |
| rictus | 52.6 [39.9, 65.0] | 57 | 0.70 | 0.92 | 20% | 29% | 8% | 4% | 0.07 | 0.07 | 0.2 | 1.7 | 10% | ruby_crystalx58, long_swordx56, vampiric_bladex53 |
| kaelis | 51.9 [38.7, 64.9] | 52 | 0.58 | 0.76 | 25% | 15% | 12% | 4% | 0.04 | 0.02 | 0.0 | 0.6 | 8% | ruby_crystalx52, cloth_armorx48, long_swordx45 |
| thornjaw | 47.9 [34.5, 61.7] | 48 | 0.62 | 0.81 | 12% | 22% | 7% | 4% | 0.02 | 0.08 | 0.2 | 1.3 | 9% | ruby_crystalx50, long_swordx42, bootsx40 |
| lumen | 47.5 [35.3, 60.0] | 59 | 0.43 | 0.57 | 33% | 7% | 2% | 6% | 0.02 | 0.02 | 0.0 | 1.4 | 7% | ruby_crystalx62, bootsx61, longbowx59 |
| ossuar | 47.2 [36.1, 58.6] | 72 | 0.39 | 0.51 | 19% | 9% | 18% | 10% | 0.01 | 0.00 | 0.0 | 4.3 | 6% | ruby_crystalx74, cloth_armorx64, long_swordx46 |
| sylphine | 47.2 [34.4, 60.3] | 53 | 0.32 | 0.41 | 7% | 4% | 23% | 18% | 0.06 | 0.06 | 0.1 | 3.8 | 5% | ruby_crystalx56, vampiric_bladex46, long_swordx45 |
| wisp | 47.2 [34.4, 60.3] | 53 | 1.00 | 1.31 | 31% | 13% | 6% | 14% | 0.00 | 0.09 | 0.2 | 0.0 | 13% | ruby_crystalx54, bootsx53, longbowx52 |
| corvane | 46.7 [34.6, 59.1] | 60 | 0.25 | 0.32 | 26% | 3% | 20% | 1% | 0.00 | 0.17 | 0.4 | 6.5 | 4% | longbowx62, ruby_crystalx62, bootsx61 |
| bastion | 44.6 [32.4, 57.6] | 56 | 0.72 | 0.94 | 27% | 12% | 2% | 1% | 0.02 | 0.00 | 0.0 | 0.5 | 10% | ruby_crystalx58, cloth_armorx57, long_swordx50 |
| mossgrove | 42.4 [30.6, 55.1] | 59 | 0.35 | 0.46 | 10% | 37% | 3% | 4% | 0.05 | 0.02 | 0.1 | 2.8 | 5% | ruby_crystalx60, long_swordx54, vampiric_bladex50 |
| brixa | 41.0 [29.5, 53.5] | 61 | 0.66 | 0.87 | 9% | 13% | 12% | 16% | 0.08 | 0.16 | 0.3 | 2.1 | 10% | long_swordx62, vampiric_bladex54, ruby_crystalx49 |
| noctis | 37.3 [26.1, 50.0] | 59 | 0.84 | 1.10 | 38% | 14% | 11% | 3% | 0.03 | 0.08 | 0.2 | 2.2 | 13% | ruby_crystalx58, longbowx56, ionian_charmx37 |
| vellum | 34.0 [22.4, 47.8] | 50 | 0.59 | 0.77 | 20% | 2% | 30% | 15% | 0.02 | 0.04 | 0.0 | 2.1 | 10% | ruby_crystalx49, longbowx32, ionian_charmx15 |
| orrin | 34.0 [22.7, 47.4] | 53 | 0.36 | 0.48 | 19% | 7% | 27% | 4% | 0.04 | 0.11 | 0.2 | 1.9 | 6% | long_swordx51, vampiric_bladex43, ruby_crystalx42 |
| sable | 33.3 [22.9, 45.6] | 63 | 0.88 | 1.15 | 30% | 13% | 2% | 8% | 0.00 | 0.03 | 0.1 | 2.7 | 14% | ruby_crystalx64, longbowx53, ionian_charmx36 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.3, 55.7] | 0.74 |
| Jungle | 50.0 [44.3, 55.7] | 0.56 |
| Mid | 50.0 [44.3, 55.7] | 1.46 |
| Support | 50.0 [44.3, 55.7] | 0.55 |
| Top | 50.0 [44.3, 55.7] | 0.51 |

## 5. Games

- length: median 20.0, p10 20, p90 20
- end reasons: {'round_limit_towers': 101, 'round_limit_hp': 43, 'round_limit_draw': 5, 'nexus': 1} (draws 5)
- priority win rate: 59.3% [51.2, 67.0]
- north win rate: 35.9% [28.5, 43.9]
- length histogram: {20: 150}

## 6. Objectives

- takes per game: {'baron': 0.5266666666666666, 'dragon': 1.0733333333333333}
- median round taken: dragon 14, baron 17
- win rate when secured: {'baron': 59.49367088607595, 'dragon': 53.246753246753244}
- camp clears per game: {'blue_buff': 3.1666666666666665, 'krugs': 4.98, 'wolves': 4.56, 'raptors': 4.8533333333333335, 'red_buff': 2.98, 'baron': 0.5266666666666666, 'dragon': 1.0733333333333333}

## 7. Structures

- first tower falls: median round 15, p10 9, p90 19
- games with at least one tower down: 79.3%
- first-tower win rate: 90.5%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| base | 3.16 |
| chips_monster | 2.27 |
| chips_wave | 1.01 |
| chips_structure | 0.41 |
| blue_buff | 0.16 |
| red_buff | 0.12 |
| champion_kill | 0.01 |

| use | AP |
|---|---|
| shop | 5.84 |
| abilities | 1.28 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.98 | 55.7% | 41.8% | +14.0 |
| cloth_armor | 5 | 1.77 | 59.7% | 45.1% | +14.5 |
| control_ward | 2 | 0.20 | - | 50.0% | - |
| frost_charm | 2 | 0.03 | - | 50.0% | - |
| health_potion | 2 | 1.99 | - | 50.0% | - |
| ionian_charm | 8 | 1.34 | 70.4% | 43.7% | +26.6 |
| long_sword | 6 | 1.92 | 56.7% | 39.4% | +17.3 |
| longbow | 6 | 1.95 | 54.6% | 45.0% | +9.5 |
| ruby_crystal | 4 | 2.00 | 50.6% | 36.7% | +13.9 |
| stopwatch | 3 | 1.95 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.88 | 56.7% | 43.8% | +12.8 |

## 10. Anomalies

- ILLEGAL[activation r20]: stacking: w27 and w22 on: 1 games

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 3.20 AP/round = 4.19x roster mean
2. **anomaly: ILLEGAL[activation r20]: stacking: w27 and w22 on** - 1 games
3. **champion win rate: ashwyn** - WR 84.6% [72.5, 92.0]
4. **Median game length 13-18 rounds** - 20.0 [20.0, 20.0]
5. **>=95% of games end by Nexus kill before round 20** - 0.7% [0.1, 3.7]
