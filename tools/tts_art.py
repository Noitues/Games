"""Pillow renderers for the Hex-Nexus Tabletop Simulator mod.

Every image here is drawn from data handed in by ``tools/tts_export.py``
(map, roster, config, items). Nothing in this module knows a game number of
its own: change the repo, rebuild, and the art follows.

Geometry: flat-top hexes, axial (q, r), north = negative r, which is the top
of every board image. ``hex_px`` maps a hex to image pixels for a given hex
radius ``R`` (centre to corner).
"""
from __future__ import annotations

import math
import os
import textwrap
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from PIL import Image, ImageDraw, ImageFont

SQRT3 = math.sqrt(3.0)
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

TEAM_COLOURS = {"north": (47, 111, 219), "south": (217, 72, 59)}
TEAM_LIGHT = {"north": (170, 196, 245), "south": (245, 180, 172)}
NEUTRAL_CHIP = (236, 232, 222)
TERRAIN = {"lane": (216, 196, 154), "river": (127, 182, 224), "jungle": (111, 163, 104),
           "base_north": (159, 184, 240), "base_south": (240, 167, 160)}
ROLE_COLOURS = {"Top": (150, 96, 60), "Jungle": (60, 130, 70), "Mid": (120, 80, 170),
                "ADC": (200, 140, 30), "Support": (40, 140, 160)}
ICON_GROUP = {
    "HIT": "damage", "AREA": "damage", "LINE": "damage",
    "MOVE": "move", "DASH": "move", "BLINK": "move",
    "PUSH": "control", "PULL": "control", "SLOW": "control", "ROOT": "control", "DELAY": "control",
    "HEAL": "support", "SHIELD": "support", "HASTE": "support", "REVEAL": "support",
}
GROUP_COLOURS = {"damage": (196, 58, 50), "move": (58, 150, 80), "control": (126, 76, 176),
                 "support": (40, 120, 196)}
TARGET_MARK = {"enemy_champion": "◆", "ally_champion": "✚", "self": "self",
               "prev": "", "enemy_any": "", None: ""}
INK = (30, 30, 34)
PAPER = (246, 242, 232)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


# ----------------------------------------------------------------- geometry
def hex_px(q: int, r: int, R: float) -> Tuple[float, float]:
    """Centre of hex (q, r) relative to the board centre, image axes (y down)."""
    return (1.5 * R * q, SQRT3 * R * (r + q / 2.0))


def hex_corners(cx: float, cy: float, R: float) -> List[Tuple[float, float]]:
    return [(cx + R * math.cos(math.radians(60 * i)), cy + R * math.sin(math.radians(60 * i)))
            for i in range(6)]


def board_extent(R: float, radius: int = 6) -> Tuple[float, float]:
    """Width and height in pixels of a radius-``radius`` flat-top board."""
    return (2 * R * (1.5 * radius + 1), SQRT3 * R * (2 * radius + 1))


def tile_bbox(hexes: Sequence[Tuple[int, int]], R: float) -> Tuple[float, float, float, float]:
    xs, ys = [], []
    for q, r in hexes:
        x, y = hex_px(q, r, R)
        xs += [x - R, x + R]
        ys += [y - SQRT3 * R / 2, y + SQRT3 * R / 2]
    return min(xs), min(ys), max(xs), max(ys)


def edge_key(a, b):
    return (round(a[0], 2), round(a[1], 2)), (round(b[0], 2), round(b[1], 2))


def outline_edges(hexes, R, ox, oy):
    """Outer boundary segments of a set of hexes (edges not shared)."""
    count = {}
    for q, r in hexes:
        cx, cy = hex_px(q, r, R)
        cs = hex_corners(cx + ox, cy + oy, R)
        for i in range(6):
            a, b = cs[i], cs[(i + 1) % 6]
            k = tuple(sorted(edge_key(a, b)))
            count[k] = count.get(k, 0) + 1
    return [k for k, n in count.items() if n == 1]


def text_center(d: ImageDraw.ImageDraw, xy, s: str, f, fill=INK, stroke=0, stroke_fill=None):
    d.text(xy, s, font=f, fill=fill, anchor="mm", stroke_width=stroke,
           stroke_fill=stroke_fill)


def rounded(d, box, r, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def darker(c, f=0.7):
    return tuple(int(v * f) for v in c[:3])


def lighter(c, f=0.5):
    return tuple(int(v + (255 - v) * f) for v in c[:3])


# ------------------------------------------------------------- step labels
def step_label(step: dict) -> Tuple[str, str]:
    """(icon text, parameter text) for one icon step, e.g. ('HIT×2', 'r1 ◆')."""
    ic = step["icon"]
    k, n, rng = step.get("k"), step.get("n"), step.get("range")
    head = ic
    if ic in ("HIT", "AREA", "LINE") and k and k > 1:
        head = f"{ic}×{k}"
    if ic in ("MOVE", "DASH", "BLINK", "PUSH", "PULL", "SLOW", "HEAL", "SHIELD") and n:
        head = f"{ic} {n}"
    if ic == "LINE" and n:
        head += f" →{n}"
    if ic == "ROOT" and step.get("area"):
        head = "ROOT area"
    parts = []
    if rng is not None:
        parts.append(f"r{rng}")
    mark = TARGET_MARK.get(step.get("target"), "")
    if mark:
        parts.append(mark)
    if step.get("target") == "prev":
        parts.append("↳")
    return head, " ".join(parts)


def ability_text(key: str, ab: dict) -> str:
    steps = " → ".join((" ".join(x for x in step_label(s) if x)) for s in ab["steps"])
    return f"{key}  {ab['cost']} AP · CD {ab['cooldown']} · {steps}"


# ------------------------------------------------------------------ tiles
def terrain_colour(h, terrain: Dict[Tuple[int, int], str], base_tiles: Dict[Tuple[int, int], str]):
    if h in base_tiles:
        return TERRAIN["base_" + base_tiles[h]]
    return TERRAIN.get(terrain.get(h, "jungle"), TERRAIN["jungle"])


def render_tile(name: str, hexes, side: str, R: float, ctx: dict, margin: int = 6) -> Image.Image:
    """One hexgroup tile, cropped to its hexes. ``side`` is 'hidden' or 'visible'.

    Visible: every hex outlined, with its terrain, markers and coordinates.
    Hidden: the tile's outline only (Rules 10), in a darker tint, with its name.
    The crop is symmetric around the bounding box, so the image centre is the
    bounding-box centre (the layout relies on that).
    """
    x0, y0, x1, y1 = tile_bbox(hexes, R)
    W, H = int(math.ceil(x1 - x0)) + 2 * margin, int(math.ceil(y1 - y0)) + 2 * margin
    ox, oy = -x0 + margin, -y0 + margin
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    terrain, base_tiles = ctx["terrain"], ctx["base_tiles"]
    for q, r in hexes:
        cx, cy = hex_px(q, r, R)
        col = terrain_colour((q, r), terrain, base_tiles)
        if side == "hidden":
            col = darker(col, 0.55)
        d.polygon(hex_corners(cx + ox, cy + oy, R + 0.8), fill=col + (255,))
    if side == "visible":
        for q, r in hexes:
            cx, cy = hex_px(q, r, R)
            cs = hex_corners(cx + ox, cy + oy, R - 1)
            d.line(cs + [cs[0]], fill=(40, 40, 40, 200), width=2)
            if (q, r) in ctx["lane_dot"]:                # lane-path dot
                d.ellipse((cx + ox - 5, cy + oy + R * 0.45 - 5, cx + ox + 5, cy + oy + R * 0.45 + 5),
                          fill=(120, 80, 40, 230))
            mark = ctx["markers"].get((q, r))
            if mark:
                text_center(d, (cx + ox, cy + oy - R * 0.05), mark, font(int(R * 0.30), True),
                            fill=(20, 20, 20), stroke=2, stroke_fill=(255, 255, 255))
            text_center(d, (cx + ox, cy + oy - R * 0.62), f"{q},{r}", font(int(R * 0.22)),
                        fill=(30, 30, 30))
    else:
        # faint internal hex lines are deliberately absent on the hidden side
        f = font(int(R * 0.26), True)
        cx = sum(hex_px(q, r, R)[0] for q, r in hexes) / len(hexes) + ox
        cy = sum(hex_px(q, r, R)[1] for q, r in hexes) / len(hexes) + oy
        lines = textwrap.wrap(name, 11)
        for i, ln in enumerate(lines):
            text_center(d, (cx, cy + (i - (len(lines) - 1) / 2) * R * 0.34), ln, f,
                        fill=(240, 240, 240), stroke=2, stroke_fill=(20, 20, 20))
        text_center(d, (cx, cy + (len(lines) / 2 + 0.4) * R * 0.34), "HIDDEN", font(int(R * 0.18)),
                    fill=(230, 230, 230))
    for (a, b) in outline_edges(hexes, R, ox, oy):
        d.line([a, b], fill=(15, 15, 15, 255), width=5 if side == "hidden" else 4)
    return img


# ------------------------------------------------------------------- mat
def render_mat(R: float, map_data: dict, versions: dict, size: Tuple[int, int]) -> Image.Image:
    """The table mat under the tiles: frame, compass, faint grid and legend."""
    W, H = size
    img = Image.new("RGB", (W, H), (58, 52, 46))
    d = ImageDraw.Draw(img)
    cx, cy = W / 2, H / 2
    for key in map_data["hexgroups"].values():
        for q, r in key:
            x, y = hex_px(q, r, R)
            cs = hex_corners(cx + x, cy + y, R + 2)
            d.polygon(cs, fill=(30, 28, 26))
    f = font(int(R * 0.45), True)
    text_center(d, (cx, R * 0.55), "NORTH  ↑", f, fill=TEAM_LIGHT["north"])
    text_center(d, (cx, H - R * 0.55), "SOUTH  ↓", f, fill=TEAM_LIGHT["south"])
    small = font(int(R * 0.26))
    text_center(d, (R * 1.9, R * 0.5), "TOP lane: west edge", small, fill=(220, 210, 190))
    text_center(d, (W - R * 1.9, R * 0.5), "BOT lane: east edge", small, fill=(220, 210, 190))
    stamp = versions["stamp"]
    text_center(d, (cx, H - R * 0.18), stamp, font(int(R * 0.2)), fill=(200, 190, 170))
    return img


# ----------------------------------------------------------------- cards
CARD_W, CARD_H = 400, 560


def draw_step_chip(d, x, y, step, maxw):
    head, sub = step_label(step)
    col = GROUP_COLOURS[ICON_GROUP[step["icon"]]]
    fh, fs = font(17, True), font(14)
    w = max(d.textlength(head, font=fh), d.textlength(sub, font=fs) if sub else 0) + 14
    w = min(w, maxw)
    rounded(d, (x, y, x + w, y + 40), 7, col, outline=darker(col), width=2)
    text_center(d, (x + w / 2, y + (12 if sub else 20)), head, fh, fill=(255, 255, 255))
    if sub:
        text_center(d, (x + w / 2, y + 30), sub, fs, fill=(255, 255, 255))
    return w


def render_champion_card(kit: dict, roster_version: str) -> Image.Image:
    img = Image.new("RGB", (CARD_W, CARD_H), PAPER)
    d = ImageDraw.Draw(img)
    rc = ROLE_COLOURS.get(kit["role"], (90, 90, 90))
    d.rectangle((0, 0, CARD_W, 78), fill=rc)
    d.text((16, 10), kit["name"], font=font(32, True), fill=(255, 255, 255))
    d.text((18, 50), kit["role"].upper(), font=font(17, True), fill=lighter(rc, 0.6))
    # HP and Speed badges
    hp, spd = kit["stats"]["hp"], kit["stats"]["speed"]
    for i, (lab, val, col) in enumerate((("HP", hp, (196, 58, 50)), ("SPD", spd, (58, 150, 80)))):
        bx = CARD_W - 150 + i * 72
        d.ellipse((bx, 8, bx + 62, 70), fill=col, outline=(255, 255, 255), width=3)
        text_center(d, (bx + 31, 34), str(val), font(28, True), fill=(255, 255, 255))
        text_center(d, (bx + 31, 58), lab, font(12, True), fill=(255, 255, 255))
    y = 88
    keys = ["L0", "Q", "W", "E", "R"]
    row_h = 78
    for key in keys:
        ab = kit["abilities"][key]
        d.rounded_rectangle((8, y, CARD_W - 8, y + row_h - 6), radius=8, fill=(255, 255, 255),
                            outline=(200, 190, 175), width=2)
        # key badge
        d.rounded_rectangle((14, y + 6, 58, y + row_h - 12), radius=6, fill=INK)
        text_center(d, (36, y + (row_h - 6) / 2), key, font(20 if key == "L0" else 24, True),
                    fill=(255, 255, 255))
        # cost coin and cooldown
        d.ellipse((64, y + 6, 96, y + 38), fill=(235, 196, 60), outline=darker((235, 196, 60)), width=2)
        text_center(d, (80, y + 22), str(ab["cost"]), font(18, True))
        text_center(d, (80, y + 50), f"CD{ab['cooldown']}", font(13, True))
        x = 104
        for s in ab["steps"]:
            if x > CARD_W - 40:
                break
            w = draw_step_chip(d, x, y + 12, s, CARD_W - 16 - x)
            x += w + 6
        y += row_h
    # identity line
    ident = kit.get("identity", "")
    for i, ln in enumerate(textwrap.wrap(ident, 52)[:3]):
        d.text((14, y + 4 + i * 17), ln, font=font(13), fill=(70, 66, 60))
    d.text((14, CARD_H - 22), f"Roster {roster_version}  ·  ◆ enemy champion  "
           f"✚ ally  ↳ same target", font=font(12), fill=(110, 104, 96))
    return img


def render_card_back(title: str, colour) -> Image.Image:
    img = Image.new("RGB", (CARD_W, CARD_H), darker(colour, 0.5))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((16, 16, CARD_W - 16, CARD_H - 16), radius=20, outline=lighter(colour, 0.4),
                        width=6)
    cs = hex_corners(CARD_W / 2, CARD_H / 2 - 20, 90)
    d.polygon(cs, outline=lighter(colour, 0.5), fill=colour)
    text_center(d, (CARD_W / 2, CARD_H / 2 - 20), "HN", font(64, True), fill=(255, 255, 255))
    text_center(d, (CARD_W / 2, CARD_H / 2 + 110), title, font(26, True), fill=(255, 255, 255))
    return img


def render_text_card(title: str, kind: str, cost: Optional[int], effect: str, colour,
                     footer: str) -> Image.Image:
    img = Image.new("RGB", (CARD_W, CARD_H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, CARD_W, 90), fill=colour)
    d.text((16, 12), title, font=font(30, True), fill=(255, 255, 255))
    d.text((18, 56), kind.upper(), font=font(16, True), fill=lighter(colour, 0.6))
    if cost is not None:
        d.ellipse((CARD_W - 86, 10, CARD_W - 14, 82), fill=(235, 196, 60), outline=(255, 255, 255),
                  width=3)
        text_center(d, (CARD_W - 50, 40), str(cost), font(30, True))
        text_center(d, (CARD_W - 50, 68), "AP", font(12, True))
    y = 130
    for ln in textwrap.wrap(effect, 26):
        text_center(d, (CARD_W / 2, y), ln, font(24, True))
        y += 34
    d.text((14, CARD_H - 24), footer, font=font(12), fill=(110, 104, 96))
    return img


def sheet(cards: List[Image.Image], cols: int, rows: int) -> Image.Image:
    """A TTS deck sheet (cols x rows, at most 10 x 7). Unused slots stay blank."""
    assert cols <= 10 and rows <= 7 and len(cards) <= cols * rows
    w, h = cards[0].size
    out = Image.new("RGB", (w * cols, h * rows), (0, 0, 0))
    for i, c in enumerate(cards):
        out.paste(c, ((i % cols) * w, (i // cols) * h))
    return out


# ----------------------------------------------------------------- tokens
def disc(size: int, fill, rim, rim_w: int) -> Tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((2, 2, size - 3, size - 3), fill=rim)
    d.ellipse((2 + rim_w, 2 + rim_w, size - 3 - rim_w, size - 3 - rim_w), fill=fill)
    return img, d


def render_standee(kit: dict, team: str, size: int = 256) -> Image.Image:
    rc = ROLE_COLOURS.get(kit["role"], (90, 90, 90))
    img, d = disc(size, lighter(rc, 0.35), TEAM_COLOURS[team], 22)
    initials = kit["name"][:2]
    text_center(d, (size / 2, size / 2 - 14), initials, font(int(size * 0.34), True),
                fill=(255, 255, 255), stroke=4, stroke_fill=darker(rc, 0.5))
    text_center(d, (size / 2, size / 2 + 52), kit["name"], font(int(size * 0.11), True),
                fill=(255, 255, 255), stroke=3, stroke_fill=(20, 20, 20))
    return img


def render_structure(team: str, label: str, hp: int, floor: int, size: int = 256) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cs = hex_corners(size / 2, size / 2, size / 2 - 4)
    d.polygon(cs, fill=darker(TEAM_COLOURS[team], 0.6), outline=TEAM_LIGHT[team])
    d.polygon(hex_corners(size / 2, size / 2, size / 2 - 22), fill=TEAM_COLOURS[team])
    text_center(d, (size / 2, size / 2 - 30), label, font(int(size * 0.17), True), fill=(255, 255, 255))
    text_center(d, (size / 2, size / 2 + 40), f"start {hp} · floor {floor}",
                font(int(size * 0.075), True), fill=(255, 255, 255))
    return img


def render_monster(label: str, hp: int, note: str, size: int = 256) -> Image.Image:
    img, d = disc(size, (92, 74, 60), (40, 32, 26), 16)
    text_center(d, (size / 2, size / 2 - 24), label, font(int(size * 0.13), True), fill=(255, 238, 200))
    text_center(d, (size / 2, size / 2 + 26), f"{hp} HP", font(int(size * 0.11), True),
                fill=(255, 238, 200))
    text_center(d, (size / 2, size / 2 + 62), note, font(int(size * 0.07)), fill=(230, 220, 200))
    return img


def render_chip(colour, size: int = 160) -> Image.Image:
    img, d = disc(size, colour, darker(colour, 0.75), 10)
    for i in range(8):
        a = math.radians(i * 45)
        x, y = size / 2 + math.cos(a) * size * 0.40, size / 2 + math.sin(a) * size * 0.40
        d.ellipse((x - 9, y - 9, x + 9, y + 9), fill=(255, 255, 255))
    d.ellipse((size * 0.28, size * 0.28, size * 0.72, size * 0.72), outline=darker(colour, 0.6), width=4)
    return img


def render_marker(label: str, colour, size: int = 160) -> Image.Image:
    img, d = disc(size, colour, (20, 20, 20), 8)
    text_center(d, (size / 2, size / 2), label, font(int(size * 0.22), True), fill=(255, 255, 255),
                stroke=2, stroke_fill=(0, 0, 0))
    return img


# -------------------------------------------------------------- dashboards
def render_dashboard(team: str, team_label: str, track_positions: int, slot_px: Tuple[int, int],
                     notes: List[str], versions: dict, px_per_unit: float,
                     layout: dict) -> Image.Image:
    """Team dashboard: the cooldown track (``track_positions`` .. 0), the AP
    pool, the buff-card row and the reminders. ``layout`` holds the pixel
    boxes the exporter also turns into snap points and zones."""
    W, H = layout["size"]
    col = TEAM_COLOURS[team]
    img = Image.new("RGB", (W, H), darker(col, 0.35))
    d = ImageDraw.Draw(img)
    d.rectangle((6, 6, W - 7, H - 7), outline=lighter(col, 0.3), width=6)
    d.text((24, 16), f"{team_label} · {team.upper()}", font=font(40, True), fill=(255, 255, 255))
    d.text((24, 64), "COOLDOWN TRACK — shift every card down 1 in Upkeep; 0 = in hand",
           font=font(22, True), fill=lighter(col, 0.6))
    for pos, box in layout["slots"].items():
        x0, y0, x1, y1 = box
        d.rounded_rectangle(box, radius=16, fill=darker(col, 0.55), outline=lighter(col, 0.4), width=4)
        text_center(d, ((x0 + x1) / 2, y0 + 36), str(pos) if pos else "0 · HAND",
                    font(44 if pos else 30, True), fill=(255, 255, 255))
        sub = layout["slot_notes"].get(pos, "")
        for i, ln in enumerate(textwrap.wrap(sub, 14)):
            text_center(d, ((x0 + x1) / 2, y1 - 70 + i * 26), ln, font(20), fill=lighter(col, 0.7))
    x0, y0, x1, y1 = layout["pool"]
    d.rounded_rectangle(layout["pool"], radius=24, fill=(40, 40, 40), outline=(235, 196, 60), width=6)
    text_center(d, ((x0 + x1) / 2, y0 + 34), "AP POOL", font(34, True), fill=(235, 196, 60))
    text_center(d, ((x0 + x1) / 2, y1 - 30), "reset to base in Upkeep", font(20), fill=(220, 220, 220))
    x0, y0, x1, y1 = layout["buffs"]
    d.rounded_rectangle(layout["buffs"], radius=16, fill=darker(col, 0.55), outline=lighter(col, 0.4),
                        width=4)
    text_center(d, ((x0 + x1) / 2, y0 + 28), "BUFF / ITEM CARDS IN HAND", font(24, True),
                fill=(255, 255, 255))
    y = layout["notes_y"]
    for n in notes:
        d.text((28, y), "• " + n, font=font(22), fill=(235, 235, 235))
        y += 30
    return img


def render_round_track(rows: List[dict], versions: dict, layout: dict) -> Image.Image:
    """Round tracker: one row per round with priority, spawns, wave size,
    decay, kill reward, death timer and objective spawns."""
    W, H = layout["size"]
    img = Image.new("RGB", (W, H), (44, 40, 36))
    d = ImageDraw.Draw(img)
    d.text((20, 12), "ROUND TRACKER", font=font(38, True), fill=(255, 255, 255))
    heads = ["Rnd", "Prio", "Waves", "Decay", "Kill (Baron)", "Death", "Monsters"]
    xs = layout["cols"]
    for x, h in zip(xs, heads):
        d.text((x, 64), h, font=font(22, True), fill=(235, 196, 60))
    for row in rows:
        y0, y1 = layout["rows"][row["round"]]
        shade = (60, 55, 50) if row["round"] % 2 else (52, 48, 44)
        d.rectangle((10, y0, W - 10, y1), fill=shade)
        vals = [str(row["round"]), row["prio"], row["waves"], row["decay"], row["kill"],
                row["death"], row["monsters"]]
        for x, v in zip(xs, vals):
            d.text((x, y0 + 8), v, font=font(22, True if x == xs[0] else False), fill=(240, 240, 240))
    d.text((20, H - 40), versions["stamp"], font=font(18), fill=(190, 180, 160))
    return img


def save(img: Image.Image, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, optimize=True)
