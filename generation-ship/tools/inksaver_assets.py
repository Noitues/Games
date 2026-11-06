"""Ink-saver versions of the Retro frames for the print-and-play kit (print/assets/).

Until there are portraits and event pictures, their windows print as solid dark teal: a lot of ink
for nothing. This makes:
- card_frame_inksaver.png: the people frame with a pale portrait window;
- event_frame_inksaver.png: the event frame with a pale picture window, then washed to ~35 % ink;
- card_back_inksaver.png: the card back washed to ~30 % ink;
- wall_panel_inksaver.png: the Wall panel with its cut-outs (windows, plaques, thumb notches) white,
  since they are cut away anyway.
The art itself (art/source/retro) is not changed.

    python3 tools/inksaver_assets.py
"""
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "art" / "source" / "retro"
OUT = ROOT / "print" / "assets"
PALE = (246, 240, 226)
CARD_PX = 16  # px per mm, cards include 3 mm bleed
WALL_PX = 8   # px per mm on the Wall panel


def fill(im, mm_points, colour, px, bleed=0.0, thresh=60):
    for x, y in mm_points:
        ImageDraw.floodfill(im, (round((x + bleed) * px), round((y + bleed) * px)), colour, thresh=thresh)
    return im


def wash(im, ink):
    """Keep `ink` of the ink: every channel moves toward white."""
    return im.point(lambda v: round(255 - (255 - v) * ink))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rgb = lambda f: Image.open(SRC / f).convert("RGB")
    # people: portrait window 49 x 40 at (11, 9)
    fill(rgb("card_frame_v4a_exact.png"), [(35.5, 29)], PALE, CARD_PX, 3).save(OUT / "card_frame_inksaver.png")
    # events: picture window 55 x 30 at (4, 4)
    ev = fill(rgb("event_frame_b.png"), [(31.5, 19)], PALE, CARD_PX, 3)
    wash(ev, 0.35).save(OUT / "event_frame_inksaver.png")
    wash(rgb("card_back.png"), 0.3).save(OUT / "card_back_inksaver.png")
    # Wall: per slot, the window, the plaque and the thumb notch are cut away
    wall = rgb("wall_panel_v4b_exact.png")
    pts = [(36.25 + 72.5 * i, y) for i in range(4) for y in (37.0, 82.5, 2.0)]
    fill(wall, pts, (255, 255, 255), WALL_PX).save(OUT / "wall_panel_inksaver.png")
    print("wrote", ", ".join(p.name for p in sorted(OUT.glob("*inksaver.png"))))


if __name__ == "__main__":
    main()
