"""Engine rule tests.  Run:  python3 harness/tests/test_engine.py"""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))

from arms import get_arm  # noqa: E402
from chargen import from_templates, personalities_for_run  # noqa: E402
from engine import Engine  # noqa: E402
from run import PLACEBO, WORLD, build_prep  # noqa: E402


def make(arm="A", seed=7, **kw) -> Engine:
    chars = from_templates(seed)
    for c, p in zip(chars, personalities_for_run(0)):
        c["personality"] = p
    e = Engine(arm=get_arm(arm), characters=chars, prep=build_prep(seed), world=WORLD, placebo=PLACEBO,
               seed=seed, **kw)
    e.start_session()
    e.start_scene()
    return e


def first_pid(e):
    return e.order[0]


class DeckTests(unittest.TestCase):
    def test_deck_is_3_gm_plus_1_per_player(self):
        e = make()
        self.assertEqual(len(e.deck), 7)
        self.assertEqual(len(e.deck_player_cards), 4)
        self.assertEqual(sum(1 for c in e.deck if e.cards[c].owner == "GM"), 3)

    def test_card_in_deck_not_live(self):
        e = make()
        cid, pid = next(iter(e.deck_player_cards.items()))
        self.assertFalse(any(o["source_id"] == cid for o in e.invokable_for(pid)))

    def test_cannot_draw_at_will(self):
        e = make()
        n = len(e.deck)
        self.assertIsNone(e.draw("gm_wants_one", actor="GM"))
        self.assertEqual(len(e.deck), n)
        self.assertTrue(any("non-trigger" in v["issue"] for v in e.violations))

    def test_guarantee_pulls_unsurfaced_player_cards_at_two(self):
        e = make()
        # Put two player cards at the bottom, then draw down to 2.
        players = list(e.deck_player_cards)
        e.deck = [c for c in e.deck if c not in players[:2]] + players[:2]
        while len(e.deck) > 2:
            cid = e.draw("tie")
            if e.is_player_deck_card(cid):
                e.surface(cid)
        self.assertEqual(sorted(e.guarantee_pulled), sorted(players[:2]))
        beat = e.next_beat_for_scene()
        self.assertTrue(beat["guarantee"])
        self.assertEqual(sorted(beat["cards"]), sorted(players[:2]))

    def test_exhaustion_makes_next_scene_climax_and_last(self):
        e = make()
        while e.deck:
            e.draw("tie")
        self.assertEqual(e.climax_scene, e.scene + 1)
        e.end_scene({})
        self.assertFalse(e.session_over)
        info = e.start_scene()
        self.assertTrue(info["is_climax"])
        e.end_scene({})
        self.assertTrue(e.session_over)


class CompelTests(unittest.TestCase):
    def test_surface_compel_accept(self):
        e = make()
        cid, pid = next(iter(e.deck_player_cards.items()))
        fp = e.chars[pid].fp
        e.resolve_compel(pid, True, card_id=cid, tag=e.cards[cid].weakness, from_deck=True, text="x")
        e.surface(cid)
        self.assertEqual(e.chars[pid].fp, fp + 1)
        self.assertIn(cid, e.rail)
        self.assertEqual(e.free_invokes.get((pid, cid)), 1)
        self.assertTrue(any(o["source_id"] == cid for o in e.invokable_for(pid)))

    def test_refuse_with_zero_fp_is_forced_accept(self):
        e = make()
        pid = first_pid(e)
        e.chars[pid].fp = 0
        r = e.resolve_compel(pid, False, card_id=None, tag="t", from_deck=False, text="x")
        self.assertTrue(r["accepted"] and r["forced"])
        self.assertEqual(e.chars[pid].fp, 1)

    def test_refuse_costs_one(self):
        e = make()
        pid = first_pid(e)
        fp = e.chars[pid].fp
        e.resolve_compel(pid, False, card_id=None, tag="t", from_deck=False, text="x")
        self.assertEqual(e.chars[pid].fp, fp - 1)


class RollTests(unittest.TestCase):
    def test_passive_opposition_caps_at_great(self):
        e = make()
        pid = first_pid(e)
        tags = [{"card_id": c, "tag": t} for c, t in e.rail_gm_tags()]
        self.assertGreaterEqual(len(tags), 4)
        ctx = e.begin_roll(pid, action="overcome", skill="Notice", target_card=None, target_npc=None,
                           opp={"opposing_tags": tags})
        self.assertEqual(ctx.opposition, 4)

    def test_tag_for_difficulty_cannot_be_invoked(self):
        e = make()
        pid = first_pid(e)
        c, t = e.rail_gm_tags()[0]
        ctx = e.begin_roll(pid, action="overcome", skill="Notice", target_card=None, target_npc=None,
                           opp={"opposing_tags": [{"card_id": c, "tag": t}], "gm_invokes": [{"card_id": c, "tag": t}]})
        self.assertEqual(ctx.gm_bonus, 0)
        self.assertTrue(any("difficulty also invoked" in v["issue"] for v in e.violations))

    def test_each_tag_once_per_roll_and_fp_paid(self):
        e = make()
        pid = first_pid(e)
        opt = e.invokable_for(pid)[0]
        fp = e.chars[pid].fp
        ctx = e.begin_roll(pid, action="overcome", skill="Notice", target_card=None, target_npc=None, opp={})
        e.apply_player_invokes(ctx, [{"source_id": opt["source_id"], "tag": opt["tag"]}] * 2)
        self.assertEqual(ctx.bonus, 2)
        self.assertEqual(e.chars[pid].fp, fp - 1)

    def test_tie_draws_and_fail_does_not(self):
        e = make()
        pid = first_pid(e)
        for _ in range(60):
            ctx = e.begin_roll(pid, action="overcome", skill="Notice", target_card=None, target_npc=None, opp={})
            n, d = len(e.deck), e.draws_this_session
            res = e.finalize_roll(ctx, take_major_cost=False)
            if res["outcome"] == "tie" and n:
                self.assertEqual(e.draws_this_session, d + 1)
            if res["outcome"] in ("fail", "success", "success_with_style"):
                self.assertEqual((len(e.deck), e.draws_this_session), (n, d))

    def test_common_random_numbers_across_arms(self):
        a, b = make("A", seed=3), make("B", seed=3)
        self.assertEqual([a.roll4df() for _ in range(20)], [b.roll4df() for _ in range(20)])


class ClockRailTensionTests(unittest.TestCase):
    def test_failed_roll_against_card_marks_clock_and_fill_queues_beat(self):
        e = make()
        pid = first_pid(e)
        gm = next(c for c in e.rail if e.cards[c].owner == "GM" and e.cards[c].track_kind == "clock")
        e.cards[gm].marks = e.cards[gm].track_size - 1
        e.chars[pid].skills = {"Notice": -4}
        tag = e.cards[gm].tags()[0]
        for _ in range(10):
            if gm not in e.rail:
                break
            ctx = e.begin_roll(pid, action="overcome", skill="Notice", target_card=gm, target_npc=None,
                               opp={"opposing_tags": [{"card_id": gm, "tag": tag}]})
            e.finalize_roll(ctx, take_major_cost=False)
        self.assertNotIn(gm, e.rail)
        self.assertTrue(any(b.get("clock_card") == gm for b in e.queued_beats))

    def test_rail_limit_evicts_oldest_non_global_gm(self):
        e = make()
        extra = [c["id"] for c in WORLD["cards"] if c["owner"] == "GM" and c["id"] not in e.rail][:5]
        for c in extra:
            e.place_on_rail(c, reason="test")
        self.assertLessEqual(len(e.rail), 5)
        self.assertTrue(any(e.cards[c].owner == "GLOBAL" for c in e.rail))

    def test_tension_rows_sum_and_clamp(self):
        e = make()
        e.tension = 6
        threat = next(c["id"] for c in WORLD["cards"] if c["type"] == "THREAT")
        e.appeared_this_session.add(threat)
        e.scene_flags["clock_advanced"] = True
        e.end_scene({"fled_or_bypassed": [threat]})
        self.assertEqual(e.tension, 6)


class BeatTests(unittest.TestCase):
    def test_type_mismatch_fills_first_empty_open_blank(self):
        e = make()
        frame = next(b for b in WORLD["beat_frames"] if b["open"] == ["WHO", "WHY"])
        loc = next(c["id"] for c in WORLD["cards"] if c["type"] == "LOCATION")
        e.deck.insert(0, loc)
        out = e.fill_beat(copy.deepcopy(frame))
        self.assertEqual(out["fills"]["WHO"], loc)   # LOCATION wants WHERE, not open -> first empty

    def test_empty_deck_uses_defaults(self):
        e = make()
        e.deck = []
        out = e.fill_beat(copy.deepcopy(WORLD["beat_frames"][0]))
        self.assertTrue(all(v is None for v in out["fills"].values()))


class HarmGrowthTests(unittest.TestCase):
    def test_absorb_options_and_taken_out(self):
        e = make()
        pid = first_pid(e)
        opts = e.absorb_options(pid, "physical", 2)
        self.assertEqual(opts[0], {"box": 2, "consequences": []})
        self.assertEqual(e.absorb_options(pid, "physical", 20), [])

    def test_growth_capped_at_two_per_session(self):
        e = make()
        pid = first_pid(e)
        cid = e.chars[pid].binder[0]
        for _ in range(4):
            e.growth_ledger.append({"card": cid, "why": "compel accepted", "scene": 1})
        e.post_session({"summary": "", "threats_left_play": []})
        self.assertEqual(e.cards[cid].growth, 2)


class ArmTests(unittest.TestCase):
    def test_placebo_never_revealed(self):
        e = make("C")
        for cid in e.deck:
            self.assertNotIn("PLACEBO", json.dumps(e.cards[cid].brief()))
        for pid in e.order:
            for cid in e.chars[pid].story_pile:
                self.assertNotIn("PLACEBO", json.dumps(e.cards[cid].brief()))

    def test_placebo_surfacing_returns_setaside_card(self):
        e = make("C")
        cid, pid = next(iter(e.deck_player_cards.items()))
        orig = e.setaside[pid]
        self.assertEqual(e.chars[pid].card_state[orig], "setaside")
        e.surface(cid)
        self.assertEqual(e.chars[pid].card_state[orig], "binder")

    def test_arm_b_has_no_deck_and_improvises_costs(self):
        e = make("B")
        self.assertEqual(e.deck, [])
        pid = first_pid(e)
        for _ in range(40):
            ctx = e.begin_roll(pid, action="overcome", skill="Notice", target_card=None, target_npc=None, opp={})
            res = e.finalize_roll(ctx, take_major_cost=True)
            if res["outcome"] in ("tie", "success_major_cost"):
                self.assertEqual(res["cost_mode"], "improvised")
                self.assertIsNone(res["drawn"])


if __name__ == "__main__":
    unittest.main()
