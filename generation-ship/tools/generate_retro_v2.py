"""Generate the revised Retro card frame and Wall panel (v2) directly, one request per image.

Direct requests cost twice the Batch API rate. The project runs image work as complete batches;
this script exists for the one-off v2 test (2026-11-05) and for re-running it.

    python3 tools/generate_retro_v2.py [--names card_frame,wall_panel] [--variants 2] [--quality high]

Each request sends the flat layout guide from tools/retro_templates.py (art/templates/retro/) to
/v1/images/edits with the prompt from art/CHATGPT_PROMPTS.md ("Retro v2"), so the painted frame keeps
the master window and the Legacy plaque exactly where the card template puts them. Saves
art/source/retro/<name>_v2a.png, _v2b.png ... and an _exact copy with the windows re-cut from the
master geometry. Skips files that already exist. Standard library + Pillow.

On your own computer set OPENAI_API_KEY; in a Claude cloud session with an OpenAI network secret the
proxy adds it.
"""
import argparse
import base64
import json
import os
import re
import string
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_images import DEFAULT_IMAGE_MODEL  # noqa: E402
import retro_templates as rt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.openai.com/v1/images/edits"
JOBS = {  # name: (guide, size = the guide's own size, so 1 guide px = 1 output px)
    "card_frame": ("card_guide.png", "1104x1504", "card"),
    "wall_panel": ("wall_guide.png", "2320x960", "wall"),
}


def prompt_for(name):
    """The 'Retro v2' prompt for <name>_v2.png from CHATGPT_PROMPTS.md, after the style text."""
    text = (ROOT / "art" / "CHATGPT_PROMPTS.md").read_text()
    sec = text.split("## D · Retro Space", 1)[1].split("\n## ", 1)[0]
    opener = re.search(r"\*\*Opener\*\*\n```\n(.*?)\n```", sec, re.S).group(1)
    style = re.sub(r"Reply \"ready\".*$", "", opener).replace("Every image in this chat uses this style:", "Style:").strip()
    body = re.search(rf"`{name}_v2\.png`\n```\n(.*?)\n```", sec, re.S).group(1)
    return f"{style}\n\n{body}"


def multipart(fields, files):
    b = uuid.uuid4().hex
    out = []
    for k, v in fields.items():
        out.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    for k, (fname, data) in files.items():
        out.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"; filename="{fname}"\r\n'
                   f'Content-Type: image/png\r\n\r\n'.encode() + data + b"\r\n")
    out.append(f"--{b}--\r\n".encode())
    return b"".join(out), f"multipart/form-data; boundary={b}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--names", default="card_frame,wall_panel")
    ap.add_argument("--variants", type=int, default=2)
    ap.add_argument("--quality", default="high")
    ap.add_argument("--model", default=DEFAULT_IMAGE_MODEL)
    a = ap.parse_args()
    key = os.environ.get("OPENAI_API_KEY")
    out = ROOT / "art" / "source" / "retro"
    for name in a.names.split(","):
        guide, size, kind = JOBS[name]
        for k in range(a.variants):
            f = out / f"{name}_v2{string.ascii_lowercase[k]}.png"
            if f.exists():
                print("exists, skipping", f.relative_to(ROOT))
                continue
            # Streamed: a high-quality render takes longer than some proxies keep a silent request open
            # (30 s in a Claude cloud session); partial images keep the connection alive.
            fields = {"model": a.model, "prompt": prompt_for(name), "size": size, "quality": a.quality,
                      "stream": "true", "partial_images": "2"}
            body, ctype = multipart(fields, {"image": (guide, (rt.OUT / guide).read_bytes())})
            headers = {"Content-Type": ctype}
            if key:
                headers["Authorization"] = f"Bearer {key}"
            print(f"generating {f.name} ({a.model}, {size}, {a.quality}) ...", flush=True)
            try:
                with urllib.request.urlopen(urllib.request.Request(API, data=body, headers=headers, method="POST"), timeout=600) as r:
                    data = None
                    for line in r:  # server-sent events; the last one is image_edit.completed
                        if line.startswith(b"data: "):
                            ev = json.loads(line[6:])
                            if ev.get("type") == "image_edit.completed":
                                data = ev
            except urllib.error.HTTPError as e:
                print(f"  FAILED: {e.code} {e.read().decode()[:400]}")
                sys.exit(1)
            if not data:
                print("  FAILED: the stream ended without a finished image")
                sys.exit(1)
            f.write_bytes(base64.b64decode(data["b64_json"]))
            print("  saved", f.relative_to(ROOT), "and", rt.stamp(f, kind).relative_to(ROOT))
            if "usage" in data:
                print("  usage", json.dumps(data["usage"]))


if __name__ == "__main__":
    main()
