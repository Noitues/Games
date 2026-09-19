# Sim report batch_0002

## 1. Header

| field | value |
|---|---|
| rules | 1.0.0 |
| roster | 1.0.0 |
| ai | 1.0.0 |
| matchup | T1_greedy vs T1_greedy (temperature 0.3) |
| games | 200 |
| seed | 424242 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 268.6s |
| engine tests | 78 passed in 25.39s |
| generated | 2026-09-19 06:02:15 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 2 FAIL / 8 INCONCLUSIVE of 10 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 20/26 abilities outside the band; roster mean 26.1%; 1 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 59.0% [52.1, 65.6] | **FAIL** |
| Median game length 13-18 rounds | 15.0 [14.0, 15.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 99.5% [97.2, 99.9] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn (roster mean 1.92 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 46.0% [39.2, 52.9] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 88.0 [82.8, 91.8] | 200 | 7.81 | 4.07 | 1% | 82% | 0% | 13% | 1.78 | 1.53 | 2.8 | 0.3 | 46% | ionian_charmx200, long_swordx200, longbowx200 |
| grivven | 58.0 [51.1, 64.6] | 200 | 1.92 | 1.00 | 25% | 5% | 1% | 52% | 0.46 | 1.31 | 2.8 | 6.2 | 14% | longbowx200, ruby_crystalx200, bootsx197 |
| dax | 53.0 [46.1, 59.8] | 200 | 0.99 | 0.52 | 13% | 20% | 4% | 44% | 0.35 | 1.22 | 2.2 | 3.5 | 7% | long_swordx200, vampiric_bladex173, longbowx171 |
| mossgrove | 51.0 [44.1, 57.8] | 200 | 0.55 | 0.29 | 14% | 20% | 7% | 28% | 0.33 | 1.16 | 2.2 | 4.5 | 4% | ruby_crystalx198, long_swordx197, vampiric_bladex159 |
| vurmak | 51.0 [44.1, 57.8] | 200 | 0.95 | 0.49 | 15% | 5% | 6% | 47% | 0.45 | 1.41 | 2.6 | 3.9 | 7% | ruby_crystalx200, long_swordx163, cloth_armorx140 |
| bastion | 49.0 [42.2, 55.9] | 200 | 1.95 | 1.02 | 10% | 16% | 1% | 45% | 0.79 | 1.05 | 2.0 | 5.1 | 14% | ruby_crystalx200, long_swordx186, cloth_armorx183 |
| thornjaw | 49.0 [42.2, 55.9] | 200 | 0.71 | 0.37 | 26% | 13% | 13% | 9% | 0.36 | 1.38 | 2.5 | 1.8 | 5% | ruby_crystalx198, long_swordx197, vampiric_bladex159 |
| kestrel | 47.0 [40.2, 53.9] | 200 | 1.77 | 0.92 | 8% | 15% | 1% | 64% | 0.66 | 1.32 | 2.4 | 6.3 | 14% | long_swordx200, longbowx189, vampiric_bladex172 |
| lumen | 42.0 [35.4, 48.9] | 200 | 0.33 | 0.17 | 47% | 5% | 3% | 22% | 0.24 | 0.74 | 1.5 | 2.2 | 3% | ruby_crystalx200, longbowx198, bootsx170 |
| vellum | 12.0 [8.2, 17.2] | 200 | 2.19 | 1.14 | 7% | 1% | 2% | 79% | 0.77 | 1.85 | 3.4 | 3.6 | 21% | longbowx183, ruby_crystalx137, ionian_charmx120 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [45.1, 54.9] | 1.38 |
| Jungle | 50.0 [45.1, 54.9] | 0.63 |
| Mid | 50.0 [45.1, 54.9] | 5.00 |
| Support | 50.0 [45.1, 54.9] | 1.13 |
| Top | 50.0 [45.1, 54.9] | 1.45 |

## 5. Games

- length: median 15.0, p10 12, p90 18
- end reasons: {'nexus': 199, 'round_limit_towers': 1} (draws 0)
- priority win rate: 59.0% [52.1, 65.6]
- north win rate: 46.0% [39.2, 52.9]
- length histogram: {8: 1, 9: 2, 10: 2, 11: 7, 12: 22, 13: 36, 14: 27, 15: 28, 16: 31, 17: 21, 18: 11, 19: 8, 20: 4}

## 6. Objectives

- takes per game: {'dragon': 2.025, 'baron': 0.945}
- median round taken: dragon 9, baron 11
- win rate when secured: {'dragon': 57.03703703703704, 'baron': 58.73015873015873}
- camp clears per game: {'wolves': 8.9, 'krugs': 9.625, 'raptors': 9.56, 'blue_buff': 5.265, 'red_buff': 5.46, 'dragon': 2.025, 'baron': 0.945}

## 7. Structures

- first tower falls: median round 3.0, p10 2, p90 5
- games with at least one tower down: 100.0%
- first-tower win rate: 67.5%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.44 |
| base | 3.44 |
| chips_wave | 3.26 |
| chips_structure | 2.66 |
| champion_kill | 0.38 |
| blue_buff | 0.35 |
| red_buff | 0.23 |

| use | AP |
|---|---|
| shop | 9.62 |
| abilities | 3.35 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.83 | 69.5% | 8.7% | +60.8 |
| cloth_armor | 5 | 1.61 | 73.0% | 28.4% | +44.6 |
| control_ward | 2 | 0.47 | - | 50.0% | - |
| frost_charm | 2 | 0.36 | - | 50.0% | - |
| health_potion | 2 | 1.92 | - | 50.0% | - |
| ionian_charm | 8 | 1.60 | 75.8% | 12.8% | +63.0 |
| long_sword | 6 | 2.00 | 56.5% | 34.4% | +22.2 |
| longbow | 6 | 1.99 | 52.6% | 46.6% | +6.0 |
| ruby_crystal | 4 | 2.00 | 54.4% | 0.0% | +54.4 |
| stopwatch | 3 | 1.95 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.73 | 66.6% | 28.2% | +38.4 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 7.81 AP/round = 4.07x roster mean
2. **champion win rate: ashwyn** - WR 88.0% [82.8, 91.8]
3. **champion win rate: vellum** - WR 12.0% [8.2, 17.2]
4. **Priority (first player) win rate 48-52%** - 59.0% [52.1, 65.6]
5. **ability usage: ashwyn.R** - used in 12.9% of affordable rounds with a legal target

## 12. Delta vs batch_0001

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +36.2 | +7.06 | yes |
| bastion | +2.8 | +1.19 | no |
| dax | +3.8 | +0.24 | no |
| grivven | +9.8 | +1.19 | no |
| kestrel | -3.8 | +1.01 | no |
| lumen | -9.8 | -0.40 | no |
| mossgrove | +0.2 | -0.18 | no |
| thornjaw | -0.2 | -0.04 | no |
| vellum | -36.2 | +1.41 | yes |
| vurmak | -2.8 | +0.17 | no |

- median length delta: -5.0
- nexus-kill rate delta: +99.5 pts
