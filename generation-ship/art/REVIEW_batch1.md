# Review of image batch 1 (all four styles)

The designer is leaning towards **Retro Space**.

## Comparison
| Style | Table readability | Identity | Print cost | Notes |
|---|---|---|---|---|
| Grimdark | Poor | Strong | Medium | Boards and Wall are near-black; sections and tokens would vanish on the table. |
| Steam / Spacepunk | Fair | Strong | High (detail, foil) | Rich, but the boards are busy and everything trends brown. |
| New Age | Fair | Weak | Medium | Pretty, but generic and glossy. Faces drift towards stock fantasy. |
| **Retro Space** | **Best** | **Strong** | **Lowest** (flat colour, halftone) | Section colours map cleanly to types, floors are calm, and the people are sincere rather than parody. |

## Retro: what works
- **Board A.** It hit the brief almost exactly:
  - turquoise reactor = Infrastructure;
  - tangerine apartments = Residential;
  - pink council room = Government;
  - lime gardens = Agricultural.

  Floors are calm enough for tokens. The chrome hull, fins and portholes read as "facing space".
- **Card frame + Wall panel.** Both chose the **rocket-nose window**. One shape across the card and the Wall makes a coherent component system.
- **Portraits.** Ostra (both versions) and Pell are on-model and sincere. Ilka's pink council room is the strongest "place" image.

## Retro: what to fix
1. **Card and Wall windows must be the same shape and size.**
   - The card frame's window is a wide arch; the Wall's windows are tall narrow rocket noses. Choose one master window, then cut the Wall from the card.
   - Recommendation: the card's arch, at about 55 × 40 mm. The card template's portrait zone grows to 9–49 mm, and the Legacy band stays at 72–88 mm.
2. **The card frame's bottom plaque is too short** for the Legacy band (it shows about 10 % of the height; it needs about 18 %). The middle text panel can shrink.
3. **The board geometry differs from the game's.** The art drew a symmetric **hub plus six rooms (7 sections)**, with hull fins top and bottom. The game's boards are 8 irregular sections with the Outer Hull on one side. Two options:
   - **(a) Keep the game geometry:** the painter follows `data/boards.json` (the safe choice, keeps balance).
   - **(b) Adopt a hub-and-ring board:** a central hub, a ring of rooms, and the hull on one arc. This is more readable and more "retro", but changes adjacency and needs re-balancing.
4. **Prompt drift:**
   - Dace came out as a woman (the prompt said a man). Keep it if you like her; otherwise re-prompt.
   - `ostra_2` has lettering on signs and book spines. Re-run or crop; never print generated text.
5. **Missing pieces for the full set:**
   - boards B–D;
   - token designs (Glitch / Fault / Failure, Crew, Decay, house influence, Breakthrough starburst);
   - a card back;
   - house player boards;
   - the four section-type corner icons (atom / house / star / leaf).

## Decisions and follow-up (2026-11-05)
- **Item 1 and 2, done (Retro v2):** one master window, the card frame's wide arch at 55 × 40 mm, and a 59 × 16 mm Legacy plaque (18 % of the card). Geometry: `tools/retro_templates.py`. New art, generated as edits of the layout guides so the windows match: `art/source/retro/card_frame_v2a/b.png` and `wall_panel_v2a/b.png`, with `_exact` copies whose windows are re-cut from the master shape.
- **Item 3, decided: option (a).** Keep the game's 8-section boards; the art follows `data/boards.json`.
- **Image API:** gpt-image-1 was shut down on 2026-10-23. Direct requests use `gpt-image-2.6-sunburst`; the Batch API (half price, now the project's only route for image runs) takes GPT Image 2.5 only, so batches use `gpt-image-2.5-sunburst`.
