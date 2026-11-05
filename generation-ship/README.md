# Stewards of the Long Voyage

A cooperative board game prototype built on Spirit Island's turn structure. Explore/Build/Ravage becomes **Dawn / Day / Dusk**: generations of leaders move down a conveyor, carry each era's crisis with them, and retire to a Wall of Leaders.

## Play the prototype
**Hosted:** https://claude.ai/artifact/EPujDZ3TFuRQtGjxB49YKe (private to the owner until shared from its Share menu). To update it after code changes, run `python3 tools/build_artifact.py` and republish `dist/artifact.html` with the same supporting files.

**Locally:**
```
cd generation-ship
python3 -m http.server 8000
# open http://localhost:8000
```
- **Seats:** pick 1–4 players and a house for each seat. Each seat is controlled by a human or a bot (`team`, `house`, `planner` or `tactician`).
- **Rules:** choose the win conditions, a destination and level, and the Landfall variant (off, begin when ready, or shuffled into Stage III).
- **Playing:** **Step** runs one phase. **Auto** keeps running until a human decision is needed. **Undo phase** rewinds.
- **Your decisions** appear in the highlighted prompt. Click sections on the map, cards in your hand, or the prompt buttons. The active house's panel is outlined.
- **Layout:** **Compact view** (the default) fits a 1080p or 1440×900 screen; **Roomy view** shows full card text everywhere.
- **Playtest aids:**
  - a Purpose meter (progress to the next Discovery and to the next Understanding tier);
  - an **Active effects** panel: Wall bonuses, Breakthroughs waiting under leaders, the Steward's Reign, the Elder's Legacy, crisis, destination, Landfall, and the free elements each house gets;
  - a threat forecast on the map: red rings mark sections that Collapse, with predicted damage and Decay warnings; arrows mark Grow;
  - a commit planner: cost, nominee, fast plays, card thresholds, elements and innate tier;
  - a phase guide and a rules quick reference;
  - **Hint** shows what the house bot would do;
  - **Undo decision** takes back your last choice; **Undo phase** rewinds a whole phase.
- **End of game:** a summary (result, Wall, per-house stats), a notes box, and a playtest record. Save it in the browser, or copy one or all records to the clipboard.
- **Saving a game:** Save downloads the game file and copies it to the clipboard (the hosted page blocks downloads). Load accepts a saved file. The game autosaves, and "Resume last game" appears on the setup screen.
- **Test:** `test/ui-playthrough.cjs` plays full hotseat games in a headless browser (random choices, hints and undos).

No build step and no dependencies. The browser loads `data/*.json` and the engine in `src/` directly.

## Print and play
Open `print.html` in the browser, served the same way as the prototype. Pick the parts you want, then print or save as a PDF. A ready-made copy is in `print/stewards-print-and-play.pdf`: A4, with the Wall on landscape pages, and the 150-card playtest deck (tick "All 400 people" for the full deck).

The kit uses the Retro art from `art/source/retro/` and the icon set from `art/icons/`. Card effects are drawn from `art/icons/effects.json`; the art tools own the icons and art, while this repo owns the data and layout. It contains:
- **Cards (63 × 88 mm, 9 per page):**
  - people cards: name, cost, guilds, target, effect, bonus, Reign, and the Legacy plaque;
  - event cards, laid out to tuck under their leader;
  - Discoveries, with their Breakthrough;
  - Ship in Crisis cards;
  - card backs, to print duplex behind the people cards.
- **House boards:** the typeset art where it exists, otherwise a layout built from the data with icons.
- **Ship boards A–D:** printed at 90 % on A4, so all boards still dock; tick "100 % (A3)" for true scale. Each board shows section IDs, type icons and starting pieces, plus the void crescent.
- **Wall of Leaders:** three panels for the top layer (cut the windows and a slit per slot) plus a backing layer.
- **Tokens:** a 16 mm punch sheet.
- **Reference:** destinations, a rules summary and the icon glossary.

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
