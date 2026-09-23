# Games — Scene-Deck Engine playtest harness

This branch holds a Monte Carlo playtest harness for the **Scene-Deck Engine**, a Fate supplement
specified in [`RULES_SPEC.md`](RULES_SPEC.md). It is unrelated to anything else in this repository.

The question it measures: does the Scene-Deck Engine make sessions more fun, and make players feel
more woven into the plot, than baseline Fate? And is any benefit caused by player backstory
specifically, or by any structured injection of complications?

| Arm | Rules |
| --- | --- |
| A — Scene-Deck | The full spec: Session Deck, Beat Frames, surfacing compels, tension, Story Piles |
| B — Baseline Fate | High concept, trouble and 3 aspects; the GM improvises complications |
| C — Placebo | Identical to A, but every "player" card drawn is a generic complication |

## Layout

```
RULES_SPEC.md            spec under test (v0.1.0) — never edited mid-batch
CHANGELOG.md             every spec patch and the version it produced
docs/design_notes.md     spec ambiguities that block automation, engine state, pilot plan
harness/
  engine.py              deck, dice, fate points, clocks, tension, stress: pure state machine
  rulings.py             interim rulings for spec gaps (each firing is logged as an AMBIGUITY)
  arms.py                ARM_A, ARM_B, ARM_C and §13 variants
  chargen.py             seeded cohort generation + Latin-rectangle personality rotation
  agents.py              role prompts, visibility, JSON schemas, dice-claim and prompt-leak guards
  llm.py                 claude -p backend (isolated context per call) + response cache + token caps
  scripted.py            zero-token heuristic agents for tests and structural Monte Carlo
  run.py                 one session end-to-end -> runs/<batch>/<run_id>.json
  batch.py               N seeds × arms in parallel, resumable, + blinded paired preferences
  analyze.py             metrics, CIs, paired comparisons, blinded analyst, report, review packet
  schema.json            run record schema
  data/                  world deck (the Sallowmere), placebo complications, chargen tables
  prompts/               player rules summaries (A/C and B), GM interface and baseline rules
  cohorts/               generated character cohorts (source of truth once written)
  tests/test_engine.py   engine rule tests
runs/<batch_id>/         run JSON, _manifest.json, _preferences.json
reports/<batch_id>.md    batch report; reports/<batch_id>_review/ is the human review packet
```

## Usage

```bash
cd harness
python3 tests/test_engine.py                                   # engine rule tests
python3 batch.py scripted-mc --seeds 40 --backend scripted    # free structural Monte Carlo
python3 batch.py pilot-01 --seeds 3 --backend claude_cli --cohort-id cohort-pilot-01 --prefs
python3 analyze.py pilot-01 --review                           # report + human review packet
```

Agents run as separate `claude -p` subprocesses: each has a replaced system prompt, no tools and no
session persistence, so no two agents share a context window. Dice, deck order, fate points and draw
triggers belong to the engine. An agent that states a dice result gets one retry; a second
offence invalidates the run.
