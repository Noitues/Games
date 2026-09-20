# Sim report batch_0019

## 1. Header

| field | value |
|---|---|
| rules | 1.1.0 |
| roster | 1.2.0 |
| ai | 1.2.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 150 |
| seed | 1802 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 440.1s |
| engine tests | not run |
| generated | 2026-09-20 17:49:55 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 5 FAIL / 20 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 51/56 abilities outside the band; roster mean 18.0%; 5 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 52.7% [44.7, 60.5] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 13.0 [12.0, 14.0] | **INCONCLUSIVE** |
| >=95% of games end by Nexus kill before round 20 | 96.7% [92.4, 98.6] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.50 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.0% [40.2, 55.9] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 77.3 [65.8, 85.7] | 66 | 9.77 | 3.91 | 2% | 87% | 0% | 6% | 0.05 | 0.02 | 0.0 | 0.1 | 49% | bootsx66, cloth_armorx66, ionian_charmx66 |
| wisp | 75.0 [62.8, 84.2] | 60 | 6.40 | 2.56 | 10% | 69% | 1% | 9% | 0.00 | 0.00 | 0.0 | 0.0 | 34% | bootsx60, longbowx60, ruby_crystalx60 |
| vurmak | 67.9 [54.8, 78.6] | 56 | 1.37 | 0.55 | 19% | 6% | 2% | 40% | 0.00 | 0.02 | 0.0 | 3.4 | 9% | ruby_crystalx56, long_swordx55, cloth_armorx54 |
| quillan | 66.7 [54.1, 77.3] | 60 | 7.92 | 3.17 | 3% | 3% | 1% | 85% | 0.00 | 0.03 | 0.1 | 2.5 | 43% | ionian_charmx60, longbowx60, ruby_crystalx60 |
| pallas | 63.0 [49.6, 74.6] | 54 | 4.78 | 1.91 | 8% | 1% | 1% | 83% | 0.00 | 0.02 | 0.0 | 4.1 | 28% | longbowx54, ruby_crystalx54, bootsx51 |
| rictus | 62.5 [51.0, 72.8] | 72 | 1.01 | 0.40 | 19% | 21% | 19% | 1% | 0.00 | 0.03 | 0.1 | 1.7 | 6% | long_swordx72, ruby_crystalx72, vampiric_bladex70 |
| dax | 60.7 [47.6, 72.4] | 56 | 1.19 | 0.48 | 19% | 27% | 4% | 18% | 0.02 | 0.00 | 0.0 | 1.9 | 8% | long_swordx56, longbowx55, vampiric_bladex53 |
| brixa | 60.6 [48.5, 71.5] | 66 | 1.22 | 0.49 | 29% | 11% | 10% | 9% | 0.00 | 0.06 | 0.1 | 1.0 | 7% | long_swordx66, longbowx66, vampiric_bladex66 |
| mossgrove | 58.9 [45.9, 70.8] | 56 | 0.91 | 0.36 | 26% | 15% | 1% | 9% | 0.02 | 0.04 | 0.1 | 3.2 | 5% | long_swordx56, ruby_crystalx56, vampiric_bladex55 |
| sable | 53.8 [40.5, 66.7] | 52 | 6.16 | 2.47 | 5% | 56% | 0% | 26% | 0.00 | 0.00 | 0.0 | 2.8 | 38% | longbowx52, ionian_charmx51, ruby_crystalx51 |
| marrow | 51.9 [38.7, 64.9] | 52 | 1.50 | 0.60 | 13% | 3% | 13% | 18% | 0.00 | 0.00 | 0.0 | 1.1 | 9% | cloth_armorx52, long_swordx52, ruby_crystalx52 |
| ossuar | 51.4 [40.1, 62.6] | 72 | 2.04 | 0.82 | 15% | 10% | 3% | 40% | 0.03 | 0.00 | 0.0 | 3.3 | 13% | ruby_crystalx72, long_swordx70, cloth_armorx69 |
| grivven | 48.5 [36.8, 60.3] | 66 | 2.85 | 1.14 | 17% | 3% | 1% | 59% | 0.00 | 0.02 | 0.0 | 7.1 | 19% | bootsx66, longbowx66, ruby_crystalx66 |
| bramblehide | 48.0 [34.8, 61.5] | 50 | 1.95 | 0.78 | 7% | 25% | 2% | 29% | 0.04 | 0.00 | 0.0 | 3.1 | 13% | long_swordx50, ruby_crystalx50, vampiric_bladex48 |
| kestrel | 47.9 [34.5, 61.7] | 48 | 1.90 | 0.76 | 46% | 16% | 4% | 21% | 0.06 | 0.00 | 0.0 | 3.1 | 13% | long_swordx48, longbowx48, vampiric_bladex48 |
| sylphine | 47.0 [35.4, 58.8] | 66 | 0.81 | 0.32 | 13% | 2% | 11% | 16% | 0.02 | 0.00 | 0.0 | 1.3 | 6% | long_swordx66, ruby_crystalx65, vampiric_bladex58 |
| bastion | 45.0 [33.1, 57.5] | 60 | 1.63 | 0.65 | 38% | 3% | 1% | 11% | 0.00 | 0.00 | 0.0 | 2.0 | 11% | long_swordx60, ruby_crystalx60, cloth_armorx59 |
| orrin | 41.0 [30.8, 52.1] | 78 | 0.88 | 0.35 | 18% | 19% | 11% | 6% | 0.00 | 0.10 | 0.2 | 2.1 | 6% | long_swordx78, longbowx75, vampiric_bladex69 |
| veyra | 40.4 [28.2, 53.9] | 52 | 1.04 | 0.42 | 12% | 34% | 7% | 17% | 0.04 | 0.00 | 0.0 | 2.8 | 7% | long_swordx52, longbowx50, vampiric_bladex45 |
| corvane | 40.0 [28.6, 52.6] | 60 | 0.44 | 0.18 | 40% | 2% | 9% | 2% | 0.00 | 0.07 | 0.1 | 3.6 | 3% | longbowx60, ruby_crystalx60, bootsx59 |
| vellum | 38.5 [26.5, 52.0] | 52 | 2.82 | 1.13 | 13% | 1% | 7% | 66% | 0.00 | 0.00 | 0.0 | 2.7 | 21% | longbowx52, ionian_charmx49, ruby_crystalx44 |
| kaelis | 35.0 [24.2, 47.6] | 60 | 0.94 | 0.38 | 23% | 17% | 3% | 11% | 0.00 | 0.00 | 0.0 | 1.0 | 7% | ruby_crystalx60, long_swordx57, cloth_armorx54 |
| thornjaw | 30.4 [19.9, 43.3] | 56 | 0.95 | 0.38 | 15% | 14% | 10% | 4% | 0.02 | 0.02 | 0.1 | 1.1 | 7% | long_swordx56, ruby_crystalx56, vampiric_bladex50 |
| lumen | 25.0 [15.8, 37.2] | 60 | 0.62 | 0.25 | 36% | 4% | 1% | 4% | 0.03 | 0.00 | 0.0 | 0.6 | 5% | longbowx60, ruby_crystalx60, bootsx54 |
| noctis | 15.7 [9.0, 26.0] | 70 | 1.37 | 0.55 | 49% | 6% | 20% | 0% | 0.01 | 0.03 | 0.1 | 0.5 | 13% | longbowx70, ionian_charmx65, ruby_crystalx60 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [44.4, 55.6] | 1.20 |
| Jungle | 50.0 [44.4, 55.6] | 1.09 |
| Mid | 50.0 [44.4, 55.6] | 5.61 |
| Support | 50.0 [44.4, 55.6] | 2.98 |
| Top | 50.0 [44.4, 55.6] | 1.52 |

## 5. Games

- length: median 13.0, p10 10, p90 17
- end reasons: {'nexus': 145, 'round_limit_towers': 5} (draws 0)
- priority win rate: 52.7% [44.7, 60.5]
- north win rate: 48.0% [40.2, 55.9]
- length histogram: {7: 1, 9: 8, 10: 18, 11: 20, 12: 20, 13: 18, 14: 19, 15: 17, 16: 8, 17: 11, 18: 2, 19: 1, 20: 7}

## 6. Objectives

- takes per game: {'dragon': 1.7133333333333334, 'baron': 0.7133333333333334}
- median round taken: dragon 8, baron 11
- win rate when secured: {'dragon': 44.3579766536965, 'baron': 39.25233644859813}
- camp clears per game: {'wolves': 5.82, 'red_buff': 3.96, 'blue_buff': 3.88, 'raptors': 6.34, 'krugs': 6.333333333333333, 'dragon': 1.7133333333333334, 'baron': 0.7133333333333334}

## 7. Structures

- first tower falls: median round 4.0, p10 3, p90 6
- games with at least one tower down: 100.0%
- first-tower win rate: 76.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.27 |
| chips_wave | 3.89 |
| chips_structure | 3.74 |
| base | 3.33 |
| blue_buff | 0.29 |
| red_buff | 0.23 |
| champion_kill | 0.01 |

| use | AP |
|---|---|
| shop | 11.86 |
| abilities | 2.09 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.93 | 61.0% | 6.6% | +54.5 |
| cloth_armor | 5 | 1.92 | 62.9% | 31.3% | +31.6 |
| control_ward | 2 | 0.94 | - | 50.0% | - |
| frost_charm | 2 | 0.77 | - | 50.0% | - |
| health_potion | 2 | 1.91 | - | 50.0% | - |
| ionian_charm | 8 | 1.94 | 64.0% | 10.4% | +53.6 |
| long_sword | 6 | 2.00 | 52.4% | 42.3% | +10.1 |
| longbow | 6 | 2.00 | 50.3% | 49.5% | +0.8 |
| ruby_crystal | 4 | 2.00 | 51.9% | 0.0% | +51.9 |
| stopwatch | 3 | 1.91 | - | 50.0% | - |
| swift_tonic | 1 | 1.95 | - | 50.0% | - |
| vampiric_blade | 5 | 1.91 | 58.4% | 33.7% | +24.7 |

## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 76.38 per game
- that is 84.4% of all ability uses


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 9.77 AP/round = 3.91x roster mean
2. **champion win rate: noctis** - WR 15.7% [9.0, 26.0]
3. **economy outlier: quillan** - 7.92 AP/round = 3.17x roster mean
4. **champion win rate: ashwyn** - WR 77.3% [65.8, 85.7]
5. **champion win rate: lumen** - WR 25.0% [15.8, 37.2]

## 12. Delta vs batch_0016

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -10.2 | +0.26 | no |
| bastion | -6.8 | +0.11 | no |
| bramblehide | -2.0 | -0.04 | no |
| brixa | +26.0 | +0.09 | no |
| corvane | +18.3 | +0.07 | no |
| dax | +7.9 | -0.01 | no |
| grivven | +16.9 | +0.14 | no |
| kaelis | +4.4 | +0.08 | no |
| kestrel | -21.0 | +0.04 | no |
| lumen | -25.0 | -0.07 | no |
| marrow | +3.3 | -0.08 | no |
| mossgrove | +11.9 | +0.14 | no |
| noctis | -10.4 | +0.11 | no |
| orrin | +4.8 | +0.02 | no |
| ossuar | -6.9 | +0.10 | no |
| pallas | -9.0 | +0.18 | no |
| quillan | +4.2 | +0.12 | no |
| rictus | +8.9 | -0.02 | no |
| sable | +15.9 | +0.33 | no |
| sylphine | -4.6 | +0.03 | no |
| thornjaw | -17.9 | -0.03 | no |
| vellum | +2.7 | +0.22 | no |
| veyra | -14.6 | +0.05 | no |
| vurmak | +16.3 | +0.10 | no |
| wisp | -8.3 | +0.20 | no |

- median length delta: +2.0
- nexus-kill rate delta: -0.7 pts
