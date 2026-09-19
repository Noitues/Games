# Iteration 0 briefs (Facilitator → agents)

Kickoff received: "Hex-Nexus Balance Lab: begin Phase 0", with
`Hex-Nexus_Rules_v1.0.md` (authoritative) and the map image.

Facilitator reading of Phase 0's exit condition (Prompts Part 5): all unit tests
pass, and a 200-game T1 vs T1 smoke batch runs with 0 anomalies.

## B0-1 → Champion & Rule Designer

Build the initial roster (Prompts 4.B Phase 0 task).
- 10 champions, 2 per role, each with a distinct League archetype.
- Build each to 22 ± 2 with the Rules 14.2 procedure: design the four abilities,
  total their net values, then set HP and Speed to land in the band.
- Every champion needs at least one AP-cost ability usable in most lane spots
  (it protects the 14.3 usage target). Junglers need an efficient camp clear;
  supports need a way to matter without farming chips.
- Icons from Rules 6.3 only. Output `roster/roster_v1.0.0.json` per Part 3.1
  with a budget worksheet per champion.
- Cap DELAY and HASTE at 1 per champion, and name every farming engine
  (an ability whose hits on a wave exceed its AP cost) in its notes.

Delivered: `roster/roster_v1.0.0.json` (+ generated `roster_v1.0.0.md`).

## B0-2 → Monte Carlo Sim Runner

Build the engine and its tests (Prompts 4.D).
- Load the map from Rules Appendix A. Model the hidden-tile movement and range
  graph, flips and flip-back, recall, whole-card cooldown, snake order, the
  chip = AP economy, World Phase timing, the Shop Phase, buff and item cards,
  Dragon and Baron, the protection order, death timers, and the round-20 limit
  with its tiebreak.
- Legal-option generators for every decision in the Policy interface; only the
  engine decides legality.
- Assertions after every step; a unit test per rulebook area, including flip
  overflow, blocked spawns, recall timing, Red Buff targeting and a wave walking
  past its own tower.
- First deliverable: the test report plus a 200-game T0 vs T0 smoke batch
  (`batch_0001`).
- Raise a RULE-Q rather than guessing; implement the most literal reading until
  the ruling lands and label it in the report.

Delivered: `engine/`, `tests/` (76 tests), `tools/run_batch.py`, batches 0001-0003.

## B0-3 → Champion AI Developer

Build T0 and T1 against the engine API (Prompts 4.C).
- T0_random: uniform over legal options, but always take a legal free farm.
- T1_greedy: one shared evaluation function, softmax over the best options at
  the given temperature. It must weigh AP now, chips denied, HP on both sides,
  kill threat and death risk including the next World Phase, structure damage,
  objective control, lane assignment, cooldown exposure, positional safety and
  AP left for the shop.
- Keep per-champion knowledge to a small documented hint set.
- Report the T1-vs-T0 acceptance number (`batch_0003`); T2 and the exploit set
  are Phase 1.

Delivered: `ai/policy_v1_0_0/` (T0_random, T1_greedy, shared evaluation).

## B0-4 → all agents

Two rulings (RQ-001, RQ-002) and one engine simplification (RQ-016) are flagged
for the lead designer in `log/decisions.md`. Work continues on the literal
reading; every report carries the label.
