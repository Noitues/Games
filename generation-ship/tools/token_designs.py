"""Hand-coded SVG concepts for the physical pieces: the machine in grey plastic, the people in wood.

    python3 tools/token_designs.py   -> art/tokens/token_sheet.svg (+ .png, rendered with Playwright)

Every piece is drawn from its real size in millimetres (SIZES), shown at SCALE px per mm:
- Threat (grey cast plastic, one colour): Glitch = a hex nut lying flat; Fault = a cog standing on
  its edge with a snapped tooth; Failure = a cracked vacuum tube in its socket. Flat -> wheel -> tower.
- People (wood): Crew = a pawn with a fishbowl helmet; house influence = rocket nose cones.
- Decay = a lump of slag; Breakthrough = a brass starburst coin.
The sheet shows each piece from the side and from above, a black-silhouette test, and the pieces on
the four section colours. Concept only: the numbers here are starting points for a sculptor.
"""
import math
import random
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "art" / "tokens"
SCALE = 10                     # px per mm on the sheet
SIZES = {                      # mm
    "glitch": {"across_flats": 12, "height": 5, "hole": 5},
    "fault": {"diameter": 16, "teeth": 10, "thickness": 4, "base_w": 11, "base_h": 2.2},
    "failure": {"height": 22, "bulb_w": 10.5, "socket_w": 12, "socket_h": 5},
    "crew": {"height": 18, "base": 12, "head": 6, "helmet": 9.5},
    "influence": {"base": 11, "height": 13},
    "decay": {"size": 13, "height": 6},
    "breakthrough": {"diameter": 20, "rays": 8},
}
HOUSE = ["#2F5DB8", "#C8323C", "#E8B23A", "#EDEBE4"]        # cobalt, cherry, mustard, pearl (wood stain)
SECTIONS = [("Infrastructure", "#3AB0A8"), ("Residential", "#F2A060"), ("Government", "#E88AA0"), ("Agricultural", "#A8C860")]
INK = "#2B2F33"


def mmv(v):
    return v * SCALE


def defs():
    return """<defs>
  <linearGradient id="plastic" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C9CDD1"/><stop offset=".55" stop-color="#9A9FA5"/><stop offset="1" stop-color="#6E7379"/></linearGradient>
  <linearGradient id="plasticSide" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7E848A"/><stop offset=".35" stop-color="#C4C8CC"/><stop offset=".7" stop-color="#9DA2A8"/><stop offset="1" stop-color="#6A6F75"/></linearGradient>
  <radialGradient id="glass" cx=".38" cy=".3" r=".75"><stop offset="0" stop-color="#E4E7EA"/><stop offset=".5" stop-color="#ADB2B8"/><stop offset="1" stop-color="#7A8086"/></radialGradient>
  <linearGradient id="wood" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B98A55"/><stop offset=".4" stop-color="#E2BE8A"/><stop offset="1" stop-color="#A8783F"/></linearGradient>
  <radialGradient id="brass" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#FFE7A0"/><stop offset=".45" stop-color="#D9A848"/><stop offset="1" stop-color="#8F6420"/></radialGradient>
  <linearGradient id="slag" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5A463C"/><stop offset=".6" stop-color="#2E2420"/><stop offset="1" stop-color="#1C1614"/></linearGradient>
  <filter id="shadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="2.5" dy="3" stdDeviation="2.5" flood-color="#000" flood-opacity=".35"/></filter>
</defs>"""


def poly(points):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


# --- the machine (grey plastic) -------------------------------------------------------------------
def glitch_top(cx, cy, solid=None):
    s = SIZES["glitch"]
    r = mmv(s["across_flats"]) / math.sqrt(3)                  # circumradius from across-flats
    hexa = [(cx + r * math.cos(math.radians(60 * k)), cy + r * math.sin(math.radians(60 * k))) for k in range(6)]
    if solid:
        return f'<polygon points="{poly(hexa)}" fill="{solid}"/><circle cx="{cx}" cy="{cy}" r="{mmv(s["hole"]) / 2}" fill="#fff"/>'
    inner = [(cx + 0.82 * (x - cx), cy + 0.82 * (y - cy)) for x, y in hexa]
    return (f'<g filter="url(#shadow)"><polygon points="{poly(hexa)}" fill="url(#plastic)" stroke="{INK}" stroke-width="1.6"/>'
            f'<polygon points="{poly(inner)}" fill="none" stroke="#E6E8EA" stroke-width="1" opacity=".7"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{mmv(s["hole"]) / 2}" fill="#4A4F55" stroke="{INK}" stroke-width="1.4"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{mmv(s["hole"]) / 2 - 3}" fill="none" stroke="#7A8086" stroke-width="1" stroke-dasharray="3 2"/>'
            f'<path d="M{cx + r * .35},{cy - r * .5} l{r * .18},{r * .14}" stroke="{INK}" stroke-width="1.2"/></g>')


def glitch_side(cx, by, solid=None):
    """Side view: across corners wide, height tall, standing on the line by."""
    s = SIZES["glitch"]
    w = mmv(s["across_flats"]) * 2 / math.sqrt(3)
    h = mmv(s["height"])
    c = h * 0.22
    pts = [(cx - w / 2, by), (cx + w / 2, by), (cx + w / 2, by - h + c), (cx + w / 2 - c, by - h), (cx - w / 2 + c, by - h), (cx - w / 2, by - h + c)]
    if solid:
        return f'<polygon points="{poly(pts)}" fill="{solid}"/>'
    return (f'<g filter="url(#shadow)"><polygon points="{poly(pts)}" fill="url(#plasticSide)" stroke="{INK}" stroke-width="1.6"/>'
            f'<line x1="{cx - w / 4}" y1="{by}" x2="{cx - w / 4}" y2="{by - h}" stroke="{INK}" stroke-width="1"/>'
            f'<line x1="{cx + w / 4}" y1="{by}" x2="{cx + w / 4}" y2="{by - h}" stroke="{INK}" stroke-width="1"/></g>')


def cog_outline(cx, cy):
    s = SIZES["fault"]
    R = mmv(s["diameter"]) / 2
    r_root = R * 0.78
    n = s["teeth"]
    pts = []
    for k in range(n):
        a0 = 2 * math.pi * k / n - math.pi / 2
        step = 2 * math.pi / n
        tip = R if k != 2 else r_root * 1.06                     # tooth 2 is snapped off (a stub)
        for frac, rad in ((0.0, r_root), (0.12, tip), (0.42, tip), (0.54, r_root)):
            a = a0 + frac * step
            pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    return pts, R


def fault_side(cx, by, solid=None):
    """Elevation: the cog standing on its edge in a little plinth (the footprint a token needs)."""
    s = SIZES["fault"]
    pts, R = cog_outline(cx, by - mmv(s["base_h"]) - mmv(s["diameter"]) / 2 + 3)
    cy = by - mmv(s["base_h"]) - R + 3
    bw, bh = mmv(s["base_w"]), mmv(s["base_h"])
    base = f'<rect x="{cx - bw / 2}" y="{by - bh}" width="{bw}" height="{bh}" rx="3"'
    if solid:
        return f'<polygon points="{poly(pts)}" fill="{solid}"/>{base} fill="{solid}"/>'
    # the snapped tooth: a jagged stub, and a hairline crack running in from it
    a = 2 * math.pi * 2.27 / s["teeth"] - math.pi / 2
    crack = [(cx + R * 0.8 * math.cos(a), cy + R * 0.8 * math.sin(a)), (cx + R * 0.6 * math.cos(a + .1), cy + R * 0.6 * math.sin(a + .1)),
             (cx + R * 0.5 * math.cos(a - .05), cy + R * 0.5 * math.sin(a - .05)), (cx + R * 0.38 * math.cos(a + .12), cy + R * 0.38 * math.sin(a + .12))]
    return (f'<g filter="url(#shadow)">{base} fill="url(#plasticSide)" stroke="{INK}" stroke-width="1.6"/>'
            f'<polygon points="{poly(pts)}" fill="url(#plastic)" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{R * .55}" fill="none" stroke="#E2E5E8" stroke-width="1.2" opacity=".7"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{R * .22}" fill="#4A4F55" stroke="{INK}" stroke-width="1.4"/>'
            + "".join(f'<circle cx="{cx + R * .42 * math.cos(2 * math.pi * k / 5)}" cy="{cy + R * .42 * math.sin(2 * math.pi * k / 5)}" r="{R * .07}" fill="#6E7379"/>' for k in range(5))
            + f'<polyline points="{poly(crack)}" fill="none" stroke="{INK}" stroke-width="1.3"/></g>')


def fault_top(cx, cy, solid=None):
    """From above: the plinth, and the cog's toothed edge seen end-on."""
    s = SIZES["fault"]
    bw, t = mmv(s["base_w"]), mmv(s["thickness"])
    R = mmv(s["diameter"]) / 2
    plinth = f'<rect x="{cx - bw / 2}" y="{cy - t * .9}" width="{bw}" height="{t * 1.8}" rx="3"'
    teeth = "".join(f'<rect x="{cx - R + k * (2 * R / 7) + 2}" y="{cy - t / 2}" width="{2 * R / 7 - 5}" height="{t}" rx="1.5"/>' for k in range(7))
    if solid:
        return f'{plinth} fill="{solid}"/><g fill="{solid}">{teeth}</g><rect x="{cx - R + 2}" y="{cy - t / 4}" width="{2 * R - 4}" height="{t / 2}" fill="{solid}"/>'
    return (f'<g filter="url(#shadow)">{plinth} fill="url(#plasticSide)" stroke="{INK}" stroke-width="1.4"/>'
            f'<rect x="{cx - R + 2}" y="{cy - t / 4}" width="{2 * R - 4}" height="{t / 2}" fill="#8A9096" stroke="{INK}" stroke-width="1.2"/>'
            f'<g fill="url(#plastic)" stroke="{INK}" stroke-width="1.2">{teeth}</g></g>')


def failure_side(cx, by, solid=None):
    s = SIZES["failure"]
    H, bw, sw, sh = mmv(s["height"]), mmv(s["bulb_w"]), mmv(s["socket_w"]), mmv(s["socket_h"])
    top = by - H
    bulb = (f"M{cx - bw / 2},{by - sh} L{cx - bw / 2},{top + bw * .55} "
            f"C{cx - bw / 2},{top + bw * .05} {cx - bw * .2},{top + mmv(1.6)} {cx - mmv(0.9)},{top + mmv(1.4)} "
            f"L{cx - mmv(0.6)},{top} L{cx + mmv(0.6)},{top} L{cx + mmv(0.9)},{top + mmv(1.4)} "
            f"C{cx + bw * .2},{top + mmv(1.6)} {cx + bw / 2},{top + bw * .05} {cx + bw / 2},{top + bw * .55} L{cx + bw / 2},{by - sh} Z")
    sock = f'<path d="M{cx - sw / 2},{by} L{cx - sw / 2},{by - sh + 4} Q{cx - sw / 2},{by - sh} {cx - sw / 2 + 4},{by - sh} L{cx + sw / 2 - 4},{by - sh} Q{cx + sw / 2},{by - sh} {cx + sw / 2},{by - sh + 4} L{cx + sw / 2},{by} Z"'
    if solid:
        return f'<path d="{bulb}" fill="{solid}"/>{sock} fill="{solid}"/>'
    # inside the glass: the plate (anode), a broken filament, and a crack across the envelope
    plate = f'<rect x="{cx - bw * .28}" y="{top + bw * .55}" width="{bw * .56}" height="{H * .42}" rx="2" fill="#80868C" stroke="{INK}" stroke-width="1" opacity=".9"/>'
    fil = f'<polyline points="{cx - 4},{by - sh - 4} {cx - 4},{top + bw * .75} {cx + 1},{top + bw * .62}" fill="none" stroke="{INK}" stroke-width="1.3"/>' \
          f'<polyline points="{cx + 4},{by - sh - 4} {cx + 4},{top + bw * .9}" fill="none" stroke="{INK}" stroke-width="1.3"/>'
    crack = f'<polyline points="{cx - bw / 2 + 1},{top + H * .32} {cx - bw * .18},{top + H * .38} {cx - bw * .05},{top + H * .3} {cx + bw * .14},{top + H * .4} {cx + bw * .3},{top + H * .34}" fill="none" stroke="{INK}" stroke-width="1.4"/>'
    pins = "".join(f'<rect x="{cx + d - 1.5}" y="{by - 1}" width="3" height="4" fill="#6E7379"/>' for d in (-sw * .3, -sw * .1, sw * .1, sw * .3))
    return (f'<g filter="url(#shadow)">{pins}<path d="{bulb}" fill="url(#glass)" stroke="{INK}" stroke-width="1.6"/>{plate}{fil}{crack}'
            f'<path d="M{cx - bw * .32},{top + bw * .5} Q{cx - bw * .36},{top + H * .45} {cx - bw * .3},{by - sh - 8}" fill="none" stroke="#F4F6F8" stroke-width="2" opacity=".7"/>'
            f'{sock} fill="url(#plasticSide)" stroke="{INK}" stroke-width="1.6"/>'
            f'<line x1="{cx - sw / 2}" y1="{by - sh * .45}" x2="{cx + sw / 2}" y2="{by - sh * .45}" stroke="{INK}" stroke-width="1"/></g>')


def failure_top(cx, cy, solid=None):
    s = SIZES["failure"]
    if solid:
        return f'<circle cx="{cx}" cy="{cy}" r="{mmv(s["socket_w"]) / 2}" fill="{solid}"/>'
    return (f'<g filter="url(#shadow)"><circle cx="{cx}" cy="{cy}" r="{mmv(s["socket_w"]) / 2}" fill="url(#plasticSide)" stroke="{INK}" stroke-width="1.5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{mmv(s["bulb_w"]) / 2}" fill="url(#glass)" stroke="{INK}" stroke-width="1.4"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{mmv(0.8)}" fill="#6E7379" stroke="{INK}"/>'
            f'<polyline points="{cx - mmv(4)},{cy - 3} {cx - mmv(1.5)},{cy + 4} {cx + mmv(1)},{cy - 2} {cx + mmv(3.5)},{cy + 5}" fill="none" stroke="{INK}" stroke-width="1.3"/></g>')


# --- the people (wood) -----------------------------------------------------------------------------
def crew_side(cx, by, solid=None):
    s = SIZES["crew"]
    H, B, hd, hm = mmv(s["height"]), mmv(s["base"]), mmv(s["head"]), mmv(s["helmet"])
    hy = by - H + hm / 2
    body = (f"M{cx - B / 2},{by} Q{cx - B / 2},{by - mmv(2)} {cx - B * .36},{by - mmv(2.4)} "
            f"L{cx - B * .2},{hy + hm * .45} L{cx + B * .2},{hy + hm * .45} L{cx + B * .36},{by - mmv(2.4)} Q{cx + B / 2},{by - mmv(2)} {cx + B / 2},{by} Z")
    if solid:
        return f'<path d="{body}" fill="{solid}"/><circle cx="{cx}" cy="{hy}" r="{hm / 2}" fill="{solid}"/>'
    grain = "".join(f'<path d="M{cx + d},{by - 2} Q{cx + d * 1.4},{by - H * .3} {cx + d * .7},{hy + hm * .5}" fill="none" stroke="#9A6A35" stroke-width=".8" opacity=".5"/>' for d in (-B * .22, -B * .05, B * .14))
    return (f'<g filter="url(#shadow)"><path d="{body}" fill="url(#wood)" stroke="#5A3A1C" stroke-width="1.5"/>{grain}'
            f'<rect x="{cx - B * .26}" y="{hy + hm * .4}" width="{B * .52}" height="{mmv(1.2)}" rx="3" fill="#C99A62" stroke="#5A3A1C" stroke-width="1.2"/>'
            f'<circle cx="{cx}" cy="{hy}" r="{hd / 2}" fill="url(#wood)" stroke="#5A3A1C" stroke-width="1.4"/>'
            f'<circle cx="{cx}" cy="{hy}" r="{hm / 2}" fill="#DDEFF2" fill-opacity=".28" stroke="#5A3A1C" stroke-width="1.6"/>'
            f'<path d="M{cx - hm * .3},{hy - hm * .22} Q{cx - hm * .18},{hy - hm * .38} {cx},{hy - hm * .4}" fill="none" stroke="#fff" stroke-width="2" opacity=".8"/></g>')


def crew_top(cx, cy, solid=None):
    s = SIZES["crew"]
    if solid:
        return f'<circle cx="{cx}" cy="{cy}" r="{mmv(s["base"]) / 2}" fill="{solid}"/>'
    return (f'<g filter="url(#shadow)"><circle cx="{cx}" cy="{cy}" r="{mmv(s["base"]) / 2}" fill="url(#wood)" stroke="#5A3A1C" stroke-width="1.4"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{mmv(s["helmet"]) / 2}" fill="#DDEFF2" fill-opacity=".3" stroke="#5A3A1C" stroke-width="1.4"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{mmv(s["head"]) / 2}" fill="url(#wood)" stroke="#5A3A1C" stroke-width="1.2"/></g>')


def influence_side(cx, by, colour, solid=None):
    s = SIZES["influence"]
    B, H = mmv(s["base"]), mmv(s["height"])
    ring = mmv(1.6)
    cone = f"M{cx - B * .44},{by - ring} C{cx - B * .44},{by - H * .55} {cx - B * .18},{by - H * .92} {cx},{by - H} C{cx + B * .18},{by - H * .92} {cx + B * .44},{by - H * .55} {cx + B * .44},{by - ring} Z"
    base = f'<rect x="{cx - B / 2}" y="{by - ring}" width="{B}" height="{ring}" rx="2"'
    if solid:
        return f'<path d="{cone}" fill="{solid}"/>{base} fill="{solid}"/>'
    return (f'<g filter="url(#shadow)"><path d="{cone}" fill="{colour}" stroke="#3A2A1A" stroke-width="1.4"/>'
            f'<path d="{cone}" fill="url(#wood)" opacity=".28"/>'
            f'<path d="M{cx - B * .22},{by - ring - 3} C{cx - B * .24},{by - H * .5} {cx - B * .1},{by - H * .8} {cx - 2},{by - H * .9}" fill="none" stroke="#fff" stroke-width="1.6" opacity=".45"/>'
            f'{base} fill="{colour}" stroke="#3A2A1A" stroke-width="1.3"/></g>')


def decay_lump(cx, cy, seed=4, solid=None):
    r = random.Random(seed)
    R = mmv(SIZES["decay"]["size"]) / 2
    pts = []
    for k in range(11):
        a = 2 * math.pi * k / 11 + r.uniform(-.15, .15)
        rad = R * r.uniform(.72, 1.0)
        pts.append((cx + rad * math.cos(a), cy + rad * 0.82 * math.sin(a)))
    if solid:
        return f'<polygon points="{poly(pts)}" fill="{solid}" stroke="{solid}" stroke-width="4" stroke-linejoin="round"/>'
    pits = "".join(f'<circle cx="{cx + r.uniform(-R * .5, R * .5)}" cy="{cy + r.uniform(-R * .4, R * .4)}" r="{r.uniform(1.5, 3.5)}" fill="#120D0B"/>' for _ in range(7))
    rust = "".join(f'<circle cx="{cx + r.uniform(-R * .5, R * .5)}" cy="{cy + r.uniform(-R * .45, R * .2)}" r="{r.uniform(1.5, 3)}" fill="#8A4A24" opacity=".8"/>' for _ in range(5))
    return (f'<g filter="url(#shadow)"><polygon points="{poly(pts)}" fill="url(#slag)" stroke="#0E0A08" stroke-width="3" stroke-linejoin="round"/>{pits}{rust}'
            f'<path d="M{cx - R * .5},{cy - R * .35} Q{cx - R * .2},{cy - R * .62} {cx + R * .2},{cy - R * .5}" fill="none" stroke="#9A8270" stroke-width="1.6" opacity=".6"/></g>')


def breakthrough_coin(cx, cy, solid=None):
    s = SIZES["breakthrough"]
    R = mmv(s["diameter"]) / 2
    star = []
    n = s["rays"] * 2
    for k in range(n * 2):
        a = math.pi * k / n - math.pi / 2
        rad = (R * .78 if (k // 2) % 2 == 0 else R * .5) if k % 2 == 0 else R * .2
        star.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    if solid:
        return f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{solid}"/>'
    return (f'<g filter="url(#shadow)"><circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#brass)" stroke="#6A4810" stroke-width="1.6"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{R * .88}" fill="none" stroke="#7A5418" stroke-width="1.2"/>'
            f'<polygon points="{poly(star)}" fill="#F2CC6A" stroke="#7A5418" stroke-width="1.2" stroke-linejoin="round"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{R * .12}" fill="#FFF1C2" stroke="#7A5418"/></g>')


# --- the sheet ------------------------------------------------------------------------------------
def label(x, y, text, size=15, weight="normal", fill="#3A3F44", anchor="middle"):
    return f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{text}</text>'


def sheet():
    W, H = 1800, 1320
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', defs(),
         f'<rect width="{W}" height="{H}" fill="#EDE6D8"/>',
         label(60, 62, "Generation Ship · piece concepts", 30, "bold", "#0F3A48", "start"),
         label(60, 92, "The machine is grey cast plastic; the people are wood. Threat escalates by silhouette: flat → wheel → tower. Drawn to scale, 10 px = 1 mm.", 16, "normal", "#4A4F55", "start")]
    # scale bar
    o.append(f'<rect x="1590" y="70" width="{mmv(10)}" height="8" fill="#0F3A48"/>' + label(1640, 100, "10 mm", 14))

    # Row 1: threat, side and top views
    o.append(label(60, 150, "THE MACHINE  ·  threat pieces, one grey plastic", 18, "bold", "#0F3A48", "start"))
    base = 330
    cols = [(240, "Glitch", "hex nut, lying flat · 12 mm", glitch_side, glitch_top),
            (620, "Fault", "cog on its edge, a snapped tooth · 16 mm", fault_side, fault_top),
            (1000, "Failure", "cracked vacuum tube in its socket · 22 mm", failure_side, failure_top)]
    for x, name, desc, side, top in cols:
        o.append(f'<line x1="{x - 150}" y1="{base}" x2="{x + 150}" y2="{base}" stroke="#B9AE98" stroke-width="2"/>')
        o.append(side(x - 70, base))
        o.append(top(x + 80, base - 60))
        o.append(label(x - 70, base + 28, "side", 13, fill="#7A7468") + label(x + 80, base + 28, "above", 13, fill="#7A7468"))
        o.append(label(x, base + 62, name, 22, "bold", "#2B2F33") + label(x, base + 86, desc, 14))
    # escalation arrows
    for x in (430, 810):
        o.append(f'<path d="M{x - 20},{base - 60} L{x + 20},{base - 60}" stroke="#E8603A" stroke-width="3" marker-end="url(#a)"/>'
                 f'<polygon points="{x + 20},{base - 66} {x + 30},{base - 60} {x + 20},{base - 54}" fill="#E8603A"/>')

    # Row 1 right: silhouette test, at half scale (about how they look from across the table)
    o.append(label(1220, 150, "SILHOUETTE TEST  ·  black, half scale", 18, "bold", "#0F3A48", "start"))
    o.append(f'<g transform="translate(1250,{base}) scale(.5)">')
    for i, f in enumerate((glitch_side, fault_side, failure_side, crew_side)):
        o.append(f(110 + i * 230, 0, solid="#1E2226"))
    o.append("</g>")
    o.append(f'<line x1="1210" y1="{base}" x2="1740" y2="{base}" stroke="#B9AE98" stroke-width="2"/>')
    o.append(label(1475, base + 62, "Each reads with no colour at all; the wooden", 14) +
             label(1475, base + 84, "Crew (round head) never reads as threat.", 14))

    # Row 2: people pieces
    o.append(label(60, 500, "THE PEOPLE  ·  wood, brass and slag", 18, "bold", "#0F3A48", "start"))
    base2 = 690
    o.append(f'<line x1="90" y1="{base2}" x2="1740" y2="{base2}" stroke="#B9AE98" stroke-width="2"/>')
    o.append(crew_side(180, base2) + crew_top(300, base2 - 60))
    o.append(label(240, base2 + 62, "Crew", 22, "bold", "#2B2F33") + label(240, base2 + 86, "wooden pawn, fishbowl helmet · 18 mm", 14))
    for i, c in enumerate(HOUSE):
        o.append(influence_side(520 + i * 105, base2, c))
    o.append(label(677, base2 + 62, "House influence", 22, "bold", "#2B2F33") + label(677, base2 + 86, "stained wooden rocket nose cones · 11 mm", 14))
    o.append(decay_lump(990, base2 - 40, 4) + decay_lump(1090, base2 - 34, 9))
    o.append(label(1040, base2 + 62, "Decay", 22, "bold", "#2B2F33") + label(1040, base2 + 86, "slag lump, never two the same · 13 mm", 14))
    o.append(breakthrough_coin(1370, base2 - 100))
    o.append(label(1370, base2 + 62, "Breakthrough", 22, "bold", "#2B2F33") + label(1370, base2 + 86, "brass starburst coin · 20 mm", 14))

    # Row 3: on the four section colours
    o.append(label(60, 860, "ON THE BOARD  ·  the same pieces on every section colour (pieces at 55 %)", 18, "bold", "#0F3A48", "start"))
    for i, (name, col) in enumerate(SECTIONS):
        x0 = 90 + i * 415
        o.append(f'<rect x="{x0}" y="890" width="380" height="330" rx="22" fill="{col}" stroke="#FBEFD6" stroke-width="5"/>')
        o.append(f'<rect x="{x0 + 30}" y="918" width="320" height="274" rx="18" fill="#000" opacity=".06"/>')
        o.append(f'<g transform="translate({x0},890) scale(.55)">')   # a section is ~70 x 60 mm here
        o.append(glitch_top(130, 130) + glitch_top(290, 110))
        o.append(fault_side(500, 300))
        o.append(failure_side(590, 560) if i in (0, 2) else glitch_top(580, 470))
        o.append(crew_side(130, 540) + crew_side(260, 560))
        o.append(influence_side(400, 555, HOUSE[i % 2]))
        if i == 1:
            o.append(decay_lump(450, 420, 12))
        o.append("</g>")
        o.append(label(x0 + 190, 1250, name, 16, "bold", "#2B2F33"))
    o.append(label(60, 1295, "Print-and-play: Glitch, Crew, influence and Decay die-cut to their top outline; Fault and Failure as small standees of their side view.", 15, "normal", "#4A4F55", "start"))
    o.append("</svg>")
    return "\n".join(o)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    svg = OUT / "token_sheet.svg"
    svg.write_text(sheet())
    png = OUT / "token_sheet.png"
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:1800,height:1320}},deviceScaleFactor:1}});"
          f"await p.goto('file://{svg}');await p.screenshot({{path:'{png}'}});await b.close();}})();")
    subprocess.run(["node", "-e", js], check=True)
    print("wrote", svg.relative_to(ROOT), "and", png.relative_to(ROOT))


if __name__ == "__main__":
    main()
