# Rewarding the phases in order (RQ-049, proposal)

The lead designer's target: a game moves through four phases, and each one
pays for its own play.

| # | phase | rounds | what should pay |
|---|---|---|---|
| 1 | Laning | 1-4 | last-hitting waves, jungle camps |
| 2 | Sieging and objectives | 5-8 | tier-1 towers, Dragon |
| 3 | Team fights and sieging | 9-12 | champion kills, tier-2 towers |
| 4 | Baron and ending | 13+ | Baron, then the Nexus |

## Why it does not happen today

Under rules 1.8.0 with tower 4 / Nexus 8 (RQ-048), the first tower falls in
round 4 and the sieger beats a laning opening 60-40 (RQ-048c). Every structure
is open from round 1, so a team that walks waves into towers skips phases 1-3
and the Baron is optional: the Nexus falls without it. Nothing in the rules
says what order things happen in; only HP does, and HP is exhausted as a
lever (RQ-038).

## The proposal: gates, not HP

Four config knobs, all off by default, so today's game is unchanged until the
designer adopts them (`engine/config.py`):

| knob | value read | effect |
|---|---|---|
| `tower_unlock_round` | tier 1: round 5, tier 2: round 9 | a tower takes no damage before its round - laning cannot be skipped |
| `last_hit_ap` | 1 | a champion that removes a wave's last chip gains +1 AP - laning pays for skill, not only presence |
| `nexus_needs_baron` + `nexus_unlock_round` | true, 16 | the Nexus takes damage only from the team holding the Baron card, or from anyone from round 16 - the Baron is the ending, and the clock stops a stalled game |
| Baron spawn | round 10 (was 7) | the Baron appears as phase 3 starts, so fights happen over it |

Dragon (spawn 3, reusable card) already sits in phases 1-2; the tier-2 gate at
round 9 puts the second siege into the fight phase.

A matching AI personality, `SM_g3_phase` (`ai/policy_v1_4_0/machines/gen3.json`),
plays the target order - laner, then sieger/objective from round 5, brawler
after a won fight from round 9, objective when the Baron is up from round 10,
sieger once it holds Baron - so the read shows whether playing the phases in
order beats ignoring them.

## How it is judged

`tools/phase_read.py` reads the per-round trace every game now carries and
reports, per batch:

1. **Where AP comes from in each window** (farm / towers / kills, as a share of
   earned, non-base AP). Pass: farm leads rounds 1-4, towers are a material
   share in 5-8, kills lead or match in 9-12.
2. **Does the phase leader win?** Win rate of the team ahead on farm at round
   4, on towers taken + Dragons at round 8, on kills in rounds 9-12, and of the
   Baron holder. Pass: every leader wins above 50% (the phase matters) and none
   above ~80% (it does not decide the game on its own).
3. **Firsts in order**: median first kill / first tower / first Dragon / Baron
   round rising through the phases.
4. **Pacing**: median 13-18, Nexus kills above 90% (the band RQ-038 missed).
5. **Personality**: `SM_g3_phase` at or above the sieger under phase rules, and
   no single personality above 60%.

Runs: `batch_0059` (today's rules) and `batch_0060` (phase rules), same seed
and field (T2_sieger, SM_g2_lane6, SM_g3_phase), 1,600 games each, paired by
seed and draw.

Nothing here goes into the rulebook until the designer rules on it.
