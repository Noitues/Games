# Sim report batch_0036

## 1. Header

| field | value |
|---|---|
| rules | 1.6.0 |
| roster | 1.6.0 |
| ai | 1.3.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 8 |
| seed | 3601 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 533.3s |
| engine tests | not run |
| generated | 2026-09-23 02:39:02 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 23 INCONCLUSIVE of 23 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 47/53 abilities outside the band; roster mean 20.6%; 10 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 75.0% [40.9, 92.9] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 12.5 [12.0, 18.0] | **INCONCLUSIVE** |
| >=95% of games end by Nexus kill before round 20 | 75.0% [40.9, 92.9] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.65 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 50.0% [21.5, 78.5] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kaelis | 100.0 [34.2, 100.0] | 2 | 1.43 | 0.54 | 20% | 8% | 0% | 12% | 0.00 | 0.50 | 1.0 | 1.5 | 10% | cloth_armorx2, ionian_charmx2, long_swordx2 |
| rictus | 100.0 [34.2, 100.0] | 2 | 0.94 | 0.35 | 21% | 5% | 37% | 0% | 0.00 | 1.50 | 3.0 | 2.5 | 7% | bootsx2, long_swordx2, ruby_crystalx2 |
| sable | 100.0 [34.2, 100.0] | 2 | 4.98 | 1.88 | 12% | 40% | 0% | 36% | 0.00 | 0.00 | 0.0 | 2.0 | 36% | bootsx2, ionian_charmx2, long_swordx2 |
| kestrel | 75.0 [30.1, 95.4] | 4 | 2.06 | 0.78 | 48% | 9% | 0% | 32% | 0.00 | 0.00 | 0.0 | 5.8 | 14% | bootsx4, long_swordx4, longbowx4 |
| lumen | 75.0 [30.1, 95.4] | 4 | 0.91 | 0.34 | 67% | 0% | 0% | 3% | 0.00 | 0.25 | 0.5 | 0.2 | 6% | bootsx4, cloth_armorx4, ionian_charmx4 |
| mossgrove | 75.0 [30.1, 95.4] | 4 | 1.27 | 0.48 | 45% | 0% | 2% | 4% | 0.00 | 0.00 | 0.0 | 3.8 | 8% | bootsx4, cloth_armorx4, ionian_charmx4 |
| orrin | 75.0 [30.1, 95.4] | 4 | 1.80 | 0.68 | 7% | 20% | 0% | 4% | 0.00 | 0.00 | 0.0 | 0.2 | 10% | bootsx4, long_swordx4, longbowx4 |
| ossuar | 75.0 [30.1, 95.4] | 4 | 2.58 | 0.98 | 0% | 0% | 0% | 69% | 0.00 | 0.00 | 0.0 | 5.5 | 16% | bootsx4, cloth_armorx4, ionian_charmx4 |
| wisp | 75.0 [30.1, 95.4] | 4 | 5.51 | 2.08 | 2% | 89% | 0% | 7% | 0.00 | 0.25 | 0.2 | 0.0 | 30% | bootsx4, cloth_armorx4, ionian_charmx4 |
| ashwyn | 50.0 [18.8, 81.2] | 6 | 6.18 | 2.33 | 1% | 73% | 0% | 20% | 0.17 | 0.17 | 0.3 | 0.0 | 33% | bootsx6, cloth_armorx6, ionian_charmx6 |
| bastion | 50.0 [9.5, 90.5] | 2 | 2.82 | 1.07 | 100% | 0% | 0% | 0% | 0.00 | 0.00 | 0.0 | 0.0 | 15% | bootsx2, cloth_armorx2, ionian_charmx2 |
| dax | 50.0 [15.0, 85.0] | 4 | 1.50 | 0.57 | 16% | 35% | 0% | 12% | 0.00 | 0.00 | 0.0 | 1.5 | 9% | bootsx4, long_swordx4, longbowx4 |
| marrow | 50.0 [9.5, 90.5] | 2 | 2.70 | 1.02 | 10% | 0% | 0% | 52% | 0.00 | 0.00 | 0.0 | 0.0 | 21% | bootsx2, cloth_armorx2, ionian_charmx2 |
| noctis | 50.0 [9.5, 90.5] | 2 | 1.80 | 0.68 | 68% | 0% | 20% | 0% | 0.00 | 0.00 | 0.0 | 0.0 | 14% | bootsx2, cloth_armorx2, ionian_charmx2 |
| thornjaw | 50.0 [9.5, 90.5] | 2 | 1.08 | 0.41 | 10% | 2% | 0% | 0% | 0.00 | 0.00 | 0.0 | 0.0 | 8% | bootsx2, cloth_armorx2, ionian_charmx2 |
| vellum | 50.0 [15.0, 85.0] | 4 | 3.24 | 1.22 | 4% | 0% | 0% | 85% | 0.00 | 0.25 | 0.8 | 2.8 | 19% | bootsx4, ionian_charmx4, long_swordx4 |
| bramblehide | 25.0 [4.6, 69.9] | 4 | 2.03 | 0.77 | 6% | 23% | 0% | 33% | 0.25 | 0.25 | 0.2 | 3.0 | 10% | bootsx4, ionian_charmx4, long_swordx4 |
| grivven | 25.0 [4.6, 69.9] | 4 | 2.77 | 1.04 | 0% | 0% | 0% | 68% | 0.00 | 0.00 | 0.0 | 8.8 | 18% | bootsx4, cloth_armorx4, ionian_charmx4 |
| pallas | 25.0 [4.6, 69.9] | 4 | 4.68 | 1.77 | 3% | 0% | 0% | 90% | 0.00 | 0.00 | 0.0 | 4.2 | 23% | bootsx4, cloth_armorx4, ionian_charmx4 |
| sylphine | 25.0 [4.6, 69.9] | 4 | 1.54 | 0.58 | 8% | 2% | 0% | 15% | 0.00 | 0.00 | 0.0 | 0.0 | 8% | bootsx4, ionian_charmx4, long_swordx4 |
| vurmak | 16.7 [3.0, 56.4] | 6 | 1.74 | 0.66 | 21% | 0% | 0% | 52% | 0.00 | 0.00 | 0.0 | 3.3 | 9% | cloth_armorx6, ionian_charmx6, long_swordx6 |
| quillan | 0.0 [0.0, 65.8] | 2 | 5.58 | 2.11 | 8% | 4% | 0% | 71% | 0.00 | 0.00 | 0.0 | 0.0 | 27% | bootsx2, cloth_armorx2, ionian_charmx2 |
| veyra | 0.0 [0.0, 49.0] | 4 | 1.79 | 0.68 | 0% | 83% | 0% | 2% | 0.00 | 0.00 | 0.0 | 0.2 | 9% | bootsx4, ionian_charmx4, long_swordx4 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [28.0, 72.0] | 1.79 |
| Jungle | 50.0 [28.0, 72.0] | 1.46 |
| Mid | 50.0 [28.0, 72.0] | 4.67 |
| Support | 50.0 [28.0, 72.0] | 3.47 |
| Top | 50.0 [28.0, 72.0] | 2.17 |

## 5. Games

- length: median 12.5, p10 12, p90 20
- end reasons: {'nexus': 6, 'round_limit_towers': 1, 'round_limit_hp': 1} (draws 0)
- priority win rate: 75.0% [40.9, 92.9]
- north win rate: 50.0% [21.5, 78.5]
- length histogram: {11: 1, 12: 3, 13: 1, 16: 1, 20: 2}

## 6. Objectives

- takes per game: {'dragon': 2.125, 'baron': 0.875}
- median round taken: dragon 9, baron 10
- win rate when secured: {'dragon': 23.529411764705884, 'baron': 28.571428571428573}
- camp clears per game: {'raptors': 6.25, 'krugs': 6.25, 'wolves': 6.375, 'red_buff': 3.75, 'blue_buff': 3.75, 'dragon': 2.125, 'baron': 0.875}

## 7. Structures

- first tower falls: median round 5.0, p10 4, p90 6
- games with at least one tower down: 100.0%
- first-tower win rate: 50.0%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_structure | 5.18 |
| chips_monster | 4.05 |
| chips_wave | 3.66 |
| base | 3.44 |
| blue_buff | 0.26 |
| red_buff | 0.19 |
| champion_kill | 0.03 |

| use | AP |
|---|---|
| shop | 12.64 |
| abilities | 2.83 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 48.7% | 100.0% | -51.3 |
| cloth_armor | 5 | 2.00 | 49.1% | 52.2% | -3.1 |
| control_ward | 2 | 1.25 | - | 50.0% | - |
| frost_charm | 2 | 1.00 | - | 50.0% | - |
| health_potion | 2 | 1.88 | - | 50.0% | - |
| ionian_charm | 8 | 2.00 | 49.3% | 60.0% | -10.7 |
| long_sword | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| longbow | 6 | 2.00 | 50.0% | 50.0% | +0.0 |
| ruby_crystal | 4 | 2.00 | 50.0% | - | - |
| stopwatch | 3 | 1.75 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 48.3% | 54.5% | -6.3 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 4 | 100.0 [51.0, 100.0] |
| T2_brawler | 2 | 50.0 [9.5, 90.5] |
| T2_warder | 4 | 50.0 [15.0, 85.0] |
| T2_objective | 4 | 25.0 [4.6, 69.9] |
| T2_laner | 2 | 0.0 [0.0, 65.8] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 71.50 per game
- that is 63.3% of all ability uses
- activations ending beside an enemy-held hexgroup (looking in): 55.7%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **>=95% of games end by Nexus kill before round 20** - 75.0% [40.9, 92.9]
2. **economy outlier: ashwyn** - 6.18 AP/round = 2.33x roster mean
3. **ability usage: ashwyn.R** - used in 20.3% of affordable rounds with a legal target
4. **ability usage: bastion.W** - used in 0.0% of affordable rounds with a legal target
5. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
