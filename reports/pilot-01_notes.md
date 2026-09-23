# Pilot-01: operator notes

What follows was written by the harness operator (Claude Code) after unblinding. The analyst's blinded conclusions are in `pilot-01.md`.

**Status: stopped at the human review gate.** No spec patches and no further batches until a human has read `pilot-01_review/` and replied.

## Batch

- 3 seeds × 3 arms = 9 runs on one cohort (`cohort-pilot-01`, LLM-generated). All 9 finished with status `complete`. No dice-claim retries, no invalid runs, no prompt-leak assertions.
- Models: GM, Referee and Analyst `claude-sonnet-5` (effort medium); players and Interviewer `claude-haiku-4-5` (effort low).
- Cost: 16.3M tokens, about $48.44 including the 36 blinded preference judgments. That is about $5.40 and 30–60 minutes per run with 5 runs in parallel.

## Structural findings (n = 3 per arm: directional only)

1. **The backstory guarantee never fired, and no Arm A session surfaced every player's card (0/3; the spec's target is 100%).**
   - The GMs ended most scenes after 1–2 rounds, so Arm A drew only about 4 cards per session (the target is 5–8).
   - Every Arm A session ended with 3 cards still in the deck. The §4 guarantee triggers only "when the deck is down to 2 cards", so it never triggered.
   - This is a spec gap, not a harness bug: the guarantee depends on the deck actually being drawn down. Candidate for a spec patch after review (for example, the guarantee also fires at the start of the final scene). It is backed by all 3 A runs plus the scripted Monte Carlo, but the brief requires the human gate first.
2. **Arm C drew more (5.7 per session) and surfaced more placebo cards (4/4 in 2 runs).** More ties happened to fall in C. With n = 3 this is noise-level.
3. **Costs built from drawn cards: engine and Referee disagree.**
   - The engine's tag check passes 93–94% of the time: the GM names a real tag of the drawn card.
   - The Referee judged only 51–61% of those costs as actually using the card in the fiction.
   - This gap is the point of the "cost must use the drawn card" rule, so it is worth a human look at the transcripts.
4. **Tension drifted to the floor.** It reached 1 in most A and C scenes: GMs applied the −1 "resolved" row generously, and clocks rarely advanced. The target is mostly 2–5.
5. **Self-reports sit at the ceiling** (6.3–6.9 out of 7 in every arm) with no separable differences.
6. **Paired preferences form a cycle:** B beat A 7–5, A beat C 8–4, and C beat B 8–4. Consistent with noise at n = 12 per pair.
7. **Only 3 lurker observations in total (1 per arm).** The key lurker comparison needs the target scale (10 per personality per arm).

## Harness issues found (fix before the next batch; none change the spec)

Most Referee ambiguity and violation entries are **logging artifacts**, not rule gaps.

- **H1.** Compel and concession events do not log the fate-point delta or balance. The Referee repeatedly flagged "accepted compel but no +1 FP" as a violation. Add `fp_change` and the running balance to every FP-affecting event.
- **H2.** Log order puts a deck draw, card-leaves-play or clock event before the roll row that caused it. Log the roll first, or link the rows with a `caused_by` field.
- **H3.** Story-pile Weight changes, module deployments and GM free-invoke grants are not logged as events, so the Referee cannot audit them.
- **H4.** Real engine bug: a free (non-deck) compel could name a card that was sitting in the Session Deck (§3/§11: not live). Refuse it and log a violation.
- **H5.** GMs tried to use scene aspects the players had created as passive-opposition tags; the engine refused, correctly. Say so explicitly in `gm_interface_*.md`.
- **H6.** GMs end scenes after round 1 about half the time. That is a legitimate GM choice, but it starves the deck, so decide whether it belongs to the rules (see finding 1) or to the GM prompt.
- **H7.** Referee input: pass the §3 "success with style on create advantage" boost/peek interaction explicitly. It was raised 3 times and is a real gap: can the player take the CA's 2 free invokes *and* the deck peek?

## Ambiguities raised ≥3 times (spec-patch candidates per the brief's rule)

AMB-12 (stress box values, 9), AMB-01 ("Attention" undefined, 6), AMB-22 (GLOBAL free invoke, 6), AMB-19 (tie on attack, 5), AMB-23 (major-cost attack, 3), and the Referee's §3 create-advantage + peek interaction (3). The engine fires AMB-12 once per run by construction, so its count only reflects runs, not a gap being hit; AMB-01 is likewise logged once per deck run. The brief makes all of these eligible for a spec patch, but not before the human gate.
