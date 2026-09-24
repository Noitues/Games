# Handoff — Hex-Nexus Balance Lab

Second handoff, written 2026-09-24 at the lead designer's request. Everything
is on `claude/hex-nexus-multiagent-prompts-aivg93`, pushed. **Nothing is
scheduled.** Two worker sessions (`batch_0051`, `batch_0053`) were within
minutes of finishing when the pause was called; each pushes its own three
report files to the branch when it completes, so pull before reading §3.

## 1. Where the lab stands

| phase | state |
|---|---|
| 0 Bootstrap | complete |
| 1 AI calibration | closed on RQ-031 |
| 2 Correctness and pacing | correctness: two placement bugs found by the exploit sweep and fixed (RQ-043). **Pacing: the open blocker.** Under the ruled economy (rules 1.8.0) towers only fall to basic attacks and waves, and games stopped ending. Tower HP and Nexus HP are being swept back into band; see §3. |
| 3 Economy | **the pillar is ruled** (P-0010: structures are never ability targets, structure chips are not AP, a tower pays one round of income). The five AREA income engines are two-thirds fixed by the AREA ruling (P-0012) and the rest is in flight as a kit lever (P-0013, roster 1.7.0, unread). |
| 4 Champion balance | one 4,000-game read taken under the **old** rules (`batch_0044`, RQ-041). It is the shape of the problem, not a number to tune against: everything must be re-read on 1.8.0 once games end again. |
| 5 Robustness | gate met on the settled field (`batch_0045`, RQ-043), with a caveat: the exploit profiles are T1-greedy weight sets and should be rebuilt on T2 before a final read. |
| 6 Release candidate | not started |

Versions: rules **1.8.0**, roster **1.7.0**, ai **1.4.0**, **165 tests** (~4m),
all passing.

`engine/config.py` defaults sit on the 1.8.0 side (`abilities_hit_structures`
False, `structure_chips_pay` False, `tower_kill_ap` 3, `area_center` True,
`dragon_card` {hits 2, cooldown 3}, `dragon_ap_each` 0, `baron_permanent`
True). Each is a switch; older requests reproduce by overriding. Three values
live only as `config_overrides` in every request since `batch_0038` and are
**not** defaults: `tower_hp` (config still says 11), `kill_ap` 3,
`death_band_bonus` 1. Copy them forward.

## 2. The rulings this session and what each did

The lead designer ruled on RQ-039/041/042/045 in the morning. Each ruling is
a patch with a pre-registered record in `log/patches/`.

| patch | ruling | read | result |
|---|---|---|---|
| **P-0010** (pillar) | structures are never ability targets; only L0 and waves damage them. Structure chips go to the supply. A tower that falls pays the taking team one round of income (3 AP); the Nexus pays nothing. | `batch_0046` vs `batch_0039` | the rule is the designer's and stands; **at tower HP 16 games stopped ending** (1 Nexus kill in 120). The AREA engines survived on wave and monster chips. |
| **P-0011** | Dragon card is a reusable Red Buff (2 hits adjacent, cooldown track 3, at most 2 held, no AP). Baron empowers waves for the rest of the game. | `batch_0047` vs `batch_0046` | direction right (Dragon secured 51→55%, Baron 50→52%, objective personality 38→43%); verdict deferred until games end. |
| **P-0012** | an AREA is a radius-1 disc around a centre the player places within the step's range; Longbow moves the centre, never the blast. | `batch_0050` vs `batch_0048` | every engine's income down a third; pallas back to the mean; sable, wisp, ashwyn, quillan still 1.6–1.9× the roster mean. |
| **P-0013** (roster 1.7.0) | cooldown 2 on the four remaining engines' AREA ability (sable W, wisp W, ashwyn W, quillan R), nothing bought back, exceptions declared. | **unread** — `reports/requests/batch_0054.json` is written | expected to halve the engine rate; pallas, whose AREA already had cooldown 2, sits at 1.01× and is the evidence. |

The Dragon card's *effect* is the lab's default for "reusable on a 2–3 round
cooldown"; the designer named the timing, not the effect.

## 3. Pacing under the ruled economy — the current blocker

With abilities unable to touch structures, tower HP 16 (a placeholder from
the old economy) cannot fall. Read so far, all on the personality field, seed
3801, full 1.8.0 rules from `batch_0048` on:

| batch | tower HP | Nexus HP | AREA | Nexus kills | median length | first tower falls |
|---|---|---|---|---|---|---|
| 0046 | 16 | 12 | old | 1% | 20 | round 16 |
| 0048 | 8 | 12 | old | 30% | 20 | round 11 |
| 0049 | 6 | 12 | old | 49% | 20 (p10 15) | round 8 |
| 0050 | 8 | 12 | centred | 15% | 20 | round 12 |
| 0051 | 4 | 8 | centred | *pull and read* | | |
| 0053 | 6 | 8 | centred | *pull and read* | | |

Targets: median 13–18 and Nexus kills above 90%. Until games end, every
personality and champion number is a round-20 tiebreak number (towers
destroyed, then structure HP) and says nothing; the sieger's 87–97% in these
batches is that artefact. Both objectives already win more under 1.8.0 than
they did under 1.7.0 even in this broken field.

If 0051/0053 do not reach the band, the levers left, in the order the lab
would try them: L0 dealing 2 hits to structures (a "siege hit"), waves dealing
2 hits to structures by default (the Baron effect made standard), fewer
towers per lane. All three are rules changes and belong to the lead designer;
`tower_hits_champion` (towers hitting harder) is the designer's own fallback
if the sieger is still too strong once games end.

## 4. The findings that govern the design

- **The game has one strategy** (RQ-037, confirmed three ways: hand-written
  personalities, an AP lever that landed and changed nothing, and a bred
  state-machine AI that converged on sieging — RQ-040). This was measured
  under 1.7.0; whether 1.8.0 changes it is exactly what `batch_0054` and the
  reads after it will say. Do not assume the sieger still dominates.
- **Income was win rate** (RQ-041): under 1.7.0, income per round and win
  rate correlated at 0.6 across the roster and the five economy outliers
  were five of the six champion outliers. The designer traced the income to
  two things that were never intended — abilities hitting towers for AP, and
  AREA as a wide disc — and ruled both out.
- **The old-rules champion read** (`batch_0044`, 4,000 games): Jungle and
  ADC balanced; Support (wisp 77%, corvane 27%) and Top (bastion 75%) broken;
  Mid split. bastion is the one outlier that was never an income story (0.26
  deaths a game). Treat this table as the shape to re-check, not as targets.
- **South wins 53.2%** over 4,000 seat-swapped games (RQ-042): Dragon sits a
  hex nearer South and is the objective teams take. Open, designer's.
- **No exploit beats the field** (RQ-043): best 21.9%, five at 0%, fog-snipe
  0% under reveal radius 2. Caveat above.
- **Pacing in a mixed field vs a sieging field** (RQ-038): under 1.7.0 the
  reveal-radius-2 ruling broke pacing only for non-sieging personalities;
  when both sides sieged, pacing passed. Under 1.8.0 it is broken for
  everyone until the HP pass lands.

## 5. Open questions for the lead designer

1. **Pacing lever beyond HP** if tower 4 / Nexus 8 is not enough (§3).
2. **AREA engines beyond cooldown** if P-0013 leaves any above 1.5×: AREA
   cost 2 is the next kit lever; the design budget prices AREA at 6 a hit.
3. **RQ-042**, the map: move a pit, compensate North, or accept 53–47.
4. **Exploit profiles on T2** before Phase 5 is called final.
5. Nothing else is waiting on a ruling. RQ-038 in its 1.7.0 form is moot
   once the 1.8.0 pacing lands.

## 6. Things I got wrong, so they are not rediscovered

- **Anchors as pool members, then anchors only against machines.** In the
  state-machine generation 1 each pair met 2–14 times; in generation 2 the
  fix (anchors drawn into half the games) made overall win rates
  non-comparable between anchors and machines, since anchors never met the
  weak `T2_search`. A Bradley-Terry fit over all pairings (script in the
  RQ-040 entry) is the honest ranking for a mixed field; use it or a
  head-to-head confirmation, never the overall column.
- **Tower HP 16 was never confirmed** and became the wall the moment
  structures stopped taking ability damage. Any pacing number under a rules
  change is suspect until games end.
- **AREA was a disc, and the rulebook's own text said "at your feet"**; the
  Longbow interaction made it 19 hexes and nobody had read the two together.
  When the designer asks "where is the income coming from", trace it to the
  step, not the champion.
- **Two batches launched ten minutes before a ruling amended the patch**
  (the tower reward); they were killed and relaunched. Ask "is the ruling
  complete?" before spending an hour of compute.
- **`pkill -f` with a pattern that matches the calling shell kills the
  shell.** Match on the process, not the command text.
- **The exploit profiles are T1** and their 0% is partly T1 vs T2.

## 7. Picking the work back up

```bash
pip install pytest
python -m pytest tests/ -q                                            # 165, ~4m
python tools/run_batch.py reports/requests/batch_0054.json --workers 4 --dump-raw --baseline reports/batch_0053.json
```

In order:

1. **Pull and read `batch_0051` and `batch_0053`** (tower 4/Nexus 8, tower
   6/Nexus 8; both should have pushed). Pick the pair that puts median length
   in 13–18 and Nexus kills above 90%. If neither does, §3 lists the next
   levers, and they are the designer's.
2. **Run `batch_0054`** (roster 1.7.0, P-0013) on that pair — edit its
   `tower_hp`/`nexus_hp` first; it carries 6/8 as a placeholder. Judge P-0013
   against the batch with the same HP and roster 1.6.0, per the record. If
   any engine is still above 1.5×, AREA cost 2 is the next kit lever.
3. **Re-check the field.** The state machines and the sieger's dominance
   were measured under 1.7.0. Read the 9c personality table of the batch
   that ends games; if the sieger is no longer clear of the others, the
   champion re-read's field is the personality pool, not the sieger + lane6.
4. **Champion re-read on 1.8.0**: 4,000 games, four shards on four cloud
   sessions (`--shard K/4`, `--merge`), the way `batch_0044` ran. About
   ±2.4 points a champion. Then Phase 4 proper: outliers first, one lever
   each, before/after pairs on the same field and seed.
5. **RQ-042** when ruled; **exploit profiles on T2**, then the Phase 5
   re-run; then the release-candidate read.

## 8. Running sims in this environment

- **The cloud container is torn down when the session goes idle with
  nothing harness-tracked running**, sometimes within 15 minutes, and a
  detached run dies with it. What works: a harness `Monitor` (30-minute
  timeout, re-armed at every expiry) tailing the checkpoint file; scheduled
  check-ins as the backup. `run_batch` checkpoints every finished game to
  `reports/raw/<batch>.partial.jsonl` and resumes from it on relaunch.
- **Workers.** A batch runs on its own four-core cloud session: create a
  session from the branch, give it the brief (launch detached; arm and
  re-arm a Monitor; relaunch on "workers gone"; verify the game count; commit
  the three report files or the gzipped shard into `reports/shards/`; push
  with pull-rebase retries; reply one line). The brief text is in this
  session's log for `batch_0044`–`batch_0054`; the parent reads results by
  pulling the branch, and `get_session` shows each worker's latest game
  count. Archive workers when done.
- **Sharding.** `--shard K/N` plays every Nth seat-swapped pair and writes
  only its checkpoint; `--merge` assembles `reports/raw/<batch>.partial*.jsonl`
  into the report and refuses on a gap. 4,000 games on four workers is
  about 8 hours; a 120-game personality batch on one worker is 55–95
  minutes depending on how many games run to round 20.
- **Pace.** 1.3–2.3 games a minute on four cores; sieging fields and
  short games are fast, mixed fields and round-20 games slow.
- **Usage.** Workers reported the account approaching its seven-day usage
  limit on 2026-09-24. Two workers at a time was the compromise.
- Raw dumps (`--dump-raw`) go to `reports/raw/`, gitignored. The per-champion
  and per-personality figures in the decisions log that are not in a report
  were computed from them.

## 9. Map of the repository

| path | holds |
|---|---|
| `rules/` | the rulebook; **1.8.0 is current** (P-0010, P-0011, P-0012 marked "v1.8" in the text) |
| `roster/` | champion kits; **1.7.0 is current** (P-0013); `validate_kit` honours `budget_exception` (whole-kit checks) and a named `ability_exception` (the per-ability floor) |
| `engine/` | map, state, abilities, phases, batch runner (checkpoint, shard, merge, anchor draw), report (9c personalities, 9d machines and anchors) |
| `ai/policy_v1_4_0` | the state machine over the personalities; `machines/gen1.json`, `gen2.json`; earlier packages frozen |
| `tests/` | 165 tests |
| `tools/` | `run_batch` (`--workers`, `--shard`, `--merge`, `--dump-raw`, `--baseline`), `ai_acceptance`, `ai_calibrate`, `search_agreement`, `ability_usage`, `refit_roster`, `tag_ambush`, `replay_view`, `roster_sheet` |
| `reports/` | requests, reports (`batch_0001`–`batch_0053`, `0054` queued), `shards/` (gzipped shard checkpoints for 0044 and 0045), `calibration` |
| `log/` | `decisions.md` (RQ-001–RQ-045), `changelog.md` (iterations 0–9), `patches/` (P-0001–P-0013) |
| `docs/` | prompt architecture, lab notes, agent role cards, this handoff |

## 10. The state machine, in brief

ai 1.4.0 makes the team AI a machine whose states are the 1.3.0 personalities
and whose transitions read flat game-state signals, re-evaluated once per
round; machines are JSON and register as tiers. Two bred generations and a
head-to-head confirmation (`batch_0041`–`batch_0043`) found nothing that
beats sieging from round 1 under 1.7.0; a laning opening was neutral. The
machinery stays: `SM_g2_lane6` was half the old champion-balance field, and if
1.8.0 gives a second strategy something to win with, breed again — with the
anchor design fixed (§6) and the field re-read first (§7 step 3).
