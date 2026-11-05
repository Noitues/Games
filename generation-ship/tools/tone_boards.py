"""Tone down the Retro board art for the table, without an image model.

    python3 tools/tone_boards.py   -> art/source/retro/board_<x>_v2[_2]_toned.png

Two passes, both driven by data/boards.json (the art was painted over the guides from
tools/retro_templates.py, so the section polygons line up with it):
1. colour: less saturation and a little less contrast, so the pieces are the brightest thing;
2. calm floors: in each section's centre, the painted props fade into the floor colour (a strong
   blur blended in through a feathered mask), leaving walls and room detail near the borders. This
   is the brief's "about 40 % of each section calm" for token space.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import retro_templates as rt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "art" / "source" / "retro"
SATURATION = 0.70        # 1 = unchanged
CONTRAST = 0.90
BRIGHTNESS = 1.03
CALM_CORE = 0.62         # each section's calm area: its polygon shrunk to this size about its centre
CALM_STRENGTH = 0.78     # how far the props fade in the calm area (1 = fully into the blur)
CALM_BLUR = 22           # px: the floor colour the props fade into
FEATHER = 34             # px: the soft edge of the calm area


def calm_mask(size, board, frame):
    s, ox, oy = frame
    m = Image.new("L", size, 0)
    d = ImageDraw.Draw(m)
    for sec in board["sections"]:
        cx, cy = sec["center"]
        pts = [(ox + s * (cx + CALM_CORE * (x - cx)), oy + s * (cy + CALM_CORE * (y - cy))) for x, y in sec["poly"]]
        d.polygon(pts, fill=int(255 * CALM_STRENGTH))
    return m.filter(ImageFilter.GaussianBlur(FEATHER))


def tone(path, board, frame):
    im = Image.open(path).convert("RGB")
    im = ImageEnhance.Color(im).enhance(SATURATION)
    im = ImageEnhance.Contrast(im).enhance(CONTRAST)
    im = ImageEnhance.Brightness(im).enhance(BRIGHTNESS)
    floor = im.filter(ImageFilter.GaussianBlur(CALM_BLUR))
    return Image.composite(floor, im, calm_mask(im.size, board, frame))


def main():
    data = json.loads((ROOT / "data" / "boards.json").read_text())
    frame = rt.board_frame(data)
    for b in data["boards"]:
        for suffix in ("", "_2"):
            src = SRC / f"board_{b['id'].lower()}_v2{suffix}.png"
            if src.exists():
                out = src.with_name(src.stem + "_toned.png")
                tone(src, b, frame).save(out)
                print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
