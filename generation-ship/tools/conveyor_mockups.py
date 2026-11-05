"""SVG layout studies for the conveyor board (Dawn / Day / Dusk), drawn to scale.

    python3 tools/conveyor_mockups.py   -> art/conveyor/conveyor_options.svg (+ .png via Playwright)

The three slots follow the sun's path across the sky: low at Dawn, high at Day, low at Dusk. The
event deck waits below the horizon before Dawn; after Dusk the leader and its event retire to the
Wall. Every leader is paired with an event card, so each option makes room for both:
  A  Tucked: the event slides behind the leader and shows its top band above the card.
  B  Event below: the event slides under the leader and shows its band at the horizon.
  C  Side by side: a mini event card (44 x 63 mm) next to each leader, both fully visible.
Cards are poker size (63 x 88 mm) with the master arch window (tools/retro_templates.py).
"""
import math
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import retro_templates as rt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "art" / "conveyor"
SRC = ROOT / "art" / "source" / "retro"
S = 3.0                                     # px per mm in the sheet
TEAL, TURQ, TANG, GOLD, CREAM, PINK = "#0F3A48", "#3AB0A8", "#E8603A", "#F6C85A", "#FBEFD6", "#E88AA0"
ICON = {"Infrastructure": "icon_infrastructure", "Residential": "icon_residential", "Government": "icon_government",
        "Agricultural": "icon_agricultural"}
SLOTS = [("DAWN", "Seed", "#F2A86A"), ("DAY", "Grow · Reign", GOLD), ("DUSK", "Collapse · Legacy", TANG)]
LEADERS = [("Ilka Tor", "ilka", 8), ("Pell Ashgrove", "pell", 1), ("Ostra Vell", "ostra", 4)]
EVENTS = [("I", ["Government"], None), ("II", ["Infrastructure"], "Power surge: at Collapse, each Fault deals +1 damage."),
          ("III", ["Residential", "Agricultural"], None)]


def m(v):
    return v * S


def uri(name):
    return (SRC / f"{name}.png").as_uri()


def defs():
    font = (ROOT / "art" / "fonts")
    return f"""<defs><style>
@font-face {{ font-family: Righteous; src: url('{(font / "Righteous-Regular.ttf").as_uri()}'); }}
@font-face {{ font-family: Josefin; src: url('{(font / "JosefinSans[wght].ttf").as_uri()}'); }}
.t {{ font-family: Righteous, sans-serif; }} .b {{ font-family: Josefin, sans-serif; }}
</style>
<linearGradient id="sky" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#F3B38A"/><stop offset=".22" stop-color="#E9C9A0"/><stop offset=".5" stop-color="#8FD3CC"/>
  <stop offset=".78" stop-color="#E9A27C"/><stop offset="1" stop-color="#7A4A6A"/></linearGradient>
<linearGradient id="skyfade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0F3A48" stop-opacity=".35"/>
  <stop offset=".6" stop-color="#0F3A48" stop-opacity="0"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity=".35"/></filter>
</defs>"""


def sun(cx, cy, r, colour):
    rays = "".join(f'<line x1="{cx + r * 1.25 * math.cos(a)}" y1="{cy + r * 1.25 * math.sin(a)}" x2="{cx + r * (1.9 if k % 2 else 1.6) * math.cos(a)}" '
                   f'y2="{cy + r * (1.9 if k % 2 else 1.6) * math.sin(a)}" stroke="{colour}" stroke-width="3" stroke-linecap="round"/>'
                   for k, a in enumerate(i * math.pi / 8 for i in range(16)))
    return f'<g>{rays}<circle cx="{cx}" cy="{cy}" r="{r}" fill="{colour}" stroke="#FFF3D0" stroke-width="2"/></g>'


def leader_card(x, y, name, portrait, cost, uid):
    """A people card at (x, y) mm: cream frame, arch portrait, name, text lines, teal Legacy plaque."""
    w, h = m(63), m(88)
    win = rt.window_path(x + rt.CARD_WIN[0], y + rt.CARD_WIN[1], S)
    px, py = x + rt.CARD_PLAQUE[0], y + rt.CARD_PLAQUE[1]
    lines = "".join(f'<rect x="{m(x + 7)}" y="{m(y + 55 + 3.2 * k)}" width="{m(49 - 8 * (k % 2))}" height="{m(1)}" rx="1" fill="#B9AE98"/>' for k in range(4))
    return (f'<g filter="url(#sh)"><rect x="{m(x)}" y="{m(y)}" width="{w}" height="{h}" rx="{m(3)}" fill="{CREAM}" stroke="#8C9AA0" stroke-width="1.5"/>'
            f'<clipPath id="w{uid}"><path d="{win}"/></clipPath>'
            f'<image href="{uri(portrait)}" x="{m(x + 2)}" y="{m(y + 6)}" width="{m(59)}" height="{m(46)}" preserveAspectRatio="xMidYMin slice" clip-path="url(#w{uid})"/>'
            f'<path d="{win}" fill="none" stroke="#A9B4BA" stroke-width="2.5"/>'
            f'<text x="{m(x + 6)}" y="{m(y + 6.4)}" class="t" font-size="{m(3.4)}" fill="{TEAL}">{name}</text>'
            f'<text x="{m(x + 57)}" y="{m(y + 6.6)}" class="t" font-size="{m(4)}" fill="{TANG}" text-anchor="end">{cost}</text>{lines}'
            f'<rect x="{m(px)}" y="{m(py)}" width="{m(rt.PLAQUE_W)}" height="{m(rt.PLAQUE_H)}" rx="{m(rt.PLAQUE_R)}" fill="{TEAL}"/>'
            f'<text x="{m(px + rt.PLAQUE_W / 2)}" y="{m(py + 6)}" class="b" font-size="{m(2.3)}" fill="{CREAM}" text-anchor="middle">Legacy: ongoing in sections matching its event…</text>'
            f'<text x="{m(x + 31.5)}" y="{m(y + 51.8)}" class="t" font-size="{m(2.2)}" fill="{TANG}" text-anchor="middle">★</text></g>')


def event_card(x, y, stage, types, twist, w=63, h=88, band_at="top", uid=0):
    """An event card at (x, y) mm. Everything a player needs is in one band (stage, section types,
    twist), at the top (option A, C) or the bottom (option B) so it can show past the leader."""
    band = 30 if w >= 60 else 26
    by = y if band_at == "top" else y + h - band
    icons = "".join(f'<image href="{uri(ICON[t])}" x="{m(x + w / 2 - 5.5 * len(types) + 11 * i + 0.5)}" y="{m(by + 2.5)}" width="{m(10)}" height="{m(10)}"/>'
                    for i, t in enumerate(types))
    tw = (f'<text x="{m(x + w / 2)}" y="{m(by + 22)}" class="b" font-size="{m(2.2)}" fill="{CREAM}" text-anchor="middle">{twist[:46]}</text>'
          f'<text x="{m(x + w / 2)}" y="{m(by + 25)}" class="b" font-size="{m(2.2)}" fill="{CREAM}" text-anchor="middle">{twist[46:92]}</text>') if twist else ""
    art_y = y + band if band_at == "top" else y
    return (f'<g filter="url(#sh)"><rect x="{m(x)}" y="{m(y)}" width="{m(w)}" height="{m(h)}" rx="{m(3)}" fill="{TEAL}" stroke="{GOLD}" stroke-width="1.5"/>'
            f'<rect x="{m(x + 2)}" y="{m(art_y + 1)}" width="{m(w - 4)}" height="{m(h - band - 3)}" rx="{m(2)}" fill="#1A5262"/>'
            + "".join(f'<circle cx="{m(x + 6 + 7 * (k % 8))}" cy="{m(art_y + 6 + 7 * (k // 8))}" r="{m(0.4)}" fill="{GOLD}" opacity=".5"/>' for k in range(int((h - band) / 7) * 8))
            + f'<circle cx="{m(x + 6)}" cy="{m(by + 6)}" r="{m(4)}" fill="{GOLD}"/>'
            f'<text x="{m(x + 6)}" y="{m(by + 7.4)}" class="t" font-size="{m(3.6)}" fill="{TEAL}" text-anchor="middle">{stage}</text>'
            f'{icons}<text x="{m(x + w / 2)}" y="{m(by + 17)}" class="t" font-size="{m(3.2 if w >= 60 else 2.6)}" fill="{CREAM}" text-anchor="middle">{" + ".join(types)}</text>{tw}</g>')


def board(ox, oy, W, H, option):
    """One conveyor board (W x H mm) at (ox, oy) mm on the sheet."""
    o = [f'<g><rect x="{m(ox)}" y="{m(oy)}" width="{m(W)}" height="{m(H)}" rx="{m(8)}" fill="url(#sky)" stroke="#C9D1D6" stroke-width="4"/>',
         f'<rect x="{m(ox)}" y="{m(oy)}" width="{m(W)}" height="{m(H)}" rx="{m(8)}" fill="url(#skyfade)"/>']
    hy = oy + H - 26                                                   # the horizon
    o.append(f'<path d="M{m(ox)},{m(hy)} Q{m(ox + W / 2)},{m(hy - 10)} {m(ox + W)},{m(hy)} L{m(ox + W)},{m(oy + H - 8)} '
             f'Q{m(ox + W)},{m(oy + H)} {m(ox + W - 8)},{m(oy + H)} L{m(ox + 8)},{m(oy + H)} Q{m(ox)},{m(oy + H)} {m(ox)},{m(oy + H - 8)} Z" fill="{TEAL}"/>')
    for k in range(int(W / 9)):                                         # portholes along the hull
        o.append(f'<circle cx="{m(ox + 6 + 9 * k)}" cy="{m(oy + H - 8)}" r="{m(1.4)}" fill="{GOLD}" opacity=".7"/>')
    cw = 63
    # slot centres along the sun's path: low, high, low
    xs = [ox + W * f for f in (0.255, 0.5, 0.745)] if option != "C" else [ox + W * f for f in (0.2, 0.5, 0.8)]
    lift = {"A": (54, 30, 54), "B": (48, 30, 48), "C": (42, 22, 42)}[option]
    ys = [oy + l for l in lift]
    # the sun's path
    path = f'M{m(ox + 12)},{m(hy - 4)} C{m(xs[0])},{m(oy + 10)} {m(xs[2])},{m(oy + 10)} {m(ox + W - 12)},{m(hy - 4)}'
    o.append(f'<path d="{path}" fill="none" stroke="#FFF3D0" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round" opacity=".9"/>')
    for i, (slot, action, colour) in enumerate(SLOTS):
        cx, top = xs[i], ys[i]
        name, portrait, cost = LEADERS[i]
        stage, types, twist = EVENTS[i]
        sx = cx - cw / 2
        if option == "A":                       # event behind, its top band showing above the leader
            o.append(f'<rect x="{m(sx - 2)}" y="{m(top - 2)}" width="{m(cw + 4)}" height="{m(88 + 30 + 4)}" rx="{m(4)}" fill="#000" opacity=".12"/>')
            o.append(event_card(sx, top, stage, types, twist, uid=i))
            o.append(leader_card(sx, top + 30, name, portrait, cost, f"a{i}"))
            o.append(sun(m(cx), m(top - 9), m(4.5), colour))
            label_y = top - 25
        elif option == "B":                     # event under, its band showing below the leader
            o.append(f'<rect x="{m(sx - 2)}" y="{m(top - 2)}" width="{m(cw + 4)}" height="{m(88 + 30 + 4)}" rx="{m(4)}" fill="#000" opacity=".12"/>')
            o.append(event_card(sx, top + 30, stage, types, twist, band_at="bottom", uid=i))
            o.append(leader_card(sx, top, name, portrait, cost, f"b{i}"))
            o.append(sun(m(cx), m(top - 9), m(4.5), colour))
            label_y = top - 25
        else:                                   # side by side: leader and a mini event
            ex = cx + cw / 2 - 18
            lx = cx - cw / 2 - 26
            o.append(f'<rect x="{m(lx - 2)}" y="{m(top - 2)}" width="{m(cw + 50)}" height="{m(92)}" rx="{m(4)}" fill="#000" opacity=".12"/>')
            o.append(leader_card(lx, top, name, portrait, cost, f"c{i}"))
            o.append(event_card(lx + cw + 3, top + 12, stage, types, twist, w=44, h=63, uid=i))
            o.append(sun(m(lx + cw + 25), m(top + 3), m(4), colour))
            label_y = top - 12
        o.append(f'<text x="{m(cx)}" y="{m(label_y)}" class="t" font-size="{m(6)}" fill="{TEAL}" text-anchor="middle">{slot}</text>')
        o.append(f'<text x="{m(cx)}" y="{m(label_y + 5)}" class="b" font-size="{m(3.4)}" fill="{TEAL}" text-anchor="middle" font-weight="700">{action}</text>')
    # the event deck before Dawn and the way to the Wall after Dusk
    dx = ox + 6
    for k in range(4):
        o.append(f'<rect x="{m(dx + k * 0.6)}" y="{m(hy - 30 - k * 0.6)}" width="{m(26)}" height="{m(36)}" rx="{m(2)}" fill="{TEAL}" stroke="{GOLD}" stroke-width="1.2"/>')
    o.append(f'<text x="{m(dx + 14)}" y="{m(hy + 12)}" class="b" font-size="{m(3)}" fill="{CREAM}" text-anchor="middle" font-weight="700">event deck</text>')
    o.append(f'<text x="{m(ox + W - 6)}" y="{m(hy + 12)}" class="b" font-size="{m(3)}" fill="{CREAM}" text-anchor="end" font-weight="700">to the Wall →</text>')
    o.append(f'<text x="{m(ox + W / 2)}" y="{m(hy + 12)}" class="b" font-size="{m(3)}" fill="{CREAM}" text-anchor="middle">resolve Dusk, then Day, then Dawn · then everyone moves one step along the sun</text>')
    o.append("</g>")
    return "".join(o)


def sheet():
    specs = [("A", "A · Tucked: the event slides behind the leader; its band (stage, section types, twist) shows above.", 360, 202),
             ("B", "B · Event below: the event slides under the leader; its band shows at the horizon.", 360, 200),
             ("C", "C · Side by side: a mini event card (44 × 63 mm) beside each leader; nothing overlaps.", 460, 162)]
    Wsheet = 500
    y = 20
    body = []
    for opt, caption, W, H in specs:
        body.append(f'<text x="{m(20)}" y="{m(y + 6)}" class="t" font-size="{m(6)}" fill="{TEAL}">{caption}</text>')
        body.append(f'<text x="{m(20)}" y="{m(y + 13)}" class="b" font-size="{m(3.6)}" fill="#4A4F55">board {W} × {H} mm</text>')
        body.append(board((Wsheet - W) / 2, y + 18, W, H, opt))
        y += H + 40
    Hs = y
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{m(Wsheet)}" height="{m(Hs)}" viewBox="0 0 {m(Wsheet)} {m(Hs)}">{defs()}'
            f'<rect width="{m(Wsheet)}" height="{m(Hs)}" fill="#EDE6D8"/>{"".join(body)}</svg>'), (m(Wsheet), m(Hs))


def render_board(option, px_per_mm, out):
    """Render one board alone (transparent outside its rounded edge) at px_per_mm, for the mock-up."""
    global S
    W, H = {"A": (360, 202), "B": (360, 200), "C": (460, 162)}[option]
    old, S = S, px_per_mm
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{m(W)}" height="{m(H)}" viewBox="0 0 {m(W)} {m(H)}">{defs()}'
           f'{board(0, 0, W, H, option)}</svg>')
    S = old
    f = Path(out).with_suffix(".svg")
    f.write_text(svg)
    w, h = round(W * px_per_mm), round(H * px_per_mm)
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{w},height:{h}}},deviceScaleFactor:1}});"
          f"await p.goto('{f.as_uri()}');await p.waitForTimeout(500);await p.screenshot({{path:'{out}',omitBackground:true}});await b.close();}})();")
    subprocess.run(["node", "-e", js], check=True)
    f.unlink()
    return Path(out)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    svg, (w, h) = sheet()
    f = OUT / "conveyor_options.svg"
    f.write_text(svg)
    png = OUT / "conveyor_options.png"
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{int(w)},height:{int(h)}}},deviceScaleFactor:1}});"
          f"await p.goto('{f.as_uri()}');await p.waitForTimeout(500);await p.screenshot({{path:'{png}'}});await b.close();}})();")
    subprocess.run(["node", "-e", js], check=True)
    print("wrote", f.relative_to(ROOT), "and", png.relative_to(ROOT))


if __name__ == "__main__":
    main()
