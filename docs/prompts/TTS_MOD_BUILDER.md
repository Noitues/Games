# Prompt: build the Hex-Nexus Tabletop Simulator mod

You are the **TTS Mod Engineer** for Hex-Nexus, a 1v1 tactical board game in
which each player commands five champions on a hex map. Your job is to build
a Tabletop Simulator (TTS) mod that humans can use to playtest the game. The
mod takes its rules, map, roster and tuning numbers from this repository, and
it runs the game's bookkeeping so the players can focus on decisions.

## Sources of truth (read these first, in this order)

| What | Where | Notes |
|---|---|---|
| Rulebook | `rules/Hex-Nexus_Rules_v1.9.0.md` | Human-readable rules. Version shown in the mod. |
| Tuning numbers | `engine/config.py` `DEFAULT_CONFIG`, **overlaid with** `config_overrides` from `reports/requests/batch_0074.json` | The settled, designer-approved values: towers 10 / Nexus 15, decay 1 HP every other round from round 3, floors 4 / 6, kill = two current waves, death timers. If the designer adopts 2 / 4 / 6 death timers, use `batch_0075.json` (`death_track_positions` [3, 5, 7]). Never hard-code a number that exists here. |
| Map | `rules/map_v1.json` (coords, hexgroups, north/south structures, monsters, terrain), `docs/hex_nexus_map_v0_7.png` | Axial hex coordinates; the South side is the 180° rotation of the North. |
| Champions | `roster/roster_v1.9.0.json` | 25 champions, 5 roles, stats and Q/W/E/R/L0 abilities as icon steps (HIT, AREA, LINE, SHIELD, HEAL, DASH, BLINK, ROOT, SLOW, PUSH, PULL, REVEAL, HASTE...). |
| Rule semantics | `engine/game.py` (round structure, upkeep order, waves, decay), `engine/resolve.py` (targeting, protection order, hits, chips to AP, kills, death track, tower reward), `engine/abilities.py` (ability plans, AREA/LINE shapes, movement), `engine/hexmap.py` (distance, hexgroups, hidden tiles, blocking), `engine/items.py` (shop), `engine/state.py` | Where the rulebook and the engine disagree, the **engine plus config is what was simulated and balanced**. Implement the engine's behaviour and list every discrepancy in `tts/RULES_DISCREPANCIES.md` for the designer. |
| Executable spec | `tests/` (pytest, ~180 tests) | Treat these as the specification of edge cases (respawn placement, hidden tiles, protection order, decay floors, kill rewards). |

Do not change the engine, the rules or the roster. This work only consumes them.

## Architecture

TTS scripts in **Lua** (MoonSharp) and cannot run Python. Build it in three layers:

1. **Exporter (Python, in this repo): `tools/tts_export.py`.** Reads the sources
   above and generates:
   - `tts/build/data.lua`: map, roster, items and config as Lua tables, stamped
     with the rules, roster and config versions and the git commit.
   - Card and token images (Pillow): champion cards showing stats and the
     Q/W/E/R/L0 icon steps; item, buff, Dragon and Baron cards; tower and Nexus
     HP dials. Lay cards out as TTS deck sheets (≤ 10×7 per sheet).
   - `tts/build/HexNexus_<rules>_<roster>.json`: the TTS save file, with every
     object, its position on the hex grid, the Global Lua script and each
     object's Lua script inlined.

   One command rebuilds the whole mod after any rules or roster change:
   `python tools/tts_export.py --rules 1.9.0 --roster 1.9.0 --config reports/requests/batch_0074.json`.
2. **Lua referee (in the mod).** A game-state machine in the Global script:
   - **Upkeep, fully automated in the engine's order:** round tracker and
     priority, cooldown tracks shift down, respawns, fountain heal, structure
     decay, AP refresh, minion wave movement then spawns, monster respawns,
     flip-back.
   - **Action Phase, assisted:** a player picks a champion. The referee
     highlights legal moves and targets, taking into account range, hidden
     hexgroups, blocking, stacking and protection order. It checks the ability
     is affordable and off cooldown, resolves hits, moves chips to the AP pool,
     handles kills (death-track position, kill reward in waves), tower falls
     (tower reward) and the Nexus win.
   - **World, Shop and Win Check:** towers shoot, the shop, the round-20
     tiebreak.
   - **Two modes, a toggle on the table:**
     - *Assist* (default for playtests): pieces move freely; the referee
       validates and warns.
     - *Enforce*: illegal actions are rejected.
3. **Parity harness.** Export golden scenarios from the Python engine: a
   starting state, one action, and the expected resulting state. Cover every
   icon and every rule the tests cover. Run them against the Lua referee in a
   plain Lua 5.2 interpreter outside TTS (`tts/tests/run.lua`). The referee
   core must be pure Lua with TTS calls isolated behind an adapter, so it runs
   headless. The mod is not done until parity passes.

**Optional layer 4, bridge (stretch goal).** `tools/tts_bridge.py` talks to TTS
through its External Editor API on localhost (TTS listens on 39999; the bridge
listens on 39998). It lets the Python engine:
- Validate the live game state each round and flag desyncs.
- Play one side with an AI personality (`ai/policy_v1_5_0`, e.g. `T2_sieger`,
  `SM_g2_lane6`) for solo playtests.
- Record logs.

## Components on the table

- **Board:** the hex map and the hexgroup tiles, which flip. Hidden tiles use
  face-down tiles and hidden zones per player colour, so concealment works for
  real.
- **Pieces:** 10 champion tokens with name plates; minion waves as chip stacks
  in team colours; towers and Nexus showing current HP and floor; monster
  tokens (camps, Dragon, Baron).
- **Cards and tracks:** champion ability cards with a cooldown track per team,
  showing positions and the death track; Dragon, Baron and buff cards; the
  shop and item deck.
- **Pools and counters:** per-team AP pools as poker chips from a shared
  supply; the round tracker and priority marker.
- **Always-visible panel:** round, phase, whose action, AP per team, active
  rules / roster / config version, and the decay schedule.

## Playtest telemetry (the point of the mod)

- **Event log.** Log every action and every end-of-round snapshot. The
  per-round snapshot must use the same schema as `GameResult.trace` in
  `engine/run.py`: round, AP by source per team, kills, towers lost, Dragons,
  Baron. Human games can then be read by `tools/phase_read.py` next to the
  simulations.
- **Game record.** Write the log as JSONL at game end, one game per line, with
  picks, winner, end reason and rounds. Deliver it by TTS WebRequest to a small
  local collector (`tools/tts_collect.py`), with a copy-to-notebook fallback.
- **Feedback card.** Add a post-game feedback card: fun 1–5, "which phase
  mattered", confusing rules (free text). It is saved into the same record.

## Milestones (commit and push after each; report what works and what doesn't)

- **M0, static mod.** Board, all components and cards generated from the
  repo; playable by hand with the rulebook. Save file loads in TTS.
- **M1, bookkeeping.** Automated Upkeep, trackers, AP pools, decay, death
  track, wave spawn and move, monster respawn, round-20 tiebreak.
- **M2, action assist.** Legal move and target highlighting; ability
  resolution for every icon; kill, tower and Nexus handling; parity harness
  green.
- **M3, telemetry.** Event log, JSONL export, collector, feedback card; one
  full hot-seat game played start to finish with the log read by
  `phase_read.py`.
- **M4 (stretch).** Bridge: desync check and an AI opponent.

## Rules for this work

- Work on the branch you are given; commit with clear messages; no pull request unless asked.
- **Isolation:**
  - Put all mod code under `tts/`, plus the new `tools/tts_*.py` scripts.
  - Do not edit `engine/`, `rules/`, `roster/`, `ai/`, or existing tests.
- **Single source of truth.** Nothing that exists in the repo may be retyped
  by hand into Lua or images: map, numbers, champions, items. It is
  generated, so the mod follows every future patch with one rebuild.
- **Visible version.** The mod shows its rules, roster and config version and
  commit on the table at all times.
- **Asset hosting.** TTS loads images from URLs. Generate them into
  `tts/build/assets/` and document the hosting step in `tts/README.md`: Steam
  Cloud via TTS's Cloud Manager, or another public host. Use local file paths
  while iterating.
- **Designer questions.** Ask before deciding anything the designer owns:
  rules ambiguities, the death-timer choice, and how hidden information is
  shown to a spectator. Record open items in `tts/RULES_DISCREPANCIES.md`
  rather than inventing rules.
- **Deliverables:**
  - `tts/README.md`: build, load, host, play, collect logs.
  - `tts/PLAYTEST_GUIDE.md`: a one-page quick start for testers.
  - The generated save file.
  - The parity test results.
