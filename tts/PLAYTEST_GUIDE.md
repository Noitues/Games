# Hex-Nexus playtest: quick start

**Build on the table:** Rules 1.9.0 · Roster 1.9.0 · Config `batch_0075`
(death timers 2 / 4 / 6, a playtest variant). The panel (top right; **HN**
hides it) always shows the build. Put it in any feedback you send.

## Start (1 minute)

1. **Seats:** North plays **Blue**, South plays **Red**. Red (South) has
   priority in round 1; it alternates after that.
2. **Draft (optional):** put a champion card from your deck into a role slot
   on your dashboard (TOP, JUNGLE, MID, ADC, SUPPORT).
3. Press **Start game**. Empty roles are filled at random, with no champion on
   both sides. The standees go to your base, and round 1's Upkeep runs: AP 3
   each, the first waves spawn, the camps come up.

## Each round: press **Next phase ▶**

| Phase | You do | The table does |
|---|---|---|
| **Upkeep** | nothing | heals surviving monsters, counts cooldowns down, respawns the dead, heals at the fountain, decays structures, resets AP, moves and spawns waves, respawns monsters, flips tiles back |
| **Action** | take your activations in snake order **1 2 2 1 1 2 2 1 1 2** (1 = priority). **Next activation ▶** steps it; the panel shows whose turn it is | pays AP, sets cooldowns, banks AP for chips, handles kills and falls |
| **World** | nothing | waves, towers and monsters hit everything next to them; kills, falls and rewards are applied |
| **Shop** | Player 1, then Player 2: right-click an item card → **Buy** | pays the cost |
| **Win Check** | nothing | a Nexus at 0 ends the game; round 20 goes to the tiebreak |

## On your activation

- **Move** your standee by hand, up to its Speed.
- **Use an ability:** right-click the champion's card → *Use Q · 1 AP · CD1*.
  The AP is paid and the whole card is out for its cooldown: the label shows
  **CD n**, then **READY**. A card on cooldown, or one the pool can't pay for,
  is refused.
- **Hit something:** left-click its HP label once per hit (right-click undoes).
  - A chip off a **monster** or an **enemy wave** is **+1 AP** to your pool,
    straight away.
  - A champion at 0 is a **kill**:
    - the killer gets 6 / 8 / 10 AP, or 10 / 12 / 14 with the Baron;
    - the card shows **DEAD n**;
    - the standee goes to its bench, and it respawns by itself.
  - A **monster** at 0 is yours: Blue Buff, Red Buff, Dragon and Baron cards
    are dealt to your hand.
  - A **tower** at 0 pays you 3 AP. Hit T1 before T2, and a whole lane before
    the Nexus; the table warns you if you don't.
- **Buff cards:** right-click → **Play**.
  - Blue Buff adds its AP.
  - Red Buff and Dragon: click the target's HP for the hits.
  - The Dragon card then goes on its own cooldown.

## Table controls

| Want to… | Do this |
|---|---|
| See the whole board | **Map view** on the panel, or bind the **Hex-Nexus: map view** key (Options → Game Keys) |
| Flip a hexgroup | right-click the tile → **Flip hexgroup**, or bind **Hex-Nexus: flip hexgroup** and press it over the tile |
| Fix a number | click it: HP labels, card cooldowns and the AP counter all take left −1, right +1 |

## Hidden hexgroups: the short version

- A hidden tile is **one space** for movement. Ranges are still counted in
  hexes.
- Your champion inside a hidden tile can't be targeted from outside. An enemy
  champion **within 2 hexes** reveals the tile.
- Standees on a hidden tile stay visible to everyone. Where on the tile you
  put them doesn't matter.

## Not automated yet

- movement;
- ability effects (shields, slows, roots, pushes);
- item effects on champions.

Play these by hand. Shields aren't tracked, so World Phase hits ignore them.

## After the game

Note the winner, the rounds played and anything confusing. Automatic logs and
a feedback card come later (M3).
