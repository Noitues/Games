"""Top-down preview of the generated TTS table, for checking the layout
without Tabletop Simulator.

    python tools/tts_preview.py            # writes tts/build/preview.png

Reads the save file and its images from ``tts/build`` and pastes every flat
object at the position and size the Global script's calibration will give it
(the LAYOUT table), seen from the South seat (North at the top).
"""
from __future__ import annotations

import json
import os
import re
import sys

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "tts", "build")
SCALE = 22                      # preview pixels per world unit
TABLE = (58.0, 40.0)            # Table_RPG surface, world units (approximate)


def asset_path(url: str) -> str:
    return os.path.join(BUILD, "assets", url.rsplit("/", 1)[-1])


def main() -> int:
    saves = [f for f in os.listdir(BUILD) if f.startswith("HexNexus_") and f.endswith(".json")]
    if not saves:
        sys.exit("no save in tts/build: run tools/tts_export.py first")
    with open(os.path.join(BUILD, sorted(saves)[-1])) as fh:
        save = json.load(fh)
    objs = {}

    def walk(o):
        objs[o.get("GMNotes", "")] = o
    for o in save["ObjectStates"]:
        walk(o)
    # LAYOUT is in data.lua; the save carries the same numbers in its script
    m = re.search(r"^LAYOUT = (\{.*?^\})", save["LuaScript"], re.S | re.M)
    layout = {}
    for tag, body in re.findall(r'\["([^"]+)"\] = \{(.*?)\}', m.group(1), re.S):
        vals = dict(re.findall(r"(\w+) = ([-\w.]+)", body))
        layout[tag] = {k: (float(v) if re.match(r"^-?[\d.]+$", v) else v) for k, v in vals.items()}
    xs = [v["x"] for v in layout.values()]
    zs = [v["z"] for v in layout.values()]
    minx, maxx = min(min(xs) - 4, -TABLE[0] / 2 - 2), max(max(xs) + 4, TABLE[0] / 2 + 2)
    minz, maxz = min(min(zs) - 4, -TABLE[1] / 2 - 2), max(max(zs) + 4, TABLE[1] / 2 + 2)
    W, H = int((maxx - minx) * SCALE), int((maxz - minz) * SCALE)
    img = Image.new("RGB", (W, H), (24, 36, 30))
    d = ImageDraw.Draw(img)

    def to_px(x, z):
        return (x - minx) * SCALE, (maxz - z) * SCALE

    order = sorted(layout.items(), key=lambda kv: (kv[1]["y"], kv[0]))
    for tag, spec in order:
        o = objs.get(tag)
        if o is None or "CustomImage" not in o or spec.get("w", 0) <= 0:
            continue
        if not spec.get("start", "true") == "true" and spec.get("start") is not None:
            pass
        im = Image.open(asset_path(o["CustomImage"]["ImageURL"])).convert("RGBA")
        w, h = int(spec["w"] * SCALE), int(spec["d"] * SCALE)
        # tiles are laid out by their opaque extent: crop the transparent margin
        bbox = im.getbbox()
        if bbox:
            im = im.crop(bbox)
        im = im.resize((max(1, w), max(1, h)))
        if abs(spec["rot"] % 360) < 1:          # reads upright from the North seat
            im = im.rotate(180)
        cx, cy = to_px(spec["x"], spec["z"])
        img.paste(im, (int(cx - w / 2), int(cy - h / 2)), im)
    for tag, spec in layout.items():
        o = objs.get(tag)
        if o is not None and "CustomImage" not in o:
            cx, cy = to_px(spec["x"], spec["z"])
            d.rectangle((cx - 30, cy - 40, cx + 30, cy + 40), outline=(255, 255, 255), width=2)
            d.text((cx - 28, cy - 36), o.get("Nickname", "")[:24], fill=(255, 255, 255))
    # Table_RPG's playing surface, as measured from a screenshot of the M0
    # build (about 58 x 40 units): everything should sit inside this line
    tx0, ty0 = to_px(-TABLE[0] / 2, TABLE[1] / 2)
    tx1, ty1 = to_px(TABLE[0] / 2, -TABLE[1] / 2)
    d.rectangle((tx0, ty0, tx1, ty1), outline=(255, 80, 80), width=3)
    for sp in save.get("SnapPoints", []):
        cx, cy = to_px(sp["Position"]["x"], sp["Position"]["z"])
        d.ellipse((cx - 4, cy - 4, cx + 4, cy + 4), fill=(255, 255, 0))
    out = os.path.join(BUILD, "preview.png")
    img.save(out)
    print(f"wrote {os.path.relpath(out, ROOT)} ({W}x{H})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
