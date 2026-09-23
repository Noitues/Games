# Scene-Deck Engine for Fate — Playtest Rules Spec

As of Sep 23, 2026 — version 0.2.0 (see CHANGELOG.md)

## 1. Overview

The Scene-Deck Engine is a Fate supplement that makes player backstories supply the specifics of the GM's plot. The GM decides *what happens* (an ambush, a betrayal, a flood). A card drawn from a shared deck decides *who, where and why*, often from a player's own history.

**Design goals**

- Every player's backstory surfaces in play at least once per session, without the GM planning it.
- The GM keeps control of pacing and the macro plot through prepared Beat Frames and faction clocks.
- GM prep for a session takes 15 minutes or less and consists of choosing cards, not writing scripts.
- All rules use Fate's existing economy (aspects, invokes, compels, fate points). No second dice system.

**What each source contributes**

| Source | What this supplement takes from it |
| --- | --- |
| Fate Core | 4dF, the ladder, aspects, invokes, compels, stress and consequences, concessions |
| Legend in the Mist | Theme cards with power tags and a weakness; a two-category card split (here ROOTS/REACH); card evolution driven by trouble (here Growth) |
| Mythic GME | A tension track and scene test that inject unplanned twists; answering plot questions by random draw; the Characters and Threads lists, rebuilt as Story Pile cards drawn on Fate triggers (§6A) |

**Rules baseline:** Fate Core skills for rolls.

## 2. Components and card anatomy

Every card is a paper insert in a clear tarot sleeve (70 × 120 mm) with a header, a title, three power tags, one weakness tag and a track.

**Header fields**

- **Owner:** `GLOBAL` (persists across scenes), `GM`, or a player code such as `PC-SILAS`.
- **Type:** one of the ten types in the table below. No other types exist.
- **ID code:** a prefix plus number (`SV-03`, `T-12`). Mutated cards add a version suffix (`T-03v2`). IDs never get reused, even after a card is retired.

**Card types**

| Type | Owner | Track holds | Fills in Beat Frames (§5) |
| --- | --- | --- | --- |
| ROOTS | Player | Growth (3) | WHO |
| REACH | Player | Growth (3) | WHY |
| THREAT | GM | Clock (4–6) | HOW |
| FACTION | GM | Clock (4–6) | WHO |
| HAZARD | GM or GLOBAL | Clock (4–8) | HOW |
| LOCATION | GM | Clock (4) | WHERE |
| CULTURE | GM | None | WHY |
| NPC | Player or GM Story Pile (§6A) | Weight (1–3) | WHO |
| THREAD | Player or GM Story Pile (§6A) | Weight (1–3) | WHY |
| BEAT | GM only, never in the deck | None | Holds the frame itself |

ROOTS replaces the draft's ANCHOR type and REACH replaces IDENTITY. A ROOTS card is an origin, a person, a place or a comfort. A REACH card is an oath, a burden, a power or a goal.

**Player binder:** exactly 4 theme cards, 2 ROOTS and 2 REACH. Each has 3 power tags and 1 weakness tag.

**Tag writing rules**

- A power tag is 2–5 words and names one thing the character can do, has or is.
- A weakness tag must be something that can plausibly cause trouble in a scene. "Paralyzing Guilt" qualifies. "Sometimes Tired" does not.
- At least one ROOTS tag per character must name a specific person, group or place. The Beat Frame engine needs these as raw material.

**Other components:** 4dF per player, fate point tokens, one tension track (1–6), the GM's library box with dividers, and the Chronicle Scrapbook.

## 3. Core resolution

Rolls are standard Fate: 4dF + skill against opposition on the ladder, with card tags acting as aspects.

**Which tags are live**

- A player's tags are live if the card is in their binder and not Strained (§8).
- A player card sitting in the Session Deck is not live. Its owner cannot invoke it until it surfaces (§4).
- Every face-up card on the rail is a situation aspect. Anyone can invoke its tags if the fiction supports it.

**Invokes**

1. Name a live tag that fits the action and spend 1 fate point or 1 free invoke.
2. Gain +2 to the roll, or reroll all four dice.
3. Each tag can be invoked at most once per roll. There is no free per-tag bonus; every tag costs an invoke.

**Fate points**

- Players start each session at refresh 3, or their current total if higher.
- The GM gets 1 fate point per player at the start of each scene. Unspent GM points do not carry over.
- Invoking a player's weakness tag against them is a hostile invoke. The target gains 1 fate point at the end of the scene.

**Opposition (passive)**

Passive opposition starts at Average (+1). Add +1 for each face-up GM or GLOBAL tag that directly opposes the action, to a maximum of Great (+4). A tag used to raise the difficulty cannot also be invoked by the GM on that roll. Named NPCs roll 4dF + their rating as active opposition, as in Fate.

**Free invokes from cards**

- A GM card placed face-up on the rail gives the GM 1 free invoke on its tags. It must be used within that scene.
- A player card that surfaces from the Session Deck gives its owner 1 free invoke on its power tags (§4).

**Outcomes and deck draws**

| Result | Outcome | Deck draw |
| --- | --- | --- |
| Shifts < 0 | Fail, or the player may choose success at a major cost | Only if they chose success at a major cost: GM draws 1 card; the major cost must use its weakness tag or a GM threat tag |
| 0 | Tie: success at a minor cost | GM draws 1 card; the minor cost must use one of its tags |
| 1–2 | Success | None |
| 3+ | Success with style | The player may look at the top card of the Session Deck and leave it or move it to the bottom, instead of taking a boost |

The GM must build the cost from the drawn card. That constraint is the point of the system; it stops costs from being invented freely.

This rule covers only the deck-draw costs in the table above. The rest of Fate runs as normal: complications that come from the fiction, compels, and temporary situation and character aspects are still made up at the table. If a player throws their weapon and the enemy falls off the cliff with it, the GM can simply give them *Weapon Lost Over the Cliff* for the scene. Whether that aspect outlives the session is the player's choice (Keep, §6A).

## 4. The Session Deck

The Session Deck holds 3 GM environment cards plus 1 card from each player, so a 4-player table has 7 cards.

**Building the deck (at session start)**

1. The GM sets out 3 environment cards chosen during prep (§7).
2. Each player shuffles their 4 binder cards and draws 1 at random, then hands it face-down to the GM.
3. The GM shuffles all cards together and places the deck face-down beside the rail.

**When the GM draws**

- A roll ends in a tie (§3).
- A player chooses success at a major cost (§3).
- The scene test calls for an interrupt (§6).
- A Beat Frame is triggered (§5).

No other event causes a Session Deck draw. The GM cannot draw at will. Story Pile draws have their own Fate triggers (§6A).

**Resolving a drawn player card**

1. The GM reveals the card, whoever's turn it is.
2. The GM offers its owner a compel. The compel uses the card's weakness tag by default. It may use a power tag only if that tag causes the trouble directly, such as "Knows Hidden Cellars" leading the party somewhere dangerous.
3. If the owner accepts, they gain 1 fate point and the complication happens as described.
4. If the owner refuses, they pay 1 fate point. The GM builds the cost from a face-up GM tag instead.
5. Either way, the card surfaces: it goes face-up on the rail, becomes live again, and its owner gains 1 free invoke on its power tags.

**Resolving a drawn GM card**

The card goes face-up on the rail. The GM gains 1 free invoke on it and builds the cost or twist from its tags.

**Cleanup at scene end**

- Surfaced player cards return to their owner's binder and stay live.
- GM cards drawn from the deck go to the Session Discard pile unless the GM keeps them on the rail for the next scene.
- Unused free invokes expire.

**When the deck runs out**

The scene after the last card is drawn is the session's climax. During the climax, ties and costs use face-up GM tags instead of draws.

**Backstory guarantee:** every player's card surfaces at least once per session. The GM pulls a player's card out of the deck, unsurfaced, at the first of these moments:

- **The deck is down to 2 cards.** The pulled card opens the next scene in a Beat Frame. That Beat Frame is triggered by this rule, overriding the §7 rule that frames are never forced; it replaces that scene's scene test.
- **The session's final scene begins.** Every player card still in the deck is pulled and opens that scene in a Beat Frame, as above.
- **The deck reaches 2 cards during the final scene.** The pulled card is revealed at once and resolved as in "Resolving a drawn player card".

Pulled cards fill the frame's open blanks before any draw. If more cards are pulled than the frame has open blanks, each extra card is revealed at the start of that scene and resolved as in "Resolving a drawn player card"; it can arrive as a memory, a messenger, news or an omen (§11).

## 5. Beat Frames (the adlib engine)

A Beat Frame is a plot event with blanks: the GM fixes what happens, and cards drawn from the Session Deck fill in the specifics.

**Anatomy of a BEAT card**

- **Name:** for example, AMBUSH.
- **Trigger:** a condition that can be checked, such as "the party travels a road" or "a clock fills" (§7).
- **Frame sentence:** "[WHO] attacks at [WHERE] using [HOW], because [WHY]."
- **Open blanks:** exactly 2 blanks marked with ◆. The deck fills these.
- **Defaults:** a prepared answer for every blank. These are used for fixed blanks and for any open blank the draw cannot fill.
- **Stakes:** what the party loses if the beat goes badly, written before play.

**Procedure**

1. The trigger fires. The GM reads the frame sentence aloud with the blanks shown.
2. Draw 1 card per open blank.
3. Each card fills the open blank matching its type (table in §2). If a card's type matches no open blank, it fills the first open blank still empty.
4. Player cards fill their blank from one of their tags, chosen by the GM. A ROOTS card becomes a specific person or place from that tag. A REACH card becomes the motive.
5. The card's owner answers one question from the GM about the filled blank, such as "What did you promise them?" Their answer is canon.
6. A player card used here surfaces and triggers a compel exactly as in §4.
7. Fill any remaining blanks with their defaults. Read the completed sentence, then frame the scene.

**Worked example**

Frame: AMBUSH — "◆WHO attacks at [the ford] using [hooked spears], because ◆WHY." The GM draws Silas's ROOTS card *The Lost Acolytes* and the GM's CULTURE card *Hide From Weather*.

- WHO: the acolytes Silas lost, now hive-touched and feral.
- WHY: they are desperate for shelter, and the party's camp is dry.
- Tom answers the GM's question: "I told them I'd come back for them." He accepts the compel on Vulnerable to the Rain and gains 1 fate point.

**Starter library (6 frames)**

| Frame | Sentence (◆ = open blank) |
| --- | --- |
| Ambush | ◆WHO attacks at [WHERE] using [HOW], because ◆WHY |
| Plea for Help | ◆WHO begs the party to go to ◆WHERE, because [WHY] |
| Betrayal | ◆WHO turns on the party, because ◆WHY |
| Rival Claim | [WHO] seizes the party's goal at ◆WHERE using ◆HOW |
| False Sanctuary | Shelter at ◆WHERE hides ◆HOW |
| Bad News | ◆WHO arrives with word that ◆WHY has happened |

## 6. Tension track (Mythic layer)

Tension runs from 1 to 6, starts the campaign at 3, and decides how often a planned scene gets twisted.

**Scene test (every scene except a session's first)**

1. The GM states the planned scene aloud.
2. Roll 1d6.
3. A result above Tension, or any 6, means the scene plays as planned.
4. An odd result at or below Tension means an **Altered scene**. The GM draws 1 card, and its tags change one element of the planned scene: who is there, the location, or the weather.
5. An even result at or below Tension means an **Interrupt**. The planned scene is set aside, and the GM triggers any prepared Beat Frame instead.

If the Session Deck is empty, Altered scenes use a face-up GM card, and Interrupts still trigger a Beat Frame using its defaults.

**Adjusting Tension at scene end**

| What happened in the scene | Change |
| --- | --- |
| The party fled, bypassed or ignored a face-up THREAT or FACTION | +1 |
| Any clock advanced during the scene | +1 (max +1 per scene from clocks) |
| The party resolved a THREAT or filled a player's goal | −1 |
| None of the above | 0 |

Tension never goes below 1 or above 6. It carries over between sessions; record it in the Chronicle.

## 6A. Story Piles (Mythic lists as cards)

Mythic's Characters and Threads lists become two kinds of story card kept in face-down Story Piles. A pile is drawn only on the Fate events below, never on a random-event roll.

**Story cards**

- NPC (Mythic Characters list): a named person or creature. 3 power tags for what they can do or want, 1 weakness tag.
- THREAD (Mythic Threads list): an open plot question, such as "Who poisoned the well?". 3 power tags for leads or leverage, 1 weakness tag for what pursuing it costs.
- Active THREAT and FACTION cards that are not face-up may also sit in the GM Story Pile, so threats come back the same way.
- Every story card has a Weight track of 1–3. It replaces Mythic's rule of listing an entry up to 3 times.

**The piles**

| Pile | Holds | Size limit |
| --- | --- | --- |
| Player Story Pile (one per player, beside the binder) | NPCs and threads tied to that character's own cards or goals | 5 cards |
| GM Story Pile | World NPCs and threads, plus active THREAT and FACTION cards | 12 cards |

- At character creation each player writes 2 story cards: 1 NPC from a ROOTS tag and 1 THREAD from a REACH tag.
- The GM starts the campaign with 3 NPC and 2 THREAD cards in the GM Story Pile. Piles persist between sessions and need no weekly prep.
- Weight: a card at Weight 2 or 3 gets 1 or 2 blank echo slips with its ID, shuffled into its pile. Drawing an echo means drawing that card.
- Story cards are not live and are not situation aspects while in a pile.

**Draw triggers (Fate events)**

| Fate event | Pile drawn | How the card is used |
| --- | --- | --- |
| A player accepts a compel that did not come from a deck draw | That player's pile | The complication must involve the drawn NPC or move the drawn thread; the GM gains 1 free invoke on it |
| A player concedes | That player's pile | The concession's narration must feature the card, such as who drags them clear or what they now owe; the player gains 1 free invoke on it |
| A player is taken out | GM Story Pile | The winner's terms must use one of the card's tags; the GM gains 1 free invoke on it |
| Success with style on create an advantage | That player's pile, optional | Instead of the boost or the Session Deck peek, an ally or lead from the pile appears; the player gains 1 free invoke on it |

Ties, costs, the scene test and Beat Frames still draw only from the Session Deck (§4). One Fate event causes at most one story draw.

**Resolving a story draw**

1. Reveal the card and place it face-up on the rail. It counts toward the 5-card rail limit and is a situation aspect.
2. Apply the row above.
3. At scene end, return it and its echo slips to its pile and reshuffle, unless it was retired.

**Empty pile.** If the pile is empty, or holds only cards already on the rail, the pile's owner writes a new NPC or THREAD on the spot. A player's new card must tie to one of their ROOTS or REACH tags. This replaces Mythic's "new character" and "new thread" results.

**Pile maintenance (scene cleanup, §7)**

- Add: any NPC who was named and mattered, and any new open question, becomes a story card. It goes to a player's pile if it ties to one character, otherwise to the GM Story Pile.
- Keep (session end only): a player may turn one temporary aspect that stuck to their character this session into a THREAD in their own Story Pile, such as Weapon Lost Over the Cliff becoming "Recover my father's sword". This is optional; if the player doesn't care (they grab a weapon off a fallen foe and move on), the aspect ends with its scene as normal Fate.
- Weight: +1 Weight (max 3) for each story card that was drawn or featured in the scene.
- Retire: an NPC who died or left the story, or a thread that was answered, goes to the Chronicle (§10).
- Over the size limit: retire the lowest-Weight card, oldest first. A player chooses for their own pile.

## 7. Prep and scene flow

Prep is choosing cards from the library, and each session runs as a loop of scenes, each closed by a fixed cleanup order.

**Pre-session prep (target: 15 minutes)**

1. **Anchors:** choose 2 cards to start face-up on the rail, 1 GLOBAL and 1 GM.
2. **Environment:** choose 3 GM cards for the Session Deck.
3. **Backup modules:** build 2 modules. Each is 2 GM cards clipped together, plus one trigger.
4. **Beat Frames:** choose 2–3 BEAT cards, each with a trigger and defaults for every blank.

**Writing triggers**

Every trigger uses the form "WHEN [event] THEN [deploy]". The event must be something an observer could confirm from the play log.

- Valid: "WHEN the party leaves the road", "WHEN any roll against the Cartel fails", "WHEN the Floodwaters clock fills".
- Invalid: "WHEN the players delay too long", "WHEN it feels right".

**The rail**

- The rail holds at most 5 face-up cards.
- GLOBAL cards stay on the rail across scenes until the GM retires them between sessions.
- If a card would exceed the limit, the GM removes the oldest non-GLOBAL GM card to the Session Discard.

**In-session clocks**

The GM marks 1 segment on a face-up GM card's clock when a roll directly against that card fails, or when a beat's stakes say so. When a clock fills, the card's threat happens: the GM triggers a Beat Frame and the card leaves the rail.

**Scene loop**

1. Run the scene test (§6), except in the session's first scene.
2. Frame the scene and play it out with rolls, invokes and compels.
3. The scene ends when its central question is answered or the party leaves.
4. Cleanup, in this order:
    1. Adjust Tension (§6).
    2. Return surfaced player cards to their binders.
    3. Move GM cards that are no longer present to the Session Discard.
    4. Update Story Piles: add, weight or retire story cards (§6A).
    5. Check every unused module and Beat Frame trigger. Deploy each one that fired.
5. Start the next scene.

Modules and Beat Frames that never trigger go back to the library unused. The GM does not force them.

## 8. Harm and card loss

Harm uses Fate stress and consequences, and each consequence also strains one of the character's cards. A card is destroyed only through a concession the player chooses.

**Stress:** two tracks, physical and mental, of 2 boxes each; Physique and Will add boxes as in Fate Core. Absorb shifts as normal.

**Consequences strain cards**

When a player takes a consequence, they write it as a normal consequence aspect. They also pick one of their cards to carry it, and that card is Strained.

| Consequence | Absorbs | Strain effect | Recovery |
| --- | --- | --- | --- |
| Mild | 2 shifts | 1 chosen power tag is not live | End of next scene |
| Moderate | 4 shifts | The whole card is not live | End of next session |
| Severe | 6 shifts | The whole card is not live, and it gains 1 Growth | After a recovery scene and 1 full session |

A Strained tag or card cannot be invoked by its owner. Opponents may still invoke its weakness tag.

**Card destruction**

- A card is never destroyed by a failed roll alone.
- When a player concedes a conflict, they may sacrifice a card. They gain the normal concession fate points plus 1 more.
- A sacrificed card goes to the Chronicle Scrapbook (§10).
- At the start of the next session, the player writes a replacement card of the same category, ROOTS or REACH. At least one of its tags must reference the lost card.

**GM cards**

A GM card leaves play when it is taken out in a conflict, overcome with success with style, or its clock fills. Cards that leave play this way go to the threat evaluation step after the session (§10).

## 9. Advancement

Cards grow through Growth. Trouble earns Growth, and 3 Growth lets the player evolve a card. Standard Fate milestones still apply to skills and refresh.

**A card gains 1 Growth when**

- Its owner accepts a compel on it, including the compel when it surfaces from the deck.
- A roll fails, or ends in success at a major cost, after one of its tags was invoked.
- It carries a severe consequence (§8).

A card gains at most 2 Growth per session. Mark Growth during the Evolution step after the session (§10), not mid-play.

**Evolving at 3 Growth**

Clear the track and choose one option:

1. Rewrite one power tag.
2. Rewrite the weakness tag to reflect growth. The new weakness must still be able to cause trouble.
3. Transform the card from ROOTS to REACH or the reverse. Keep 1 tag and write 2 new ones.
4. Retire the card to the Chronicle and write a new card of either category.

## 10. Post-session procedures

After each session the table evolves its characters, then the GM spends about 10 minutes moving the world forward and filing the Chronicle.

**Group step: Evolution**

1. Each player reviews every card of theirs that surfaced, was compelled or was invoked this session.
2. Mark Growth per §9, then evolve any card that reached 3.
3. Players who sacrificed a card write its replacement now or at the start of next session.

**GM step A: Advance clocks**

- **Bypassed:** each THREAT or FACTION that was face-up this session, faced no roll, and was not taken out gains 1 segment.
- **Off-screen:** each FACTION in the library that did not appear this session rolls 1d6. On a 5 or 6 it gains 1 segment.
- **Filled:** any clock that filled triggers a world change. Write it on the Chronicle page and prepare a Beat Frame for it next session.

**GM step B: Evaluate threats that left play**

- If the fiction left the threat alive, for example because it fled or was only driven off, it mutates. Replace 1 power tag with a tag reflecting what the party did to it. Add 1 clock segment and a version suffix (T-03 becomes T-03v2).
- If the threat was destroyed or fully resolved, retire it to the Chronicle.

**GM step C: The Chronicle Scrapbook**

Each session gets a two-page spread.

- **Left page:** session number and date; a 3-sentence summary; a list of World Reverberations covering every clock change, mutation, card lost or evolved, and the closing Tension value.
- **Right page:** clear pockets holding every card retired this session. Only cards that appeared in play can be retired.
- **Legacy Footer:** on the back of each retired insert, write the session number, how the card left play, and one sentence of epitaph.

## 11. Edge-case rulings

These rulings override any looser reading of sections 3–10.

| Situation | Ruling |
| --- | --- |
| A drawn player card doesn't fit the scene at all | The GM must still use one of its tags. It can arrive as a memory, a messenger, news or an omen. The card cannot be discarded unused. |
| The drawn card belongs to the player who rolled | Allowed. The compel applies normally. |
| The owner has 0 fate points and wants to refuse the compel | They cannot refuse, as in standard Fate. |
| The card's owner is absent this session | Their card is not added to the deck. If it is somehow drawn, set it aside and draw again. |
| A tie happens while a Beat Frame is resolving | Resolve the Beat Frame's draws first, then the tie's draw. |
| A Beat Frame triggers and the deck is empty | Use the frame's defaults for every blank. |
| A player wants to invoke a GM card's tag | Allowed if the fiction supports it. They pay 1 fate point. The GM's free invoke on that card belongs to the GM only. |
| One tag both helps and hinders the action | Each side may invoke it once on that roll, paying separately. |
| An opponent wants to invoke a card that is in the Session Deck | Not allowed. Cards in the deck are not live for anyone. |
| A consequence must strain a card | The player must pick a card in their binder, not the one in the deck. |
| Evolution breaks the 2 ROOTS / 2 REACH split | Allowed. The split applies only at character creation. |
| What counts as a roll "against" a GM card for clocks | Any roll where that card's tag set the difficulty or the GM invoked it. |
| More than 4 players | The deck is 3 GM cards plus 1 per player. Nothing else changes. |
| A new player joins mid-campaign | They build 4 cards and add 1 to the next session's deck. |

## 12. Agent playtest protocol

Run each scenario with six agents, log every event in one fixed format, and log any gap in this spec instead of papering over it.

**Agent roles**

| Agent | Given | Job |
| --- | --- | --- |
| GM | This spec, the world deck, prep packet | Run the session using only these rules |
| Player 1 (Protector) | Silas's binder | Plays to protect others; accepts most compels |
| Player 2 (Opportunist) | Vesper's binder | Maximises fate points and invokes; tests the economy |
| Player 3 (Storyteller) | Kael's binder | Leans into backstory; answers Beat Frame questions richly |
| Player 4 (Rules lawyer) | Mira's binder | Refuses compels when affordable; probes edge cases |
| Referee | This spec only | Checks every event against the rules; logs violations and ambiguities |

**Ground rules for agents**

- Dice are rolled by a random number generator, never chosen by an agent.
- If the spec doesn't cover a situation, the Referee logs an AMBIGUITY with the section number and the interim ruling used. No agent invents a rule silently.
- The GM agent may not draw from the deck except on a trigger listed in §4.

**Event log format (one row per event)**

```csv
scene,actor,action,skill,tags_invoked,fp_spent,dice,total,opposition,result,draw_id,compel,clock_change,tension,notes
2,Mira,Overcome: scout tower,Stealth +2,Muddy Camouflage,1,-1,+3,+2,success,,,,3,
2,Vesper,Attack: guard,Fight +2,,0,0,+2,+2,tie,SV-03,accepted,,3,Silas panics at cellar crack
```

**Scenarios**

1. **Baseline:** one session of 5 scenes, 4 players, Tension 3, standard prep.
2. **Tie storm:** make ties likely by setting opposition equal to each player's rolled skill. This tests deck exhaustion, the climax rule and the backstory guarantee.
3. **Refusal economy:** all player agents refuse every compel they can afford. This tests whether backstories still surface and whether fate points break.
4. **Beat Frame stress:** three frames trigger in one session, including a forced type mismatch, such as a LOCATION drawn for a WHO blank.
5. **Concession:** a conflict where one player concedes and sacrifices a card, followed by the next session's opening and the replacement card.
6. **Campaign:** 4 linked sessions with full post-session procedures. This tests clocks, mutation, Tension drift and card Growth.

**Metrics and targets**

| Metric | Target |
| --- | --- |
| Sessions where every player's card surfaced | 100% |
| Deck draws per session | 5–8 |
| Draws where the cost actually used the drawn card | 100% |
| Average player fate points at session end | 1–5 |
| Referee rule violations | 0 |
| AMBIGUITY entries per session | Falling across runs, toward 0 |
| Tension value across the campaign scenario | Mostly 2–5, not pinned at 1 or 6 |
| Cards reaching 3 Growth by session 4 | At least 1 per player |

**Run report (each run ends with)**

- The metrics table filled in.
- Every AMBIGUITY entry with the section it points to.
- The top 3 friction points, in the Referee's judgment.
- One sentence from each player agent: did their backstory feel used well, ignored, or used against them unfairly?

## 13. Open design questions and test variables

These are deliberate choices the playtest should settle. Run each variant against the baseline scenario and compare metrics.

| Question | Default in this spec | Variant to test |
| --- | --- | --- |
| How does a player's card enter the deck? | Random draw from binder | Player chooses which card to put in, as a "spotlight bid" |
| How much does surfacing reward the owner? | 1 free invoke | 2 free invokes, or none |
| What is the GM's fate point budget? | 1 per player per scene | A flat 2 per scene |
| How many open blanks does a Beat Frame have? | Exactly 2 | 1, to save deck cards; or 3, for more backstory |
| How high can passive opposition go? | Great (+4) | Superb (+5) |
| How big is the Session Deck? | 3 GM cards + 1 per player | 2 GM cards + 1 per player, for a faster climax |
| When is Growth marked? | After the session | Immediately, in play |
| What is the tension track's range? | 1–6 on a d6 | 1–9 on a d10, as in Mythic |
| What triggers a Story Pile draw? | The four Fate events in §6A | Also draw from the GM Story Pile on every Altered scene result (§6) |

Draft inconsistencies fixed by this spec: the 7-card deck count (the draft said 8), the undefined "Forest Ghost" theme, the Growth trigger for Silas, the Broken Compass destroyed by a single miss, the missing FACTION and CULTURE types, and the H-03 card archived without appearing in play.
