# Changelog

Every rule patch to `RULES_SPEC.md`, with the spec version it produced. Harness-only changes are listed separately.

## Spec

### 0.2.0 — 2026-09-23
- **§4 Backstory guarantee** now also fires **at the start of the session's final scene**, pulling every player card still in the deck, and **during the final scene** if the deck reaches 2 (the card is resolved at once). A guarantee Beat Frame is explicitly forced (it overrides §7's "never forced" and replaces that scene's test). Pulled cards beyond the frame's open blanks surface at the start of the scene as a memory, messenger, news or omen.
- **Evidence:** pilot-01 had 0/3 Arm A sessions with every player's card surfaced (target 100%). All three ended with 3 cards still in the deck, so the "down to 2 cards" condition never triggered. Scripted Monte Carlo (40 seeds) went 97% → 100% under the patch, with turn and invoke Gini unchanged (0.08 / 0.36).
- Resolves interim rulings AMB-02 and AMB-25, which the engine no longer fires.
- Regression on the pilot's seeds (`pilot-01-regress`): Arm A all-players-surfaced 0/3 → 3/3; draws 4.0 → 6.0 per session; turn Gini 0.02 → 0.01; invoke Gini 0.25 → 0.29 (within noise). No spotlight regression. See `reports/pilot-01-regress_notes.md`.

### 0.1.0 — 2026-09-22
- Initial spec as supplied. No patches yet: the brief allows patches only between batches, after the human review gate, and only on repeated structural evidence (a rule with 3 or more ambiguities).

## Harness

### 2026-09-23
- Initial harness: engine, arms (A, B, C and §13 variants), chargen, run, batch, analyze, schema, scripted backend and engine tests.
- Interim rulings AMB-01…AMB-26 (see `docs/design_notes.md` and `harness/rulings.py`).
- Per-role thinking effort for agents (`llm.py`). Players and interviewer run at low effort, GM, referee and analyst at medium; the first probe spent about 4k hidden tokens per call.

### 2026-09-23 — pilot-01 (spec 0.1.0)
- 9 runs, all complete. See `reports/pilot-01.md`, `reports/pilot-01_notes.md` and the review packet `reports/pilot-01_review/`.
- No spec patches: stopped at the human review gate.

### 2026-09-23 — fixes after pilot-01
- H1: every event row carries `fp_balances` and `gm_fp`; compels, concessions, rolls and hostile payouts carry `fp_change`; rolls carry `gm_fp_spent`. Hostile payouts are one row per player.
- H2: a roll's row is logged before the draw, clock mark or card-leaves-play it causes; those rows carry `caused_by`.
- H3: Story Pile weight changes, module deployments and GM free-invoke grants are logged as events.
- H4: engine bug fixed — a free compel naming a card in the Session Deck (or set aside, or not the player's) is refused and logged as a §3/§11 violation.
- H5: GM interface states that only face-up GM/GLOBAL card tags can set passive difficulty, and that compels may not name deck cards.
- H7: new interim ruling AMB-27 (success with style on create advantage gets both the 2 free invokes and the deck peek), fired each time it happens.
- The Referee prompt explains the new log fields.
- H6 (GMs ending scenes after one round) was deliberately not changed. The v0.2.0 guarantee addresses its consequence, and forcing longer scenes would bias the GM.
