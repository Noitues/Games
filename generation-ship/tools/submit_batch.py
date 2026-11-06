"""Submit, check and collect OpenAI Batch API jobs (standard library only).

    python3 tools/submit_batch.py submit art/retro_batch2_edits.jsonl   -> uploads, creates the batch
    python3 tools/submit_batch.py status                                -> every batch in art/batches.json
    python3 tools/submit_batch.py collect                               -> downloads finished outputs and
                                                                           decodes them (decode_image_batch.py)

Batch ids are kept in art/batches.json. On your own computer set OPENAI_API_KEY; in a Claude cloud
session with an OpenAI network secret the proxy adds it.
"""
import json
import os
import sys
import urllib.request
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decode_image_batch  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.openai.com/v1"
LOG = ROOT / "art" / "batches.json"


def call(method, path, body=None, ctype="application/json", raw=False):
    headers = {"Content-Type": ctype} if body is not None else {}
    if os.environ.get("OPENAI_API_KEY"):
        headers["Authorization"] = f"Bearer {os.environ['OPENAI_API_KEY']}"
    if body is not None and ctype == "application/json":
        body = json.dumps(body).encode()
    with urllib.request.urlopen(urllib.request.Request(API + path, data=body, headers=headers, method=method), timeout=600) as r:
        data = r.read()
    return data if raw else json.loads(data)


def log():
    return json.loads(LOG.read_text()) if LOG.exists() else []


def submit(path):
    path = Path(path).resolve()
    first = json.loads(path.read_text().splitlines()[0])
    b = uuid.uuid4().hex
    body = (f'--{b}\r\nContent-Disposition: form-data; name="purpose"\r\n\r\nbatch\r\n'
            f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="{path.name}"\r\n'
            f"Content-Type: application/jsonl\r\n\r\n").encode() + path.read_bytes() + f"\r\n--{b}--\r\n".encode()
    f = call("POST", "/files", body, f"multipart/form-data; boundary={b}")
    batch = call("POST", "/batches", {"input_file_id": f["id"], "endpoint": first["url"], "completion_window": "24h"})
    entries = log() + [{"id": batch["id"], "input": str(path.relative_to(ROOT)), "status": batch["status"]}]
    LOG.write_text(json.dumps(entries, indent=1) + "\n")
    print("submitted", batch["id"], batch["status"], "for", path.name)


def status(collect=False):
    entries = log()
    for e in entries:
        b = call("GET", f"/batches/{e['id']}")
        e["status"] = b["status"]
        c = b.get("request_counts", {})
        print(f"{e['id']}  {e['input']}  {b['status']}  {c.get('completed', 0)}/{c.get('total', 0)} done, {c.get('failed', 0)} failed")
        if collect and b["status"] == "completed" and not e.get("collected"):
            for key in ("output_file_id", "error_file_id"):
                if b.get(key):
                    out = ROOT / "art" / f"{e['id']}_{key.split('_')[0]}.jsonl"
                    out.write_bytes(call("GET", f"/files/{b[key]}/content", raw=True))
                    decode_image_batch.main(out)
                    out.unlink()  # the images are saved; the base64 dump is not worth committing
            e["collected"] = True
    LOG.write_text(json.dumps(entries, indent=1) + "\n")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "submit":
        submit(sys.argv[2])
    else:
        status(collect=cmd == "collect")
