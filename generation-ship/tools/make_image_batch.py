"""Build an OpenAI Batch API input file (.jsonl) from art/CHATGPT_PROMPTS.md.

Each request is self-contained (a batch has no chat memory), so every prompt is the style's
description (from its "Opener") followed by the image prompt.

    python3 tools/make_image_batch.py [--endpoint responses|images] [--quality high] [--variants 2]
    -> art/image_batch_responses.jsonl  (default: /v1/responses with the image_generation tool)
    -> art/image_batch.jsonl            (--endpoint images: /v1/images/generations; --model sets the image model)

After the batch finishes, download its output file and run tools/decode_image_batch.py on it.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "art" / "CHATGPT_PROMPTS.md"
SIZES = {"Wide landscape": "1536x1024", "Tall portrait": "1024x1536", "Square": "1024x1024"}
# Images worth extra variants to choose from (the style anchor and the board).
KEY = {"ostra", "board_a"}
from generate_images import BATCH_IMAGE_MODEL  # the Batch API takes GPT Image 2.5 only


def style_text(opener):
    """The style part of an opener: drop the chat set-up and the 'reply ready' request."""
    t = opener.strip()
    t = re.sub(r"Reply \"ready\".*$", "", t).strip()
    t = t.replace("Every image in this chat uses this style:", "Style:")
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--endpoint", choices=["responses", "images"], default="responses")
    ap.add_argument("--model", default=None, help="images: the image model (default: BATCH_IMAGE_MODEL in generate_images.py); responses: the model that calls the image tool (default gpt-4.1-mini)")
    ap.add_argument("--quality", default="high")
    ap.add_argument("--variants", type=int, default=2, help="images for ostra and board_a (others get 1)")
    a = ap.parse_args()
    text = SRC.read_text()
    lines, total = [], 0
    for sec in re.split(r"\n## ", text)[1:]:
        m = re.search(r"\(folder `art/source/(\w+)/`\)", sec)
        if not m:
            continue
        style = m.group(1)
        opener = re.search(r"\*\*Opener\*\*\n```\n(.*?)\n```", sec, re.S).group(1)
        st = style_text(opener)
        for name, prompt in re.findall(r"`(\w+)\.png`\n```\n(.*?)\n```", sec, re.S):
            if name.endswith("_v2"):
                continue  # edits of a layout guide: tools/generate_retro_v2.py, not a batch
            size = next(v for k, v in SIZES.items() if prompt.startswith(k))
            n = a.variants if name in KEY else 1
            full = f"{st}\n\n{prompt}"
            if a.endpoint == "images":
                body = {"model": a.model or BATCH_IMAGE_MODEL, "prompt": full, "size": size, "quality": a.quality, "n": n}
                lines.append({"custom_id": f"{style}__{name}", "method": "POST", "url": "/v1/images/generations", "body": body})
            else:
                # The Responses API has no n: one request per variant.
                for k in range(n):
                    body = {"model": a.model or "gpt-4.1-mini",
                            "input": "Generate exactly one image from this description. Do not reply with text.\n\n" + full,
                            "tools": [{"type": "image_generation", "model": BATCH_IMAGE_MODEL, "size": size, "quality": a.quality}],
                            "tool_choice": {"type": "image_generation"}}
                    cid = f"{style}__{name}" + (f"__{k + 1}" if k else "")
                    lines.append({"custom_id": cid, "method": "POST", "url": "/v1/responses", "body": body})
            total += n
    OUT = ROOT / "art" / ("image_batch.jsonl" if a.endpoint == "images" else "image_batch_responses.jsonl")
    OUT.write_text("".join(json.dumps(x) + "\n" for x in lines))
    print(f"wrote {OUT.relative_to(ROOT)}: {len(lines)} requests, {total} images")


if __name__ == "__main__":
    main()
