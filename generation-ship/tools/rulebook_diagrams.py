"""Rulebook diagrams, hand-coded SVG over the real typeset cards (no image model).

    python3 tools/rulebook_diagrams.py   -> art/rulebook/conveyor.svg, wall_slotting.svg, card_anatomy.svg
                                           (+ a .png of each, and the card/slot images they use)

The SVGs reference their images and fonts by relative path (art/rulebook/img/*.png, art/fonts/), so
they work from the rulebook's HTML when art/ is served alongside it. Rules wording follows GDD.md
("Each round", "The leader conveyor", "The Wall of Leaders").
"""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
import event_cards  # noqa: E402
import retro_templates as rt  # noqa: E402
import table_mockup as tm  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "art" / "rulebook"
IMG = OUT / "img"
SRC = ROOT / "art" / "source" / "retro"
TEAL, TANG, CREAM, GOLD, INK, GREY = "#0F3A48", "#E8603A", "#FBEFD6", "#F6C85A", "#203038", "#4A4F55"
K = 4                       # px per mm in the diagrams


def m(v):
    return v * K


# --- images the diagrams use --------------------------------------------------------------------
def build_images():
    IMG.mkdir(parents=True, exist_ok=True)
    people = json.loads((ROOT / "data" / "people.json").read_text())
    events = {e["id"]: e for e in json.loads((ROOT / "data" / "events.json").read_text())["cards"]}
    rem = [p for p in people if p["tier"] != "Common"]
    com = [p for p in people if p["tier"] == "Common"]
    leaders = {"ilka": (rem[2], "Ilka Tor"), "pell": (com[30], "Pell Ashgrove"), "ostra": (rem[21], "Ostra Vell"), "dace": (com[5], "Dace Morrow")}
    for key, (person, name) in leaders.items():
        tm.people_card(person, SRC / f"{key}.png", name).save(IMG / f"leader_{key}.png")
    b = rt.BLEED * rt.CARD_PX
    for eid in ("E1-3", "E2-1", "E3-5", "E1-4"):
        frame = "event_example.png" if eid == "E2-1" else "event_frame_b.png"
        ev = event_cards.typeset(events[eid], frame)
        tm.round_corners(ev.crop((b, b, ev.width - b, ev.height - b)), 3 * rt.CARD_PX).save(IMG / f"event_{eid}.png")
    # one Wall slot with its windows cut out (transparent), so a card can show through
    s = rt.WALL_PX
    wall = Image.open(SRC / "wall_panel_v3b_exact.png").convert("RGBA")
    ox, oy = rt.wall_slot_origins()[0]
    cut = tm.window_mask(wall.size, s, [(ox, oy)], erode=False)
    d = ImageDraw.Draw(cut)
    d.rounded_rectangle(tm.plaque_box(ox, oy, s), rt.PLAQUE_R * s, fill=255)
    wall.putalpha(Image.eval(cut, lambda v: 255 - v))
    pitch = rt.WALL_W / rt.WALL_SLOTS
    wall.crop((0, 0, round(pitch * s), wall.height)).save(IMG / "wall_slot.png")


def render(name, svg, w, h):
    f = OUT / f"{name}.svg"
    f.write_text(svg)
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{w},height:{h}}},deviceScaleFactor:2}});"
          f"await p.goto('{f.as_uri()}');await p.waitForTimeout(600);await p.screenshot({{path:'{OUT / (name + '.png')}'}});await b.close();}})();")
    subprocess.run(["node", "-e", js], check=True)
    print("wrote", f.relative_to(ROOT), "and", (OUT / f"{name}.png").relative_to(ROOT))


def svg_open(w, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            "<defs><style>@font-face{font-family:Righteous;src:url('../fonts/Righteous-Regular.ttf')}"
            "@font-face{font-family:Josefin;src:url('../fonts/JosefinSans[wght].ttf')}"
            ".t{font-family:Righteous,sans-serif;fill:#0F3A48}.b{font-family:Josefin,sans-serif;fill:#203038}</style>"
            '<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 Z" fill="{TANG}"/></marker>'
            '<filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity=".3"/></filter></defs>'
            f'<rect width="{w}" height="{h}" fill="#F7F1E4"/>')


def img(href, x, y, w, h, extra=""):
    return f'<image href="img/{href}" x="{x}" y="{y}" width="{w}" height="{h}" {extra}/>'


def text(x, y, s, size=16, cls="b", anchor="start", weight=None, fill=None):
    wt = f' font-weight="{weight}"' if weight else ""
    fl = f' style="fill:{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" text-anchor="{anchor}"{wt}{fl}>{s}</text>'


def lines(x, y, rows, size=15, gap=None, anchor="start", weight=None):
    gap = gap or size * 1.3
    return "".join(text(x, y + i * gap, r, size, anchor=anchor, weight=weight) for i, r in enumerate(rows))


def arrow(x1, y1, x2, y2, w=4, dash=None, curve=None):
    d = f"M{x1},{y1} Q{curve[0]},{curve[1]} {x2},{y2}" if curve else f"M{x1},{y1} L{x2},{y2}"
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{TANG}" stroke-width="{w}"{da} marker-end="url(#ah)"/>'


def pair(x, y, leader, event, s=1.0):
    """A leader card with its event tucked below (30.5 mm of the event shows), top-left at x, y."""
    cw, ch = m(63) * s, m(88) * s
    return (f'<g filter="url(#sh)">{img(event, x, y + m(30.5) * s, cw, ch)}{img(leader, x, y, cw, ch)}</g>')


# --- 1. the conveyor ----------------------------------------------------------------------------
def conveyor():
    W, H = 1500, 1120
    s = 0.85
    cw, chh = m(63) * s, m(118.5) * s                                 # a card, and a card with its event tucked
    o = [svg_open(W, H), text(40, 54, "The leader conveyor: Dawn, Day, Dusk", 34, "t"),
         lines(40, 88, ["Each leader is paired with an event, tucked below it; only the event's lower band shows (stage, section types, twist).",
                        "Every generation the leaders move one step along the sun, each event with its leader."], 17)]
    xs, ys = [430, 750, 1070], [330, 270, 330]
    o.append(f'<path d="M150,{ys[0] + 40} C{xs[0]},{ys[1] - 150} {xs[2]},{ys[1] - 150} 1350,{ys[0] + 40}" fill="none" stroke="{GOLD}" stroke-width="4" stroke-dasharray="3 12" stroke-linecap="round"/>')
    slots = [("DAWN", "the heir", ["Its event SEEDS: +1 Glitch in", "each matching section on the", "Outer Hull or next to a Fault", "or Failure."],
              "leader_ilka.png", "event_E1-3.png", "#F2A86A"),
             ("DAY", "the Steward", ["Its REIGN applies, and its", "event GROWS: +1 Fault in each", "matching section with threat", "(a Failure if it has 2 Faults)."],
              "leader_pell.png", "event_E2-1.png", GOLD),
             ("DUSK", "the Elder", ["Its LEGACY takes hold for the", "rest of the voyage, then its", "event COLLAPSES: matching", "sections take their threat's damage."],
              "leader_ostra.png", "event_E3-5.png", TANG)]
    for (name, who, rows, leader, event, col), x, y in zip(slots, xs, ys):
        o.append(f'<circle cx="{x}" cy="{y - 30}" r="16" fill="{col}" stroke="{TEAL}" stroke-width="3"/>')
        o.append(text(x - 30, y - 22, name, 30, "t", "end") + text(x + 30, y - 22, who, 17, anchor="start", weight="700"))
        o.append(pair(x - cw / 2, y, leader, event, s))
        o.append(lines(x, ys[0] + chh + 44, rows, 16, anchor="middle"))
    for a, b in ((0, 1), (1, 2)):
        o.append(arrow(xs[a] + cw / 2 + 10, ys[a] + 120, xs[b] - cw / 2 - 10, ys[b] + 120, dash="8 6"))
    # the event deck and the Wall
    dx, dy = 80, 420
    o.append('<g filter="url(#sh)">' + "".join(f'<rect x="{dx + k * 3}" y="{dy - k * 3}" width="{m(36)}" height="{m(50)}" rx="10" fill="{TEAL}" stroke="{GOLD}" stroke-width="2"/>' for k in range(4)) + "</g>")
    o.append(lines(dx + m(18), dy + m(50) + 34, ["EVENT DECK", "drawn at Dawn,", "after the vote"], 15, anchor="middle"))
    o.append(arrow(dx + m(36) + 14, dy + 60, xs[0] - cw / 2 - 12, ys[0] + 210, curve=(dx + m(36) + 70, dy + 40)))
    wx, wy = 1290, 400
    o.append(f'<g filter="url(#sh)"><rect x="{wx}" y="{wy}" width="{m(42)}" height="{m(58)}" rx="12" fill="{CREAM}" stroke="#B9A57A" stroke-width="3"/>'
             f'<path d="M{wx + 24},{wy + 56} C{wx + 24},{wy + 26} {wx + 144},{wy + 26} {wx + 144},{wy + 56} L{wx + 144},{wy + 120} L{wx + 24},{wy + 120} Z" fill="{TEAL}"/>'
             f'<rect x="{wx + 18}" y="{wy + 160} " width="{m(42) - 36}" height="40" rx="8" fill="{TEAL}"/></g>')
    o.append(lines(wx + m(21), wy + m(58) + 34, ["THE WALL", "retired leaders,", "Legacies in force"], 15, anchor="middle"))
    o.append(arrow(xs[2] + cw / 2 + 10, ys[2] + 120, wx - 10, wy + 110, dash="8 6"))
    # time passes
    by = H - 160
    o.append(f'<rect x="40" y="{by}" width="{W - 80}" height="130" rx="16" fill="{CREAM}" stroke="#D8CDB6"/>')
    o.append(text(70, by + 40, "Time passes (end of every generation)", 22, "t"))
    o.append(lines(70, by + 74, ["1. The Dusk leader and its event (and any Breakthrough) move to the next Wall slot. Day moves to Dusk, Dawn moves to Day.",
                                 "2. Each generation resolves Dusk, then Day, then Dawn. At Dawn the houses vote for the heir BEFORE its event is drawn."], 16))
    o.append("</svg>")
    render("conveyor", "".join(o), W, H)


# --- 2. Wall slotting --------------------------------------------------------------------------
def wall_slotting():
    W, H = 1500, 1180
    o = [svg_open(W, H), text(40, 54, "The Wall of Leaders: how a leader retires", 34, "t"),
         lines(40, 86, ["At Time passes, the Dusk leader slides into the next empty slot, from the top edge, between the two layers of the Wall.",
                        "Its portrait shows in the frame and its Legacy in the plaque below, still in force for the rest of the voyage."], 17)]
    sw, sh = 290 / 4 * K * 1.25, 120 * K * 1.25                        # one slot, 1.25x scale (panel 2)
    cw, ch = m(63) * 1.25, m(88) * 1.25
    # A: the card above an empty slot (the dark backing shows through its windows)
    a = 0.9
    asw, ash, acw, ach = sw / 1.25 * a, sh / 1.25 * a, cw / 1.25 * a, ch / 1.25 * a
    ax, aslot = 90, 590
    o.append(text(ax + asw / 2, 150, "1 · Slide in from the top", 22, "t", "middle"))
    o.append(f'<g filter="url(#sh)">{img("leader_ostra.png", ax + (asw - acw) / 2, 190, acw, ach)}</g>')
    o.append(f'<rect x="{ax + 10}" y="{aslot + 10}" width="{asw - 20}" height="{ash - 20}" rx="10" fill="#1B3440"/>')
    o.append(f'<g filter="url(#sh)">{img("wall_slot.png", ax, aslot, asw, ash)}</g>')
    o.append(arrow(ax + asw + 30, 260, ax + asw + 30, aslot + 40, w=6))
    o.append(f'<rect x="{ax + (asw - acw) / 2 - 4}" y="{aslot - 4}" width="{acw + 8}" height="8" rx="4" fill="{TEAL}"/>')
    o.append(text(ax + asw / 2, aslot + ash + 32, "the slit along the Wall's top edge", 15, anchor="middle"))
    # B: in place
    bx = 520
    o.append(text(bx + sw / 2, 150, "2 · In place", 22, "t", "middle"))
    o.append(f'<g filter="url(#sh)">{img("leader_ostra.png", bx + (sw - cw) / 2, 200 + 8 * K * 1.25, cw, ch)}{img("wall_slot.png", bx, 200, sw, sh)}</g>')
    py = 200 + (8 + rt.CARD_WIN[1] + rt.WIN_H / 2) * K * 1.25
    ly = 200 + (8 + rt.CARD_PLAQUE[1] + rt.PLAQUE_H / 2) * K * 1.25
    o.append(f'<line x1="{bx + sw - 30}" y1="{py}" x2="{bx + sw + 40}" y2="{py}" stroke="{TEAL}" stroke-width="2"/>'
             + lines(bx + sw + 48, py - 6, ["portrait window", "(the card's arch)"], 15))
    o.append(f'<line x1="{bx + sw - 30}" y1="{ly}" x2="{bx + sw + 40}" y2="{ly}" stroke="{TEAL}" stroke-width="2"/>'
             + lines(bx + sw + 48, ly - 6, ["Legacy plaque", "(still in force)"], 15))
    by = 200 + (8 + rt.CARD_PLAQUE[1] + rt.PLAQUE_H + 7.5) * K * 1.25
    o.append(f'<line x1="{bx + sw / 2 + 24}" y1="{by}" x2="{bx + sw + 40}" y2="{by + 30}" stroke="{TEAL}" stroke-width="2"/>'
             + lines(bx + sw + 48, by + 26, ["slot number:", "the game clock"], 15))
    # C: cross-section
    x0, y0 = 1210, 230
    o.append(text(x0 + 150, 150, "3 · Side view", 22, "t", "middle"))
    o.append(f'<rect x="{x0}" y="{y0}" width="34" height="480" rx="6" fill="#E9DFC8" stroke="#B9A57A" stroke-width="3"/>'
             f'<rect x="{x0 + 70}" y="{y0}" width="34" height="480" rx="6" fill="#E9DFC8" stroke="#B9A57A" stroke-width="3"/>'
             f'<rect x="{x0 + 44}" y="{y0 + 40}" width="16" height="420" rx="4" fill="{CREAM}" stroke="{TEAL}" stroke-width="3"/>'
             f'<rect x="{x0 - 4}" y="{y0 + 110}" width="42" height="120" fill="#F7F1E4"/><rect x="{x0 - 4}" y="{y0 + 300}" width="42" height="56" fill="#F7F1E4"/>')
    o.append(arrow(x0 + 52, y0 - 70, x0 + 52, y0 + 30, w=5))
    o.append(lines(x0 - 18, y0 + 66, ["top layer, 2 mm:", "windows cut through"], 15, anchor="end")
             + lines(x0 - 18, y0 + 396, ["the card, slotted", "between the layers"], 15, anchor="end")
             + lines(x0 + 124, y0 + 250, ["bottom layer,", "2 mm: backing"], 15))
    o.append(f'<line x1="{x0}" y1="{y0 + 60}" x2="{x0 - 12}" y2="{y0 + 60}" stroke="{TEAL}" stroke-width="2"/>'
             f'<polyline points="{x0 + 52},{y0 + 390} {x0 - 12},{y0 + 390}" fill="none" stroke="{TEAL}" stroke-width="2"/>'
             f'<line x1="{x0 + 104}" y1="{y0 + 245}" x2="{x0 + 118}" y2="{y0 + 245}" stroke="{TEAL}" stroke-width="2"/>')
    o.append(f'<rect x="40" y="{H - 120}" width="{W - 80}" height="90" rx="16" fill="{CREAM}" stroke="#D8CDB6"/>')
    o.append(lines(70, H - 82, ["Its paired event (and any Breakthrough token, set on the frame) goes to the same slot. When every slot is full and the event deck",
                             "is empty, the next Dawn draw loses the game: the Wall is the game's clock."], 16))
    o.append("</svg>")
    render("wall_slotting", "".join(o), W, H)


# --- 3. card anatomy ---------------------------------------------------------------------------
def card_anatomy():
    W, H = 1780, 1000
    S = 6.2                                                             # px per mm for the two cards
    cwp, chp = 63 * S, 88 * S
    lx, ly, ex, ey = 290, 130, 1190, 130
    o = [svg_open(W, H), text(40, 54, "Card anatomy", 34, "t")]
    o.append(f'<g filter="url(#sh)">{img("leader_pell.png", lx, ly, cwp, chp)}</g>')
    o.append(f'<g filter="url(#sh)">{img("event_E2-1.png", ex, ey, cwp, chp)}</g>')
    o.append(text(lx + cwp / 2, 112, "A people card (a leader once chosen)", 20, "t", "middle"))
    o.append(text(ex + cwp / 2, 112, "An event card", 20, "t", "middle"))

    def call(cx, cy, card, side, rows, dy=0):
        """From a point on a card (mm) to a label beside it, with an elbow when the label is moved by dy."""
        bx, by = card
        px, py = bx + cx * S, by + cy * S
        edge = bx - 18 if side == "L" else bx + cwp + 18
        tx = bx - 30 if side == "L" else bx + cwp + 30
        anchor = "end" if side == "L" else "start"
        ty = py + dy
        return (f'<circle cx="{px}" cy="{py}" r="6" fill="{TANG}" stroke="#fff" stroke-width="2"/>'
                f'<polyline points="{px},{py} {edge},{py} {tx + (6 if side == "L" else -6)},{ty}" fill="none" stroke="{TANG}" stroke-width="2"/>'
                + text(tx, ty + 5, rows[0], 17, anchor=anchor, weight="700")
                + "".join(text(tx, ty + 26 + 19 * i, r, 15, anchor=anchor) for i, r in enumerate(rows[1:])))
    L, R = (lx, ly), (ex, ey)
    o.append(call(5, 4.8, L, "L", ["Name", "the person on the card"]))
    o.append(call(31.5, 28, L, "L", ["Portrait", "shows through the Wall's", "window once retired"]))
    o.append(call(5, 54.2, L, "L", ["Guilds", "count toward thresholds"], dy=-30))
    o.append(call(5, 58.6, L, "L", ["Reign", "while this leader is in Day,", "in its event's sections"], dy=30))
    o.append(call(4, 78, L, "L", ["Legacy", "from Dusk on, for the rest of", "the voyage: one benefit,", "one or more drawbacks"], dy=40))
    o.append(call(59, 4.8, L, "R", ["Cost", "in credits"]))
    o.append(call(36, 54.2, L, "R", ["Effect", "in icons: 2 credits; Lockout"]))
    E = rt.EVENT
    o.append(call(31.5, 19, R, "L", ["Picture", "where the trouble is"]))
    o.append(call(10, 44, R, "L", ["When revealed", "(optional, not yet in use):", "a possible one-time effect"], dy=-20))
    o.append(call(3, E["tuck"], R, "L", ["Tuck line", "the leader covers everything", "above it on the conveyor"], dy=20))
    o.append(call(E["stage"][0], E["stage"][1], R, "L", ["Stage", "I, II or III"], dy=70))
    o.append(call(E["icons"][0][0], E["icons"][0][1], R, "R", ["Section types", "where it seeds, grows", "and collapses"], dy=-20))
    o.append(call(52, 82, R, "R", ["Twist", "Stage II and III:", "an extra rule"]))
    o.append(f'<rect x="40" y="{H - 110}" width="{W - 80}" height="80" rx="16" fill="{CREAM}" stroke="#D8CDB6"/>')
    o.append(lines(70, H - 78, ["Icons: a number, then what it acts on, read left to right. 2 [wrench] = 2 damage to threat; 1 [shield] = Brace 1.",
                                "Teal bands are benefits, red bands drawbacks. The icon sheet at the back of the rulebook lists every icon."], 16))
    o.append("</svg>")
    render("card_anatomy", "".join(o), W, H)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    build_images()
    conveyor()
    wall_slotting()
    card_anatomy()


if __name__ == "__main__":
    main()
