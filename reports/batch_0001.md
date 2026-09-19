# Sim report batch_0001

## 1. Header

| field | value |
|---|---|
| rules | 1.0.0 |
| roster | 1.0.0 |
| ai | 1.0.0 |
| matchup | T0_random vs T0_random (temperature 1.0) |
| games | 200 |
| seed | 424242 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 105.3s |
| engine tests | 78 passed in 25.30s |
| generated | 2026-09-19 05:57:21 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 10 INCONCLUSIVE of 10 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 26/26 abilities outside the band; roster mean 3.1%; 0 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 68.3% [61.6, 74.4] | **FAIL** |
| Median game length 13-18 rounds | 20.0 [20.0, 20.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 0.0% [0.0, 1.9] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | none (roster mean 0.75 AP/round) | **PASS** |
| North vs South win rate 48-52% | north 46.2% [39.4, 53.2] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vurmak | 53.8 [46.8, 60.6] | 199 | 0.78 | 1.04 | 3% | 2% | 3% | 3% | 0.03 | 3.13 | 6.2 | 0.8 | 10% | bootsx155, ruby_crystalx148, cloth_armorx134 |
| ashwyn | 51.8 [44.8, 58.6] | 199 | 0.74 | 0.99 | 4% | 1% | 6% | 4% | 0.03 | 3.61 | 7.0 | 0.9 | 9% | ruby_crystalx158, bootsx157, vampiric_bladex135 |
| lumen | 51.8 [44.8, 58.6] | 199 | 0.73 | 0.97 | 3% | 1% | 1% | 2% | 0.03 | 3.84 | 7.1 | 0.3 | 9% | bootsx154, ruby_crystalx152, cloth_armorx137 |
| kestrel | 50.8 [43.9, 57.6] | 199 | 0.76 | 1.01 | 5% | 4% | 4% | 3% | 0.01 | 3.12 | 6.4 | 1.1 | 9% | ruby_crystalx158, bootsx156, vampiric_bladex138 |
| mossgrove | 50.8 [43.9, 57.6] | 199 | 0.73 | 0.97 | 2% | 5% | 3% | 3% | 0.02 | 3.20 | 6.3 | 0.8 | 9% | bootsx158, ruby_crystalx157, vampiric_bladex143 |
| dax | 49.2 [42.4, 56.1] | 199 | 0.75 | 0.99 | 6% | 3% | 4% | 6% | 0.07 | 3.35 | 6.8 | 1.0 | 9% | ruby_crystalx161, bootsx160, cloth_armorx137 |
| thornjaw | 49.2 [42.4, 56.1] | 199 | 0.75 | 1.00 | 3% | 4% | 2% | 1% | 0.05 | 3.83 | 7.3 | 0.3 | 10% | bootsx159, ruby_crystalx157, cloth_armorx132 |
| grivven | 48.2 [41.4, 55.2] | 199 | 0.73 | 0.97 | 4% | 4% | 1% | 1% | 0.02 | 3.15 | 6.3 | 1.2 | 9% | ruby_crystalx162, bootsx157, vampiric_bladex132 |
| vellum | 48.2 [41.4, 55.2] | 199 | 0.78 | 1.04 | 5% | 2% | 4% | 3% | 0.07 | 3.00 | 6.0 | 1.1 | 10% | ruby_crystalx167, bootsx156, cloth_armorx150 |
| bastion | 46.2 [39.4, 53.2] | 199 | 0.76 | 1.01 | 4% | 8% | 4% | 1% | 0.06 | 2.63 | 5.3 | 0.7 | 10% | ruby_crystalx163, bootsx153, cloth_armorx142 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [45.1, 54.9] | 0.75 |
| Jungle | 50.0 [45.1, 54.9] | 0.74 |
| Mid | 50.0 [45.1, 54.9] | 0.76 |
| Support | 50.0 [45.1, 54.9] | 0.73 |
| Top | 50.0 [45.1, 54.9] | 0.77 |

## 5. Games

- length: median 20.0, p10 20, p90 20
- end reasons: {'round_limit_towers': 131, 'round_limit_hp': 65, 'round_limit_kills': 3, 'round_limit_draw': 1} (draws 1)
- priority win rate: 68.3% [61.6, 74.4]
- north win rate: 46.2% [39.4, 53.2]
- length histogram: {20: 200}

## 6. Objectives

- takes per game: {'dragon': 1.455, 'baron': 0.895}
- median round taken: dragon 12, baron 17
- win rate when secured: {'dragon': 65.86206896551724, 'baron': 71.91011235955057}
- camp clears per game: {'wolves': 12.305, 'krugs': 13.02, 'raptors': 12.925, 'red_buff': 6.06, 'blue_buff': 5.99, 'dragon': 1.455, 'baron': 0.895}

## 7. Structures

- first tower falls: median round 17, p10 13, p90 20
- games with at least one tower down: 76.5%
- first-tower win rate: 92.8%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| base | 3.24 |
| chips_wave | 3.20 |
| champion_kill | 0.77 |
| chips_monster | 0.34 |
| blue_buff | 0.20 |
| red_buff | 0.16 |
| chips_structure | 0.06 |

| use | AP |
|---|---|
| shop | 7.32 |
| abilities | 0.36 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 51.1% | 46.2% | +4.9 |
| cloth_armor | 5 | 1.97 | 54.3% | 41.3% | +13.0 |
| control_ward | 2 | 1.99 | - | 50.0% | - |
| frost_charm | 2 | 1.99 | - | 50.0% | - |
| health_potion | 2 | 1.99 | - | 50.0% | - |
| ionian_charm | 8 | 1.75 | 54.2% | 47.8% | +6.5 |
| long_sword | 6 | 2.00 | 54.6% | 44.1% | +10.5 |
| longbow | 6 | 1.98 | 52.2% | 47.0% | +5.1 |
| ruby_crystal | 4 | 2.00 | 51.0% | 46.4% | +4.6 |
| stopwatch | 3 | 1.88 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 52.1% | 46.0% | +6.1 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **Priority (first player) win rate 48-52%** - 68.3% [61.6, 74.4]
2. **Median game length 13-18 rounds** - 20.0 [20.0, 20.0]
3. **>=95% of games end by Nexus kill before round 20** - 0.0% [0.0, 1.9]
4. **ability usage: ashwyn.W** - used in 1.2% of affordable rounds with a legal target
5. **ability usage: ashwyn.R** - used in 4.1% of affordable rounds with a legal target
