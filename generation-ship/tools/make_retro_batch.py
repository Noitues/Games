"""Build the Retro batch 2 Batch API input files from art/CHATGPT_PROMPTS.md.

    python3 tools/make_retro_batch.py [--batch 2|3]
    -> art/retro_batch2_edits.jsonl        (/v1/images/edits: a layout guide attached as a data URL)
    -> art/retro_batch2_generations.jsonl  (/v1/images/generations)

A batch file may hold one endpoint and one model, hence two files. One image per request; the
custom_id "retro__<name>" (or "retro__<name>__<k>" for variant k) is what
tools/decode_image_batch.py turns into art/source/retro/<name>.png (<name>_<k>.png).
Submit with tools/submit_batch.py. Prints the image count and an estimated cost.
"""
import base64
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_images import BATCH_IMAGE_MODEL  # noqa: E402
import generate_retro_v2  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
GUIDES = ROOT / "art" / "templates" / "retro"
QUALITY = "high"
# Batch rates per 1M tokens (developers.openai.com pricing, 2026-11-05): image output, image input, text input.
RATE_OUT, RATE_IMG_IN, RATE_TXT_IN = 15.0, 4.0, 2.5
# Measured on the v2 run (high quality): about 1,700 output tokens for a card, 1,230 for the Wall.
EST_OUT_TOKENS, EST_GUIDE_TOKENS, EST_TEXT_TOKENS = 1700, 1500, 500

HOUSES = {
    "galvan": "Galvan, the Spark-Wardens: fast, aggressive repair; lightning bolts, sparks and coiled cables, electric-blue accent",
    "keel": "Keel, the Hullwrights: slow and defensive; riveted hull plates, braces and anchors, steel-grey and turquoise accent",
    "gardeners": "Gardeners, the Greenkeepers: influence as armour; vines, leaves and seed pods, lime-green accent",
    "voidwardens": "Voidwardens, the Airlock Keepers: Outer Hull specialists; airlock hatches, portholes and stars, deep violet accent",
}

# name: (prompt key, guide or None, size, variants)
EDITS = {
    "card_frame_v2c": ("card_frame_v2", "card_guide.png", "1104x1504", 1),
    "card_frame_v2d": ("card_frame_v2", "card_guide.png", "1104x1504", 1),
    "wall_panel_v2c": ("wall_panel_v2", "wall_guide.png", "2320x960", 1),
    "wall_panel_v2d": ("wall_panel_v2", "wall_guide.png", "2320x960", 1),
    **{f"board_{b}_v2": ("board", f"board_{b}_guide.png", "1296x1536", 2) for b in "abcd"},
}
EDITS_3 = {f"{n}_v3{v}": (f"{n}_v3", g, size, 1) for n, g, size in
           (("wall_panel", "wall_guide.png", "2320x960"), ("card_frame", "card_guide.png", "1104x1504")) for v in "ab"}
GENERATIONS_3 = {n: (n, None, "1536x1024", 1) for n in ("threat_machine_parts", "threat_gremlins", "people_pieces")}
GENERATIONS_4 = {**{n: (n, None, "1536x1536", 1) for n in ("cover_generations", "cover_ancestors", "cover_ship")},
                 **{n: (n, None, "1536x640", 1) for n in ("logo_a", "logo_b")}}
EMBLEMS = {
    "meridian": "a flowing wave crossing a compass meridian arc with a small arrowhead, ocean teal and gold",
    "vigil": "a mid-century lantern with radiating rays of light, amber and gold",
    "foremen": "a shift whistle crossed with a riveter's hammer over a gear, brick red and chrome",
    "tellers": "an open book with a starburst rising from its pages, rose and gold",
    "galvan": "a lightning bolt striking through a cog, crackling sparks, electric blue",
    "keel": "a ship's anchor over a riveted hull plate, steel grey and turquoise",
    "gardeners": "a sprouting seed inside a glass dome with two leaves, lime green",
    "voidwardens": "a round airlock hatch wheel with a four-pointed star at its centre, deep violet",
}
EDITS_5 = {"event_frame_a": ("event_frame", "event_guide.png", "1104x1504", 1),
           "event_frame_b": ("event_frame", "event_guide.png", "1104x1504", 1),
           "event_example": ("event_example", "event_guide.png", "1104x1504", 1),
           **{f"house_{h}_v2": ("house_board_v2", f"house_{h}_guide.png", "1536x1024", 1) for h in EMBLEMS}}
HOUSE_LOOK_2 = {   # the other four houses (Retro batch 7)
    "meridian": ("ocean teal (#2A9D8F)", "faint flowing current lines and route-map dashes"),
    "vigil": ("amber (#E8A23A) with a cream border, not gold on gold", "faint lamplight rays and a few constellation lines"),
    "foremen": ("brick red (#C9482A)", "faint girders, rivets and a shift-roster grid"),
    "tellers": ("dusky rose (#D86A8A)", "faint ribbons of script-like flourishes and page edges, with no readable letters"),
}
HOUSE_LOOK = {   # colour, background motif (the emblem is EMBLEMS)
    "galvan": ("electric blue (#3A6FD8)", "faint arcing electrical traces and circuit lines"),
    "keel": ("steel grey (#7A8C96), not turquoise", "faint riveted hull plates, seams and cross-braces"),
    "gardeners": ("lime green (#8FB04A)", "faint climbing vines and leaf veins"),
    "voidwardens": ("deep violet (#6A4A9A)", "a faint starfield and concentric airlock rings"),
}
EDITS_6 = {f"house_{h}_v3": ("house_board_v3", f"house_{h}_guide.png", "1536x1024", 1) for h in HOUSE_LOOK}
EDITS_7 = {f"house_{h}_v3": ("house_board_v3", f"house_{h}_guide.png", "1536x1024", 1) for h in HOUSE_LOOK_2}
HOUSE_LOOK.update(HOUSE_LOOK_2)
EDITS_8 = {**{f"card_frame_v4{v}": ("card_frame_v4", "card_guide.png", "1104x1504", 1) for v in "ab"},
           **{f"wall_panel_v4{v}": ("wall_panel_v3", "wall_guide.png", "2320x960", 1) for v in "ab"}}
EDITS_9 = {"board_d_v2": ("board", "board_d_guide.png", "1296x1536", 2)}   # board D reshaped (2026-11-06)
GENERATIONS = {
    "card_back": ("card_back", None, "1104x1504", 1),
    **{f"icon_{t}": (f"icon_{t}", None, "1024x1024", 1) for t in ("infrastructure", "residential", "government", "agricultural")},
    **{f"token_{t}": (f"token_{t}", None, "1024x1024", 1) for t in ("glitch", "fault", "failure", "crew", "decay", "breakthrough")},
    "token_influence": ("token_influence", None, "1536x1024", 1),
    **{f"house_{h}": ("house_<id>", None, "1536x1024", 1) for h in HOUSES},
}


def prompts(batch):
    text = (ROOT / "art" / "CHATGPT_PROMPTS.md").read_text()
    sec = text.split(f"## Retro batch {batch}", 1)[1].split("\n## Retro batch ", 1)[0]
    return {k: v for k, v in re.findall(r"`([\w<>]+)\.png`[^\n]*\n```\n(.*?)\n```", sec, re.S)}


def build(jobs, endpoint, style, ps):
    lines, n_img, n_guide = [], 0, 0
    for name, (key, guide, size, variants) in jobs.items():
        if key.endswith("_v2") and key not in ps:
            full = generate_retro_v2.prompt_for(key.removesuffix("_v2"))
        else:
            body = ps[key]
            if key == "house_<id>":
                body = body.replace("<identity>", HOUSES[name.removeprefix("house_")])
            if key == "house_board_v3":
                h = name.removeprefix("house_").removesuffix("_v3")
                body = body.replace("<colour>", HOUSE_LOOK[h][0]).replace("<emblem>", EMBLEMS[h]).replace("<motif>", HOUSE_LOOK[h][1])
            if key == "house_board_v2":
                body = body.replace("<emblem>", EMBLEMS[name.removeprefix("house_").removesuffix("_v2")])
            full = f"{style}\n\n{body}"
        for k in range(variants):
            b = {"model": BATCH_IMAGE_MODEL, "prompt": full, "size": size, "quality": QUALITY}
            if name.startswith("logo_"):
                b["background"] = "transparent"
                b["output_format"] = "png"
            if guide:
                data = base64.b64encode((GUIDES / guide).read_bytes()).decode()
                b["images"] = [{"image_url": f"data:image/png;base64,{data}"}]
                n_guide += 1
            else:
                b["n"] = 1
            cid = f"retro__{name}" + (f"__{k + 1}" if k else "")
            lines.append({"custom_id": cid, "method": "POST", "url": endpoint, "body": b})
            n_img += 1
    return lines, n_img, n_guide


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=2, choices=(2, 3, 4, 5, 6, 7, 8, 9))
    batch = ap.parse_args().batch
    ps = prompts({7: 6, 9: 2}.get(batch, batch))   # batch 7 reuses batch 6 (house boards), batch 9 batch 2 (boards)
    if batch == 9:
        ps = prompts(2)                            # batch 9 reuses batch 2's board prompt
    if batch == 8:
        ps = {**prompts(3), **ps}                  # batch 8's Wall reuses batch 3's wall_panel_v3
    edits, gens = {2: (EDITS, GENERATIONS), 3: (EDITS_3, GENERATIONS_3), 4: ({}, GENERATIONS_4), 5: (EDITS_5, {}), 6: (EDITS_6, {}), 7: (EDITS_7, {}), 8: (EDITS_8, {}), 9: (EDITS_9, {})}[batch]
    text = (ROOT / "art" / "CHATGPT_PROMPTS.md").read_text()
    sec = text.split("## D · Retro Space", 1)[1]
    opener = re.search(r"\*\*Opener\*\*\n```\n(.*?)\n```", sec, re.S).group(1)
    style = re.sub(r"Reply \"ready\".*$", "", opener).replace("Every image in this chat uses this style:", "Style:").strip()
    total_img = total_cost = 0
    for jobs, endpoint, fname in ((edits, "/v1/images/edits", f"retro_batch{batch}_edits.jsonl"),
                                  (gens, "/v1/images/generations", f"retro_batch{batch}_generations.jsonl")):
        if not jobs:
            continue
        lines, n_img, n_guide = build(jobs, endpoint, style, ps)
        out = ROOT / "art" / fname
        out.write_text("".join(json.dumps(x) + "\n" for x in lines))
        cost = (n_img * EST_OUT_TOKENS * RATE_OUT + n_guide * EST_GUIDE_TOKENS * RATE_IMG_IN
                + n_img * EST_TEXT_TOKENS * RATE_TXT_IN) / 1e6
        total_img += n_img
        total_cost += cost
        print(f"{out.relative_to(ROOT)}: {n_img} images ({endpoint}, {BATCH_IMAGE_MODEL}, {QUALITY}), about ${cost:.2f}")
        for x in lines:
            print("   ", x["custom_id"], x["body"]["size"])
    print(f"total: {total_img} images, about ${total_cost:.2f} at the Batch rate")


if __name__ == "__main__":
    main()
