# pilot-01-regress: operator notes (spec 0.2.0 vs 0.1.0)

These notes are the operator's, written after unblinding. The regression re-ran pilot-01's seeds (87940–87942), cohort and prep packets under spec 0.2.0 plus the harness fixes. That is 9 runs, all `complete`, costing about $50.93 including 36 preference judgments.

**Status: stopped at the human review gate again.** The review packet is in `pilot-01-regress_review/`.

## Did the patch work? Yes, on its target metric

| Arm A (n = 3) | 0.1.0 (pilot-01) | 0.2.0 (regress) |
| --- | --- | --- |
| Every player's own card surfaced | **0 / 3** | **3 / 3** |
| Deck draws per session (target 5–8) | 4.0 | 6.0 |
| Guarantee pulls that fired | 0 | 1 per session |
| Scenes per session | 5.0 | 4.3 (the deck ran out in one run, so the climax rule ended it at scene 4) |
| Spotlight Gini, turns / invokes | 0.02 / 0.25 | 0.01 / 0.29 (invoke CI is wide: 0.13–0.52) |
| Mean player FP at end (target 1–5) | 1.42 | 2.33 |

The regression check on spotlight is **no evidence of harm**. Turn Gini is unchanged; invoke Gini moved within noise.

## What got worse, or did not improve

1. **Arm A violations rose from 4.0 to 10.0 per session. Most of the rise comes from better detection, not worse play.** The 18-violation run is mostly GM agent errors the engine now refuses:
   - NPCs named as active opposition without ever being introduced (5 times);
   - "fiction:" triggers reported with their text instead of their ID (2 times);
   - compels naming a card still in the Session Deck (the H4 fix: in pilot-01 this was silently allowed).

   The remaining Referee violations are real GM-quality issues: Story Pile cards drawn after a free compel were not worked into the narration (§6A).
2. **The Referee still judges only 58% of Arm A deck costs as genuinely using the drawn card** (C: 81%), even though the engine's tag check passes 100%. The GM names the right tag but the fiction often doesn't use it. This is the system's core constraint (§3) and it is not being met in spirit.
3. **Paired preferences now favor B over A, 9–3** (pilot: 7–5). A beat C 7–5 and B beat C 7–5. At n = 12 per pair these splits are within noise of the pilot's cycle, but the direction is now consistent: the baseline is preferred.
4. **Tension is still pinned low**: mostly 1 in A and C. The "resolved −1" row is applied generously. This is not addressed yet.
5. Self-reports remain at the ceiling (involvement 6.42 in every arm).

The analyst reported Arm C's "0% all players' backstory" as a negative, but that is by construction: C's surfaced cards are placebos. Read it as the manipulation working, not a failure.

## Suggested next decisions (for the human)

- **§3 cost rule:** tighten it (the cost must quote or paraphrase the tag in the fiction), or have the harness re-prompt the GM when the Referee says the card was not used.
- **Tension (§6):** define "resolved a THREAT" narrowly (the card leaves play), or change the −1 row. This is the second batch pinned at 1.
- **Scale:** these results are at n = 3 per arm. The brief's target is 30 per arm, about $500 at the current per-run cost. A cheaper first step: 10 seeds × 3 arms (about $170).
