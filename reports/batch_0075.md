# Sim report batch_0075

## 1. Header

| field | value |
|---|---|
| rules | 1.8.0 |
| roster | 1.9.0 |
| ai | 1.5.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 2000 |
| seed | 7301 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 1.2s |
| engine tests | not run |
| generated | 2026-09-28 07:56:09 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 1 FAIL / 16 INCONCLUSIVE of 25 | **FAIL** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 14.7%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 49.1% [47.0, 51.3] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 16.0 [16.0, 16.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 99.7% [99.3, 99.8] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, vellum (roster mean 1.12 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 47.9% [45.7, 50.0] | **INCONCLUSIVE** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 58.5 [55.0, 61.9] | 788 | 1.52 | 1.37 | 7% | 66% | 1% | 3% | 0.18 | 0.79 | 2.7 | 5.0 | 14% | longbowx788, ruby_crystalx788, bootsx772 |
| bastion | 57.9 [54.4, 61.2] | 802 | 1.02 | 0.92 | 46% | 1% | 0% | 7% | 0.27 | 0.29 | 1.3 | 1.6 | 10% | long_swordx802, ruby_crystalx802, cloth_armorx800 |
| veyra | 55.9 [52.4, 59.4] | 776 | 0.97 | 0.87 | 2% | 58% | 0% | 2% | 0.46 | 0.60 | 2.4 | 0.4 | 9% | long_swordx776, longbowx773, vampiric_bladex756 |
| pallas | 54.1 [50.7, 57.5] | 826 | 1.37 | 1.23 | 6% | 1% | 2% | 73% | 0.14 | 0.66 | 2.5 | 5.2 | 12% | longbowx826, ruby_crystalx826, bootsx821 |
| thornjaw | 53.4 [49.9, 56.9] | 792 | 0.68 | 0.61 | 12% | 4% | 1% | 3% | 0.31 | 0.50 | 2.0 | 0.1 | 6% | long_swordx792, ruby_crystalx792, vampiric_bladex753 |
| sylphine | 52.8 [49.4, 56.2] | 828 | 0.72 | 0.64 | 11% | 3% | 0% | 11% | 0.29 | 0.38 | 1.5 | 0.0 | 7% | ruby_crystalx828, long_swordx827, vampiric_bladex779 |
| kestrel | 52.7 [49.2, 56.0] | 830 | 1.24 | 1.11 | 50% | 8% | 0% | 9% | 0.50 | 0.40 | 1.7 | 1.8 | 11% | long_swordx830, longbowx830, vampiric_bladex823 |
| sable | 52.1 [48.8, 55.5] | 844 | 2.23 | 2.00 | 3% | 37% | 0% | 40% | 0.21 | 0.33 | 1.3 | 3.8 | 20% | longbowx844, ruby_crystalx830, ionian_charmx826 |
| vellum | 51.5 [48.0, 55.0] | 784 | 1.87 | 1.67 | 3% | 0% | 4% | 66% | 0.37 | 0.62 | 2.4 | 3.2 | 17% | longbowx784, ionian_charmx762, ruby_crystalx754 |
| brixa | 51.1 [47.7, 54.6] | 790 | 0.77 | 0.69 | 21% | 3% | 7% | 1% | 0.40 | 0.67 | 2.5 | 0.8 | 7% | long_swordx790, longbowx790, vampiric_bladex783 |
| ossuar | 51.1 [47.7, 54.4] | 840 | 1.60 | 1.43 | 33% | 1% | 0% | 35% | 0.29 | 0.23 | 1.0 | 3.5 | 15% | ruby_crystalx840, long_swordx837, cloth_armorx829 |
| bramblehide | 50.0 [46.5, 53.5] | 776 | 1.25 | 1.12 | 1% | 13% | 1% | 25% | 0.28 | 0.42 | 1.6 | 3.4 | 11% | long_swordx776, ruby_crystalx776, vampiric_bladex773 |
| lumen | 49.2 [45.9, 52.5] | 868 | 0.51 | 0.46 | 47% | 1% | 0% | 1% | 0.28 | 0.44 | 1.5 | 0.2 | 5% | longbowx868, ruby_crystalx868, bootsx857 |
| quillan | 49.0 [45.5, 52.5] | 796 | 1.87 | 1.68 | 7% | 8% | 1% | 61% | 0.21 | 0.81 | 2.9 | 2.8 | 18% | longbowx796, ionian_charmx789, ruby_crystalx783 |
| noctis | 48.7 [45.1, 52.2] | 756 | 1.09 | 0.97 | 65% | 0% | 12% | 2% | 0.50 | 0.64 | 2.4 | 0.3 | 11% | longbowx756, ionian_charmx747, ruby_crystalx739 |
| ashwyn | 48.5 [45.1, 52.0] | 820 | 1.84 | 1.65 | 4% | 53% | 1% | 20% | 0.33 | 0.93 | 3.1 | 2.0 | 18% | longbowx820, ionian_charmx819, ruby_crystalx819 |
| marrow | 48.5 [45.1, 52.0] | 804 | 1.47 | 1.32 | 3% | 1% | 0% | 56% | 0.16 | 0.24 | 1.0 | 4.9 | 13% | ruby_crystalx804, long_swordx803, cloth_armorx800 |
| mossgrove | 48.3 [45.0, 51.7] | 842 | 0.72 | 0.64 | 20% | 1% | 1% | 4% | 0.29 | 0.43 | 1.7 | 2.8 | 7% | long_swordx842, ruby_crystalx842, vampiric_bladex814 |
| vurmak | 46.6 [43.1, 50.1] | 764 | 0.85 | 0.76 | 20% | 6% | 1% | 24% | 0.51 | 0.32 | 1.3 | 2.7 | 8% | ruby_crystalx764, long_swordx754, cloth_armorx698 |
| kaelis | 45.7 [42.3, 49.2] | 790 | 0.57 | 0.51 | 23% | 3% | 6% | 5% | 0.30 | 0.42 | 1.8 | 0.7 | 6% | ruby_crystalx790, long_swordx787, cloth_armorx770 |
| orrin | 45.6 [42.3, 49.0] | 840 | 0.84 | 0.75 | 4% | 17% | 1% | 0% | 0.29 | 0.76 | 2.9 | 0.0 | 8% | long_swordx839, longbowx831, vampiric_bladex804 |
| rictus | 45.3 [41.8, 48.8] | 762 | 0.68 | 0.61 | 12% | 3% | 20% | 2% | 0.40 | 0.80 | 2.9 | 2.2 | 7% | long_swordx762, ruby_crystalx762, vampiric_bladex738 |
| dax | 44.8 [41.3, 48.3] | 764 | 0.83 | 0.75 | 12% | 25% | 3% | 4% | 0.41 | 0.62 | 2.4 | 0.9 | 8% | long_swordx764, longbowx763, vampiric_bladex749 |
| grivven | 44.2 [40.5, 47.9] | 704 | 1.00 | 0.90 | 5% | 4% | 5% | 38% | 0.11 | 0.53 | 2.2 | 6.0 | 10% | longbowx704, ruby_crystalx704, bootsx701 |
| corvane | 43.5 [40.1, 46.9] | 814 | 0.37 | 0.34 | 46% | 0% | 1% | 4% | 0.48 | 0.80 | 2.9 | 0.9 | 4% | longbowx814, ruby_crystalx814, bootsx812 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [48.5, 51.5] | 0.93 |
| Jungle | 50.0 [48.5, 51.5] | 0.80 |
| Mid | 50.0 [48.5, 51.5] | 1.79 |
| Support | 50.0 [48.5, 51.5] | 0.95 |
| Top | 50.0 [48.5, 51.5] | 1.11 |

## 5. Games

- length: median 16.0, p10 13, p90 18
- end reasons: {'nexus': 1993, 'round_limit_towers': 7} (draws 0)
- priority win rate: 49.1% [47.0, 51.3]
- north win rate: 47.9% [45.7, 50.0]
- length histogram: {11: 9, 12: 55, 13: 152, 14: 265, 15: 445, 16: 513, 17: 287, 18: 181, 19: 60, 20: 33}

## 6. Objectives

- takes per game: {'dragon': 1.5725, 'baron': 0.4575}
- median round taken: dragon 8, baron 13
- win rate when secured: {'dragon': 52.08267090620032, 'baron': 47.650273224043715}
- camp clears per game: {'wolves': 5.329, 'raptors': 5.4465, 'krugs': 4.929, 'blue_buff': 2.8425, 'red_buff': 2.6785, 'dragon': 1.5725, 'baron': 0.4575}

## 7. Structures

- first tower falls: median round 8.0, p10 6, p90 11
- games with at least one tower down: 100.0%
- first-tower win rate: 57.5%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.05 |
| base | 3.00 |
| chips_wave | 2.25 |
| champion_kill | 1.24 |
| tower_kill | 0.56 |
| dragon | 0.21 |
| blue_buff | 0.18 |
| red_buff | 0.09 |

| use | AP |
|---|---|
| shop | 8.68 |
| abilities | 1.51 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.98 | 56.0% | 38.9% | +17.1 |
| cloth_armor | 5 | 1.95 | 54.5% | 46.7% | +7.8 |
| control_ward | 2 | 0.12 | - | 50.0% | - |
| frost_charm | 2 | 0.06 | - | 50.0% | - |
| health_potion | 2 | 1.93 | - | 50.0% | - |
| ionian_charm | 8 | 1.97 | 57.2% | 43.8% | +13.5 |
| long_sword | 6 | 2.00 | 51.2% | 46.4% | +4.8 |
| longbow | 6 | 2.00 | 50.0% | 49.9% | +0.1 |
| ruby_crystal | 4 | 2.00 | 50.6% | 28.8% | +21.9 |
| stopwatch | 3 | 1.91 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.97 | 52.9% | 45.8% | +7.0 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 | 2000 | 62.1 [59.9, 64.2] |
| T2_sieger | 2000 | 38.0 [35.8, 40.1] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| SM_g2_lane6 | 2000 | 62.1 [59.9, 64.2] |  | sieger 68%, laner 32% | 1.0 |
| T2_sieger | 2000 | 38.0 [35.8, 40.1] |  | - | - |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 38.38 per game
- that is 35.7% of all ability uses
- of which true snipes (from cover, two or more hexes away): 31.7% of all uses
- snipes aimed at a champion: 4.8 per game
- activations ending beside an enemy-held hexgroup (looking in): 65.4%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **ability usage: ashwyn.R** - used in 19.8% of affordable rounds with a legal target
2. **ability usage: bastion.W** - used in 0.6% of affordable rounds with a legal target
3. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
4. **ability usage: bastion.R** - used in 7.2% of affordable rounds with a legal target
5. **ability usage: bramblehide.Q** - used in 1.4% of affordable rounds with a legal target
