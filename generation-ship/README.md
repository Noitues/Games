# Generation Ship

A cooperative board game prototype built on Spirit Island's turn structure. Explore/Build/Ravage becomes **Dawn / Day / Dusk**: generations of leaders move down a conveyor, carry each era's crisis with them, and retire to a Wall of Leaders.

## Play the prototype
```
cd generation-ship
python3 -m http.server 8000
# open http://localhost:8000
```
- **Seats:** pick 1–4 players and a house for each seat. Each seat is controlled by a human or a bot (`team`, `house`, `planner` or `tactician`).
- **Rules:** choose Offset or Direct event pairing, the win conditions, a destination and level, and whether to use the Landfall card.
- **Playing:** **Step** runs one phase. **Auto** keeps running until a human decision is needed. **Undo phase** rewinds.
- **Your decisions** appear in the highlighted prompt. Click sections on the map, cards in your hand, or the prompt buttons.

No build step and no dependencies. The browser loads `data/*.json` and the engine in `src/` directly.

## Print and play
Open `print.html` in the browser (served the same way as the prototype). Pick the parts you want, then print or save as a PDF. Cards are poker size (63 × 88 mm), 9 per A4 page, with dashed cut lines. A ready-made copy of everything (59 pages) is in `print/generation-ship-print-and-play.pdf`.

## Repository map
| Path | What |
|---|---|
| `GDD.md` | The game design document: rules, decisions and reasons, balance framework, open questions |
| `houses/` | The eight houses, one sheet each |
| `data/` | Game data: 400 people cards, events, Discoveries, crisis cards, boards, houses, destinations, calibration |
| `tools/` | Deterministic card generators (Python) |
| `src/engine/` | Headless rules engine (shared by the browser and the simulations) |
| `src/ai/` | State evaluation and the layered bots |
| `src/ui/` | Browser prototype |
| `sim/` | Monte Carlo runners, tuners, and results (`sim/RESULTS.md`) |

## Simulations
```
node sim/smoke.js                                    # quick check: every bot level and player count
node sim/parallel.js --games 60 --threads 4          # every 2-house pairing, per-house strength
node sim/parallel.js --players 3 --games 30          # every 3-house combination
node sim/destinations.js --games 30                  # win rate per destination level
node sim/calibrate.js --games 30                     # measure threshold and innate hit rates
node sim/tune-weights.js --games 40                  # self-play tuning of bot evaluation weights
```
