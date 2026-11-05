"""Typeset the house boards: house data (data/houses.json) set into the blank panels of the Retro
house-board art, in the style guide's fonts (Righteous for titles, Josefin Sans for text).

    python3 tools/house_boards.py   -> art/source/retro/house_<id>_typeset.png

The panels are found in each image, not hard-coded: cream regions are labelled, then sorted into
the name banner (top), the three growth cards (a row of equal rectangles), the special-rules panel
(the largest), the track sockets (two rows of small squares) and the two innate panels (wide, at
the bottom), with the small threshold circles inside them. Effect wording comes from VERB in
src/print/print.js, so the boards match the print-and-play cards.
"""
import json
import re
from collections import deque
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "art" / "source" / "retro"
FONTS = ROOT / "art" / "fonts"
TEAL, TANGERINE, INK = "#0F3A48", "#C9482A", "#203038"
GUILD_ABBR = {"Engineers": "Eng", "Navigators": "Nav", "Bureaucrats": "Bur", "Farmers": "Far", "Medics": "Med",
              "Laborers": "Lab", "Keepers": "Kee", "Scholars": "Sch"}


def title_font(px):
    return ImageFont.truetype(str(FONTS / "Righteous-Regular.ttf"), px)


def text_font(px, weight="Regular"):
    f = ImageFont.truetype(str(FONTS / "JosefinSans[wght].ttf"), px)
    try:
        f.set_variation_by_name(weight)
    except (OSError, ValueError):
        pass
    return f


def verbs():
    js = (ROOT / "src" / "print" / "print.js").read_text()
    block = js[js.index("const VERB = {"):js.index("};", js.index("const VERB = {"))]
    v = dict(re.findall(r'(\w+): "([^"]*)"', block))
    v.update({"brace_each_haven": "Brace {n} at each Haven", "fast_play": "+{n} fast play", "extra_draw": "draw +{n}",
              "credits": "+{n} credits", "place_influence_from_track": "place {n} influence"})
    return v


VERB = verbs()


def fx(effects):
    return "; ".join(VERB.get(k, k.replace("_", " ")).replace("{n}", str(n)) for k, n in effects.items())


# --- finding the panels ---------------------------------------------------------------------------
def regions(im, k=4):
    """Cream regions (x0, y0, x1, y1, area) in full-size pixels."""
    small = im.convert("RGB").resize((im.width // k, im.height // k))
    W, H = small.size
    px = small.load()
    cream = [[False] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            r, g, b = px[x, y]
            mx, mn = max(r, g, b), min(r, g, b)
            cream[y][x] = mx > 215 and mx - mn < 58 and r >= b
    seen = [[False] * W for _ in range(H)]
    out = []
    for y in range(H):
        for x in range(W):
            if cream[y][x] and not seen[y][x]:
                q, pts = deque([(x, y)]), []
                seen[y][x] = True
                while q:
                    cx, cy = q.popleft()
                    pts.append((cx, cy))
                    for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                        if 0 <= nx < W and 0 <= ny < H and cream[ny][nx] and not seen[ny][nx]:
                            seen[ny][nx] = True
                            q.append((nx, ny))
                if len(pts) > 30:
                    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
                    out.append((min(xs) * k, min(ys) * k, (max(xs) + 1) * k, (max(ys) + 1) * k, len(pts) * k * k))
    return out


def layout(im):
    regs = [r for r in regions(im) if r[4] > 900]
    big = sorted([r for r in regs if r[4] > 30000], key=lambda r: r[4])
    small = [r for r in regs if r[4] <= 30000]
    special = big[-1]
    banner = min((r for r in big if (r[2] - r[0]) > 2.5 * (r[3] - r[1])), key=lambda r: r[1])
    innate = sorted([r for r in big if r[1] > im.height * 0.6 and r is not banner], key=lambda r: r[0])[:2]
    growth = sorted([r for r in big if r not in (special, banner) and r not in innate], key=lambda r: r[0])[:3]
    inside = lambda r, p: p[0] >= r[0] and p[2] <= r[2] and p[1] >= r[1] and p[3] <= r[3]  # noqa: E731
    circles = [[c for c in small if inside(p, c)] for p in innate]
    sockets = sorted([c for c in small if not any(inside(p, c) for p in innate) and c[4] > 2300], key=lambda c: (c[1], c[0]))
    rows = []
    for c in sockets:
        if rows and abs(rows[-1][0][1] - c[1]) < 40:
            rows[-1].append(c)
        else:
            rows.append([c])
    rows = [sorted(r, key=lambda c: c[0]) for r in rows if len(r) >= 4][:2]
    return {"banner": banner, "growth": growth, "special": special, "tracks": rows, "innate": innate,
            "circles": [sorted(c, key=lambda c: c[0]) for c in circles]}


# --- typesetting ----------------------------------------------------------------------------------
def wrap(d, text, f, width):
    lines, line = [], ""
    for word in text.split():
        t = (line + " " + word).strip()
        if d.textlength(t, font=f) <= width or not line:
            line = t
        else:
            lines.append(line)
            line = word
    return lines + [line]


def block(d, box, title, body, pad=16, tsize=24, bsize=19, title_fill=TEAL, gap=True):
    """A title and wrapped body text in a box; shrinks the body (to 14 px, about 7 pt at print
    size) until it fits. The left pad clears the corner stripe some panels have."""
    x0, y0, x1, y1 = box[:4]
    x0 += 18
    for size in range(bsize, 13, -1):
        f = text_font(size)
        lines = []
        for para in body:
            lines += wrap(d, para, f, x1 - x0 - 2 * pad) + ([""] if gap else [])
        if y0 + pad + tsize + 8 + len(lines) * size * 1.18 <= y1 - pad:
            break
    y = y0 + pad
    if title:
        y += 6
        d.text((x0 + pad, y), title, fill=title_fill, font=title_font(tsize))
        y += tsize + 8
    for line in lines:
        if line:
            d.text((x0 + pad, y), line, fill=INK, font=f)
        y += size * 1.18
    return y


def slot_label(v):
    if isinstance(v, int):
        return str(v), title_font(30)
    k, n = next(iter(v.items()))
    if k == "element":
        return GUILD_ABBR.get(n, n[:3]), text_font(17, "Bold")
    return {"draw": f"+{n}\ncard", "clone": "clone", "fast_play": "fast"}.get(k, k), text_font(15, "Bold")


def typeset(house):
    im = Image.open(SRC / f"house_{house['id']}.png").convert("RGB")
    L = layout(im)
    d = ImageDraw.Draw(im)
    # banner: the name, and the guilds
    x0, y0, x1, y1 = L["banner"][:4]
    name, _, epithet = house["name"].partition(", ")
    d.text((x0 + 20, (y0 + y1) / 2), name, fill=TEAL, font=title_font(46), anchor="lm")
    nx = x0 + 20 + d.textlength(name, font=title_font(46)) + 16
    d.text((nx, (y0 + y1) / 2 - 12), epithet, fill=TANGERINE, font=text_font(22, "SemiBold"), anchor="lm")
    g = house["guilds"]
    d.text((nx, (y0 + y1) / 2 + 16), f"{g['primary']} · {g['secondary']}", fill=INK, font=text_font(18), anchor="lm")
    # growth: pick one per generation
    perks = house.get("growth_perk") or {}
    for box, gr in zip(L["growth"], house["growth"]):
        body = [gr["text"]] + ([f"Perk: {perks[gr['id']]['text']}"] if gr["id"] in perks else [])
        block(d, box, f"Growth {gr['id']}", body, tsize=24, bsize=18)
    # special rules and set-up
    sp = house["special"]
    block(d, L["special"], sp["id"].replace("_", " ").title(),
          [sp["text"], f"Start: {house['starting_influence']['text']}.", f"Hand +{house.get('hand_bonus', 0)} · Clone slots {house.get('clone', 0)}"],
          tsize=28, bsize=19)
    # tracks: credits on the first row, card plays on the second; sockets beyond the data stay empty
    for row, (key, label) in zip(L["tracks"], (("credits", "credits"), ("plays", "plays"))):
        d.text((row[0][0] + 4, row[0][1] - 4), label.upper(), fill="#FBEFD6", font=text_font(15, "Bold"), anchor="ls")
        for sock, v in zip(row, house["tracks"][key]):
            text, f = slot_label(v)
            d.multiline_text(((sock[0] + sock[2]) / 2, (sock[1] + sock[3]) / 2), text, fill=TEAL if isinstance(v, int) else TANGERINE,
                             font=f, anchor="mm", align="center", spacing=0)
    # innate power: tiers I-II in the first panel, tier III in the second; thresholds in the circles
    inn = house["innate"]
    tiers = inn["tiers"]
    numerals = ["I", "II", "III"]
    th = lambda t: " + ".join(f"{n} {GUILD_ABBR.get(g, g)}" for g, n in t["threshold"].items())  # noqa: E731
    rng = lambda t: f"range {t['range']}" if t.get("range") else "here"  # noqa: E731
    panels = [tiers[:2], tiers[2:]]
    for i, (box, ts) in enumerate(zip(L["innate"], panels)):
        circles = L["circles"][i] if i < len(L["circles"]) else []
        bottom = min([c[1] for c in circles], default=box[3]) - 4
        title = f"{inn['name']} · {inn['speed']}" if i == 0 else f"{inn['name']} (top tier)"
        body = [f"{numerals[t['tier'] - 1]} · {th(t)} · {rng(t)}: {fx(t['effects'])}" for t in ts]
        block(d, (box[0], box[1], box[2], max(bottom, box[1] + 110)), title, body, tsize=24, bsize=18, gap=False)
        for c, t in zip(circles, ts):
            d.text(((c[0] + c[2]) / 2, (c[1] + c[3]) / 2), numerals[t["tier"] - 1], fill=TANGERINE, font=title_font(22), anchor="mm")
    out = SRC / f"house_{house['id']}_typeset.png"
    im.save(out)
    return out


def main():
    houses = json.loads((ROOT / "data" / "houses.json").read_text())["houses"]
    for h in houses:
        if (SRC / f"house_{h['id']}.png").exists():
            print("wrote", typeset(h).relative_to(ROOT))


if __name__ == "__main__":
    main()
