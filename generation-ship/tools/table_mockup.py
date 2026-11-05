"""A mid-game table mock-up pieced together from the Retro concept art (no image model involved).

    python3 tools/table_mockup.py   -> art/mockups/retro_table_midgame.png (+ _preview.png)

Everything is placed to scale (6 px per mm) from the game's own data: two boards docked in the
"pair" layout of data/boards.json, the Wall of Leaders with retired leaders in its master windows,
the Dawn / Day / Dusk conveyor, two house boards with hands, and tokens on sections and in the
supply. The state shown is illustrative, not a simulated game. Uses Pillow; one core.
"""
import json
import math
import random
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import retro_templates as rt  # noqa: E402
import conveyor_mockups  # noqa: E402
import house_boards  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "art" / "source" / "retro"
OUT = ROOT / "art" / "mockups"
PX = 6                                # px per mm on the table
TABLE = (900, 640)                    # mm
FONT_B = str(ROOT / "art" / "fonts" / "Righteous-Regular.ttf")          # style guide: titles
FONT = str(ROOT / "art" / "fonts" / "JosefinSans[wght].ttf")            # style guide: body text
rng = random.Random(7)                # fixed: the mock-up is reproducible


def jfont(px, weight="Medium"):
    """Josefin Sans is a variable font: pick a weight, or Pillow uses its thinnest."""
    f = ImageFont.truetype(FONT, px)
    try:
        f.set_variation_by_name(weight)
    except (OSError, ValueError):
        pass
    return f


def mm(v):
    return round(v * PX)


def font(path, size_mm):
    return ImageFont.truetype(path, max(8, round(size_mm * PX * 4)))   # pieces are drawn at 4x scale


# --- cut-outs ------------------------------------------------------------------------------------
def cutout(path, thresh=38):
    """A token on a plain cream background -> RGBA, background flood-filled away from the corners."""
    im = Image.open(path).convert("RGB")
    key = (255, 0, 255)
    work = im.copy()
    for c in ((0, 0), (im.width - 1, 0), (0, im.height - 1), (im.width - 1, im.height - 1)):
        ImageDraw.floodfill(work, c, key, thresh=thresh)
    alpha = Image.eval(ImageChops.difference(work, Image.new("RGB", im.size, key)).convert("L"), lambda v: 255 if v > 0 else 0)
    alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
    out = im.convert("RGBA")
    out.putalpha(alpha)
    return out.crop(alpha.getbbox())


def split_row(rgba):
    """The influence sheet -> one RGBA per token (columns separated by empty alpha)."""
    a = rgba.getchannel("A")
    cols = [any(a.getpixel((x, y)) for y in range(0, a.height, 4)) for x in range(a.width)]
    parts, start = [], None
    for x, on in enumerate(cols + [False]):
        if on and start is None:
            start = x
        elif not on and start is not None:
            if x - start > 20:
                p = rgba.crop((start, 0, x, rgba.height))
                parts.append(p.crop(p.getchannel("A").getbbox()))
            start = None
    return parts


def sized(im, w_mm):
    w = mm(w_mm)
    return im.resize((w, max(1, round(im.height * w / im.width))), Image.LANCZOS)


# --- people cards ---------------------------------------------------------------------------------
def window_mask(size, s, origins, erode=True):
    m = Image.new("L", size, 0)
    d = ImageDraw.Draw(m)
    for ox, oy in origins:
        d.polygon(rt.window_points(ox + rt.CARD_WIN[0], oy + rt.CARD_WIN[1], s), fill=255)
    return m.filter(ImageFilter.MinFilter(2 * round(s) + 1)) if erode else m


def plaque_box(ox, oy, s):
    x, y = (ox + rt.CARD_PLAQUE[0]) * s, (oy + rt.CARD_PLAQUE[1]) * s
    return (x, y, x + rt.PLAQUE_W * s, y + rt.PLAQUE_H * s)


def portrait_into(base, portrait, s, origin, lift=0.18):
    """Fill the master window at origin (mm) with a portrait, cropped to cover it."""
    x0, y0 = (origin[0] + rt.CARD_WIN[0]) * s, (origin[1] + rt.CARD_WIN[1]) * s
    w, h = rt.WIN_W * s, rt.WIN_H * s
    p = Image.open(portrait).convert("RGB")
    k = max(w / p.width, h / p.height) * 1.08
    p = p.resize((round(p.width * k), round(p.height * k)), Image.LANCZOS)
    cx = (p.width - w) / 2
    cy = (p.height - h) * lift
    layer = Image.new("RGB", base.size)
    layer.paste(p.crop((round(cx), round(cy), round(cx + w), round(cy + h))), (round(x0), round(y0)))
    base.paste(layer, mask=window_mask(base.size, s, [origin]))


def wrap(d, text, f, width):
    lines, line = [], ""
    for word in text.split():
        t = (line + " " + word).strip()
        if d.textlength(t, font=f) <= width:
            line = t
        else:
            lines.append(line)
            line = word
    return lines + [line]


def people_card(person, portrait, name):
    """A finished people card at 16 px/mm (no bleed), from card_frame_v3b_exact."""
    s, b = rt.CARD_PX, rt.BLEED
    im = Image.open(SRC / "card_frame_v3b_exact.png").convert("RGB")
    portrait_into(im, portrait, s, (b, b))
    im = im.crop((b * s, b * s, (b + rt.CARD_W) * s, (b + rt.CARD_H) * s))
    d = ImageDraw.Draw(im)
    teal, cream = rt.TEAL, rt.CREAM
    nx, ny, nw, nh = rt.CARD_NAME
    d.text(((nx + 2) * s, (ny + nh / 2) * s), name, fill=teal, font=ImageFont.truetype(FONT_B, round(3.4 * s)), anchor="lm")
    d.text(((nx + nw - 2) * s, (ny + nh / 2) * s), str(person["cost"]), fill=rt.TANGERINE, font=ImageFont.truetype(FONT_B, round(4 * s)), anchor="rm")
    tx, ty, tw, th = rt.CARD_TEXT
    f = jfont(round(2.3 * s))
    fb = ImageFont.truetype(FONT_B, round(2.3 * s))
    y = (ty + 1.5) * s
    d.text(((tx + 2) * s, y), " · ".join(person["guilds"]), fill=rt.TANGERINE, font=fb)
    y += 3.6 * s
    for line in wrap(d, person["text"], f, (tw - 4) * s)[:2]:
        d.text(((tx + 2) * s, y), line, fill=teal, font=f)
        y += 3 * s
    for line in wrap(d, "Reign: " + person["reign"]["text"], f, (tw - 4) * s)[:2]:
        d.text(((tx + 2) * s, y), line, fill=teal, font=f)
        y += 3 * s
    legacy_text(d, person, plaque_box(0, 0, s), s, cream)
    return round_corners(im, 3 * s)


def legacy_text(d, person, box, s, fill):
    f = jfont(round(2.2 * s))
    x0, y0, x1, y1 = box
    lines = wrap(d, "Legacy: " + person["legacy"]["text"], f, x1 - x0 - 4 * s)[:4]
    y = (y0 + y1) / 2 - len(lines) * 1.4 * s
    for line in lines:
        d.text(((x0 + x1) / 2, y), line, fill=fill, font=f, anchor="mt")
        y += 2.8 * s


def round_corners(im, r):
    im = im.convert("RGBA")
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    im.putalpha(m)
    return im


def card_back():
    s = rt.CARD_PX
    im = Image.open(SRC / "card_back.png").convert("RGB").resize((round((rt.CARD_W + 2 * rt.BLEED) * s), round((rt.CARD_H + 2 * rt.BLEED) * s)))
    im = im.crop((rt.BLEED * s, rt.BLEED * s, (rt.BLEED + rt.CARD_W) * s, (rt.BLEED + rt.CARD_H) * s))
    return round_corners(im, 3 * s)


# --- the Wall --------------------------------------------------------------------------------------
def wall_panel(leaders, first_slot):
    """One Wall panel (8 px/mm) with retired leaders showing through its windows."""
    s = rt.WALL_PX
    im = Image.open(SRC / "wall_panel_v3b_exact.png").convert("RGB")
    d = ImageDraw.Draw(im)
    origins = rt.wall_slot_origins()
    numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
    for i, o in enumerate(origins):
        if i < len(leaders):
            person, portrait = leaders[i]
            portrait_into(im, portrait, s, o)
            legacy_text(d, person, plaque_box(*o, s), s, rt.CREAM)
        cx = (o[0] + rt.CARD_W / 2) * s
        cy = (o[1] + rt.CARD_PLAQUE[1] + rt.PLAQUE_H + 7.5) * s
        d.text((cx, cy), numerals[first_slot + i], fill="#5A3E14", font=ImageFont.truetype(FONT_B, round(4.2 * s)), anchor="mm")
    return round_corners(im, 8 * s)


# --- ship boards ----------------------------------------------------------------------------------
def board_piece(art, d):
    """Board art clipped to the hull outline plus the printed void crescent, as RGBA, and the board
    centre in its pixels."""
    im = Image.open(art).convert("RGB")
    s, ox, oy = rt.board_frame(d)
    m = Image.new("L", im.size, 0)
    dr = ImageDraw.Draw(m)
    dr.polygon([(ox + s * x, oy + s * y) for x, y in d["void_zone"]], fill=255)
    dr.polygon([(ox + s * x, oy + s * y) for x, y in d["outline"]], fill=255)
    out = im.convert("RGBA")
    out.putalpha(m.filter(ImageFilter.GaussianBlur(0.8)))
    return out, (ox, oy), s


# --- composing -------------------------------------------------------------------------------------
def drop(table, piece, xy_mm, angle=0.0, shadow=1.0):
    """Place an RGBA piece centred at xy (mm), rotated by angle (degrees, clockwise), with a shadow."""
    if angle:
        piece = piece.rotate(-angle, resample=Image.BICUBIC, expand=True)
    x, y = mm(xy_mm[0]) - piece.width // 2, mm(xy_mm[1]) - piece.height // 2
    if shadow:
        a = piece.getchannel("A")
        sh = Image.new("RGBA", piece.size, (20, 10, 0, 0))
        sh.putalpha(a.point(lambda v: int(v * 0.55 * shadow)).filter(ImageFilter.GaussianBlur(mm(1.6))))
        off = mm(1.2 * shadow + 0.6)
        table.alpha_composite(sh, (x + off, y + off))
    table.alpha_composite(piece, (x, y))


def table_top():
    w, h = mm(TABLE[0]), mm(TABLE[1])
    base = Image.new("RGB", (w // 4, h // 4), (92, 56, 34))
    px = base.load()
    r = random.Random(3)
    for y in range(base.height):            # walnut: long horizontal grain with slow waves
        g = r.uniform(-14, 14)
        for x in range(base.width):
            v = g + 9 * math.sin(x / 37.0 + y / 5.0) + r.uniform(-5, 5)
            px[x, y] = (int(92 + v), int(56 + v * 0.7), int(34 + v * 0.5))
    base = base.filter(ImageFilter.GaussianBlur(0.7)).resize((w, h), Image.BICUBIC)
    return base.convert("RGBA")


def light(im):
    """A warm lamp over the table: brighter centre, darker corners."""
    w, h = im.size
    v = Image.new("L", (w // 8, h // 8), 0)
    d = ImageDraw.Draw(v)
    for i in range(40):
        k = i / 40
        d.ellipse((v.width * (0.5 - 0.75 * (1 - k)), v.height * (0.48 - 0.85 * (1 - k)),
                   v.width * (0.5 + 0.75 * (1 - k)), v.height * (0.48 + 0.85 * (1 - k))), fill=int(110 + 145 * k))
    v = v.filter(ImageFilter.GaussianBlur(6)).resize((w, h), Image.BICUBIC)
    dark = ImageEnhance.Brightness(im.convert("RGB")).enhance(0.55)
    return Image.composite(im.convert("RGB"), dark, v)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    data = json.loads((ROOT / "data" / "boards.json").read_text())
    people = json.loads((ROOT / "data" / "people.json").read_text())
    remarkable = [p for p in people if p["tier"] != "Common"]
    common = [p for p in people if p["tier"] == "Common"]
    table = table_top()

    # The v3 pieces (art/tokens/sprites, drawn by tools/token_designs.py at 10 px/mm): standing pieces
    # seen from the side, flat ones from above; damage shown by posture.
    sp = ROOT / "art" / "tokens" / "sprites"
    if not sp.exists():
        sys.exit("run tools/token_designs.py first (it draws art/tokens/sprites)")
    tok = {}
    for f in sorted(sp.glob("*.png")):
        im = Image.open(f).convert("RGBA")
        im = im.crop(im.getchannel("A").getbbox())
        tok[f.stem] = im.resize((max(1, round(im.width * PX / 10)), max(1, round(im.height * PX / 10))), Image.LANCZOS)
    influence = [tok[f"influence_{i}"] for i in range(4)]             # blue, red, gold, white

    # Ship: boards A and B in the "pair" layout; board units -> mm (radius 180 units = 100 mm).
    pair = data["layouts"]["pair"]
    U = 100 / 180
    ship_origin = (205, 330)                                            # mm on the table for (0, 0)
    for bid, art in (("A", "board_a_v2_toned.png"), ("B", "board_b_v2_toned.png")):   # tools/tone_boards.py
        piece, (ox, oy), s = board_piece(SRC / art, data)
        piece = piece.resize((round(piece.width * PX * U / s), round(piece.height * PX * U / s)), Image.LANCZOS)
        cx, cy = ox * PX * U / s, oy * PX * U / s                       # board centre inside the piece
        x, y, rot = pair["place"][bid]
        # rotate about the board centre: pad so the centre is the image centre
        pad = round(max(cx, piece.width - cx, cy, piece.height - cy))
        sq = Image.new("RGBA", (2 * pad, 2 * pad))
        sq.alpha_composite(piece, (round(pad - cx), round(pad - cy)))
        drop(table, sq, (ship_origin[0] + x * U, ship_origin[1] + y * U), rot, shadow=0.6)

    def section_xy(sec, bid):
        x, y, rot = pair["place"][bid]
        a = math.radians(rot)
        px_, py_ = sec["center"]
        return (ship_origin[0] + (px_ * math.cos(a) - py_ * math.sin(a) + x) * U,
                ship_origin[1] + (px_ * math.sin(a) + py_ * math.cos(a) + y) * U)

    # Mid-game spread: threats (some damaged, by posture), Crew (one injured), Decay, influence, Isolate.
    state = {
        "A1": ["crew", "crew", "inf0"], "A2": ["fault_flat", "glitch"], "A3": ["inf1", "crew"],
        "A4": ["failure_side", "decay", "crew_injured"], "A5": ["glitch", "inf1", "inf1"], "A6": ["crew", "inf0"],
        "A7": ["glitch", "glitch"], "A8": ["decay_b", "fault", "crew"],
        "B1": ["inf0", "crew", "glitch"], "B2": ["fault", "isolate"], "B3": ["inf1", "crew", "crew_injured"],
        "B4": ["failure_up", "fault", "decay"], "B5": ["crew", "inf0", "inf0"], "B6": ["glitch"],
        "B7": ["crew", "decay_b"], "B8": ["inf1", "failure", "crew"],
    }
    flat = {"glitch", "fault_flat", "decay", "decay_b", "breakthrough"}
    for bid in ("A", "B"):
        board = next(b for b in data["boards"] if b["id"] == bid)
        for sec in board["sections"]:
            items = state.get(sec["id"], [])
            cx, cy = section_xy(sec, bid)
            placed = []
            for i, it in enumerate(items):
                ang = 2 * math.pi * i / max(1, len(items)) + rng.uniform(-0.3, 0.3)
                rad = 0 if len(items) == 1 else 10
                placed.append(((cx + rad * math.cos(ang), cy + rad * math.sin(ang)), it))
            for pos, it in sorted(placed, key=lambda q: q[0][1]):           # back to front
                piece = influence[int(it[3])] if it.startswith("inf") else tok[it]
                spin = rng.uniform(-40, 40) if it in flat else rng.uniform(-3, 3)
                drop(table, piece, pos, spin, shadow=0.5)

    # The Wall of Leaders: two panels of the tri-fold unfolded along the top. Only four portraits exist
    # so far: Ilka, Pell and Ostra are in the conveyor, and Dace has retired to slot I.
    leaders = [(common[5], SRC / "dace.png")]           # Ilka, Pell and Ostra are in the conveyor
    for k, first in enumerate((0, 4)):
        panel = wall_panel(leaders[first:first + 4], first)
        panel = panel.resize((mm(rt.WALL_W), mm(rt.WALL_H)), Image.LANCZOS)
        drop(table, panel, (300 + k * 291, 72), 0, shadow=0.8)
    drop(table, tok["breakthrough"], (300 - 145 + 72.5 * 0.5 + 22, 80), 15, 0.7)    # on slot I, between portrait and plaque

    # The conveyor board (option A, tools/conveyor_mockups.py): leaders with their events tucked behind.
    conv = conveyor_mockups.render_board("A", PX, OUT / "_conveyor_a.png")
    cb = Image.open(conv).convert("RGBA")
    conv.unlink()
    drop(table, cb, (712, 246), 0, shadow=0.8)

    # House boards (typeset by tools/house_boards.py) with hands, along the bottom.
    back = card_back().resize((mm(63), mm(88)), Image.LANCZOS)
    for hx, house, inf in ((560, "galvan", 0), (775, "gardeners", 1)):
        art = Image.open(SRC / f"house_{house}_typeset.png").convert("RGB")
        rows = house_boards.layout(Image.open(SRC / f"house_{house}.png"))["tracks"]
        k = mm(190) / art.width
        hb = round_corners(art, 40).resize((mm(190), mm(127)), Image.LANCZOS)
        top_left = (hx - 95, 440 - 63.5)
        drop(table, hb, (hx, 440), 0, shadow=0.8)
        for row, first in zip(rows, (3, 4)):                          # influence still covering the later sockets
            for sock in row[first:]:
                cx = top_left[0] + (sock[0] + sock[2]) / 2 * k / PX
                cy = top_left[1] + (sock[1] + sock[3]) / 2 * k / PX
                drop(table, influence[inf], (cx, cy - 1), 0, 0.5)
        for j in range(4):                                             # the hand, fanned below
            drop(table, back, (hx - 36 + j * 22, 556 + abs(j - 1.5) * 4), -12 + j * 8, shadow=0.7)

    # The people deck and the supply.
    for j in range(6):
        drop(table, back, (440 - j * 0.4, 585 - j * 0.5), 1.5, shadow=0.4 if j else 0.9)
    supply = [("glitch", 9), ("fault", 6), ("failure", 3), ("crew", 8), ("decay", 6)]
    for i, (n, k) in enumerate(supply):
        heap = sorted(((28 + (i % 2) * 52 + rng.uniform(-11, 11), 40 + (i // 2) * 48 + rng.uniform(-10, 10)) for _ in range(k)), key=lambda q: q[1])
        for j, pos in enumerate(heap):
            name = n if n != "decay" else ("decay", "decay_b")[j % 2]
            drop(table, tok[name], pos, rng.uniform(0, 360) if name in flat else rng.uniform(-4, 4), 0.5)

    final = light(table)
    final.save(OUT / "retro_table_midgame.png", optimize=True)
    final.resize((final.width // 3, final.height // 3), Image.LANCZOS).save(OUT / "retro_table_midgame_preview.png")
    print("wrote", (OUT / "retro_table_midgame.png").relative_to(ROOT), final.size)


if __name__ == "__main__":
    main()
