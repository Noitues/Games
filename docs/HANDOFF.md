# Handoff — Hex-Nexus Balance Lab

Written at the lead designer's request, mid-pacing-retune. Everything below is
on `claude/hex-nexus-multiagent-prompts-aivg93`, pushed.

## 1. Where the lab stands

| phase | state |
|---|---|
| 0 Bootstrap | **complete** |
| Roster expansion to 25 | **complete** — roster 1.3.0 |
| 1 AI calibration | **closed** on the lead designer's ruling (RQ-031, gate lowered to 60%). T2 reads 58.5% [53.6, 63.2] — inconclusive against the new gate, not a pass. |
| 2 Correctness and pacing | **in progress, one arm outstanding.** Median length passed on T1 (P-0002) but that tuning was measured on the wrong AI — see §3. Being re-tuned on T2. |
| 3 Economy | **patched, not yet measured** — P-0004 is in rules 1.3.0 and roster 1.4.0; `batch_0032` will judge it. See §5. |
| 4 Champion balance | not started |
| 5 Robustness | exploit gate already met; needs a re-run on rules 1.2.0 |
| 6 Release candidate | not started |

Versions: rules **1.3.0**, roster **1.4.0**, ai **1.2.0**, **110 tests** (~55s).

The engine default `tower_hp` is still **11**, the value P-0002 chose against
T1. It is known to be wrong for T2 (§3) and is waiting on `batch_0031`.

## 2. What is in flight

Nothing is running — the pacing arms were stopped mid-run when work paused.
Three batches are written and ready but have **no results**:

| run | what it settles | command |
|---|---|---|
| `batch_0031` — T2, 80 games, tower HP 16 | the leading candidate for P-0003 | `python tools/run_batch.py reports/requests/batch_0031.json --workers 4 --baseline reports/batch_0029.json` |
| `batch_0030` — T2, 80 games, tower HP 15 | the fallback if 16 overshoots | `python tools/run_batch.py reports/requests/batch_0030.json --workers 4 --baseline reports/batch_0029.json` |
| `batch_0032` — T2, 120 games, roster 1.4.0 | judges P-0004, the economy patch | `python tools/run_batch.py reports/requests/batch_0032.json --workers 4 --baseline reports/batch_0028.json` |

A T2 batch costs roughly 18s a game on 4 cores, so each of these is 25–40
minutes. **`batch_0032` is the one to run first** — P-0004 is committed to the
rulebook and roster but has never been measured.

## 3. The finding that matters most right now

**Pacing must be tuned on T2, not T1.** Everything in P-0002 was measured on T1
mirrors, and T1 turns out to misreport the game badly:

| same rules, roster and tower HP 10 | median | p90 | ends by Nexus kill |
|---|---|---|---|
| T1 mirror (`batch_0026`, 150 games) | 14 | 20 | 92.0% |
| T2 mirror (`batch_0028`, 80 games) | **10** | 14 | **100%** |

T1 leaves 8% of games unresolved and reads about four rounds longer. Inspecting
those unresolved games, the pressured side still held a median 2.5 of 6 towers
and in half of them neither Nexus had been scratched — they are not close games
that ran out of clock, they are games where T1 never organised a siege. T2
closes every one of them. So the round-limit tail was an AI-competence artefact
and no rules lever was ever going to fix it. Two evenings of pacing levers
(tower HP sweeps, a second wave-growth step) were spent chasing it.

**Consequence: the adopted tower HP of 11 is wrong.** It was chosen because it
put T1 at median 14. On T2 the sweep so far reads:

| tower HP (T2 mirror, 80 games) | median | p10 | p90 | Nexus kills |
|---|---|---|---|---|
| 10 | 10 | 8 | 14 | 100.0% |
| 13 | 12 | 10 | 15 | 97.5% |
| 15 | *`batch_0030`, in flight* | | | |

Extrapolating, tower HP around 15–16 should land the 13–15 median the lead
designer asked for. **Do not adopt a value until `batch_0030` lands**, and set
the default in `engine/config.py` (`tower_hp`) plus the Rules §8 line together.
The second wave-growth step (`wave_chips_late2`, round 13) is in the engine and
made almost no difference on T1; it has not been measured on T2 and can be
reverted cheaply if it earns nothing.

## 4. The rulings, and what they did

All four rulings from the last session are implemented, tested and measured.

**RQ-001 / RQ-002 — hidden hexgroups are a refuge** (rules 1.1.0). Movement
distance and effect distance are now separate: a hidden hexgroup is a shortcut
for walking, not for shooting. Champions inside cannot be reached from outside;
minions, towers and camps keep their own hex, so a tower covers its hex's
neighbours instead of the whole tile edge.

**RQ-033 — my implementation of that ruling was wrong the first time, twice
over.** The first cut made concealment symmetric, so a hidden champion could not
attack out either; because a champion's own tile is hidden whenever no enemy
shares it, that broke ranged play entirely. The second cut replaced board
distance with raw hex distance for *every* effect, which quietly shrank every
ability's reach and stopped the game resolving (0.7% of games ended by Nexus
kill, team AP fell by two thirds). Both are fixed. The lesson is in the rule now:
the ruling changes *who* can be reached, not how far anything reaches.

**RQ-016 — bump-and-continue** is implemented as Rules 3.3 step 4 always said.

**RQ-030 / patch P-0001 — §14.2 recalibrated** (credits cut to −2 per AP and
−1.5 per cooldown round, ability floor raised to 3, R capped at 1.75× the Q/W/E
mean), with roster 1.2.0 refit to it. Judged on two batches differing only in
roster: the 0-AP-to-3-AP usage gap went from **+27.2 points to −4.5**, so the
pricing inversion is gone. Its second metric missed — 34 of 100 abilities still
sit under 5% use against a target of 25 — and that residue is situational
effects (REVEAL, shields, blinks) the policy rarely wants, not a pricing
problem. No revert condition triggered.

**RQ-032 — retested clean.** A dedicated `X_exploit_fogsnipe` policy loses to T2
at 12.5% [5.5, 26.1]. Sniping from concealment is not a degenerate strategy.

**RQ-034 — ambush abilities** (rules 1.2.0, roster 1.3.0). Measuring RQ-032
turned up that 85% of all ability uses were being made from inside a hidden
hexgroup at a target outside it, and champion kills had collapsed from 17.31 per
game under the literal reading to **0.20**. The lead designer's fix: tag which
abilities may be used out of cover, one per champion and two for junglers,
preferring a move-and-attack that commits the champion. Result:

| | before | after (`batch_0023`) |
|---|---|---|
| champion kills per game | 0.24 | **4.48** |
| attacks made from cover | 85% of uses | 46% |

**One judgment call in RQ-034 still wants confirmation.** Only 7 of 25 kits own
a move-and-attack, so tagging alone would have left 18 champions sniping from
cover with a ranged ability. I made springing an ambush flip the hexgroup face
up for the rest of the round, which is what turns an ambush into a one-shot
rather than a firing position. That is an extra rule beyond what was asked, it
is in Rules 1.2.0 §3.1, and it should be confirmed or removed.

## 5. Economy: patched, awaiting its batch

Measured on T2 (`batch_0028`), four champions sit far above the 1.5× target:

| champion | AP/round | × roster mean | the cheap engine |
|---|---|---|---|
| ashwyn | 10.34 | **3.99×** | W: AREA at 0 AP |
| quillan | 7.84 | **3.03×** | W: LINE, R: AREA |
| wisp | 6.51 | **2.51×** | W: AREA |
| sable | 6.31 | **2.43×** | W: AREA, R: AREA+HEAL |

22 of 25 champions own an AREA or LINE somewhere and average 1.08×, so the
ability type is not the problem — a *cheap* one is. This confirms the standing
hypothesis that §14.2 prices AREA and LINE by hits rather than by the chips they
can bank: a 0-AP AREA touching three units banks three AP for nothing.

**P-0004 is written, committed and unmeasured** (`log/patches/P-0004.json`).
Rules 1.3.0 prices AREA at 6 per hit at r1 climbing 4 per extra step of range,
LINE at (3 + n) per hit, and forbids a free AREA or LINE outright. Roster 1.4.0
is refit to it: 13 of 100 abilities changed, 3 single-step stat changes, and no
free farming engine left anywhere. All 25 kits validate and the RQ-034 ambush
tags survive the refit.

Its success metric is: no champion above 1.5× the roster-mean AP per round in a
T2 mirror, top champion under 2.0×. `batch_0032` decides it.

**One thing in P-0004 wants a designer's eye.** grivven is the single kit the
new table could not price. Its R paired AREA with ROOT, which costs 14 gross
under the new values — above the 1.75× spread cap at every combination of
numbers, with no room left under the 22 ± 2 band. Rules §14.2 allows a redesign
once stat and number levers are exhausted, so its R became a harder area hit
(AREA k2) and **lost the root**. That is a genuine identity change, not a
number tweak.

Two bugs surfaced while building this, both fixed and worth knowing about:
`tools/refit_roster.py` rebuilt each ability from its numbers and silently
dropped the ambush tags, and `validate_kit` priced gross with the default point
table rather than the kit's own, so the fitter and the validator disagreed
about what an AREA was worth.

## 6. Picking the work back up

```bash
pip install pytest
python -m pytest tests/ -q                      # 108 tests, ~60s
python tools/run_batch.py reports/requests/batch_0030.json --workers 4 --baseline reports/batch_0028.json
```

In order:

1. **Run `batch_0032`** and judge P-0004 against its metric (§5). It is the
   only committed patch with no evidence behind it.
2. **Land `batch_0031`** (and `batch_0030` if 16 overshoots), pick the tower HP
   that puts the T2 median in 13–15, set it in `engine/config.py` *and* the
   Rules §8 line together, and confirm with a 300-game T2 mirror. Write it up
   as P-0003 in `log/patches/` — that file does not exist yet. Note that
   P-0004 removes some economy, which may itself lengthen games, so the tower
   HP should be chosen on a roster-1.4.0 batch rather than on the 1.3.0 sweep.
3. **Champion balance.** Note RQ-028: with 5 champions per role a champion plays
   40% of games, so ±2.2-point verdicts need ~5,000-game batches. T2 now costs
   about 18s a game on 4 cores, so a 5,000-game T2 batch is roughly 6 hours.
   Either budget for it, run the sweep on T1 and confirm only the outliers on
   T2, or shrink T2's opponent model for bulk batches. **Do not** tune anything
   pacing-adjacent on T1 alone again — see §3.
4. **Re-run the exploit sweep on rules 1.2.0.** The Phase 5 gate was met under
   rules 1.0.0 and the game has changed twice since.

### Useful tools added this session

| tool | what it answers |
|---|---|
| `tools/ability_usage.py` | regroups ability usage by price rather than by champion |
| `tools/refit_roster.py` | refits a roster to a new §14.2 table, protecting identity |
| `tools/tag_ambush.py` | picks each champion's ambush ability |
| `tools/ai_calibrate.py --ai --roster` | now takes `config_overrides`, so rules variants run head to head |

Report Part 9b carries the concealment metric (attacks made from cover).

## 7. Decisions waiting on the lead designer

1. **The ambush reveal** (§4) — confirm or remove.
2. **Tower HP** once `batch_0030` lands, if the sweep does not land cleanly in
   13–15; the choice trades median length against the Nexus-kill rate.
3. **Phase 4 batch budget** (§6 item 3): ~6 hours of T2, or a T1 sweep with T2
   confirmation.

## 8. Map of the repository

| path | owner role | what it holds |
|---|---|---|
| `rules/` | Facilitator | the rulebook; **1.2.0 is current** |
| `roster/` | Designer | champion kits; **1.3.0 is current** |
| `engine/` | Sim Runner | map graph, state, abilities, phases, batch runner, report builder |
| `ai/policy_v1_1_0`, `ai/policy_v1_2_0` | AI Developer | frozen and current policy packages |
| `tests/` | Sim Runner | 108 tests, one module per rulebook area |
| `tools/` | Sim Runner / AI Dev | see the table in §6 |
| `reports/` | Sim Runner | sim requests, batch reports, calibration results |
| `log/` | Facilitator | `decisions.md` (34 RULE-Qs), `changelog.md`, `briefs/`, `patches/` |
| `docs/` | Facilitator | prompt architecture, lab notes, agent role cards, this handoff |

Why a rule resolves the way it does is in `log/decisions.md`; why the engine and
AI are built the way they are is in `docs/LAB_NOTES.md`; what each patch expected
and what it actually did is in `log/patches/`.
