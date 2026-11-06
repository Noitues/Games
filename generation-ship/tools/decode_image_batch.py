"""Turn an OpenAI Batch API output file of image generations into PNG files.

    python3 tools/decode_image_batch.py path/to/batch_output.jsonl
    -> art/source/<style>/<name>.png   (extra variants: <name>_2.png, <name>_3.png, ...)

Each output line carries the custom_id ("<style>__<name>" or "<style>__<name>__<k>") and the API
response. Images come back base64-encoded: from /v1/images/generations in body.data[i].b64_json,
from /v1/responses in body.output[i].result (items of type "image_generation_call").
"""
import base64
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(path):
    ok = bad = 0
    for line in Path(path).read_text().splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        cid = rec.get("custom_id", "?")
        resp = rec.get("response") or {}
        if rec.get("error") or resp.get("status_code", 200) != 200:
            print(f"FAILED {cid}: {rec.get('error') or resp.get('body')}")
            bad += 1
            continue
        parts = cid.split("__")
        style, name = parts[0], parts[1]
        offset = int(parts[2]) - 1 if len(parts) > 2 else 0
        out = ROOT / "art" / "source" / style
        out.mkdir(parents=True, exist_ok=True)
        body = resp.get("body", {})
        items = body.get("data") or [{"b64_json": o.get("result")} for o in body.get("output", []) if o.get("type") == "image_generation_call"]
        for j, img in enumerate(items):
            i = j + offset
            b64 = img.get("b64_json")
            if not b64:
                print(f"no image data for {cid} #{i + 1}")
                continue
            f = out / (f"{name}.png" if i == 0 else f"{name}_{i + 1}.png")
            f.write_bytes(base64.b64decode(b64))
            ok += 1
            print("saved", f.relative_to(ROOT))
    print(f"{ok} images saved, {bad} requests failed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
