# Handoff — Hex-Nexus Balance Lab

Third handoff, written 2026-09-27 while the Phase 4 champion re-read
(`batch_0057`) runs. Everything is on
`claude/hex-nexus-multiagent-prompts-aivg93`, pushed. **Four shards of
`batch_0057` are in flight** (§8 lists the sessions); each pushes its gzipped
checkpoint into `reports/shards/` when it finishes, so pull before reading.

## 1. Where the lab stands

| phase | state |
|---|---|
| 0 Bootstrap | complete |
| 1 AI calibration | closed on RQ-031 |
| 2 Correctness and pacing | correctness: two placement bugs found by the exploit sweep and fixed (RQ-043). **Pacing: the HP lever is exhausted** (RQ-038 closed): tower 4 / Nexus 8 is the working pair, games end on a sieging field and stall 25-30% on a mixed one; the lever beyond HP is a rules change and the designer's (§3). |
| 3 Economy | the pillar is ruled (P-0010). AREA is a centred disc (P-0012). P-0013 (cooldown 2 on the four engines) read **partial**: wisp and ashwyn in line, quillan 1.56x and sable 1.70x remain (RQ-046). **Income is no longer win rate** under 1.8.0 (RQ-047), which changes what the 1.5x list means (§4). |
| 4 Champion balance | the 1.8.0 re-read is running: `batch_0057`, 4,000 games, sieger + lane6, tower 4 / Nexus 8, roster 1.7.0. The old-rules read (`batch_0044`) is the shape to compare against. |
| 5 Robustness | gate met on the 1.7.0 field (`batch_0045`, RQ-043). The exploit set now exists on T2 (ai 1.5.0, `X2_exploit_*`); its sweep is queued as `batch_0056` behind the re-read. |
| 6 Release candidate | not started |

Versions: rules **1.8.0**, roster **1.7.0**, ai **1.5.0**, **174 tests** (~4m),
all passing.

`engine/config.py` defaults sit on the 1.8.0 side (`abilities_hit_structures`
False, `structure_chips_pay` False, `tower_kill_ap` 3, `area_center` True,
`dragon_card` {hits 2, cooldown 3}, `dragon_ap_each` 0, `baron_permanent`
True). Each is a switch; older requests reproduce by overriding. Five values
live only as `config_overrides` in every request since `batch_0051` and are
**not** defaults: `tower_hp` 4 (config still says 11), `nexus_hp` 8 (config
12), `kill_ap` 3, `death_band_bonus` 1, `area_center` True. Copy them
forward. Once the designer confirms the pair, move tower/Nexus HP into the
config and the rulebook's tuning table (§14, "Tower HP 11").

## 2. The rulings and what each did

| patch | ruling | read | result |
|---|---|---|---|
| **P-0010** (pillar) | structures are never ability targets; only L0 and waves damage them. Structure chips go to the supply. A tower that falls pays one round of income (3 AP); the Nexus pays nothing. | `batch_0046` vs `batch_0039` | stands. At tower HP 16 games stopped ending; the HP pass followed. |
| **P-0011** | Dragon card is a reusable Red Buff (2 hits adjacent, cooldown track 3, at most 2 held, no AP). Baron empowers waves for the rest of the game. | `batch_0047` vs `batch_0046` | direction right (Dragon secured 51→55%, objective personality 38→43%); under 1.8.0 with games ending, both objectives sit at 43-47% when secured. Verdict still open: the objective personality is 38-43% in every 1.8.0 batch. |
| **P-0012** | an AREA is a radius-1 disc around a centre the player places within the step's range; Longbow moves the centre, never the blast. | `batch_0050` vs `batch_0048` | every engine's income down a third; pallas to the mean; four remained. |
| **P-0013** (roster 1.7.0) | cooldown 2 on the four remaining engines' AREA ability (sable W, wisp W, ashwyn W, quillan R), nothing bought back. | `batch_0054` vs `batch_0051` | **partial.** wisp 1.79→1.26x, ashwyn 1.66→1.49x, quillan 1.84→1.56x, sable 1.92→1.70x; usage held at 47-68%. sable 36% [24, 50], and it was 38% before the patch. Adopted; the next kit lever waits for `batch_0057` (§4, RQ-047). |

## 3. Pacing — closed on HP, open on rules

All on the personality field, seed 3801, full 1.8.0 rules from `batch_0048`:

| batch | tower HP | Nexus HP | roster | Nexus kills | median length | first tower falls |
|---|---|---|---|---|---|---|
| 0046 | 16 | 12 | 1.6.0 | 1% | 20 | round 16 |
| 0048 | 8 | 12 | 1.6.0 | 30% | 20 | round 11 |
| 0049 | 6 | 12 | 1.6.0 | 49% | 20 (p10 15) | round 8 |
| 0050 | 8 | 12 | 1.6.0, centred AREA | 15% | 20 | round 12 |
| 0053 | 6 | 8 | 1.6.0 | 39% | 20 (p10 16) | round 8 |
| **0051** | **4** | **8** | 1.6.0 | **75%** | **16** (p10 11, p90 20) | round 4 |
| 0055 | 4 | 6 | 1.6.0 | 75.8% | 16 (p10 9) | round 4 |
| 0054 | 4 | 8 | 1.7.0 | 69% | 17 | round 5 |

Targets: median 13–18 and Nexus kills above 90%. **Nexus 6 is identical to
Nexus 8**, so the Nexus is not what stalls games. The `batch_0054` raw dump
says what does: of 37 games at round 20, 33 were decided on towers, only 4
had a sieger in them, and in every one the leader had taken 2–5 towers and
stopped. The sieger stalls 7% of its games; warder 47%, brawler 38%, laner
37%, objective 33%. **Under 1.8.0 a team that does not siege cannot end a
game**, and tower HP cannot go below 4 (the first tower already falls in
round 4). Tower 4 / Nexus 8 is adopted as the working pair; on the sieging
field `batch_0057` reads pacing directly and should pass.

The levers beyond HP, in the order the lab would try them, all rules changes
and the lead designer's: L0 dealing 2 hits to structures (a "siege hit"),
waves dealing 2 hits to structures by default (the Baron effect made
standard), fewer towers per lane. Whether a mixed field *should* end 95% of
its games is itself the designer's call: RQ-038 in its 1.7.0 form showed the
same split (pacing passed when both sides sieged).

## 4. The findings that govern the design

- **Income is no longer win rate** (RQ-047, new). Under 1.7.0 the two
  correlated at 0.60 across the roster; on the three 1.8.0 personality
  batches the correlation is −0.09, 0.00, −0.09 (Spearman −0.22, −0.01,
  −0.25). sable earns the most AP on the roster and wins 36–38%. The
  designer's reading behind P-0010 is confirmed from the other side. So the
  1.5x AP check is now a check on the *economy's shape* (the design budget
  prices AREA at 6 a hit), not a proxy for balance; a champion that is only
  an income outlier is not a balance outlier. Read `batch_0057` with that in
  mind, and do not tax sable's AREA further on the strength of the 1.5x list.
- **The game still has one strategy under 1.8.0.** The sieger is 89.7%,
  93.1% and 87.9% in batches 0051, 0054, 0055; laner 54–57%, objective
  38–41%, warder 24–34%, brawler 19–26%. RQ-037's finding survives the
  ruled economy. The champion re-read's field is therefore still the
  sieger + `SM_g2_lane6`; breeding again (§10) has nothing new to work with.
- **The old-rules champion read** (`batch_0044`, 4,000 games): Jungle and
  ADC balanced; Support (wisp 77%, corvane 27%) and Top (bastion 75%)
  broken; Mid split. bastion was the one outlier that was never an income
  story. `batch_0057` replaces this table; compare shapes, not numbers.
- **South wins 53.2%** over 4,000 seat-swapped games (RQ-042). Open,
  designer's. `batch_0057` gives a second 4,000-game read of it for free.
- **No exploit beats the field** (RQ-043), with the T1 caveat now addressed
  in code (ai 1.5.0) and waiting on `batch_0056`.
- **P-0013's shape.** A whole-card cooldown of 2 took a fifth to a third
  off each engine, not half: the champion spends the off round on Q/E or on
  walking to the next wave, and the roster mean fell with the engines.

## 5. Open questions for the lead designer

1. **Pacing lever beyond HP** (§3): siege hit for L0, 2-hit waves, fewer
   towers — or accept that a non-sieging field stalls a quarter of its games.
2. **Tower 4 / Nexus 8** as the rulebook values (§14 tuning table), pending 1.
3. **The engines after P-0013**: quillan 1.56x and sable 1.70x remain above
   1.5x, but income no longer buys wins (RQ-047). Is the 1.5x check still a
   target, or is the budget (AREA at 6 a hit) the thing to enforce? The lab
   recommends deciding after `batch_0057`.
4. **RQ-042**, the map: move a pit, compensate North, or accept 53–47.
5. **P-0011's verdict**: the objective personality is still 38–43% and
   Dragon/Baron secured win rates sit at 43–47%. Objectives are not yet worth
   fighting over; is that acceptable, or is the objective the next lever?

## 6. Things I got wrong, so they are not rediscovered

- **Anchors as pool members, then anchors only against machines.** Use a
  Bradley-Terry fit (script in the RQ-040 entry) or a head-to-head, never
  the overall column, for a mixed field.
- **Tower HP 16 was never confirmed** and became the wall the moment
  structures stopped taking ability damage. Any pacing number under a rules
  change is suspect until games end.
- **Nexus HP looked like the next wall and was not.** Read the end reasons
  and the raw dump (who is in the stalled games) before sweeping a number:
  `batch_0055` was an hour of compute that the `batch_0051` end reasons
  (18 of 30 stalls decided on towers) had already answered.
- **AREA was a disc, and the rulebook's own text said "at your feet"**;
  trace income to the step, not the champion.
- **Two batches launched ten minutes before a ruling amended the patch**
  were killed and relaunched. Ask "is the ruling complete?" first.
- **`pkill -f` with a pattern that matches the calling shell kills the
  shell.** Match on the process (`pgrep -f 'run_batch.py .*batch_005[7]'`).
- **The exploit profiles were T1** and their 0% was partly T1 vs T2. Fixed
  in ai 1.5.0; unread.
- **Running the test suite beside a batch** halves the batch's pace for
  four minutes. Run tests before launching, not during.

## 7. Picking the work back up

```bash
pip install pytest
python -m pytest tests/ -q                                            # 174, ~4m
git pull                                                              # shards land here
ls reports/shards/batch_0057*                                         # want four
for f in reports/shards/batch_0057.partial.shard*of4.jsonl.gz; do gunzip -kc "$f" > "reports/raw/$(basename "${f%.gz}")"; done
python tools/run_batch.py reports/requests/batch_0057.json --merge --dump-raw
```

In order:

1. **Merge and read `batch_0057`** once all four shards are in
   (`--merge` refuses on a gap and names it; a missing shard is relaunched
   with `--shard K/4` and resumes from its checkpoint if the worker still
   has it, or restarts if not). Read: pacing on the sieging field (§5 of the
   report; expected in band), champions outside 45–55 with the interval
   clear of 50, the four engines, the roles table, North/South. Write the
   RQ entry as `batch_0044`'s was written (RQ-041), then the recommended
   order of levers — remembering RQ-047.
2. **Phase 4 proper**: outliers first, one lever each, before/after pairs on
   the same field and seed (2,000 games is enough for ten champions). The
   designer said "use the design levers"; the engines' AREA cost 2 stays
   the candidate for quillan if `batch_0057` confirms it.
3. **`batch_0056`** (exploits on T2, ai 1.5.0): the request carries
   placeholders for anchors and HP — replace them with what 1 confirms, then
   four shards, then the RQ-043 re-read.
4. **RQ-042** and the pacing lever when ruled; then the release-candidate
   read.

## 8. Running sims in this environment

- **The cloud container is torn down when the session goes idle with
  nothing harness-tracked running**, sometimes within 15 minutes, and a
  detached run dies with it. What works: a harness `Monitor` (30-minute
  timeout, re-armed at every expiry) tailing the checkpoint file; a
  `send_later` check-in as the backup. `run_batch` checkpoints every
  finished game to `reports/raw/<batch>.partial*.jsonl` and resumes from it
  on relaunch.
- **Sessions in flight for `batch_0057`** (Sonnet 5 workers, created
  2026-09-27 ~04:37 UTC; each pushes
  `reports/shards/batch_0057.partial.shardKof4.jsonl.gz` and replies one
  line; archive when done). The parent runs no shard itself and idles on a
  `send_later` check-in, which fires into it and merges once all four land.
  - shard 0/4: `session_01SvJXpfkvff4LRB8w5weYpG`
  - shard 1/4: `session_01TMY5jf9k4AhXEKGqrE8M1m`
  - shard 2/4: `session_01XUMtJM5AiGsL5Y2Q52L4e3`
  - shard 3/4: `session_016Bjs2YCPHQwnEMcA2wkjS7`
- **Worker model.** The lead designer cleared lower models for sim runs.
  A worker only launches, re-arms a Monitor and pushes one file, and the sim
  itself is Python, so the model never touches a number. Sonnet 5 is the
  default; Haiku is cheaper but a single missed re-arm loses a shard.
- **A worker's brief** (the text used for 0055 and the 0057 shards): confirm
  branch and request; launch detached with `nohup … & disown`; arm a 30-min
  Monitor that prints the checkpoint line count, exits 0 on the done line,
  exits 1 with the log tail if `pgrep -f '…batch_005[7]'` finds nothing;
  re-arm on expiry; relaunch on process gone; verify the count; commit only
  the three report files (or the one gzipped shard); `git pull --rebase`
  then push with 2/4/8/16 s retries; reply one line. Say explicitly: no
  tests, no other edits, no PR, no `--merge`, never `pkill -f` on the
  command text.
- **Pace.** 1.3–2.3 games a minute on four cores; sieging fields are fast.
  A 120-game personality batch is 55–95 minutes; a 1,000-game shard of a
  sieging field 7–10 hours. `get_session` shows a worker's latest count.
- **Usage.** Workers reported the account approaching its seven-day limit on
  2026-09-24; two workers at a time was the compromise until the designer
  asked for all four `batch_0057` shards at once and cleared lower models. A 1-hour worker costs about $2 in tokens,
  nearly all of it Monitor re-arms.
- Raw dumps (`--dump-raw`) go to `reports/raw/`, gitignored. The stall
  analysis in RQ-038 came from `batch_0054`'s dump with a 40-line script
  (who is in the round-20 games, towers taken, HP left); write it again
  rather than looking for it.

## 9. Map of the repository

| path | holds |
|---|---|
| `rules/` | the rulebook; **1.8.0 is current** (P-0010, P-0011, P-0012 marked "v1.8" in the text); §14 tuning table still says tower 11 / Nexus 12 |
| `roster/` | champion kits; **1.7.0 is current** (P-0013); `validate_kit` honours `budget_exception` and a named `ability_exception` |
| `engine/` | map, state, abilities, phases, batch runner (checkpoint, shard, merge, anchor draw), report (9c personalities, 9d machines and anchors) |
| `ai/policy_v1_5_0` | current: 1.4.0 plus the seven `X2_exploit_*` tiers (the T1 exploits' distortions on the T2 search); `policy_v1_4_0` the state machine, `machines/gen1.json`, `gen2.json`; earlier packages frozen |
| `tests/` | 174 tests |
| `tools/` | `run_batch` (`--workers`, `--shard`, `--merge`, `--dump-raw`, `--baseline`), `ai_acceptance`, `ai_calibrate`, `search_agreement`, `ability_usage`, `refit_roster`, `tag_ambush`, `replay_view`, `roster_sheet` |
| `reports/` | requests (`0001`–`0057`; `0052` not run, `0056` queued with placeholders), reports (`batch_0001`–`batch_0055`), `shards/` (0044, 0045; 0057 arriving), `calibration` |
| `log/` | `decisions.md` (RQ-001–RQ-047), `changelog.md` (iterations 0–9), `patches/` (P-0001–P-0013, each with its `result`) |
| `docs/` | prompt architecture, lab notes, agent role cards, this handoff |

## 10. The state machine, in brief

ai 1.4.0 makes the team AI a machine whose states are the 1.3.0 personalities
and whose transitions read flat game-state signals, re-evaluated once per
round; machines are JSON and register as tiers. Two bred generations and a
head-to-head confirmation (`batch_0041`–`batch_0043`) found nothing that
beats sieging from round 1 under 1.7.0, and the 1.8.0 personality tables
(§4) say the sieger is still clear, so there is nothing to breed toward yet.
The machinery stays: `SM_g2_lane6` is half the champion-balance field. If a
pacing ruling gives a second strategy something to win with, breed again —
with the anchor design fixed (§6) and the field re-read first.
