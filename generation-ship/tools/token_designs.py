"""Hand-coded SVG concepts for the physical pieces: the machine in grey plastic, the people in wood.

    python3 tools/token_designs.py   -> art/tokens/token_sheet.svg (+ .png, rendered with Playwright)

Every piece is drawn from its real size in millimetres (SIZES), shown at SCALE px per mm:
- Threat: safety signs (designer, 2026-11-05): Glitch = Notice, a blue disc on a base; Fault =
  Caution, a yellow triangle on a base; Failure = Warning, a thick red octagon on a short pole.
- People (wood): Crew = a pawn with a fishbowl helmet; house influence = flat house crests.
- Decay = a cracked, buckled panel lying on a base (rust-brown plastic); Breakthrough = a brass coin.
Damage states (GDD "Threat pieces": damage clears at Time passes) use no extra parts, only the way a
piece sits: 1 damage knocks a Fault or Failure over; 2 damage turns a Failure upside down (it stands
on the octagon's flat top edge); an injured Crew lies on its side; Glitch (health 1) has no state.
A downgrade replaces the piece with an
undamaged one standing upright (damage does not carry over). Contain (after Spirit Island's Strife) is a wooden collar marker with a no-entry badge, slipped over a threat piece's base; it moves with the piece and comes off at that piece's next Collapse.
The sheet shows each piece from the side and from above in every state, a black-silhouette test, and
the pieces on the four section colours. Concept only: the numbers are starting points for a sculptor.
"""
import json
import math
import random
import subprocess
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import icons  # noqa: E402  (the house crest and the rubble share their shapes with the icons)

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
    "contain": {"d": 13},          # the collar fits round a sign base (10-12 mm)
}
ACCENT, DAMAGE_INK = "#E8763A", "#8A3A16"
HOUSE = ["#3A6FD8", "#8FB04A", "#7A8C96", "#6A4A9A"]        # Galvan, Gardeners, Keel, Voidwardens (wood stain)
HOUSE_IDS = ["galvan", "gardeners", "keel", "voidwardens"]
SECTIONS = [("Infrastructure", "#3AB0A8"), ("Residential", "#F2A060"), ("Government", "#E88AA0"), ("Agricultural", "#A8C860")]
INK = "#1A1D20"                 # outline; the threat plastic is gunmetal (gradients in defs)


def mmv(v):
    return v * SCALE


def defs():
    return """<defs>
  <linearGradient id="plastic" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7A8088"/><stop offset=".55" stop-color="#4E545B"/><stop offset="1" stop-color="#33383E"/></linearGradient>
  <linearGradient id="plasticSide" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3A3F45"/><stop offset=".35" stop-color="#737980"/><stop offset=".7" stop-color="#50565D"/><stop offset="1" stop-color="#30353A"/></linearGradient>
  <radialGradient id="glass" cx=".38" cy=".3" r=".75"><stop offset="0" stop-color="#8E959C"/><stop offset=".5" stop-color="#5A6067"/><stop offset="1" stop-color="#3A3F45"/></radialGradient>
  <linearGradient id="wood" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B98A55"/><stop offset=".4" stop-color="#E2BE8A"/><stop offset="1" stop-color="#A8783F"/></linearGradient>
  <radialGradient id="brass" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#FFE7A0"/><stop offset=".45" stop-color="#D9A848"/><stop offset="1" stop-color="#8F6420"/></radialGradient>
  <linearGradient id="slag" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5A463C"/><stop offset=".6" stop-color="#2E2420"/><stop offset="1" stop-color="#1C1614"/></linearGradient>
  <filter id="shadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="2.5" dy="3" stdDeviation="2.5" flood-color="#000" flood-opacity=".35"/></filter>
</defs>"""


def poly(points):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


# --- the machine (grey plastic) -------------------------------------------------------------------
# --- the threat: safety signs (designer, 2026-11-05) -------------------------------------------
# Level 1 Notice = Glitch: a blue disc standing in a base. Level 2 Caution = Fault: a yellow
# triangle standing in a base. Level 3 Warning = Failure: a thick red octagon on a short pole on a
# base. Colour and shape both escalate (shape alone still reads for colourblind players).
# Damage, no extra parts: 1 damage = knocked over; 2 damage (Failure only) = upside down, standing
# on the octagon's flat top edge.
BLUE, YELLOW, RED, WHITE, BLACK = "#2F6FB8", "#F2C230", "#C8323C", "#FFFFFF", "#1A1D20"
SIGN = {
    "glitch": {"base_w": 10, "base_h": 2, "d": 10, "t": 2.5},
    "fault": {"base_w": 12, "base_h": 2, "side": 14, "t": 2.5},
    "failure": {"base_w": 12, "base_h": 2.2, "pole_w": 2.6, "pole_h": 3.5, "flat": 14, "t": 4},
}


def sign_base(cx, by, w, h, solid=None):
    return (f'<path d="M{cx - mmv(w) / 2},{by} L{cx - mmv(w) / 2},{by - mmv(h) + 4} Q{cx},{by - mmv(h) - 6} {cx + mmv(w) / 2},{by - mmv(h) + 4} '
            f'L{cx + mmv(w) / 2},{by} Z" fill="{solid or "url(#plasticSide)"}" stroke="{solid or INK}" stroke-width="1.6"/>')


def excl(cx, cy, s, colour):
    """An exclamation mark centred at (cx, cy), s mm tall."""
    h = mmv(s)
    return (f'<rect x="{cx - h * .1}" y="{cy - h / 2}" width="{h * .2}" height="{h * .62}" rx="{h * .08}" fill="{colour}"/>'
            f'<circle cx="{cx}" cy="{cy + h * .4}" r="{h * .11}" fill="{colour}"/>')


def octa_pts(cx, cy, r):
    return [(cx + r * math.cos(math.radians(22.5 + 45 * k)), cy + r * math.sin(math.radians(22.5 + 45 * k))) for k in range(8)]


def glitch_face(cx, cy, solid=None):
    r = mmv(SIGN["glitch"]["d"]) / 2
    if solid:
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{solid}"/>'
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BLUE}" stroke="{INK}" stroke-width="1.8"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r * .84}" fill="none" stroke="{WHITE}" stroke-width="2.2"/>{excl(cx, cy, 5.2, WHITE)}')


def fault_face(cx, cy, solid=None):
    """The caution triangle, centred on its centroid (cx, cy)."""
    a = mmv(SIGN["fault"]["side"])
    h = a * math.sqrt(3) / 2
    pts = [(cx, cy - 2 * h / 3), (cx + a / 2, cy + h / 3), (cx - a / 2, cy + h / 3)]
    if solid:
        return f'<polygon points="{poly(pts)}" fill="{solid}" stroke="{solid}" stroke-width="6" stroke-linejoin="round"/>'
    inner = [(cx + .76 * (x - cx), cy + .76 * (y - cy)) for x, y in pts]
    return (f'<polygon points="{poly(pts)}" fill="{YELLOW}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
            f'<polygon points="{poly(inner)}" fill="none" stroke="{BLACK}" stroke-width="3.2" stroke-linejoin="round"/>{excl(cx, cy + h * .04, 5.6, BLACK)}')


def failure_face(cx, cy, solid=None, thick=True):
    r = mmv(SIGN["failure"]["flat"]) / 2 / math.cos(math.radians(22.5))
    pts = octa_pts(cx, cy, r)
    if solid:
        return f'<polygon points="{poly(octa_pts(cx + 6, cy - 6, r))}" fill="{solid}"/><polygon points="{poly(pts)}" fill="{solid}"/>'
    back = f'<polygon points="{poly(octa_pts(cx + 7, cy - 7, r))}" fill="#7A1E24" stroke="{INK}" stroke-width="1.6"/>' if thick else ""
    return (f'{back}<polygon points="{poly(pts)}" fill="{RED}" stroke="{INK}" stroke-width="1.8"/>'
            f'<polygon points="{poly(octa_pts(cx, cy, r * .86))}" fill="none" stroke="{WHITE}" stroke-width="3"/>'
            f'<rect x="{cx - r * .55}" y="{cy - r * .14}" width="{r * 1.1}" height="{r * .28}" rx="3" fill="{WHITE}"/>')


def glitch_upright(cx, by, solid=None):
    g = SIGN["glitch"]
    r = mmv(g["d"]) / 2
    return f'{glitch_face(cx, by - mmv(g["base_h"]) - r + 5, solid)}{sign_base(cx, by, g["base_w"], g["base_h"], solid)}'


def fault_upright(cx, by, solid=None):
    f = SIGN["fault"]
    h = mmv(f["side"]) * math.sqrt(3) / 2
    return f'{fault_face(cx, by - mmv(f["base_h"]) - h / 3 + 5, solid)}{sign_base(cx, by, f["base_w"], f["base_h"], solid)}'


def failure_upright(cx, by, solid=None):
    f = SIGN["failure"]
    r = mmv(f["flat"]) / 2 / math.cos(math.radians(22.5))
    flat = mmv(f["flat"]) / 2
    pole_top = by - mmv(f["base_h"]) - mmv(f["pole_h"])
    pole = (f'<rect x="{cx - mmv(f["pole_w"]) / 2}" y="{pole_top - 4}" width="{mmv(f["pole_w"])}" height="{mmv(f["pole_h"]) + 8}" '
            f'fill="{solid or "url(#plasticSide)"}" stroke="{solid or INK}" stroke-width="1.4"/>')
    return f'{pole}{failure_face(cx, pole_top - flat + 2, solid)}{sign_base(cx, by, f["base_w"], f["base_h"], solid)}'


# (half-width, height) of each upright piece in px: what a knocked-over or upside-down piece needs
def _dims(kind):
    if kind == "fault":
        f = SIGN["fault"]
        return mmv(max(f["side"], f["base_w"])) / 2, mmv(f["base_h"]) + mmv(f["side"]) * math.sqrt(3) / 2 - 5
    f = SIGN["failure"]
    return mmv(f["flat"]) / 2 / math.cos(math.radians(22.5)) + 7, mmv(f["base_h"] + f["pole_h"] + f["flat"]) + 5


def lay(body, kind, cx, by, mode):
    hw, h = _dims(kind)
    if mode == "over":      # knocked over: a quarter turn, resting on the ground line
        return f'<g transform="translate({cx + h / 2} {by - hw}) rotate(-90) translate({-cx} {-by})">{body}</g>'
    return f'<g transform="translate({cx} {by - h}) rotate(180) translate({-cx} {-by})">{body}</g>'


def glitch_side(cx, by, solid=None):
    return f'<g filter="url(#shadow)">{glitch_upright(cx, by, solid)}</g>'


def glitch_top(cx, cy, solid=None):
    g = SIGN["glitch"]
    return (f'<g filter="url(#shadow)"><circle cx="{cx}" cy="{cy}" r="{mmv(g["base_w"]) / 2}" fill="{solid or "url(#plastic)"}" stroke="{solid or INK}" stroke-width="1.5"/>'
            f'<rect x="{cx - mmv(g["d"]) / 2}" y="{cy - mmv(g["t"]) / 2}" width="{mmv(g["d"])}" height="{mmv(g["t"])}" rx="6" fill="{solid or BLUE}" stroke="{solid or INK}" stroke-width="1.5"/></g>')


def fault_side(cx, by, solid=None, damage=0):
    body = fault_upright(cx, by, solid)
    return f'<g filter="url(#shadow)">{lay(body, "fault", cx, by, "over") if damage else body}</g>'


def fault_top(cx, cy, solid=None, damage=0):
    f = SIGN["fault"]
    if damage:      # knocked over, face up: the whole triangle, the base along its foot
        h = mmv(f["side"]) * math.sqrt(3) / 2
        return (f'<g filter="url(#shadow)"><rect x="{cx - mmv(f["base_w"]) / 2}" y="{cy + h / 3 - 4}" width="{mmv(f["base_w"])}" height="{mmv(f["base_h"]) + 6}" rx="5" fill="{solid or "url(#plastic)"}" stroke="{solid or INK}" stroke-width="1.5"/>'
                f'{fault_face(cx, cy, solid)}</g>')
    return (f'<g filter="url(#shadow)"><circle cx="{cx}" cy="{cy}" r="{mmv(f["base_w"]) / 2}" fill="{solid or "url(#plastic)"}" stroke="{solid or INK}" stroke-width="1.5"/>'
            f'<rect x="{cx - mmv(f["side"]) / 2}" y="{cy - mmv(f["t"]) / 2}" width="{mmv(f["side"])}" height="{mmv(f["t"])}" rx="5" fill="{solid or YELLOW}" stroke="{solid or INK}" stroke-width="1.5"/></g>')


def failure_side(cx, by, solid=None, damage=0):
    body = failure_upright(cx, by, solid)
    if damage == 1:
        body = lay(body, "failure", cx, by, "over")
    elif damage == 2:
        body = lay(body, "failure", cx, by, "up")
    return f'<g filter="url(#shadow)">{body}</g>'


def failure_top(cx, cy, solid=None, damage=0):
    f = SIGN["failure"]
    base = f'<circle cx="{cx}" cy="{cy}" r="{mmv(f["base_w"]) / 2}" fill="{solid or "url(#plastic)"}" stroke="{solid or INK}" stroke-width="1.5"/>'
    slab = f'<rect x="{cx - mmv(f["flat"]) / 2}" y="{cy - mmv(f["t"]) / 2}" width="{mmv(f["flat"])}" height="{mmv(f["t"])}" rx="4" fill="{solid or RED}" stroke="{solid or INK}" stroke-width="1.5"/>'
    if damage == 1:      # knocked over, face up (centred on the whole piece, not the octagon)
        cy -= mmv(f["pole_h"] + f["base_h"]) / 2 + 22
        r = mmv(f["flat"]) / 2
        return (f'<g filter="url(#shadow)"><rect x="{cx - mmv(f["pole_w"]) / 2}" y="{cy + r - 4}" width="{mmv(f["pole_w"])}" height="{mmv(f["pole_h"]) + 6}" fill="{solid or "url(#plastic)"}" stroke="{solid or INK}" stroke-width="1.4"/>'
                f'<rect x="{cx - mmv(f["base_w"]) / 2}" y="{cy + r + mmv(f["pole_h"])}" width="{mmv(f["base_w"])}" height="{mmv(f["base_h"]) + 4}" rx="5" fill="{solid or "url(#plastic)"}" stroke="{solid or INK}" stroke-width="1.5"/>'
                f'{failure_face(cx, cy, solid, thick=False)}</g>')
    if damage == 2:      # upside down: the base is on top
        return f'<g filter="url(#shadow)">{slab}{base}<circle cx="{cx}" cy="{cy}" r="{mmv(1.4)}" fill="{INK}"/></g>'
    return f'<g filter="url(#shadow)">{base}{slab}</g>'


def contain_marker(cx, by, angle=0):
    """Contain: a wooden collar with a no-entry badge, slipped over a threat piece's base; drawn on
    the ground line by (place it over a piece's base). Moves with the piece; off at its next Collapse."""
    w = mmv(SIZES["contain"]["d"])
    h = mmv(2.4)
    badge = w * .36
    return (f'<g filter="url(#shadow)" transform="rotate({angle} {cx} {by})">'
            f'<path d="M{cx - w / 2},{by - h * .2} C{cx - w / 2},{by - h * 1.2} {cx + w / 2},{by - h * 1.2} {cx + w / 2},{by - h * .2} '
            f'L{cx + w / 2},{by + h * .3} C{cx + w / 2},{by + h * 1.1} {cx - w / 2},{by + h * 1.1} {cx - w / 2},{by + h * .3} Z" fill="url(#wood)" stroke="#5A3A1C" stroke-width="1.6"/>'
            f'<g transform="translate({cx + w / 2 - badge * .7} {by - badge * .9}) scale({badge / 100})">{icons.isolate()}</g></g>')


def isolate_tag(cx, cy, angle=0):
    """Back-compat name: the Contain marker on its own (by its base line)."""
    return contain_marker(cx, cy, angle)


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


def influence_side(cx, by, colour, solid=None, house=None):
    """House influence: a flat wooden token in the house crest's shape (it lies flat, like Spirit
    Island presence), stained the house colour with the emblem engraved; seen from above."""
    s = SIZES["influence"]
    w = mmv(s["base"]) * 1.15
    house = house or (HOUSE_IDS[HOUSE.index(colour)] if colour in HOUSE else None)
    body = (f'<path d="{icons.CREST_PATH}" fill="{solid}"/>' if solid else
            f'<path d="{icons.CREST_PATH}" fill="{colour}" stroke="#3A2A1A" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="{icons.CREST_PATH}" fill="url(#wood)" opacity=".25"/>'
            f'<path d="{icons.CREST_BAND}" fill="#000" opacity=".18"/>{icons.emblem(house, "#FBEFD6")}')
    return f'<g filter="url(#shadow)" transform="translate({cx - w / 2} {by - w}) scale({w / 100})">{body}</g>'


RUST, RUSTHI = "#7A4030", "#A86A50"


def decay_lump(cx, cy, seed=4, solid=None):
    """Decay, from above: a hull panel cracked in two and buckled, lying flat on a round base, all
    rust-brown cast plastic (designer, 2026-11-05)."""
    s = SIZES["decay"]["size"]
    r = mmv(s) / 2
    w = mmv(s * .78) / 2
    crack = [(cx - 4, cy - w), (cx + 6, cy - w * .45), (cx - 5, cy - w * .05), (cx + 5, cy + w * .4), (cx - 2, cy + w)]
    left = [(cx - w, cy - w)] + crack + [(cx - w, cy + w)]
    right = [(cx + w, cy - w)] + crack + [(cx + w, cy + w)]
    rot = (seed * 37) % 90 - 45
    if solid:
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{solid}"/>'
    rivets = "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{INK}"/>' for x, y in ((cx - w + 7, cy - w + 7), (cx - w + 7, cy + w - 7), (cx + w - 7, cy - w + 7), (cx + w - 7, cy + w - 7)))
    return (f'<g filter="url(#shadow)" transform="rotate({rot} {cx} {cy})"><circle cx="{cx}" cy="{cy}" r="{r}" fill="#5A2E22" stroke="{INK}" stroke-width="1.6"/>'
            f'<polygon points="{poly(left)}" fill="{RUST}" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round" transform="translate(-3 1)"/>'
            f'<polygon points="{poly(right)}" fill="{RUSTHI}" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round" transform="translate(3 -1)"/>'
            f'{rivets}</g>')


def decay_side(cx, by, solid=None):
    """Decay from the side: the two halves tent up a little towards the crack."""
    s = SIZES["decay"]["size"]
    w = mmv(s) / 2
    pw = mmv(s * .78) / 2
    base = f'<rect x="{cx - w}" y="{by - mmv(2)}" width="{2 * w}" height="{mmv(2)}" rx="4" fill="{solid or "#5A2E22"}" stroke="{solid or INK}" stroke-width="1.5"/>'
    lh = f'<polygon points="{cx - pw},{by - mmv(2)} {cx - 4},{by - mmv(4.2)} {cx - 4},{by - mmv(3.2)} {cx - pw},{by - mmv(1.6) + 2}" fill="{solid or RUST}" stroke="{solid or INK}" stroke-width="1.5"/>'
    rh = f'<polygon points="{cx + pw},{by - mmv(2)} {cx + 4},{by - mmv(4.6)} {cx + 4},{by - mmv(3.6)} {cx + pw},{by - mmv(1.6) + 2}" fill="{solid or RUSTHI}" stroke="{solid or INK}" stroke-width="1.5"/>'
    return f'<g filter="url(#shadow)">{base}{lh}{rh}</g>'


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
         label(60, 62, "Stewards of the Long Voyage · piece concepts, v4", 30, "bold", "#0F3A48", "start"),
         label(60, 92, "Threat = safety signs, escalating in shape and colour: Notice → Caution → Warning. The people are wood. "
               "Damage is shown by how a piece sits: knocked over, then upside down.", 16, "normal", "#4A4F55", "start"),
         f'<rect x="1640" y="40" width="{mmv(10)}" height="8" fill="#0F3A48"/>', label(1690, 66, "10 mm, to scale", 13)]

    # Row 1: the machine, healthy, side and top
    base = 330
    o.append(head(60, 160, "THE THREAT  ·  safety signs on gunmetal bases"))
    cols = [(240, "Glitch · Notice", "blue disc on a base · 10 mm · health 1", glitch_side, glitch_top),
            (620, "Fault · Caution", "yellow triangle on a base · 14 mm · health 2", fault_side, fault_top),
            (1000, "Failure · Warning", "thick red octagon, short pole · 20 mm · health 3", failure_side, failure_top)]
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
    o.append(label(1475, base + 60, "Shape alone tells them apart:", 14) +
             label(1475, base + 82, "circle, triangle, octagon: the colour is a bonus.", 14))

    # Row 2: damage states, side view
    base = 700
    o.append(head(60, 470, "DAMAGE STATES  ·  by how the piece sits; all stand up again at Time passes"))
    o.append(ground(80, 1740, base))
    states = [(140, fault_side, 0, "undamaged"), (330, fault_side, 1, "1 damage: knocked over"),
              (540, failure_side, 0, "undamaged"), (760, failure_side, 1, "1 damage: knocked over"),
              (1000, failure_side, 2, "2 damage: upside down")]
    for x, f, dmg, state in states:
        o.append(f(x, base, damage=dmg))
        o.append(label(x, base + 30, state, 14, "bold" if dmg else "normal", DAMAGE_INK if dmg else "#4A4F55"))
    o.append(label(235, base + 58, "Fault (health 2)", 15, "bold", "#2B2F33") + label(770, base + 58, "Failure (health 3)", 15, "bold", "#2B2F33"))
    o.append(crew_side(1200, base) + crew_injured(1320, base))
    o.append(label(1200, base + 30, "standing", 14) + label(1330, base + 30, "injured: on its side", 14, "bold", DAMAGE_INK))
    o.append(label(1265, base + 58, "Crew (health 2)", 15, "bold", "#2B2F33"))
    o.append(fault_side(1560, base) + contain_marker(1560, base + 2))
    o.append(label(1590, base + 30, "Contain", 14, "bold", DAMAGE_INK) + label(1590, base + 58, "collar on the piece (a power, not damage)", 14))

    # Row 2b: the same states from above
    base = 900
    o.append(label(60, 812, "From above, as players see them on the board:", 15, "bold", "#4A4F55", "start"))
    tops = [(140, fault_top, 0, "upright: a yellow edge"), (330, fault_top, 1, "over: the whole triangle"),
            (540, failure_top, 0, "upright: a red edge"), (760, failure_top, 1, "over: the whole octagon"),
            (1000, failure_top, 2, "upside down: base on top")]
    for x, f, dmg, cap in tops:
        o.append(f(x, base, damage=dmg) + label(x, base + 105, cap, 13, fill="#7A7468"))
    o.append(crew_top(1200, base) + crew_injured(1320, base + 45) + label(1265, base + 105, "a ring / a lying pawn", 13, fill="#7A7468"))
    o.append(label(60, 1050, "Rules: 1 damage knocks a Fault or Failure over; a second turns a Failure upside down; one more destroys it. "
                   "Glitch (health 1) has no state. A downgraded piece is replaced standing upright: damage does not carry over.", 14, "bold", "#4A4F55", "start"))

    # Row 3: the people
    base = 1300
    o.append(head(60, 1100, "THE PEOPLE  ·  wood and brass (Decay: rust-brown plastic)"))
    o.append(ground(80, 1740, base))
    o.append(crew_side(180, base) + crew_top(300, base - 55) + name(240, base + 60, "Crew", "wooden pawn, fishbowl helmet · 16 mm · health 2"))
    for i, c in enumerate(HOUSE):
        o.append(influence_side(530 + i * 95, base, c))
    o.append(name(672, base + 60, "House influence", "flat wooden house crests, emblem engraved · 12 mm"))
    o.append(decay_side(985, base) + decay_lump(1085, base - 60, 4) + name(1035, base + 60, "Decay", "cracked panel lying on a base · 12 mm"))
    o.append(breakthrough_coin(1360, base - 92) + name(1360, base + 60, "Breakthrough", "brass starburst coin · 18 mm"))
    o.append(contain_marker(1620, base - 10, 0) + name(1620, base + 60, "Contain", "wooden collar marker · 13 mm"))

    # Row 4: on the board, mid-turn
    y0 = 1490
    o.append(head(60, y0 - 30, "ON THE BOARD  ·  mid-turn, on every section colour (pieces at 55 %)"))
    for i, (sname, col) in enumerate(SECTIONS):
        x0 = 90 + i * 415
        o.append(f'<rect x="{x0}" y="{y0}" width="380" height="330" rx="22" fill="{col}" stroke="#FBEFD6" stroke-width="5"/>')
        o.append(f'<rect x="{x0 + 30}" y="{y0 + 28}" width="320" height="274" rx="18" fill="#000" opacity=".06"/>')
        o.append(f'<g transform="translate({x0},{y0}) scale(.55)">')
        o.append(glitch_side(130, 200) + glitch_side(260, 180))
        o.append(fault_top(520, 160, damage=1) if i in (1, 3) else fault_side(520, 290))
        if i in (0, 2):
            o.append(failure_side(560, 560, damage=i // 2 + 1))
        else:
            o.append(glitch_side(580, 520))
        o.append(crew_side(130, 540))
        o.append(crew_injured(270, 560) if i in (0, 3) else crew_side(260, 560))
        o.append(influence_side(410, 555, HOUSE[i % 2]))
        if i == 1:
            o.append(decay_lump(440, 430, 12))
        if i == 3:
            o.append(fault_side(500, 420) + contain_marker(500, 422))
        o.append("</g>")
        o.append(label(x0 + 190, y0 + 360, sname, 16, "bold", "#2B2F33"))
    o.append(label(60, y0 + 430, "Print-and-play: every piece is a die-cut token with an undamaged face and a damaged face; the Failure's back face "
                   "is split into its two damaged states (rotate it to show 2 damage).", 15, "normal", "#4A4F55", "start"))
    o.append("</svg>")
    return "\n".join(o)


# --- sprites for the table mock-up: one transparent PNG per piece and state, at SCALE px per mm --
def sprite_svgs():
    """name -> SVG body: standing pieces seen from the side (ground at y 260), flat ones from above."""
    g = 260
    s = {"glitch": glitch_side(150, g), "fault": fault_side(150, g), "fault_flat": fault_top(150, 150, damage=1),
         "failure": failure_side(150, g), "failure_side": failure_side(150, g, damage=1), "failure_up": failure_side(150, g, damage=2),
         "crew": crew_side(150, g), "crew_injured": crew_injured(150, g), "decay": decay_lump(150, 150, 4),
         "decay_b": decay_lump(150, 150, 9), "breakthrough": breakthrough_coin(150, 150), "contain": fault_side(150, g) + contain_marker(150, g + 2)}
    for i, c in enumerate(HOUSE):
        s[f"influence_{i}"] = influence_side(150, g, c)
    return s


def export_sprites():
    """Write art/tokens/sprites/<name>.png (transparent, cropped later by the mock-up)."""
    d = OUT / "sprites"
    d.mkdir(parents=True, exist_ok=True)
    jobs = []
    for name, body in sprite_svgs().items():
        f = d / f"{name}.svg"
        f.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300">{defs()}{body}</svg>')
        jobs.append((str(f), str(d / f"{name}.png")))
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
          "const p=await b.newPage({viewport:{width:300,height:300},deviceScaleFactor:1});"
          f"for (const [s,o] of {json.dumps(jobs)}){{await p.goto('file://'+s);await p.screenshot({{path:o,omitBackground:true}});}}"
          "await b.close();})();")
    subprocess.run(["node", "-e", js], check=True)
    for svg, _ in jobs:
        Path(svg).unlink()
    return d


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    print("sprites in", export_sprites().relative_to(ROOT))
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
