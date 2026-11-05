"""Brainstorm: five families for the threat ladder (Glitch -> Fault -> Failure), as silhouettes.

    python3 tools/threat_concepts.py   -> art/tokens/threat_concepts.svg (+ .png)

Each family is drawn to scale (about 10 / 14 / 22 mm, in gunmetal plastic) with its damage postures
(Fault: 1 state; Failure: 2 states, no extra parts) and a scorecard against what the ladder must
do: read as one thing escalating; distinct silhouettes at 10 mm; fit "the Forgotten Machine"; make
the verbs (repair, vent, seed, grow) feel right; survive manufacture (no thin parts).
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "art" / "tokens"
GUN, HI, INK, ACT, CREAM = "#4E545B", "#7A8088", "#1A1D20", "#E8603A", "#FBEFD6"
K = 8                                         # px per mm


def g(body, x, y, s=1.0, rot=0):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">{body}</g>'


def solid(d, extra=""):
    return f'<path d="{d}" fill="{GUN}" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>{extra}'


# Each piece is drawn standing on y = 0, centred on x = 0, in px (K per mm).
FAMILIES = [
    ("Machine parts (current)", "loose nut → broken cog → cracked vacuum tube", [
        solid("M-40,0 L-46,-12 L-40,-34 L40,-34 L46,-12 L40,0 Z"),
        solid("M-56,0 L-50,-30 L-56,-56 L-30,-56 L-20,-90 L20,-90 L30,-56 L56,-56 L50,-30 L56,0 Z"),
        solid("M-44,0 L-44,-30 L-18,-30 L-18,-48 C-38,-56 -38,-80 -38,-150 C-38,-178 38,-178 38,-150 C38,-80 38,-56 18,-48 L18,-30 L44,-30 L44,0 Z")],
     ["+ one family, clearly mechanical", "− nut and cog read as 'spare parts', not 'danger'", "− weakest escalation feeling"], 2),
    ("Leaks", "coolant drip → spraying pipe joint → burst valve", [
        solid("M0,-56 C14,-34 24,-22 24,-12 C24,4 -24,4 -24,-12 C-24,-22 -14,-34 0,-56 Z"),
        solid("M-56,0 L-56,-24 L-14,-24 L-14,-70 L14,-70 L14,-24 L14,-24 L14,0 Z",
              f'<path d="M14,-60 L60,-90 M14,-52 L66,-60 M14,-44 L60,-30" stroke="{GUN}" stroke-width="9" stroke-linecap="round"/>'),
        solid("M-40,0 L-40,-24 L-16,-24 L-16,-60 L-48,-60 L-48,-74 L48,-74 L48,-60 L16,-60 L16,-24 L40,-24 L40,0 Z",
              f'<path d="M0,-74 C-30,-90 -40,-130 -10,-150 C-30,-170 10,-190 24,-170 C50,-176 56,-140 36,-128 C56,-110 30,-84 0,-74 Z" fill="{GUN}" stroke="{INK}" stroke-width="2.5"/>')],
     ["+ the machine failing, physically: drip, spray, burst", "+ vent = it flows to the next section; Hull seeds = air leaks",
      "+ chunky shapes; posture works (drip has no state)", "− steam plume must be sculpted solid"], 5),
    ("Alarms", "warning lamp → klaxon → beacon tower", [
        solid("M-34,0 L-34,-14 L-24,-14 C-24,-44 24,-44 24,-14 L34,-14 L34,0 Z"),
        solid("M-40,0 L-40,-16 L-10,-16 L-10,-40 L-40,-70 L-40,-96 L40,-96 L40,-70 L10,-40 L10,-16 L40,-16 L40,0 Z"),
        solid("M-36,0 L-36,-20 L-20,-20 L-20,-120 L-30,-120 L-30,-136 C-30,-176 30,-176 30,-136 L30,-120 L20,-120 L20,-20 L36,-20 L36,0 Z",
              f'<path d="M-30,-146 L-60,-162 M30,-146 L60,-162 M0,-176 L0,-196" stroke="{GUN}" stroke-width="7" stroke-linecap="round"/>')],
     ["+ instantly reads as 'danger, rising'", "+ great silhouettes, very retro",
      "− an alarm is the symptom, not the problem: 'repairing an alarm' is odd", "− could be cast in translucent amber (a colour)"], 3),
    ("Rogue drones", "maintenance drone → crawler → servitor", [
        solid("M-40,-14 C-40,-34 40,-34 40,-14 L48,-14 L48,-6 L-48,-6 L-48,-14 Z",
              f'<path d="M-24,-6 L-30,0 M24,-6 L30,0" stroke="{GUN}" stroke-width="7" stroke-linecap="round"/>'),
        solid("M-30,-30 C-30,-64 30,-64 30,-30 Z",
              f'<path d="M-28,-30 L-56,0 M-14,-30 L-30,0 M14,-30 L30,0 M28,-30 L56,0" stroke="{GUN}" stroke-width="9" stroke-linecap="round"/>'),
        solid("M-30,0 L-30,-60 L-40,-60 L-40,-120 L-20,-120 L-20,-160 L20,-160 L20,-120 L40,-120 L40,-60 L30,-60 L30,0 L8,0 L8,-50 L-8,-50 L-8,0 Z",
              f'<path d="M0,-160 L0,-184" stroke="{GUN}" stroke-width="5"/><circle cx="0" cy="-188" r="6" fill="{GUN}" stroke="{INK}" stroke-width="2"/>')],
     ["+ strongest silhouettes; posture reads naturally (knocked over)", "+ the ship's own servants turning: on theme",
      "− makes the threat an enemy with intent, not decay", "− legs and antennae: thin parts"], 4),
    ("Electrical", "spark → arcing coil → fire", [
        solid("M-6,0 L-6,-20 L-20,-20 L4,-60 L0,-34 L16,-34 L-2,0 Z"),
        solid("M-30,0 L-30,-14 L-12,-14 L-12,-80 L12,-80 L12,-14 L30,-14 L30,0 Z",
              "".join(f'<rect x="-20" y="{-74 + 12 * i}" width="40" height="7" rx="3" fill="{GUN}" stroke="{INK}" stroke-width="2"/>' for i in range(5))),
        solid("M-40,0 C-50,-40 -30,-80 -10,-110 C-12,-80 0,-70 10,-90 C20,-130 6,-160 22,-180 C40,-140 60,-100 46,-40 C44,-20 40,-6 40,0 Z")],
     ["+ urgent and readable", "+ fire is the classic escalation",
      "− thin zigzags and flame tips snap off", "− fire on a ship pulls the tone towards disaster film"], 3),
]


def sheet():
    W, rowh = 1800, 300
    H = 120 + rowh * len(FAMILIES) + 60
    o = [f'<rect width="{W}" height="{H}" fill="#EDE6D8"/>',
         f'<text x="60" y="62" font-family="Righteous" font-size="32" fill="#0F3A48">The threat ladder: five families</text>',
         f'<text x="60" y="94" font-family="Josefin" font-size="18" fill="#4A4F55">Glitch → Fault → Failure, gunmetal plastic, to scale (8 px = 1 mm). Right: the Failure\'s damage postures (on its side, upside down). Score: designer fit, out of 5.</text>']
    y = 140
    for name, ladder, pieces, notes, score in FAMILIES:
        base = y + 220
        o.append(f'<rect x="40" y="{y}" width="{W - 80}" height="{rowh - 20}" rx="18" fill="#F7F1E4" stroke="#D8CDB6"/>')
        o.append(f'<text x="70" y="{y + 40}" font-family="Righteous" font-size="26" fill="#0F3A48">{name}</text>')
        o.append(f'<text x="70" y="{y + 68}" font-family="Josefin" font-size="17" fill="#4A4F55">{ladder}</text>')
        o.append(f'<line x1="70" y1="{base}" x2="760" y2="{base}" stroke="#B9AE98" stroke-width="2"/>')
        for i, (p, lab) in enumerate(zip(pieces, ("Glitch", "Fault", "Failure"))):
            x = 150 + i * 220
            o.append(g(p, x, base))
            o.append(f'<text x="{x}" y="{base + 28}" font-family="Josefin" font-size="15" font-weight="700" fill="#4A4F55" text-anchor="middle">{lab}</text>')
        # the Failure's damage postures
        o.append(f'<line x1="800" y1="{base}" x2="1120" y2="{base}" stroke="#B9AE98" stroke-width="2"/>')
        o.append(g(pieces[2], 880, base - 30, 0.8, -90))
        o.append(g(pieces[2], 1050, base - 150, 0.8, 180))
        o.append(f'<text x="880" y="{base + 28}" font-family="Josefin" font-size="15" fill="#8A3A16" text-anchor="middle">1 damage</text>')
        o.append(f'<text x="1050" y="{base + 28}" font-family="Josefin" font-size="15" fill="#8A3A16" text-anchor="middle">2 damage</text>')
        for j, n in enumerate(notes):
            col = "#2E6B3A" if n.startswith("+") else "#8A3A16"
            o.append(f'<text x="1160" y="{y + 50 + 30 * j}" font-family="Josefin" font-size="17" fill="{col}">{n}</text>')
        o.append(f'<text x="1160" y="{y + 50 + 30 * len(notes) + 10}" font-family="Righteous" font-size="20" fill="#0F3A48">'
                 f'{"★" * score}{"☆" * (5 - score)}</text>')
        y += rowh
    font = ROOT / "art" / "fonts"
    defs = (f"<defs><style>@font-face {{ font-family: Righteous; src: url('{(font / 'Righteous-Regular.ttf').as_uri()}'); }}"
            f"@font-face {{ font-family: Josefin; src: url('{(font / 'JosefinSans[wght].ttf').as_uri()}'); }}</style></defs>")
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{defs}{"".join(o)}</svg>', (W, H)


def main():
    svg, (w, h) = sheet()
    f = OUT / "threat_concepts.svg"
    f.write_text(svg)
    png = OUT / "threat_concepts.png"
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{w},height:{h}}},deviceScaleFactor:1}});"
          f"await p.goto('{f.as_uri()}');await p.waitForTimeout(400);await p.screenshot({{path:'{png}'}});await b.close();}})();")
    subprocess.run(["node", "-e", js], check=True)
    print("wrote", f.relative_to(ROOT), "and", png.relative_to(ROOT))


if __name__ == "__main__":
    main()
