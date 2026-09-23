# Handoff — Hex-Nexus Balance Lab

Written at the lead designer's request. Everything below is on
`claude/hex-nexus-multiagent-prompts-aivg93`, pushed.

Written at the lead designer's request; extended after batches 0039 and 0040.
Nothing is running.

## 1. Where the lab stands

| phase | state |
|---|---|
| 0 Bootstrap | complete |
| 1 AI calibration | closed on RQ-031 (gate lowered to 60%) |
| 2 Correctness and pacing | **deferred on purpose, and now broken by a ruling.** Rules 1.7.0 moved median length to 18 and Nexus kills to 78% on T2 (RQ-038). Waiting on the lead designer. |
| 3 Economy | **partly done, stuck on a pillar question.** See §4. The objective lever (P-0009) was tried and is inert; see §3. |
| 4 Champion balance | **not started, and should not start yet.** See §3. |
| 5 Robustness | exploit gate met under rules 1.0.0; needs a re-run, the game has changed six times since |
| 6 Release candidate | not started |

Versions: rules **1.7.0**, roster **1.6.0**, ai **1.3.0**, **119 tests** (~2m20s), all passing on 2026-09-23.

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
| **the personality state machine** (§9) | a team AI that switches personality on the game state, bred over generations. Now the next step: it changes the field champion balance is measured in, and it is the one remaining way to ask whether anything beats the sieger. |
| champion balance | only after §9 has a winner, and read on a mixed field. See §3. |

Two RULE-Qs are open for the lead designer before anything pacing-adjacent is
touched: **RQ-038** (reveal radius 2 broke pacing; `tower_hp` 16 is the
obvious lever) and **RQ-039** (objectives priced in AP are inert; what should
they pay in?).

A 120-game T2 personality batch costs 65–80 minutes on 4 cores.

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

1. **Make the team AI a state machine over the personalities** (§9). It is
   now the first item: both number levers have been tried, and §9 is the one
   remaining way to ask whether any way of playing beats the sieger. Read it
   against `batch_0039` values (P-0008 overrides, `dragon_ap_each` 1).
2. **Champion balance**, on a mixed field, not a mirror — and once §9 has a
   winner, against that rather than against fixed personalities. RQ-028 still
   applies: with 5 champions per role a champion plays 40% of games, so
   ±2.2-point verdicts need roughly 5,000 games. Consider a T1 sweep to find
   outliers and a T2 batch to confirm only those.
3. **Pacing**, when RQ-038 is ruled. `tower_hp` 16 has never been confirmed,
   and rules 1.7.0 moved the game to median 18 with a fifth of games
   unresolved. Do not tune it on T1.
4. **The objective's payoff**, when RQ-039 is ruled. Do not re-run an AP-priced
   objective lever; `log/patches/P-0009.json` records why.
5. **Re-run the exploit sweep.** The Phase 5 gate was met under rules 1.0.0.

Running sims in this environment: the cloud container is reclaimed after
roughly an hour idle and a detached run dies with it (`batch_0040` was lost
once this way and re-run). Launch a batch in the background, then keep the
session active with a scheduled check-in every 30 minutes until it reports.
Raw per-game dumps (`--dump-raw`) go to `reports/raw/`, which is gitignored;
the per-personality Dragon and AP figures above were computed from them.

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
