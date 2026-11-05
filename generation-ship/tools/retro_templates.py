"""Retro Space master geometry: one window shape shared by the people card and the Wall of Leaders.

    python3 tools/retro_templates.py            -> art/templates/retro/*.svg and *_guide.png
    python3 tools/retro_templates.py --stamp art/source/retro/card_frame_v2a.png card
                                                -> ..._exact.png: the master windows re-cut on top

Every measurement is in millimetres and lives here, so the card frame, the Wall panel and the
layout files cannot drift apart:
- the card is 63 x 88 mm (3 mm bleed: 69 x 94 mm);
- the portrait window is the card frame's wide arch, 55 x 40 mm, at x 4-59, y 9-49;
- the Legacy plaque is 59 x 16 mm (18 % of the card height), at x 2-61, y 70.5-86.5;
- the guilds + effect text panel shrinks to y 51-69 (18 mm);
- the Wall cuts exactly the same two windows over every slotted card.

The guide PNGs are flat layout drawings. They are sent with the prompt to /v1/images/edits so the
painted frame keeps the windows where the layout needs them. --stamp re-cuts the windows exactly,
as a die-cut or a layout program would.
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "art" / "templates" / "retro"

# --- master shapes (mm) -------------------------------------------------------------------------
WIN_W, WIN_H = 55.0, 40.0          # the master window
WIN_SIDE = 18.0                    # where the straight sides end and the arch starts (from the top)
WIN_FOOT_R = 3.0                   # bottom corner radius
PLAQUE_W, PLAQUE_H, PLAQUE_R = 59.0, 16.0, 4.0

CARD_W, CARD_H, BLEED = 63.0, 88.0, 3.0
CARD_WIN = (4.0, 9.0)              # top-left of the window on the card
CARD_PLAQUE = (2.0, 70.5)          # top-left of the Legacy plaque on the card
CARD_NAME = (4.0, 1.5, 55.0, 6.5)  # name bar x, y, w, h
CARD_TEXT = (4.0, 51.0, 55.0, 18.0)  # guilds + effect text panel x, y, w, h

WALL_W, WALL_H = 290.0, 120.0      # one panel of the tri-fold Wall
WALL_SLOTS = 4
WALL_CARD_TOP = 8.0                # a slotted card's top edge on the panel
NOTCH_R = 8.0                      # thumb notch at the top edge of each slot

# Retro palette (ART_BRIEF Part 2 D)
TEAL, TANGERINE, CREAM, TURQ, CHROME = "#0F3A48", "#E8603A", "#FBEFD6", "#3AB0A8", "#C9D1D6"


def window_path(x, y, s=1.0):
    """The master window as an SVG path, top-left at (x, y) mm, scaled by s (px per mm)."""
    w, h, k, r = WIN_W * s, WIN_H * s, WIN_SIDE * s, WIN_FOOT_R * s
    x, y = x * s, y * s
    return (f"M{x + r:.2f},{y + h:.2f} L{x + w - r:.2f},{y + h:.2f} Q{x + w:.2f},{y + h:.2f} {x + w:.2f},{y + h - r:.2f} "
            f"L{x + w:.2f},{y + k:.2f} C{x + w:.2f},{y + k * 0.45:.2f} {x + w * 0.70:.2f},{y + s * 0.6:.2f} {x + w / 2:.2f},{y:.2f} "
            f"C{x + w * 0.30:.2f},{y + s * 0.6:.2f} {x:.2f},{y + k * 0.45:.2f} {x:.2f},{y + k:.2f} "
            f"L{x:.2f},{y + h - r:.2f} Q{x:.2f},{y + h:.2f} {x + r:.2f},{y + h:.2f} Z")


def window_points(x, y, s=1.0, steps=48):
    """The same outline as a polygon (for drawing with PIL), in px."""
    def cubic(p0, p1, p2, p3):
        return [tuple((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t ** 2 * c + t ** 3 * d
                      for a, b, c, d in zip(p0, p1, p2, p3)) for t in (i / steps for i in range(steps + 1))]

    def quad(p0, p1, p2):
        return [tuple((1 - t) ** 2 * a + 2 * (1 - t) * t * b + t ** 2 * c for a, b, c in zip(p0, p1, p2))
                for t in (i / 12 for i in range(13))]
    w, h, k, r = WIN_W, WIN_H, WIN_SIDE, WIN_FOOT_R
    pts = [(r, h), (w - r, h)] + quad((w - r, h), (w, h), (w, h - r))
    pts += cubic((w, k), (w, k * 0.45), (w * 0.70, 0.6), (w / 2, 0))
    pts += cubic((w / 2, 0), (w * 0.30, 0.6), (0, k * 0.45), (0, k))
    pts += quad((0, h - r), (0, h), (r, h))
    return [((x + px) * s, (y + py) * s) for px, py in pts]


def rrect(x, y, w, h, r):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>'


def wall_slot_origins():
    """Top-left of a slotted card on the Wall panel, per slot."""
    pitch = WALL_W / WALL_SLOTS
    return [(pitch * (i + 0.5) - CARD_W / 2, WALL_CARD_TOP) for i in range(WALL_SLOTS)]


def write_svgs():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "master_window.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIN_W}mm" height="{WIN_H}mm" viewBox="0 0 {WIN_W} {WIN_H}">'
        f'<path d="{window_path(0, 0)}" fill="{TEAL}"/></svg>\n')
    b = BLEED
    cx, cy = CARD_WIN
    px, py = CARD_PLAQUE
    (OUT / "card_template.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{CARD_W + 2 * b}mm" height="{CARD_H + 2 * b}mm" '
        f'viewBox="{-b} {-b} {CARD_W + 2 * b} {CARD_H + 2 * b}">\n'
        f'<rect x="{-b}" y="{-b}" width="{CARD_W + 2 * b}" height="{CARD_H + 2 * b}" fill="{TANGERINE}"/>\n'
        f'<rect x="0" y="0" width="{CARD_W}" height="{CARD_H}" rx="3" fill="none" stroke="#000" stroke-width="0.2" stroke-dasharray="1 1"/>\n'
        f'<g fill="{CREAM}">{rrect(*CARD_NAME, 2)}{rrect(*CARD_TEXT, 2)}</g>\n'
        f'<path id="portrait" d="{window_path(cx, cy)}" fill="{TEAL}"/>\n'
        f'<g id="legacy" fill="{TEAL}">{rrect(px, py, PLAQUE_W, PLAQUE_H, PLAQUE_R)}</g>\n</svg>\n')
    slots = "".join(f'<path d="{window_path(x + cx, y + cy)}"/>{rrect(x + px, y + py, PLAQUE_W, PLAQUE_H, PLAQUE_R)}'
                    for x, y in wall_slot_origins())
    notches = "".join(f'<circle cx="{x + CARD_W / 2}" cy="0" r="{NOTCH_R}"/>' for x, y in wall_slot_origins())
    (OUT / "wall_panel_template.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WALL_W}mm" height="{WALL_H}mm" viewBox="0 0 {WALL_W} {WALL_H}">\n'
        f'<rect width="{WALL_W}" height="{WALL_H}" rx="8" fill="{TANGERINE}"/>\n'
        f'<g id="windows" fill="{TEAL}">{slots}</g>\n<g id="thumb_notches" fill="#fff">{notches}</g>\n</svg>\n')


# --- raster guides (for /v1/images/edits) and the exact re-cut ----------------------------------
CARD_PX = 16       # px per mm: 69 x 94 mm -> 1104 x 1504 px
WALL_PX = 8        # px per mm: 290 x 120 mm -> 2320 x 960 px


def draw_windows(d, s, origins, fill, outline=None, width=0):
    for ox, oy in origins:
        d.polygon(window_points(ox + CARD_WIN[0], oy + CARD_WIN[1], s), fill=fill, outline=outline, width=width)
        x, y = (ox + CARD_PLAQUE[0]) * s, (oy + CARD_PLAQUE[1]) * s
        d.rounded_rectangle((x, y, x + PLAQUE_W * s, y + PLAQUE_H * s), PLAQUE_R * s, fill=fill, outline=outline, width=width)


def card_guide():
    s, b = CARD_PX, BLEED
    im = Image.new("RGB", (round((CARD_W + 2 * b) * s), round((CARD_H + 2 * b) * s)), TANGERINE)
    d = ImageDraw.Draw(im)
    for x, y, w, h in (CARD_NAME, CARD_TEXT):
        d.rounded_rectangle(((x + b) * s, (y + b) * s, (x + b + w) * s, (y + b + h) * s), 2 * s, fill=CREAM, outline=CHROME, width=s)
    draw_windows(d, s, [(b, b)], TEAL, CHROME, s)
    return im


def wall_guide():
    s = WALL_PX
    im = Image.new("RGB", (round(WALL_W * s), round(WALL_H * s)), TANGERINE)
    d = ImageDraw.Draw(im)
    draw_windows(d, s, wall_slot_origins(), TEAL, CHROME, s)
    for x, _ in wall_slot_origins():
        c = (x + CARD_W / 2) * s
        d.ellipse((c - NOTCH_R * s, -NOTCH_R * s, c + NOTCH_R * s, NOTCH_R * s), fill=TEAL)
    return im


def stamp(path, kind):
    """Re-cut the master windows (flat teal) into a generated image, scaled to its size.

    The guides draw a 1 mm chrome line just inside each window edge, and the painted bezel sits
    there, so the flat teal is cut 1 mm inside the master shape and the bezel is kept."""
    im = Image.open(path).convert("RGB")
    if kind == "card":
        s = im.width / (CARD_W + 2 * BLEED)
        origins = [(BLEED, BLEED)]
    else:
        s = im.width / WALL_W
        origins = wall_slot_origins()
    mask = Image.new("L", im.size, 0)
    draw_windows(ImageDraw.Draw(mask), s, origins, 255)
    mask = mask.filter(ImageFilter.MinFilter(2 * round(s) + 1))   # erode by 1 mm
    im.paste(TEAL, mask=mask)
    out = Path(path).with_name(Path(path).stem + "_exact.png")
    im.save(out)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stamp", nargs=2, metavar=("IMAGE", "card|wall"))
    a = ap.parse_args()
    if a.stamp:
        print("wrote", stamp(*a.stamp))
        return
    write_svgs()
    card_guide().save(OUT / "card_guide.png")
    wall_guide().save(OUT / "wall_guide.png")
    for f in sorted(OUT.iterdir()):
        print("wrote", f.relative_to(ROOT))


if __name__ == "__main__":
    main()
