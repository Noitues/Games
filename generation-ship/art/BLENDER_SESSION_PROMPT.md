# Prompt for a local Claude session that drives Blender

Paste everything below the line into a Claude Code session running **on your own computer**. Use the Claude Desktop app, or run `claude` in a terminal, in the folder where you keep the repo. Blender must be installed.

There are two ways to let Claude drive Blender:
- **Headless scripts (simplest).** Claude writes Python scripts and runs `blender --background --python <script>` from the terminal. Nothing to install beyond Blender itself.
- **Blender MCP (optional, interactive).** Install the open-source `blender-mcp` add-on and server, then connect it to Claude Desktop or Claude Code. This lets Claude inspect and tweak the open scene live. It can also pull free HDRIs and textures from Poly Haven.

Both work with the prompt below; it tells Claude to prefer reproducible scripts either way.

---

You are helping me produce physical-product renders for my board game **Generation Ship**, so I can choose an art direction. Build everything in **Blender** with **reproducible Python scripts**. Don't hand-place anything that can't be regenerated.

## Get the project
- Repo: `https://github.com/Noitues/Games`, branch `claude/spirit-island-time-game-hm161z`. If it isn't cloned yet, clone it; otherwise `git pull` that branch. The game lives in `generation-ship/`.
- Read these first:
  - `generation-ship/art/ART_BRIEF.md`: the four art directions, palettes, component specs and the fixed card template.
  - `generation-ship/data/boards.json`: the exact board geometry.
    - `outline`: the hexagonal hull module shared by every board, in units where the circumradius 180 = **100 mm**.
    - `void_zone`: the printed void crescent beyond the hull.
    - `boards[].sections[].poly`: section polygons, with `type`, `hull` and `center`.
    - `layouts`: board placements `[x, y, rotation°]` for multi-board ships.
  - The "Wall of Leaders" and "People cards" sections of `generation-ship/GDD.md`.
- If `generation-ship/art/source/<style>/` contains painted images (portraits, board art, frames), use them. Otherwise use the palette fallbacks described below. **Never invent text inside textures:** names and rules text are set as real text objects or omitted.

## What to build (scripts in `generation-ship/tools/blender/`)
1. **`common.py`**: shared helpers.
   - Millimetre units, so the scene is real-scale.
   - Load `boards.json`; convert units to mm (scale 100/180); flip Y, because SVG y points down.
   - Build a mesh from a 2D polygon, extruded by a thickness.
   - Bevel, materials, and a style loader.
2. **`style_presets.py`**: one preset per direction: `grimdark`, `spacepunk`, `newage`, `retro`. Each preset holds:
   - the section-type colours and corner-icon tint,
   - the void colour plus a star texture,
   - hull-plating colour, metalness and roughness,
   - card frame colours,
   - Wall panel material,
   - the Breakthrough token shape: oil lamp / brass gear / clear acrylic crystal / gold starburst.

   Take the colours from `ART_BRIEF.md`. Use procedural materials (noise or Voronoi for rust, brushed metal, frosted acrylic, halftone) when no painted texture exists.
3. **`board_tile.py`**: a ship board as a real punched tile.
   - **Tile body:** 2 mm greyboard, extruded from `outline`. Visible grey core on the edges, a slight edge bevel, a matte printed top.
   - **Sections:** each section polygon as a separate printed area, with its type colour or its clipped painted art. Section borders 0.6 mm, printed.
   - **Print layout:**
     - the section ID and a type icon in a corner;
     - the hull-side sections marked;
     - the void crescent printed on the same tile (it is part of the tile), with stars.
   - **Option:** `--board A|B|C|D`.
4. **`card.py`**: a 63 × 88 mm card, 0.3 mm thick, with 3 mm rounded corners. Follow the template in `ART_BRIEF.md`:
   - name bar 0–9 mm,
   - **portrait zone 9–44 mm**,
   - text zone 44–72 mm,
   - **Legacy band 72–88 mm**.

   Use real text objects for the name, cost and Legacy. Default card: R024 "Ostra Vell"; take its effect, Reign and Legacy text from `data/people.json`.
5. **`wall.py`**: the **Wall of Leaders as a dual-layer board**. This is the most important piece.
   - **Size:** tri-fold, three panels of four slots (12 slots), each panel about 290 × 120 mm. Two 2 mm layers.
   - **Top layer cutouts, per slot:**
     - a **frame window** over the card's portrait zone (about 55 × 33 mm, in the style's frame shape: arch / porthole / hexagon; Retro: the master window, 55 × 40 mm, from `art/templates/retro/`),
     - a **plaque window** over the Legacy band (about 59 × 14 mm).

     Print a frame around each window, and a slot number.
   - **Slots:** a slit in the top edge of each slot; the card slides down between the layers and seats so its portrait and Legacy line up with the windows. Add a thumb notch at the top of each slit.
   - **Scene fill:** slot three leader cards fully (portraits visible through the frames, Legacy visible through the plaques). Show one more card **half-inserted**, sticking up out of its slit. Put a Breakthrough token on one frame. Leave the remaining slots empty, showing the backing layer.
   - **Cut-away view:** also produce a version cut along one slot, showing the layer sandwich with the card between.
6. **`tokens.py`**:
   - threat tokens: Glitch (triangle), Fault (square), Failure (hexagon), each 16 mm;
   - Crew meeples (wood);
   - Decay markers;
   - four house-colour influence discs (wood).
7. **`scene_table.py`**: the hero table scene.
   - **Boards:** the `pair` layout (boards A and B docked, from `layouts.pair`).
   - **Pieces on the table:**
     - tokens on a few sections,
     - a fanned hand of 5 cards,
     - a deck,
     - the folded-out Wall behind.
   - **Surface:** a dark wood or felt table.
   - **Lighting:** an HDRI if available (Poly Haven via Blender MCP, or any studio HDRI), otherwise a three-point light rig.
   - **Cameras:**
     - `hero` (three-quarter view, 35 mm lens, shallow depth of field),
     - `top` (orthographic, straight down),
     - `wall_close` (the Wall front-on, 50 mm lens),
     - `wall_cutaway`.
8. **`render_all.py`**: renders every style × every camera.
   - Output to `generation-ship/art/renders/<style>/<camera>.png`.
   - Settings: Cycles, 1920 × 1080; 128 samples with denoising for previews, 512 for finals. Expose `--samples` and `--threads`; I may want to limit CPU use.
   - Also write a contact sheet, `generation-ship/art/renders/contact_sheet.png`: 4 styles × 4 cameras.

## How to work
- Start with **one style (retro)** and **one camera (wall_close)**. Show me the render before building the rest; the Wall is the riskiest piece.
- Then do the board tile, then the table scene, then the other three styles.
- **Never change the board outline or docking profile:** boards must still fit together. Interior art may follow section borders like rooms seen from above.
- Every script runs headless:

  ```
  blender --background --python tools/blender/render_all.py -- --style retro --camera wall_close --samples 64
  ```

  Re-running must reproduce the same image.
- After each render, look at the PNG yourself and check:
  - windows line up with the card's portrait and Legacy;
  - text is readable;
  - section types are distinguishable;
  - tokens stay legible on the art.

  Fix any problem before showing me.
- **Commit:**
  - **Commit** the scripts, and small preview renders under 1 MB each, to the branch above.
  - **Don't commit** full-resolution renders or downloaded HDRIs/textures. Add them to `.gitignore` under `generation-ship/art/renders/full/` and `generation-ship/art/cache/`.
- Tell me which painted assets would most improve the renders (from the `ART_BRIEF.md` prompts), so I can generate them and drop them into `art/source/<style>/`.

## Done looks like
For each of the four styles:
- a `wall_close` render,
- a `wall_cutaway` render,
- a `top` view of board A,
- a `hero` table shot,

all real-scale and physically plausible as a manufactured product. Plus the contact sheet, and a short note on any manufacturing concerns you noticed (window sizes, layer thickness, card fit tolerance, about 0.5 mm per side).
