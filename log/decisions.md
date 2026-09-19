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

### Open for the lead designer

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

### Engine interpretations recorded in reports

- Option enumeration is capped per activation (`config.enum`), so a policy sees a
  representative sample of legal plans, not the full combinatorial set. Movement,
  recall and flip-entry options are never dropped by the cap.
- Ability step enumeration reads the state before the ability resolves, so a
  follow-up step's target list does not account for an earlier step's kill.
  Execution resolves steps in order for real.
