# Sim report batch_0074

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
| runtime | 2.0s |
| engine tests | not run |
| generated | 2026-09-28 07:56:02 |

## 2. Balance scorecard

| check | value | verdict |
|---|---|---|
| Champion win rate within 45-55% | 0 FAIL / 16 INCONCLUSIVE of 25 | **INCONCLUSIVE** |
| AP-cost ability usage 40-70% of affordable rounds | 52/58 abilities outside the band; roster mean 14.5%; 4 champions >15pp from it | **FAIL** |
| Priority (first player) win rate 48-52% | 51.8% [49.7, 54.0] | **INCONCLUSIVE** |
| Median game length 13-18 rounds | 16.0 [16.0, 16.0] | **PASS** |
| >=95% of games end by Nexus kill before round 20 | 99.8% [99.5, 99.9] | **PASS** |
| No champion above 1.5x roster-mean AP per round | ashwyn, quillan, sable, vellum (roster mean 1.12 AP/round) | **FAIL** |
| North vs South win rate 48-52% | north 45.6% [43.5, 47.8] | **FAIL** |

## 3. Champions

| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wisp | 56.1 [52.6, 59.5] | 788 | 1.52 | 1.36 | 7% | 65% | 1% | 3% | 0.18 | 0.76 | 2.7 | 5.0 | 14% | longbowx788, ruby_crystalx788, bootsx767 |
| bastion | 56.0 [52.5, 59.4] | 802 | 1.03 | 0.92 | 46% | 1% | 0% | 7% | 0.24 | 0.26 | 1.1 | 1.6 | 10% | long_swordx802, ruby_crystalx802, cloth_armorx799 |
| thornjaw | 55.2 [51.7, 58.6] | 792 | 0.71 | 0.64 | 12% | 4% | 1% | 3% | 0.29 | 0.48 | 1.9 | 0.1 | 7% | long_swordx792, ruby_crystalx792, vampiric_bladex760 |
| pallas | 54.0 [50.6, 57.4] | 826 | 1.39 | 1.24 | 5% | 1% | 2% | 73% | 0.12 | 0.63 | 2.4 | 5.2 | 13% | longbowx826, ruby_crystalx826, bootsx819 |
| veyra | 53.5 [50.0, 57.0] | 776 | 0.98 | 0.88 | 2% | 58% | 0% | 2% | 0.45 | 0.61 | 2.4 | 0.5 | 9% | long_swordx776, longbowx774, vampiric_bladex752 |
| kestrel | 52.8 [49.4, 56.1] | 830 | 1.26 | 1.13 | 51% | 8% | 0% | 9% | 0.49 | 0.37 | 1.5 | 1.8 | 12% | long_swordx830, longbowx830, vampiric_bladex823 |
| sylphine | 52.7 [49.3, 56.0] | 828 | 0.73 | 0.65 | 11% | 3% | 0% | 11% | 0.30 | 0.37 | 1.4 | 0.0 | 7% | ruby_crystalx828, long_swordx827, vampiric_bladex765 |
| sable | 51.1 [47.7, 54.4] | 844 | 2.22 | 1.99 | 3% | 37% | 0% | 39% | 0.22 | 0.32 | 1.3 | 3.8 | 20% | longbowx844, ionian_charmx828, ruby_crystalx827 |
| noctis | 50.8 [47.2, 54.3] | 756 | 1.09 | 0.98 | 66% | 1% | 11% | 2% | 0.51 | 0.65 | 2.5 | 0.3 | 11% | longbowx756, ionian_charmx750, ruby_crystalx746 |
| brixa | 50.3 [46.8, 53.7] | 790 | 0.75 | 0.67 | 21% | 3% | 7% | 1% | 0.40 | 0.65 | 2.5 | 0.8 | 7% | long_swordx789, longbowx788, vampiric_bladex780 |
| lumen | 49.9 [46.6, 53.2] | 868 | 0.51 | 0.46 | 46% | 0% | 0% | 1% | 0.25 | 0.43 | 1.5 | 0.2 | 5% | longbowx868, ruby_crystalx868, bootsx855 |
| ashwyn | 49.4 [46.0, 52.8] | 820 | 1.83 | 1.64 | 4% | 53% | 1% | 19% | 0.32 | 0.93 | 3.3 | 2.0 | 17% | ionian_charmx820, longbowx820, ruby_crystalx819 |
| quillan | 49.4 [45.9, 52.8] | 796 | 1.87 | 1.67 | 8% | 8% | 1% | 60% | 0.20 | 0.77 | 2.8 | 2.8 | 18% | longbowx796, ionian_charmx785, ruby_crystalx780 |
| vellum | 49.4 [45.9, 52.9] | 784 | 1.82 | 1.63 | 3% | 0% | 4% | 64% | 0.39 | 0.64 | 2.5 | 3.1 | 17% | longbowx783, ionian_charmx762, ruby_crystalx744 |
| marrow | 49.3 [45.8, 52.7] | 804 | 1.45 | 1.30 | 2% | 0% | 0% | 55% | 0.16 | 0.24 | 1.0 | 4.9 | 13% | ruby_crystalx804, long_swordx803, cloth_armorx802 |
| bramblehide | 49.1 [45.6, 52.6] | 776 | 1.23 | 1.10 | 1% | 13% | 1% | 25% | 0.24 | 0.43 | 1.7 | 3.3 | 11% | long_swordx776, ruby_crystalx776, vampiric_bladex770 |
| kaelis | 48.4 [44.9, 51.8] | 790 | 0.57 | 0.51 | 22% | 3% | 7% | 5% | 0.32 | 0.40 | 1.6 | 0.7 | 6% | ruby_crystalx790, long_swordx785, cloth_armorx767 |
| vurmak | 48.3 [44.8, 51.8] | 764 | 0.85 | 0.76 | 19% | 6% | 1% | 23% | 0.48 | 0.34 | 1.4 | 2.7 | 9% | ruby_crystalx764, long_swordx750, cloth_armorx687 |
| ossuar | 48.1 [44.7, 51.5] | 840 | 1.60 | 1.43 | 34% | 1% | 0% | 35% | 0.27 | 0.24 | 1.0 | 3.5 | 15% | ruby_crystalx840, long_swordx836, cloth_armorx829 |
| orrin | 47.6 [44.3, 51.0] | 840 | 0.84 | 0.75 | 4% | 18% | 1% | 0% | 0.26 | 0.74 | 2.9 | 0.0 | 8% | long_swordx839, longbowx829, vampiric_bladex794 |
| rictus | 46.6 [43.1, 50.1] | 762 | 0.70 | 0.62 | 12% | 3% | 19% | 2% | 0.38 | 0.76 | 2.9 | 2.1 | 7% | ruby_crystalx762, long_swordx761, vampiric_bladex735 |
| mossgrove | 46.4 [43.1, 49.8] | 842 | 0.73 | 0.65 | 20% | 1% | 1% | 4% | 0.28 | 0.43 | 1.7 | 2.9 | 7% | long_swordx842, ruby_crystalx842, vampiric_bladex821 |
| grivven | 45.9 [42.2, 49.6] | 704 | 1.01 | 0.90 | 5% | 3% | 5% | 37% | 0.11 | 0.54 | 2.1 | 6.0 | 10% | ruby_crystalx704, longbowx703, bootsx701 |
| dax | 45.8 [42.3, 49.4] | 764 | 0.84 | 0.75 | 12% | 24% | 3% | 4% | 0.42 | 0.60 | 2.3 | 0.9 | 8% | long_swordx764, longbowx764, vampiric_bladex755 |
| corvane | 43.7 [40.4, 47.2] | 814 | 0.39 | 0.35 | 47% | 0% | 1% | 4% | 0.47 | 0.75 | 2.7 | 0.9 | 4% | longbowx814, ruby_crystalx814, bootsx809 |

## 4. Roles

Under `random_by_role_no_duplicates` both teams field exactly one champion of each role, so role win rate is 50% by construction. Read the AP column, and read win rates from the champion table.

| role | WR% [95% CI] | AP/round |
|---|---|---|
| ADC | 50.0 [48.5, 51.5] | 0.94 |
| Jungle | 50.0 [48.5, 51.5] | 0.82 |
| Mid | 50.0 [48.5, 51.5] | 1.78 |
| Support | 50.0 [48.5, 51.5] | 0.95 |
| Top | 50.0 [48.5, 51.5] | 1.11 |

## 5. Games

- length: median 16.0, p10 14, p90 18
- end reasons: {'nexus': 1996, 'round_limit_hp': 2, 'round_limit_towers': 2} (draws 0)
- priority win rate: 51.8% [49.7, 54.0]
- north win rate: 45.6% [43.5, 47.8]
- length histogram: {10: 1, 11: 12, 12: 52, 13: 129, 14: 303, 15: 460, 16: 524, 17: 285, 18: 156, 19: 55, 20: 23}

## 6. Objectives

- takes per game: {'dragon': 1.5555, 'baron': 0.4665}
- median round taken: dragon 8, baron 13
- win rate when secured: {'dragon': 50.7875281260045, 'baron': 45.444801714898176}
- camp clears per game: {'wolves': 5.3045, 'raptors': 5.3955, 'krugs': 4.907, 'blue_buff': 2.8505, 'red_buff': 2.6805, 'dragon': 1.5555, 'baron': 0.4665}

## 7. Structures

- first tower falls: median round 9.0, p10 6, p90 11
- games with at least one tower down: 100.0%
- first-tower win rate: 61.5%

## 8. Economy (AP per team-round)

| source | AP |
|---|---|
| chips_monster | 3.04 |
| base | 3.00 |
| chips_wave | 2.26 |
| champion_kill | 1.22 |
| tower_kill | 0.56 |
| dragon | 0.20 |
| blue_buff | 0.18 |
| red_buff | 0.09 |

| use | AP |
|---|---|
| shop | 8.68 |
| abilities | 1.50 |
| wasted | 0.00 |

## 9. Items

| item | cost | purchases/game | owner WR | non-owner WR | diff |
|---|---|---|---|---|---|
| boots | 4 | 1.98 | 54.7% | 41.3% | +13.4 |
| cloth_armor | 5 | 1.94 | 53.7% | 47.3% | +6.4 |
| control_ward | 2 | 0.11 | - | 50.0% | - |
| frost_charm | 2 | 0.06 | - | 50.0% | - |
| health_potion | 2 | 1.93 | - | 50.0% | - |
| ionian_charm | 8 | 1.97 | 55.4% | 45.4% | +10.0 |
| long_sword | 6 | 2.00 | 50.9% | 47.2% | +3.7 |
| longbow | 6 | 2.00 | 50.1% | 49.9% | +0.1 |
| ruby_crystal | 4 | 2.00 | 50.5% | 34.2% | +16.3 |
| stopwatch | 3 | 1.90 | - | 50.0% | - |
| swift_tonic | 1 | 1.99 | - | 50.0% | - |
| vampiric_blade | 5 | 1.97 | 52.3% | 46.8% | +5.5 |

## 9c. Personalities

| policy | games | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 | 2000 | 60.8 [58.6, 62.9] |
| T2_sieger | 2000 | 39.2 [37.1, 41.4] |


## 9d. State machines (ai 1.4.0) - field ranked by lower confidence bound

| policy | games | win rate [95% CI] |  | state occupancy | switches/game |
|---|---|---|---|---|
| SM_g2_lane6 | 2000 | 60.8 [58.6, 62.9] |  | sieger 68%, laner 32% | 1.0 |
| T2_sieger | 2000 | 39.2 [37.1, 41.4] |  | - | - |


## 9b. Concealment (RQ-032)

- attacks made from inside a hidden hexgroup on something outside it: 38.34 per game
- that is 35.7% of all ability uses
- of which true snipes (from cover, two or more hexes away): 31.8% of all uses
- snipes aimed at a champion: 4.7 per game
- activations ending beside an enemy-held hexgroup (looking in): 65.3%


## 10. Anomalies

None.

## 11. Top 5 flags (evidence only)

1. **North vs South win rate 48-52%** - north 45.6% [43.5, 47.8]
2. **ability usage: ashwyn.R** - used in 19.4% of affordable rounds with a legal target
3. **ability usage: bastion.W** - used in 0.6% of affordable rounds with a legal target
4. **ability usage: bastion.E** - used in 0.0% of affordable rounds with a legal target
5. **ability usage: bastion.R** - used in 7.1% of affordable rounds with a legal target
