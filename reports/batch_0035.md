# Sim report batch_0035

## 1. Header

| field | value |
|---|---|
| rules | 1.6.0 |
| roster | 1.6.0 |
| ai | 1.2.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 120 |
| seed | 3501 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 3985.7s |
| engine tests | not run |
| generated | 2026-09-23 03:46:59 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 7 FAIL / 18 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 51/58 abilities outside the band; roster mean 20.2%; 12 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 46.7% [38.0, 55.6] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 16.0 [15.0, 16.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 97.5% [92.9, 99.1] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.53 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 51.7% [42.8, 60.4] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 84.8 [71.8, 92.4] | 46 | 5.89 | 2.33 | 2% | 86% | 0% | 7% | 0.07 | 0.37 | 0.7 | 0.0 | 31% | bootsx46, cloth_armorx46, longbowx46 |
| bastion | 81.0 [66.7, 90.0] | 42 | 2.50 | 0.99 | 91% | 0% | 0% | 3% | 0.36 | 0.05 | 0.1 | 0.5 | 14% | cloth_armorx42, ionian_charmx42, long_swordx42 |
| sable | 72.2 [59.1, 82.4] | 54 | 6.30 | 2.50 | 1% | 58% | 0% | 36% | 0.09 | 0.20 | 0.3 | 1.2 | 35% | ionian_charmx54, long_swordx54, longbowx54 |
| ashwyn | 70.8 [56.8, 81.8] | 48 | 5.76 | 2.28 | 2% | 75% | 0% | 15% | 0.08 | 0.33 | 0.7 | 0.0 | 32% | ionian_charmx48, long_swordx48, longbowx48 |
| pallas | 67.9 [54.8, 78.6] | 56 | 4.51 | 1.78 | 4% | 0% | 0% | 89% | 0.04 | 0.48 | 0.9 | 4.3 | 24% | bootsx56, cloth_armorx56, longbowx56 |
| dax | 61.4 [46.6, 74.3] | 44 | 1.52 | 0.60 | 9% | 49% | 1% | 13% | 0.27 | 0.27 | 0.5 | 1.2 | 9% | long_swordx44, longbowx44, vampiric_bladex44 |
| bramblehide | 58.3 [45.7, 69.9] | 60 | 2.05 | 0.81 | 4% | 27% | 0% | 30% | 0.08 | 0.20 | 0.3 | 3.6 | 13% | long_swordx60, ruby_crystalx60, vampiric_bladex60 |
| marrow | 56.0 [42.3, 68.8] | 50 | 2.81 | 1.11 | 5% | 1% | 0% | 47% | 0.08 | 0.04 | 0.1 | 0.0 | 18% | long_swordx50, ruby_crystalx50, cloth_armorx49 |
| thornjaw | 52.9 [36.7, 68.5] | 34 | 1.48 | 0.58 | 14% | 5% | 3% | 1% | 0.12 | 0.09 | 0.1 | 0.1 | 9% | long_swordx34, ruby_crystalx34, vampiric_bladex34 |
| vurmak | 52.9 [36.7, 68.5] | 34 | 1.59 | 0.63 | 15% | 3% | 0% | 54% | 0.15 | 0.21 | 0.5 | 4.1 | 10% | ruby_crystalx34, long_swordx33, cloth_armorx32 |
| kestrel | 50.0 [36.1, 63.9] | 46 | 1.90 | 0.75 | 61% | 9% | 0% | 24% | 0.20 | 0.04 | 0.1 | 4.1 | 12% | long_swordx46, longbowx46, vampiric_bladex46 |
| mossgrove | 50.0 [36.9, 63.1] | 52 | 1.30 | 0.51 | 35% | 0% | 0% | 8% | 0.08 | 0.13 | 0.2 | 3.9 | 8% | bootsx52, long_swordx52, ruby_crystalx52 |
| orrin | 48.2 [35.7, 61.0] | 56 | 1.87 | 0.74 | 8% | 38% | 0% | 0% | 0.12 | 0.18 | 0.3 | 0.0 | 11% | bootsx56, long_swordx56, longbowx56 |
| rictus | 48.2 [35.7, 61.0] | 56 | 1.32 | 0.52 | 14% | 5% | 32% | 0% | 0.14 | 0.41 | 0.6 | 2.3 | 8% | long_swordx56, ruby_crystalx56, vampiric_bladex54 |
| brixa | 47.8 [34.1, 61.9] | 46 | 1.58 | 0.62 | 43% | 3% | 5% | 2% | 0.11 | 0.22 | 0.3 | 0.5 | 10% | long_swordx46, longbowx46, vampiric_bladex46 |
| kaelis | 46.0 [33.0, 59.6] | 50 | 1.33 | 0.53 | 22% | 4% | 3% | 12% | 0.20 | 0.14 | 0.3 | 1.2 | 9% | cloth_armorx50, long_swordx50, ruby_crystalx50 |
| veyra | 43.8 [30.7, 57.7] | 48 | 1.53 | 0.61 | 2% | 73% | 0% | 7% | 0.17 | 0.33 | 0.7 | 1.4 | 10% | long_swordx48, longbowx48, vampiric_bladex47 |
| quillan | 42.9 [29.1, 57.8] | 42 | 5.39 | 2.13 | 6% | 11% | 0% | 75% | 0.07 | 0.33 | 0.8 | 0.0 | 32% | bootsx42, ionian_charmx42, long_swordx42 |
| grivven | 37.0 [24.5, 51.4] | 46 | 2.63 | 1.04 | 6% | 0% | 0% | 76% | 0.02 | 0.26 | 0.6 | 8.5 | 17% | bootsx46, cloth_armorx46, longbowx46 |
| sylphine | 36.8 [23.4, 52.7] | 38 | 1.48 | 0.59 | 14% | 2% | 0% | 8% | 0.13 | 0.08 | 0.1 | 0.0 | 9% | long_swordx38, ruby_crystalx38, vampiric_bladex38 |
| noctis | 32.7 [21.5, 46.2] | 52 | 1.70 | 0.67 | 73% | 0% | 16% | 0% | 0.04 | 0.42 | 0.8 | 0.0 | 13% | ionian_charmx52, longbowx52, ruby_crystalx52 |
| corvane | 32.6 [20.9, 47.0] | 46 | 0.59 | 0.24 | 55% | 0% | 0% | 1% | 0.11 | 0.15 | 0.4 | 3.7 | 4% | longbowx46, ruby_crystalx46, bootsx45 |
| vellum | 27.3 [16.3, 41.8] | 44 | 2.81 | 1.11 | 5% | 0% | 0% | 81% | 0.07 | 0.48 | 1.0 | 2.8 | 19% | ionian_charmx44, longbowx44, ruby_crystalx42 |
| ossuar | 26.6 [17.3, 38.5] | 64 | 2.42 | 0.96 | 7% | 4% | 0% | 64% | 0.09 | 0.08 | 0.2 | 4.6 | 15% | cloth_armorx64, long_swordx64, ruby_crystalx64 |
| lumen | 23.9 [13.9, 37.9] | 46 | 0.88 | 0.35 | 67% | 1% | 0% | 1% | 0.07 | 0.02 | 0.0 | 0.1 | 7% | longbowx46, ruby_crystalx46, bootsx45 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.69 |
| Jungle | 50.0 [43.7, 56.3] | 1.55 |
| Mid | 50.0 [43.7, 56.3] | 4.40 |
| Support | 50.0 [43.7, 56.3] | 2.97 |
| Top | 50.0 [43.7, 56.3] | 2.17 |

## 5. Games

- length: median 16.0, p10 12, p90 18
- end reasons: {'nexus': 117, 'round_limit_hp': 1, 'round_limit_towers': 2} (draws 0)
- priority win rate: 46.7% [38.0, 55.6]
- north win rate: 51.7% [42.8, 60.4]
- length histogram: {9: 2, 10: 1, 11: 5, 12: 6, 13: 12, 14: 17, 15: 15, 16: 27, 17: 17, 18: 7, 19: 7, 20: 4}

## 6. Objectives

- takes per game: {'dragon': 1.9333333333333333, 'baron': 0.8916666666666667}
- median round taken: dragon 9.0, baron 11
- win rate when secured: {'dragon': 51.293103448275865, 'baron': 45.794392523364486}
- camp clears per game: {'raptors': 6.758333333333334, 'wolves': 6.283333333333333, 'krugs': 6.241666666666666, 'dragon': 1.9333333333333333, 'red_buff': 3.9166666666666665, 'blue_buff': 3.933333333333333, 'baron': 0.8916666666666667}

## 7. Structures

- first tower falls: median round 6.0, p10 4, p90 8
- games with at least one tower down: 100.0%
- first-tower win rate: 63.3%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 4.90 |
| chips_monster | 3.99 |
| chips_wave | 3.66 |
| base | 3.43 |
| blue_buff | 0.26 |
| red_buff | 0.15 |
| champion_kill | 0.07 |

| use | AP |
|---|---|
| shop | 11.70 |
| abilities | 2.55 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.98 | 54.1% | 6.7% | +47.4 |
| cloth_armor | 5 | 1.98 | 55.5% | 37.9% | +17.6 |
| control_ward | 2 | 1.23 | - | 50.0% | - |
| frost_charm | 2 | 1.14 | - | 50.0% | - |
| health_potion | 2 | 1.99 | - | 50.0% | - |
| ionian_charm | 8 | 2.00 | 55.7% | 8.3% | +47.5 |
| long_sword | 6 | 2.00 | 50.5% | 48.0% | +2.5 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 50.5% | 0.0% | +50.5 |
| stopwatch | 3 | 1.98 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.99 | 52.5% | 42.9% | +9.6 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 68.04 per game
- that is 54.8% of all ability uses
- activations ending beside an enemy-held hexgroup (looking in): 66.4%


## 10. Anomalies

- ILLEGAL[activation r5]: stacking: n_mid_T2 and w13 on: 1 games
- ILLEGAL[activation r9]: stacking: s_mid_T2 and w26 on: 1 games

## 11. Top 5 flags (evidence only)

1. **anomaly: ILLEGAL[activation r5]: stacking: n_mid_T2 and w13 on** - 1 games
2. **anomaly: ILLEGAL[activation r9]: stacking: s_mid_T2 and w26 on** - 1 games
3. **champion win rate: wisp** - WR 84.8% [71.8, 92.4]
4. **champion win rate: bastion** - WR 81.0% [66.7, 90.0]
5. **champion win rate: lumen** - WR 23.9% [13.9, 37.9]

## 12. Delta vs batch_0034

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -4.2 | +0.12 | no |
| bastion | +21.6 | +0.07 | no |
| bramblehide | +10.4 | -0.08 | no |
| brixa | -4.2 | +0.01 | no |
| corvane | +20.1 | +0.07 | no |
| dax | +7.9 | -0.03 | no |
| grivven | -24.2 | -0.10 | no |
| kaelis | +0.5 | +0.05 | no |
| kestrel | -2.6 | -0.04 | no |
| lumen | -1.1 | +0.00 | no |
| marrow | -0.5 | +0.07 | no |
| mossgrove | +7.5 | +0.00 | no |
| noctis | -8.0 | +0.05 | no |
| orrin | -1.8 | +0.07 | no |
| ossuar | -2.3 | -0.03 | no |
| pallas | +2.9 | +0.01 | no |
| quillan | +1.6 | +0.15 | no |
| rictus | +4.1 | +0.02 | no |
| sable | +7.9 | -0.09 | no |
| sylphine | -27.4 | +0.04 | no |
| thornjaw | +6.2 | +0.04 | no |
| vellum | -1.0 | -0.08 | no |
| veyra | +1.4 | +0.08 | no |
| vurmak | -8.8 | -0.03 | no |
| wisp | +0.8 | -0.10 | no |

- median length delta: +0.0
- nexus-kill rate delta: -0.8 pts
