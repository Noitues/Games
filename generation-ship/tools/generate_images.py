"""Generate the concept-art images directly (no Batch API), one request at a time.

Run on your own computer, from the generation-ship folder, with your key in the environment:
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated styles (grimdark,spacepunk,newage,retro)")
    ap.add_argument("--names", help="comma-separated image names (ostra,dace,ilka,pell,board_a,card_frame,wall_panel,cover)")
    ap.add_argument("--quality", help="override quality: low, medium or high")
    a = ap.parse_args()
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.exit("Set OPENAI_API_KEY in your environment first.")
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
        if a.quality:
            body["quality"] = a.quality
        print(f"generating {style}/{name} ({body['size']}, x{body.get('n', 1)}) ...", flush=True)
        req = urllib.request.Request(API, data=json.dumps(body).encode(), method="POST",
                                     headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
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
