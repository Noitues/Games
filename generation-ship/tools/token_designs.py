"""Hand-coded SVG concepts for the physical pieces: the machine in grey plastic, the people in wood.

    python3 tools/token_designs.py   -> art/tokens/token_sheet.svg (+ .png, rendered with Playwright)

Every piece is drawn from its real size in millimetres (SIZES), shown at SCALE px per mm:
- Threat (grey cast plastic, one colour): Glitch = a hex nut lying flat; Fault = a cog standing on
  its edge with a snapped tooth; Failure = a cracked vacuum tube in its socket. Flat -> wheel -> tower.
- People (wood): Crew = a pawn with a fishbowl helmet; house influence = rocket nose cones.
- Decay = a lump of slag; Breakthrough = a brass starburst coin.
Damage states (GDD "Threat pieces": damage clears at Time passes) use no extra parts, only the way a
piece sits: a damaged Fault (health 2) lies flat; a Failure (health 3) lies on its side at 1 damage and
stands upside down at 2; an injured Crew (health 2) lies on its side; Glitch (health 1) has no state.
The shapes are made for it: the cog has a flat-ground foot, the tube an octagonal ("octal") socket
so it cannot roll, and a flat top cap so it stands upside down. A downgrade replaces the piece with an
undamaged one standing upright (damage does not carry over). Isolate is a wooden lockout tag.
The sheet shows each piece from the side and from above in every state, a black-silhouette test, and
the pieces on the four section colours. Concept only: the numbers are starting points for a sculptor.
"""
import math
import random
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "art" / "tokens"
SCALE = 10                     # px per mm on the sheet
SIZES = {                      # mm
    "glitch": {"across_flats": 10, "height": 4.2, "hole": 4.2},
    "fault": {"diameter": 14, "teeth": 10, "thickness": 3.5, "foot": 0.84},   # foot: flat at 0.84 R below centre
    "failure": {"height": 23, "bulb_w": 9.5, "neck_w": 5.5, "neck_h": 2.6, "socket_w": 12.5, "socket_h": 5.2,
                "cap_w": 5.6, "cap_h": 1.6},                    # octal socket; flat top cap to stand upside down
    "crew": {"height": 16, "base": 11, "head": 5.4, "helmet": 8.5},
    "influence": {"base": 10, "height": 12},
    "decay": {"size": 12, "height": 5.5},
    "breakthrough": {"diameter": 18, "rays": 8},
    "isolate": {"w": 6, "h": 8.5},
}
ACCENT, DAMAGE_INK = "#E8763A", "#8A3A16"
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
    """The cog's face: 10 teeth, one snapped off (tooth 2), and the bottom ground flat as a foot."""
    s = SIZES["fault"]
    R = mmv(s["diameter"]) / 2
    r_root = R * 0.78
    n = s["teeth"]
    foot = cy + R * s["foot"]
    pts = []
    for k in range(n):
        a0 = 2 * math.pi * k / n - math.pi / 2
        step = 2 * math.pi / n
        tip = R if k != 2 else r_root * 1.06
        for frac, rad in ((0.0, r_root), (0.12, tip), (0.42, tip), (0.54, r_root)):
            a = a0 + frac * step
            pts.append((cx + rad * math.cos(a), min(foot, cy + rad * math.sin(a))))
    return pts, R


def fault_face(cx, cy, solid=None):
    """The cog seen face-on, centred at (cx, cy)."""
    pts, R = cog_outline(cx, cy)
    if solid:
        return f'<polygon points="{poly(pts)}" fill="{solid}"/>'
    s = SIZES["fault"]
    a = 2 * math.pi * 2.27 / s["teeth"] - math.pi / 2
    crack = [(cx + R * k * math.cos(a + d), cy + R * k * math.sin(a + d)) for k, d in ((.8, 0), (.6, .1), (.5, -.05), (.4, .12))]
    return (f'<polygon points="{poly(pts)}" fill="url(#plastic)" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{R * .58}" fill="none" stroke="#E2E5E8" stroke-width="1.2" opacity=".7"/>'
            + "".join(f'<circle cx="{cx + R * .44 * math.cos(2 * math.pi * (k + .5) / 5)}" cy="{cy + R * .44 * math.sin(2 * math.pi * (k + .5) / 5)}" r="{R * .07}" fill="#6E7379"/>' for k in range(5))
            + f'<circle cx="{cx}" cy="{cy}" r="{R * .2}" fill="#4A4F55" stroke="{INK}" stroke-width="1.4"/>'
            f'<polyline points="{poly(crack)}" fill="none" stroke="{INK}" stroke-width="1.3"/>')


def fault_edge(cx, cy, solid=None):
    """The cog seen edge-on (a toothed slab), centred at (cx, cy), long axis horizontal."""
    s = SIZES["fault"]
    R, t = mmv(s["diameter"]) / 2, mmv(s["thickness"])
    teeth = "".join(f'<rect x="{cx - R + k * (2 * R / 7) + 2}" y="{cy - t / 2}" width="{2 * R / 7 - 5}" height="{t}" rx="1.5"/>' for k in range(7))
    core = f'<rect x="{cx - R * .8}" y="{cy - t / 2}" width="{R * 1.6}" height="{t}" rx="2"'
    if solid:
        return f'<g fill="{solid}">{teeth}</g>{core} fill="{solid}"/>'
    return (f'{core} fill="#8A9096" stroke="{INK}" stroke-width="1.2"/>'
            f'<g fill="url(#plasticSide)" stroke="{INK}" stroke-width="1.2">{teeth}</g>')


def fault_side(cx, by, solid=None, damage=0):
    """Side view standing on the line by: upright on its foot (healthy) or lying flat (1 damage)."""
    s = SIZES["fault"]
    R = mmv(s["diameter"]) / 2
    if damage:
        return f'<g filter="url(#shadow)">{fault_edge(cx, by - mmv(s["thickness"]) / 2, solid)}</g>'
    return f'<g filter="url(#shadow)">{fault_face(cx, by - R * s["foot"], solid)}</g>'


def fault_top(cx, cy, solid=None, damage=0):
    """From above: an edge-on slab when upright, the whole toothed face when lying flat."""
    return f'<g filter="url(#shadow)">{fault_face(cx, cy, solid) if damage else fault_edge(cx, cy, solid)}</g>'


def tube(cx, by, solid=None):
    """The vacuum tube standing upright on the line by (the healthy Failure)."""
    s = SIZES["failure"]
    H, bw, sw, sh = mmv(s["height"]), mmv(s["bulb_w"]), mmv(s["socket_w"]), mmv(s["socket_h"])
    nw, nh, cw, ch = mmv(s["neck_w"]), mmv(s["neck_h"]), mmv(s["cap_w"]), mmv(s["cap_h"])
    top = by - H
    gt = top + ch                                         # top of the glass, under the cap
    nt = by - sh - nh                                     # top of the neck
    bulb = (f"M{cx - nw / 2},{by - sh} L{cx - nw / 2},{nt} C{cx - nw / 2},{nt - mmv(1)} {cx - bw / 2},{nt - mmv(1.2)} {cx - bw / 2},{nt - mmv(2.6)} "
            f"L{cx - bw / 2},{gt + mmv(4.2)} C{cx - bw / 2},{gt + mmv(1.2)} {cx - cw * .9},{gt} {cx - cw / 2},{gt} L{cx + cw / 2},{gt} C{cx + cw * .9},{gt} {cx + bw / 2},{gt + mmv(1.2)} {cx + bw / 2},{gt + mmv(4.2)} "
            f"L{cx + bw / 2},{nt - mmv(2.6)} C{cx + bw / 2},{nt - mmv(1.2)} {cx + nw / 2},{nt - mmv(1)} {cx + nw / 2},{nt} L{cx + nw / 2},{by - sh} Z")
    sock = f'<rect x="{cx - sw / 2}" y="{by - sh}" width="{sw}" height="{sh}" rx="2"'
    cap = f'<rect x="{cx - cw / 2}" y="{top}" width="{cw}" height="{ch + 1}" rx="2"'
    if solid:
        return f'<path d="{bulb}" fill="{solid}"/>{sock} fill="{solid}"/>{cap} fill="{solid}"/>'
    bt, bb = gt + mmv(3.6), nt - mmv(2.4)
    plate = f'<rect x="{cx - bw * .2}" y="{bt}" width="{bw * .4}" height="{bb - bt}" rx="1.5" fill="#868C92" stroke="{INK}" stroke-width="1" opacity=".75"/>'
    fil = (f'<polyline points="{cx - 3},{nt} {cx - 3},{bt + 10} {cx + 1},{bt + 2}" fill="none" stroke="{INK}" stroke-width="1.3"/>'
           f'<polyline points="{cx + 3},{nt} {cx + 3},{bt + 18}" fill="none" stroke="{INK}" stroke-width="1.3"/>')
    my = (bt + bb) / 2 + mmv(1)
    crack = (f'<polyline points="{cx + bw / 2 - 1},{my - mmv(2)} {cx + bw * .25},{my - mmv(1.2)} {cx + bw * .32},{my - mmv(.2)} '
             f'{cx + bw * .12},{my + mmv(.6)} {cx + bw * .2},{my + mmv(1.6)}" fill="none" stroke="{INK}" stroke-width="1.4"/>')
    facets = "".join(f'<line x1="{cx + d}" y1="{by - sh}" x2="{cx + d}" y2="{by}" stroke="{INK}" stroke-width="1"/>' for d in (-sw * .3, sw * .3))
    pins = "".join(f'<rect x="{cx + d - 1.5}" y="{by - 1}" width="3" height="4" fill="#6E7379"/>' for d in (-sw * .3, -sw * .1, sw * .1, sw * .3))
    return (f'{pins}<path d="{bulb}" fill="url(#glass)" stroke="{INK}" stroke-width="1.6"/>{plate}{fil}{crack}'
            f'<path d="M{cx - bw * .32},{bt} Q{cx - bw * .36},{(bt + bb) / 2} {cx - bw * .3},{bb}" fill="none" stroke="#F4F6F8" stroke-width="2" opacity=".7"/>'
            f'{cap} fill="url(#plasticSide)" stroke="{INK}" stroke-width="1.4"/>'
            f'{sock} fill="url(#plasticSide)" stroke="{INK}" stroke-width="1.6"/>{facets}')


def failure_side(cx, by, solid=None, damage=0):
    """Side view on the line by: upright (healthy), on its side (1 damage), upside down (2 damage)."""
    s = SIZES["failure"]
    H, sw = mmv(s["height"]), mmv(s["socket_w"])
    if damage == 1:      # lying on a flat of the octal socket; the bulb end rests lower
        return f'<g filter="url(#shadow)" transform="rotate(-90 {cx} {by - sw / 2}) translate(0 {sw / 2 - H / 2 + 0})"><g transform="translate(0 {H / 2 - sw / 2})">{tube(cx, by - sw / 2 + H / 2, solid)}</g></g>'
    if damage == 2:      # upside down, standing on the flat top cap; the socket and pins on top
        return f'<g filter="url(#shadow)" transform="translate(0 {2 * by - H}) scale(1 -1) translate(0 {-by})"><g transform="translate(0 {by - H / 2 - H / 2 + H})">{tube(cx, by, solid)}</g></g>'
    return f'<g filter="url(#shadow)">{tube(cx, by, solid)}</g>'


def octagon(cx, cy, r):
    return [(cx + r * math.cos(math.radians(22.5 + 45 * k)), cy + r * math.sin(math.radians(22.5 + 45 * k))) for k in range(8)]


def failure_top(cx, cy, solid=None, damage=0):
    """From above: upright = the cap inside the bulb inside the octal socket; on its side = the whole
    tube; upside down = the socket's base with its eight pins."""
    s = SIZES["failure"]
    sr = mmv(s["socket_w"]) / 2 / math.cos(math.radians(22.5))
    if damage == 1:
        H = mmv(s["height"])
        return f'<g filter="url(#shadow)" transform="rotate(-90 {cx} {cy})">{tube(cx, cy + H / 2, solid)}</g>'
    if solid:
        return f'<polygon points="{poly(octagon(cx, cy, sr))}" fill="{solid}"/>'
    sock = f'<polygon points="{poly(octagon(cx, cy, sr))}" fill="url(#plasticSide)" stroke="{INK}" stroke-width="1.5"/>'
    if damage == 2:
        pins = "".join(f'<circle cx="{cx + sr * .62 * math.cos(math.radians(45 * k))}" cy="{cy + sr * .62 * math.sin(math.radians(45 * k))}" r="3" fill="#5A5F65" stroke="{INK}"/>' for k in range(8))
        return (f'<g filter="url(#shadow)">{sock}<circle cx="{cx}" cy="{cy}" r="{sr * .62 + 6}" fill="none" stroke="#7E848A" stroke-width="1"/>{pins}'
                f'<circle cx="{cx}" cy="{cy}" r="{mmv(1.2)}" fill="#8A9096" stroke="{INK}" stroke-width="1.2"/>'
                f'<rect x="{cx - 2}" y="{cy - mmv(1.6)}" width="4" height="{mmv(0.8)}" fill="{INK}"/></g>')
    return (f'<g filter="url(#shadow)">{sock}<circle cx="{cx}" cy="{cy}" r="{mmv(s["bulb_w"]) / 2}" fill="url(#glass)" stroke="{INK}" stroke-width="1.4"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{mmv(s["cap_w"]) / 2}" fill="url(#plastic)" stroke="{INK}" stroke-width="1.3"/>'
            f'<polyline points="{cx - mmv(3.3)},{cy + mmv(2.6)} {cx - mmv(1)},{cy + mmv(3.4)} {cx + mmv(1.4)},{cy + mmv(2.4)}" fill="none" stroke="{INK}" stroke-width="1.3"/></g>')


def isolate_tag(cx, cy, angle=-14):
    """Isolate: a wooden lockout tag, cream with tangerine hazard stripes, leaning on the piece."""
    s = SIZES["isolate"]
    w, h = mmv(s["w"]), mmv(s["h"])
    stripes = "".join(f'<path d="M{cx - w / 2 + k * 10},{cy + h * .1} l10,0 l-12,{h * .4} l-10,0 Z" fill="{ACCENT}"/>' for k in range(-1, 7))
    return (f'<g transform="rotate({angle} {cx} {cy})" filter="url(#shadow)"><clipPath id="tag{int(cx)}{int(cy)}"><rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="5"/></clipPath>'
            f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="5" fill="#F3E4C4" stroke="#5A3A1C" stroke-width="1.5"/>'
            f'<g clip-path="url(#tag{int(cx)}{int(cy)})">{stripes}</g>'
            f'<circle cx="{cx}" cy="{cy - h * .28}" r="{mmv(0.9)}" fill="#5A3A1C"/>'
            f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="5" fill="none" stroke="#5A3A1C" stroke-width="1.5"/></g>')


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


def crew_injured(cx, by):
    """An injured Crew lies on its side (a small flat on the helmet keeps it from rolling)."""
    s = SIZES["crew"]
    B = mmv(s["base"])
    return f'<g transform="rotate(-90 {cx} {by - B / 2}) translate(0 {B / 2 - mmv(s["helmet"]) * .06})">{crew_side(cx, by)}</g>'


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


def ground(x0, x1, y):
    return f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#B9AE98" stroke-width="2"/>'


def head(x, y, text):
    return label(x, y, text, 18, "bold", "#0F3A48", "start")


def name(x, y, title, desc):
    return label(x, y, title, 22, "bold", "#2B2F33") + label(x, y + 24, desc, 14)


def sheet():
    W, H = 1800, 2010
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', defs(),
         f'<rect width="{W}" height="{H}" fill="#EDE6D8"/>',
         label(60, 62, "Generation Ship · piece concepts, v3", 30, "bold", "#0F3A48", "start"),
         label(60, 92, "The machine is grey cast plastic; the people are wood. Threat escalates by silhouette: flat → wheel → tower. "
               "Damage is shown by how a piece sits, with no extra parts.", 16, "normal", "#4A4F55", "start"),
         f'<rect x="1640" y="40" width="{mmv(10)}" height="8" fill="#0F3A48"/>', label(1690, 66, "10 mm, to scale", 13)]

    # Row 1: the machine, healthy, side and top
    base = 330
    o.append(head(60, 160, "THE MACHINE  ·  threat pieces, one grey plastic"))
    cols = [(240, "Glitch", "hex nut, lying flat · 10 mm · health 1", glitch_side, glitch_top),
            (620, "Fault", "cog on its edge, flat-ground foot · 14 mm · health 2", fault_side, fault_top),
            (1000, "Failure", "cracked octal tube, flat top cap · 23 mm · health 3", failure_side, failure_top)]
    for x, title, desc, side, top in cols:
        o.append(ground(x - 150, x + 150, base) + side(x - 70, base) + top(x + 80, base - 55))
        o.append(label(x - 70, base + 26, "side", 13, fill="#7A7468") + label(x + 80, base + 26, "above", 13, fill="#7A7468"))
        o.append(name(x, base + 60, title, desc))
    for x in (430, 810):
        o.append(f'<path d="M{x - 20},{base - 55} L{x + 18},{base - 55}" stroke="#0F3A48" stroke-width="3"/>'
                 f'<polygon points="{x + 18},{base - 61} {x + 28},{base - 55} {x + 18},{base - 49}" fill="#0F3A48"/>')
    o.append(head(1220, 160, "SILHOUETTE TEST  ·  black, half scale"))
    o.append(f'<g transform="translate(1250,{base}) scale(.5)">')
    for i, f in enumerate((glitch_side, fault_side, failure_side, crew_side)):
        o.append(f(110 + i * 230, 0, solid="#1E2226"))
    o.append("</g>" + ground(1210, 1740, base))
    o.append(label(1475, base + 60, "From above too, every piece differs:", 14) +
             label(1475, base + 82, "hexagon, slab, octagon, ring.", 14))

    # Row 2: damage states, side view
    base = 700
    o.append(head(60, 470, "DAMAGE STATES  ·  by how the piece sits; all stand up again at Time passes"))
    o.append(ground(80, 1740, base))
    states = [(150, fault_side, 0, "undamaged"), (300, fault_side, 1, "1 damage: lies flat"),
              (500, failure_side, 0, "undamaged"), (710, failure_side, 1, "1 damage: on its side"),
              (930, failure_side, 2, "2 damage: upside down")]
    for x, f, dmg, state in states:
        o.append(f(x, base, damage=dmg))
        o.append(label(x, base + 30, state, 14, "bold" if dmg else "normal", DAMAGE_INK if dmg else "#4A4F55"))
    o.append(label(225, base + 58, "Fault (health 2)", 15, "bold", "#2B2F33") + label(715, base + 58, "Failure (health 3)", 15, "bold", "#2B2F33"))
    o.append(crew_side(1170, base) + crew_injured(1300, base))
    o.append(label(1170, base + 30, "standing", 14) + label(1305, base + 30, "injured: on its side", 14, "bold", DAMAGE_INK))
    o.append(label(1235, base + 58, "Crew (health 2)", 15, "bold", "#2B2F33"))
    o.append(fault_side(1560, base) + isolate_tag(1620, base - 42))
    o.append(label(1590, base + 30, "Isolate", 14, "bold", DAMAGE_INK) + label(1590, base + 58, "lockout tag (a power, not damage)", 14))

    # Row 2b: the same states from above
    base = 900
    o.append(label(60, 812, "From above, as players see them on the board:", 15, "bold", "#4A4F55", "start"))
    tops = [(150, fault_top, 0, "upright: a slab"), (300, fault_top, 1, "flat: the whole cog"),
            (500, failure_top, 0, "upright: cap in an octagon"), (710, failure_top, 1, "on its side: the whole tube"),
            (930, failure_top, 2, "upside down: eight pins")]
    for x, f, dmg, cap in tops:
        o.append(f(x, base, damage=dmg) + label(x, base + 105, cap, 13, fill="#7A7468"))
    o.append(crew_top(1170, base) + crew_injured(1300, base + 45) + label(1235, base + 105, "a ring / a lying pawn", 13, fill="#7A7468"))
    o.append(label(60, 1036, "Rules: one damage tips a Fault flat; a Failure goes on its side, then upside down, and one more destroys it. "
                   "Glitch (health 1) has no state. A downgraded piece is replaced standing upright: damage does not carry over.", 14, "bold", "#4A4F55", "start"))

    # Row 3: the people
    base = 1300
    o.append(head(60, 1100, "THE PEOPLE  ·  wood, brass and slag"))
    o.append(ground(80, 1740, base))
    o.append(crew_side(180, base) + crew_top(300, base - 55) + name(240, base + 60, "Crew", "wooden pawn, fishbowl helmet · 16 mm · health 2"))
    for i, c in enumerate(HOUSE):
        o.append(influence_side(530 + i * 95, base, c))
    o.append(name(672, base + 60, "House influence", "stained wooden rocket nose cones · 10 mm"))
    o.append(decay_lump(985, base - 36, 4) + decay_lump(1080, base - 30, 9) + name(1035, base + 60, "Decay", "slag lump, never two the same · 12 mm"))
    o.append(breakthrough_coin(1360, base - 92) + name(1360, base + 60, "Breakthrough", "brass starburst coin · 18 mm"))
    o.append(isolate_tag(1620, base - 44, 0) + name(1620, base + 60, "Isolate", "wooden lockout tag · 6 × 8.5 mm"))

    # Row 4: on the board, mid-turn
    y0 = 1490
    o.append(head(60, y0 - 30, "ON THE BOARD  ·  mid-turn, on every section colour (pieces at 55 %)"))
    for i, (sname, col) in enumerate(SECTIONS):
        x0 = 90 + i * 415
        o.append(f'<rect x="{x0}" y="{y0}" width="380" height="330" rx="22" fill="{col}" stroke="#FBEFD6" stroke-width="5"/>')
        o.append(f'<rect x="{x0 + 30}" y="{y0 + 28}" width="320" height="274" rx="18" fill="#000" opacity=".06"/>')
        o.append(f'<g transform="translate({x0},{y0}) scale(.55)">')
        o.append(glitch_top(130, 130) + glitch_top(270, 110))
        o.append(fault_top(520, 160, damage=1) if i in (1, 3) else fault_side(520, 290))
        if i in (0, 2):
            o.append(failure_side(560, 560, damage=i // 2 + 1))
        else:
            o.append(glitch_top(580, 470))
        o.append(crew_side(130, 540))
        o.append(crew_injured(270, 560) if i in (0, 3) else crew_side(260, 560))
        o.append(influence_side(410, 555, HOUSE[i % 2]))
        if i == 1:
            o.append(decay_lump(440, 430, 12))
        if i == 3:
            o.append(fault_side(500, 420) + isolate_tag(555, 380))
        o.append("</g>")
        o.append(label(x0 + 190, y0 + 360, sname, 16, "bold", "#2B2F33"))
    o.append(label(60, y0 + 430, "Print-and-play: every piece is a die-cut token with an undamaged face and a damaged face; the Failure's back face "
                   "is split into its two damaged states (rotate it to show 2 damage).", 15, "normal", "#4A4F55", "start"))
    o.append("</svg>")
    return "\n".join(o)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    svg = OUT / "token_sheet.svg"
    svg.write_text(sheet())
    png = OUT / "token_sheet.png"
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:1800,height:2010}},deviceScaleFactor:1}});"
          f"await p.goto('file://{svg}');await p.screenshot({{path:'{png}'}});await b.close();}})();")
    subprocess.run(["node", "-e", js], check=True)
    print("wrote", svg.relative_to(ROOT), "and", png.relative_to(ROOT))


if __name__ == "__main__":
    main()
