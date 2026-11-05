"""Physical-token studies (designer, 2026-11-05: settle the pieces first, then the icons follow).

    python3 tools/token_studies.py   -> art/tokens/token_studies.svg (+ .png)

1. Decay as a token: each option on a base, side view and top view.
2. The threat ladder as warning signs: several versions, each Glitch -> Fault -> Failure with the
   Failure's damage postures (on its side, upside down). A posture only reads if the piece is not
   symmetric, so every version builds in a "this way up" (a post, a foot, a lamp, a symbol).
All gunmetal (threat) or rust-brown (Decay) cast plastic, drawn to scale at 8 px per mm.
"""
import math
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from threat_concepts import GUN, INK, g, solid  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "art" / "tokens"
RUST, RUSTHI = "#7A4030", "#A0604A"


def rust(d, extra=""):
    return f'<path d="{d}" fill="{RUST}" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round" fill-rule="evenodd"/>{extra}'


def base(w=88, h=12):
    """A round base seen from the side (every Decay sits on one, so it reads as a token)."""
    return f'<path d="M{-w / 2},0 L{-w / 2},{-h} Q0,{-h - 8} {w / 2},{-h} L{w / 2},0 Z" fill="{RUST}" stroke="{INK}" stroke-width="2.5"/>'


def base_top(r=44, extra=""):
    return f'<circle cx="0" cy="0" r="{r}" fill="{RUST}" stroke="{INK}" stroke-width="2.5"/>{extra}'


# --- Decay on a base: (name, side view, top view, note) -------------------------------------------
DECAY = [
    ("Cracked panel, upright", base() + rust("M-30,-14 L-30,-92 L-4,-100 L-12,-80 L2,-66 L-8,-50 L4,-30 L-4,-14 Z M4,-14 L10,-30 L0,-50 L10,-66 L-2,-80 L6,-100 L30,-94 L30,-14 Z",
                                                  f'<circle cx="-22" cy="-84" r="3" fill="{INK}"/><circle cx="22" cy="-84" r="3" fill="{INK}"/>'),
     base_top(extra=rust("M-30,-6 L-2,-6 L4,0 L-2,6 L-30,6 Z M4,-6 L30,-6 L30,6 L4,6 L10,0 Z")),
     "a hull panel split down the middle, standing on its base: tall, reads at once"),
    ("Cracked panel, buckled", base() + rust("M-34,-14 L-28,-70 L-6,-76 L-12,-56 L0,-44 L-10,-14 Z M2,-14 L12,-44 L4,-58 L14,-80 L40,-60 L30,-14 Z"),
     base_top(extra=rust("M-34,-8 L-6,-10 L-2,0 L-8,8 L-30,8 Z M2,-10 L36,-4 L30,10 L4,8 L8,0 Z")),
     "the two halves fold apart like a broken hatch: lower, sturdier"),
    ("Twisted girder", base() + rust("M-40,-20 L-10,-56 L4,-38 L36,-84 L44,-76 L8,-24 L-6,-42 L-32,-12 Z",
                                       f'<line x1="-22" y1="-40" x2="-14" y2="-32" stroke="{INK}" stroke-width="2"/><line x1="22" y1="-64" x2="28" y2="-56" stroke="{INK}" stroke-width="2"/>'),
     base_top(extra=rust("M-34,8 L-10,-12 L4,2 L34,-22 L40,-14 L8,12 L-6,-2 L-28,16 Z")),
     "an I-beam bent double: unmistakably structural, a little thin"),
    ("Scorch crater", rust("M-48,0 L-48,-10 C-48,-28 -30,-38 -20,-30 C-14,-46 14,-46 20,-30 C30,-38 48,-28 48,-10 L48,0 Z",
                           f'<path d="M-24,-16 C-16,-26 16,-26 24,-16" fill="none" stroke="#2A1810" stroke-width="7"/>'),
     base_top(extra=f'<circle r="26" fill="#3A2016" stroke="{INK}" stroke-width="2"/><circle r="12" fill="#1E120C"/>'),
     "a burnt hole: reads from above, but low and plain from the side"),
]

# --- warning-sign versions: (name, [glitch, fault, failure] side views, note) ---------------------
EXCL = lambda cx, cy, s: f'<rect x="{cx - 3 * s}" y="{cy - 14 * s}" width="{6 * s}" height="{18 * s}" rx="{2 * s}" fill="{INK}"/><circle cx="{cx}" cy="{cy + 9 * s}" r="{3.6 * s}" fill="{INK}"/>'  # noqa: E731


def tri(cx, cy, r):
    return f"M{cx},{cy - r} L{cx + r * 0.87},{cy + r * 0.5} L{cx - r * 0.87},{cy + r * 0.5} Z"


def dia(cx, cy, r):
    return f"M{cx},{cy - r} L{cx + r},{cy} L{cx},{cy + r} L{cx - r},{cy} Z"


def octa(cx, cy, r):
    pts = [(cx + r * math.cos(math.radians(22.5 + 45 * k)), cy + r * math.sin(math.radians(22.5 + 45 * k))) for k in range(8)]
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"


def post(h, foot=30):
    return solid(f"M{-foot},0 L{-foot},-10 L-5,-10 L-5,-{h} L5,-{h} L5,-10 L{foot},-10 L{foot},0 Z")


def bollard(h, w):
    """A short traffic bollard: a cone body on a square foot."""
    return solid(f"M{-w},0 L{-w},-10 L{-w * 0.55},-10 L{-w * 0.3},-{h} L{w * 0.3},-{h} L{w * 0.55},-10 L{w},-10 L{w},0 Z",
                 f'<path d="M{-w * 0.48},-{h * 0.35} L{w * 0.48},-{h * 0.35} M{-w * 0.4},-{h * 0.62} L{w * 0.4},-{h * 0.62}" stroke="{INK}" stroke-width="2"/>')


SIGNS = [
    ("A · Signs on posts", [
        post(34) + solid(tri(0, -62, 36), EXCL(0, -60, 0.8)),
        post(44) + solid(dia(0, -90, 48), EXCL(0, -88, 1.1)),
        post(62) + solid(octa(0, -122, 62), f'<rect x="-36" y="-130" width="72" height="16" rx="3" fill="{INK}"/>')],
     "the round-1 study: a post and foot give a clear 'this way up'", [(31, 98), (48, 138), (62, 184)]),
    ("B · Sign plates on a foot", [
        solid(tri(0, -34, 40), EXCL(0, -32, 0.85)) + solid("M-36,0 L-36,-6 L36,-6 L36,0 Z"),
        solid(dia(0, -54, 54), EXCL(0, -54, 1.1)) + solid("M-30,0 L-30,-6 L30,-6 L30,0 Z"),
        solid(octa(0, -74, 74), f'<rect x="-42" y="-82" width="84" height="18" rx="3" fill="{INK}"/>') + solid("M-50,0 L-50,-8 L50,-8 L50,0 Z")],
     "no post: chunkier, sturdier, the shape is the whole piece; the foot shows which way is up", [(36, 74), (54, 108), (74, 148)]),
    ("C · Bollards with a sign face", [
        bollard(48, 30) + solid(tri(0, -34, 20), EXCL(0, -33, 0.45)),
        bollard(78, 38) + solid(dia(0, -50, 28), EXCL(0, -50, 0.65)),
        bollard(118, 48) + solid(octa(0, -74, 36), f'<rect x="-20" y="-79" width="40" height="10" rx="2" fill="{INK}"/>')],
     "a hazard bollard you place in the room: escalates by height and by sign; knocked over reads well", [(30, 54), (38, 78), (48, 118)]),
    ("D · Lamp signs", [
        solid("M-24,0 L-24,-10 L-6,-10 L-6,-30 L6,-30 L6,-10 L24,-10 L24,0 Z") + solid(tri(0, -56, 32), f'<circle cx="0" cy="-50" r="8" fill="#2A2F34" stroke="{INK}" stroke-width="2"/>'),
        solid("M-28,0 L-28,-10 L-6,-10 L-6,-40 L6,-40 L6,-10 L28,-10 L28,0 Z") + solid(dia(0, -82, 44), f'<circle cx="0" cy="-82" r="11" fill="#2A2F34" stroke="{INK}" stroke-width="2"/>'),
        solid("M-34,0 L-34,-10 L-8,-10 L-8,-54 L8,-54 L8,-10 L34,-10 L34,0 Z") + solid(octa(0, -112, 58), f'<circle cx="0" cy="-112" r="16" fill="#2A2F34" stroke="{INK}" stroke-width="2"/>')
        + f'<path d="M-62,-150 L-80,-166 M62,-150 L80,-166 M0,-172 L0,-192" stroke="{GUN}" stroke-width="7" stroke-linecap="round"/>'],
     "the signal-lamp idea merged in: a warning shape with a lamp lens, the Failure's lamp blazing", [(28, 88), (44, 126), (80, 192)]),
    ("E · One shape, rising (all triangles)", [
        post(30) + solid(tri(0, -56, 30), EXCL(0, -54, 0.7)),
        post(40) + solid(tri(0, -80, 44), EXCL(0, -84, 0.85) + EXCL(-14, -66, 0.0)),
        post(52) + solid(tri(0, -112, 64), "".join(EXCL(x, -108, 0.8) for x in (-16, 16)))],
     "one sign that grows and gains marks (! / !! ): simplest to learn, weakest silhouettes", [(30, 86), (40, 124), (56, 176)]),
]


def lay(piece, dim, ax, b, mode, s=1.0):
    """A piece on its side (rotated a quarter turn) or upside down, resting on the ground line b."""
    hw, h = dim[0] * s, dim[1] * s
    if mode == "side":      # rotate(-90): x' = y in [-h, 0], y' = -x in [-hw, hw]
        return f'<g transform="translate({ax + h / 2} {b - hw}) rotate(-90) scale({s})">{piece}</g>'
    return f'<g transform="translate({ax} {b - h}) rotate(180) scale({s})">{piece}</g>'


def sheet():
    W = 1800
    o = [f'<text x="60" y="62" font-family="Righteous" font-size="32" fill="#0F3A48">Token studies: Decay on a base, and warning-sign threat ladders</text>',
         f'<text x="60" y="94" font-family="Josefin" font-size="18" fill="#4A4F55">To scale, 8 px = 1 mm. Threat in gunmetal plastic; Decay in rust-brown plastic. The pieces first; the icons will follow them.</text>']
    y = 130
    o.append(f'<rect x="40" y="{y}" width="{W - 80}" height="340" rx="18" fill="#F7F1E4" stroke="#D8CDB6"/>')
    o.append(f'<text x="70" y="{y + 40}" font-family="Righteous" font-size="26" fill="#0F3A48">1 · Decay as a token (every option on a round base, 11 mm)</text>')
    for i, (name, side, top, note) in enumerate(DECAY):
        x = 140 + i * 420
        o.append(f'<line x1="{x - 70}" y1="{y + 210}" x2="{x + 70}" y2="{y + 210}" stroke="#B9AE98" stroke-width="2"/>')
        o.append(g(side, x, y + 210) + g(top, x + 160, y + 160))
        o.append(f'<text x="{x}" y="{y + 236}" font-family="Josefin" font-size="13" fill="#7A7468" text-anchor="middle">side</text>'
                 f'<text x="{x + 160}" y="{y + 236}" font-family="Josefin" font-size="13" fill="#7A7468" text-anchor="middle">above</text>')
        o.append(f'<text x="{x + 80}" y="{y + 270}" font-family="Righteous" font-size="20" fill="#2B2F33" text-anchor="middle">{name}</text>')
        for j, part in enumerate(note.split(": ")):
            o.append(f'<text x="{x + 80}" y="{y + 294 + 18 * j}" font-family="Josefin" font-size="14" fill="#4A4F55" text-anchor="middle">{part}</text>')
    y += 360
    for name, pieces, note, dim in SIGNS:
        o.append(f'<rect x="40" y="{y}" width="{W - 80}" height="290" rx="18" fill="#F7F1E4" stroke="#D8CDB6"/>')
        o.append(f'<text x="70" y="{y + 40}" font-family="Righteous" font-size="24" fill="#0F3A48">{name}</text>')
        o.append(f'<text x="70" y="{y + 66}" font-family="Josefin" font-size="16" fill="#4A4F55">{note}</text>')
        b = y + 250
        o.append(f'<line x1="70" y1="{b}" x2="760" y2="{b}" stroke="#B9AE98" stroke-width="2"/>')
        for i, (p, lab) in enumerate(zip(pieces, ("Glitch", "Fault", "Failure"))):
            o.append(g(p, 170 + i * 230, b))
            o.append(f'<text x="{170 + i * 230}" y="{b + 26}" font-family="Josefin" font-size="14" font-weight="700" fill="#4A4F55" text-anchor="middle">{lab}</text>')
        o.append(f'<line x1="820" y1="{b}" x2="1720" y2="{b}" stroke="#B9AE98" stroke-width="2"/>')
        for ax, k, mode, lab in ((930, 1, "side", "Fault, 1 damage"), (1220, 2, "side", "Failure, 1 damage"), (1540, 2, "up", "Failure, 2 damage")):
            o.append(lay(pieces[k], dim[k], ax, b, mode, 0.85 if k == 2 else 1.0))
            o.append(f'<text x="{ax}" y="{b + 26}" font-family="Josefin" font-size="14" fill="#8A3A16" text-anchor="middle">{lab}</text>')
        y += 310
    font = ROOT / "art" / "fonts"
    H = y + 20
    defs = (f"<defs><style>@font-face {{ font-family: Righteous; src: url('{(font / 'Righteous-Regular.ttf').as_uri()}'); }}"
            f"@font-face {{ font-family: Josefin; src: url('{(font / 'JosefinSans[wght].ttf').as_uri()}'); }}</style></defs>")
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{defs}<rect width="{W}" height="{H}" fill="#EDE6D8"/>{"".join(o)}</svg>', (W, H)


def main():
    svg, (w, h) = sheet()
    f = OUT / "token_studies.svg"
    f.write_text(svg)
    png = OUT / "token_studies.png"
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{w},height:{h}}},deviceScaleFactor:1}});"
          f"await p.goto('{f.as_uri()}');await p.waitForTimeout(400);await p.screenshot({{path:'{png}'}});await b.close();}})();")
    subprocess.run(["node", "-e", js], check=True)
    print("wrote", f.relative_to(ROOT), "and", png.relative_to(ROOT))


if __name__ == "__main__":
    main()
