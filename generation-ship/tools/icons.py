"""The icon language for the common power actions, as hand-coded SVG (no image model).

    python3 tools/icons.py   -> art/icons/icon_sheet.svg (+ .png) and art/icons/<name>.svg

Modelled on Spirit Island's iconography: every piece has a silhouette that appears inline in text;
common actions are a glyph with a number beside it (like Push, Gather and Defend); range is an arrow
with its number; elements (here: guilds) are a row of symbols. The glyphs share one style: a 100-unit
box, deep-teal ink, tangerine for "the players' action", cream counters. Effects from the data are
mapped to glyphs by ICON_FOR (the verbs in src/print/print.js), so cards can be set as icons.
"""
import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "art" / "icons"
INK, ACT, CREAM, GUN, WOOD, GOLD = "#0F3A48", "#E8603A", "#FBEFD6", "#4E545B", "#D9B07A", "#E8B23A"
RUST = "#7A4030"                                 # Decay: rust-brown cast plastic
SW = 6                                            # stroke width in icon units


def P(points):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


def reg(cx, cy, r, n, rot=0.0):
    return [(cx + r * math.cos(rot + 2 * math.pi * k / n), cy + r * math.sin(rot + 2 * math.pi * k / n)) for k in range(n)]


# The house banner (designer, 2026-11-05: the banners the batch-5 house boards painted read very
# well, so the influence token and its icon take that shape). One shape for the influence token (it
# lies flat, like Spirit Island presence), its icon and the banner on the house board
# (tools/retro_templates.py banner_points). The emblem sits in the banner's upper body.
CREST_PATH = "M22,6 L78,6 L78,94 L50,76 L22,94 Z"
CREST_BAND = "M14,2 L86,2 L86,8 L14,8 Z"          # the hanging rod


def emblem(house, colour=CREAM):
    """Each house's emblem, sized to sit in the banner's body (a 40-unit box centred at 50, 42)."""
    e = {
        "galvan": f'<circle cx="50" cy="42" r="14" fill="none" stroke="{colour}" stroke-width="6" stroke-dasharray="6 4"/><polygon points="54,22 39,46 50,46 45,64 63,37 52,37 57,22" fill="{colour}"/>',
        "keel": f'<g transform="translate(50 43) scale(.72) translate(-50 -52)"><circle cx="50" cy="32" r="6" fill="none" stroke="{colour}" stroke-width="6"/><path d="M50,38 L50,72 M38,46 L62,46 M32,58 C34,70 44,74 50,74 C56,74 66,70 68,58" fill="none" stroke="{colour}" stroke-width="7" stroke-linecap="round"/></g>',
        "gardeners": f'<g transform="translate(0 -6)"><path d="M34,66 L34,44 C34,30 66,30 66,44 L66,66 Z" fill="none" stroke="{colour}" stroke-width="5"/><path d="M50,64 L50,50 M50,54 C42,54 38,48 38,42 C46,42 50,46 50,54 M50,50 C56,50 62,44 62,38 C54,38 50,42 50,50" fill="{colour}" stroke="{colour}" stroke-width="3"/></g>',
        "voidwardens": f'<circle cx="50" cy="42" r="15" fill="none" stroke="{colour}" stroke-width="5"/>' + "".join(
            f'<line x1="{50 + 15 * math.cos(a)}" y1="{42 + 15 * math.sin(a)}" x2="{50 + 21 * math.cos(a)}" y2="{42 + 21 * math.sin(a)}" stroke="{colour}" stroke-width="5"/>' for a in (0, math.pi / 2, math.pi, 3 * math.pi / 2))
            + f'<polygon points="50,33 53,39 59,42 53,45 50,51 47,45 41,42 47,39" fill="{colour}"/>',
    }
    return e.get(house, f'<polygon points="50,26 55,38 68,40 58,48 61,60 50,53 39,60 42,48 32,40 45,38" fill="{colour}"/>')


def crest(house=None, colour="#B98A55"):
    return (f'<path d="{CREST_PATH}" fill="{colour}" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
            f'<path d="M30,8 L30,80 M70,8 L70,80" stroke="{GOLD}" stroke-width="2.5" opacity=".8"/>'
            f'<path d="{CREST_BAND}" fill="{GOLD}" stroke="{INK}" stroke-width="3"/>{emblem(house)}')


# --- pieces (the same silhouettes as the physical pieces) ----------------------------------------
def glitch():
    return f'<polygon points="{P(reg(50, 50, 38, 6))}" fill="{GUN}" stroke="{INK}" stroke-width="{SW}"/><circle cx="50" cy="50" r="14" fill="{CREAM}" stroke="{INK}" stroke-width="4"/>'


def fault():
    pts = []
    for k in range(10):
        a0 = 2 * math.pi * k / 10 - math.pi / 2
        for f, r in ((0, 30), (.12, 42), (.42, 42), (.54, 30)):
            a = a0 + f * 2 * math.pi / 10
            pts.append((50 + r * math.cos(a), 50 + r * math.sin(a)))
    return f'<polygon points="{P(pts)}" fill="{GUN}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/><circle cx="50" cy="50" r="11" fill="{CREAM}" stroke="{INK}" stroke-width="4"/>'


def failure():
    """Placeholder until the threat ladder is chosen (art/tokens/threat_concepts.svg)."""
    return (f'<rect x="26" y="74" width="48" height="18" rx="4" fill="{GUN}" stroke="{INK}" stroke-width="{SW}"/>'
            f'<path d="M38,74 L38,66 C38,62 30,61 30,56 L30,22 C30,13 38,10 42,10 L58,10 C62,10 70,13 70,22 L70,56 C70,61 62,62 62,66 L62,74 Z" fill="{GUN}" stroke="{INK}" stroke-width="{SW}"/>')



def crew():
    return (f'<path d="M24,92 Q24,82 32,80 L42,52 L58,52 L68,80 Q76,82 76,92 Z" fill="{WOOD}" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
            f'<circle cx="50" cy="32" r="22" fill="{CREAM}" stroke="{INK}" stroke-width="{SW}"/><circle cx="50" cy="33" r="13" fill="{WOOD}" stroke="{INK}" stroke-width="4"/>')


def decay():
    """Decay, permanent damage: a hull plate broken in two along a jagged crack, one half buckled,
    cast in rust-brown plastic (Patch, by contrast, is a whole plate with a tangerine plaster)."""
    left = "12,20 52,14 44,34 56,48 40,62 50,86 14,82"
    right = "58,14 90,22 86,80 56,88 46,64 62,48 50,34"
    return (f'<polygon points="{left}" fill="{RUST}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
            f'<polygon points="{right}" fill="{RUST}" stroke="{INK}" stroke-width="5" stroke-linejoin="round" transform="rotate(8 70 50) translate(4 2)"/>'
            f'<path d="M62,20 L84,26 L82,40" fill="none" stroke="#B0705A" stroke-width="3" transform="rotate(8 70 50) translate(4 2)"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{INK}"/>' for x, y in ((20, 28), (20, 74)))
            + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{INK}"/>' for x, y in ((84, 32), (80, 76))))



def influence(colour="#B98A55", house=None):
    """House influence: the house crest, lying flat; in the house colour with its emblem."""
    return crest(house, colour)



def haven():
    return (f'<path d="M50,8 L88,24 L88,52 C88,74 70,88 50,94 C30,88 12,74 12,52 L12,24 Z" fill="{CREAM}" stroke="{INK}" stroke-width="{SW}"/>'
            f'<path d="M30,56 L50,38 L70,56 L70,76 L30,76 Z" fill="{WOOD}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')


def purpose():
    star = []
    for k in range(16):
        a = math.pi * k / 8 - math.pi / 2
        r = 46 if k % 4 == 0 else (34 if k % 2 == 0 else 20)
        star.append((50 + r * math.cos(a), 50 + r * math.sin(a)))
    return f'<polygon points="{P(star)}" fill="{GOLD}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/><circle cx="50" cy="50" r="10" fill="{CREAM}" stroke="{INK}" stroke-width="4"/>'



def credits():
    return (f'<circle cx="50" cy="50" r="40" fill="{GOLD}" stroke="{INK}" stroke-width="{SW}"/><circle cx="50" cy="50" r="30" fill="none" stroke="{INK}" stroke-width="3"/>'
            f'<text x="50" y="66" font-family="Righteous" font-size="46" fill="{INK}" text-anchor="middle">¢</text>')


def card():
    return f'<rect x="24" y="12" width="52" height="76" rx="7" fill="{INK}" stroke="{INK}" stroke-width="4"/><rect x="31" y="19" width="38" height="62" rx="4" fill="none" stroke="{GOLD}" stroke-width="3"/>'


# --- tokens -------------------------------------------------------------------------------------
def brace():
    return f'<path d="M50,8 L86,22 L86,50 C86,74 68,88 50,94 C32,88 14,74 14,50 L14,22 Z" fill="{CREAM}" stroke="{INK}" stroke-width="{SW}"/><path d="M50,22 L72,31 L72,50 C72,66 62,75 50,80 Z" fill="{INK}"/>'


def patch():
    return (f'<rect x="14" y="30" width="72" height="40" rx="10" fill="{CREAM}" stroke="{INK}" stroke-width="{SW}" transform="rotate(-30 50 50)"/>'
            f'<rect x="36" y="38" width="28" height="24" rx="3" fill="{ACT}" transform="rotate(-30 50 50)"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="{INK}" transform="rotate(-30 50 50)"/>' for x, y in ((22, 42), (22, 58), (78, 42), (78, 58))))


def lockout():
    return (f'<path d="M32,46 L32,32 C32,16 68,16 68,32 L68,46" fill="none" stroke="{INK}" stroke-width="9"/>'
            f'<rect x="20" y="44" width="60" height="46" rx="8" fill="{ACT}" stroke="{INK}" stroke-width="{SW}"/><circle cx="50" cy="63" r="6" fill="{INK}"/><rect x="47" y="64" width="6" height="14" fill="{INK}"/>')


def quarantine():
    hexa = reg(50, 50, 42, 6, math.pi / 6)
    stripes = "".join(f'<line x1="{x}" y1="10" x2="{x - 30}" y2="90" stroke="{ACT}" stroke-width="7"/>' for x in range(20, 140, 18))
    return (f'<clipPath id="q"><polygon points="{P(hexa)}"/></clipPath><g clip-path="url(#q)"><rect width="100" height="100" fill="{CREAM}"/>{stripes}</g>'
            f'<polygon points="{P(hexa)}" fill="none" stroke="{INK}" stroke-width="{SW}"/><polygon points="{P(reg(50, 50, 22, 6, math.pi / 6))}" fill="{CREAM}" stroke="{INK}" stroke-width="5"/>')


def unrest():
    """A raised fist: rebellion (short, curled fingers so it reads as a fist, not a hand)."""
    return (f'<path d="M36,94 L36,70 L66,70 L66,94" fill="{ACT}" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
            f'<path d="M26,72 L26,40 C26,34 30,30 36,30 L70,30 C76,30 80,34 80,40 L80,58 C80,66 74,72 66,72 Z" fill="{ACT}" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
            f'<path d="M43,30 L43,46 M53,30 L53,46 M63,30 L63,46" stroke="{INK}" stroke-width="4"/>'
            f'<path d="M26,46 L56,46 C62,46 64,52 60,56 L44,56" fill="none" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>')



def isolate():
    """Isolate (this threat piece deals no damage at its next collapse): the universal prohibition
    sign over a threat piece."""
    return (f'<g transform="translate(18 18) scale(.64)">{fault()}</g>'
            f'<circle cx="50" cy="50" r="40" fill="none" stroke="{ACT}" stroke-width="11"/>'
            f'<line x1="22" y1="22" x2="78" y2="78" stroke="{ACT}" stroke-width="11"/>'
            f'<circle cx="50" cy="50" r="46" fill="none" stroke="{INK}" stroke-width="3"/>')



# --- actions ----------------------------------------------------------------------------------------
def repair():
    """Damage to threat is repair: a wrench (the players' action colour)."""
    return (f'<path d="M24,84 L58,50" stroke="{INK}" stroke-width="18" stroke-linecap="round"/><path d="M24,84 L58,50" stroke="{ACT}" stroke-width="8" stroke-linecap="round"/>'
            f'<path d="M58,50 C50,36 58,14 78,14 L70,28 L76,36 L88,30 C90,50 72,60 58,50 Z" fill="{ACT}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')


def arrow(x1, y1, x2, y2, colour=ACT, w=10):
    a = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 16 * math.cos(a), y2 - 16 * math.sin(a)
    left = (hx + 14 * math.cos(a + math.pi / 2), hy + 14 * math.sin(a + math.pi / 2))
    right = (hx + 14 * math.cos(a - math.pi / 2), hy + 14 * math.sin(a - math.pi / 2))
    return (f'<line x1="{x1}" y1="{y1}" x2="{hx}" y2="{hy}" stroke="{INK}" stroke-width="{w + 6}" stroke-linecap="round"/>'
            f'<line x1="{x1}" y1="{y1}" x2="{hx}" y2="{hy}" stroke="{colour}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<polygon points="{P([(x2, y2), left, right])}" fill="{colour}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')


def section_box():
    return f'<rect x="18" y="18" width="64" height="64" rx="12" fill="{CREAM}" stroke="{INK}" stroke-width="4" stroke-dasharray="8 6" opacity=".9"/>'


def vent():
    """Push out of the section: one arrow from the centre out to the right (Spirit Island's Push)."""
    return f'{section_box()}<circle cx="50" cy="50" r="9" fill="{INK}"/>' + arrow(56, 50, 98, 50)



def gather():
    """Gather into the section: one arrow from the left into the centre."""
    return f'{section_box()}<circle cx="50" cy="50" r="9" fill="{INK}"/>' + arrow(2, 50, 42, 50)



def move():
    return arrow(12, 70, 88, 30)


def add():
    return f'<circle cx="50" cy="50" r="40" fill="{CREAM}" stroke="{INK}" stroke-width="{SW}"/><path d="M50,28 L50,72 M28,50 L72,50" stroke="{ACT}" stroke-width="12" stroke-linecap="round"/>'


def remove():
    """Remove: a minus (Add is the plus)."""
    return f'<circle cx="50" cy="50" r="40" fill="{CREAM}" stroke="{INK}" stroke-width="{SW}"/><path d="M28,50 L72,50" stroke="{ACT}" stroke-width="12" stroke-linecap="round"/>'



def downgrade():
    """Downgrade (Failure to Fault, Fault to Glitch): one step down."""
    return (f'<circle cx="50" cy="50" r="42" fill="{CREAM}" stroke="{INK}" stroke-width="{SW}"/>'
            f'<path d="M28,30 L50,50 L72,30 M28,52 L50,72 L72,52" fill="none" stroke="{ACT}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>')



def restore_decay():
    """Restore Decay: a Decay leaves the board and returns to its card (the pool)."""
    return (f'<g transform="translate(-4 30) scale(.68)">{decay()}</g>'
            f'<path d="M34,52 C34,22 60,10 84,22" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>'
            f'<path d="M34,52 C34,22 60,10 84,22" fill="none" stroke="{ACT}" stroke-width="7" stroke-linecap="round"/>'
            f'<polygon points="94,28 74,32 84,12" fill="{ACT}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')



def crew_strike():
    burst = []
    for k in range(16):
        a = math.pi * k / 8
        r = 22 if k % 2 else 12
        burst.append((74 + r * math.cos(a), 30 + r * math.sin(a)))
    return f'<g transform="translate(-6 8) scale(.85)">{crew()}</g><polygon points="{P(burst)}" fill="{ACT}" stroke="{INK}" stroke-width="4"/>'


def foresee():
    return (f'<path d="M6,50 Q50,8 94,50 Q50,92 6,50 Z" fill="{CREAM}" stroke="{INK}" stroke-width="{SW}"/>'
            f'<circle cx="50" cy="50" r="18" fill="{INK}"/><circle cx="56" cy="44" r="6" fill="{CREAM}"/>')


def temper_legacy():
    """Temper the Elder's Legacy: its costliest drawback is struck out, for good."""
    return (f'<rect x="8" y="22" width="84" height="56" rx="12" fill="{INK}"/>'
            f'<rect x="18" y="34" width="52" height="7" rx="3" fill="{CREAM}"/><rect x="18" y="47" width="64" height="7" rx="3" fill="{CREAM}"/>'
            f'<rect x="18" y="60" width="40" height="7" rx="3" fill="{CREAM}"/>'
            f'<path d="M12,52 L88,48" stroke="{ACT}" stroke-width="8" stroke-linecap="round"/>')



def draw():
    return f'<g transform="translate(-8 0)">{card()}</g><circle cx="74" cy="70" r="18" fill="{ACT}" stroke="{INK}" stroke-width="4"/><path d="M74,60 L74,80 M64,70 L84,70" stroke="{CREAM}" stroke-width="6" stroke-linecap="round"/>'


def fast():
    return (f'<path d="M50,6 C66,20 70,40 66,64 L34,64 C30,40 34,20 50,6 Z" fill="{CREAM}" stroke="{INK}" stroke-width="{SW}" transform="rotate(40 50 50)"/>'
            f'<circle cx="50" cy="36" r="8" fill="{INK}" transform="rotate(40 50 50)"/>'
            f'<path d="M36,64 L28,80 L42,72 Z M64,64 L72,80 L58,72 Z" fill="{ACT}" stroke="{INK}" stroke-width="4" transform="rotate(40 50 50)"/>'
            f'<path d="M14,86 L30,70 M8,72 L22,60 M26,94 L38,80" stroke="{ACT}" stroke-width="7" stroke-linecap="round"/>')


def slow():
    return (f'<path d="M24,10 L76,10 M24,90 L76,90" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M30,12 C30,40 50,40 50,50 C50,60 30,60 30,88 L70,88 C70,60 50,60 50,50 C50,40 70,40 70,12 Z" fill="{CREAM}" stroke="{INK}" stroke-width="{SW}"/>'
            f'<path d="M38,80 L62,80 L50,66 Z" fill="{GOLD}"/>')


def range_():
    return (f'<circle cx="18" cy="50" r="12" fill="{INK}"/>' + arrow(30, 50, 92, 50, colour=CREAM, w=10))


def hull():
    """The Outer Hull: the hull's edge, its portholes, and the void beyond."""
    return (f'<path d="M6,62 A44,44 0 0 1 94,62 Z" fill="{INK}"/>'
            f'<polygon points="30,30 32,36 38,36 33,40 35,46 30,42 25,46 27,40 22,36 28,36" fill="{GOLD}"/><circle cx="66" cy="34" r="3" fill="{GOLD}"/>'
            f'<path d="M4,62 L96,62 L96,88 L4,88 Z" fill="{GUN}" stroke="{INK}" stroke-width="5"/>'
            + "".join(f'<circle cx="{x}" cy="75" r="6" fill="{CREAM}" stroke="{INK}" stroke-width="3"/>' for x in (22, 50, 78)))



# --- guilds (the game's elements) -------------------------------------------------------------
def guild_ring(inner, colour):
    return f'<circle cx="50" cy="50" r="44" fill="{colour}" stroke="{INK}" stroke-width="{SW}"/>{inner}'


GUILD = {
    "Engineers": lambda: guild_ring(f'<path d="M30,72 L56,46" stroke="{INK}" stroke-width="12" stroke-linecap="round"/><path d="M56,46 C50,34 56,20 70,20 L64,30 L68,36 L78,32 C80,46 66,54 56,46 Z" fill="{INK}"/>', "#9DB8C4"),
    "Navigators": lambda: guild_ring(f'<polygon points="50,14 58,44 86,50 58,56 50,86 42,56 14,50 42,44" fill="{INK}"/><circle cx="50" cy="50" r="6" fill="{CREAM}"/>', "#8FD3CC"),
    "Bureaucrats": lambda: guild_ring(f'<rect x="38" y="20" width="24" height="26" rx="10" fill="{INK}"/><rect x="26" y="46" width="48" height="12" rx="4" fill="{INK}"/><rect x="22" y="64" width="56" height="10" rx="3" fill="{INK}"/>', "#E8B8C4"),
    "Farmers": lambda: guild_ring(f'<path d="M50,82 L50,46" stroke="{INK}" stroke-width="8"/><path d="M50,52 C30,52 22,38 24,24 C40,24 50,34 50,52 Z M50,46 C64,46 76,34 76,22 C60,20 50,30 50,46 Z" fill="{INK}"/>', "#C8DC9A"),
    "Medics": lambda: guild_ring(f'<path d="M40,18 L60,18 L60,40 L82,40 L82,60 L60,60 L60,82 L40,82 L40,60 L18,60 L18,40 L40,40 Z" fill="{INK}"/>', "#F2C8B8"),
    "Laborers": lambda: guild_ring(f'<rect x="46" y="38" width="10" height="46" rx="3" fill="{INK}"/><rect x="26" y="20" width="50" height="22" rx="6" fill="{INK}"/>', "#F2C890"),
    "Keepers": lambda: guild_ring(f'<circle cx="36" cy="40" r="14" fill="none" stroke="{INK}" stroke-width="9"/><path d="M46,50 L78,82 M66,70 L74,62 M72,76 L80,68" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>', "#F6DC9A"),
    "Scholars": lambda: guild_ring(f'<path d="M14,30 C30,24 44,26 50,34 C56,26 70,24 86,30 L86,74 C70,68 56,70 50,78 C44,70 30,68 14,74 Z" fill="{INK}"/><path d="M50,34 L50,78" stroke="{CREAM}" stroke-width="4"/>', "#C8C0E8"),
}

GROUPS = [
    ("PIECES", [("Glitch", glitch), ("Fault", fault), ("Failure", failure), ("Crew", crew), ("Decay", decay),
                ("Influence", influence), ("Haven", haven), ("Purpose", purpose), ("Credits", credits), ("Card", card)]),
    ("TOKENS", [("Brace", brace), ("Patch", patch), ("Lockout", lockout), ("Quarantine", quarantine),
                ("Unrest", unrest), ("Isolate", isolate)]),
    ("ACTIONS", [("Repair (damage)", repair), ("Vent (push)", vent), ("Gather", gather), ("Move", move), ("Add", add),
                 ("Remove", remove), ("Downgrade", downgrade), ("Restore Decay", restore_decay), ("Crew strike", crew_strike),
                 ("Foresee", foresee), ("Temper Legacy", temper_legacy), ("Draw", draw), ("Fast", fast), ("Slow", slow),
                 ("Range", range_), ("Outer Hull", hull)]),
    ("GUILDS  ·  the elements", [(g, f) for g, f in GUILD.items()]),
    ("HOUSE CRESTS  ·  influence pieces lie flat in this shape; the house board banner is the same crest",
     [(h.title(), (lambda h=h, c=c: crest(h, c))) for h, c in (("galvan", "#3A6FD8"), ("keel", "#7A8C96"), ("gardeners", "#8FB04A"), ("voidwardens", "#6A4A9A"))]),
]

# Effect verbs -> (icons, how to show n). An icon list reads left to right after the number.
ICON_FOR = {
    "damage": [repair], "brace": [brace], "gather_crew": [gather, crew], "add_crew": [add, crew], "move_crew": [move, crew],
    "lockout": [lockout], "patch": [patch], "quarantine": [quarantine], "purpose": [purpose], "credits": [credits],
    "vent_glitch": [vent, glitch], "vent_fault": [vent, fault], "vent_failure": [vent, failure],
    "vent_glitch_or_fault": [vent, glitch, fault], "remove_glitch": [remove, glitch], "remove_fault": [remove, fault],
    "isolate_fault": [isolate, fault], "isolate_failure": [isolate, failure], "downgrade": [downgrade],
    "downgrade_failure": [downgrade], "restore_decay": [restore_decay], "crew_strike": [crew_strike], "foresee": [foresee],
    "temper_legacy": [temper_legacy], "extra_draw": [draw], "move_influence": [move, influence], "add_influence": [add, influence],
    "damage_per_crew": [repair, crew],
}


def place(fn, x, y, size):
    return f'<g transform="translate({x} {y}) scale({size / 100})">{fn()}</g>'


def effect_row(effects, x, y, size=46):
    """An effect dict rendered as icons: n, then the glyphs; effects separated by a thin rule."""
    out, cx = [], x
    for k, n in effects.items():
        icons = ICON_FOR.get(k)
        if not icons:
            continue
        if n != 1 or k in ("damage", "brace", "purpose", "credits"):
            out.append(f'<text x="{cx}" y="{y + size * .78}" font-family="Righteous" font-size="{size * .9}" fill="{INK}">{n}</text>')
            cx += size * .55
        for j, fn in enumerate(icons):
            if k.endswith("_per_crew") and j == 1:               # "per": Spirit Island's slash
                out.append(f'<text x="{cx}" y="{y + size * .8}" font-family="Righteous" font-size="{size * .9}" fill="{INK}">/</text>')
                cx += size * .4
            out.append(place(fn, cx, y, size))
            cx += size * 1.02
        out.append(f'<line x1="{cx + 4}" y1="{y + 6}" x2="{cx + 4}" y2="{y + size - 6}" stroke="#B9AE98" stroke-width="2"/>')
        cx += 14
    return "".join(out), cx


def sheet():
    font = (ROOT / "art" / "fonts")
    W = 1800
    o, y = [], 40
    o.append(f'<text x="60" y="{y + 30}" font-family="Righteous" font-size="34" fill="{INK}">Stewards of the Long Voyage · icon language</text>')
    o.append(f'<text x="60" y="{y + 62}" font-family="Josefin" font-size="18" fill="#4A4F55">Pieces appear inline as silhouettes; actions are a glyph and a number; tangerine marks what the players do. After Spirit Island.</text>')
    y += 100
    for title, items in GROUPS:
        o.append(f'<text x="60" y="{y + 20}" font-family="Righteous" font-size="22" fill="{INK}">{title}</text>')
        y += 36
        for i, (name, fn) in enumerate(items):
            col, row = i % 10, i // 10
            x, yy = 60 + col * 170, y + row * 170
            o.append(f'<rect x="{x}" y="{yy}" width="150" height="150" rx="14" fill="#F7F1E4" stroke="#D8CDB6"/>')
            o.append(place(fn, x + 30, yy + 14, 90))
            o.append(f'<text x="{x + 75}" y="{yy + 136}" font-family="Josefin" font-size="16" font-weight="700" fill="{INK}" text-anchor="middle">{name}</text>')
        y += ((len(items) - 1) // 10 + 1) * 170 + 20
    # before / after, from real data
    people = json.loads((ROOT / "data" / "people.json").read_text())
    picks = [p for p in people if len(p["effects"]) >= 2 and all(k in ICON_FOR for k in p["effects"])][:5]
    o.append(f'<text x="60" y="{y + 20}" font-family="Righteous" font-size="22" fill="{INK}">ON A CARD  ·  the same effects, text and icons (from data/people.json)</text>')
    y += 44
    for p in picks:
        o.append(f'<text x="60" y="{y + 30}" font-family="Josefin" font-size="20" fill="{INK}">{p["id"]}: {p["text"]}</text>')
        row, _ = effect_row(p["effects"], 980, y, 46)
        o.append(f'<rect x="960" y="{y - 6}" width="780" height="58" rx="12" fill="{CREAM}" stroke="#D8CDB6"/>{row}')
        y += 70
    y += 30
    defs = (f"<defs><style>@font-face {{ font-family: Righteous; src: url('{(font / 'Righteous-Regular.ttf').as_uri()}'); }}"
            f"@font-face {{ font-family: Josefin; src: url('{(font / 'JosefinSans[wght].ttf').as_uri()}'); }}</style></defs>")
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{y}" viewBox="0 0 {W} {y}">{defs}<rect width="{W}" height="{y}" fill="#EDE6D8"/>{"".join(o)}</svg>', (W, y)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for _, items in GROUPS:
        for name, fn in items:
            slug = name.split(" (")[0].lower().replace(" ", "_")
            (OUT / f"{slug}.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">{fn()}</svg>')
    svg, (w, h) = sheet()
    f = OUT / "icon_sheet.svg"
    f.write_text(svg)
    png = OUT / "icon_sheet.png"
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{w},height:{int(h)}}},deviceScaleFactor:1}});"
          f"await p.goto('{f.as_uri()}');await p.waitForTimeout(400);await p.screenshot({{path:'{png}'}});await b.close();}})();")
    subprocess.run(["node", "-e", js], check=True)
    print("wrote", f.relative_to(ROOT), "and", png.relative_to(ROOT))


if __name__ == "__main__":
    main()
