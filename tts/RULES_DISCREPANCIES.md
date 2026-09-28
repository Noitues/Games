# Rules discrepancies and open designer questions

The mod follows **the engine plus config**, which is what was simulated and
balanced (see `docs/prompts/TTS_MOD_BUILDER.md`). This file lists every place
where the rulebook (`rules/Hex-Nexus_Rules_v1.9.0.md`) and the engine disagree
or where the engine settles something the rulebook leaves open. It also lists
the questions that belong to the designer.

The mod is built from `reports/requests/batch_0075.json`, the settled rules
with 2 / 4 / 6 death timers, as the designer chose on 2026-09-28.

Status: **D** = discrepancy, the mod follows the engine; **Q** = open question
for the designer, the mod does what is stated until answered.

## Discrepancies

| # | Topic | Rulebook | Engine + config (what the mod does) | Status |
|---|---|---|---|---|
| 1 | Death timers | §6.4 (v1.9): track positions 4 / 5 / 6, i.e. 3 / 4 / 5 rounds missed. §13 lever table says the same. | `batch_0075` `death_track_positions` [3, 5, 7]: 2 / 4 / 6 rounds missed for deaths in rounds 1-4 / 5-8 / 9+. This is the designer's choice for the mod. | D: rulebook to update if 2 / 4 / 6 is adopted |
| 2 | Cooldown track length | §1 Components: track positions 4-3-2-1-0. | Deaths go to position 7, so the dashboard track runs 7 … 0. The length is computed from the config and roster, not typed in. | D (follows from 1) |
| 3 | Rules version of the request | The rulebook is v1.9.0. | `batch_0074.json` and `batch_0075.json` say `"rules": "1.8.0"`, but their `config_overrides` are the v1.9 values (towers 10, Nexus 15, decay, kill = two waves). The mod is labelled Rules 1.9.0. | D: request metadata |
| 4 | Dragon AP | §5.1 step 4: +1 AP per Dragon card held (max +2) at Refresh. | §11 (v1.8) and config `dragon_ap_each` = 0: the Dragon card is a reusable "2 hits adjacent, then cooldown track 3" card and gives no AP. The rulebook contradicts itself; §5.1 is a leftover. | D: fix §5.1 |
| 5 | Late wave growth | §9.1 and §13: waves are 3 chips, rising to 4 from round 7. | Config `wave_chips_late2` = 5 from `wave_growth_round2` = 13 (P-0003). §6.4 already assumes it ("10 AP from Round 13"). The mod's tracker shows +3 / +4 / +5. | D: fix §9.1 and §13 |
| 6 | Spawn hex held by a friendly champion | §9.1: a spawn is skipped if an *enemy* unit is on the spawn hex. | RQ-027: any other unit, including a friendly champion, skips that spawn. A friendly wave merges. | D |
| 7 | Monster respawn blocked | §11: respawns N rounds after the kill. | RQ-018: it reappears only when its own hex is empty. Otherwise it retries every Upkeep. | D |
| 8 | Respawn with a full base | §6.4: fountain, else any empty base hex. | Also an empty hex adjacent to the base (the §3.4 overflow). If even that is full, the champion stays dead and Upkeep retries (batch_0045). | D |
| 9 | Blue Buff timing | §11: "take a Blue Buff card: gain 2 AP immediately". | The card goes to the team's hand. The 2 AP are gained when the card is **played** with an ability, like every other buff card. | D (the "immediately" is ambiguous) |
| 10 | Decay step | §5.1 lists decay as a sub-bullet of step 3 (fountain healing). | Decay runs after fountain healing and before AP refresh, on rounds 3, 5, 7, …. The order and schedule are the same; only the numbering differs. | D (cosmetic) |
| 11 | `from_hidden` on abilities | Not in the rulebook. | Every roster ability carries `from_hidden`, but it only matters with `ambush_gate` on (retired by RQ-036, off in config). The mod does not print it. | D (inert data) |

## Open questions for the designer

| # | Question | What the mod does until answered |
|---|---|---|
| Q1 | **Kill reward with the Baron.** §6.4 says "twice the chips of a wave spawned that round". For a team holding the Baron, its waves spawn 2 chips bigger. Does the kill reward include that? | Engine: no. The kill reward is 2 × the base wave (6 / 8 / 10) for both teams. |
| Q2 | **Hidden information for spectators.** How much should a spectator (or a streamed game) see of champions inside hidden hexgroups? | M0 has no concealment. Hidden tiles are drawn hidden, but a standee placed on one is visible to everyone. Concealment via per-colour hidden zones comes with the referee (M1/M2), and the spectator view needs this answer. |
| Q3 | **First player.** §5.1 says priority passes every round but does not say who has it in round 1. | A panel toggle ("First: Blue/Red"). Odd rounds go to the first player, even rounds to the other. |
| Q4 | **Adopting 2 / 4 / 6 in the rulebook.** The mod uses it; the rulebook still says 3 / 4 / 5. Is it the new rule, or a playtest variant? | The mod labels it on the table ("death 2/4/6 rounds") so playtest logs are unambiguous. Rebuild with `--config reports/requests/batch_0074.json` for 3 / 4 / 5. |

## How this list grows

M0 found these by reading the engine against the rulebook. The M2 parity
harness replays engine scenarios against the Lua referee, one per icon and per
rule the tests cover. Every mismatch that is a rules question, not a Lua bug,
is added here.
