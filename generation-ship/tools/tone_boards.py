"""Tone down the Retro board art for the table, without an image model.

    python3 tools/tone_boards.py   -> art/source/retro/board_<x>_v2[_2]_toned.png

Passes, all driven by data/boards.json (the art was painted over the guides from
tools/retro_templates.py, so the section polygons line up with it). The void crescent is left as
painted (designer, 2026-11-05: "void space is good").
1. details: inside the hull, every painted detail takes its colour from the floor around it (its
   own colour mostly goes) and loses about half its light-dark contrast, so props read as shading
   of the room colour rather than as objects competing with the pieces;
2. wash: the section colours move a little towards cream and lose saturation;
3. borders: the section borders are redrawn crisp from the data on top;
4. calm floors: in each section's centre, the props fade further into the floor (a strong blur
   blended in through a feathered mask): the brief's "about 40 % of each section calm".
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import retro_templates as rt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "art" / "source" / "retro"
SATURATION = 0.78        # 1 = unchanged (after the wash; keeps the four room hues apart)
CONTRAST = 0.92
BRIGHTNESS = 1.02
DETAIL_CHROMA = 0.22     # how much of a detail's own colour survives (the rest is the floor's)
DETAIL_CONTRAST = 0.55   # how much of a detail's light-dark difference from the floor survives
DETAIL_BLUR = 26         # px: "the floor around it"
WASH = 0.13              # blend towards cream
BORDER_PX = 5            # section borders redrawn crisp from the data (the brief: borders come from data)
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


def hull_mask(size, data, frame):
    s, ox, oy = frame
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).polygon([(ox + s * x, oy + s * y) for x, y in data["outline"]], fill=255)
    return m.filter(ImageFilter.GaussianBlur(1.5))


def mute_details(im):
    """Recolour details from the local floor colour and flatten their contrast (YCbCr)."""
    floor = im.filter(ImageFilter.GaussianBlur(DETAIL_BLUR))
    y, cb, cr = im.convert("YCbCr").split()
    fy, fcb, fcr = floor.convert("YCbCr").split()
    mix = lambda a, b, k: Image.blend(b, a, k)  # noqa: E731  (k of a, the rest b)
    y2 = mix(y, fy, DETAIL_CONTRAST)
    cb2, cr2 = mix(cb, fcb, DETAIL_CHROMA), mix(cr, fcr, DETAIL_CHROMA)
    return Image.merge("YCbCr", (y2, cb2, cr2)).convert("RGB")


def tone(path, board, frame, data):
    original = Image.open(path).convert("RGB")
    im = mute_details(original)
    im = Image.blend(im, Image.new("RGB", im.size, (251, 239, 214)), WASH)
    im = ImageEnhance.Color(im).enhance(SATURATION)
    im = ImageEnhance.Contrast(im).enhance(CONTRAST)
    im = ImageEnhance.Brightness(im).enhance(BRIGHTNESS)
    floor = im.filter(ImageFilter.GaussianBlur(CALM_BLUR))
    im = Image.composite(floor, im, calm_mask(im.size, board, frame))
    im = Image.composite(im, original, hull_mask(im.size, data, frame))      # the void stays as painted
    s, ox, oy = frame
    d = ImageDraw.Draw(im)
    for sec in board["sections"]:
        pts = [(ox + s * x, oy + s * y) for x, y in sec["poly"]]
        d.line(pts + pts[:1], fill=(70, 92, 100), width=BORDER_PX + 3, joint="curve")
        d.line(pts + pts[:1], fill=(251, 239, 214), width=BORDER_PX - 1, joint="curve")
    return im


def main():
    data = json.loads((ROOT / "data" / "boards.json").read_text())
    frame = rt.board_frame(data)
    for b in data["boards"]:
        for suffix in ("", "_2"):
            src = SRC / f"board_{b['id'].lower()}_v2{suffix}.png"
            if src.exists():
                out = src.with_name(src.stem + "_toned.png")
                tone(src, b, frame, data).save(out)
                print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
