#!/usr/bin/env python3
"""Run one sim request (Prompts Part 3.4) and write its report (Part 3.5)."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.batch import run_batch
from engine.kits import load_roster
from engine.report import summarise, to_markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("request")
    ap.add_argument("--workers", type=int, default=0)
    ap.add_argument("--tests", action="store_true", help="run pytest and record the result")
    ap.add_argument("--baseline", default=None)
    ap.add_argument("--dump-raw", action="store_true",
                    help="write per-game results to reports/raw/<batch>.jsonl.gz")
    ap.add_argument("--no-checkpoint", action="store_true",
                    help="do not write or resume from reports/raw/<batch>.partial.jsonl")
    args = ap.parse_args()

    with open(args.request) as fh:
        spec = json.load(fh)
    spec.setdefault("roster_path", os.path.join(ROOT, "roster", f"roster_v{spec['roster']}.json"))
    spec["p1"] = spec["matchup"]["p1"]
    spec["p2"] = spec["matchup"]["p2"]
    spec["temperature"] = spec["matchup"].get("temperature", 0.3)
    if spec["matchup"].get("personality_pool"):
        spec["personality_pool"] = spec["matchup"]["personality_pool"]
    kits = load_roster(spec["roster_path"])
    spec["costs"] = {cid: {k: v.get("cost", 0) for k, v in kit["abilities"].items()}
                     for cid, kit in kits.items()}

    tests = {}
    if args.tests:
        t = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-q"],
                           cwd=ROOT, capture_output=True, text=True)
        tests = {"summary": t.stdout.strip().splitlines()[-1] if t.stdout else "no output",
                 "returncode": t.returncode}

    checkpoint = None
    if not args.no_checkpoint:
        os.makedirs(os.path.join(ROOT, "reports", "raw"), exist_ok=True)
        checkpoint = os.path.join(ROOT, "reports", "raw", f"{spec['batch_id']}.partial.jsonl")
    t0 = time.time()
    results = run_batch(spec, workers=args.workers, checkpoint=checkpoint)
    spec["runtime_s"] = time.time() - t0
    if spec.get("resumed_games"):
        print(f"{spec['batch_id']}: resumed with {spec['resumed_games']} games from {checkpoint}; "
              f"runtime covers the remainder only")

    baseline = None
    if args.baseline and os.path.exists(args.baseline):
        with open(args.baseline) as fh:
            baseline = json.load(fh)
    summary = summarise(results, spec, tests, baseline)

    out_json = os.path.join(ROOT, "reports", f"{spec['batch_id']}.json")
    out_md = os.path.join(ROOT, "reports", f"{spec['batch_id']}.md")
    with open(out_json, "w") as fh:
        json.dump(summary, fh, indent=2)
    with open(out_md, "w") as fh:
        fh.write(to_markdown(summary))
    if args.dump_raw:
        import gzip
        os.makedirs(os.path.join(ROOT, "reports", "raw"), exist_ok=True)
        raw_path = os.path.join(ROOT, "reports", "raw", f"{spec['batch_id']}.jsonl.gz")
        with gzip.open(raw_path, "wt") as fh:
            for r in results:
                fh.write(json.dumps({k: v for k, v in r.items() if k != "replay"}) + "\n")

    replays = [r for r in results if r.get("replay")]
    if replays:
        with open(os.path.join(ROOT, "reports", f"{spec['batch_id']}_replays.json"), "w") as fh:
            json.dump([{"game": r["game_index"], "winner": r["winner"], "rounds": r["rounds"],
                        "picks": r["picks"], "events": r["replay"]} for r in replays], fh, indent=2)
    if checkpoint and os.path.exists(checkpoint):
        os.remove(checkpoint)
    print(f"{spec['batch_id']}: {len(results)} games in {spec['runtime_s']:.1f}s -> {out_md}")
    for c in summary["scorecard"]:
        print(f"  [{c['verdict']:<13}] {c['check']}: {c['value']}")


if __name__ == "__main__":
    main()
