# Sim report batch_0058

## 1. Header

| field | value |
|---|---|
| rules | 1.8.0 |
| roster | 1.8.0 |
| ai | 1.5.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 2000 |
| seed | 5701 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 0.7s |
| engine tests | not run |
| generated | 2026-09-27 19:16:17 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 15 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 50/58 abilities outside the band; roster mean 14.0%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 50.0% [47.8, 52.1] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 12.0 [12.0, 12.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 100.0% [99.8, 100.0] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, vellum (roster mean 1.07 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.4% [46.2, 50.5] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bastion | 57.8 [54.3, 61.2] | 784 | 1.08 | 1.01 | 52% | 1% | 0% | 7% | 0.18 | 0.18 | 0.5 | 1.2 | 11% | ruby_crystalx784, long_swordx776, cloth_armorx706 |
| wisp | 56.4 [52.9, 59.9] | 766 | 1.51 | 1.41 | 8% | 61% | 2% | 3% | 0.12 | 0.55 | 1.4 | 3.9 | 15% | longbowx764, ruby_crystalx738, bootsx499 |
| pallas | 54.9 [51.6, 58.2] | 856 | 1.35 | 1.26 | 6% | 1% | 2% | 69% | 0.11 | 0.45 | 1.1 | 4.2 | 13% | longbowx854, ruby_crystalx851, bootsx671 |
| bramblehide | 54.5 [50.9, 58.0] | 762 | 1.04 | 0.97 | 1% | 13% | 1% | 20% | 0.14 | 0.31 | 0.8 | 2.5 | 10% | long_swordx762, ruby_crystalx761, vampiric_bladex630 |
| brixa | 52.6 [49.2, 56.0] | 834 | 0.72 | 0.67 | 18% | 3% | 6% | 1% | 0.23 | 0.55 | 1.4 | 0.6 | 7% | long_swordx834, longbowx790, vampiric_bladex665 |
| thornjaw | 52.1 [48.5, 55.5] | 780 | 0.60 | 0.56 | 14% | 4% | 1% | 3% | 0.19 | 0.39 | 1.1 | 0.1 | 6% | long_swordx772, ruby_crystalx753, vampiric_bladex425 |
| lumen | 51.8 [48.3, 55.3] | 786 | 0.50 | 0.47 | 44% | 1% | 0% | 1% | 0.18 | 0.31 | 0.7 | 0.1 | 5% | longbowx785, ruby_crystalx779, bootsx585 |
| quillan | 51.7 [48.3, 55.2] | 804 | 1.73 | 1.61 | 9% | 9% | 1% | 59% | 0.11 | 0.61 | 1.6 | 2.8 | 18% | longbowx802, ionian_charmx697, ruby_crystalx558 |
| noctis | 51.5 [48.2, 54.9] | 840 | 1.15 | 1.07 | 68% | 0% | 12% | 2% | 0.40 | 0.45 | 1.1 | 0.2 | 12% | longbowx836, ionian_charmx742, ruby_crystalx620 |
| ossuar | 50.5 [47.0, 54.0] | 772 | 1.55 | 1.44 | 39% | 1% | 0% | 32% | 0.18 | 0.15 | 0.4 | 2.6 | 15% | ruby_crystalx772, long_swordx742, cloth_armorx567 |
| vellum | 50.3 [46.7, 53.8] | 750 | 1.69 | 1.57 | 3% | 0% | 4% | 65% | 0.23 | 0.43 | 1.2 | 3.3 | 17% | longbowx738, ionian_charmx594, ruby_crystalx461 |
| kestrel | 49.9 [46.5, 53.2] | 856 | 1.20 | 1.12 | 53% | 7% | 1% | 6% | 0.32 | 0.32 | 0.9 | 1.0 | 12% | long_swordx856, longbowx830, vampiric_bladex678 |
| veyra | 49.6 [46.0, 53.2] | 736 | 1.01 | 0.94 | 1% | 59% | 0% | 2% | 0.35 | 0.48 | 1.3 | 0.3 | 10% | long_swordx736, longbowx678, vampiric_bladex451 |
| vurmak | 49.3 [45.9, 52.6] | 852 | 0.90 | 0.84 | 23% | 6% | 1% | 24% | 0.34 | 0.23 | 0.6 | 2.1 | 9% | ruby_crystalx852, long_swordx723, cloth_armorx399 |
| dax | 49.1 [45.6, 52.6] | 792 | 0.84 | 0.78 | 13% | 25% | 3% | 3% | 0.28 | 0.47 | 1.3 | 0.6 | 9% | long_swordx792, longbowx767, vampiric_bladex620 |
| mossgrove | 48.7 [45.3, 52.1] | 838 | 0.67 | 0.62 | 21% | 2% | 1% | 4% | 0.18 | 0.33 | 0.9 | 2.3 | 7% | long_swordx838, ruby_crystalx827, vampiric_bladex577 |
| orrin | 48.6 [45.1, 52.1] | 782 | 0.77 | 0.72 | 4% | 15% | 1% | 0% | 0.21 | 0.64 | 1.6 | 0.0 | 8% | long_swordx780, longbowx726, vampiric_bladex500 |
| sylphine | 48.5 [45.0, 52.1] | 752 | 0.64 | 0.60 | 12% | 3% | 0% | 11% | 0.17 | 0.27 | 0.7 | 0.0 | 7% | long_swordx748, ruby_crystalx737, vampiric_bladex403 |
| ashwyn | 48.5 [45.0, 52.0] | 790 | 1.82 | 1.69 | 5% | 52% | 1% | 21% | 0.21 | 0.66 | 1.6 | 2.0 | 18% | longbowx790, ionian_charmx764, ruby_crystalx709 |
| sable | 47.9 [44.5, 51.3] | 816 | 2.10 | 1.95 | 3% | 41% | 0% | 39% | 0.10 | 0.21 | 0.6 | 3.7 | 21% | longbowx815, ionian_charmx696, ruby_crystalx558 |
| kaelis | 47.6 [44.2, 51.1] | 800 | 0.54 | 0.50 | 26% | 3% | 7% | 5% | 0.17 | 0.27 | 0.8 | 0.5 | 6% | ruby_crystalx800, long_swordx745, cloth_armorx579 |
| rictus | 46.8 [43.5, 50.1] | 868 | 0.67 | 0.63 | 13% | 4% | 20% | 2% | 0.24 | 0.64 | 1.6 | 1.8 | 7% | long_swordx866, ruby_crystalx852, vampiric_bladex530 |
| marrow | 44.9 [41.5, 48.4] | 792 | 1.33 | 1.24 | 6% | 1% | 0% | 45% | 0.08 | 0.20 | 0.5 | 3.4 | 13% | ruby_crystalx792, long_swordx749, cloth_armorx542 |
| grivven | 43.9 [40.5, 47.4] | 788 | 1.00 | 0.93 | 5% | 4% | 5% | 34% | 0.09 | 0.36 | 1.0 | 4.6 | 10% | longbowx788, ruby_crystalx784, bootsx679 |
| corvane | 42.9 [39.5, 46.4] | 804 | 0.41 | 0.38 | 48% | 0% | 0% | 3% | 0.26 | 0.53 | 1.3 | 0.6 | 4% | longbowx804, ruby_crystalx796, bootsx686 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [48.5, 51.5] | 0.91 |
| Jungle | 50.0 [48.5, 51.5] | 0.72 |
| Mid | 50.0 [48.5, 51.5] | 1.69 |
| Support | 50.0 [48.5, 51.5] | 0.96 |
| Top | 50.0 [48.5, 51.5] | 1.07 |

## 5. Games

- length: median 12.0, p10 9, p90 15
- end reasons: {'nexus': 2000} (draws 0)
- priority win rate: 50.0% [47.8, 52.1]
- north win rate: 48.4% [46.2, 50.5]
- length histogram: {5: 1, 6: 12, 7: 41, 8: 94, 9: 176, 10: 268, 11: 339, 12: 343, 13: 281, 14: 199, 15: 131, 16: 60, 17: 31, 18: 18, 19: 6}

## 6. Objectives

- takes per game: {'dragon': 1.0575, 'baron': 0.099}
- median round taken: dragon 6, baron 12.0
- win rate when secured: {'dragon': 47.84869976359338, 'baron': 47.97979797979798}
- camp clears per game: {'red_buff': 1.963, 'krugs': 3.8245, 'raptors': 4.1485, 'blue_buff': 2.099, 'wolves': 4.0725, 'dragon': 1.0575, 'baron': 0.099}

## 7. Structures

- first tower falls: median round 4.0, p10 3, p90 7
- games with at least one tower down: 100.0%
- first-tower win rate: 64.4%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.05 |
| base | 3.00 |
| chips_wave | 2.10 |
| tower_kill | 0.77 |
| champion_kill | 0.48 |
| blue_buff | 0.18 |
| dragon | 0.14 |
| red_buff | 0.09 |

| use | AP |
|---|---|
| shop | 7.87 |
| abilities | 1.51 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.56 | 49.0% | 50.4% | -1.4 |
| cloth_armor | 5 | 1.40 | 48.7% | 50.3% | -1.6 |
| control_ward | 2 | 0.01 | - | 50.0% | - |
| frost_charm | 2 | 0.00 | - | 50.0% | - |
| health_potion | 2 | 1.80 | - | 50.0% | - |
| ionian_charm | 8 | 1.75 | 48.1% | 50.5% | -2.4 |
| long_sword | 6 | 2.00 | 49.9% | 50.2% | -0.3 |
| longbow | 6 | 2.00 | 49.7% | 50.4% | -0.7 |
| ruby_crystal | 4 | 2.00 | 49.5% | 52.2% | -2.7 |
| stopwatch | 3 | 1.73 | - | 50.0% | - |
| swift_tonic | 1 | 1.95 | - | 50.0% | - |
| vampiric_blade | 5 | 1.57 | 48.3% | 50.9% | -2.6 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 2000 | 60.2 [58.1, 62.4] |
| SM_g2_lane6 | 2000 | 39.8 [37.6, 41.9] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| T2_sieger | 2000 | 60.2 [58.1, 62.4] |  | - | - |
| SM_g2_lane6 | 2000 | 39.8 [37.6, 41.9] |  | sieger 57%, laner 43% | 1.0 |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 30.25 per game
- that is 36.5% of all ability uses
- of which true snipes (from cover, two or more hexes away): 32.6% of all uses
- snipes aimed at a champion: 3.7 per game
- activations ending beside an enemy-held hexgroup (looking in): 62.9%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **Median game length 13-18 rounds** - 12.0 [12.0, 12.0]
2. **ability usage: ashwyn.R** - used in 21.4% of affordable rounds with a legal target
3. **ability usage: bastion.W** - used in 0.7% of affordable rounds with a legal target
4. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
5. **ability usage: bastion.R** - used in 6.5% of affordable rounds with a legal target
