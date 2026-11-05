"""Generate the concept-art images directly (no Batch API), one request at a time.

Run from the generation-ship folder. On your own computer, put your key in the environment
(in a Claude cloud session with an OpenAI network secret, no key is needed):
    export OPENAI_API_KEY=...            (Windows PowerShell: $env:OPENAI_API_KEY="...")
    python3 tools/generate_images.py [--only retro] [--names ostra,board_a] [--quality medium]

Reads the requests in art/image_batch.jsonl (/v1/images/generations) and saves
art/source/<style>/<name>.png (variants: <name>_2.png ...). Skips images that already exist,
so it can be re-run after an interruption. Standard library only; no installs needed.
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.openai.com/v1/images/generations"
# gpt-image-1 was shut down on 2026-10-23. GPT Image 2.6 Sunburst is OpenAI's current model for
# detailed work and edit precision (Flare, gpt-image-2.6-flare, is the fast one).
DEFAULT_IMAGE_MODEL = "gpt-image-2.6-sunburst"
# The Batch API (half price) takes GPT Image 2.5 only, for /v1/images/generations and /edits.
BATCH_IMAGE_MODEL = "gpt-image-2.5-sunburst"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated styles (grimdark,spacepunk,newage,retro)")
    ap.add_argument("--names", help="comma-separated image names (ostra,dace,ilka,pell,board_a,card_frame,wall_panel,cover)")
    ap.add_argument("--quality", help="override quality: low, medium, high, xhigh or max")
    ap.add_argument("--model", default=DEFAULT_IMAGE_MODEL, help="image model (replaces the model in the batch file)")
    a = ap.parse_args()
    # On your own computer, set OPENAI_API_KEY. In a Claude cloud session with an OpenAI network
    # secret, leave it unset: the session's proxy adds the key to requests to api.openai.com.
    key = os.environ.get("OPENAI_API_KEY")
    styles = set(a.only.split(",")) if a.only else None
    names = set(a.names.split(",")) if a.names else None
    reqs = [json.loads(l) for l in (ROOT / "art" / "image_batch.jsonl").read_text().splitlines() if l.strip()]
    for r in reqs:
        style, name = r["custom_id"].split("__", 1)
        if (styles and style not in styles) or (names and name not in names):
            continue
        out = ROOT / "art" / "source" / style
        if (out / f"{name}.png").exists():
            print("exists, skipping", style, name)
            continue
        body = dict(r["body"])
        body["model"] = a.model
        if a.quality:
            body["quality"] = a.quality
        print(f"generating {style}/{name} ({body['size']}, x{body.get('n', 1)}) ...", flush=True)
        headers = {"Content-Type": "application/json"}
        if key:
            headers["Authorization"] = f"Bearer {key}"
        req = urllib.request.Request(API, data=json.dumps(body).encode(), method="POST", headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            print(f"  FAILED: {e.code} {e.read().decode()[:300]}")
            continue
        out.mkdir(parents=True, exist_ok=True)
        for i, img in enumerate(data.get("data", [])):
            f = out / (f"{name}.png" if i == 0 else f"{name}_{i + 1}.png")
            f.write_bytes(base64.b64decode(img["b64_json"]))
            print("  saved", f.relative_to(ROOT))


if __name__ == "__main__":
    main()
