# Iteration 2 status (Facilitator to lead designer)

1. **T2 and the six exploit policies are built and calibrated** (ai 1.1.0, then
   ai 1.2.0 after calibration). 94 tests pass; every batch since Phase 0 runs
   with 0 anomalies.
2. **T1 vs T0 passes**: 97.0% [93.6, 98.6] against a >=90% gate (`batch_0005`).
3. **T2 vs T1 fails**: 58.5% [53.6, 63.2] on 400 games against a >=65% gate
   (`batch_0008`), on a tight interval rather than a noisy one.
4. **Depth is not the bottleneck.** Ten variants over 890 games all landed
   between 52% and 62%. The searched move differs from the greedy move 45.4%
   of the time and pays 4.1 points of immediate value to do so, for a few
   points of win rate: a large share of activations look near value-neutral.
5. **That is a design signal, not an AI backlog item.** Candidate causes, all
   pillar-level: damage resolves in a separate World Phase so nothing can be
   answered inside a round; one activation is one champion of five; whole-card
   cooldown makes every ability cost the same; 1 hit = 1 HP compresses outcomes.
6. **Seat balance is unresolved.** The T2 mirrors disagree: priority 55.0%
   [51.0, 58.9] in `batch_0007` (ai 1.1.0) against 48.8% [43.9, 53.6] in
   `batch_0009` (ai 1.2.0, calibrated). Different T2 configurations, so the
   earlier 55% reads as an artefact of the uncalibrated search. Re-measure on
   one configuration before spending a lever. Pacing meanwhile got worse:
   median 11 rounds under the calibrated T2, against a 13-18 target.
7. **All 4.C checks are now run** (`reports/ai_acceptance_v1.2.0.md`): three
   pass, one inconclusive, three fail. The good news is the Phase 5 gate is
   already met - no exploit policy beats T2 (worst is split-push at 32.5%).
   The other two failures are decisions, not code: 47 of 100 abilities are used
   in under 5% of their affordable rounds, and a 2,000-game T2 batch projects
   to about 4 hours on 4 cores against Phase 4's need for ~5,000 games.
8. **Needs your decision**: the 65% gate (lower it to ~60%, treat it as a design
   problem, or keep investing in AI - recommendation is the first plus a design
   conversation), and the still-open RQ-001, RQ-002 and RQ-016.
