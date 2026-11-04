# Generation Ship — Game Design Document v0

*Working title: none chosen yet. "Generation Ship" is a placeholder.*

**Status:** v0. This document records the decisions made during the design conversation, the reasons for them, and what is still open. Values marked **(default)** were not decided in conversation. They are starting points for the prototype, live in the config file, and are listed again under *Open questions*.

---

## Tech stack

Browser prototype: **vanilla JavaScript (ES modules) + HTML/CSS + inline SVG for the ship map + Web Audio API.** No build step; it runs from a static file server. *(default: the tech stack was not discussed.)*

Suggested file structure:
- `index.html`: entry point and layout.
- `src/main.js`: boot, game loop, phase sequencing.
- `src/config.js`: **every tunable value and rule toggle** (pool sizes, health, damage, costs, hand size, card plays, deck sizes, Offset/Direct toggle, Landfall card toggle).
- `src/state.js`: the game state model, plus undo snapshots for rapid testing.
- `src/phases/`: one file per phase (`growth.js`, `fast.js`, `dusk.js`, `day.js`, `dawn.js`, `slow.js`, `timePasses.js`).
- `src/systems/`: `threat.js`, `crew.js`, `decay.js`, `influence.js`, `purpose.js`, `leaders.js`, `wall.js`, `tokens.js`, `targeting.js`.
- `src/data/`: `boards.js`, `people.js` (Common and Remarkable cards), `events.js`, `discoveries.js`, `destinations.js`, `houses.js`.
- `src/ui/`: map renderer, conveyor/Wall panel, house panels, log.

Card and board content goes in data files, so new cards and boards can be added without touching logic.

---

## Game concept

A cooperative strategy board game for 1–4 players, structurally modeled on **Spirit Island**. The players are the **Great Houses** of a centuries-old **generation ship** whose technology is so old the crew no longer understands it. They treat it as ritual and near-magic: Engineers are a priesthood, and the reactor is "the Heart." This is the **Forgotten Machine** tone.

Spirit Island's Explore → Build → Ravage conveyor becomes **Dawn → Day → Dusk**. Every round is a **generation**:
- the rising heir enters at **Dawn**,
- rules the ship as **Steward** at **Day**,
- ages out as **Elder** at **Dusk**, leaving a **Legacy**,
- then retires to the **Wall of Leaders**.

Each leader carries the crisis of their reign with them down the conveyor. The houses choose who leads from among the people they played, knowing that the leader's legacy will land a generation later.

Inspirations: *Spirit Island* (structure, threat conveyor, elements, fear, adversaries), and the Dawn/Day/Dusk generational triad from the *Foundation* TV series. The triad is used as a structural inspiration only; none of that IP is used.

---

## Visual style

*(Directional default: visual style was not discussed. It follows from the Forgotten Machine tone.)*
- **The look:** ancient technology treated as sacred. Think a ship's schematic redrawn as an illuminated manuscript: worn, ritualized, hand-annotated.
- **Sections** read as machine-diagrams with a ceremonial overlay.
- **Pieces are simple, distinct glyphs.** The threat ladder (Glitch / Fault / Failure) must be readable at a glance by size and shape.
- **Avoid:** sleek modern sci-fi chrome, grimdark, and clutter that hides piece counts.
- **For the prototype,** clarity beats art: flat shapes, clear labels, colored section-type fills.

---

## Camera

A static 2D top-down view of the full ship map, which is 1–4 connected player boards. It must:
- show every section, its pieces and its adjacency (conduits) at once,
- support pan and zoom when 3–4 boards are in play,
- keep the leader conveyor and the Wall permanently visible outside the map area.

---

## Controls

Mouse-driven, **hot-seat**: one person can control every house, for rapid solo prototyping.
- **Growth:** click a growth option on the house panel.
- **Commit:** click cards in a hand to play them. Credits are deducted automatically. Mark one played card as the **nominee**. Click a card in hand to place it in the clone slot.
- **Resolving a power:** select the card. Legal target sections (by range and type) highlight; click one. Then follow prompts for piece choices, such as which Glitch to damage or where to vent.
- **Vote:** click one nominee, or enter tie-break by Steward's house.
- **Damage and cascade choices** (which Crew take damage, where Decay cascades) are prompted with clickable sections or pieces.
- A **"Next step"** button advances automatic phases. An **undo** button reverts to the last phase snapshot.
- A **settings panel** sets rule toggles, player count, destination and level before a game.

---

## Core gameplay loop

**Setup**
1. Choose the player count (1–4), a house per player, a destination and difficulty level, and the rule toggles (Offset/Direct, Landfall card on/off).
2. Lay out one ship board per player. Place the starting pieces shown by each board's setup symbols, and each house's starting influence.
3. Build the event deck: Stage I, Stage II, Stage III, plus any destination changes. Set the **Wall** to one slot per card in the event deck.
4. Set the Decay pool and Purpose pool for the player count. Set the Understanding tier to I.
5. Draw the **starting event** and a **random starting leader** from the Common people deck. Pair them in **Dawn** and resolve the event's **Dawn seed**. Then advance them to **Day**. *(Mirrors Spirit Island's setup explore, and avoids two leaders in Dawn on round 1.)* Dusk starts empty and the Wall starts empty.

**Each round (one generation)**
1. **Growth.** Each house draws a fresh hand from the Common deck (it may take Remarkable cards by draw substitution). It keeps any cloned card from last generation, picks one growth option, and gains credits.
2. **Commit.** Each house chooses its plays, up to its card-play limit, and pays their credit costs. It marks **one** played card as its **nominee**. The nominee costs 0 credits and is that house's only fast card. All other played cards are slow.
3. **Fast phase.** Nominees resolve.
4. **Dusk.**
   1. Earned Discovery cards resolve: for each, choose a one-time effect or a Breakthrough.
   2. The **Elder's Legacy** resolves in the sections matching the Elder's paired event.
   3. The Elder's event **collapses**.
5. **Day.** The Steward's **Reign** applies. The Steward's event **grows**.
6. **Dawn.**
   1. All houses **vote** for one nominee as successor. Ties go to the Steward's house's choice.
   2. The chosen card goes to the Dawn slot. Unchosen nominees go to the discard pile.
   3. **Offset (default toggle):** now draw the next event, pair it with the new heir, and resolve its **seed**.
   4. **Direct (toggle):** the event was drawn and shown before the vote; pair it and seed now.
7. **Slow phase.** All other played cards resolve. Targets are chosen now, with knowledge of the new event.
8. **Time passes.**
   1. The Dusk leader and its event (and any Breakthrough) move to the next Wall slot. Day moves to Dusk, and Dawn moves to Day.
   2. Damage on Crew and threat pieces clears.
   3. Hands are discarded, except cloned cards. Credits carry over.

**Ending**
- **Win (base):** you win the moment the board meets your current Understanding tier's condition **and** the destination's Landfall requirement.
- **Win (Landfall card toggle):** when the condition above is met, the players may place the set-aside Landfall event as the next Dawn event. You win when the Landfall event retires to the Wall with its leader.
- **Loss:** you lose if an event must be drawn at Dawn and the event deck is empty. *(The Wall is full and the deck is empty at the same moment.)*
- **Loss:** you lose if the Decay pool is empty after the Ship in Crisis card has flipped.
- **Loss:** you lose if any house has no influence on the ship.

---

## The leader conveyor (Dawn / Day / Dusk)

**Slots:** Dawn, Day and Dusk each hold one leader card paired with one event card.
- **Dawn** = the rising heir. Its event **seeds**.
- **Day** = the **Steward**. Its Reign applies, and its event **grows**.
- **Dusk** = the **Elder**. Its Legacy resolves, then its event **collapses**.

**Leader cards are people cards.** Any people card can become a leader. Its **Reign** and **Legacy** text is used only while it is in the conveyor.
- **Reign:** an ongoing effect while the card is in Day.
- **Legacy:** a one-time effect at Dusk, resolved **in the sections matching the leader's paired event**. Legacies are mostly costly.

**Nomination:**
- Each house nominates exactly **one** of the cards it played this generation.
- The nominee costs **0** credits and resolves in the fast phase.
- Houses may gain more fast candidates as a house growth unlock.

**Succession vote:**
- All houses choose one nominee. The Steward's house breaks ties.
- If no Steward exists (round 1 has a Steward from setup), the first player breaks ties. *(default)*

**What happens to leader cards:**
- The chosen card is **permanently removed** from the people deck. It goes Dawn → Day → Dusk → Wall.
- Unchosen nominees go to the people discard pile.

**Event pairing toggle:**
- **Offset (default):** the event is drawn *after* the vote, so you choose a leader without knowing what they will face. *Reason:* this recreates Spirit Island's tension, where you plan for coming problems and the next card disrupts the plan.
- **Direct:** the event is drawn and shown before the vote, so the choice is informed.

---

## The Wall of Leaders

- One slot per event card in the event deck. **Default: 12 slots.**
- At Time passes, the Dusk leader moves into the next empty slot, together with **its paired event and any Breakthrough credited to its reign.**
- The Wall is the game clock. When the Wall is full, the event deck is empty, and the next Dawn draw loses the game.
- Breakthroughs on the Wall stay active for the rest of the game.
- The Wall as an additional power-curve source is parked.

---

## Event deck (threat cards)

**Principles** (all five adopted from Spirit Island):
1. Event cards say only **where** (a section type). The slot decides **what** happens.
2. Damage is simple counting.
3. One loss clock that cascades (Decay).
4. The Crew fight back.
5. Escalation comes from deck stages, not new rules.

**Composition (default: Spirit Island's 3/4/5):**

| Stage | Count | Content |
|---|---|---|
| I | 3 | Names one section type |
| II | 4 | Names one section type, plus a twist line (see `data/README.md`). The pool also holds one **Outer Hull** card, matching every Hull section. One dealt Stage II card carries an **Escalation** symbol. |
| III | 5 | Names two section types |

- Section types are **Infrastructure, Residential, Government, Agricultural**.
- Build a pool with **one card per section type at each stage** (Stage III uses pairs of types). Shuffle each stage separately, deal the needed counts, and stack them I on top, III at the bottom.
- **Escalation symbol:** when the escalation card resolves its seed, apply the destination's Escalation effect, if the destination defines one. Otherwise ignore it.
- **Landfall event** *(toggle only)*: set aside at setup. It matches **every** section.

**Slot actions** (Spirit Island resolution order: Dusk, then Day, then Dawn):
- **Seed (Dawn):** add 1 Glitch to each matching section that is on the **Outer Hull** or **adjacent to a section with a Fault or Failure**.
- **Grow (Day):** in each matching section that has at least one threat piece, add 1 Fault. If that section already has 2 or more Faults, add 1 Failure instead.
- **Collapse (Dusk):**
  1. Each matching section with threat pieces takes damage equal to the **total damage of its threat pieces**.
  2. If a section takes **2 or more damage**, add 1 Decay.
  3. The same total damage is **also** dealt to the Crew there (not split between section and Crew). Players assign it, at 2 health per Crew.
  4. **Each surviving Crew in a collapsed section then deals 2 damage** (repair) to threat pieces there. Players assign it.

---

## Threat pieces

| Piece | Spirit Island equivalent | Health | Damage | Purpose when destroyed |
|---|---|---|---|---|
| Glitch | Explorer | 1 | 1 | 0 |
| Fault | Town | 2 | 2 | 1 |
| Failure | City | 3 | 3 | 2 |

- Damage on threat pieces clears at Time passes.
- Powers can **repair** (deal damage), **downgrade** (Failure → Fault → Glitch), **vent** (push a piece to an adjacent section; this moves the problem rather than removing it, so it earns no Purpose), and **prevent** (stop a section's Day grow).

---

## Crew

- Spirit Island's Dahan equivalent.
- **Health 2. Each Crew deals 2 damage** (repair) when fighting back after a collapse.
- **No natural births.** Crew are added only by powers.
- Powers can **move, gather, add, shelter** (protect) and **rally** Crew.
- Damage on Crew clears at Time passes.
- Losing Crew does not lose the game. A destination may require a Crew count for Landfall.
- Loyal/Restless crew states: **rejected.**

---

## Decay and Ship in Crisis

- Spirit Island's Blight equivalent.
- **Decay pool:** **4 per player + 1** *(tuned by simulation; was 2 per player + 1)*.
- **When Decay is placed:**
  - each house loses **1 influence** in that section, and
  - if the section **already had Decay**, **cascade**: place 1 more Decay in an adjacent section of the players' choice.
- Cascades can chain.
- A section with a **Quarantine** token cannot receive a cascade.
- **Ship in Crisis card:** Spirit Island's Blighted Island equivalent.
  - The first time the Decay pool is empty, flip the card.
  - Add **1 Decay per player** to the pool *(default)*, and apply the card's ongoing crisis effect.
  - If the pool empties again, the players lose.
  - The crisis effect content is not designed yet.

---

## Purpose, Discoveries and Understanding

Spirit Island's Fear equivalent. *Narrative:* the crew's Purpose drives them to relearn how their own ship works.

**Purpose pool:** **4 per player** *(tuned by simulation for the heavier starting setup)*. Gain Purpose from:
- **destroying a Fault: 1**,
- **destroying a Failure: 2**,
- cards that grant it.

When the pool fills, earn 1 **Discovery** card face-down and reset the pool.

**Discovery cards** resolve at the **start of Dusk**. Each card offers a choice:
- **Apply:** use its one-time effect at the current Understanding tier (I / II / III), then discard it.
- **Breakthrough:** tuck it under the **current Steward** as a weaker **permanent** ongoing effect. It travels with that leader to the Wall and stays active.
  - **Maximum one Breakthrough per leader.** If the Steward already holds one, the Discovery must be applied.
- *Example: "Fault Mapping."*
  - I: remove 1 Glitch from each Outer Hull section.
  - II: skip the Day grow in one section type.
  - III: downgrade every Fault in one section type to a Glitch.

**Understanding tiers** *(default: 3 Discoveries per tier, as in Spirit Island)*:

| Tier | Example name | Reached at | Base win condition |
|---|---|---|---|
| I | Superstition | Start | No threat pieces **and no Decay** on the ship |
| II | Understanding | 3 Discoveries earned | No threat pieces |
| III | Mastery | 6 Discoveries earned | No Faults or Failures |

*Pacing target:* an average table should win at about Understanding III. The conditions above are one step stricter than Spirit Island's pattern. With the original conditions (I: no threat; II: no Faults/Failures; III: no Failures), tier II was barely harder than III, so simulated games were won at tier II by generation 5–7. The original set is kept in config as `tierConditions: "classic"`.

The destination's Landfall requirement is added on top of the tier condition.

---

## Ship map

**Boards:**
- One board per player, connected edge to edge.
- Each board's setup symbols define its starting pieces. Each board sets the starting sections for its player's house.
- **Default board:** 8 sections, 2 of each section type, 3 on the Outer Hull. Adjacency is hand-authored.

**Section types:** Infrastructure, Residential, Government, Agricultural.

**Meta-regions:** **Outer Hull** (Spirit Island's coastal equivalent; seeding enters from the void) and **Core** (inland).

**Conduits:** the adjacency connections between sections.

**Setup symbols per board** (as in Spirit Island, threat starts on the board):
- **1 Failure, 2 Faults and 1 Glitch, each in a different section type**, so every type starts with some threat at a different strength. Which type gets the Failure rotates between boards (A: Infrastructure, B: Residential, C: Government, D: Agricultural).
- 1 Decay next to the Failure,
- 6 Crew (2, 2, 1, 1) across 4 sections away from the Failure and the Decay,
- 2 influence for the board's house in the marked start sections.

Starting Decay does not come from the pool, as in Spirit Island.

---

## Influence and Havens

- **Influence:** Spirit Island's presence equivalent. Houses add and move it through growth and powers.
- **Range:** cards target **0–3** sections from a section where the house has influence. Each card defines its range and its target type (a section type, Hull/Core, or **ANY**).
- **Haven:** a section where a house has **2 or more influence** (Spirit Island's sacred site equivalent). *"Haven" is a proposed name; "Stronghold" was rejected as too militaristic.* Effects are defined on cards (e.g. "range from a Haven").
- **A house with zero influence on the ship loses the game for everyone.**

---

## People cards (one shared deck)

All houses draw from **one shared people deck** with two tiers. There is no deck scaling by player count. When a pile is empty, it is reshuffled from its own discard pile.

| Tier | Credit cost | Notes |
|---|---|---|
| **Common** | 0–3 | Standard draws |
| **Remarkable** | 0–8 | Take 1 Remarkable **instead of 2 Common draws**. Stronger effects, **harsher Legacy**. |

**Card anatomy:**
- name,
- tier,
- **credit cost**,
- **guild elements** (2–4 icons, **average 3**),
- **range** (0–3) and **target** (section type / Hull / Core / ANY / another house),
- **effect**,
- **Reign** text,
- **Legacy** text.

There is **no printed speed**: the nominee is fast and every other play is slow.

**Cooperative powers:** some cards target another house. They can give credits, move or add that house's influence, or extend its range.

**Effect verbs available to cards:**
- **Threat:** repair (deal damage), downgrade, vent (push), prevent grow.
- **Crew:** add, move, gather, shelter, rally.
- **Decay:** restore (remove Decay).
- **Tokens:** place any token.
- **Influence:** add, move.
- **Purpose:** gain.
- **Time:** foresee (look at the top of the event deck), temper a Legacy, boost a Reign.

**Hand rules:**
- **Hand size = card plays + 2.** Houses may modify the +2 (e.g. Meridian: +3). Cloned cards are kept on top of this.
- **Card plays:** set by the house's card-play track (base 2). The nominee counts as one of the plays *(default)*.
- **Clone slot:** keep **1** card into the next generation (base). Houses may raise or lower this.
- At Time passes, all other cards in hand go to the discard pile.

**Credits** (Spirit Island's energy):
- Credit gain per generation is set by the house's credit track. Houses start with 0 credits *(default)*.
- Credits carry over between generations.

**No card gain and no deck thinning:** Spirit Island's "gain a power" is replaced by house power-growth unlocks.

---

## Elements (guilds)

Eight guild elements:
- Engineers
- Farmers
- Medics
- Bureaucrats
- Navigators
- Scholars
- Laborers
- Keepers

**How guilds relate to the rest of the game:**
- Guilds have obvious targeting tendencies (e.g. Farmer cards usually target Agricultural sections), but are not bound to section types.
- **Elements come only from cards a house plays this generation and from raw elements on its growth track.**
- **Innate powers** on the house board unlock at guild thresholds.
- If the power curve proves too weak, the next step is to let the **current Steward's elements count for every house**.

**Making thresholds reachable.** In Spirit Island, each spirit's own starting cards carry its elements. Our shared deck doesn't, so houses use any mix of these levers:
- **Cards carry 2–4 guild icons, averaging 3**, so element density is high across the deck.
- **Raw elements on house tracks** (a bigger share of identity than in Spirit Island).
- **Guild substitution** as a house rule (e.g. "count Laborers as Engineers").
- **Cloning** an element-rich card into the next generation.

---

## Houses (player factions)

Asymmetry lives **entirely on the house boards**. There are no unique house cards until that becomes a needed gap.

**Design principle:** houses bend and break core rules to express their identity (e.g. Galvan resolves extra cards fast).

**Houses are built from the *Balance framework* below**, and each house lives in its own file next to this document, in `houses/`. Every part of a house lists its Power Point value.

**Each house board has:**
- **Growth options.** Pick one per generation.
- **Influence tracks.** Placing influence uncovers unlocks, as on Spirit Island's presence tracks. Possible unlocks:
  - **+1 card play** (unlocks are asymmetric per house),
  - **+1 hand size**,
  - **+1 fast candidate** (an extra nominee),
  - **+1 clone slot**,
  - **−1 credit cost** on plays,
  - **+credit gain**,
  - **raw guild elements**,
  - **move influence**.
- **Innate powers** with guild-element thresholds.
- **Special rules.**
- **Two tracks only:** a credit track and a card-play track. Special slots on either track grant an element, a fast play or a clone slot.

**Houses** (Spirit Island template in brackets): see `houses/README.md`. The first four are modeled on the low-complexity base spirits, the second four on the moderate- and high-complexity base spirits.
- **Galvan, the Spark-Wardens** [Lightning's Swift Strike]: fast and aggressive.
- **Meridian, the Flowkeepers** [River Surges in Sunlight]: movement and logistics.
- **Keel, the Hullwrights** [Vital Strength of the Earth]: slow and defensive.
- **Vigil, the Lamplighters** [Shadows Flicker Like Flame]: Purpose and reach.
- **Foremen, the Shift-Callers** [Thunderspeaker]: Crew-led offense. *Crew Captains:* Crew in their sections deal +1 damage when fighting back.
- **Gardeners, the Greenkeepers** [A Spread of Rampant Green]: influence as armor. *Rooted:* Decay that would land on them removes 1 of their influence instead. Growth A places 2 influence.
- **Voidwardens, the Airlock Keepers** [Ocean's Hungry Grasp]: Outer Hull specialists. *Airlock:* threat they vent out of a Hull section is destroyed (+1 credit per Fault/Failure). They can only add influence to Hull sections.
- **Tellers, the Keepers of the Story** [Bringer of Dreams and Nightmares]: *Spin:* their damage never destroys threat; it becomes 1 Purpose per point.

---

## Balance framework (Power Points)

Houses, cards and innates are built from priced parts so every house lands in the same power range, with a curve shape that matches its identity. **All prices are starting values to be calibrated by Monte Carlo playtesting in the prototype.**

**Unit:** **1 PP = 1 damage to threat at range 1, slow.** **1 credit = 1 PP.**

**Effect prices:**

| Effect | PP |
|---|---|
| Damage X | X |
| Downgrade 1 piece | 1.5 |
| Vent a Glitch / Fault / Failure | 0.5 / 1 / 1.5 |
| Patch (prevent the next grow) | 1.5 |
| Lockout (prevent the next seed) | 1 |
| Isolate (a piece deals no damage) | 1 per 2 damage negated |
| Brace X | 0.5 × X |
| Quarantine | 1 |
| Gather or move 1 Crew | 0.5 |
| Add 1 Crew | 3 |
| Restore 1 Decay | 3 |
| Add 1 influence | 2 |
| Move 1 influence | 1 |
| +1 Purpose | 1 |
| +1 credit | 1 |
| Foresee | 0.5 |
| Temper the Elder's Legacy | 3 |

**Modifiers** (multiplied together):

| Modifier | Values |
|---|---|
| Range | 0: ×0.8 · 1: ×1.0 · 2: ×1.15 · 3: ×1.3 |
| Target | ANY ×1.0 · one section type ×0.85 · narrow condition (e.g. Hull only) ×0.75 |
| Speed | Slow ×1.0 · Fast ×1.25 |
| Ongoing | Per-generation value × expected generations active |
| Chance-based | Value × probability it triggers |

**Card pricing:**
- **Common:** Card Value = **2 + cost** (cost 0–3).
- **Remarkable:** Card Value = **2 + 1.5 × cost** (cost 0–8).
- The **2** is the value of a card play itself.
- **Leader panel:** Common Reign − Legacy ≈ **+1 PP**; Remarkable ≈ **+2 PP**, with larger values on both sides.

**Element costs** (for pricing innate thresholds):

| Element | PP each |
|---|---|
| House's primary guild | 1 |
| House's secondary guild | 1.5 |
| Any other guild | 2 |
| Covered by raw track elements | 0 |

**Innate rule:** innate tiers are cumulative. The **cumulative effect PP of a tier should equal its threshold cost**, within −10% / **+20% for the top tier** (rewarding specialization).

**House parts:**

| Part | PP |
|---|---|
| +1 credit per generation | 1 per generation |
| +1 card play per generation | 2 per generation (also +1 hand size) |
| Raw element per generation | That element's cost per generation |
| +1 fast play | 1 per generation |
| +1 clone slot | 1 per generation |
| Starting influence | 2 each, +1 if it forms a Haven |
| Growth option | Its PP per use; a house's options within ±1 PP of each other |
| Special rule | Expected PP per generation |

**Generation value** = 2 × cards played + credits spent + innate tiers met + special rule + growth choice. Credits beyond 3 × card plays can only be spent on Remarkables, at 1.5 PP per credit.

**Reference pacing** (until simulation replaces it): a house uncovers one track slot in each of generations 1–4, then in generations 6, 8, 10 and 12, alternating tracks and starting with credits.

**Targets:**
- **Total value** over 12 generations: every house within **±5%** of the average.
- **Curve shape** = late power (gens 9–12) ÷ early power (gens 1–4):

| Shape | Late ÷ early |
|---|---|
| Front-loaded | < 1.5 |
| Standard | 1.5–2.0 |
| Steep | > 2.0 |

**Card thresholds:** a card's element-threshold bonus is worth **1 PP per required element**. Commons require 2–3 elements, Remarkables 3–6. The threshold is drawn from the card's own guilds.

**Reign and Legacy pricing:** effects that act per section are priced at **2 reference sections**, and per-house effects at **2 houses**. Legacy effects use the effect prices with the sign reversed; Add Decay costs 4 (because of cascade risk).

**Discovery pricing:** one-time effects are worth **4 / 6 / 8 PP** at Understanding I / II / III. A Breakthrough is worth about **1 PP per generation**.

**The people deck** (400 cards: 300 Common, 100 Remarkable) is generated from these rules by `tools/generate_people.py` into `data/`. Events, 24 Discoveries and 4 Ship in Crisis cards come from `tools/generate_decks.py`. Four ship boards and the four houses are hand-authored in `data/`. See `data/README.md`.

**Power summary:** a house's PP summed by category (**Repair, Control, Protection, Purpose, Utility**) generates its identity bars, as on Spirit Island's spirit panels.

---

## Tokens

| Token | Spirit Island equivalent | Effect |
|---|---|---|
| **Brace** | Defend | Prevent X damage in this section this generation. X is set by the card. |
| **Quarantine** | Isolate (section) | The section is cut off: no seed, vent or cascade into or out of it this generation. |
| **Patch** | Disease | The next **grow** in this section is skipped. Then remove one Patch. |
| **Lockout** | Wilds | The next **seed** in this section is skipped. Then remove one Lockout. |
| **Unrest** | Badlands | Every source of damage in this section deals +1 damage, from both threat (collapse) and players. |
| **Isolate** | Strife (on a threat piece) | This threat piece deals no damage at its next collapse. Then remove Isolate. |

Brace and Quarantine clear at Time passes. Patch, Lockout and Isolate are removed when used. Unrest persists *(defaults follow Spirit Island)*.

---

## Destinations (adversary equivalent)

Chosen before the game, with a difficulty **level 0–6**. Each destination defines:
- **Landfall requirement:** an extra win condition added to every Understanding tier, or a change to the standard one. Examples: "Crew ≥ 10", "no Decay in Infrastructure".
- **Journey hazard:** an always-on rule from level 1.
- **Escalation:** the effect triggered by the Stage II escalation card. If undefined, the escalation symbol is ignored.
- **Levels 1–6:** a mix of setup changes (extra Faults, Decay or Failures), harsher or added rules, event deck changes (more Stage III cards, **fewer total events, which shortens the clock and the Wall**), and a stricter Landfall requirement.

**Levels are cumulative**: a level-N game applies every level from 1 to N. Level 0 means no destination rules (the base game). Full text is in `data/destinations.json`.

**The Verdant Reach** (a garden world; needs living colonists):

| Level | Adds |
|---|---|
| 1 | Landfall requirement: ≥ 3 Crew per player. *Spore Drift:* when Grow adds a Fault in an Agricultural section, also add 1 Glitch to its least-threatened neighbor. |
| 2 | Setup: +1 Fault in one Agricultural section per board. |
| 3 | Escalation: +1 Glitch in every Agricultural section. |
| 4 | Requirement rises to ≥ 4 Crew per player. |
| 5 | *Blight Season:* Collapse in Agricultural sections destroys 1 extra Crew. |
| 6 | Deck: one Stage I card becomes an extra Stage III card. |

**Cinder** (scorched by solar flares; the hull takes the brunt):

| Level | Adds |
|---|---|
| 1 | Landfall requirement: no Decay in Infrastructure. *Flare:* seeded Outer Hull sections gain 1 extra Glitch. |
| 2 | Setup: +1 Glitch in every Outer Hull section. |
| 3 | Escalation: +1 Unrest in every Outer Hull section with threat. |
| 4 | Setup: +1 Decay in one Outer Hull section per board (not from the pool). |
| 5 | *Radiation:* Collapse in Outer Hull sections deals +1 damage. |
| 6 | Deck: one fewer Stage I card. |

**The Long Dark** (a rogue planet; belief wears thin):

| Level | Adds |
|---|---|
| 1 | Landfall requirement: Understanding III. *The Cold:* lose 1 Purpose at the start of each Day. Deck: +1 Stage II card. |
| 2 | Setup: +1 Fault in one Government section per board. |
| 3 | Escalation: lose 3 Purpose. |
| 4 | The Cold drains 2 Purpose per Day. |
| 5 | Setup: +1 Failure in one Residential section on board A. |
| 6 | Deck: one fewer Stage I card. |

**Landfall card variant (toggle):** when the win condition and the Landfall requirement are met (and at least 2 events remain), the Landfall event becomes the next Dawn event. It seeds, grows and collapses in every section. The players win when it retires to the Wall.

---

## Player-count scaling

| Players | Ship boards | Decay pool | Purpose pool | Event deck / Wall |
|---|---|---|---|---|
| 1 | 1 | 5 | 4 | 12 |
| 2 | 2 | 9 | 8 | 12 |
| 3 | 3 | 13 | 12 | 12 |
| 4 | 4 | 17 | 16 | 12 |

The people deck does not scale. Solo-specific tuning is deferred until multiplayer is settled; solo players can play two-handed.

---

## Design decisions and rationale

| Decision | Reason |
|---|---|
| Dawn / Day / Dusk instead of Past / Present / Future | Generations aging through a conveyor fit Spirit Island's structure. "Past = next generation" was confusing. |
| Defend the ship as the Great Houses | Gives freedom to design houses the way Spirit Island designs spirits. |
| Generation ship setting | A confined board, plenty of disasters, and a shared goal of human survival. |
| Forgotten Machine tone | More design space than strict realism, while staying understandable. |
| Fully cooperative | Matches Spirit Island. |
| One clock: every round is a generation | A second, slower leadership timer was rejected. |
| Heirs are a second use of people cards | Avoids adding a separate system. |
| Nominee is the only fast card | Removes printed speed. The card you need most urgently is the one at risk of being taken as leader. |
| Offset event pairing by default, Direct as a toggle | Keeps Spirit Island's "the next card disrupts your plans" tension. |
| One event drawn after the vote (not one per candidate) | Simpler, and you see the problems the leader faces after choosing. |
| Dusk = Legacy + collapse, Day = grow | Puts damage and the leader's downside together in the same sections. |
| Threat ladder (Glitch/Fault/Failure) over a single Strain dial | Chosen for tactical richness, close to Spirit Island. |
| A single threat track (no separate people/unrest track) | Avoids doubling the system. |
| One shared people deck, a fresh hand each generation | Fits "a new set of people every generation" better than a deckbuilder. Removes reclaim and thinning. |
| Clone slot | Gives limited planning and control over random draws. |
| Remarkable: draw substitution + higher cost + harsher Legacy | Replaces Spirit Island's "forget a card" trade-off. |
| Guilds as elements, not tied to section types | Raw elements come from the growth track instead. |
| Purpose → Discoveries → Understanding tiers | Keeps Spirit Island's fear structure. "Mission Forgotten" loss was dropped. |
| Discovery choice: one-time effect or a Breakthrough | Breakthroughs give the power curve, a history on the Wall, and a cap of one per leader. |
| Event deck size = Wall slots; empty deck = loss | Like Spirit Island's invader deck clock, but visible. |
| Destinations as adversaries | Flavor comes from the journey. Levels change setup, rules, deck and the Landfall target. |
| Fixed-length game and a mid-game "choose to land" decision | Rejected. The Landfall card toggle is the alternative climax. |
| Loss: Decay pool, or a house with no influence | Matches Spirit Island. Crew loss is not a loss condition. |
| Win conditions shifted one step stricter; Purpose 4 per player; Decay 4 per player + 1 | Simulation tuning so an average table wins at about Understanding III, around generation 8–9. |
| Keel starts at 2 card plays | With 1 play and a free nominee, Keel never spent credits. |
| Boards start with threat in every section type (1 Failure, 2 Faults, 1 Glitch) | Like Spirit Island's starting towns and cities; every type is under some pressure from the first generation, at different strengths. |
| No house perk for the chosen heir | It's a joint decision with built-in gains. Kept as a later option. |
| No score, no scenarios, no Loyal/Restless crew | Out of scope for now (Loyal/Restless is rejected outright). |
| Hand size = card plays + 2 | A fixed hand made extra plays useless; deriving it keeps both values meaningful. |
| Vent = push, earns no Purpose | Moving a problem is not solving it. |
| Power Point framework for houses and cards | Houses are assembled from priced parts so power levels can be compared and tuned; curve shape expresses identity. |
| Cards average 3 guild icons | The shared deck doesn't supply each house's elements the way Spirit Island's unique powers do. |
| Unrest affects both sides | Otherwise no player power would want to place it. |
| Easy Spirit Island spirits as house templates | Each house keeps its template's identity and curve shape. |

---

## UI

- **Top bar:**
  - generation number,
  - current phase and step,
  - event deck count (= remaining Wall slots),
  - Decay pool (healthy or crisis side),
  - Purpose pool fill,
  - Understanding tier and the current win condition (tier + Landfall requirement),
  - destination and level.
- **Left panel: the conveyor.** Three stacked slots (Dusk, Day, Dawn). Each shows the leader card (Reign/Legacy highlighted for its slot) and its paired event (section types plus the slot's action). It also holds the earned Discovery cards awaiting resolution.
- **Center: the ship map.**
  - Sections are colored by type and Hull sections are edge-marked; conduits are drawn as lines.
  - Each section shows its threat pieces, Crew, Decay, influence per house, tokens and current damage.
  - Legal targets highlight while a card resolves.
- **Right panel: house panels**, one per house:
  - hand, clone slot, credits,
  - card-play limit and plays used,
  - current elements,
  - influence tracks with uncovered unlocks,
  - innate powers with threshold status.
- **Bottom: the Wall of Leaders.** A row of slots, each holding its leader, event and Breakthrough once filled. Empty slots show the remaining clock.
- **Vote panel** (during Dawn): nominee cards side by side showing Reign/Legacy. In Direct mode it also shows the upcoming event.
- **Discovery choice modal** (at the start of Dusk): the tiered effect versus the Breakthrough text, with "Apply" and "Breakthrough" buttons. "Breakthrough" is disabled if the Steward already has one.
- **Log panel** (collapsible): a step-by-step record of every placement, damage and choice.
- **Settings panel** (pre-game): player count, houses, destination and level, rule toggles, and numeric overrides from the config file.
- **End screen:** win or loss, the cause, and the Wall shown as the voyage's history.

---

## Audio

Procedural Web Audio tones for key events:
- phase changes,
- seed / grow / collapse (low, heavy for collapses),
- Decay placed or cascading,
- Discovery earned,
- succession chosen,
- win and loss stingers.

A mute toggle is included.

---

## Vertical slice / first implementation target

*Status:* built. The browser prototype (`index.html`, `src/ui/`) runs the full game, including all eight houses, 1–4 players, destinations, the Landfall card and human or bot seats. See `README.md` to run it. The list below is the original target, kept for reference.

- **2 players, 2 ship boards** (8 sections each, hand-authored adjacency, default setup symbols).
- **Houses:** Galvan and Keel from `houses/` (the front-loaded and steep extremes).
- **House calculator:** reads house data and reports total PP, curve shape and power summary.
- The **full round loop**: Growth, Commit, Fast, Dusk, Day, Dawn vote, Slow, Time passes.
- **Leader conveyor** with Offset/Direct toggle, nomination, vote with tie-break, and the Wall with 12 slots.
- **Event deck** with 3/4/5 stages, seed/grow/collapse, Spirit Island resolution order, and the escalation symbol (ignored at level 0).
- **Threat ladder, Crew fight-back, Decay with cascade and influence loss, and the Ship in Crisis flip** (placeholder crisis effect: none).
- **Purpose pool, Discovery choice and Breakthroughs, Understanding tiers and their win conditions.**
- **People deck:** the generated 400-card deck in `data/people.json`.
- **Discovery deck:** about 9 placeholder cards with I/II/III effects and a Breakthrough line.
- **Tokens:** Brace, Quarantine, Patch, Lockout, Unrest, Isolate.
- **All three loss checks and the base win check.** The Landfall card toggle comes second.
- **Config file** exposing every default listed in this document.
- **Undo** to the previous phase.
- **Out of scope for the slice:** destinations beyond level 0, 3–4 player boards, Meridian and Vigil, art and audio polish. **Monte Carlo auto-play** to calibrate prices is the next target after the slice.

---

## Open questions and missing items

**Defaults chosen for the prototype (not decided in conversation):**
- tech stack,
- visual style,
- the Wall / event deck size (12) and stage split (3/4/5),
- the crisis flip refill (1 per player), and Discoveries per tier (3),
- starting credits (0),
- whether the nominee counts as a play,
- starting credits (1) and base credit gain (1),
- board size (8 sections),
- token durations,
- the tie-break when there is no Steward.

**Remarkable access:** whether drawing a Remarkable by substitution is always available or gated by a house unlock was not decided.

**Not yet designed:**
- house special-rule and innate values beyond first estimates (see `houses/README.md`),
- destination levels,
- Haven effects beyond targeting.

**Small gaps:**
- the Outer Hull event card in the Stage II pool, and the four Stage II twists, are first versions,
- whether elements from the Steward should count for everyone (deferred until the power curve is tested).

**Simulation:** a rules engine, layered bots and a Monte Carlo runner live in `src/` and `sim/` (see `sim/README.md`). First findings are in `sim/RESULTS.md`: run 1 found Keel too weak (fixed: 2 starting plays) and games won too early (fixed: shifted tier conditions). Run 3 adds Spirit Island–style starting threat in every section type, with Purpose 4 and Decay 4 per player + 1: about 64% wins at generation ~8.3, about 94% of them at Understanding III. Innate tiers II–III are still rarely reached. The engine's interpretations of unclear rules are listed in `sim/README.md`.

**Calibration:** every PP price, element cost and the reference pacing are first guesses, to be replaced by Monte Carlo results. Purpose at 1 PP is a specific suspect (Vigil reaches 5 Purpose per generation).

**Parked ideas:**
- the Wall as a further power source,
- a perk for the house whose heir is chosen,
- unique house cards,
- a dummy candidate deck for low player counts,
- solo tuning,
- scenarios,
- "learning from failure" (Purpose from Decay) as a possible house trait,
- a game name.
