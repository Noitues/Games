# Generation Ship — Art Brief and Prompt Set

This brief covers four candidate art directions:
- A: Grimdark,
- B: Steam / Spacepunk,
- C: New Age Space,
- D: Retro Space.

Its purpose is to produce real, painted concept renders so the designer can choose one direction. Everything here is meant to be manufactured as a physical board game. Art must survive print (CMYK, matte card stock, 2 mm greyboard) and read across a table.

- **Part 1:** shared specs that every style must obey.
- **Part 2:** one section per style: palette, materials, rules, and ready-to-paste image prompts.
- **Part 3:** how to keep a set consistent.

---

> **Using ChatGPT?** Paste the ready-made messages in `art/CHATGPT_PROMPTS.md` instead of the Part 2 prompts.

## Part 1 — Shared specs (all styles)

### The game in one paragraph (for any artist)
A cooperative game about Great Houses stewarding a generation ship. Generations of leaders move down a conveyor (Dawn, Day, Dusk) and retire to a Wall of Leaders. Threat spreads through ship sections as Glitches, Faults and Failures. Crew live and fight in the sections. Decay is permanent damage. The tone is "the Forgotten Machine": people live inside a vast machine they no longer fully understand.

### Components to render
1. **People card** (poker size, 63 × 88 mm, 3 mm bleed). 400 in the game; every leader is a people card.
2. **Ship board module** (a hexagonal cardboard tile, 2 mm greyboard). Eight sections, an Outer Hull edge, and a printed void crescent beyond the hull.
3. **Wall of Leaders**, a dual-layer slotted board. Retired leader cards slide in from the top edge. Windows show each card's portrait and Legacy.
4. **Tokens:**
   - threat: Glitch, Fault and Failure;
   - Crew;
   - Decay;
   - house influence (4 colours);
   - Breakthrough marker (one per style: lamp / gear / crystal / starburst).
5. **Box cover** (optional, for the final pick).

### Hard layout constraints

**People card template.** These positions are fixed for every card, because the Wall windows must line up.

| Zone | Position (from the card top, 88 mm tall) | Content |
|---|---|---|
| Name bar | 0–9 mm | Name, cost (top right) |
| **Portrait window** | 9–44 mm, full width (63 × 35 mm art area; 69 × 38 mm with bleed) | The person's portrait. Must read inside an arch or round frame inset 4 mm from each side. |
| Guilds + effect text | 44–72 mm | 2–4 guild icons; effect; threshold bonus; Reign |
| **Legacy band** | 72–88 mm (63 × 16 mm) | Legacy text, always last. Shows through the Wall's plaque window. |

**Ship board module.**
- **Outline:** every board shares one flat-top hexagonal hull module, about 200 mm across. The exact outline is `outline` in `data/boards.json` (circumradius 180 units = 100 mm).
- **Docking sides:** five sides have a dovetail tab-and-socket profile, so boards dock on any side. Keep 6 mm of art clear of each docking edge, so seams line up between boards.
- **Outer Hull:** the top side, with armour plating, a prow and two fins. Its sections must read as "facing space" (viewports, armour, airlocks).
- **Void crescent:** printed beyond the hull, about 45 mm deep (`void_zone` in `data/boards.json`). It is open space and is reserved for future houses, so keep it mostly empty.
- **Sections:** eight per board, of four types. The four types **must be distinguishable at a glance and for colourblind players**: use a different light value plus a corner icon, not hue alone.
  - **Infrastructure:** reactors, pumps, conduits, power.
  - **Residential:** bunks, corridors, laundry lines, homes.
  - **Government:** council chamber, archives, comms.
  - **Agricultural:** hydroponic terraces, orchards, water tanks.
- **Art can bend the board, not the outline.** Interior art may follow the section borders like walls of rooms seen from above (a cutaway "dollhouse" top-down view). The outer silhouette and docking profile must stay exactly as in the data, or boards won't fit together. Fins, prow and plating detail can be enriched within the hull edge.
- **Leave clear space:** about 40 % of each section stays calm, low-detail mid-tone, so tokens (about 16 mm) stay legible on top.

**Wall of Leaders (dual-layer board).**
- **Size:** a tri-fold board, 3 panels of 4 slots each (12 leaders), each panel about 290 × 120 mm.
- **Top layer** (2 mm) has, per slot:
  - a frame window over the card's portrait zone (about 55 × 33 mm),
  - a plaque window over the Legacy band (about 59 × 14 mm),
  - a printed frame around each window,
  - a slot number (I–XII or 1–12).
- **Bottom layer** (2 mm) backs it. The card slides down between the layers through slits in the top edge. Optionally, a thumb notch at the top of each slit.
- **Breakthrough marker:** a token that sits on the frame of a slot.
- **Look:** a gallery or memorial of ancestors, not a spreadsheet.

### Print realities (all styles)
- Rich blacks and deep darks need a CMYK rich-black build. Avoid large areas of pure 100 % black in Grimdark; aim for 85–90 % value.
- Text on art: always on a solid or near-solid panel, at least 7 pt.
- Foil, emboss and holo are box and deluxe options only, never needed to read the game.
- Every component must also work in a plain print-and-play build.

### Characters for portrait tests (use the same four in every style)
1. **Ostra Vell, Archivist** (Remarkable; Scholars, Engineers, Keepers). Woman in her 60s, sharp and tired eyes, ink-stained fingers. She holds a lantern or data-slate. A keeper of the ship's lost manuals.
2. **Dace Morrow, Hydroponics Hand** (Common; Farmers, Laborers). Broad-shouldered man in his 30s, sleeves rolled, soil and coolant stains, a seedling tray.
3. **Ilka Tor, Steward of the Council** (Remarkable; Bureaucrats, Keepers). Androgynous elder with a severe posture and a chain of office. Calm, unreadable.
4. **Pell Ashgrove, Junior Engineer** (Common; Engineers, Navigators). Teenager, oversized gloves, welding goggles pushed up, grinning.

Portraits are **head and shoulders, three-quarter view, the face in the upper-middle third**, so they survive the arch window crop. Each needs a simple background that hints at the guild (archives, terraces, council, engine room).

### Board art test
Paint **board A** first, using these sections (centres from `data/boards.json`):
- **Outer Hull:** A1 Infrastructure, A2 Residential, A3 Agricultural.
- **Core:** A4 Government, A5 Agricultural, A6 Infrastructure, A7 Government, A8 Residential.

---

## Part 2 — The four directions

> **Prompt format.** Each prompt is written to paste into an image model (Midjourney / Flux / gpt-image / Stable Diffusion). Aspect ratios are given as `--ar` (Midjourney syntax); for other tools, set the size to match. The negative prompt goes in the tool's negative field where supported; otherwise drop it.
>
> **Shared negative prompt:** `text, letters, words, watermark, signature, logo, UI, frame border, extra fingers, deformed hands, blurry, low resolution, 3d render plastic look, photograph`

### A · Grimdark

**Pitch.** Every generation pays for the last one's mistakes. Rust, bone, lamp-smoke, iron devotion. A ship that has become a cathedral of maintenance rituals.

**Palette:**

| Role | Colour |
|---|---|
| Base darks | `#14110F`, `#2A221C` |
| Rust | `#7A2A14` |
| Blood accent | `#8A2A1E` |
| Bone | `#D8CFC0` |
| Tarnished brass | `#8A6A3A` |
| Lamp orange | `#FF7A4A` (light source only) |

**Section types:**

| Type | Colour | Icon |
|---|---|---|
| Infrastructure | gunmetal `#4A4E52` | cog |
| Residential | rust brown `#6A3A24` | bunk |
| Government | oxblood `#4A2A2E` | seal |
| Agricultural | sick olive `#4A4A2A` | sprout |

**Materials and light:** oil-paint texture, heavy chiaroscuro, single warm light sources (lamps, furnace glow) in cold dark space. Corroded iron, riveted plates, chains, votive candles beside machinery, frayed cloth.

**Typography:**
- **Titles:** a blackletter display face, such as Pirata One or UnifrakturCook.
- **Body:** Spectral.

**Wall:** iron arch niches like a mausoleum; plaques are cast-iron nameplates. Breakthrough marker: an oil lamp.

**Risk:** too dark to read on the table. Keep section mid-tones lighter than you think, and keep token contrast high.

**Prompts.**
- **Portrait: Ostra Vell.** `grimdark science-fantasy oil painting, head and shoulders three-quarter portrait of a woman in her sixties, the archivist of a decaying generation ship, sharp tired eyes, ink-stained fingers holding a smoking iron lantern, hooded threadbare robes over a rusted collar of cables, background of corroded conduits and stacks of mouldering manuals, single warm lamp light from the right, deep shadows, painterly brushwork, muted rust bone and oxblood palette, solemn devotional mood --ar 63:35`
- **Portrait: Dace Morrow.** `grimdark oil painting, head and shoulders three-quarter portrait of a broad-shouldered man in his thirties, hydroponics labourer on a dying generation ship, sleeves rolled, soil and black coolant stains, holding a tray of pale seedlings under a flickering grow-lamp, iron pipes dripping behind him, harsh single light, painterly, rust and sick-green palette --ar 63:35`
- **Portrait: Ilka Tor.** `grimdark oil painting, head and shoulders three-quarter portrait of an androgynous elder steward, severe upright posture, heavy iron chain of office with a gear-shaped seal, shaved head, calm unreadable face, council chamber of iron pews and red banners behind, candlelight, deep chiaroscuro, painterly, oxblood and bone palette --ar 63:35`
- **Portrait: Pell Ashgrove.** `grimdark oil painting, head and shoulders three-quarter portrait of a grinning teenage engineer, oversized scorched gloves, welding goggles pushed up on soot-black hair, engine-room furnace glow behind, sparks, painterly brushwork, rust and ember palette, a rare moment of hope in a grim world --ar 63:35`
- **Board A.** `top-down orthographic cutaway illustration of a hexagonal module of a gothic industrial generation ship, eight rooms separated by thick riveted iron walls: reactor and pump room, crowded rusted bunk hall, iron council chamber with banners, hydroponic terraces under sickly lamps, seen directly from above like a dollhouse map, top edge is armoured outer hull with viewports and two fins facing black space with faint red stars, oil painting texture, muted rust bone gunmetal palette, game board art, even lighting for readability --ar 1:1`
- **Card frame.** `ornate grimdark card frame design, tarnished iron and bone filigree border, gothic arch-shaped window at top, empty parchment text panel below, cast-iron nameplate at the bottom, flat front view, no text, painterly texture, rust and bone palette --ar 63:88`
- **Wall panel.** `front view of a gothic iron memorial wall panel with four arched niches in a row, each niche has a small iron nameplate below it, empty niches showing dark backing, rivets, candle soot, rust streaks, votive candles at the base, painterly oil texture, game component art, flat orthographic --ar 29:12`
- **Box cover.** `epic grimdark science-fantasy oil painting, a colossal gothic generation ship drifting through black space, its hull a cathedral of rusted iron spires and lit stained-glass viewports, tiny silhouettes of robed crew on a gantry holding lanterns, sense of vast age and devotion, dramatic chiaroscuro --ar 4:5`

### B · Steam / Spacepunk

**Pitch.** A Victorian engine room that learned to fly. Brass, copper, mahogany, pressure gauges, orreries, aether. Optimistic ingenuity under strain.

**Palette:**

| Role | Colour |
|---|---|
| Mahogany | `#3A2014` |
| Brass | `#D9A85A` |
| Copper | `#B8663A` |
| Verdigris teal | `#2E5A5A` / `#7AB0A8` |
| Cream paper | `#F2E2C0` |
| Aether blue | `#1E3A4A` |

**Section types:**

| Type | Colour | Icon |
|---|---|---|
| Infrastructure | verdigris | boiler |
| Residential | copper | teacup |
| Government | plum lacquer `#5A3448` | quill |
| Agricultural | olive brass `#6A6A24` | glass dome with fern |

**Materials and light:** polished and tarnished metal, warm gaslight, glass domes, rivets, gauges, leather, steam. Painterly, with crisp specular highlights on brass.

**Typography:**
- **Titles:** Playfair Display SC.
- **Body:** Libre Baskerville.

**Wall:** brass porthole frames on mahogany; engraved brass plaques. Breakthrough marker: a brass gear.

**Risk:** everything turns brown. Keep the teal and plum section colours strong.

**Prompts.**
- **Portrait: Ostra Vell.** `steampunk space-age oil painting, head and shoulders three-quarter portrait of a woman in her sixties, chief archivist of a brass-and-mahogany generation ship, round brass spectacles, ink-stained fingers holding a glowing data-slate in a brass case, leather apron, background of a brass orrery and shelves of bound manuals, warm gaslight, verdigris and copper palette, rich painterly detail --ar 63:35`
- **Portrait: Dace Morrow.** `steampunk space-age oil painting, head and shoulders three-quarter portrait of a broad-shouldered hydroponics labourer, rolled shirt sleeves and braces, holding a seedling tray under a glass dome with copper misting pipes, ferns and brass valves behind, warm light, verdigris and brass palette --ar 63:35`
- **Portrait: Ilka Tor.** `steampunk space-age oil painting, head and shoulders portrait of an androgynous elder council steward in a high-collared plum frock coat, gold chain of office with a compass seal, calm unreadable face, mahogany council chamber with brass speaking tubes behind, gaslight, painterly --ar 63:35`
- **Portrait: Pell Ashgrove.** `steampunk space-age oil painting, head and shoulders portrait of a grinning teenage engineer, brass welding goggles pushed up, oversized leather gloves, soot on cheek, copper pipes and pressure gauges hissing steam behind, warm glow, painterly --ar 63:35`
- **Board A.** `top-down orthographic cutaway illustration of a hexagonal deck of a steampunk generation ship, eight rooms divided by riveted brass bulkheads: boiler and pump room with gauges, cosy copper-panelled cabins with tea sets, plum-lacquered council chamber with speaking tubes, hydroponic glass domes with ferns, top edge is a riveted hull with porthole windows and two fins facing the blue aether with stars, seen from directly above like a map, painterly, brass verdigris copper palette, even light --ar 1:1`
- **Card frame.** `steampunk card frame design, brass and mahogany border with rivets and small gears, round porthole window at top, cream paper text panel, engraved brass plaque at the bottom, flat front view, no text --ar 63:88`
- **Wall panel.** `front view of a mahogany wall panel with four brass porthole frames in a row and an engraved brass plaque under each, rivets, small pressure gauge between portholes, empty dark glass in the portholes, painterly, game component art, flat orthographic --ar 29:12`
- **Box cover.** `steampunk space-age oil painting, a vast brass generation ship with copper sails and glowing portholes crossing a blue aether nebula, crew in waistcoats on an observation gallery, sense of wonder and invention --ar 4:5`

### C · New Age Space

**Pitch.** The voyage as a long meditation. Nebula washes, crystal light, sacred geometry, soft luminous people. Calm, hopeful, a little mysterious.

**Palette:**

| Role | Colour |
|---|---|
| Night indigo | `#1B1838`, `#2A2458` |
| Lilac | `#B48AE0` |
| Aqua | `#4AC0C8` |
| Rose | `#F0A0C0` |
| Pearl white | `#F6F3FC` |
| Soft gold accent | `#E8D8A0` |

**Section types:**

| Type | Colour | Icon |
|---|---|---|
| Infrastructure | aqua | wave |
| Residential | rose | circle |
| Government | lilac | triangle |
| Agricultural | mint `#8AC8A0` | leaf |

Each type also gets a distinct geometric glyph.

**Materials and light:** soft glow, translucent crystal, iridescence, mist, airbrushed painting, gentle bloom. People lit from within or by soft aura light.

**Typography:**
- **Titles:** Cormorant.
- **Body:** Outfit.

**Wall:** frosted acrylic look, with hexagonal crystal windows and soft pearl plaques. Breakthrough marker: a clear acrylic crystal.

**Risk:** low contrast and "screensaver" vagueness. Keep strong value steps between sections, and keep the people specific and grounded.

**Prompts.**
- **Portrait: Ostra Vell.** `luminous new-age science-fiction painting, head and shoulders three-quarter portrait of a serene woman in her sixties, archivist of a crystal generation ship, silver hair, ink-dark fingertips touching a floating translucent crystal tablet, soft halo of geometric light, nebula of lilac aqua and rose behind, airbrushed painterly glow, calm wise expression --ar 63:35`
- **Portrait: Dace Morrow.** `luminous new-age science-fiction painting, head and shoulders portrait of a broad-shouldered gardener in his thirties, holding a glowing seedling in cupped hands, hydroponic garden of bioluminescent plants behind, mint and aqua light, gentle smile, soft painterly glow --ar 63:35`
- **Portrait: Ilka Tor.** `luminous new-age science-fiction painting, head and shoulders portrait of an androgynous elder steward in flowing pale robes, a thin gold circlet, calm unreadable face, sacred geometry mandala of light behind, lilac and pearl palette, ethereal --ar 63:35`
- **Portrait: Pell Ashgrove.** `luminous new-age science-fiction painting, head and shoulders portrait of a grinning teenage engineer with light-filament goggles on their forehead, holding a glowing crystal component, aqua sparks, nebula colours behind, joyful, soft painterly glow --ar 63:35`
- **Board A.** `top-down orthographic illustration of a hexagonal module of a crystalline generation ship, eight chambers separated by thin glowing white seams: aqua energy chamber, rose living quarters with soft lights, lilac council chamber with a mandala floor, mint garden terraces, top edge is a translucent crystal hull facing a lilac nebula with stars, seen from directly above like a map, airbrushed painterly glow, readable distinct chamber colours --ar 1:1`
- **Card frame.** `elegant new-age card frame, thin iridescent pearl border with fine sacred geometry, hexagonal window at top, soft white text panel, rounded pearl plaque at bottom, flat front view, no text --ar 63:88`
- **Wall panel.** `front view of a frosted glass wall panel with four hexagonal crystal windows in a row and a soft pearl plaque under each, subtle sacred geometry etched in the glass, soft lilac and aqua glow, flat orthographic, game component art --ar 29:12`
- **Box cover.** `luminous new-age science-fiction painting, a crystalline generation ship like a cathedral of light drifting through a vast lilac and aqua nebula, tiny silhouettes of people in a glowing observation dome, serene and hopeful --ar 4:5`

### D · Retro Space

**Pitch.** 1950s–60s pulp optimism: rocket fins, atomic starbursts, ringed planets, turquoise and tangerine, halftone print. A golden-age paperback cover come to life.

**Palette:**

| Role | Colour |
|---|---|
| Deep teal | `#0F3A48` |
| Turquoise | `#3AB0A8` |
| Tangerine | `#E8603A` |
| Mustard gold | `#F6C85A` |
| Cream | `#FBEFD6` |
| Pink | `#E88AA0` |
| Lime | `#A8C860` |

**Section types:**

| Type | Colour | Icon |
|---|---|---|
| Infrastructure | turquoise | atom |
| Residential | tangerine `#F2A060` | house |
| Government | pink | star |
| Agricultural | lime | leaf |

**Materials and light:** gouache-like flat colour with soft painted gradients, halftone dot shading, chunky outlines, chrome highlights, cheerful key light.

**Typography:**
- **Titles:** Righteous (or an atomic-age display face).
- **Body:** Josefin Sans.

**Wall:** rounded tangerine panel with rocket-nose windows and mission-plaque windows. Breakthrough marker: a gold starburst.

**Risk:** reads as parody. Keep the people sincere; the stakes are real.

**Prompts.**
- **Portrait: Ostra Vell.** `1950s pulp science-fiction paperback illustration, gouache painting, head and shoulders three-quarter portrait of a sharp-eyed woman in her sixties, chief archivist of an atomic-age generation ship, silver bob haircut, cat-eye glasses, holding a punch-card ledger, round viewport with a ringed planet behind, turquoise tangerine and cream palette, halftone texture, sincere and intelligent expression --ar 63:35`
- **Portrait: Dace Morrow.** `1950s pulp science-fiction gouache illustration, head and shoulders portrait of a broad-shouldered hydroponics farmer in a turquoise jumpsuit, rolled sleeves, holding a tray of seedlings under a chrome grow-lamp, rows of space plants behind, warm optimistic light, halftone texture --ar 63:35`
- **Portrait: Ilka Tor.** `1950s pulp science-fiction gouache illustration, head and shoulders portrait of an androgynous elder council steward in a high-collared uniform with a gold starburst medallion, calm unreadable face, mid-century modern council chamber with a big round window behind, pink and teal palette, halftone --ar 63:35`
- **Portrait: Pell Ashgrove.** `1950s pulp science-fiction gouache illustration, head and shoulders portrait of a grinning teenage rocket mechanic, chrome goggles pushed up, oversized gloves, wrench on shoulder, rocket engine glowing tangerine behind, cheerful, halftone texture --ar 63:35`
- **Board A.** `top-down orthographic illustration of a hexagonal deck of a 1950s atomic-age generation ship, eight rooms with rounded mid-century walls: turquoise reactor room with atom motifs, tangerine family apartments with boomerang tables, pink council room with starburst floor, lime hydroponic gardens, top edge is a chrome hull with rocket fins and round portholes facing deep teal space with gold starbursts and a ringed planet, seen from directly above like a map, gouache and halftone, bold readable colours --ar 1:1`
- **Card frame.** `1950s retro space card frame, rounded tangerine border with chrome trim and small starbursts, rocket-nose shaped window at top, cream text panel, teal mission plaque at bottom, flat front view, no text --ar 63:88`
- **Wall panel.** `front view of a mid-century retro space wall panel, rounded tangerine panel with four rocket-nose shaped windows in a row and a teal mission plaque under each, chrome trim, gold starbursts, flat orthographic, gouache and halftone, game component art --ar 29:12`
- **Box cover.** `1950s pulp science-fiction paperback cover painting, a gleaming chrome generation ship with rocket fins leaving a ringed planet, families waving from a big round observation window, gold starbursts, turquoise and tangerine, optimistic golden-age adventure --ar 4:5`

---

## Part 3 — Consistency and workflow

**Generating the art:**
1. **Lock each style first.** Generate 4–8 portraits of Ostra Vell in a style, then pick one as the **style reference** (Midjourney `--sref` / image prompt; Flux or SD: IP-Adapter or a small LoRA). Reuse it for every other image in that style.
2. **Keep the characters the same across styles.** Keep the same character descriptions and use the chosen Ostra image as a **character reference** (`--cref`) when testing the other styles.
3. **Boards come out of image models imprecise.** Generate the board *art* square, then clip it to the real outline and section polygons from `data/boards.json` (the Blender scene or a layout tool does this). The section borders printed on top should come from the data, not the painting.
4. **Text is never in the image.** Names, numbers and rules are typeset on top in layout, using the fonts listed per style.

**Laying out and rendering:**
1. **Composite into the templates.** Card art goes in the 63 × 35 mm portrait zone. Board art is clipped per section. Wall art is the frame layer only; the portraits come from the cards.
2. **Render physical mockups** in Blender (see `art/BLENDER_SESSION_PROMPT.md`). Show cards in the slotted Wall, boards docked on a table, and tokens on sections.

**The decision.** For each style, compare four things:
- the hero portrait,
- board A at table distance,
- the Wall with three leaders slotted,
- one table-spread render.
