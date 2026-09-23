# Harness design notes (pre-code "first response")

Spec under test: `RULES_SPEC.md` v0.1.0 (Sep 22, 2026). This file answers the harness brief's
"first response" requirement: spec ambiguities that block automation, the exact engine state,
and the pilot plan. Every interim ruling below is implemented in `harness/rulings.py` and is
logged on the run as an `AMBIGUITY` record (source `engine`) **each time it actually fires**, so
the analyst can count how often each gap is hit rather than how often it is theoretically possible.

## 1. Ambiguities that block automation

IDs are stable; they appear in run JSON as `referee.ambiguities[].id`.

| ID | § | Gap | Interim ruling used by the engine |
| --- | --- | --- | --- |
| AMB-01 | brief | The brief's Arm A lists "Attention", which the spec never defines. | Not modelled. Logged once per Arm A/C run. |
| AMB-02 | §4 vs §7 | Backstory guarantee says the pulled card is "used in the next Beat Frame", but §7 says frames are never forced. If no frame triggers, the guarantee silently fails. | When the deck reaches 2 cards with unsurfaced player cards, those cards are pulled and a **guarantee Beat Frame** is forced at the start of the next scene (overrides that scene's test). |
| AMB-03 | §4 | "The scene after the last card is drawn is the climax" — does the session end after it? What if that is scene 2 of 5? | Climax scene is the session's last scene. The 5-scene cap still ends the session if the deck is never exhausted. |
| AMB-04 | §6 | Tension adjustments: do rows stack (flee +1 AND clock +1 AND resolve −1)? | All applicable rows are summed, then clamped to 1–6. |
| AMB-05 | §7/§6A | Rail overflow when no non-GLOBAL GM card is on the rail (rail full of player/story/GLOBAL cards). | Remove the oldest non-GLOBAL card of any kind (player cards return to binder, story cards to pile). |
| AMB-06 | §6 | Interrupt says "trigger any prepared Beat Frame" — which one, and what if all prepared frames have been used? | GM agent chooses among unused prepared frames; if none remain, the engine picks a starter-library frame not yet used this session by seeded RNG. |
| AMB-07 | §3/§4 | A tie draws a player card: is the "minor cost" the compel complication, or a separate cost in addition to the compel? | The compel complication *is* the cost. On refusal, the cost comes from a face-up GM tag (§4.4). |
| AMB-08 | §3 | "Major cost must use its weakness tag or a GM threat tag" — a drawn player card's weakness is also the compel's default tag. | Same as AMB-07: compel = cost. |
| AMB-09 | §6 | Altered scene draws a player card: does §4's compel also apply? | Yes: every Session Deck draw of a player card runs §4 (compel + surface). |
| AMB-10 | §9 | "A roll fails … after one of its tags was invoked" — invoked by whom? | By the card's owner only. Hostile invokes on a weakness do not earn Growth. |
| AMB-11 | §3 | Fate lets invokes happen after the roll. The GM's opposing invokes and passive-opposition tags have no stated timing. | GM commits opposing tags and invokes **before** the roll (one GM call per round); players invoke **after** seeing the dice. |
| AMB-12 | §8 | Stress box values are not given (only "2 boxes"). | Fate Core values: boxes worth 1 and 2; Physique/Will +1–+2 adds a 3 box, +3 or more adds a 3 and a 4 box. A hit checks one box ≥ remaining shifts, plus any consequences. |
| AMB-13 | §6A | Rail limit counts story cards, but the eviction rule only names GM cards. | Covered by AMB-05. |
| AMB-14 | §6/§5 | A Beat Frame's "stakes" advance a clock "when the stakes say so" — nothing says who decides that the beat "went badly". | The GM agent reports `beat_went_badly` at scene end; the Referee checks it. |
| AMB-15 | §3 | Hostile invoke FP is paid "at the end of the scene" — what if the session ends first? | Paid at the end of that scene, including the final scene. |
| AMB-16 | §4 | Deck draw while the deck is empty outside a climax (for example, a guarantee frame emptied it mid-scene). | Treated as climax behaviour for the rest of the scene: the cost uses a face-up GM tag. |
| AMB-17 | §7 | Trigger events must be "confirmable from the play log", but several useful triggers are fictional ("the party leaves the road"). | Prep uses machine-checkable triggers where possible (clock fills, roll against card X fails, scene N starts, tension ≥ N, compel refused). Fictional triggers are reported by the GM agent and audited by the Referee. |
| AMB-18 | §3/§5 | Beat Frame and interrupt draws have no "cost" — what must the drawn GM card be used for? | The GM must use one of its tags in the filled blank; the Referee audits it. |

Harness-level gaps (not in the spec, but needed to automate):

- **Arm B resolution.** The brief says B is "Fate Accelerated as written" (approaches), but Arms A and C use Fate Core skills. Using approaches in B would change the success math, a confound unrelated to backstory. By default B uses the same Fate Core skills with FAE-shaped aspects (high concept, trouble, 3 aspects). `arms.py` has `B_FAE` (approaches) as an opt-in variant.
- **Arm C content.** Each player still sets aside one random binder card at deck build, so the number of live tags matches A. A generic placebo card of the same type (ROOTS or REACH) takes its place in the deck and is "assigned" to that player. The compel economy, Beat Frame blank-filling and the backstory guarantee all run unchanged, and surfacing the placebo returns the set-aside card to the binder. Player Story Piles in C also hold generic placebo NPCs and threads.
- **Latin square vs 5-run cohorts.** 8 personalities × 4 seats need 8 runs for each personality to sit in each seat once, but cohorts rotate every 5 runs. The harness uses a global 8-run cyclic Latin rectangle, `personality(run r, seat p) = (r + 2p) mod 8`, indexed by the run's position in the batch. The same run index in every arm uses the same assignment, so arms stay paired. The rotation therefore continues across cohort boundaries.
- **Turn-taking.** Each round, every player agent is offered a turn and may pass, and the GM can address players by name. Lurkers are thus measured by what they choose, not by a forced turn order.

## 2. Engine state (`harness/engine.py`)

Everything below is plain data with deterministic transitions. Agents never mutate it directly.
They return structured choices, the engine validates them (an illegal choice is refused and logged
as a `VIOLATION` against that agent) and applies them.

- **RNG streams** (separate `random.Random` instances derived from the run seed): `dice`, `deck`,
  `scene_test`, `story`, `offscreen`, `misc`. Separate streams mean the *k*-th 4dF roll of a seed is
  the same in every arm (common random numbers), which tightens paired A/B/C comparisons.
- **Table:** arm, scene index, tension (1–6), climax flag, GM fate points (reset to 1 per player
  per scene), GM free invokes `{card_id: n}`, pending hostile-invoke payouts, token/time budgets.
- **Characters:** skills (Fate Core pyramid), refresh, fate points, stress tracks `{physical, mental}`
  as box lists, consequences `{mild, moderate, severe}` holding the aspect text and the strained
  card/tag, binder (4 cards, each with location `binder|deck|rail|strained|sacrificed`), free invokes
  per card, growth marks per card (a raw session ledger, capped at 2 during Evolution), taken-out
  and conceded flags, and for Arm B the FAE aspects instead of a binder.
- **Cards:** id, type, owner, title, 3 power tags, weakness, track kind/size/marks, version suffix,
  origin (`world|player|placebo|story`), `assigned_player` for placebo cards.
- **Session Deck:** ordered list (top = index 0), discard pile, surfaced set, guarantee-pulled set,
  peeked-card record.
- **Rail:** ordered list of face-up card ids with the order each entered (for eviction), capped at 5.
- **Story Piles:** one per player plus the GM pile; each pile is a list of `(card_id, weight)`
  expanded into echo slips when shuffled; retired list.
- **NPCs in conflict:** name, rating, stress boxes, consequence slots, link to a card id.
- **Prep packet:** anchors, environment, modules (2 GM cards + trigger), beat frames (+ trigger,
  defaults, stakes, stakes_clock), used/unused flags.
- **Triggers:** small DSL evaluated against the event log: `clock_fills:<id>`,
  `roll_fails_against:<id>`, `scene_start:<n>`, `tension_at_least:<n>`, `compel_refused`,
  `deck_at_most:<n>`, `fiction:<text>` (GM-reported).
- **Event log:** one row per event in the §12 CSV columns, plus harness-only columns (`arm`,
  `event_type`, `card_source`, `cost_tag`, `improvised`) kept in the JSON only.
- **Post-session:** Growth ledger → Evolution, clock advancement (bypassed/off-screen), threat
  mutation/retirement, Chronicle entry, closing tension.

## 3. Pilot plan

- **Backends.** `claude_cli` runs each agent call as an isolated `claude -p` subprocess with a
  replaced system prompt, no tools, no session persistence and JSON-schema output, so no two agents
  share a context window. A `scripted` backend (seeded heuristic bots per personality) drives the
  engine at zero token cost; it exists for tests and structural Monte Carlo, and its surveys are
  marked synthetic and excluded from experiential analysis.
- **Agent visibility** is enforced by construction. Each call's prompt is assembled only from what
  that role may see (see `harness/agents.py`), and a leak test greps player prompts for banned words
  (`playtest`, `arm`, `placebo`, `metric`, and so on).
- **Models (pilot):** players `claude-haiku-4-5-20251001`; GM, Referee, Interviewer and Analyst
  `claude-sonnet-5`. The 10% strong-model subsample (`claude-opus-5-5`) comes after the pilot.
- **Pilot batch:** one cohort (LLM-generated from seeded concept picks, cached to
  `harness/cohorts/`), 3 seeds × 3 arms = 9 runs, baseline scenario (1 session, 5 scenes,
  Tension 3), identical prep packet per seed across arms, personalities from the Latin rectangle.
- **Before any LLM run:** unit tests for the engine plus a scripted-backend batch (hundreds of runs)
  to shake out crashes and check structural metrics such as deck draws per session and
  surfacing rate.
- **After the pilot:** analyze → blinded analyst conclusions → human review packet
  (`reports/<batch>_review/`) → **stop** at the human gate. No spec patches before the human replies.
