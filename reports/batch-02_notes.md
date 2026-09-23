# batch-02: operator notes (spec 0.3.1)

These notes are the operator's, written after unblinding. The batch ran 12 sessions: 10 in Arm A, plus 1 each in B and C as references on the first seed. It used two fresh LLM-generated cohorts (one per 5 seeds) and the blind per-session judge. All 12 runs finished with status `complete`, for about $46.

**Status: stopped at the human review gate.** The review packet is in `batch-02_review/`.

A duplicate batch process ran for about 20 minutes early on (my launch error) and was killed. Every final run file comes from the surviving process; the duplicate cost roughly $5–10 extra.

## The v0.3.x rule changes, measured on 10 Arm A sessions

| Arm A | pilot-01 (0.1.0) | regress (0.2.0) | batch-02 (0.3.1) |
| --- | --- | --- | --- |
| Every player's own card surfaced | 0/3 | 3/3 | **10/10** |
| Referee: cost actually used the drawn card | 61% | 58% | **90%** |
| Cost text uses its tag (engine check, after rewrite) | — | — | 96% (4.5 rewrites per session) |
| Tension values seen | mostly 1 | mostly 1 | **2–6, mostly 3–4** |
| Rule violations per session | 4.0 | 10.0 | 4.8 |
| Cost / minutes per session | $5.4 / 45 | $6.3 / 55 | **$4.0 / 32** |

- **§3 "cost must use the tag" works, but the GM misses it often.** About 4.5 costs per session needed a rewrite. The Referee now agrees that 90% of costs really use the drawn card.
- **§6 tension moves in both directions** and never pinned at 1. Distribution: 2 ×8, 3 ×24, 4 ×16, 5 ×9, 6 ×3.
- **Deck draws averaged 4.6 per session**, still below the 5–8 target. The v0.2.0 guarantee is what delivers 100% surfacing.

## Blind judge

The judge scored each session alone, from a story-only, redacted transcript.

| Score (1–10) | A (n=10) | B (n=1) | C (n=1) |
| --- | --- | --- | --- |
| overall | 6.7 [6.4, 7.0] | 6.0 | 5.0 |
| engagement | 6.8 | 6.0 | 5.0 |
| player agency | 6.1 | 5.0 | 4.0 |
| backstory score | 7.7 | 8.0 | 7.25 |
| every player's backstory "used" | 10/10 | 1/1 | 1/1 |

- **With one B and one C session, A cannot be compared to them statistically.** A's scores sit above the single B and C sessions, but that is only suggestive.
- **The judge's "backstory used" measure hits the ceiling in every arm.** LLM players bring their own backstory into their dialogue unprompted, so even baseline Fate (B) scores 100% "used". The judge therefore cannot see the deck's backstory effect with this measure. It needs a sharper question, for example "did an *event the players did not start* come from a character's background?", or the structural metric (own card surfaced: A 10/10, and not applicable to B or C by construction).
- **Lurkers get less:** their backstory score is 6.0, against 7.7 for everyone in Arm A.

## Next decisions (for the human)

1. **Sharpen the judge's backstory question**, so that player-initiated backstory talk doesn't count.
2. **Size the B and C comparison.** One reference session each gives no power for A-vs-B or A-vs-C claims. At about $3–4 per session, 5 each would add about $35.
3. **Deck draws below target (4.6).** Accept it, since the guarantee covers surfacing, or shrink the deck. The spec §13 variant is 2 GM cards + 1 per player.
