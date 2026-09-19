# Sim report batch_0003

## 1. Header

| field | value |
|---|---|
| rules | 1.0.0 |
| roster | 1.0.0 |
| ai | 1.0.0 |
| matchup | T1_greedy vs T0_random (temperature 0.3) |
| games | 100 |
| seed | 90210 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 94.0s |
| engine tests | 78 passed in 25.30s |
| generated | 2026-09-19 06:04:15 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 10 INCONCLUSIVE of 10 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 24/26 abilities outside the band; roster mean 15.8%; 1 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 100.0% [96.3, 100.0] | **FAIL** |
| Median game length 13-18 rounds | 13.5 [13.0, 14.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 92.0% [85.0, 95.9] | **INCONCLUSIVE** |
| No champion above 1.5x roster-mean AP per round | ashwyn (roster mean 1.53 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 50.0% [40.4, 59.6] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ashwyn | 62.0 [52.2, 70.9] | 100 | 5.53 | 3.62 | 3% | 55% | 3% | 12% | 0.65 | 1.74 | 3.3 | 0.6 | 30% | bootsx85, ruby_crystalx84, longbowx76 |
| kestrel | 60.0 [50.2, 69.1] | 100 | 1.43 | 0.94 | 5% | 13% | 4% | 35% | 0.37 | 1.41 | 2.5 | 4.7 | 11% | ruby_crystalx77, bootsx77, vampiric_bladex75 |
| bastion | 58.0 [48.2, 67.2] | 100 | 1.58 | 1.04 | 9% | 10% | 3% | 30% | 0.40 | 1.22 | 2.1 | 4.0 | 12% | vampiric_bladex78, ruby_crystalx76, bootsx75 |
| grivven | 54.0 [44.3, 63.4] | 100 | 1.55 | 1.01 | 13% | 4% | 1% | 26% | 0.33 | 1.67 | 3.1 | 3.9 | 11% | bootsx81, ruby_crystalx79, cloth_armorx67 |
| thornjaw | 54.0 [44.3, 63.4] | 100 | 0.76 | 0.49 | 16% | 10% | 9% | 7% | 0.15 | 1.64 | 2.8 | 1.2 | 7% | vampiric_bladex74, ruby_crystalx73, bootsx71 |
| lumen | 46.0 [36.6, 55.7] | 100 | 0.46 | 0.30 | 29% | 4% | 2% | 12% | 0.10 | 1.73 | 2.9 | 1.2 | 6% | ruby_crystalx75, bootsx70, cloth_armorx61 |
| mossgrove | 46.0 [36.6, 55.7] | 100 | 0.62 | 0.40 | 8% | 12% | 3% | 15% | 0.07 | 1.72 | 3.0 | 2.7 | 7% | bootsx75, ruby_crystalx70, vampiric_bladex68 |
| vurmak | 42.0 [32.8, 51.8] | 100 | 0.87 | 0.57 | 9% | 4% | 5% | 23% | 0.17 | 1.80 | 3.2 | 2.2 | 9% | ruby_crystalx75, cloth_armorx63, vampiric_bladex59 |
| dax | 40.0 [30.9, 49.8] | 100 | 0.83 | 0.54 | 9% | 13% | 4% | 25% | 0.12 | 1.86 | 3.2 | 2.2 | 9% | ruby_crystalx68, vampiric_bladex58, bootsx57 |
| vellum | 38.0 [29.1, 47.8] | 100 | 1.66 | 1.08 | 7% | 2% | 6% | 40% | 0.29 | 1.74 | 3.0 | 2.1 | 15% | ruby_crystalx61, bootsx52, long_swordx48 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.1, 56.9] | 1.13 |
| Jungle | 50.0 [43.1, 56.9] | 0.69 |
| Mid | 50.0 [43.1, 56.9] | 3.59 |
| Support | 50.0 [43.1, 56.9] | 1.01 |
| Top | 50.0 [43.1, 56.9] | 1.23 |

## 5. Games

- length: median 13.5, p10 12, p90 19
- end reasons: {'nexus': 92, 'round_limit_hp': 1, 'round_limit_towers': 7} (draws 0)
- priority win rate: 100.0% [96.3, 100.0]
- north win rate: 50.0% [40.4, 59.6]
- length histogram: {9: 1, 11: 9, 12: 19, 13: 21, 14: 13, 15: 10, 16: 6, 17: 4, 18: 4, 19: 4, 20: 9}

## 6. Objectives

- takes per game: {'dragon': 1.56, 'baron': 0.78}
- median round taken: dragon 8.0, baron 12.0
- win rate when secured: {'dragon': 92.3076923076923, 'baron': 91.02564102564102}
- camp clears per game: {'wolves': 8.69, 'raptors': 9.17, 'krugs': 9.2, 'blue_buff': 4.76, 'red_buff': 4.74, 'dragon': 1.56, 'baron': 0.78}

## 7. Structures

- first tower falls: median round 4.0, p10 3, p90 6
- games with at least one tower down: 100.0%
- first-tower win rate: 100.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| base | 3.32 |
| chips_wave | 2.93 |
| chips_monster | 2.43 |
| chips_structure | 1.85 |
| champion_kill | 0.52 |
| blue_buff | 0.30 |
| red_buff | 0.20 |

| use | AP |
|---|---|
| shop | 8.64 |
| abilities | 2.15 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.97 | 66.6% | 12.4% | +54.2 |
| cloth_armor | 5 | 1.84 | 65.0% | 34.6% | +30.4 |
| control_ward | 2 | 1.28 | - | 50.0% | - |
| frost_charm | 2 | 1.21 | - | 50.0% | - |
| health_potion | 2 | 1.82 | - | 50.0% | - |
| ionian_charm | 8 | 1.35 | 91.2% | 10.7% | +80.4 |
| long_sword | 6 | 1.73 | 78.0% | 20.5% | +57.4 |
| longbow | 6 | 1.70 | 73.3% | 33.8% | +39.5 |
| ruby_crystal | 4 | 1.92 | 67.8% | 0.0% | +67.8 |
| stopwatch | 3 | 1.65 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.94 | 66.5% | 28.5% | +38.0 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: ashwyn** - 5.53 AP/round = 3.62x roster mean
2. **Priority (first player) win rate 48-52%** - 100.0% [96.3, 100.0]
3. **ability usage: ashwyn.R** - used in 11.6% of affordable rounds with a legal target
4. **ability usage: bastion.W** - used in 10.3% of affordable rounds with a legal target
5. **ability usage: bastion.E** - used in 3.3% of affordable rounds with a legal target
