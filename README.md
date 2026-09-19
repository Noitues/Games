# Hex-Nexus Balance Lab

A simulation lab for **Hex-Nexus**, a 2-player tactical board game that distils
League of Legends into a 5v5 skirmish on a 127-hex map.

This repository is the execution of `docs/Hex-Nexus_MultiAgent_Prompts.md`: four
agent roles (Facilitator, Champion & Rule Designer, Champion AI Developer, Monte
Carlo Sim Runner) build a digital version of the game, play it thousands of
times and tune it against the balance contract in Rules section 14.3.

```
rules/     Hex-Nexus_Rules_v1.0.0.md (authoritative) + map_v1.json (Appendix A)
roster/    champion kits as JSON, with a budget worksheet per champion
engine/    the game engine: map, state, abilities, phases, batches, reports
ai/        policy packages implementing the Policy interface
tests/     one test module per rulebook area (pytest)
tools/     run_batch.py: run a sim request, write the report
reports/   requests/batch_*.json (sim requests) and batch_*.{json,md} (reports)
log/       decisions.md (RULE-Q rulings) and changelog.md
docs/      the multi-agent prompt architecture, the map image, lab notes
```

## Running it

```bash
pip install pytest
python -m pytest tests/ -q                                   # 76 unit tests
python tools/run_batch.py reports/requests/batch_0002.json --workers 4 --tests
```

A sim request follows Part 3.4 of the prompt architecture; the report follows
Part 3.5 and is written as both JSON and Markdown into `reports/`.

## Status

Phase 0 (bootstrap) is complete: roster v1.0.0, engine with a full test suite,
T0 and T1 policies, and smoke batches. See `log/changelog.md` for the history
and `reports/` for the data behind every claim.

## The rules in one paragraph

Each player commands 5 champions (Top, Jungle, Mid, ADC, Support) on a hex board
built from 27 flippable tiles. A tile holding one team's units is hidden and
counts as a single space for movement and range; it flips face up when both
teams are inside. Chips are HP *and* AP: every chip a champion knocks off a
minion wave, monster, tower or Nexus becomes 1 AP for its team immediately, and
each team's pool resets to 3 every round. Using an ability puts the champion's
whole card on the cooldown track, so it cannot even move until the card returns.
Champions activate once each per round in snake order 1-2-2-1-1-2-2-1-1-2. Kill
the enemy Nexus to win.
