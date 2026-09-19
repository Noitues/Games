# Iteration 2 briefs (Facilitator to agents)

Phase 1: AI calibration. Exit condition (Prompts Part 5): the acceptance tests
in 4.C pass.

## B2-1 -> Champion AI Developer

Build T2_search and the exploit set (Prompts 4.C).
- T2 looks ahead over the snake order: several of its own activations plus the
  opponent's likely replies, with T1 as the opponent model, under a per-decision
  time budget. Include macro planning: lane assignment by role, jungle routes,
  Dragon and Baron setups, recall timing, shop builds by role.
- Required exploit set: all-in early dive, pure farm-and-scale, split-push,
  objective hoarding, turtle-under-towers, cooldown-lock.
- Keep the evaluation function shared; per-champion knowledge stays a small
  documented hint set. An exploit is a weight profile, not bespoke code.
- Run the acceptance tests and report which of them fail, with batch evidence.

## B2-2 -> Monte Carlo Sim Runner

- Publish the snake order on the state so a searching policy can read whose
  activation comes next. It is public information (Rules 5.2).
- Close two gaps against Prompts 4.D: assists are not tracked, and replays have
  no compact text viewer.
- Add per-policy configuration to the sim request (`p1_config`, `p2_config`) so
  the AI Developer can run calibration variants without editing code.
- Batches ordered: 0005 (T1 vs T0, 200), 0006 (T2 vs T1, 200), 0007 (T2 mirror,
  600, also the ability-usage reference under T2).

## B2-3 -> Champion & Rule Designer

Stand by. No champion patch is approved while AI competence is the open
category: ability usage and the champion win-rate spread cannot be trusted
until T2 passes its acceptance tests. Keep the batch_0004 evidence for the
economy brief that follows (four champions above 1.5x the roster-mean AP, all
cheap area or multi-hit abilities).
