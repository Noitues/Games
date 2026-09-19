# Sim report batch_0007

## 1. Header

| field | value |
|---|---|
| rules | 1.0.0 |
| roster | 1.1.0 |
| ai | 1.1.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 600 |
| seed | 777003 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 1565.2s |
| engine tests | not run |
| generated | 2026-09-19 17:40:42 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 8 FAIL / 17 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 48/58 abilities outside the band; roster mean 28.5%; 10 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 55.0% [51.0, 58.9] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 12.0 [11.0, 12.0] | **FAIL** |
| >=95% of games end by Nexus kill before round 20 | 99.5% [98.5, 99.8] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, ossuar, quillan, sable (roster mean 2.33 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 48.3% [44.4, 52.3] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quillan | 89.2 [84.6, 92.5] | 240 | 10.87 | 4.66 | 0% | 4% | 0% | 94% | 1.87 | 1.40 | 2.0 | 2.0 | 51% | ionian_charmx240, longbowx240, ruby_crystalx240 |
| ossuar | 72.6 [66.2, 78.2] | 208 | 4.55 | 1.95 | 1% | 0% | 0% | 94% | 0.73 | 0.75 | 1.2 | 4.2 | 25% | ruby_crystalx208, long_swordx207, cloth_armorx202 |
| sable | 61.7 [55.5, 67.5] | 248 | 7.67 | 3.29 | 1% | 7% | 0% | 90% | 1.45 | 1.57 | 2.3 | 2.5 | 42% | longbowx243, ruby_crystalx228, ionian_charmx226 |
| ashwyn | 61.7 [55.0, 67.9] | 214 | 6.96 | 2.98 | 1% | 82% | 0% | 15% | 1.09 | 1.69 | 2.7 | 0.5 | 40% | longbowx214, ionian_charmx213, ruby_crystalx211 |
| wisp | 61.1 [54.7, 67.1] | 234 | 3.09 | 1.32 | 6% | 39% | 0% | 49% | 0.85 | 1.55 | 2.5 | 2.6 | 19% | longbowx229, ruby_crystalx229, bootsx198 |
| grivven | 60.7 [54.1, 67.0] | 214 | 1.93 | 0.83 | 26% | 1% | 1% | 58% | 0.37 | 1.28 | 2.3 | 5.3 | 12% | longbowx214, ruby_crystalx214, bootsx202 |
| brixa | 58.8 [52.8, 64.7] | 260 | 1.11 | 0.48 | 13% | 4% | 5% | 58% | 0.28 | 1.11 | 1.9 | 3.5 | 7% | long_swordx259, longbowx229, vampiric_bladex225 |
| veyra | 54.2 [47.9, 60.4] | 238 | 1.15 | 0.50 | 3% | 18% | 1% | 70% | 0.18 | 1.16 | 2.0 | 5.3 | 8% | long_swordx216, longbowx201, vampiric_bladex184 |
| rictus | 54.1 [47.8, 60.2] | 246 | 0.63 | 0.27 | 26% | 3% | 19% | 16% | 0.70 | 1.41 | 2.3 | 2.1 | 4% | ruby_crystalx244, long_swordx229, vampiric_bladex189 |
| bramblehide | 53.4 [47.4, 59.4] | 262 | 2.94 | 1.26 | 0% | 6% | 2% | 83% | 0.93 | 1.69 | 2.7 | 3.6 | 19% | long_swordx262, ruby_crystalx262, vampiric_bladex246 |
| dax | 52.2 [45.7, 58.6] | 228 | 1.11 | 0.48 | 8% | 19% | 2% | 57% | 0.36 | 1.07 | 1.8 | 3.5 | 8% | long_swordx225, longbowx203, vampiric_bladex197 |
| thornjaw | 51.9 [45.2, 58.5] | 214 | 0.78 | 0.33 | 37% | 4% | 12% | 7% | 0.43 | 0.97 | 1.7 | 1.4 | 5% | ruby_crystalx207, long_swordx201, vampiric_bladex163 |
| bastion | 48.4 [42.3, 54.5] | 254 | 1.73 | 0.74 | 11% | 5% | 0% | 51% | 0.51 | 1.00 | 1.8 | 4.7 | 12% | ruby_crystalx254, cloth_armorx227, long_swordx223 |
| pallas | 48.0 [42.0, 54.2] | 254 | 2.69 | 1.15 | 4% | 4% | 3% | 74% | 0.50 | 1.67 | 2.7 | 3.3 | 17% | ruby_crystalx254, longbowx241, bootsx222 |
| vurmak | 47.7 [41.7, 53.8] | 258 | 1.12 | 0.48 | 12% | 2% | 3% | 62% | 0.57 | 1.25 | 2.0 | 3.6 | 8% | ruby_crystalx257, long_swordx227, cloth_armorx202 |
| sylphine | 46.9 [40.9, 53.0] | 256 | 0.69 | 0.30 | 27% | 6% | 5% | 33% | 0.36 | 0.98 | 1.8 | 2.5 | 5% | ruby_crystalx246, long_swordx232, vampiric_bladex182 |
| kestrel | 46.7 [40.6, 53.0] | 244 | 1.71 | 0.73 | 4% | 19% | 0% | 69% | 0.42 | 1.10 | 1.9 | 5.5 | 12% | long_swordx243, longbowx221, vampiric_bladex207 |
| marrow | 43.8 [37.9, 49.9] | 258 | 1.22 | 0.52 | 6% | 2% | 1% | 58% | 0.36 | 1.00 | 1.7 | 3.3 | 9% | ruby_crystalx258, long_swordx205, cloth_armorx193 |
| lumen | 43.4 [37.7, 49.4] | 274 | 0.56 | 0.24 | 71% | 1% | 0% | 11% | 0.34 | 0.48 | 0.8 | 1.1 | 4% | ruby_crystalx272, longbowx269, bootsx239 |
| mossgrove | 43.2 [36.9, 49.8] | 222 | 0.60 | 0.26 | 17% | 10% | 1% | 35% | 0.42 | 1.21 | 2.0 | 4.1 | 4% | ruby_crystalx222, long_swordx215, vampiric_bladex175 |
| kaelis | 40.5 [34.3, 47.1] | 222 | 0.89 | 0.38 | 20% | 5% | 2% | 43% | 0.40 | 1.25 | 2.0 | 2.8 | 7% | ruby_crystalx222, long_swordx179, cloth_armorx175 |
| corvane | 38.4 [32.3, 44.9] | 224 | 0.21 | 0.09 | 57% | 5% | 0% | 5% | 0.29 | 0.77 | 1.4 | 4.0 | 2% | ruby_crystalx222, longbowx220, bootsx205 |
| orrin | 37.0 [31.0, 43.4] | 230 | 0.83 | 0.36 | 10% | 50% | 6% | 2% | 0.33 | 1.26 | 2.1 | 3.3 | 6% | long_swordx225, longbowx198, vampiric_bladex181 |
| vellum | 32.5 [27.0, 38.6] | 246 | 2.71 | 1.16 | 2% | 0% | 0% | 92% | 0.70 | 1.74 | 2.9 | 3.2 | 22% | longbowx231, ionian_charmx187, ruby_crystalx185 |
| noctis | 8.3 [5.5, 12.4] | 252 | 0.57 | 0.25 | 29% | 0% | 36% | 17% | 0.71 | 1.06 | 1.9 | 2.3 | 6% | longbowx221, ruby_crystalx169, ionian_charmx131 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [47.2, 52.8] | 1.19 |
| Jungle | 50.0 [47.2, 52.8] | 1.17 |
| Mid | 50.0 [47.2, 52.8] | 5.68 |
| Support | 50.0 [47.2, 52.8] | 1.68 |
| Top | 50.0 [47.2, 52.8] | 1.82 |

## 5. Games

- length: median 12.0, p10 9, p90 16
- end reasons: {'nexus': 597, 'round_limit_towers': 2, 'round_limit_hp': 1} (draws 0)
- priority win rate: 55.0% [51.0, 58.9]
- north win rate: 48.3% [44.4, 52.3]
- length histogram: {6: 3, 7: 7, 8: 30, 9: 59, 10: 106, 11: 91, 12: 87, 13: 68, 14: 55, 15: 28, 16: 33, 17: 10, 18: 12, 19: 6, 20: 5}

## 6. Objectives

- takes per game: {'dragon': 1.8333333333333333, 'baron': 0.8}
- median round taken: dragon 6.0, baron 10.0
- win rate when secured: {'dragon': 51.90909090909091, 'baron': 58.125}
- camp clears per game: {'wolves': 7.458333333333333, 'raptors': 7.8933333333333335, 'krugs': 7.92, 'blue_buff': 4.506666666666667, 'red_buff': 4.616666666666666, 'dragon': 1.8333333333333333, 'baron': 0.8}

## 7. Structures

- first tower falls: median round 3.0, p10 1, p90 4
- games with at least one tower down: 100.0%
- first-tower win rate: 67.8%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 4.18 |
| chips_wave | 3.48 |
| chips_structure | 3.42 |
| base | 3.41 |
| champion_kill | 0.45 |
| blue_buff | 0.36 |
| red_buff | 0.23 |

| use | AP |
|---|---|
| shop | 11.01 |
| abilities | 3.33 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.78 | 69.9% | 13.0% | +56.9 |
| cloth_armor | 5 | 1.67 | 70.9% | 33.4% | +37.5 |
| control_ward | 2 | 0.28 | - | 50.0% | - |
| frost_charm | 2 | 0.17 | - | 50.0% | - |
| health_potion | 2 | 1.78 | - | 50.0% | - |
| ionian_charm | 8 | 1.66 | 75.2% | 17.8% | +57.4 |
| long_sword | 6 | 1.96 | 57.4% | 33.2% | +24.2 |
| longbow | 6 | 1.97 | 53.3% | 45.7% | +7.7 |
| ruby_crystal | 4 | 2.00 | 54.7% | 0.8% | +53.9 |
| stopwatch | 3 | 1.81 | - | 50.0% | - |
| swift_tonic | 1 | 1.89 | - | 50.0% | - |
| vampiric_blade | 5 | 1.69 | 67.0% | 30.4% | +36.6 |

## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **economy outlier: quillan** - 10.87 AP/round = 4.66x roster mean
2. **champion win rate: noctis** - WR 8.3% [5.5, 12.4]
3. **champion win rate: quillan** - WR 89.2% [84.6, 92.5]
4. **economy outlier: sable** - 7.67 AP/round = 3.29x roster mean
5. **economy outlier: ashwyn** - 6.96 AP/round = 2.98x roster mean

## 12. Delta vs batch_0004

| champion | WR delta | AP/round delta | significant (Holm) |
|---|---|---|---|
| ashwyn | +1.7 | +0.16 | no |
| bastion | -4.6 | +0.10 | no |
| bramblehide | +1.9 | +0.07 | no |
| brixa | +3.4 | +0.20 | no |
| corvane | +3.7 | +0.04 | no |
| dax | +4.0 | +0.14 | no |
| grivven | +1.0 | +0.11 | no |
| kaelis | +0.7 | +0.16 | no |
| kestrel | -17.1 | +0.09 | yes |
| lumen | -3.0 | +0.21 | no |
| marrow | -1.4 | +0.24 | no |
| mossgrove | -15.2 | +0.06 | no |
| noctis | +1.9 | +0.23 | no |
| orrin | -5.2 | +0.10 | no |
| ossuar | +4.2 | -0.03 | no |
| pallas | -16.1 | +0.09 | yes |
| quillan | -1.9 | -0.08 | no |
| rictus | +18.1 | +0.15 | yes |
| sable | +0.2 | +0.65 | no |
| sylphine | -7.2 | +0.11 | no |
| thornjaw | +0.6 | +0.13 | no |
| vellum | +2.4 | +0.58 | no |
| veyra | +11.7 | +0.17 | no |
| vurmak | +4.7 | +0.15 | no |
| wisp | +16.1 | +0.46 | no |

- median length delta: +0.0
- nexus-kill rate delta: +0.7 pts
