# Decision log — Hex-Nexus Balance Lab

Owner: Facilitator. One entry per ruling. Rulings marked **HUMAN** are paused for
the lead designer; the engine implements the stated reading in the meantime and
labels it in reports (Prompts 2.5 / 4.D).

Rulebook: `rules/Hex-Nexus_Rules_v1.0.0.md`.

## Iteration 0 (Phase 0 bootstrap) — RULE-Q rulings

| id | question (rules ref) | ruling | status |
|---|---|---|---|
| RQ-001 | Can a unit inside a hidden hexgroup be targeted from outside it? (3.1, 4.1) | Yes. Range ignores blocking and there is no hidden-information rule; the tile is one space, so every unit in it sits at tile range. Stacking a team in one tile is therefore exposed to AREA and LINE. | **HUMAN** |
| RQ-002 | Does a tower or monster inside a hidden tile threaten every hex bordering that tile in the World Phase? (3.1, 5.3) | Yes, by the same "one space" reading. A hidden tile widens a tower's threat zone; flipping it face up shrinks the zone back to its hex. | **HUMAN** |
| RQ-003 | Does AREA hit monsters? (6.3) | Yes. 6.3 defines an unmarked target as "any enemy unit: champion, wave, monster or structure". Monsters take area damage but stay neutral for flips (3.2). | ruled |
| RQ-004 | Do monsters hit champions of both teams? (5.3, 11) | Yes. Monsters are neutral: 1 hit to every adjacent champion, either team. | ruled |
| RQ-005 | How do friendly structures, enemy structures and monsters block? (4.3) | Friendly structures may be passed through but not stopped in (explicit in 4.3). Enemy structures and all monsters block entry and passage. Inside a hidden tile nothing blocks, because the tile is a single space. | ruled |
| RQ-006 | What can PUSH and PULL move? (6.3) | Champions and minion waves only; structures and monsters are immovable. The target steps along the board-distance gradient and stops early at any node it could not legally stop in — including a hidden tile holding the other team. | ruled |
| RQ-007 | When during movement may a champion recall? (5.2) | At any point, from any hidden tile it can reach. The engine charges the cheapest legal recall point, then spends the remaining movement from the fountain. | ruled |
| RQ-008 | May a champion that recalled still use an ability? (5.2) | Yes, before or after the movement, as normal. | ruled |
| RQ-009 | A champion dies while its card is already on the cooldown track. (6.4) | The card is set to the death-band position (2/3/4 by round band), not added to the current position. | ruled |
| RQ-010 | HASTE or Stopwatch brings a dead champion's card to position 0 mid-round. (6.3, 12) | It returns to hand and the champion respawns at its fountain at full HP immediately, and may activate this round if it has not already. | ruled |
| RQ-011 | Who gets the +1 AP when a tower, wave or monster kills a champion? (6.4, 7) | The team that owns the killing source. A monster kill gives no AP to anyone. | ruled |
| RQ-012 | Do SHIELDs stack? (6.3) | No. A new shield sets the value to the larger of the two and expires at the end of the next round. | ruled |
| RQ-013 | Does the protection order bind minions and monsters too, or only champions? (8) | Every damage source. A wave next to a protected T2 or Nexus deals it no damage. | ruled |
| RQ-014 | May an ability be used with no legal target? (6.3, 14.3) | No. An ability needs at least one legal target or effect. This is also the denominator of the ability-usage metric. | ruled |
| RQ-015 | A minion wave walks into a hidden tile holding enemies. (3.3, 3.6) | The wave stops outside, the tile flips, and that wave's movement ends for this Upkeep. | ruled |
| RQ-016 | A champion bumps into a hidden tile holding enemies. (3.3) | Rules 3.3 lets the mover continue after the flip. The engine ends that champion's movement at the stop hex instead, because its decision model resolves one flip per activation. Recorded as an engine simplification in every report. | **HUMAN** |
| RQ-017 | Flip overflow placement. (3.4) | Owner places each extra champion in an empty hex adjacent to the hexgroup, nearest first. Confirms the rulebook DEFAULT. | ruled |
| RQ-018 | A monster's respawn hex is occupied. (11) | The monster does not respawn; it appears on the first Upkeep when its hex is clear. | ruled |
| RQ-019 | Occupied minion spawn hex. (9.1) | Friendly wave: merge the chips. Enemy unit present: that spawn is skipped. Confirms the rulebook DEFAULT. | ruled |
| RQ-020 | All three round-20 tiebreakers tie. (13) | The game is a draw, recorded as `round_limit_draw`. Draws are excluded from win-rate denominators and reported separately. | ruled |
| RQ-021 | When is Swift Tonic declared? (12) | With the ability, before the movement it pays for. The engine offers it as part of the activation. | ruled |
| RQ-022 | How long does a revealed or warded tile stay face up? (6.3, 12) | REVEAL: to the end of the current round. Control Ward: to the end of the next round. Neither tile may flip back while the effect lasts, which also blocks enemy recalls there. | ruled |
| RQ-023 | "At the fountain" for Upkeep healing. (5.1) | Anywhere in the champion's own base tile. Confirms the rulebook DEFAULT. | ruled |
| RQ-024 | Do empowered (Baron) waves deal 2 hits to everything? (11) | No. 2 hits to enemy towers and the Nexus, 1 hit to everything else. | ruled |
| RQ-025 | Does terrain do anything? (2.4) | No. Terrain is colour only in v1.0.0; the engine treats it as cosmetic. Left open as a rulebook TBD. | ruled |
| RQ-026 | Minion waves inside hidden tiles. (3.6) | A wave always holds a specific path hex, even inside a hidden tile, and never uses the hidden shortcut. Confirms the rulebook DEFAULT. | ruled |
| RQ-027 | A friendly *champion* stands on the minion spawn hex. (9.1) | The spawn is skipped. Rules 9.1 only covers a friendly wave (merge) and an enemy unit (skip); anything else that cannot merge skips the spawn, because a visible hex holds one unit (4.2). | ruled |

## Iteration 3 — the lead designer's rulings

All four open items were ruled on. Rules 1.1.0 carries the two rules changes.

| id | ruling | status |
|---|---|---|
| RQ-001 / RQ-002 | **Flipped to the safe-haven reading.** A hidden hexgroup hides champions: a champion inside one cannot be targeted, hit or affected from outside, though it may still act outward. Minions, structures and monsters keep their own hex, so a tower inside a hidden hexgroup covers its own hex's neighbours instead of the whole tile edge. Stated in Rules 1.1.0 §3.1, §4.1 and §5.3 as the split between movement distance and effect distance: a hidden hexgroup is a shortcut for walking, not for shooting. | ruled, implemented |
| RQ-016 | **Bump-and-continue implemented.** The engine no longer ends movement on a flip: the mover stops, the tile flips, and it spends what is left of its movement inside the revealed hexgroup, as Rules 3.3 step 4 always said. The engine simplification is retired from the report labels. | ruled, implemented |
| RQ-030 | **Recalibrate 14.2 rather than redesign 47 abilities.** An ability is to be priced against the activation it consumes, not only against its AP cost. The cheap slots have to be worth an activation, so the floor rises rather than the ultimates falling. Proposed as an `economy`-class patch with the roster refitted to the new values. | ruled, in progress |
| RQ-031 | **The T2-vs-T1 acceptance gate drops from 65% to 60%.** Ten calibration variants over 890 games all landed between 52% and 62%, and the search-agreement diagnostic shows depth is not the bottleneck: the searched move differs from the greedy move 45.4% of the time and wins only a few points more often. Balance work needs a stable AI, not a stronger one. Recorded so the check is graded against 60% from now on. | ruled |
| RQ-033 | **Implementation error, found and fixed.** The first cut of the safe-haven ruling replaced board distance with raw hex distance for every effect, not just for concealment. That quietly shrank every ability's reach - a range 3 ability could previously cross a hidden hexgroup in one step - and the game stopped resolving: `batch_0010` and `batch_0012` ran 20-round games with 0.7-20.3% ending by Nexus kill and team AP down two thirds. Range is back on board distance (Rules 4.1); the ruling now changes only *who* can be reached, plus the tower's own reach. `batch_0014`: 99.3% Nexus kills, median 11 rounds, north 48.7%. | ruled, fixed |
| RQ-034 | **New, open - the biggest open question in the lab.** Concealment is doing far more than intended. 85% of all ability uses are made from inside a hidden hexgroup on a target outside it, because a champion's own tile is hidden whenever no enemy shares it, and a tile only flips when both teams stand *inside* it. So two champions in adjacent hexgroups can never reach each other. Champion kills per game: 17.31 under the literal reading, 0.20 under the refuge as ruled, 2.92 with the reveal remedy. The game still resolves - structures decide it - but the 5v5 skirmish has stopped happening. This is a pillar question about the hidden-hexgroup mechanic and no balance lever reaches it. | **HUMAN** |
| RQ-032 | **Retested clean on the corrected rules.** X_exploit_fogsnipe loses to T2 at 12.5% [5.5, 26.1] with the flag off and 2.5% with it on, so sniping from concealment is not a degenerate strategy and the remedy is not needed for that reason. The flag stays implemented and off. Superseded in importance by RQ-034. | ruled |
| RQ-032-old | **Superseded.** Concealment as ruled is one-way: a champion inside a hidden hexgroup cannot be hit from outside but may still attack out of it. That invites a "sniper in the fog" strategy. The lab is running the ruling as given and watching the exploit sweep for it; if it shows up, the natural fix is that acting on a unit outside the hexgroup flips it face up. Implemented behind `reveal_on_outward_effect`, default off. Tested in `batch_0013` against `batch_0012` and it made no measurable difference (0.7% Nexus kills either way) - but that pair ran on the broken geometry of RQ-033, so the test says nothing yet and should be redone on the corrected rules before the flag is judged. | **HUMAN** |

### Previously open, now closed

1. **RQ-001 / RQ-002 (hidden-tile range).** These two rulings decide how much the
   hidden-tile pillar is a hiding place versus a trap. Under the current reading a
   stacked team is an AREA magnet and a tower inside a hidden tile covers a wide
   ring. The alternative reading — units inside a hidden tile may not be targeted
   from outside, and structures inside one only reach their own hex — would make
   hidden tiles a genuine safe haven and slow the game down. Batch data on tower
   timings is attached to each report; the lab is running the literal reading.
2. **RQ-016 (bump-and-continue).** Engine simplification only; no player-facing
   rule change. Confirm that ending movement on a flip is acceptable for
   simulation, or it goes on the backlog as a two-part activation decision.

## Iteration 1 — roster expansion

| id | question | ruling | status |
|---|---|---|---|
| RQ-028 | The lead designer asked for 25 champions now, while Prompts Part 5 expands the roster only after Phase 4 passes with 10. | The lead designer's instruction wins: roster 1.1.0 carries 25 champions, 5 per role. The consequence is recorded rather than argued away - with 5 per role a champion plays 40% of games, so a champion win-rate read at the Rules 14.3 precision (+/-2.2 pts) now needs about 5,000 games per batch instead of 2,000, and every batch below that size reports champion verdicts as INCONCLUSIVE. | ruled |
| RQ-029 | Do the 15 new champions need new icons? | No. Every kit uses only the Rules 6.3 vocabulary, so no point value in 14.2 had to change and the budget calculator needed no edit. | ruled |

### Engine interpretations recorded in reports

- Option enumeration is capped per activation (`config.enum`), so a policy sees a
  representative sample of legal plans, not the full combinatorial set. Movement,
  recall and flip-entry options are never dropped by the cap.
- (Retired at RQ-016: the engine used to end movement when a bump flipped a
  tile. It now continues, as Rules 3.3 step 4 says.)
- Ability step enumeration reads the state before the ability resolves, so a
  follow-up step's target list does not account for an earlier step's kill.
  Execution resolves steps in order for real.

## Iteration 2 (Phase 1 close-out) — RULE-Q rulings

| id | question | ruling | status |
|---|---|---|---|
| RQ-030 | The Rules 14.3 ability-usage check fails 47 of 100 abilities. Is that 47 weak kits (a Designer problem) or one shared cause (a 14.2 pricing problem)? | One shared cause. `tools/ability_usage.py` regroups the same numbers by price rather than by champion, and usage rises monotonically with both levers the budget calculator charges for: 9.3% mean use at 0 AP up to 54.9% at 3 AP, and 13.3% at cooldown 1 up to 44.2% at cooldown 3. The expensive abilities are the used ones. Per-champion, 16 of 25 champions spend =>70% of their activations on one ability and only 2.36 of 4 abilities clear 5%. This is a 14.2 pricing question, not 47 kit redesigns, and the pricing question is downstream of the whole-card-cooldown pillar — so it needs a lead-designer ruling before Phase 4 spends any lever on it. | **HUMAN** |

### Why the direction matters

A cost curve is meant to ration: an ability that costs more should be used less
often, because it is affordable less often and its cooldown keeps the card off
the board longer. Hex-Nexus produces the opposite ordering.

The mechanism is the whole-card-cooldown pillar (Rules 6.4, Prompts 2.3). Using
*any* ability spends the same thing — the champion's activation, and its card's
place on the board. AP and cooldown are charged on top of that, but they are the
smaller term. So within a round where several abilities are ready, the only
question is which one is biggest, and a 0-AP ability is not cheap at all: it
costs a full activation, exactly what the ultimate costs.

The denominators make that comparison direct rather than inferred. The engine
records an opportunity per (round, champion, ability) whenever the ability was
affordable and had a legal plan (RQ-014), so every ability ready in the same
round shares that round's denominator and only one of them can be used. The
cheap abilities are not going unmeasured; they are being passed over.

This is the same finding `tools/search_agreement.py` reached from the AI side.
There, search gave up 4.1 points of immediate value on 45.4% of decisions and
won barely more often — activations are close to value-neutral *across plans*.
Here the neutrality shows up *within a kit*: three of a champion's four
abilities are dominated by the fourth. Both are readings of one pillar, which is
why neither is fixable in the AI backlog.

### Open for the lead designer

3. **RQ-030 (ability pricing vs the activation).** Two directions, both pillar-
   adjacent. (a) Recalibrate 14.2 so an ability is priced against the activation
   it consumes rather than against its AP cost — the cheap slots need to be worth
   an activation, which means raising the floor rather than nerfing the
   ultimates. (b) Change what an activation buys, so that using Q and using R are
   not the same expenditure — that is a whole-card-cooldown change and therefore
   a pillar decision. Direction (a) is a Designer brief; direction (b) is yours.

## Iteration 5 - what the personalities found

| id | question | finding | status |
|---|---|---|---|
| RQ-037 | Does Hex-Nexus reward more than one way of playing? | **No, and the spread is 65 points.** `batch_0037`, 120 games, five appetites drawn per game: sieger 86.5% [74.7, 93.3], objective 68.2% [53.4, 80.0], laner 52.2% [38.1, 65.9], warder 21.7% [12.3, 35.6], brawler 21.2% [12.2, 34.0]. The sieger and brawler intervals do not come close to overlapping. A policy that groups and hunts kills loses four games in five to one that ignores it and hits towers. | **HUMAN** |

### Why this matters before champion balance

Every champion number the lab has produced was measured in a field where
sieging wins. A champion win rate read there is mostly a measure of how much
that champion contributes to a siege, so tuning champions against it would
tune the roster toward one strategy and then declare the roster balanced.

The cause is not subtle. A champion kill pays +1 AP and a few rounds of the
victim's cooldown; a tower pays 11 chips, which is 11 AP, and moves the win
condition. Fighting is priced as a means to farming, and farming is priced
below sieging. `batch_0037` also shows the fight is not merely unrewarded but
actively wasteful: the brawler spends activations on champions while the
sieger spends them on structures, and the sieger wins.

Levers a designer might reach for, none of them applied:

1. Raise what a kill pays - AP, or a tempo reward that compounds.
2. Lengthen the window a kill opens (death timers by round band, Rules 6.4).
3. Make objectives need the fight: Dragon and Baron are contested ground, so
   pricing them higher pulls teams into each other.
4. Make towers need the fight: a tower that only falls while your wave is
   present, for instance, forces teams to hold ground rather than trade maps.

Levers 1 and 2 are numbers. Levers 3 and 4 change what the map is for, so they
are pillar-adjacent and belong to the lead designer.

### A second reading from the same batch

The mixed field produced 2 champions clearly off 50% against 7 in the
`batch_0035` mirror. Some of that is genuinely a broader test and some is
simply wider intervals from mixed match-ups, so it is not yet evidence that the
roster is better balanced than the mirror said - only that the mirror was
measuring against one taste.

## Iteration 6 - the lead designer's rulings on RQ-036 and RQ-037

| id | ruling | status |
|---|---|---|
| RQ-036a | **Sight reaches as far as a damage step: reveal radius 2.** While sight reached 1 and abilities reached 2 there was a band in which a champion could fire without ever being seen, and simulation found it was where most of the shooting happened - the P-0007 reach cap moved sniping barely at all (65.6 to 63.5 a game) because it narrowed that band rather than closing it. At radius 2 the two numbers are equal: if you can hit it, you can see it. Probes put champion snipes down about a fifth and champion combat up about 40%. Rules 1.7.0. | ruled, implemented |
| RQ-037a | **Objectives may be priced higher; towers may not be made to need a wave.** The objective lever is approved as a way to pull teams into each other; the map-shaped alternative - a tower that only falls while your wave is present - is rejected. `dragon_ap_each` is wired as a config knob and is not yet changed from 1: P-0008 is in flight and pricing two things at once would make neither attributable. | ruled, one lever pending |

## Iteration 7 - the T2 read at reveal radius 2, and the objective lever

| id | question | finding | status |
|---|---|---|---|
| RQ-038 | Does the RQ-036a ruling (reveal radius 2) hold on T2, and what does it cost? | **The direction holds and the cost is pacing.** `batch_0039` re-runs `batch_0038` unchanged under rules 1.7.0, same seed, so the draws pair. Concealment moved the way the T1 probes said: attacks from cover 67.8 to 57.3 a game, true snipes from 54.4% to 40.2% of all uses, and AP paid for champion kills per team-round 0.24 to 0.41. Sight now reaching as far as a damage step also reaches as far as a tower dive, and that is the cost: the first tower falls in round 8 rather than 6, structure income drops from 4.64 to 3.73 AP per team-round, median game length goes from 15 to **18** rounds, and games ending by Nexus kill fall from 96.7% to **78.3%**, 26 of 120 games hitting the round limit. The stalled games are not the sieger's (8.6% of its games reach the limit) but the warder's (36.8%), brawler's (27.1%) and objective's (23.8%): the teams that were already not sieging now cannot close either, because a defender sees the dive coming. Typical limit game: towers 3-3 or 3-2, both sides at the inner towers. The personality field did not move: sieger 69.0%, laner 59.3%, objective 47.6%, brawler 35.4%, warder 28.9%, spread 40 from 36, every change inside its interval. | **HUMAN** |

### What is being asked

Rules 1.7.0 stands on its merits - it closed the unseen firing band, which is
what RQ-036a set out to do - but it moved the game out of the pacing band that
P-0002 and P-0003 put it in, and pacing is ruled to be tuned last. Two of the
scorecard's pacing checks now fail (median length 18, Nexus kills 78.3%).
`tower_hp` 16 is the number under this: it was a placeholder from the T2
pacing sweep, never confirmed, chosen when a tower could be hit from a hex the
defender could not see. The lab's recommendation is to leave the ruling alone
and treat the placeholder as the lever, but that is a pacing patch, and the
lead designer moved pacing last. Options, none applied:

1. Bring `tower_hp` down from 16 (towards P-0002's 11) and re-read pacing on T2.
2. Leave pacing where it is until champion balance is done, accepting that
   every batch until then reads at median 18 with a fifth of games unresolved.
3. Something map-shaped - the lab has no evidence for a specific one.

P-0009 (`batch_0040`) is read against `batch_0039`, so its verdict is not
confounded by this; but its pre-registered revert condition on median length
must be read as a delta from 18, since the baseline is already outside 13-16.

| id | question | finding | status |
|---|---|---|---|
| RQ-039 | Does pricing the Dragon higher (RQ-037a's approved lever) pull teams into each other? | **No. P-0009 failed both metrics and the lever is inert.** `batch_0040` doubled what a Dragon card pays, paired by seed with `batch_0039`. Sieger 69.0% to **74.1%**, objective 47.6% to **40.5%**, spread 40 to 42.5; 97 of 120 paired games had the same winner. Dragon takes did not move (2.33 to 2.37 a game) and the same teams took them: the sieger 0.59 a game in both batches, the objective personality 1.8-1.9. The AP landed where it should - the objective personality's income rose 3.74 to 4.65 a round - and it lost more. In both batches the team with more Dragons than its opponent wins 42%; Baron, whose payoff is already map-shaped, sits at 47.7% when secured. Shop spend runs 11 AP a team-round against 2.4 on abilities, and AP-cost abilities are used in 19.5% of the rounds they are affordable: **teams are not short of AP, so paying them more of it changes nothing.** The only thing on the map that pays back the activations it costs is a tower. `dragon_ap_each` stays at 1. | **HUMAN** |

### What this says about RQ-037

RQ-037 found that the game rewards one way of playing. P-0008 priced the fight
and closed half the gap; P-0009 priced the objective and closed none of it,
and the reason is now visible in the economy rather than the personalities: AP
is abundant and activations are scarce. Every source of AP is fungible (the
chip-equals-AP pillar) and most of it goes to the shop, so a lever that adds AP
anywhere adds nothing at the margin. A tower is different in kind: chipping it
spends activations directly on the win condition. Dragon and Baron spend
activations on AP, and AP does not win games.

Levers a designer might reach for, none applied and all pillar-adjacent:

1. Pay objectives in tempo rather than AP - a Dragon card that deals hits to a
   structure at Upkeep, or extends reach, or shortens a cooldown.
2. Make objectives cheaper in activations (Dragon HP 8, Baron 12) so the price
   matches what they pay.
3. Make AP scarce, so that it matters who has it: a lower base, or shop prices
   that rise, so that objective income is the difference.
4. Accept the sieger as the game's spine and use the §9 state machine to ask
   whether any switching strategy can beat it. If none can, RQ-037 is a
   design fact, not a tuning problem.

The AI is not the confound here. The objective personality already goes to the
pit and takes the Dragon; what it cannot do is turn the card into towers.

| id | question | finding | status |
|---|---|---|---|
| RQ-040 | Does any way of switching between the personalities beat sieging from round 1? (Handoff §9, generation 1) | **Not in generation 1, and the field says why.** `batch_0041`, 400 games, ai 1.4.0: eight machines drawn per game with two fixed anchors, ranked on the lower confidence bound. Top three: `SM_g1_clock3` 66.7% [54.1, 77.3] (lane, then objectives, then siege from round 9), `SM_g1_clock2` 61.0% [50.2, 70.8] (lane, then siege from round 4), `SM_g1_ap_lead` 59.7% [48.2, 70.3] (siege when ahead on income). `T2_sieger` itself 57.4% [45.5, 68.4]. All three winners spend most of the game in the sieger state (48%, 81%, 43% of rounds); the three machines that sit in sieger 40% of rounds or more average 62.5% and the five that do not average 45.1%. The two that live in the objective state - `SM_g1_objective_window` (85% objective) 40.7% and the five-state `SM_g1_full` (74% objective) 37.2% - finish at the bottom beside plain `T2_search` at 38.6%. **No machine's lower bound clears the sieger's point estimate**, so nothing is shown to beat sieging; the best two differ from it only by opening on the lane. This is RQ-037 confirmed from a direction that has nothing to do with how the personalities were written, and RQ-039 again: any time spent at the pit is time lost. The head-to-head records against the anchors are 2-14 games each and say nothing yet; ten tiers over 400 games is too thin for a per-pair number. | lab; generation 2 queued |

### What generation 1 settles and what it does not

Settled: the state machine has, so far, rediscovered the sieger. Every state
other than sieger costs win rate in proportion to the time spent in it, with
one possible exception - a laning opening. Both clocks open on `laner` and
both sit above the pure sieger on the point estimate, which is the one place
a second generation might find something real.

Not settled: whether that opening is real (intervals overlap by 20 points),
and whether a reactive machine could beat a clock if given the right signal -
`SM_g1_ap_lead`, the one reactive machine in the top three, switched 3.8 times
a game and still landed on sieger 43% of the time.

Generation 2 keeps the two clocks and breeds eight around them: the length of
the laning opening (rounds 3, 5, 6), whether the objective band earns its
place (clock3 with the band shortened or removed), crossovers of a lane
opening with the income signal, and two unrelated designs as required. The
anchors need more games: generation 2 should draw an anchor in one seat of
half the games rather than treating anchors as two more tiers, so the
against-anchor record is worth reading.

### RQ-040, generation 2 (`batch_0042`)

480 games; the two generation-1 survivors and eight bred around them, with
the anchors drawn into one seat of half the games rather than pooled as tiers.
Two readings, because the overall win-rate column is not comparable between
anchors and machines (anchors only ever meet machines; machines also meet the
weak `T2_search`): a Bradley-Terry strength fitted over every pairing, and
the machine-versus-machine record with anchor games excluded.

| policy | Bradley-Terry vs sieger (log-odds) | overall WR [95% CI] | machine-vs-machine WR [95% CI] | occupancy |
|---|---|---|---|---|
| SM_g2_lane6 (lane → siege r6) | **+0.51** | 64.5 [52.1, 75.3] | **75.0 [59.8, 85.8]** (40) | sieger 66%, laner 34% |
| SM_g2_clock3_short (lane → objective r5-6 → siege r7) | +0.35 | 64.1 [53.0, 73.9] | 56.5 [42.2, 69.8] (46) | sieger 60%, laner 26%, objective 13% |
| SM_g1_clock2 (lane → siege r4) | +0.29 | 61.3 [50.3, 71.2] | 56.5 [42.2, 69.8] (46) | sieger 79%, laner 21% |
| SM_g1_clock3 (lane → objective r5-8 → siege r9) | +0.29 | 60.8 [49.4, 71.1] | 59.5 [44.5, 73.0] (42) | sieger 48%, laner 26%, objective 26% |
| SM_g2_lane_map (lane → siege, ward when behind) | +0.20 | 57.1 [44.1, 69.2] | 57.9 [42.2, 72.1] (38) | sieger 60%, laner 20%, warder 20% |
| SM_g2_lane5 (lane → siege r5) | +0.01 | 53.6 [40.7, 66.0] | 47.8 [34.1, 61.9] (46) | sieger 74%, laner 26% |
| **T2_sieger** (anchor, 128 games) | 0.00 | 50.0 [41.5, 58.5] | - | - |
| SM_g2_lane3 (lane → siege r3) | -0.06 | 47.1 [35.9, 58.7] | 36.0 [24.1, 49.9] (50) | sieger 87%, laner 13% |
| SM_g2_siege_guard (siege r1, ward when 2 down) | -0.19 | 43.9 [33.7, 54.7] | 40.7 [28.7, 54.0] (54) | sieger 87%, warder 13% |
| SM_g2_lane_ap (lane → siege, objectives when poor) | -0.20 | 48.8 [38.1, 59.5] | 50.0 [37.3, 62.7] (56) | sieger 50%, objective 31%, laner 20% |
| T2_search (anchor, 118 games) | -0.54 | 35.6 [27.5, 44.6] | - | - |
| SM_g2_brawl_open (brawl r1-3 → siege) | -1.03 | 26.3 [17.7, 37.2] | 30.0 [19.1, 43.8] (50) | sieger 60%, brawler 40% |

**What it says.** The pure sieger is mid-field. Every machine above it lanes
first and sieges from round 4-7; both machines that siege from round 1
(`siege_guard`, and `lane3` which is in sieger by round 3) sit below it, in
this generation as in the last. Opening on a fight is the worst thing a team
can do (brawl_open, -1.03). Time in the objective state still costs
(`lane_ap`, 31% objective, -0.20), except when it is a short band on the way
to sieging (`clock3_short`). The laning opening is therefore real relative to
sieging from round 1, and worth roughly +0.3 to +0.5 log-odds, a 57-62%
expected win rate against the pure sieger.

**What it does not say.** The direct records against `T2_sieger` are 2-22
games a machine and do not agree with the fit (`lane6` is 25% over 12,
`clock3_short` 67% over 18); pooled, the machines are exactly 50% over 128.
The anchor design fixed the sample size and introduced a confound in its
place, so the ranking above rests on the fit, not on a head-to-head. That is
what `batch_0043` is for: every game one of the two survivors against the
pure sieger, 80 games each, no other opposition.

**Pacing, noted for RQ-038.** With almost every team sieging, this batch
plays median 15 rounds and 99.4% of games end by Nexus kill - both pacing
checks pass. `batch_0039`'s break (median 18, 78%) came from the warder,
brawler and objective personalities failing to close, not from the sieger.
The game paces correctly when both sides play its dominant strategy.

Survivors: `SM_g2_lane6`, `SM_g2_clock3_short`.

### RQ-040 closed: the confirmation (`batch_0043`)

Every game one generation-2 survivor against the pure `T2_sieger`; nothing
else on the table.

| policy | games vs sieger | win rate [95% CI] |
|---|---|---|
| SM_g2_lane6 (lane → siege from round 6) | 92 | 51.1 [41.0, 61.1] |
| SM_g2_clock3_short (lane → objectives r5-6 → siege) | 68 | 45.6 [34.3, 57.3] |

**Neither beats sieging from round 1.** The +0.3 to +0.5 log-odds the
Bradley-Terry fit gave the lane openers in `batch_0042` was opposition mix:
they beat the machines that fight, ward, or chase objectives, and are level
with the machine that just sieges. Two generations and a confirmation say the
same thing the personalities said (RQ-037) and the economy said (RQ-039): in
Hex-Nexus as ruled, the winning strategy is to hit towers, and every round
spent on anything else costs in proportion. **The state machine is
unnecessary**, which the handoff (§9.2) listed as a finding worth having.

Consequences:

- **RQ-037 is a design fact, not a tuning problem.** Three independent
  reads - hand-written personalities, an AP lever that landed and did
  nothing, and a bred switching AI that converged on sieging - all agree. The
  levers left are the pillar-adjacent ones in RQ-039, and they are the lead
  designer's.
- **Champion balance can proceed**, on the field this settles: the sieger and
  `SM_g2_lane6`, drawn per game. They are 50/50 against each other and differ
  in shape (one lanes for five rounds first), so a champion is read against
  the strongest play in two forms rather than against a script that loses.
- **Stop breeding.** A generation 3 would be measuring noise around 50%.
