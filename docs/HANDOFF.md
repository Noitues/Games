# Handoff — Hex-Nexus Balance Lab

Written at the lead designer's request. Everything below is on
`claude/hex-nexus-multiagent-prompts-aivg93`, pushed.

Written at the lead designer's request; extended after batches 0039-0044.
Nothing is running.

## 1. Where the lab stands

| phase | state |
|---|---|
| 0 Bootstrap | complete |
| 1 AI calibration | closed on RQ-031 (gate lowered to 60%) |
| 2 Correctness and pacing | **deferred on purpose, and now broken by a ruling.** Rules 1.7.0 moved median length to 18 and Nexus kills to 78% on T2 (RQ-038). Waiting on the lead designer. |
| 3 Economy | **stuck on the pillar question, which Phase 4 has now shown to be the champion-balance question.** See §4 and RQ-041. |
| 4 Champion balance | **read taken, no patch yet.** `batch_0044`, 4,000 games on the settled field: 10 of 25 champions clear of 45-55, Support and Top broken, Jungle and ADC balanced, and the HIGH champions are the Phase 3 AREA engines. The first patch is the pillar ruling (RQ-039), not a kit. See RQ-041. |
| 5 Robustness | exploit gate met under rules 1.0.0; needs a re-run, the game has changed six times since. ~400 games, one shard session, independent of everything else. |
| 6 Release candidate | not started |

Versions: rules **1.7.0**, roster **1.6.0**, ai **1.4.0**, **139 tests** (~3m), all passing on 2026-09-23.

`engine/config.py` holds the live knobs. `tower_hp` **16** is a placeholder from
the T2 pacing sweep, never confirmed, and `reveal_radius` **2** has now been read
on T2 (`batch_0039`): the two together put the game outside its pacing band.
Note that the P-0008 values (`kill_ap` 3, `death_band_bonus` 1) and `tower_hp`
16 live as `config_overrides` in every request since `batch_0038`, not as
defaults in `config.py`; carry them forward in any new request.

## 2. What is queued and why

| run | what it settles |
|---|---|
| ~~P-0009~~ | **done, failed** (`batch_0040`, RQ-039). Pricing the Dragon in AP changed nothing; `dragon_ap_each` is back at 1. |
| ~~a T2 read at reveal radius 2~~ | **done** (`batch_0039`, RQ-038). Direction held; pacing broke. Waiting on the lead designer. |
| ~~the personality state machine, generation 1~~ | **built and run** (ai 1.4.0, `batch_0041`, RQ-040). Nothing beats sieging; the two clocks that open on the lane sit above the pure sieger on the point estimate, inside overlapping intervals. Survivors: `SM_g1_clock3`, `SM_g1_clock2`. |
| ~~generation 2~~ | **run** (`batch_0042`, RQ-040 in the decisions log). A laning opening before sieging is real relative to sieging from round 1, worth about +0.3 to +0.5 log-odds on a Bradley-Terry fit; not yet confirmed head-to-head. Survivors `SM_g2_lane6`, `SM_g2_clock3_short`. |
| ~~the confirmation, `batch_0043`~~ | **run.** lane6 51.1% [41.0, 61.1], clock3_short 45.6% [34.3, 57.3] against the pure sieger. Neither beats it. RQ-040 closed; breeding stopped. |
| ~~`batch_0044`, the champion read~~ | **done**, RQ-041 and RQ-042 in the decisions log. |
| **the AREA-conversion pillar patch** | needs the lead designer's ruling on RQ-039 (cap per use, or no conversion on waves). Then one before/after pair against `batch_0044`, same field and seed, 2,000-4,000 games sharded. |
| **bastion** | the one outlier the pillar will not touch: 74.9% on 0.26 deaths a game. Read the kit, patch one lever, before/after pair. |
| the bottom five | corvane, lumen, kaelis, vellum, ossuar - after the pillar re-read, one income lever each. |
| the exploit sweep | independent; one shard session any time. |

Open for the lead designer: **RQ-039** (the AREA conversion - now the
gating question for champion balance too), **RQ-042** (South wins 53-47 on
the settled field), and **RQ-038** (pacing broke at reveal radius 2 in a
mixed field; it is in band, median 14, when both sides siege - so it may
be moot once the field is what players actually do).

A 120-game T2 personality batch costs 65–80 minutes on 4 cores; a 400-game
generation costs about 3h15m.

## 3. The finding that should govern what happens next

**The game rewards one way of playing, and every champion number in this repo
was measured in that field.** `batch_0037`, 120 games, five personalities drawn
per game:

| personality | before P-0008 | after P-0008 |
|---|---|---|
| sieger | 86.5% | **70.7%** |
| objective | 68.2% | 45.2% |
| laner | 52.2% | 55.6% |
| warder | 21.7% | 34.2% |
| brawler | 21.2% | 35.4% |

P-0008 (a kill pays 3 AP instead of 1, death timers a round longer) passed both
its metrics and closed the spread from 65 points to 36. It did not level the
field: the sieger still wins 70.7% and its interval sits clear of everything
below the laner.

Two batches since, both paired with `batch_0038` by seed:

| personality | batch_0038 (radius 1) | batch_0039 (radius 2) | batch_0040 (+ Dragon pays 2) |
|---|---|---|---|
| sieger | 70.7% | 69.0% | **74.1%** |
| laner | 55.6% | 59.3% | 59.3% |
| objective | 45.2% | 47.6% | **40.5%** |
| brawler | 35.4% | 35.4% | 33.3% |
| warder | 34.2% | 28.9% | 31.6% |

Neither the sight ruling nor the objective lever moved the field. P-0009 is the
instructive one: the extra AP landed exactly where it should (the objective
personality's income rose 3.74 to 4.65 a round) and that personality lost more.
The sieger takes 0.59 Dragons a game and wins; the team with more Dragons than
its opponent wins 42% in both batches; Baron, already map-shaped, sits at 47.7%
when secured. Shop spend runs 11 AP a team-round against 2.4 on abilities.
**Teams are not short of AP, so any lever that pays AP is inert at the
margin.** A tower is the only thing on the map that converts activations
directly into the win condition. That is RQ-037 restated from the economy
side, and it is why the levers left are pillar-adjacent (RQ-039 lists four).

The state machine (§9) then said the same thing from a third direction.
`batch_0041`, generation 1, ranked on the lower confidence bound:

| policy | games | win rate [95% CI] | occupancy |
|---|---|---|---|
| SM_g1_clock3 (lane → objective → siege from r9) | 60 | 66.7 [54.1, 77.3] | sieger 48%, laner 26%, objective 26% |
| SM_g1_clock2 (lane → siege from r4) | 82 | 61.0 [50.2, 70.8] | sieger 81%, laner 19% |
| SM_g1_ap_lead (siege when ahead on income) | 72 | 59.7 [48.2, 70.3] | sieger 43%, objective 42%, laner 15% |
| T2_sieger | 68 | 57.4 [45.5, 68.4] | - |
| SM_g1_map_commit | 78 | 52.6 [41.6, 63.3] | laner 59%, sieger 22%, warder 19% |
| SM_g1_fight | 82 | 50.0 [39.4, 60.6] | laner 60%, brawler 21%, sieger 17% |
| SM_g1_map | 106 | 45.3 [36.1, 54.8] | laner 59%, warder 23%, sieger 18% |
| SM_g1_objective_window | 86 | 40.7 [30.9, 51.3] | objective 85%, sieger 15% |
| T2_search | 88 | 38.6 [29.1, 49.1] | - |
| SM_g1_full | 78 | 37.2 [27.3, 48.3] | objective 74%, laner 16%, sieger 7% |

Win rate tracks time spent in the sieger state and nothing else. The one
thread worth pulling is the laning opening both clocks share - and generation
2 (`batch_0042`, table under RQ-040) pulled it: on a Bradley-Terry fit over
every pairing the pure sieger is mid-field, every machine above it lanes for
3-6 rounds and then sieges, both machines that siege from round 1 sit below
it, and a machine that opens on a fight is a full log-odds below. A short
laning opening is worth roughly +0.3 to +0.5 log-odds against the pure
sieger. `batch_0043` tested that head-to-head and it is not there: lane6 is
51.1% [41.0, 61.1] against the pure sieger over 92 games. RQ-040 is closed.
**The game has one strategy, and three independent methods agree.**

On that field, `batch_0044` (4,000 games, ±2.4 points a champion) reads the
roster. Win rates are against role peers:

| role | champions, best to worst (win rate %) |
|---|---|
| Top | bastion **74.9**, marrow 50.5, vurmak 45.7, kaelis **40.3**, ossuar **38.3** |
| Jungle | thornjaw 52.6, sylphine 52.3, bramblehide 50.6, rictus 49.3, mossgrove 45.2 |
| Mid | sable **58.6**, ashwyn **58.4**, quillan 53.5, noctis 44.4, vellum **35.0** |
| ADC | veyra 54.8, kestrel 52.5, dax 48.9, brixa 48.7, orrin 45.3 |
| Support | wisp **77.4**, pallas **57.5**, grivven 48.3, lumen **38.6**, corvane **27.4** |

Bold is clear of 45-55 with the whole interval. Income per round and win
rate correlate at 0.6, and the five HIGH champions other than bastion are
the five AREA engines Phase 3 flagged. RQ-041 has the reading and the order
of patches.

The consequence for Phase 4 is the important part. A champion win rate read in
a field where sieging wins is mostly a measure of that champion's siege
contribution. Tuning the roster against it would tune the roster toward one
strategy and then declare it balanced. **Do the objective lever first, then
re-baseline champion balance on a mixed personality field.**

## 4. Economy: stuck against a pillar

Phase 3's exit condition is no champion above 1.5× the roster-mean AP per
round. Five still are. The history matters, because two of the three patches
were wrong in instructive ways:

- **P-0004 (failed).** Re-priced AREA and LINE in the §14.2 budget. Moved the
  design budget and not the behaviour: raising an AREA's price just forces the
  kit to give something back elsewhere. A point table has no grip on a
  per-activation rate.
- **P-0006 (partial).** Took the range step off AREA. This was the right lever
  and the evidence is unambiguous — the two AREAs with reach to lose dropped
  34% and 23% of their absolute income. But it only reaches champions who had
  reach; the three reach-1 engines went *up*.
- What is left is the **conversion itself** — an AREA banking fewer chips as
  AP — and that is the chip-equals-AP pillar. Two shapes were put to the lead
  designer and neither has been ruled on: cap how many chips an AREA banks per
  use, or stop area damage on minion waves converting at all.

The attribution tooling for this is in place: `apply_plan` books every AP a
champion earns against the ability that earned it, which is how the engines
were found (one AREA supplies 94–98% of each outlier's income).

## 5. Rulings implemented since the last handoff

- **RQ-034 → RQ-036, the hidden-hexgroup redesign.** The ambush-gate approach
  was replaced: a champion may now use any ability from cover, and an occupied
  hexgroup is revealed by an enemy champion within **2 hexes** (rules 1.7.0).
  The two numbers are equal on purpose — while sight reached 1 and abilities
  reached 2 there was a band to shoot from unseen, and that is where most of
  the shooting happened. Probes: champion snipes down about a fifth, champion
  combat up about 40%.
- **RQ-037a.** Objectives may be priced higher (approved, not yet applied); a
  tower that only falls while your wave is present was **rejected** and is
  recorded as rejected.
- **grivven keeps the roster's only area root**, with his basics nerfed 4 gross
  and a stated `budget_exception`. Kits may now sit outside the band on purpose
  if they say why — the budget is a first guess at equal power and win rate is
  the real test. `validate_kit` honours that for the whole-kit checks only.

## 6. Things I got wrong, so they are not rediscovered

- **Twice over-implemented a rules ruling.** The safe-haven reading was first
  made symmetric (which broke ranged play entirely) and then implemented by
  replacing board distance with hex distance for every effect (which shrank
  every ability's reach and stopped games resolving). The ruling changed *who*
  can be reached, not how far anything reaches.
- **Tuned pacing on T1.** T1 runs about four rounds longer than T2 and leaves
  8% of games unresolved, and those unresolved games are not close finishes —
  T1 simply never organises a siege. P-0002's tower HP of 11 was chosen against
  T1 and is wrong for a T2 world. **Do not tune anything pacing-adjacent on T1
  alone.**
- **Chose two metrics that could not move.** "Share of ability uses made from
  cover" measures location, not sniping — being in cover is the default state.
  "Activations ending on a hexgroup edge" counted any hex bordering any other
  hexgroup, which is nearly all of them, and read 98%. Both are replaced; the
  concealment section of a report now separates true snipes, and snipes aimed
  at a champion, from farming a wave.
- **The refitter dropped data it did not tune** (the ambush tags), **bought
  budget back by lengthening abilities**, and **disagreed with the validator**
  about ties and about which point table to price with. All fixed, but it is
  worth re-reading `tools/refit_roster.py` against `engine/kits.py` before
  trusting a refit.

## 7. Picking the work back up

```bash
pip install pytest
python -m pytest tests/ -q                     # 119 tests, ~2m20s
python tools/run_batch.py reports/requests/batch_0038.json --workers 4   # the pattern
```

In order:

1. **Get the RQ-039 ruling, then patch the AREA conversion** and read it as
   a before/after pair against `batch_0044` (same field, same seed, sharded
   across four sessions as `batch_0044` was). Five HIGH champions should move
   at once. Do not tune the five engines kit by kit first; RQ-041 says why.
2. **bastion**, one lever, one pair.
3. **The bottom five** on the re-read field.
4. **Pacing**, when RQ-038 is ruled. `tower_hp` 16 has never been confirmed,
   and rules 1.7.0 moved the game to median 18 with a fifth of games
   unresolved. Do not tune it on T1.
5. **The objective's payoff** beyond the AREA question: do not re-run an
   AP-priced objective lever; `log/patches/P-0009.json` records why.
6. **Re-run the exploit sweep.** The Phase 5 gate was met under rules 1.0.0.

Running sims in this environment: the cloud container is torn down whenever
the session goes idle with nothing harness-tracked running - sometimes within
15 minutes - and a detached run dies with it (`batch_0040` was lost once,
`batch_0041` twice). Two things make long runs survivable, and both are now
in place: `run_batch` checkpoints every finished game to
`reports/raw/<batch>.partial.jsonl` and resumes from it on relaunch; and a
harness `Monitor` tailing the checkpoint file, re-armed every 30 minutes,
kept the container alive for the whole of `batch_0041`'s 3h15m. Scheduled
check-ins every 15-30 minutes are the backup that relaunches from the
checkpoint if it dies anyway. Raw per-game dumps (`--dump-raw`) go to
`reports/raw/`, which is gitignored.

## 8. Map of the repository

| path | holds |
|---|---|
| `rules/` | the rulebook; **1.7.0 is current** |
| `roster/` | champion kits; **1.6.0 is current** |
| `engine/` | map graph, state, abilities, phases, batch runner, report builder |
| `ai/policy_v1_1_0 … v1_3_0` | policy packages; **1.3.0 current**, earlier ones frozen so old batches stay reproducible |
| `tests/` | 119 tests, one module per rulebook area |
| `tools/` | `run_batch`, `ai_acceptance`, `ai_calibrate`, `search_agreement`, `ability_usage`, `refit_roster`, `tag_ambush`, `replay_view`, `roster_sheet` |
| `reports/` | sim requests, batch reports, calibration results |
| `log/` | `decisions.md` (37 RULE-Qs), `changelog.md`, `patches/` (P-0001…P-0008, each with what it expected and what it did), `briefs/` |
| `docs/` | prompt architecture, lab notes, agent role cards, this handoff |

Patches record their own verdicts, including the two that failed. Read
`log/patches/` before re-running any economy lever.

## 9. Next AI step: a state machine over the personalities

The five personalities in ai 1.3.0 are fixed for a whole game, which is not how
anyone plays. A team opens on lane discipline, groups when an objective is up,
sieges when it is ahead, and wards when it is behind. The next step is to make
the team AI a **state machine whose states are the personalities and whose
transitions read the game state**, then to breed the transition logic rather
than hand-tune it.

### 9.1 The machine

A candidate is a pair: the set of states it may occupy (any subset of
`warder`, `brawler`, `sieger`, `objective`, `laner`, or new ones) and the
transition logic between them. Re-evaluate the machine once per round at
Upkeep, not per activation — switching personality mid-round makes the snake
order incoherent and the logs unreadable.

Signals the transition logic may read, all already on `GameState`:

| signal | why it should matter |
|---|---|
| round number and band | opening, mid-game, closing play differ |
| towers standing, own vs enemy | ahead on the map → siege; behind → ward and farm |
| Nexus chips, own vs enemy | how close either side is to winning |
| champions alive, and HP pool | a won fight is the moment to group |
| Dragon or Baron alive, and its respawn round | an objective coming up should pull a team to it |
| AP per round, own vs enemy | who can afford to contest |
| champion deaths in the last round or two | reacting to a lost fight rather than repeating it |

Worth trying across iterations, not just threshold tweaks: pure time-scripted
machines (round bands only), pure reactive ones (differentials only), hysteresis
so a machine cannot oscillate every round, a "commit" timer that locks a state
for N rounds once entered, and two-state minimal machines as a control — if a
two-state machine matches a five-state one, the extra states are decoration.

### 9.2 The tournament

Ten candidates per generation, evenly spread across the batch so each plays
roughly the same number of games, drawn per game the way `personality_pool`
already draws personalities (`engine/batch.py`). Rank them, keep the **top 2**,
and fill the next generation with **8 new** candidates — mutations of the
survivors, crossovers between them, and at least two unrelated designs so the
search cannot collapse into one family. Repeat.

Four things will decide whether this produces a real answer or a dressed-up
coin flip:

- **Sample size per candidate.** Ten candidates in a 200-game batch is 40 games
  each, an interval of roughly ±15 points. Ranking on that promotes luck, not
  skill. Budget at least 60–80 games per candidate per generation, so 300–400
  games per generation, and expect 4–5 hours of T2 on 4 cores. Screening early
  generations on T1 is reasonable; confirming the survivors on T2 is not
  optional, because §6 records what happened the last time a decision rested on
  T1 alone.
- **Select on the lower confidence bound, not the point estimate.** Promoting
  the top 2 by raw win rate promotes whoever got the kindest draw. Sorting by
  `wr_lo` promotes candidates that are probably good.
- **Keep a fixed anchor in every batch.** In a field of evolving agents a 55%
  win rate in generation 5 means nothing next to 55% in generation 1, because
  the opposition changed underneath it. Put plain `T2_search` in every
  generation as a constant share of the field and report every candidate's
  record against it; that number is comparable across generations and the
  head-to-head one is not.
- **Log the state occupancy.** Record which state each team was in per round,
  the way the concealment metrics are recorded, so a winning machine can be
  read and explained rather than just scored. A machine that wins while sitting
  in one state all game has discovered that the state machine is unnecessary,
  which is itself a finding worth having.

### 9.3 What it is for

Two things, in order of importance. It makes the field a champion is measured
in resemble a played game rather than a fixed script, which is what §3 says the
balance numbers need. And it is a second, independent read on RQ-037: if every
surviving machine converges on sieging regardless of game state, that is the
strategy imbalance confirming itself from a direction that has nothing to do
with how the personalities were hand-written.

### 9.4 Generation 1 result, and the generation 2 plan

Built as ai 1.4.0 (`ai/policy_v1_4_0`): a machine is a JSON spec - default
state, commit timer, ordered rules over the flat signals in `SIGNALS` - so it
can be bred without touching code; `validate_machine` fails loudly on a typo.
Occupancy is logged per round and read in report section 9d. Generation 1 is
`batch_0041` (table in §3, RQ-040 in the decisions log).

Survivors: `SM_g1_clock3` and `SM_g1_clock2`. Generation 2 should hold:

- mutations of the clocks: laning opening ending at round 3, 5 and 6; clock3
  with the objective band cut to rounds 5-6, and with it removed (which is
  clock2 at round 5, the control);
- crossovers: a lane opening followed by `SM_g1_ap_lead`'s income rule; a
  lane opening followed by `SM_g1_map_commit`'s tower rule;
- two unrelated designs, as the protocol requires - for instance a machine
  that sieges from round 1 and drops to `warder` only when two champions
  down, and a `brawler`-opening machine, since no generation-1 machine opened
  on a fight.

Change the draw before running it: with ten tiers over 400 games each pair
met 2-14 times, so the against-anchor record was unreadable. Draw an anchor
into one seat of half the games (a spec field, in `engine/batch.py` beside
`personality_pool`) so each machine meets each anchor 20+ times.

### 9.5 Generation 2 result

`batch_0042`, RQ-040 in the decisions log. The anchor draw gave every machine
12-22 games against each anchor - enough that the pooled number is readable
(machines 50.0% against the sieger over 128) and not enough for any single
machine's record to be. It also introduced a confound: anchors meet only
machines, machines also meet `T2_search`, so overall win rates are comparable
among machines but not between a machine and an anchor. Use the Bradley-Terry
fit in the decisions log, or the machine-versus-machine column, for ranking;
a small script that fits it from `reports/raw/<batch>.jsonl.gz` is worth
adding to `tools/` before a generation 3.

If breeding continues, the next things to vary are the round the opening
ends (5, 6, 7, 8 - `lane6` won and `lane5` did not, so the curve is not yet
mapped) and whether a short objective band on the way to sieging helps
(`clock3_short` beat `clock3`, inside noise). Do not spend candidates on
brawler or warder states; two generations have priced them.

### 9.6 The confirmation, and what the state machine was for

`batch_0043` put each survivor against the pure sieger with nothing else on
the table: lane6 51.1% [41.0, 61.1] over 92 games, clock3_short 45.6% [34.3,
57.3] over 68. The lane opening is neutral. The machine rediscovered the
sieger, which is the finding §9.2 said would be worth having, and it is the
third independent confirmation of RQ-037. Keep ai 1.4.0: `SM_g2_lane6` is
half the champion-balance field, and the machinery is there if a rules change
ever gives a second strategy something to win with.

Running a batch across containers: `tools/run_batch.py ... --shard K/N`
plays every Nth seat-swapped pair and writes only its checkpoint; `--merge`
assembles the shards and refuses on a gap. The child-session brief that
worked is in the session log for `batch_0044`: launch detached, arm a
30-minute `Monitor` on the checkpoint file and re-arm at every expiry,
relaunch on "workers gone", gzip the shard into `reports/shards/` and push
with pull-rebase retries.

