"""The batch runner's checkpoint: a killed run resumes, it does not restart."""
import json
import os

from engine.batch import run_batch
from tests.conftest import ROSTER


def _spec(n):
    return {"batch_id": "t", "seed": 3, "games": n, "roster_path": ROSTER, "ai": "1.3.0",
            "p1": "T0_random", "p2": "T0_random", "temperature": 0.3, "replays": 0,
            "config_overrides": {"round_limit": 2}}


def test_checkpoint_resumes_without_replaying(tmp_path):
    ck = str(tmp_path / "partial.jsonl")
    first = run_batch(_spec(2), workers=1, checkpoint=ck)
    assert len(first) == 2 and len(open(ck).read().splitlines()) == 2
    second = run_batch(_spec(3), workers=1, checkpoint=ck)
    lines = [json.loads(l) for l in open(ck).read().splitlines()]
    assert len(second) == 3 and [r["game_index"] for r in lines] == [0, 1, 2]
    assert [r["game_index"] for r in second] == [0, 1, 2]
    assert second[0]["winner"] == first[0]["winner"] and second[0]["rounds"] == first[0]["rounds"]


def test_no_checkpoint_still_runs():
    assert len(run_batch(_spec(2), workers=1)) == 2


def test_anchor_share_puts_an_anchor_in_one_seat():
    from engine.batch import play_one
    spec = dict(_spec(40), personality_pool=["T1_greedy", "T0_random"], anchors=["T2_search"],
                anchor_share=1.0, config_overrides={"round_limit": 1},
                p1_config={"time_budget_ms": 20}, p2_config={"time_budget_ms": 20})
    for i in range(4):
        r = play_one((i, spec))
        tiers = sorted(r["tiers"].values())
        assert "T2_search" in tiers and len([t for t in tiers if t != "T2_search"]) == 1
    # the two seats of a swapped pair see the same draw
    a, b = play_one((0, spec)), play_one((1, spec))
    assert a["tiers"]["north"] == b["tiers"]["south"] and a["tiers"]["south"] == b["tiers"]["north"]
