# Sim report batch_0053

## 1. Header

| field | value |
|---|---|
| rules | 1.8.0 |
| roster | 1.6.0 |
| ai | 1.3.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 120 |
| seed | 3801 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 4702.1s |
| engine tests | not run |
| generated | 2026-09-24 19:28:24 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 1 FAIL / 24 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 51/58 abilities outside the band; roster mean 16.2%; 6 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 47.9% [39.1, 56.8] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 20.0 [20.0, 20.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 39.2% [30.9, 48.1] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, marrow, quillan, sable, wisp (roster mean 1.55 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 51.3% [42.4, 60.1] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 72.7 [58.2, 83.7] | 44 | 2.71 | 1.75 | 7% | 5% | 0% | 74% | 0.14 | 0.77 | 2.1 | 0.0 | 23% | ionian_charmx44, longbowx44, ruby_crystalx43 |
| ashwyn | 61.5 [49.4, 72.4] | 65 | 2.48 | 1.60 | 5% | 64% | 0% | 17% | 0.28 | 0.94 | 2.8 | 0.0 | 21% | ionian_charmx66, longbowx66, ruby_crystalx66 |
| kaelis | 60.4 [46.3, 73.0] | 48 | 0.83 | 0.53 | 20% | 2% | 6% | 4% | 0.42 | 0.38 | 1.2 | 0.6 | 8% | long_swordx48, ruby_crystalx48, cloth_armorx47 |
| mossgrove | 58.8 [45.2, 71.2] | 51 | 0.98 | 0.64 | 24% | 3% | 0% | 3% | 0.25 | 0.51 | 1.7 | 3.1 | 9% | long_swordx52, ruby_crystalx52, vampiric_bladex52 |
| brixa | 58.7 [44.3, 71.7] | 46 | 1.08 | 0.69 | 26% | 2% | 7% | 1% | 0.37 | 0.46 | 1.4 | 0.7 | 9% | long_swordx46, vampiric_bladex46, longbowx45 |
| grivven | 58.7 [44.3, 71.7] | 46 | 1.12 | 0.72 | 7% | 4% | 5% | 43% | 0.02 | 0.57 | 1.8 | 7.5 | 10% | bootsx46, longbowx46, ruby_crystalx46 |
| sylphine | 58.7 [44.3, 71.7] | 46 | 0.94 | 0.61 | 11% | 4% | 1% | 7% | 0.24 | 0.35 | 1.1 | 0.1 | 8% | long_swordx46, ruby_crystalx46, vampiric_bladex46 |
| dax | 56.4 [43.3, 68.6] | 55 | 1.06 | 0.68 | 14% | 31% | 3% | 4% | 0.45 | 0.58 | 1.8 | 0.8 | 10% | long_swordx56, longbowx56, vampiric_bladex56 |
| vurmak | 54.1 [41.7, 66.0] | 61 | 1.13 | 0.73 | 17% | 6% | 1% | 24% | 0.62 | 0.26 | 0.9 | 2.9 | 10% | ruby_crystalx62, long_swordx61, cloth_armorx60 |
| corvane | 53.2 [39.2, 66.7] | 47 | 0.38 | 0.24 | 32% | 0% | 0% | 2% | 0.21 | 0.85 | 2.5 | 2.9 | 4% | longbowx48, ruby_crystalx48, bootsx47 |
| orrin | 52.0 [38.5, 65.2] | 50 | 1.23 | 0.80 | 5% | 16% | 1% | 0% | 0.28 | 0.56 | 1.8 | 0.0 | 10% | long_swordx50, longbowx50, ruby_crystalx49 |
| ossuar | 50.0 [35.5, 64.5] | 42 | 2.00 | 1.29 | 8% | 1% | 0% | 63% | 0.14 | 0.29 | 1.0 | 5.3 | 16% | cloth_armorx42, long_swordx42, ruby_crystalx42 |
| pallas | 50.0 [36.6, 63.4] | 50 | 1.56 | 1.01 | 9% | 0% | 3% | 77% | 0.10 | 0.74 | 2.3 | 5.9 | 13% | bootsx50, longbowx50, ruby_crystalx50 |
| rictus | 50.0 [36.4, 63.6] | 48 | 1.01 | 0.65 | 13% | 3% | 23% | 1% | 0.44 | 0.77 | 2.4 | 2.4 | 9% | long_swordx48, ruby_crystalx48, vampiric_bladex47 |
| wisp | 50.0 [37.3, 62.7] | 56 | 2.86 | 1.85 | 4% | 81% | 1% | 6% | 0.21 | 0.55 | 1.7 | 0.0 | 22% | longbowx56, ruby_crystalx56, bootsx55 |
| bastion | 42.1 [27.9, 57.8] | 38 | 1.99 | 1.29 | 75% | 0% | 0% | 5% | 0.50 | 0.11 | 0.4 | 1.2 | 16% | cloth_armorx38, long_swordx38, ruby_crystalx38 |
| veyra | 41.5 [29.3, 54.9] | 53 | 1.28 | 0.82 | 2% | 69% | 0% | 2% | 0.51 | 0.51 | 1.6 | 0.5 | 11% | long_swordx54, longbowx54, vampiric_bladex54 |
| thornjaw | 41.5 [27.8, 56.6] | 41 | 1.05 | 0.67 | 11% | 3% | 1% | 4% | 0.46 | 0.32 | 0.9 | 0.2 | 9% | long_swordx42, ruby_crystalx42, vampiric_bladex41 |
| marrow | 40.8 [28.2, 54.8] | 49 | 2.57 | 1.66 | 3% | 0% | 0% | 62% | 0.27 | 0.22 | 0.8 | 0.0 | 21% | cloth_armorx50, long_swordx50, ruby_crystalx50 |
| bramblehide | 40.4 [28.2, 53.9] | 52 | 1.68 | 1.08 | 3% | 16% | 0% | 31% | 0.17 | 0.29 | 0.9 | 3.6 | 13% | long_swordx52, ruby_crystalx52, vampiric_bladex52 |
| kestrel | 38.2 [23.9, 55.0] | 34 | 1.60 | 1.03 | 74% | 7% | 0% | 6% | 0.24 | 0.18 | 0.6 | 1.6 | 13% | long_swordx34, longbowx34, vampiric_bladex33 |
| noctis | 37.5 [25.2, 51.6] | 48 | 1.45 | 0.94 | 78% | 0% | 9% | 1% | 0.60 | 0.54 | 1.6 | 0.1 | 13% | ionian_charmx48, longbowx48, long_swordx47 |
| vellum | 37.5 [22.9, 54.7] | 32 | 2.15 | 1.38 | 2% | 0% | 1% | 69% | 0.31 | 0.56 | 1.8 | 3.2 | 19% | longbowx32, ionian_charmx30, ruby_crystalx30 |
| lumen | 35.9 [22.7, 51.6] | 39 | 0.67 | 0.43 | 55% | 0% | 0% | 1% | 0.21 | 0.31 | 0.9 | 0.1 | 6% | longbowx40, ruby_crystalx40, bootsx39 |
| sable | 34.7 [22.9, 48.7] | 49 | 2.95 | 1.91 | 1% | 52% | 0% | 32% | 0.22 | 0.27 | 0.8 | 1.7 | 25% | ionian_charmx50, longbowx50, ruby_crystalx50 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.22 |
| Jungle | 50.0 [43.7, 56.3] | 1.14 |
| Mid | 50.0 [43.7, 56.3] | 2.37 |
| Support | 50.0 [43.7, 56.3] | 1.40 |
| Top | 50.0 [43.7, 56.3] | 1.66 |

## 5. Games

- length: median 20.0, p10 16, p90 20
- end reasons: {'nexus': 47, 'round_limit_towers': 50, 'round_limit_hp': 20, 'round_limit_draw': 1, 'round_limit_kills': 2} (draws 1)
- priority win rate: 47.9% [39.1, 56.8]
- north win rate: 51.3% [42.4, 60.1]
- length histogram: {11: 1, 12: 2, 13: 2, 14: 5, 15: 2, 16: 5, 17: 5, 18: 9, 19: 8, 20: 81}

## 6. Objectives

- takes per game: {'dragon': 3.075, 'baron': 1.5333333333333334}
- median round taken: dragon 11, baron 13.0
- win rate when secured: {'dragon': 44.38356164383562, 'baron': 46.7032967032967}
- camp clears per game: {'wolves': 8.458333333333334, 'raptors': 8.683333333333334, 'krugs': 8.408333333333333, 'blue_buff': 5.058333333333334, 'red_buff': 4.8, 'dragon': 3.075, 'baron': 1.5333333333333334}

## 7. Structures

- first tower falls: median round 8, p10 4, p90 13
- games with at least one tower down: 99.2%
- first-tower win rate: 84.7%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.12 |
| chips_wave | 3.26 |
| base | 3.00 |
| champion_kill | 0.37 |
| dragon | 0.32 |
| tower_kill | 0.29 |
| blue_buff | 0.27 |
| red_buff | 0.15 |

| use | AP |
|---|---|
| shop | 9.15 |
| abilities | 2.02 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.98 | 46.6% | 70.2% | -23.6 |
| cloth_armor | 5 | 1.98 | 48.1% | 52.9% | -4.8 |
| control_ward | 2 | 1.09 | - | 50.0% | - |
| frost_charm | 2 | 0.78 | - | 50.0% | - |
| health_potion | 2 | 1.81 | - | 50.0% | - |
| ionian_charm | 8 | 1.98 | 45.5% | 62.5% | -17.1 |
| long_sword | 6 | 2.00 | 49.3% | 52.5% | -3.2 |
| longbow | 6 | 2.00 | 49.9% | 50.1% | -0.2 |
| ruby_crystal | 4 | 2.00 | 49.6% | 80.0% | -30.4 |
| stopwatch | 3 | 1.82 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 1.99 | 48.3% | 54.0% | -5.6 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 100.0 [93.8, 100.0] |
| T2_laner | 53 | 50.9 [37.9, 63.9] |
| T2_objective | 42 | 42.9 [29.1, 57.8] |
| T2_warder | 38 | 21.1 [11.1, 36.3] |
| T2_brawler | 47 | 17.0 [8.9, 30.1] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 67.22 per game
- that is 46.1% of all ability uses
- of which true snipes (from cover, two or more hexes away): 41.7% of all uses
- snipes aimed at a champion: 9.2 per game
- activations ending beside an enemy-held hexgroup (looking in): 45.3%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **Median game length 13-18 rounds** - 20.0 [20.0, 20.0]
2. **>=95% of games end by Nexus kill before round 20** - 39.2% [30.9, 48.1]
3. **champion win rate: quillan** - WR 72.7% [58.2, 83.7]
4. **ability usage: ashwyn.R** - used in 16.5% of affordable rounds with a legal target
5. **ability usage: bastion.W** - used in 0.3% of affordable rounds with a legal target

## 12. Delta vs batch_0039

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +4.0 | -1.94 | no |
| bastion | -10.5 | -0.27 | no |
| bramblehide | -11.5 | -0.05 | no |
| brixa | +17.4 | -0.26 | no |
| corvane | +24.0 | -0.14 | no |
| dax | -4.4 | -0.25 | no |
| grivven | +15.2 | -1.18 | no |
| kaelis | +8.3 | -0.38 | no |
| kestrel | -14.7 | -0.19 | no |
| lumen | -1.6 | -0.13 | no |
| marrow | +2.8 | +0.33 | no |
| mossgrove | +14.6 | -0.18 | no |
| noctis | +4.2 | -0.07 | no |
| orrin | +2.0 | -0.49 | no |
| ossuar | -7.1 | -0.20 | no |
| pallas | -6.0 | -2.29 | no |
| quillan | +6.8 | -1.39 | no |
| rictus | +4.2 | -0.16 | no |
| sable | -17.3 | -2.68 | no |
| sylphine | -2.2 | -0.38 | no |
| thornjaw | -6.2 | -0.21 | no |
| vellum | +3.1 | -0.50 | no |
| veyra | -2.9 | -0.10 | no |
| vurmak | +2.5 | -0.31 | no |
| wisp | -26.8 | -2.19 | no |

- median length delta: +2.0
- nexus-kill rate delta: -39.2 pts
