# Rules engine, bots and Monte Carlo

A headless rules engine with layered AI players, for testing balance by auto-play. Plain JavaScript ES modules, no dependencies (Node 18+). The engine in `src/engine/` is written to be reused by the browser prototype later.

```
node sim/smoke.js                                         # every bot level x 1-4 players x offset/direct
node sim/run.js --games 200 --houses galvan,keel --bot house
node sim/run.js --ladder --games 100                      # compare bot levels
node sim/run.js --sweep --games 150 --bot house           # every 2-house pairing
node sim/run.js ... --pairing direct --seed 7 --json out.json
node sim/tune.js --games 40 --grid purposePerPlayer=4,5 decayPerPlayer=3,4   # parameter grid
```

Runs are deterministic for a given `--seed`.

## Layout
| File | Role |
|---|---|
| `src/engine/config.js` | Every tunable value and rule toggle |
| `src/engine/rules.js` | Board queries, effect verbs, damage, Decay/cascade, Purpose, win/loss checks |
| `src/engine/game.js` | Setup, the eight phases, leaders, Discoveries, game loop |
| `src/ai/eval.js` | State evaluation (weights in `W`) |
| `src/ai/bots.js` | The layered bots |
| `sim/load.js` | Loads `data/*.json` |
| `sim/run.js` | Batch runner and report |

The engine asks agents for every decision through `choose(G, state, house, kind, options, ctx)`. Decision kinds:
- **Targeting and placement:** `cardTarget`, `innateTarget`, `ventTo`, `gatherFrom`, `cascade`, `moveInfluenceFrom`, `growthInfluence`, `influenceFor`, `addCrewAt`, `restoreAt`, `breakthroughAt`.
- **Round decisions:** `growth`, `track`, `remarkables`, `commit`, `clone`.
- **Table decisions:** `vote`, `discovery`.

## Bot layers
| Level | Name | Adds |
|---|---|---|
| 0 | `random` | Legal random choices everywhere |
| 1 | `tactician` | **Best single-state choice.** Every target or placement is tried on a cloned state and scored with the evaluator. |
| 2 | `planner` | **Whole-round choices.** Growth option, which track to uncover (looking past "no change" slots), Remarkable draws, cloning, and the commit. The commit is chosen by enumerating every affordable play set: card values from level-1 lookahead, plus threshold bonuses and the innate tier the set's elements reach, minus credits spent. The nominee is the set's most expensive card, since it's free; extra fast plays go to the highest-value cards. |
| 3 | `house` | **Table judgement and rollouts.** The top 6 play sets are each **simulated through Fast → Dusk → Day → Slow**, with tactician-level choices inside, and the best result is played. It also votes for successors by Reign versus Legacy (using the known event in Direct mode), chooses Apply or Breakthrough by comparing immediate value with the Breakthrough's value over the remaining generations, and holds credits according to the house's curve shape. |

## How the engine interprets the rules
Points where the GDD left room, or where the engine simplifies:
- **Player damage pools within a section** for the generation and kills the set of pieces that removes the most threat damage. Leftover damage persists until Time passes.
- **Brace and Contain reduce Collapse damage** before the Decay check, and the reduced damage is dealt to Crew.
- **Unrest adds +1 once** per damage source, including the Crew counter-attack.
- **"Move Crew" works like "gather Crew"**: it pulls Crew into the target section.
- **Remarkable substitution is available every generation** (at most 1). Whether it's gated was an open question.
- **Meridian's Supply Lines does nothing yet**, because no card or innate targets "from a Haven".
- **A tempered Legacy loses its single most costly effect.**
- **The Discovery and cascade choices are made by house 0's bot** (the table).

## Run 1 results (house bots, 2 players, offset pairing, 150 games per pairing)

*Superseded by run 2 in `RESULTS.md` (Keel at 2 plays, retuned pacing).*

| Pairing | Win rate | Avg length (gens) | Main loss |
|---|---|---|---|
| Galvan + Meridian | 94% | 5.4 | Decay 6% |
| Meridian + Vigil | 90% | 5.4 | Decay 10% |
| Galvan + Vigil | 87% | 5.3 | Decay 13% |
| Galvan + Keel | 64% | 6.7 | Decay 36% |
| Meridian + Keel | 61% | 6.6 | Decay 39% |
| Keel + Vigil | 52% | 6.1 | Decay 48% |

Bot ladder, Galvan + Keel (100 games each; house bot confirmed at 300 games):

| Bot | random | tactician | planner | house |
|---|---|---|---|---|
| Win rate | 0% | 5% | 48–53% | 62–63% |

See `RESULTS.md` for findings.
