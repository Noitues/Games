# Hex-Nexus — Master Ruleset v1.3

A 1v1 tactical board game that distills League of Legends into a skirmish: each player commands a full team of 5 champions.

**Status tags used in this document**

| Tag | Meaning |
|---|---|
| (none) | Confirmed by the designer. |
| **[DEFAULT]** | Proposed to fill a gap. Treat as a rule until overridden. |
| **[TBD]** | Open decision. A placeholder value is given where one is needed for simulation. |

---

## 0. Design Goals & Constraints

- **Players and teams:** 2 players, each controlling 5 champions: Top, Jungle, Mid, ADC, Support.
- **Target playtime:** 60–90 minutes, not counting setup.
- **Iconography:** Card text is replaced by icons wherever possible. Every ability is an icon sequence plus stated range, cost and cooldown.
- **One hit = 1 HP** for every unit type. There are no damage values.
- **Snowball** comes only from the item shop, monster kills and structure kills. Champions do not level up.
- **Balance requirement:** Across the game, every champion should be able to use its AP-cost abilities at a roughly equal rate. See §14.

---

## 1. Components

| Component | Notes |
|---|---|
| Board | Hexagon, 7 hexes per side, 127 hexes. Built from 27 double-sided hexgroup tiles (see §2). |
| Champion cards | 10 total, 5 per player. Each card shows HP, Speed, L0 and four abilities (Q, W, E, R). |
| Champion standees | 10 total. |
| Team dashboard | One per player. HP cubes for each champion, the AP pool area, and the cooldown track. |
| Cooldown track | One per player, positions 4-3-2-1-0. Position 0 is "in hand" (ready). |
| Round tracker | Shared. Shows the round number, the Priority marker and the death-timer bands. |
| Chips | Poker chips. **Every chip is 1 HP and 1 AP.** Chips represent the HP of minions, monsters, towers and the Nexus, and also serve as the AP tokens in each team's pool. Minion chips come in each team's colour. |
| Structure markers | Per team: 6 towers (outer T1 and inner T2 in each lane) and 1 Nexus. |
| Monster markers | Dragon, Baron, and two each of Blue Buff, Red Buff, Wolves, Raptors and Krugs. |
| Item cards | A fixed catalogue: each player has their own set of every item (§12). |
| Buff cards | Blue Buff, Red Buff, Dragon and Baron cards (see §11). |

---

## 2. Map

### 2.1 Geometry and coordinates

- The board uses flat-top hexes with axial coordinates (q, r), where s = −q − r.
- Every hex satisfies max(|q|, |r|, |s|) ≤ 6.
- North is negative r. The North base sits in the north corner, the South base in the south corner.
- The tile layout is mirror-symmetric in both directions: north–south, (q, r) → (q, −q − r), and east–west, (q, r) → (−q, r + q).
- The monster pits are **point-symmetric** only. Dragon at (3,−1) is 1 hex closer to the South Nexus. Baron at (−3,1) is 1 hex closer to the North Nexus. Each team therefore has one objective slightly nearer to it.
- **Top lane** runs along the west edge and **Bot lane** along the east edge.
- **Baron** is in the west river, **Dragon** in the east river.

### 2.2 Hexgroups (tiles)

Every hex belongs to exactly one tile. There are **27 tiles** in total; full membership is in Appendix A.

**Tile rules**
- **Size:** at most 7 hexes. Tile sizes are 3, 4, 5 and 7.
- **Width:** at most 2 steps between any two hexes in a tile.
- **Flippable:** every tile is mirror-symmetric, so it fits back into place when flipped.

| Tile (count) | Hexes | Contents |
|---|---|---|
| North Base / South Base (2) | 7 | Fountain, Nexus, mid T2 |
| Mid Lane Inner (2: N, S) | 5 | Mid lane between the base and T1; no tower |
| Mid Lane Outer (2: N, S) | 4 | Mid T1 |
| Mid River (1) | 5 | Centre of the map |
| Lane Inner (4: Top/Bot × N/S) | 5 | That lane's T2 |
| Lane Outer (4: Top/Bot × N/S) | 5 | That lane's T1, on the map corner, plus one jungle-edge hex |
| River Crossing (2: Top, Bot) | 5 | Side lane where the river meets it |
| Dragon Pit / Baron Pit (2) | 4 | Dragon / Baron |
| Jungle (4: East/West × N/S) | 5 | Wolves, Raptors or Krugs (see §2.5) |
| Buff tiles (4: North/South × Blue/Red) | 3 | Blue Buff or Red Buff |

**Hidden-route distances** (tiles stepped through when everything on the route is hidden):

| Route | Tiles |
|---|---|
| Own base → own outer side-lane tower | 2 |
| Own base → Dragon Pit, Baron Pit or Mid River | 3 |
| Own base → enemy outer side-lane tower | 4 |
| Base → base (also the longest route on the board) | 6 |

### 2.3 Structure positions (North team; South is the 180° rotation)

| Structure | Hex |
|---|---|
| Fountain | (0,−6) |
| Nexus | (0,−5) |
| Mid T2 | (0,−4) |
| Mid T1 | (0,−2) |
| Bot T2 | (3,−6) |
| Bot T1 | (6,−6) |
| Top T2 | (−3,−3) |
| Top T1 | (−6,0) |

Dragon sits at (3,−1), 6 hexes from the South Nexus and 7 from the North. Baron sits at (−3,1), 6 hexes from the North Nexus and 7 from the South. Both pits are 3 hidden tiles from either base.

### 2.4 Terrain

Terrain is shown by colour only. It has no rules effect yet [TBD].

| Terrain | Hexes |
|---|---|
| Base | The two base flowers (blue North, red South) |
| Lane (tan) | Every outer-ring hex outside the bases, plus the centre column q = 0 |
| River (blue) | Dragon Pit and Baron Pit tiles, plus (−1,0), (−1,1), (1,−1), (1,0), (−5,2), (−5,3), (5,−2), (5,−3) |
| Jungle (green) | All remaining hexes |

The per-hex terrain is listed in Appendix A.

### 2.5 Jungle camps

Each camp occupies its hex and blocks movement. The layout is point-symmetric, so every camp has a twin on the other side of the board.

| Camp | North-side hex (tile) | South-side hex (tile) |
|---|---|---|
| Blue Buff | (4,−4) (North Blue Buff) | (−4,4) (South Blue Buff) |
| Red Buff | (−4,0) (North Red Buff) | (4,0) (South Red Buff) |
| Wolves | (2,−4) (East Jungle N) | (−2,4) (West Jungle S) |
| Raptors | (2,−2) (East Jungle N) | (−2,2) (West Jungle S) |
| Krugs | (−2,−2) (West Jungle N) | (2,2) (East Jungle S) |

Each team's side holds one of each camp. East Jungle N and West Jungle S each contain two camps (Wolves and Raptors).

---

## 3. Hexgroups: Hidden and Visible

### 3.1 Hidden side

- A hidden hexgroup counts as **one space** for movement. It does **not**
  shorten effects: see §4.1.
- **A hidden hexgroup hides champions.** A champion inside one cannot be
  targeted, hit or affected by anything outside it. Minions, structures and
  monsters inside a hidden hexgroup keep their own hex and are affected
  normally (§4.1).
- **Cover cuts both ways: the ambush rule.** While a champion is inside a
  hidden hexgroup it may only reach *outside* that hexgroup with an **ambush
  ability** — the one ability on its card marked with the ambush icon (junglers
  carry two). Every other ability, and the basic attack, may still be used on
  anything sharing the hexgroup: that is how a jungler clears its camp and how
  a contested hexgroup is fought over.
- **An ambush is a one-shot, not a firing position.** Using an ambush ability
  on anything outside the hexgroup flips that hexgroup face up for the rest of
  the round, exposing the ambusher exactly as if it had stepped into the open.
- **Entering** a hidden hexgroup costs 1 movement. **Leaving** it for any adjacent hex costs 1 movement.
- Any number of units from **one team** may share a hidden hexgroup.

### 3.2 When a hexgroup flips

- A hexgroup must be on its visible side whenever units of **both teams** are inside it.
- Units that cause a flip: champions, minions and structures.
- Monsters are neutral and never cause a flip **[DEFAULT]**.

### 3.3 Flip procedure

1. When a moving unit would enter a hidden hexgroup that contains enemy units, the mover stops in the last hex it occupied outside that hexgroup.
2. The hexgroup flips to its visible side.
3. Units already inside choose individual hexes. They must be empty hexes within the hexgroup, and the owning player places them.
4. The mover continues with its remaining movement, now paying 1 per hex. It
   may end its movement inside the hexgroup it just revealed.

### 3.4 Overflow [DEFAULT]

If a hexgroup flips and more units are inside than there are empty hexes, the owner places the extra units in empty hexes adjacent to the hexgroup.

### 3.5 Flip-back [DEFAULT timing]

A visible hexgroup that contains units of at most one team flips back to its hidden side. This is checked at two moments:
- after every activation
- after minion movement in Upkeep

When a hexgroup flips back, the units inside lose their individual hexes and are simply "in" the hexgroup.

### 3.6 Minions and hexgroups [DEFAULT]

- Minions ignore the hidden-hexgroup movement shortcut. They always move hex by hex along their lane path.
- A minion wave always sits on a specific path hex, even inside a hidden hexgroup.

---

## 4. Distance, Stacking and Blocking

### 4.1 Distance: movement and effects

**Movement distance** is the shortest path counting each visible hex as 1 step
and each hidden hexgroup as 1 step.

**Effect distance** — every ability range, card range and World Phase
adjacency — is counted in **hexes**, from the acting unit's hex to the target's
hex. A hidden hexgroup is a shortcut for walking, not for shooting.

- Every unit inside one hidden hexgroup is adjacent to every other unit in it,
  including monsters. That is how a jungler reaches a camp.
- A champion inside a hidden hexgroup cannot be reached from outside it. It may
  still act outward, which reveals nothing by itself.
- A minion wave, tower, Nexus or monster inside a hidden hexgroup keeps its own
  hex: it reaches, and is reached at, plain hex range. A tower inside a hidden
  hexgroup therefore covers its own hex's neighbours, not the whole tile edge.
- Effect range ignores blocking. There is no line-of-sight rule **[DEFAULT]**.

### 4.2 Stacking

- A visible hex holds at most one unit: a champion, a minion wave, a structure or a monster.
- Units share space only inside hidden hexgroups (see §3.1).

### 4.3 Blocking

- A unit may not enter or pass through a hex holding an enemy unit.
- Champions block enemy champions and enemy minions.
- Structures and monsters block everything.
- A unit may pass through, but not stop in, a hex holding a friendly unit. This lets minion waves walk past their own towers.

---

## 5. Round Structure

Each round has five phases: Upkeep, Action, World, Shop, Win Check.

### 5.1 Upkeep (steps in order)

1. **Advance the round tracker.** Priority passes to the other player. The Priority Player is **Player 1** this round; the other player is **Player 2**.
2. **Shift both cooldown tracks down by 1.**
   - Any card that reaches position 0 returns to its owner's hand.
   - A returning dead champion respawns at its fountain with full HP.
3. **Fountain healing.** Every champion at its own fountain is restored to full HP. "At the fountain" means anywhere in its own base tile **[DEFAULT]**.
4. **Refresh AP.** Return all chips in each team's pool to the supply, then give each team 3 chips, plus 1 for each Dragon card it holds (maximum +2). AP never carries over between rounds.
5. **Minion movement.** All of Player 1's waves move, then all of Player 2's (see §9).
6. **Wave spawns.** New minion waves spawn on odd rounds.
7. **Monster respawns** (see §11).
8. **Flip-back check** (see §3.5).

### 5.2 Action Phase

**Snake order.** Activations alternate in this order:

| Activation | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Player | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 |

**Taking an activation.** When it is your activation, you choose one champion that is in your hand and hasn't activated this round, and activate it. Each champion activates at most once per round.

**Passing** **[DEFAULT]**. You may pass an activation instead. If you have no champions in hand, you must pass. Once one player has no champions left to activate, the other player takes their remaining activations back to back.

**What an activation contains.**
- The champion moves up to its Speed.
- The champion uses at most one ability, either before or after that movement but not partway through it **[DEFAULT]**.
- Movement printed in an ability's own icon sequence is separate from the champion's Speed movement.

**Recall.**
- **Where:** only while the champion is inside a hidden hexgroup. A tile is hidden only when no enemy is in it, so a champion can never recall while an enemy shares its tile.
- **Cost:** 1 movement. The champion is placed at its fountain.
- **After recalling:** it continues with any remaining movement from the fountain, and may still use its ability before or after moving as normal.
- **Healing:** a champion that is at its fountain at the start of the next round heals to full HP (§5.1, step 3).
- **Walking home** is just normal movement, not a recall.

**Whole-card cooldown.** When a champion uses an ability, its entire champion card goes onto the cooldown track at the position equal to that ability's cooldown. That champion cannot activate at all (no movement, no abilities) until the card returns to hand. It stays on the board, where it still blocks and can still be targeted.

**Move-only activation.** Movement is free: a champion that moves without using an ability does not go on the cooldown track. Turn its card sideways to show it has activated this round **[DEFAULT marker]**, and straighten all cards in Upkeep.

**Playing buff and item cards.** A buff card (§11) or item card (§12) is played together with the activating champion's ability, and both take effect. A champion that only moves cannot play these cards.

### 5.3 World Phase

- Every minion wave, tower and monster deals hits to **all adjacent enemy units** at the same time. Adjacency is effect distance 1 (§4.1), so a source inside a hidden hexgroup reaches its own hex's neighbours, and a champion hidden inside a hexgroup is not reached at all.
- Damage is applied at the same moment for everyone. Two opposing waves trading hits lose chips at the same rate.

Hit values for each source are listed below.

| Source | Hits |
|---|---|
| Minion wave | 1 hit to each adjacent enemy unit |
| Tower, vs. an adjacent enemy champion | 2 hits |
| Tower, vs. an adjacent enemy minion wave | 1 hit (removes 1 chip) |
| Tower, vs. an adjacent monster | Does not target monsters **[DEFAULT]** |
| Monster | 1 hit to each adjacent champion **[DEFAULT placeholder; see §11]** |
| Nexus | Does not attack **[DEFAULT]** |

### 5.4 Shop Phase

- Player 1, then Player 2, may spend any AP left in their pool on items (§12).
- This includes AP gained from chips during the round. Farming therefore pays for items as well as same-round abilities.
- Any AP still unspent is lost when the pool resets in the next Upkeep.

### 5.5 Win Check

If a Nexus is at 0 HP, its owner loses. Otherwise, begin the next round. See §13 for the round limit.

---

## 6. Champions

### 6.1 Stats

| Stat | Range |
|---|---|
| HP | 6–9 |
| Speed | 2–4 |

Both stats are champion design parameters and are paid for out of the design budget (§14).

### 6.2 Abilities

**L0**, identical on every champion:

| Cost | Cooldown | Range | Effect |
|---|---|---|---|
| 0 AP | 1 | Adjacent | 1 hit |

**Q, W, E and R**, set per champion:

| Parameter | Allowed values |
|---|---|
| Cost | 0–3 AP |
| Cooldown | 1 or more |
| Range | Stated on the card |
| Effect | An icon sequence of hits, moves and effects |

- A cooldown of 1 means the champion is usable again next round.
- A cooldown of N means the champion misses N − 1 rounds.
- There is no fixed Q/W/E/R tier structure. R is expected to be the high-impact ability, but that is a design norm rather than a rule.

### 6.3 Icon grammar [DRAFT]

An ability is written as **cost · cooldown · a sequence of steps**. One
ability per card also carries the **ambush icon** (§3.1); junglers carry two.
An ambush ability is normally a move-and-attack, so springing it commits the
champion rather than letting it poke from cover.

An ability is written as **cost · cooldown · a sequence of steps**. Steps resolve left to right; an arrow (→) separates them.

**Targeting**
- A step with a range measures it from the champion's position at the moment the step resolves, using board distance (§4.1).
- Control icons that follow a HIT apply to that HIT's target. A standalone control icon targets a unit within range 1.
- Target types:

| Marker | Meaning |
|---|---|
| (none) | Any enemy unit: champion, wave, monster or structure |
| ◆ | Enemy champion only |
| ✚ | Friendly champion (self included) |

- Hits on chips earn AP (§7). Hits on champions remove HP cubes.

**Damage icons**

| Icon | Effect |
|---|---|
| HIT r | 1 hit on one target within range r |
| HIT×k r | k hits on the same target |
| AREA k r | k hits on every enemy unit within r of the champion |
| LINE k n | k hits on every enemy unit in a straight line of n hexes from the champion |

**Movement icons (self)**

| Icon | Effect |
|---|---|
| MOVE n | Up to n hexes, following normal movement and blocking rules |
| DASH n | Up to n hexes in a straight line. It passes through units but must end in an empty hex |
| BLINK n | Place the champion in any empty hex within n |

**Control icons**

| Icon | Effect |
|---|---|
| PUSH n | Move the target up to n hexes directly away. It stops early if blocked |
| PULL n | Move the target up to n hexes directly toward the champion |
| SLOW n | Target gets −n Speed on its next activation |
| ROOT | Target cannot move on its next activation. ROOT (area) roots every enemy within range 1 |
| DELAY | The target champion's card moves 1 position up the cooldown track (or onto position 1 if it's in hand) |

**Support icons**

| Icon | Effect |
|---|---|
| HEAL n r | Restore n HP to a friendly champion within r |
| SHIELD n r | A friendly champion within r ignores the next n hits it takes before the end of the next round |
| HASTE r | A friendly champion's card moves 1 position down the cooldown track |
| REVEAL r | Flip a tile within r visible until the end of the round |

This vocabulary is a starting set. New icons are allowed if they get a point value in §14.2.

### 6.4 Death and respawn

- A champion at 0 HP is removed from the board.
- Its card is placed on the cooldown track according to the round it died in:

| Died in | Track position | Full rounds missed |
|---|---|---|
| Rounds 1–4 | 2 | 1 |
| Rounds 5–8 | 3 | 2 |
| Rounds 9+ | 4 | 3 |

- The champion respawns at its fountain with full HP when the card returns to hand. If the fountain hex is occupied, it respawns in any empty hex of its base **[DEFAULT]**.
- The killing team gains **+1 AP** immediately.

### 6.5 Healing

Champions heal in three ways:
- **Abilities.** Healing is part of champion kits, via the Heal icon (§6.3).
- **Fountain.** A champion at its own fountain at the start of a round is restored to full HP (§5.1, step 3). Champions get there by recalling or walking (§5.2).
- **Respawn.** A dead champion respawns at full HP.

---

## 7. Action Points (AP)

- **Refresh:** Each team's pool is set to 3 in every Upkeep. Unspent AP is lost at the end of the round.
- **No cap:** A team may gain any amount of AP within a round. Combo turns are intended.
- **Spending:** AP pays for ability costs and buff-card effects during the Action Phase, and for items in the Shop Phase at the end of the round.
- **Chips are AP.** When a champion's hit removes a chip from a minion wave, monster, tower or Nexus, that chip goes straight into the champion's team pool. It can be spent immediately.
  - An ability that removes 3 chips gains 3 AP.
  - There is no separate kill bonus. HP *is* the reward, so an 8-HP tower is worth 8 AP to whoever chips it down.
  - The old "minion refund" rule is replaced by this rule.
- **World Phase chips go to the supply.** Chips removed by towers, minions or monsters benefit no one.
- **Champion kills:** Champion HP is tracked with cubes, not chips, so hitting a champion gains no AP. A champion kill gives **+1 AP**.
- **Buff cards:** Blue Buff cards give AP (§11).

---

## 8. Structures

**Towers**
- 11 HP each, as 11 chips. Removing a tower's chips earns AP (§7).
- Each tower occupies its hex and blocks all movement.
- They deal hits as listed in §5.3.

**Nexus**
- 12 HP. Does not attack.

**Fountain**
- The respawn point. Any other function is [TBD].

**Protection order (outward in)**
- A T2 cannot be hit until the T1 in the same lane is destroyed.
- A Nexus cannot be hit until both towers in at least one lane are destroyed.

---

## 9. Minions

### 9.1 Waves

- A wave is a stack of chips in one hex. It acts as a single unit whose HP equals its number of chips.
- Waves spawn on **odd rounds**, one per lane per team, in that team's spawn hex.
- A wave has **3 chips**, rising to **4 chips from Round 7**.

| Lane | North spawn hex | South spawn hex |
|---|---|---|
| Top | (−2,−4) | (−2,6) |
| Mid | (0,−3) | (0,3) |
| Bot | (2,−6) | (2,4) |

**Occupied spawn hex [DEFAULT]**
- If a friendly wave is already there, the new chips merge into it.
- If an enemy unit is there, that spawn is skipped.

### 9.2 Movement

- Waves move **2 hexes** along their lane path each Upkeep. Player 1's waves move first.
- A wave stops instead of entering a hex it cannot enter. Friendly structures can be passed through but not stopped in.
- A wave behind a stopped friendly wave also stops **[DEFAULT]**.

### 9.3 Lane paths (North waves, listed in travel order)

| Lane | Path |
|---|---|
| Mid | (0,−3) → (0,4) |
| Bot | (2,−6), (3,−6) … (6,−6), (6,−5) … (6,0), (5,1) … (2,4), then (1,4) |
| Top | (−2,−4), (−3,−3) … (−6,0), (−6,1) … (−6,6), (−5,6) … (−2,6), then (−1,5) |

- Each path ends in a hex adjacent to the enemy Nexus.
- South waves use the 180° rotation of these paths.

### 9.4 Combat

- Minions hit during the World Phase (§5.3).
- **Farming:** Every chip a champion removes from a wave is +1 AP for its team (§7). The free L0 ability (1 hit, adjacent) therefore earns 1 AP per use against a wave.

---

## 10. Hexgroup Tiles: Physical Notes

- Each hexgroup is one physical tile.
  - **Hidden side:** only the outline of the whole hexgroup is printed.
  - **Visible side:** each individual hex is outlined.
- Tiles are 3–7 hexes (mostly 5), and no tile is more than 2 steps across. Every hex on the board belongs to exactly one tile.
- Every tile shape has at least one mirror axis. Flipping a tile over that axis returns it to the same outline, so it always fits back in place.

---

## 11. Monsters

Positions are fixed (§2.3 and §2.5). Every monster's HP is a stack of chips, and each chip a champion removes is +1 AP (§7).

**Rewards**

| Monster | Reward beyond its chips |
|---|---|
| Wolves, Raptors, Krugs | None. Their chips are the whole reward. |
| Blue Buff | The killing team takes a **Blue Buff card**: gain 2 AP immediately. |
| Red Buff | The killing team takes a **Red Buff card**: deal 2 hits immediately to a target adjacent to the champion playing it. Both hits go to one target **[DEFAULT]**. |
| Dragon | The killing team takes a **Dragon card** and keeps it for the rest of the game. Each Dragon card adds +1 AP at every Upkeep refresh. A team can benefit from at most 2 Dragon cards (+2 AP). |
| Baron | The killing team takes the **Baron card** and places it on its cooldown track at position 3 **[DEFAULT timing]**. While the card is on the track, that team's minion waves are **Empowered** (below). |

**Buff card rules**
- Each buff card is used once, then discarded.
- It is played together with a champion's ability during that champion's activation (§5.2), and both take effect.
- Chips removed by a Red Buff card's hits earn AP as normal.
- A team may hold a buff card across rounds until it plays it **[DEFAULT]**.

**Empowered minions (Baron)**
- Every wave spawned while the Baron card is on the track spawns with +2 chips.
- Every one of that team's waves deals 2 hits (instead of 1) to adjacent enemy towers and the Nexus.
- The effect ends when the Baron card leaves the track, which is 3 Upkeeps after the kill. It then returns to the supply until Baron is killed again.
- Tracking the buff on the cooldown track means no extra timer component is needed.

**Placeholder values for simulation** (HP is also the AP value)

| Monster | HP | Spawn / respawn |
|---|---|---|
| Wolves, Raptors, Krugs | 3 | Spawn in Round 1; respawn 3 rounds after being killed |
| Blue Buff, Red Buff | 4 | Spawn in Round 1; respawn 4 rounds after being killed |
| Dragon, at (3,−1) | 8 | Spawns in Round 3; respawns 4 rounds after being killed |
| Baron, at (−3,1) | 12 | Spawns in Round 7; respawns 5 rounds after being killed |

Monsters hit adjacent champions (see §5.3). They are neutral and never cause a tile to flip.

---

## 12. Shop and Items

**Rules**
- Items are bought in the **Shop Phase at the end of each round** (§5.4), with any AP left in the pool, from anywhere on the map.
- **Fixed catalogue.** Every item is always available. Each player has their own copies, so nothing is drawn or sold out.
- Buying items is the main way a lead snowballs. AP you don't spend on abilities becomes strength in later rounds.
- There are two kinds of item:
  - **Stat boosts** apply directly to one champion permanently and persist through death. There are no item slots. A champion may take each boost only once **[DEFAULT]**.
  - **Cards in hand** go to the team's hand. They follow the buff-card rules (§11): one use, played together with a champion's ability. A team may hold at most 2 copies of each card **[DEFAULT]**.

**Starter catalogue [DEFAULT prices; the Monte Carlo agent should tune them]**

The economy assumption behind the prices: about 3 base AP plus roughly 3–6 AP from chips per round, much of it spent on abilities, leaving about 2–4 AP per round for items. Over about 15 rounds that is roughly 40–50 AP of items per team.

*Stat boosts (permanent, applied to one champion)*

| Item | Cost | Effect |
|---|---|---|
| Ruby Crystal | 4 | +2 max HP. Also heal 2 now. |
| Boots | 4 | +1 Speed (maximum Speed 5). |
| Vampiric Blade | 5 | Heal 1 each time this champion removes a chip. Gives sustain in lane without recalling. |
| Cloth Armor | 5 | Take 1 fewer hit from each tower, minion or monster source in the World Phase. |
| Long Sword | 6 | This champion's L0 deals 2 hits instead of 1. A farming engine. |
| Longbow | 6 | +1 range to all of this champion's abilities, except L0. |
| Ionian Charm | 8 | This champion's ability cooldowns are 1 lower (minimum 1). |

*Cards in hand (one use)*

| Item | Cost | Effect |
|---|---|---|
| Swift Tonic | 1 | The playing champion gets +2 Speed this activation. |
| Health Potion | 2 | Heal the playing champion 3. |
| Control Ward | 2 | Choose a tile containing or adjacent to the playing champion. It is flipped visible and stays visible until the end of the next round, and cannot flip back while the ward is there. This removes the hidden shortcut and stops enemy recalls on that tile. |
| Frost Charm | 2 | An enemy champion within range 2 of the playing champion has −2 Speed on its next activation (minimum 0). |
| Stopwatch | 3 | Move one of your champion cards 1 position down the cooldown track. If it reaches 0, it returns to hand immediately. |

---

## 13. Win Conditions and Game Length

- **Win:** Destroy the enemy Nexus.
- **Round limit:** Round 20 is a hard stop. The winner is decided by towers destroyed, then total structure HP remaining, then champion kills.
- **Reaching the limit is a design failure, not a normal ending.** Estimated round length is 4–5 minutes, so 60–90 minutes is roughly 13–18 rounds. Games should end by Nexus kill well before Round 20.

**Pacing levers**

If simulated games run long, tune these (roughly from gentlest to strongest) rather than lowering the limit:

| Lever | Current value |
|---|---|
| Minion wave size | 3 chips, rising to 4 from Round 7 |
| Minion wave schedule | Odd rounds only |
| Wave growth | +1 chip from Round 7 |
| Death timers | 1, 2 or 3 rounds missed, by round band (§6.4) |
| Baron strength | +2 chips per wave; 2 hits on structures; lasts 3 rounds |
| Baron timing | Spawns Round 7 |
| Dragon cap | +2 AP |
| Tower HP | 11 (raised from 8 by patch P-0002 to bring median game length into 13–15 rounds) |
| Nexus HP | 12 |
| Tower damage | 2 hits to champions |
| Protection order | T1 before T2; one lane of towers before the Nexus |

---

## 14. Champion Design Framework (for the Monte Carlo agent)

### 14.1 Parameters per champion

- Role
- HP (6–9)
- Speed (2–4)
- Four abilities, each with: cost (0–3), cooldown (≥1), range, and icon sequence

### 14.2 Design budget [DRAFT seed values]

Every champion is built to **22 ± 2 points**. The Monte Carlo agent should treat the values below as a starting point and recalibrate them from simulation results. Values that are too high will show up as champions winning more than expected at that budget.

**Equalising with stat levers.** Champions are balanced to the budget mainly through their stats, not by reworking abilities:
1. Design the four abilities and total their net values.
2. Choose HP (6–9) and Speed (2–4) to bring the champion's total as close to 22 as possible, within ±2.
3. Only if no stat combination reaches the band, adjust ability numbers: hits, range, cost, cooldown.
4. After simulation, fix an over- or under-performing champion with the smallest change first:
   - a stat lever, such as ±1 HP (±3 points) or ±1 Speed (±5 points);
   - then ability numbers;
   - redesign an ability only as a last resort.

**Stats** (L0 is standard and costs nothing)

| Stat | Points |
|---|---|
| HP | +3 per HP above 6 |
| Speed | +5 per step above 3; −5 per step below 3 |

**Steps**

| Icon | Points |
|---|---|
| HIT | 3 per hit, plus 1 per hit for each range step beyond 1 |
| AREA | 6 per hit at r1, +4 per extra step of range (10 at r2, 14 at r3) |
| LINE | (3 + n) per hit |
| MOVE | 1 per hex |
| DASH | 1.5 per hex |
| BLINK | 2 per hex |
| PUSH, PULL | 2 per hex |
| SLOW | 1.5 per point |
| ROOT | 5 (single); 8 (area) |
| DELAY | 8 |
| HEAL | 2 per HP |
| SHIELD | 1.5 per hit |
| Friendly target at range 2 or more | +1 |
| HASTE | 6 |
| REVEAL | 3 |

*Why AREA and LINE cost more than their hits suggest.* Chips are AP (§2.2), so
an ability's real price is the chips it can bank, not the hits it writes on the
card. AREA and LINE touch several units at once and were priced as though they
touched one.

**Credits** (subtracted from an ability's value)
- −2 per AP of cost.
- −1.5 per cooldown round beyond 1. Because the whole card goes on cooldown, a champion on cooldown can't move and is exposed on the board.

*Why these are smaller than they look.* An ability is priced against the
**activation** it consumes, not only against its AP. A champion activates once
per round and any ability puts the whole card on the track, so a 0 AP ability
and a 3 AP ability cost the same activation. Crediting price too generously
buys large ultimates and leaves the cheap slots too weak to be worth using —
which is exactly what simulation found (see the RQ-030 entry in the decision
log).

**Constraints**
- HP 6–9 and Speed 2–4.
- **An ability containing AREA or LINE costs at least 1 AP.** These are farming
  engines: they bank a chip from every unit they touch, so a free one pays for
  itself several times over in a single activation. Simulation found the four
  worst AP outliers in the roster were exactly the champions holding a cheap
  one.
- Exactly one ability carries the ambush icon, or two for a jungler. This costs
  no points: every champion has one, so it prices into the baseline rather than
  into any single kit. Prefer a move-and-attack; where a kit has none, the
  shortest-reach attack is the closest thing to committing.
- **Each ability's net value is at least 3** — it has to be worth the
  activation it spends.
- R has the highest gross value (before credits) of the four abilities, and
  **no more than 1.75× the average gross of Q, W and E**. A kit whose R dwarfs
  its basics is a kit with one real ability.
- Cost 0–3 AP; cooldown 1 or more.

**Economy watch:** any ability that can put k hits on a single wave returns k AP. So an ability with cost < hits is a farming engine. Track AP generated per champion as its own metric.

**Worked examples**

*Bastion (tank)*: HP 9 (+9), Speed 2 (−5). Stats total 4.

| Ability | Cost / CD | Steps | Gross | Net |
|---|---|---|---|---|
| Q | 0 / 1 | HIT 1 → PUSH 1 | 5 | 5 |
| W | 1 / 1 | SHIELD 4 ✚ r2 | 7 | 4 |
| E | 1 / 2 | DASH 2 → ROOT ◆ | 8 | 3 |
| R | 3 / 3 | AREA 2 r1 → ROOT (area) | 18 | 5 |

Total: **21**.

*Kestrel (marksman)*: HP 8 (+6), Speed 3 (0). Stats total 6. HP was raised from 7 to 8 to bring the total nearer 22.

| Ability | Cost / CD | Steps | Gross | Net |
|---|---|---|---|---|
| Q | 0 / 1 | HIT 3 | 5 | 5 |
| W | 1 / 1 | HIT×2 3 | 10 | 7 |
| E | 0 / 2 | BLINK 2 | 4 | 2 |
| R | 3 / 3 | LINE 2 6 | 16 | 3 |

Total: **23**. Note that Kestrel's W nets +1 AP per use against a wave, so it's a farming engine.

### 14.3 Balance targets (pass/fail checks)

| Check | Target |
|---|---|
| Ability usage | Each AP-cost ability is used in 40–70% of rounds where it's affordable and has a legal target. No champion is more than 15 percentage points from the roster mean. |
| Win rate | Every champion's win rate is within ±5% of 50% across randomised teams. |
| Player-seat balance | Priority/first-player win rate is within 48–52%. |
| Game length | Median game length is 13–18 rounds. |
| Nexus kills | 95% or more of games end by Nexus destruction before the Round 20 limit. |
| Economy | No single champion generates more than 1.5× the roster-mean AP per round. |

---

## 15. Open Items

1. **Tuning pass** on HP values, item prices, point values and pacing levers. The multi-agent loop does this against the balance targets in §14.3.
2. **Remaining [DEFAULT] rulings are minor edge cases.** They cover overflow placement, flip-back timing, spawn-hex conflicts, passing, and card-holding limits. The Rule Designer agent may propose changes if the simulation shows a problem.

---

## Appendix A — Map Data (machine-readable)

```json
{
  "coords": "axial (q,r), flat-top, north = negative r; radius 6. 27 tiles, each mirror-symmetric (flippable), max 7 hexes, max internal distance 2.",
  "hexgroups": {
    "Baron Pit": [[-4,2],[-3,1],[-3,2],[-2,1]],
    "Bot Lane N Inner": [[2,-6],[2,-5],[3,-6],[3,-5],[4,-6]],
    "Bot Lane N Outer": [[4,-5],[5,-6],[5,-5],[6,-6],[6,-5]],
    "Bot Lane S Inner": [[2,3],[2,4],[3,2],[3,3],[4,2]],
    "Bot Lane S Outer": [[4,1],[5,0],[5,1],[6,-1],[6,0]],
    "Bot River Crossing": [[5,-3],[5,-2],[6,-4],[6,-3],[6,-2]],
    "Dragon Pit": [[2,-1],[3,-2],[3,-1],[4,-2]],
    "East Jungle N": [[2,-4],[2,-3],[2,-2],[3,-4],[3,-3]],
    "East Jungle S": [[2,0],[2,1],[2,2],[3,0],[3,1]],
    "Mid Lane N Inner": [[-1,-3],[-1,-2],[0,-3],[1,-4],[1,-3]],
    "Mid Lane N Outer": [[-1,-1],[0,-2],[0,-1],[1,-2]],
    "Mid Lane S Inner": [[-1,3],[-1,4],[0,3],[1,2],[1,3]],
    "Mid Lane S Outer": [[-1,2],[0,1],[0,2],[1,1]],
    "Mid River": [[-1,0],[-1,1],[0,0],[1,-1],[1,0]],
    "North Base": [[-1,-5],[-1,-4],[0,-6],[0,-5],[0,-4],[1,-6],[1,-5]],
    "North Blue Buff": [[4,-4],[4,-3],[5,-4]],
    "North Red Buff": [[-5,1],[-4,0],[-4,1]],
    "South Base": [[-1,5],[-1,6],[0,4],[0,5],[0,6],[1,4],[1,5]],
    "South Blue Buff": [[-5,4],[-4,3],[-4,4]],
    "South Red Buff": [[4,-1],[4,0],[5,-1]],
    "Top Lane N Inner": [[-4,-2],[-3,-3],[-3,-2],[-2,-4],[-2,-3]],
    "Top Lane N Outer": [[-6,0],[-6,1],[-5,-1],[-5,0],[-4,-1]],
    "Top Lane S Inner": [[-4,6],[-3,5],[-3,6],[-2,5],[-2,6]],
    "Top Lane S Outer": [[-6,5],[-6,6],[-5,5],[-5,6],[-4,5]],
    "Top River Crossing": [[-6,2],[-6,3],[-6,4],[-5,2],[-5,3]],
    "West Jungle N": [[-3,-1],[-3,0],[-2,-2],[-2,-1],[-2,0]],
    "West Jungle S": [[-3,3],[-3,4],[-2,2],[-2,3],[-2,4]]
  },
  "north": {
    "fountain": [0,-6],
    "nexus": [0,-5],
    "towers": {
      "mid_T2": [0,-4],
      "mid_T1": [0,-2],
      "bot_T2": [3,-6],
      "bot_T1": [6,-6],
      "top_T2": [-3,-3],
      "top_T1": [-6,0]
    },
    "lane_paths": {
      "top": [[-2,-4],[-3,-3],[-4,-2],[-5,-1],[-6,0],[-6,1],[-6,2],[-6,3],[-6,4],[-6,5],[-6,6],[-5,6],[-4,6],[-3,6],[-2,6],[-1,5]],
      "mid": [[0,-3],[0,-2],[0,-1],[0,0],[0,1],[0,2],[0,3],[0,4]],
      "bot": [[2,-6],[3,-6],[4,-6],[5,-6],[6,-6],[6,-5],[6,-4],[6,-3],[6,-2],[6,-1],[6,0],[5,1],[4,2],[3,3],[2,4],[1,4]]
    }
  },
  "south": {
    "fountain": [0,6],
    "nexus": [0,5],
    "towers": {
      "mid_T2": [0,4],
      "mid_T1": [0,2],
      "bot_T2": [-3,6],
      "bot_T1": [-6,6],
      "top_T2": [3,3],
      "top_T1": [6,0]
    },
    "lane_paths": {
      "top": [[-2,6],[-3,6],[-4,6],[-5,6],[-6,6],[-6,5],[-6,4],[-6,3],[-6,2],[-6,1],[-6,0],[-5,-1],[-4,-2],[-3,-3],[-2,-4],[-1,-4]],
      "mid": [[0,3],[0,2],[0,1],[0,0],[0,-1],[0,-2],[0,-3],[0,-4]],
      "bot": [[2,4],[3,3],[4,2],[5,1],[6,0],[6,-1],[6,-2],[6,-3],[6,-4],[6,-5],[6,-6],[5,-6],[4,-6],[3,-6],[2,-6],[1,-5]]
    }
  },
  "monsters": {
    "dragon": [[3,-1]],
    "baron": [[-3,1]],
    "blue_buff": [[4,-4],[-4,4]],
    "red_buff": [[-4,0],[4,0]],
    "wolves": [[2,-4],[-2,4]],
    "raptors": [[2,-2],[-2,2]],
    "krugs": [[-2,-2],[2,2]]
  },
  "terrain": {
    "lane": [[-6,0],[-6,1],[-6,2],[-6,3],[-6,4],[-6,5],[-6,6],[-5,-1],[-5,6],[-4,-2],[-4,6],[-3,-3],[-3,6],[-2,-4],[-2,6],[0,-3],[0,-2],[0,-1],[0,0],[0,1],[0,2],[0,3],[2,-6],[2,4],[3,-6],[3,3],[4,-6],[4,2],[5,-6],[5,1],[6,-6],[6,-5],[6,-4],[6,-3],[6,-2],[6,-1],[6,0]],
    "river": [[-5,2],[-5,3],[-4,2],[-3,1],[-3,2],[-2,1],[-1,0],[-1,1],[1,-1],[1,0],[2,-1],[3,-2],[3,-1],[4,-2],[5,-3],[5,-2]],
    "jungle": [[-5,0],[-5,1],[-5,4],[-5,5],[-4,-1],[-4,0],[-4,1],[-4,3],[-4,4],[-4,5],[-3,-2],[-3,-1],[-3,0],[-3,3],[-3,4],[-3,5],[-2,-3],[-2,-2],[-2,-1],[-2,0],[-2,2],[-2,3],[-2,4],[-2,5],[-1,-3],[-1,-2],[-1,-1],[-1,2],[-1,3],[-1,4],[1,-4],[1,-3],[1,-2],[1,1],[1,2],[1,3],[2,-5],[2,-4],[2,-3],[2,-2],[2,0],[2,1],[2,2],[2,3],[3,-5],[3,-4],[3,-3],[3,0],[3,1],[3,2],[4,-5],[4,-4],[4,-3],[4,-1],[4,0],[4,1],[5,-5],[5,-4],[5,-1],[5,0]]
  }
}
```

## Appendix B — Map Image

See `hex_nexus_map_v0_7.svg`: thick outlines mark tile borders, dotted outlines mark individual hexes, pink dashed lines mark each tile's flip axis, and brown dots mark minion lane paths.
