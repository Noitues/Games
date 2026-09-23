# Sim report batch_0039

## 1. Header

| field | value |
|---|---|
| rules | 1.7.0 |
| roster | 1.6.0 |
| ai | 1.3.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 120 |
| seed | 3801 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 4824.9s |
| engine tests | not run |
| generated | 2026-09-23 16:38:13 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 2 FAIL / 23 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 51/58 abilities outside the band; roster mean 19.4%; 9 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 52.5% [43.6, 61.2] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 18.0 [17.0, 18.5] | **INCONCLUSIVE** |
| >=95% of games end by Nexus kill before round 20 | 78.3% [70.1, 84.8] | **FAIL** |
| No champion above 1.5x roster-mean AP per round | ashwyn, pallas, quillan, sable, wisp (roster mean 2.18 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 52.5% [43.6, 61.2] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 76.8 [64.2, 85.9] | 56 | 5.06 | 2.32 | 4% | 82% | 0% | 8% | 0.30 | 0.57 | 1.7 | 0.0 | 28% | bootsx56, cloth_armorx56, longbowx56 |
| quillan | 65.9 [51.1, 78.1] | 44 | 4.10 | 1.89 | 9% | 9% | 0% | 72% | 0.11 | 1.05 | 3.2 | 0.0 | 27% | longbowx44, ionian_charmx43, long_swordx43 |
| sylphine | 60.9 [46.5, 73.6] | 46 | 1.32 | 0.61 | 9% | 1% | 1% | 11% | 0.28 | 0.37 | 1.1 | 0.1 | 9% | bootsx46, long_swordx46, ruby_crystalx46 |
| dax | 60.7 [47.6, 72.4] | 56 | 1.31 | 0.60 | 10% | 41% | 3% | 14% | 0.27 | 0.46 | 1.3 | 1.8 | 9% | long_swordx56, longbowx56, ruby_crystalx56 |
| ashwyn | 57.6 [45.6, 68.8] | 66 | 4.42 | 2.03 | 4% | 69% | 0% | 19% | 0.18 | 0.91 | 2.9 | 0.0 | 28% | ionian_charmx66, long_swordx66, longbowx66 |
| ossuar | 57.1 [42.2, 70.9] | 42 | 2.20 | 1.01 | 7% | 4% | 0% | 56% | 0.17 | 0.14 | 0.5 | 4.1 | 13% | cloth_armorx42, long_swordx42, ruby_crystalx42 |
| pallas | 56.0 [42.3, 68.8] | 50 | 3.85 | 1.77 | 4% | 0% | 0% | 88% | 0.06 | 0.72 | 2.2 | 4.6 | 24% | bootsx50, cloth_armorx50, longbowx50 |
| kestrel | 52.9 [36.7, 68.5] | 34 | 1.79 | 0.82 | 64% | 13% | 0% | 17% | 0.35 | 0.09 | 0.2 | 3.4 | 11% | long_swordx34, longbowx34, ruby_crystalx34 |
| bastion | 52.6 [37.3, 67.5] | 38 | 2.26 | 1.04 | 85% | 0% | 0% | 3% | 0.42 | 0.26 | 0.9 | 0.6 | 16% | cloth_armorx38, long_swordx38, ruby_crystalx38 |
| kaelis | 52.1 [38.3, 65.5] | 48 | 1.21 | 0.56 | 19% | 4% | 3% | 11% | 0.29 | 0.44 | 1.2 | 1.2 | 9% | cloth_armorx48, ruby_crystalx48, long_swordx47 |
| sable | 52.0 [38.5, 65.2] | 50 | 5.64 | 2.59 | 4% | 49% | 0% | 38% | 0.20 | 0.22 | 0.6 | 1.4 | 34% | ionian_charmx50, longbowx50, ruby_crystalx50 |
| bramblehide | 51.9 [38.7, 64.9] | 52 | 1.73 | 0.80 | 5% | 26% | 1% | 23% | 0.25 | 0.31 | 0.9 | 3.5 | 11% | bootsx52, long_swordx52, ruby_crystalx52 |
| vurmak | 51.6 [39.4, 63.6] | 62 | 1.44 | 0.66 | 13% | 3% | 1% | 55% | 0.44 | 0.53 | 1.7 | 4.2 | 10% | cloth_armorx62, long_swordx62, ruby_crystalx62 |
| orrin | 50.0 [36.6, 63.4] | 50 | 1.72 | 0.79 | 9% | 36% | 1% | 0% | 0.20 | 0.66 | 2.0 | 0.0 | 12% | long_swordx50, vampiric_bladex50, longbowx49 |
| thornjaw | 47.6 [33.4, 62.3] | 42 | 1.25 | 0.58 | 12% | 7% | 3% | 4% | 0.29 | 0.17 | 0.5 | 0.2 | 8% | long_swordx42, ruby_crystalx42, vampiric_bladex42 |
| rictus | 45.8 [32.6, 59.7] | 48 | 1.17 | 0.54 | 13% | 5% | 34% | 1% | 0.25 | 0.77 | 2.2 | 2.7 | 8% | long_swordx48, ruby_crystalx48, vampiric_bladex48 |
| veyra | 44.4 [32.0, 57.6] | 54 | 1.38 | 0.63 | 2% | 74% | 0% | 7% | 0.57 | 0.43 | 1.3 | 1.3 | 10% | long_swordx54, longbowx54, vampiric_bladex54 |
| mossgrove | 44.2 [31.6, 57.7] | 52 | 1.17 | 0.54 | 35% | 3% | 1% | 5% | 0.19 | 0.48 | 1.5 | 3.3 | 8% | long_swordx52, ruby_crystalx52, vampiric_bladex52 |
| grivven | 43.5 [30.2, 57.8] | 46 | 2.30 | 1.06 | 5% | 1% | 1% | 70% | 0.07 | 0.52 | 1.8 | 8.1 | 16% | bootsx46, longbowx46, ruby_crystalx46 |
| brixa | 41.3 [28.3, 55.7] | 46 | 1.34 | 0.62 | 43% | 3% | 9% | 2% | 0.41 | 0.52 | 1.6 | 0.9 | 9% | long_swordx46, longbowx46, ruby_crystalx46 |
| marrow | 38.0 [25.9, 51.8] | 50 | 2.24 | 1.03 | 7% | 2% | 0% | 38% | 0.22 | 0.20 | 0.6 | 0.0 | 15% | cloth_armorx50, long_swordx50, ruby_crystalx50 |
| lumen | 37.5 [24.2, 53.0] | 40 | 0.81 | 0.37 | 66% | 1% | 0% | 1% | 0.15 | 0.30 | 1.0 | 0.1 | 6% | bootsx40, longbowx40, ruby_crystalx40 |
| vellum | 34.4 [20.4, 51.7] | 32 | 2.65 | 1.22 | 4% | 0% | 1% | 78% | 0.16 | 0.97 | 3.2 | 3.0 | 19% | ionian_charmx32, long_swordx32, longbowx32 |
| noctis | 33.3 [21.7, 47.5] | 48 | 1.52 | 0.70 | 77% | 0% | 15% | 0% | 0.29 | 0.54 | 1.7 | 0.1 | 12% | ionian_charmx48, longbowx48, ruby_crystalx48 |
| corvane | 29.2 [18.2, 43.2] | 48 | 0.52 | 0.24 | 56% | 0% | 0% | 3% | 0.21 | 0.69 | 2.1 | 4.1 | 4% | bootsx48, cloth_armorx48, longbowx48 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [43.7, 56.3] | 1.48 |
| Jungle | 50.0 [43.7, 56.3] | 1.33 |
| Mid | 50.0 [43.7, 56.3] | 3.80 |
| Support | 50.0 [43.7, 56.3] | 2.66 |
| Top | 50.0 [43.7, 56.3] | 1.82 |

## 5. Games

- length: median 18.0, p10 14, p90 20
- end reasons: {'nexus': 94, 'round_limit_hp': 9, 'round_limit_towers': 17} (draws 0)
- priority win rate: 52.5% [43.6, 61.2]
- north win rate: 52.5% [43.6, 61.2]
- length histogram: {10: 2, 11: 2, 12: 1, 13: 1, 14: 12, 15: 12, 16: 9, 17: 14, 18: 18, 19: 14, 20: 35}

## 6. Objectives

- takes per game: {'dragon': 2.3333333333333335, 'baron': 1.0833333333333333}
- median round taken: dragon 10.0, baron 12.0
- win rate when secured: {'dragon': 47.142857142857146, 'baron': 48.46153846153846}
- camp clears per game: {'wolves': 7.058333333333334, 'raptors': 7.125, 'krugs': 7.058333333333334, 'blue_buff': 4.366666666666666, 'dragon': 2.3333333333333335, 'red_buff': 4.175, 'baron': 1.0833333333333333}

## 7. Structures

- first tower falls: median round 8.0, p10 5, p90 11
- games with at least one tower down: 100.0%
- first-tower win rate: 74.2%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.91 |
| chips_structure | 3.73 |
| base | 3.52 |
| chips_wave | 3.27 |
| champion_kill | 0.41 |
| blue_buff | 0.25 |
| red_buff | 0.16 |

| use | AP |
|---|---|
| shop | 10.83 |
| abilities | 2.35 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 2.00 | 51.8% | 25.9% | +26.0 |
| cloth_armor | 5 | 2.00 | 52.5% | 44.0% | +8.5 |
| control_ward | 2 | 1.47 | - | 50.0% | - |
| frost_charm | 2 | 1.31 | - | 50.0% | - |
| health_potion | 2 | 1.91 | - | 50.0% | - |
| ionian_charm | 8 | 1.99 | 53.6% | 23.6% | +30.0 |
| long_sword | 6 | 2.00 | 50.2% | 49.4% | +0.8 |
| longbow | 6 | 2.00 | 50.1% | 49.9% | +0.2 |
| ruby_crystal | 4 | 2.00 | 50.2% | 16.7% | +33.5 |
| stopwatch | 3 | 1.90 | - | 50.0% | - |
| swift_tonic | 1 | 2.00 | - | 50.0% | - |
| vampiric_blade | 5 | 2.00 | 51.3% | 46.1% | +5.2 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| T2_sieger | 58 | 69.0 [56.2, 79.4] |
| T2_laner | 54 | 59.3 [46.0, 71.3] |
| T2_objective | 42 | 47.6 [33.4, 62.3] |
| T2_brawler | 48 | 35.4 [23.4, 49.6] |
| T2_warder | 38 | 28.9 [17.0, 44.8] |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 57.27 per game
- that is 43.2% of all ability uses
- of which true snipes (from cover, two or more hexes away): 40.2% of all uses
- snipes aimed at a champion: 10.8 per game
- activations ending beside an enemy-held hexgroup (looking in): 57.5%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **champion win rate: wisp** - WR 76.8% [64.2, 85.9]
2. **>=95% of games end by Nexus kill before round 20** - 78.3% [70.1, 84.8]
3. **economy outlier: sable** - 5.64 AP/round = 2.59x roster mean
4. **champion win rate: corvane** - WR 29.2% [18.2, 43.2]
5. **economy outlier: wisp** - 5.06 AP/round = 2.32x roster mean

## 12. Delta vs batch_0038

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | -3.0 | -0.98 | no |
| bastion | -5.3 | -0.06 | no |
| bramblehide | +3.8 | -0.26 | no |
| brixa | -8.7 | -0.22 | no |
| corvane | -8.3 | -0.04 | no |
| dax | -3.6 | -0.11 | no |
| grivven | -2.2 | -0.40 | no |
| kaelis | +10.4 | -0.03 | no |
| kestrel | -2.9 | -0.13 | no |
| lumen | +2.5 | -0.08 | no |
| marrow | -10.0 | -0.36 | no |
| mossgrove | +7.7 | -0.05 | no |
| noctis | -4.2 | -0.13 | no |
| orrin | +8.0 | -0.16 | no |
| ossuar | +14.3 | -0.11 | no |
| pallas | +8.0 | -0.47 | no |
| quillan | +6.8 | -1.13 | no |
| rictus | -8.3 | -0.19 | no |
| sable | +6.0 | -0.65 | no |
| sylphine | -2.2 | -0.08 | no |
| thornjaw | -2.4 | -0.09 | no |
| vellum | -6.2 | -0.13 | no |
| veyra | +5.6 | -0.07 | no |
| vurmak | -6.5 | -0.13 | no |
| wisp | +0.0 | -0.70 | no |

- median length delta: +3.0
- nexus-kill rate delta: -18.3 pts
