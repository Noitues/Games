# Handoff — Hex-Nexus Balance Lab

Written mid-Phase-1, at the lead designer's request. Everything below is on
`claude/hex-nexus-multiagent-prompts-aivg93`, pushed.

## 1. Where the lab stands

| phase | state |
|---|---|
| 0 Bootstrap | **complete** — engine, tests, T0/T1, 200-game T1 mirror with 0 anomalies (`batch_0002`) |
| Roster expansion to 25 | **complete** (out of order, on your instruction) — roster v1.1.0, 5 per role, all on budget (`batch_0004`) |
| 1 AI calibration | **complete as evidence, blocked on a decision** — every 4.C check has been run (`reports/ai_acceptance_v1.2.0.md`). Three pass, three fail; the phase cannot be signed off until you rule on the 65% gate. See §4. |
| 2–6 pacing, economy, champion balance, robustness, release | not started |

Versions in play: rules 1.0.0, roster 1.1.0 (25 champions), engine with 94
unit tests, ai 1.1.0 (frozen, as batches 0005–0007 ran it) and ai 1.2.0
(calibrated T2, used from `batch_0008`).

## 2. What was in flight when work paused

Two things were running in the background and are **not** in the repo yet:

| run | state | how to redo it |
|---|---|---|
| `batch_0009` — T2 mirror, 400 games, ai 1.2.0 | **finished and committed** after the handoff was first written; it changed a finding, see below | `python tools/run_batch.py reports/requests/batch_0009.json --workers 4 --baseline reports/batch_0007.json` |
| exploit sweep + acceptance report | **finished and committed**: `reports/ai_acceptance_v1.2.0.{md,json}` | `python tools/ai_acceptance.py --t1vt0 batch_0005 --t2vt1 batch_0008 --mirror batch_0009 --exploit-games 40 --ai 1.2.0 --workers 4` |

Both are pure re-runs: the sim requests are committed, seeds are in them, and
nothing else depends on them finishing. Expect ~35 min and ~25 min on 4 cores.
The acceptance tool writes `reports/ai_acceptance_v1.2.0.{md,json}` and needs
`batch_0009` to exist first.

## 3. The evidence so far

Every number below carries its batch id; all reports are in `reports/`.

**Engine integrity.** Every batch since the fixes runs with **0 anomalies** and
no illegal states. Four real engine bugs were caught by the in-engine
assertions and fixed with regression tests (monster respawning onto an occupied
hex; a wave spawning under a friendly champion; a tile flipping face up
mid-ability invalidating a move target; a destination hex taken between
enumeration and execution), plus one report bug (the role loop overwrote the
priority win rate).

**The 4.C acceptance checks** (`reports/ai_acceptance_v1.2.0.md`):

| check | result | verdict |
|---|---|---|
| T1 beats T0 ≥90% | 97.0% [93.6, 98.6] | PASS |
| T2 beats T1 ≥65% | 58.5% [53.6, 63.2] | FAIL |
| Mirror lands at 50 ± 2% | 48.8% [43.9, 53.6] | INCONCLUSIVE (needs ~2,400 games for that precision) |
| No illegal action | 0 illegal states across every batch | PASS |
| Every ability used >5% under T2 | 47 of 100 below 5% | FAIL |
| Decisions inside the time budget | 7.4s per game; a 2,000-game T2 batch projects to ~4 hours | FAIL |
| No exploit beats T2 >60% (Phase 5 gate) | worst is split-push at 32.5% [20.1, 48.0] | PASS |

The exploit sweep is a genuinely good result: dive 20.0%, farm 30.0%,
split-push 32.5%, objectives 27.5%, turtle 20.0%, cooldown-lock 27.5%, all
against T2 over 40 games each with 0 anomalies. No single strategy pushed to
the extreme breaks the game — the Phase 5 gate is already met.

The two new failures both need a decision rather than more code. **Ability
usage**: 47 of 100 abilities are used in under 5% of the rounds where they are
affordable and have a legal target, which is a kit-design signal now that the
AI is stable — the Designer's brief for Phase 4, with the caveat that T2 is
only ~8 points better than greedy. **Runtime**: at 7.4s per game a 2,000-game
T2 batch takes ~4 hours on 4 cores, and Phase 4 needs ~5,000 games; see §5.5
for the three ways out.

**AI strength.**

| matchup | result | gate |
|---|---|---|
| T1 vs T0 (`batch_0005`, 200) | 97.0% [93.6, 98.6] | ≥90% **PASS** |
| T2 vs T1 (`batch_0006`, 200, ai 1.1.0) | 55.5% [48.6, 62.2] | ≥65% fail |
| T2 vs T1 (`batch_0008`, 400, ai 1.2.0) | 58.5% [53.6, 63.2] | ≥65% **FAIL** |

**Why T2 does not clear the gate — the important finding.** Ten T2 variants
(`reports/calibration/plan_a..d`, 890 games) all landed between 52% and 62%:
wider root, finer opponent model, World Phase resolved at the leaf, sharper
softmax, full round rollout. `tools/search_agreement.py` then measured the
thing that separates an AI problem from a game problem: over 399 decisions the
**searched move differed from the greedy move 45.4% of the time**, giving up
an average of **4.1 points** of immediate value to do so — and won only a few
points more often. The search is not failing to find alternatives; the
alternatives barely matter. A large share of activations in Hex-Nexus look
close to value-neutral.

Plausible structural causes, for the designer rather than the AI backlog:
damage lands in a separate World Phase so nothing can be answered inside a
round; one activation is one champion of five; whole-card cooldown makes the
cost of *any* ability identical (the card is out either way); and 1 hit = 1 HP
with no damage values compresses outcomes.

**Game-level findings already visible** (do not patch these yet — the
Facilitator's triage order puts AI competence first):

- Pacing slipped below band with 25 champions: median **12 rounds** (target
  13–18) in `batch_0004`, `batch_0007`, `batch_0008`. 98.8–99.5% of games end
  by Nexus kill.
- Economy outliers, stable across every batch: quillan 4.7×, sable 3.3×,
  ashwyn 3.0×, ossuar 2.0× the roster-mean AP per round. All are cheap area or
  multi-hit abilities. The likely root cause is §14.2 pricing AREA by hits
  rather than by the chips it can bank.
- Champion spread: quillan 89.2% [84.6, 92.5] vs noctis 8.3% [5.5, 12.4]
  (`batch_0007`, T2 mirror, 600 games).
- **Seat balance is unresolved, not failing.** The two T2 mirrors disagree:
  priority **55.0% [51.0, 58.9]** in `batch_0007` (600 games, ai 1.1.0) but
  **48.8% [43.9, 53.6]** in `batch_0009` (400 games, ai 1.2.0, the calibrated
  T2). They used different T2 configurations, so the honest reading is that the
  earlier 55% was an artefact of the uncalibrated search — high-temperature
  sampling and a leaf that had not resolved the World Phase — rather than a
  first-player advantage that grows with skill. Re-measure on one fixed
  configuration before spending any lever on it.
- **Pacing is worse than the T1 reads suggested**: median **11 rounds**
  [11, 11] under the calibrated T2 (`batch_0009`), against a 13–18 target, with
  100% [99.0, 100.0] of games ending by Nexus kill.

## 4. Decisions waiting on you

1. **The 65% gate (new).** T2 beats T1 by ~8 points, not 15, and the diagnostic
   says depth is not the bottleneck. Three ways forward: (a) lower the gate to
   ~60% and move to Phase 2 on the evidence that greedy play is near the
   ceiling; (b) treat it as a design finding and add decision consequence —
   that touches pillars (World Phase timing, whole-card cooldown), so it is
   yours; (c) keep investing in AI (learned evaluation, deeper search), which
   the agreement data suggests will pay poorly. Recommendation: (a) now and (b)
   as a design conversation, because the balance work does not need a stronger
   AI to proceed — it needs a *stable* one, which T2 is.
2. **RQ-001 / RQ-002** (`log/decisions.md`): can units and towers inside a
   hidden tile be reached at *tile* range? The lab is running the literal yes,
   which makes hidden tiles a trap rather than a haven and widens tower threat
   zones. This shapes the hidden-hexgroup pillar's feel.
3. **RQ-016**: the engine ends a champion's movement when a bump flips a tile,
   where Rules 3.3 lets it continue. Engine simplification only.

## 5. Picking the work back up

```bash
pip install pytest
python -m pytest tests/ -q                 # 94 tests, ~35s
python tools/run_batch.py reports/requests/batch_0009.json --workers 4 --baseline reports/batch_0007.json
python tools/ai_acceptance.py --t1vt0 batch_0005 --t2vt1 batch_0008 --mirror batch_0009 --exploit-games 40 --ai 1.2.0 --workers 4
```

Then, in the Facilitator's triage order:

1. Close Phase 1 with whatever you decide on the gate; record it in
   `log/decisions.md` as a RULE-Q ruling.
2. **Phase 2, pacing**: median length is 12. Gentlest levers first — tower HP
   8→9, then wave size. One lever class, at most 3 changes, with a hypothesis
   and a revert condition (`log/briefs/`, Part 3.2 format).
3. **Phase 3, economy**: the four AP outliers. Prefer a §14.2 recalibration of
   AREA/multi-hit pricing over four separate kit nerfs — they share one cause.
4. **Phase 4, champion balance**: with 5 champions per role each plays 40% of
   games, so ±2.2-point champion verdicts need ~5,000-game batches (RQ-028).
   At T2's current cost that is roughly 5 hours on 4 cores; either budget for
   it, run Phase 4 on T1 (which is 4× cheaper and, per the agreement data,
   nearly as strong), or shrink T2's opponent model for bulk batches.
5. The **priority advantage** (55% under T2) needs its own lever once the AI
   question is settled — it is a §14.3 target in its own right.

## 6. Map of the repository

| path | owner role | what it holds |
|---|---|---|
| `rules/` | Facilitator | the authoritative rulebook and the machine-readable map |
| `roster/` | Designer | champion kits plus a generated card sheet |
| `engine/` | Sim Runner | map graph, state, abilities, phases, batch runner, report builder |
| `ai/policy_v1_1_0`, `ai/policy_v1_2_0` | AI Developer | frozen and current policy packages |
| `tests/` | Sim Runner | 94 tests, one module per rulebook area plus the AI contract |
| `tools/` | Sim Runner / AI Dev | `run_batch`, `ai_acceptance`, `ai_calibrate`, `search_agreement`, `replay_view`, `roster_sheet` |
| `reports/` | Sim Runner | sim requests, batch reports (md + json), calibration results |
| `log/` | Facilitator | decisions (29 RULE-Qs), changelog, briefs, iteration summaries |
| `docs/` | Facilitator | the prompt architecture, lab notes, agent role cards, this handoff |

Anything a new session needs to know that is not in the code is in
`log/decisions.md` (why a rule resolves the way it does) and
`docs/LAB_NOTES.md` (why the engine and AI are built the way they are).
