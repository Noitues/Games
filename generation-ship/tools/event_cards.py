"""Typeset event cards on the Retro event frame (tuck-below layout, tools/retro_templates.py EVENT).

    python3 tools/event_cards.py   -> art/source/retro/event_<id>.png (a few examples) and
                                      art/mockups/event_tuck_demo.png (an event tucked under a leader)

Upper part (covered once the leader is placed): the picture and the one-time effect, if the event
has one. Band (always visible): stage, section-type icon(s), type name, twist.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import retro_templates as rt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "art" / "source" / "retro"
FONTS = ROOT / "art" / "fonts"
S, B = rt.CARD_PX, rt.BLEED
ICON = {"Infrastructure": "icon_infrastructure", "Residential": "icon_residential", "Government": "icon_government",
        "Agricultural": "icon_agricultural"}
NUMERAL = {1: "I", 2: "II", 3: "III", 4: "★"}


def font(name, px, weight=None):
    f = ImageFont.truetype(str(FONTS / name), px)
    if weight:
        try:
            f.set_variation_by_name(weight)
        except (OSError, ValueError):
            pass
    return f


def px(x, y):
    return ((x + B) * S, (y + B) * S)


def wrap(d, text, f, width):
    lines, line = [], ""
    for w in text.split():
        t = (line + " " + w).strip()
        if d.textlength(t, font=f) <= width or not line:
            line = t
        else:
            lines.append(line)
            line = w
    return lines + [line]


def typeset(event, frame="event_example.png"):
    im = Image.open(SRC / frame).convert("RGB")
    d = ImageDraw.Draw(im)
    E = rt.EVENT
    # one-time effect (covered once the leader is placed)
    x, y, w, h, _ = E["once"]
    once = event.get("once") or "One-time effect, if this event has one: read it when the event is revealed. The leader covers it."
    f = font("JosefinSans[wght].ttf", round(2.5 * S), "Medium")
    yy = (y + 3.6) * S + B * S
    d.text(px(x + 2.5, y + 2.2), "WHEN REVEALED", fill=rt.TANGERINE, font=font("JosefinSans[wght].ttf", round(2.2 * S), "Bold"))
    for line in wrap(d, once, f, (w - 5) * S)[:4]:
        d.text(((x + 2.5 + B) * S, yy + 1.2 * S), line, fill=rt.TEAL, font=f)
        yy += 3.1 * S
    # band: stage, icons, name, twist
    cx, cy, r = E["stage"]
    d.text(px(cx, cy), NUMERAL[event["stage"]], fill=rt.TEAL, font=font("Righteous-Regular.ttf", round(4.6 * S)), anchor="mm")
    (a, c, ri) = E["icons"]
    types = event["types"]
    spots = [a, c] if len(types) == 2 else [a]
    if len(types) == 1:                                # paint the unused socket out with the band colour
        band = im.getpixel((round((c[0] + ri + 3 + B) * S), round((c[1] + B) * S)))
        d.ellipse(((c[0] - ri - 0.6 + B) * S, (c[1] - ri - 0.6 + B) * S, (c[0] + ri + 0.6 + B) * S, (c[1] + ri + 0.6 + B) * S), fill=band)
    for (ix, iy), t in zip(spots, types):
        ic = Image.open(SRC / f"{ICON[t]}.png").convert("RGBA").resize((round(2 * ri * S * 0.92),) * 2, Image.LANCZOS)
        m = Image.new("L", ic.size, 0)
        ImageDraw.Draw(m).ellipse((0, 0, ic.width - 1, ic.height - 1), fill=255)
        im.paste(ic, (round((ix + B) * S - ic.width / 2), round((iy + B) * S - ic.height / 2)), m)
    x, y, w, h, _ = E["name"]
    d.text(px(x + w / 2, y + h / 2), " + ".join(types), fill=rt.TEAL, font=font("Righteous-Regular.ttf", round(3.3 * S)), anchor="mm")
    x, y, w, h, _ = E["twist"]
    tw = (event.get("twist") or {}).get("text") or "No twist."
    f = font("JosefinSans[wght].ttf", round(2.3 * S), "SemiBold")
    lines = wrap(d, tw, f, (w - 4) * S)[:2]
    for i, line in enumerate(lines):
        d.text(((x + w / 2 + B) * S, (y + h / 2 + B + (i - (len(lines) - 1) / 2) * 2.8) * S), line, fill=rt.TEAL, font=f, anchor="mm")
    return im


def tuck_demo(event_im, leader_im):
    """The event tucked under its leader, as on the conveyor: only the band shows below."""
    s = 6 / S                                     # to 6 px per mm
    ev = event_im.resize((round(event_im.width * s), round(event_im.height * s)), Image.LANCZOS)
    ld = leader_im.resize((round(leader_im.width * s), round(leader_im.height * s)), Image.LANCZOS)
    off = round(30.5 * 6)
    canvas = Image.new("RGB", (ev.width + 40, ev.height + off + 40), (237, 230, 216))
    canvas.paste(ev, (20, 20 + off))
    canvas.paste(ld, (20, 20))
    return canvas


def main():
    events = json.loads((ROOT / "data" / "events.json").read_text())["cards"]
    picks = [e for e in events if e["id"] in ("E1-1", "E2-1", "E3-1")]
    outs = []
    for e in picks:
        frame = "event_example.png" if e["types"] == ["Infrastructure"] else "event_frame_b.png"
        im = typeset(e, frame)
        out = SRC / f"event_{e['id']}.png"
        im.save(out)
        outs.append(out)
        print("wrote", out.relative_to(ROOT))
    leader = Image.open(SRC / "card_frame_v3b_exact.png").convert("RGB")
    demo = tuck_demo(Image.open(outs[1]), leader)
    out = ROOT / "art" / "mockups" / "event_tuck_demo.png"
    demo.save(out)
    print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
