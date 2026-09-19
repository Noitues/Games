# Roster v1.0.0 (rules 1.0.0)

Phase 0 roster. 2 champions per role, each built to 22 +/- 2 by Rules 14.2. Budgets are recomputed by engine/kits.py and asserted in tests/test_roster.py.

## Bastion — Top

*Engage tank. Slow, very hard to kill, locks a fight down with a point-blank ultimate.*

**HP 9 · Speed 2** (stats +4 points)

| ability | cost / CD | icon sequence | gross | net |
|---|---|---|---|---|
| Q | 0 / 1 | HIT r1 -> PUSH 1 | 5 | 5 |
| W | 1 / 1 | SHIELD 4 r2 + | 7 | 4 |
| E | 1 / 2 | DASH 2 -> ROOT r1 <> | 8 | 3 |
| R | 3 / 3 | AREA 2 r1 -> ROOT r1 (area) <> | 18 | 5 |

**Budget total: 21** (on budget)

Notes: Speed 2 means Bastion needs a lane assignment it can hold; R is the only area root in the roster.

## Vurmak — Top

*Split-pushing juggernaut. Shoves waves and chews towers; self-sustains instead of recalling.*

**HP 9 · Speed 3** (stats +9 points)

| ability | cost / CD | icon sequence | gross | net |
|---|---|---|---|---|
| Q | 1 / 1 | HIT x2 r1 | 6 | 3 |
| W | 0 / 2 | HEAL 2 r1 + | 4 | 2 |
| E | 0 / 2 | DASH 3 -> PUSH 1 r1 | 6.5 | 4.5 |
| R | 2 / 2 | HIT x4 r1 | 12 | 4 |

**Budget total: 22.5** (on budget)

Notes: Q nets +1 AP per use on a wave and R nets +2: watch the economy metric. R is the roster's best single-target tower chipper.

## Thornjaw — Jungle

*Skirmishing jungler. Fastest champion on the board; clears camps with a two-hit rend and ganks with a dash.*

**HP 8 · Speed 4** (stats +11 points)

| ability | cost / CD | icon sequence | gross | net |
|---|---|---|---|---|
| Q | 0 / 1 | HIT r2 | 4 | 4 |
| W | 1 / 1 | DASH 2 -> HIT r1 | 6 | 3 |
| E | 1 / 2 | HIT x2 r1 -> SLOW 1 | 7.5 | 2.5 |
| R | 2 / 2 | HIT x2 r1 -> PUSH 2 | 10 | 2 |

**Budget total: 22.5** (on budget)

Notes: Camp clear: E (2) + Q (1) kills a 3-chip camp in two activations, or R (2) + Q (1).

## Mossgrove — Jungle

*Objective jungler. Slow, self-healing, built to solo Dragon and Baron and to scout with REVEAL.*

**HP 8 · Speed 3** (stats +6 points)

| ability | cost / CD | icon sequence | gross | net |
|---|---|---|---|---|
| Q | 0 / 2 | HIT x2 r1 | 6 | 4 |
| W | 0 / 1 | REVEAL r3 -> MOVE 2 | 5 | 5 |
| E | 1 / 1 | SHIELD 3 r2 + | 5.5 | 2.5 |
| R | 2 / 3 | HIT x3 r1 -> HEAL 2 r1 + | 13 | 3 |

**Budget total: 20.5** (on budget)

Notes: Q is a free 2-chip farm on a 2-round cooldown: the roster's cleanest camp clear. R sustains through monster damage.

## Ashwyn — Mid

*Burst mage. The most fragile champion in the game; deletes a single target from range 3 and blinks away.*

**HP 6 · Speed 3** (stats +0 points)

| ability | cost / CD | icon sequence | gross | net |
|---|---|---|---|---|
| Q | 0 / 1 | HIT r3 | 5 | 5 |
| W | 1 / 1 | AREA 1 r2 | 7 | 4 |
| E | 0 / 2 | BLINK 3 | 6 | 4 |
| R | 2 / 2 | HIT x3 r3 | 15 | 7 |

**Budget total: 20** (on budget)

Notes: W is the roster's only r2 area hit: it farms stacked waves and punishes units sharing a hidden tile. 6 HP means a single tower volley plus one hit kills.

## Vellum — Mid

*Control mage. Durable, slows and cooldown-locks a key target, and rakes a whole lane with a line ultimate.*

**HP 8 · Speed 3** (stats +6 points)

| ability | cost / CD | icon sequence | gross | net |
|---|---|---|---|---|
| Q | 1 / 1 | HIT r3 -> SLOW 2 | 8 | 5 |
| W | 2 / 2 | HIT r2 <> -> DELAY | 12 | 4 |
| E | 0 / 2 | BLINK 2 | 4 | 2 |
| R | 2 / 2 | LINE 2 len 5 | 14 | 6 |

**Budget total: 23** (on budget)

Notes: Only DELAY in the roster (Designer cap: 1 per champion). Watch the cooldown-lock exploit policy against it.

## Kestrel — ADC

*Long-range marksman. Out-ranges everything, farms from safety, wins by out-scaling through AP.*

**HP 8 · Speed 3** (stats +6 points)

| ability | cost / CD | icon sequence | gross | net |
|---|---|---|---|---|
| Q | 0 / 1 | HIT r3 | 5 | 5 |
| W | 1 / 1 | HIT x2 r3 | 10 | 7 |
| E | 0 / 2 | BLINK 2 | 4 | 2 |
| R | 3 / 3 | LINE 2 len 6 | 16 | 3 |

**Budget total: 23** (on budget)

Notes: Rulebook worked example (Rules 14.2). W nets +1 AP per use against a wave: the roster's reference farming engine.

## Dax — ADC

*Mobile hyper-carry. Shorter range than Kestrel but repositions with every ability and self-peels with a knockback.*

**HP 7 · Speed 3** (stats +3 points)

| ability | cost / CD | icon sequence | gross | net |
|---|---|---|---|---|
| Q | 0 / 1 | MOVE 1 -> HIT r2 | 5 | 5 |
| W | 1 / 1 | HIT x2 r2 | 8 | 5 |
| E | 1 / 2 | HIT r2 -> PUSH 2 | 8 | 3 |
| R | 2 / 2 | HIT x3 r2 -> MOVE 2 | 14 | 6 |

**Budget total: 22** (on budget)

Notes: Three farming engines (Q, W, R all beat their cost in chips). Highest expected AP per round in the roster: economy watch.

## Lumen — Support

*Enchanter. Keeps a carry alive and on tempo; the only HASTE in the roster.*

**HP 8 · Speed 4** (stats +11 points)

| ability | cost / CD | icon sequence | gross | net |
|---|---|---|---|---|
| Q | 1 / 1 | HIT r2 -> HEAL 1 r2 + | 7 | 4 |
| W | 1 / 1 | SHIELD 3 r2 + | 5.5 | 2.5 |
| E | 1 / 2 | HASTE r2 + | 7 | 2 |
| R | 2 / 2 | HEAL 3 r2 + -> SHIELD 2 r2 + | 11 | 3 |

**Budget total: 22.5** (on budget)

Notes: Q is the support's answer to Rules 4.B 'useful without farming': it pokes and heals in one step. E is the roster's only HASTE (Designer cap: 1 per champion).

## Grivven — Support

*Catcher. Tanky hook support that drags a target out of position and locks an area down with the ultimate.*

**HP 9 · Speed 3** (stats +9 points)

| ability | cost / CD | icon sequence | gross | net |
|---|---|---|---|---|
| Q | 1 / 2 | HIT r3 -> PULL 2 | 9 | 4 |
| W | 0 / 2 | SHIELD 2 r3 + | 4 | 2 |
| E | 0 / 2 | PUSH 2 r1 -> SLOW 1 | 5.5 | 3.5 |
| R | 2 / 3 | AREA 1 r1 -> ROOT r1 (area) <> | 13 | 3 |

**Budget total: 21.5** (on budget)

Notes: Q pulls a champion out of a hidden tile's protection; R is the second area root. No farming engine by design.

## Budget summary

| champion | role | HP | Speed | stats | Q | W | E | R | total |
|---|---|---|---|---|---|---|---|---|---|
| Bastion | Top | 9 | 2 | 4 | 5 | 4 | 3 | 5 | 21 |
| Vurmak | Top | 9 | 3 | 9 | 3 | 2 | 4.5 | 4 | 22.5 |
| Thornjaw | Jungle | 8 | 4 | 11 | 4 | 3 | 2.5 | 2 | 22.5 |
| Mossgrove | Jungle | 8 | 3 | 6 | 4 | 5 | 2.5 | 3 | 20.5 |
| Ashwyn | Mid | 6 | 3 | 0 | 5 | 4 | 4 | 7 | 20 |
| Vellum | Mid | 8 | 3 | 6 | 5 | 4 | 2 | 6 | 23 |
| Kestrel | ADC | 8 | 3 | 6 | 5 | 7 | 2 | 3 | 23 |
| Dax | ADC | 7 | 3 | 3 | 5 | 5 | 3 | 6 | 22 |
| Lumen | Support | 8 | 4 | 11 | 4 | 2.5 | 2 | 3 | 22.5 |
| Grivven | Support | 9 | 3 | 9 | 4 | 2 | 3.5 | 3 | 21.5 |

L0 (every champion): 0 AP, cooldown 1, HIT 1 adjacent.
