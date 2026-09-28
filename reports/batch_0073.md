# Sim report batch_0073

## 1. Header

| field | value |
|---|---|
| rules | 1.8.0 |
| roster | 1.8.0 |
| ai | 1.5.0 |
| matchup | T2_search vs T2_search (temperature 0.3) |
| games | 2000 |
| seed | 7301 |
| seat swap | True |
| team sampling | random_by_role_no_duplicates |
| runtime | 1.5s |
| engine tests | not run |
| generated | 2026-09-28 08:23:23 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 17 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 14.4%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 50.9% [48.7, 53.1] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 16.0 [16.0, 16.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 100.0% [99.7, 100.0] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, vellum (roster mean 1.11 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 45.8% [43.6, 48.0] | **FAIL** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bastion | 57.1 [53.7, 60.5] | 802 | 1.04 | 0.93 | 46% | 1% | 0% | 7% | 0.24 | 0.28 | 1.2 | 1.7 | 10% | ruby_crystalx802, long_swordx801, cloth_armorx800 |
| thornjaw | 56.8 [53.3, 60.2] | 792 | 0.70 | 0.63 | 12% | 4% | 1% | 3% | 0.28 | 0.48 | 2.0 | 0.1 | 7% | long_swordx792, ruby_crystalx792, vampiric_bladex759 |
| wisp | 56.7 [53.2, 60.1] | 788 | 1.49 | 1.34 | 7% | 64% | 1% | 3% | 0.19 | 0.78 | 2.8 | 5.0 | 14% | longbowx788, ruby_crystalx788, bootsx772 |
| pallas | 55.0 [51.6, 58.3] | 826 | 1.42 | 1.27 | 6% | 1% | 2% | 73% | 0.13 | 0.62 | 2.3 | 5.3 | 13% | longbowx826, ruby_crystalx826, bootsx822 |
| veyra | 54.5 [51.0, 58.0] | 776 | 0.98 | 0.88 | 1% | 59% | 0% | 2% | 0.45 | 0.63 | 2.5 | 0.4 | 9% | long_swordx776, longbowx775, vampiric_bladex750 |
| sable | 54.5 [51.1, 57.8] | 844 | 2.24 | 2.01 | 3% | 38% | 0% | 39% | 0.26 | 0.30 | 1.2 | 3.8 | 21% | longbowx844, ionian_charmx829, ruby_crystalx819 |
| noctis | 52.0 [48.4, 55.5] | 756 | 1.09 | 0.97 | 66% | 0% | 12% | 2% | 0.48 | 0.64 | 2.4 | 0.3 | 11% | longbowx756, ionian_charmx747, ruby_crystalx746 |
| kestrel | 51.7 [48.3, 55.1] | 830 | 1.25 | 1.13 | 51% | 8% | 0% | 9% | 0.50 | 0.41 | 1.6 | 1.8 | 12% | long_swordx830, longbowx829, vampiric_bladex825 |
| sylphine | 51.0 [47.6, 54.4] | 828 | 0.72 | 0.65 | 11% | 3% | 0% | 11% | 0.28 | 0.36 | 1.4 | 0.0 | 7% | ruby_crystalx828, long_swordx824, vampiric_bladex763 |
| bramblehide | 50.9 [47.4, 54.4] | 776 | 1.24 | 1.11 | 1% | 13% | 1% | 26% | 0.29 | 0.45 | 1.7 | 3.5 | 11% | long_swordx776, ruby_crystalx776, vampiric_bladex770 |
| ashwyn | 50.0 [46.6, 53.4] | 820 | 1.83 | 1.64 | 4% | 53% | 1% | 19% | 0.32 | 0.90 | 3.2 | 2.0 | 17% | longbowx820, ruby_crystalx820, ionian_charmx819 |
| brixa | 49.6 [46.1, 53.1] | 790 | 0.77 | 0.69 | 21% | 3% | 6% | 1% | 0.41 | 0.68 | 2.6 | 0.7 | 7% | long_swordx790, longbowx787, vampiric_bladex786 |
| ossuar | 49.2 [45.8, 52.5] | 840 | 1.61 | 1.44 | 34% | 1% | 0% | 35% | 0.31 | 0.21 | 0.9 | 3.5 | 15% | ruby_crystalx840, long_swordx838, cloth_armorx831 |
| lumen | 49.1 [45.8, 52.4] | 868 | 0.51 | 0.46 | 47% | 1% | 0% | 1% | 0.26 | 0.44 | 1.6 | 0.2 | 5% | longbowx868, ruby_crystalx868, bootsx851 |
| marrow | 49.0 [45.6, 52.5] | 804 | 1.36 | 1.22 | 5% | 1% | 0% | 43% | 0.16 | 0.30 | 1.2 | 4.1 | 13% | ruby_crystalx804, long_swordx801, cloth_armorx789 |
| kaelis | 48.7 [45.3, 52.2] | 790 | 0.57 | 0.51 | 22% | 3% | 6% | 5% | 0.32 | 0.41 | 1.6 | 0.7 | 6% | ruby_crystalx790, long_swordx780, cloth_armorx770 |
| orrin | 48.2 [44.9, 51.6] | 840 | 0.83 | 0.75 | 4% | 17% | 1% | 0% | 0.30 | 0.73 | 2.9 | 0.0 | 8% | long_swordx839, longbowx823, vampiric_bladex801 |
| vellum | 48.0 [44.5, 51.5] | 784 | 1.86 | 1.67 | 3% | 0% | 4% | 66% | 0.37 | 0.65 | 2.5 | 3.2 | 17% | longbowx784, ionian_charmx764, ruby_crystalx739 |
| mossgrove | 47.6 [44.3, 51.0] | 842 | 0.71 | 0.64 | 20% | 2% | 1% | 4% | 0.31 | 0.45 | 1.8 | 2.9 | 7% | long_swordx842, ruby_crystalx842, vampiric_bladex824 |
| dax | 45.9 [42.4, 49.5] | 764 | 0.82 | 0.74 | 12% | 24% | 3% | 4% | 0.46 | 0.60 | 2.3 | 0.8 | 8% | long_swordx764, longbowx762, vampiric_bladex752 |
| grivven | 45.9 [42.2, 49.6] | 704 | 1.01 | 0.91 | 5% | 3% | 5% | 37% | 0.10 | 0.54 | 2.1 | 6.0 | 10% | longbowx704, ruby_crystalx704, bootsx702 |
| vurmak | 45.8 [42.3, 49.4] | 764 | 0.86 | 0.78 | 20% | 6% | 1% | 23% | 0.50 | 0.35 | 1.4 | 2.7 | 9% | ruby_crystalx764, long_swordx751, cloth_armorx687 |
| quillan | 45.4 [41.9, 48.8] | 796 | 1.86 | 1.67 | 7% | 9% | 1% | 60% | 0.21 | 0.79 | 3.0 | 2.8 | 18% | longbowx796, ionian_charmx785, ruby_crystalx784 |
| rictus | 43.6 [40.1, 47.1] | 762 | 0.69 | 0.62 | 12% | 4% | 20% | 3% | 0.39 | 0.76 | 2.9 | 2.2 | 7% | long_swordx762, ruby_crystalx762, vampiric_bladex728 |
| corvane | 43.0 [39.6, 46.4] | 814 | 0.38 | 0.35 | 46% | 0% | 0% | 4% | 0.44 | 0.78 | 2.8 | 0.9 | 4% | longbowx814, ruby_crystalx814, bootsx812 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [48.5, 51.5] | 0.93 |
| Jungle | 50.0 [48.5, 51.5] | 0.81 |
| Mid | 50.0 [48.5, 51.5] | 1.79 |
| Support | 50.0 [48.5, 51.5] | 0.95 |
| Top | 50.0 [48.5, 51.5] | 1.10 |

## 5. Games

- length: median 16.0, p10 14, p90 18
- end reasons: {'nexus': 1999, 'round_limit_towers': 1} (draws 0)
- priority win rate: 50.9% [48.7, 53.1]
- north win rate: 45.8% [43.6, 48.0]
- length histogram: {10: 2, 11: 11, 12: 47, 13: 127, 14: 254, 15: 461, 16: 543, 17: 296, 18: 171, 19: 67, 20: 21}

## 6. Objectives

- takes per game: {'dragon': 1.561, 'baron': 0.4735}
- median round taken: dragon 8.0, baron 13
- win rate when secured: {'dragon': 50.60858424087124, 'baron': 45.828933474128824}
- camp clears per game: {'wolves': 5.293, 'raptors': 5.4455, 'krugs': 4.928, 'blue_buff': 2.815, 'red_buff': 2.726, 'dragon': 1.561, 'baron': 0.4735}

## 7. Structures

- first tower falls: median round 9.0, p10 6, p90 11
- games with at least one tower down: 100.0%
- first-tower win rate: 59.8%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.04 |
| base | 3.00 |
| chips_wave | 2.26 |
| champion_kill | 1.24 |
| tower_kill | 0.56 |
| dragon | 0.20 |
| blue_buff | 0.18 |
| red_buff | 0.09 |

| use | AP |
|---|---|
| shop | 8.64 |
| abilities | 1.56 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.98 | 55.4% | 40.0% | +15.4 |
| cloth_armor | 5 | 1.94 | 54.4% | 46.8% | +7.6 |
| control_ward | 2 | 0.11 | - | 50.0% | - |
| frost_charm | 2 | 0.06 | - | 50.0% | - |
| health_potion | 2 | 1.94 | - | 50.0% | - |
| ionian_charm | 8 | 1.97 | 56.3% | 44.6% | +11.7 |
| long_sword | 6 | 2.00 | 51.1% | 46.6% | +4.5 |
| longbow | 6 | 2.00 | 50.1% | 49.9% | +0.2 |
| ruby_crystal | 4 | 2.00 | 50.6% | 31.6% | +19.0 |
| stopwatch | 3 | 1.92 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.97 | 52.6% | 46.3% | +6.3 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 | 2000 | 62.2 [60.1, 64.3] |
| T2_sieger | 2000 | 37.8 [35.7, 39.9] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| SM_g2_lane6 | 2000 | 62.2 [60.1, 64.3] |  | sieger 68%, laner 32% | 1.0 |
| T2_sieger | 2000 | 37.8 [35.7, 39.9] |  | - | - |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 38.72 per game
- that is 36.0% of all ability uses
- of which true snipes (from cover, two or more hexes away): 31.9% of all uses
- snipes aimed at a champion: 4.8 per game
- activations ending beside an enemy-held hexgroup (looking in): 65.4%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **North vs South win rate 48-52%** - north 45.8% [43.6, 48.0]
2. **ability usage: ashwyn.R** - used in 19.5% of affordable rounds with a legal target
3. **ability usage: bastion.W** - used in 0.7% of affordable rounds with a legal target
4. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
5. **ability usage: bastion.R** - used in 7.4% of affordable rounds with a legal target
