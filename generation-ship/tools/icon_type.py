"""Set a line of icons and numbers with Pillow, from the rasters in art/icons/png (tools/icons.py).

Items: ("icon", name), ("n", "2") a number in the title face, ("text", "...") a short word in the
body face, ("sep",) a thin divider between effects, ("gap",). Lines shrink to fit their width.
"""
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
PNG = ROOT / "art" / "icons" / "png"
FONTS = ROOT / "art" / "fonts"
INK = "#0F3A48"


@lru_cache(maxsize=None)
def glyph(name, size, dim=False):
    """A glyph; dim=True greys it out (an absent guild in the card's guild column)."""
    g = Image.open(PNG / f"{name}.png").convert("RGBA").resize((size, size), Image.LANCZOS)
    if dim:
        grey = g.convert("LA").convert("RGBA")
        grey = Image.blend(grey, Image.new("RGBA", g.size, (251, 239, 214, 0)), 0.45)
        grey.putalpha(g.getchannel("A").point(lambda v: int(v * 0.55)))
        g = grey
    return g


def guild_column(im, s, origin, guilds, frame_mm):
    """The Spirit Island-style guild column: all eight guilds top to bottom, the card's own in colour,
    the others greyed out. s = px per mm; origin = the card's top-left in mm on im; frame_mm = (centres
    list, icon diameter) from tools/retro_templates.py."""
    centres, d = frame_mm
    order = ["Engineers", "Navigators", "Bureaucrats", "Farmers", "Medics", "Laborers", "Keepers", "Scholars"]
    size = round(d * s)
    for (cx, cy), g in zip(centres, order):
        gl = glyph(f"guild_{g}", size, dim=g not in guilds)
        im.paste(gl, (round((origin[0] + cx) * s - size / 2), round((origin[1] + cy) * s - size / 2)), gl)


def title_font(px):
    return ImageFont.truetype(str(FONTS / "Righteous-Regular.ttf"), px)


def text_font(px):
    f = ImageFont.truetype(str(FONTS / "JosefinSans[wght].ttf"), px)
    try:
        f.set_variation_by_name("SemiBold")
    except (OSError, ValueError):
        pass
    return f


def _width(d, items, size):
    w = 0
    for it in items:
        if it[0] == "icon":
            w += size * 1.04
        elif it[0] == "n":
            w += d.textlength(it[1], font=title_font(round(size * .8))) + size * .08
        elif it[0] == "text":
            w += d.textlength(it[1], font=text_font(round(size * .42))) + size * .2
        elif it[0] == "sep":
            w += size * .45
        else:
            w += size * .3
    return w


def draw(im, x, cy, items, size, max_w=None, colour=INK):
    """Draw items left to right, vertically centred on cy. Returns the end x."""
    d = ImageDraw.Draw(im)
    if max_w:
        while size > 18 and _width(d, items, size) > max_w:
            size -= 2
    for it in items:
        if it[0] == "icon":
            g = glyph(it[1], size)
            im.paste(g, (round(x), round(cy - size / 2)), g)
            x += size * 1.04
        elif it[0] == "n":
            f = title_font(round(size * .8))
            d.text((x, cy), it[1], fill=colour, font=f, anchor="lm")
            x += d.textlength(it[1], font=f) + size * .08
        elif it[0] == "text":
            f = text_font(round(size * .42))
            d.text((x + size * .1, cy), it[1], fill=colour, font=f, anchor="lm")
            x += d.textlength(it[1], font=f) + size * .2
        elif it[0] == "sep":
            d.line((x + size * .2, cy - size * .36, x + size * .2, cy + size * .36), fill="#B9AE98", width=max(2, size // 22))
            x += size * .45
        else:
            x += size * .3
    return x
