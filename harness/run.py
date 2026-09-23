"""Run one session end-to-end and write one run JSON.

    python run.py --arm A --seed 11 --run-index 0 --batch-id smoke --backend scripted

The orchestrator owns the loop: engine state changes happen only in engine.py, and every agent is
asked for exactly one structured decision at a time.
"""

from __future__ import annotations

import argparse
import copy
import json
import random
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import scripted as scripted_mod
from agents import (ANALYST_SYSTEM, INTERVIEWER_SYSTEM, PERSONALITIES, Agent, DiceClaimError, gm_system, j,
                    player_system, referee_system, render_transcript)
from arms import get_arm
from chargen import cohort_index_for_run, generate_cohort, personalities_for_run
from engine import (GM_TYPES, LADDER, PLAYER_TYPES, ROLL_ACTIONS, SPEC_VERSION, Engine, InvalidRun, derive_seed,
                    fmt_dice, ladder)
from llm import AgentFailure, BudgetExceeded, LLMClient, TokenMeter

HERE = Path(__file__).parent
ROOT = HERE.parent
WORLD = json.loads((HERE / "data" / "world.json").read_text())
PLACEBO = json.loads((HERE / "data" / "placebo.json").read_text())
MAX_ROUNDS = 3
DEFENSE_SKILL = {"physical": "Athletics", "mental": "Will"}


# ====================================================================== prep packet
def build_prep(seed: int) -> dict:
    """Same packet for every arm of a seed (§7 pre-session prep)."""
    rng = random.Random(derive_seed(seed, "prep"))
    cards = WORLD["cards"]
    by = lambda owner, types: sorted(c["id"] for c in cards if c["owner"] == owner and c["type"] in types)
    glob = rng.choice(by("GLOBAL", {"HAZARD"}))
    anchor_gm = rng.choice(by("GM", {"THREAT", "FACTION", "LOCATION"}))
    pool = [c for c in by("GM", GM_TYPES) if c != anchor_gm]
    rng.shuffle(pool)
    environment = pool[:3]
    rest = pool[3:]
    threats = [c for c in rest if c.startswith(("T-", "F-"))]
    trigger_menu = [f"roll_fails_against:{anchor_gm}", "scene_start:3", "tension_at_least:4",
                    "compel_refused", "deck_at_most:3", f"clock_fills:{anchor_gm}",
                    "fiction:the party leaves the road or causeway", "fiction:the party enters a settlement"]
    rng.shuffle(trigger_menu)
    modules = []
    for i in range(2):
        a = rest.pop(0)
        b = next((t for t in threats if t not in (a,) and t in rest), rest[0])
        rest.remove(b)
        modules.append({"id": f"M-{i+1}", "cards": [a, b], "trigger": trigger_menu.pop()})
    frames = copy.deepcopy(rng.sample(WORLD["beat_frames"], 3))
    for f in frames:
        f["trigger"] = trigger_menu.pop()
    return {"anchors": [glob, anchor_gm], "environment": environment, "modules": modules,
            "beat_frames": frames}


def prep_text(prep: dict) -> str:
    card = {c["id"]: c for c in WORLD["cards"]}

    def show(cid):
        c = card[cid]
        clock = f", clock {c['track']['size']}" if c["track"]["kind"] == "clock" else ""
        return (f"  {cid} {c['type']} '{c['title']}' ({c['owner']}{clock}) — tags: {', '.join(c['power_tags'])}; "
                f"weakness: {c['weakness']}. {c.get('blurb', '')}")
    lines = ["Anchors (start face-up):"] + [show(c) for c in prep["anchors"]]
    lines += ["Environment cards (in the Session Deck):"] + [show(c) for c in prep["environment"]]
    lines += ["Backup modules:"]
    for m in prep["modules"]:
        lines += [f" {m['id']} WHEN {m['trigger']} THEN deploy:"] + [show(c) for c in m["cards"]]
    lines += ["Beat Frames:"]
    for b in prep["beat_frames"]:
        lines.append(f" {b['id']} {b['name']} WHEN {b['trigger']}: \"{b['sentence']}\" open blanks {b['open']}; "
                     f"defaults {b['defaults']}; stakes: {b['stakes']}"
                     + (f" (stakes clock {b['stakes_clock']})" if b.get("stakes_clock") else ""))
    return "\n".join(lines)


def prep_text_B(prep: dict) -> str:
    """Arm B sees the same prep, minus the deck mechanics: environment cards are just more ideas."""
    card = {c["id"]: c for c in WORLD["cards"]}
    show = lambda cid: (f"  {cid} '{card[cid]['title']}' — {', '.join(card[cid]['power_tags'])}; "
                        f"weakness: {card[cid]['weakness']}. {card[cid].get('blurb', '')}")
    lines = ["Situation aspects on the table at the start:"] + [show(c) for c in prep["anchors"]]
    lines += ["Other elements you may bring in when the story calls for them:"]
    lines += [show(c) for c in prep["environment"] + [x for m in prep["modules"] for x in m["cards"]]]
    lines += ["Story ideas you may use:"]
    for b in prep["beat_frames"]:
        lines.append(f"  {b['name']}: {b['sentence'].format(**b['defaults'])} Stakes: {b['stakes']}")
    return "\n".join(lines)


# ====================================================================== the session
class Session:
    def __init__(self, *, arm_key: str, seed: int, run_index: int, batch_id: str, backend: str,
                 out_dir: Path, cache_dir: Path | None, token_cap: int | None, batch_meter=None,
                 models: dict | None = None, max_scenes: int = 5, tension: int = 3,
                 cohort_id: str | None = None, parallel_players: bool = True):
        self.arm = get_arm(arm_key)
        self.arm_key = arm_key
        self.seed = seed
        self.run_index = run_index
        self.batch_id = batch_id
        self.backend = backend
        self.run_id = f"{batch_id}__{arm_key}__s{seed}__r{run_index}"
        self.out_path = out_dir / f"{self.run_id}.json"
        self.meter = TokenMeter(token_cap)
        self.parallel = parallel_players
        self.notes: list[dict] = []
        self.cost_records: list[dict] = []
        self.referee = {"violations": [], "ambiguities": [], "cost_checks": [], "friction": []}
        self.addressed: set[str] = set()
        self.turns: dict[str, int] = {}
        self.scenes: list[dict] = []
        self.started = time.time()
        self.scripted = scripted_mod.Scripted(seed=seed, run_id=self.run_id)
        self.client = LLMClient(backend, cache_dir=cache_dir / self.run_id if cache_dir else None,
                                run_id=self.run_id, run_meter=self.meter, batch_meter=batch_meter,
                                models=models, scripted=self.scripted)
        cidx = cohort_index_for_run(run_index)
        self.cohort_id = cohort_id or f"{batch_id}-cohort{cidx:02d}"
        cohort_seed = derive_seed(0, f"cohort:{self.cohort_id}") % 10**6   # same for every run of the cohort
        self.cohort = generate_cohort(self.cohort_id, cohort_seed, backend=backend, client=self.client,
                                      world=WORLD)
        self.personalities = personalities_for_run(run_index)
        chars = copy.deepcopy(self.cohort["characters"])
        for ch, p in zip(chars, self.personalities):
            ch["personality"] = p
        self.characters = chars
        self.prep = build_prep(seed)
        self.engine = Engine(arm=self.arm, characters=chars, prep=self.prep, world=WORLD, placebo=PLACEBO,
                             seed=seed, tension=tension, max_scenes=max_scenes)
        e = self.engine
        ptext = prep_text(self.prep) if self.arm["deck"] else prep_text_B(self.prep)
        self.gm = Agent(self.client, "gm", "GM", gm_system(self.arm, WORLD, ptext), on_note=self._note)
        self.players = {pid: Agent(self.client, "player", e.chars[pid].name,
                                   player_system(ch, ch["personality"], self.arm, WORLD["name"]),
                                   on_note=self._note)
                        for pid, ch in zip(e.order, chars)}
        self.ref_agent = Agent(self.client, "referee", "Referee", referee_system(self.arm), on_note=self._note)
        self.interviewer = Agent(self.client, "interviewer", "Interviewer", INTERVIEWER_SYSTEM)

    # ------------------------------------------------------------------ helpers
    def _note(self, kind, agent, call_kind, detail):
        self.notes.append({"kind": kind, "agent": agent, "call": call_kind, "detail": detail,
                           "scene": self.engine.scene})

    def _pmap(self, fn, items):
        if self.parallel and len(items) > 1:
            with ThreadPoolExecutor(max_workers=len(items)) as ex:
                return list(ex.map(fn, items))
        return [fn(x) for x in items]

    def p_prompt(self, pid: str, task: str, extra: dict | None = None) -> str:
        e = self.engine
        parts = [f"== Your character sheet ==\n{j(e.player_sheet(pid))}",
                 f"== At the table now ==\n{j(e.public_state())}",
                 f"== The story so far ==\n{render_transcript(e.transcript, pid)}"]
        if extra:
            parts.append(f"== Details ==\n{j(extra)}")
        if e.chars[pid].name in self.addressed:
            parts.append("(The GM just spoke to your character directly.)")
        parts.append(f"== What you need to decide ==\n{task}")
        return "\n\n".join(parts)

    def gm_prompt(self, task: str, extra: dict | None = None) -> str:
        e = self.engine
        parts = [f"== Table state ==\n{j(e.gm_state())}",
                 f"== The story so far ==\n{render_transcript(e.transcript, None, 20000)}"]
        if extra:
            parts.append(f"== Details ==\n{j(extra)}")
        parts.append(f"== Your decision ==\n{task}")
        return "\n\n".join(parts)

    def base_ctx(self, pid: str | None = None, **kw) -> dict:
        e = self.engine
        ctx = {"arm": self.arm, "engine": e, "pid": pid, "addressed": self.addressed}
        ctx.update(kw)
        return ctx

    def mech(self, text: str) -> None:
        self.engine.say("Table", text, kind="mechanics")

    # ------------------------------------------------------------------ run
    def run(self) -> dict:
        e = self.engine
        status, error = "complete", None
        try:
            e.start_session()
            self.mech("Session begins. Each player has " + ", ".join(f"{c.name} {c.fp} FP" for c in e.chars.values())
                      + ". Face-up: " + ", ".join(f"{e.cards[c].title} [{c}]" for c in e.rail) + ".")
            while not e.session_over:
                self.play_scene()
                self.write(status="partial")
            self.post_session()
            self.run_surveys()
        except DiceClaimError as ex:
            status, error = "invalid", f"dice claim: {ex}"
        except InvalidRun as ex:
            status, error = "invalid", str(ex)
        except BudgetExceeded as ex:
            status, error = "truncated", str(ex)
        except AgentFailure as ex:
            status, error = "failed", str(ex)
        except Exception as ex:   # harness bug: keep the traceback in the record
            status, error = "crashed", traceback.format_exc()
        return self.write(status=status, error=error)

    # ------------------------------------------------------------------ scenes
    def play_scene(self) -> None:
        e = self.engine
        info = e.start_scene()
        rec = {"index": e.scene, "tension_before": e.tension if self.arm["tension"] else None,
               "scene_test": None, "outcome": "", "beat": None, "rounds": 0, "climax": info["is_climax"]}
        self.addressed = set()
        if self.arm["deck"]:
            e.final_scene_guarantee()   # spec 0.2.0 §4
        beat = e.next_beat_for_scene() if self.arm["beat_frames"] else None
        plan = self.gm.ask("gm_frame", self.gm_prompt(
            "Plan the next scene: state it and frame it assuming it plays as planned."
            + (" This is the session's CLIMAX: the deck is empty; ties and costs use face-up GM tags."
               if info["is_climax"] else "")
            + ("" if e.scene > 1 else " This is the first scene of the session.")),
            self.base_ctx(call="plan"))
        framing = plan
        if beat:
            rec["outcome"] = "beat_frame"
            rec["beat"] = beat["reason"]
            framing = self.run_beat(beat, plan)
        else:
            test = e.scene_test()
            rec["scene_test"] = test["roll"]
            rec["outcome"] = test["result"]
            if test["result"] == "altered":
                framing = self.altered_scene(plan)
            elif test["result"] == "interrupt":
                frame = e.pick_frame(None)
                framing = self.run_beat({"reason": "interrupt", "frame_id": frame["id"], "guarantee": False},
                                        plan)
                rec["beat"] = "interrupt"
        self.apply_framing(framing)
        for rnd in range(1, MAX_ROUNDS + 1):
            rec["rounds"] = rnd
            over, report = self.play_round(rnd, final=(rnd == MAX_ROUNDS))
            if over:
                break
        cleanup = e.end_scene(report or {})
        rec["tension_after"] = e.tension if self.arm["tension"] else None
        rec["triggers_fired"] = cleanup["triggers_fired"]
        self.scenes.append(rec)
        self.referee_scene()

    def apply_framing(self, fr: dict) -> None:
        e = self.engine
        e.say("GM", fr.get("narration", ""))
        e.log(event_type="frame", actor="GM", action="Frame scene", notes=fr.get("central_question", "")[:200])
        for n in fr.get("npcs", [])[:6]:
            e.add_npc(n.get("name", "Someone"), n.get("rating", 2), n.get("stress", 2), n.get("hostile", True),
                      n.get("card_id") or None)
        self.addressed = set(fr.get("address", []))
        self.central_question = fr.get("central_question", "")

    def altered_scene(self, plan: dict) -> dict:
        e = self.engine
        cid = e.draw("altered_scene", actor="engine")
        extra = {"planned_scene": plan.get("planned_scene"), "scene_test": "ALTERED"}
        if cid is None:
            e.fire("AMB-16", "altered scene with empty deck")
            extra["instruction"] = "The deck is empty: change one element using a face-up GM card's tag."
        elif e.is_player_deck_card(cid):
            self.player_card_compel(cid, reason="altered scene")
            extra["drawn_card"] = e.cards[cid].brief()
        else:
            e.place_drawn_gm_card(cid)
            extra["drawn_card"] = e.cards[cid].brief()
        fr = self.gm.ask("gm_frame", self.gm_prompt(
            "The scene test came up ALTERED. Use one tag of the drawn card to change one element of the planned "
            "scene (who is there, the location, or the weather) and reframe it. Put the card and tag in used_card.",
            extra), self.base_ctx(call="altered", drawn=cid))
        uc = fr.get("used_card") or {}
        valid = bool(uc) and ((cid and uc.get("card_id") == cid and uc.get("tag") in e.cards[cid].tags())
                              or (cid is None and (uc.get("card_id"), uc.get("tag")) in e.rail_gm_tags()))
        self.cost_records.append({"event": "altered", "scene": e.scene, "draw_id": cid or "", "valid": valid,
                                  "tag": uc.get("tag", ""), "text": fr.get("narration", "")[:300],
                                  "improvised": cid is None})
        if not valid:
            e.violation("GM", "§6", f"altered scene did not use a tag of the drawn card ({cid}): {uc}")
        return fr

    def player_card_compel(self, cid: str, reason: str, question: dict | None = None,
                           offer: dict | None = None) -> dict:
        """§4 'Resolving a drawn player card' — compel, then surface."""
        e = self.engine
        pid = e.deck_player_cards[cid]
        card = e.cards[cid]
        if offer is None:
            out = self.gm.ask("gm_costs", self.gm_prompt(
                f"You drew {e.name(pid)}'s card for {reason}. Write the compel you offer them (weakness tag by "
                "default) in one item; refusal_cost must use a face-up GM tag.",
                {"drawn_card": card.brief(), "owner": e.name(pid), "event_id": 0}),
                self.base_ctx(call="compel_offer", items=[{"event_id": 0, "card_id": cid, "mode": "player_card_compel"}]))
            items = out.get("items") or [{}]
            offer = {"tag_used": items[0].get("tag_used", card.weakness), "complication": items[0].get("text", ""),
                     "refusal_cost": items[0].get("refusal_cost") or {}}
        tag = offer.get("tag_used") or card.weakness
        tag_ok = tag in card.tags()
        if not tag_ok:
            e.violation("GM", "§4", f"compel on {cid} used tag not on the card: {tag!r}")
        task = (f"The GM reveals one of your cards and offers a compel: \"{offer.get('complication', '')}\" "
                f"(on '{tag}'). Accept (gain 1 fate point, it happens) or refuse (pay 1 fate point)?")
        if question:
            task = f"The GM asks you: \"{question.get('question', '')}\" Your answer becomes true; put it in 'answer'.\n" + task
        ans = self.players[pid].ask("player_compel", self.p_prompt(pid, task, {"card": card.brief()}),
                                    self.base_ctx(pid, call="compel", from_deck=True, question=bool(question)))
        if question and ans.get("answer"):
            e.say(e.name(pid), ans["answer"], kind="speech")
        res = e.resolve_compel(pid, bool(ans.get("accept", True)), card_id=cid if card.origin == "player" else None,
                               tag=tag, from_deck=True, text=offer.get("complication", ""))
        if ans.get("speech"):
            e.say(e.name(pid), ans["speech"], kind="speech")
        refusal_valid = None
        if not res["accepted"]:
            rc = offer.get("refusal_cost") or {}
            refusal_valid = (rc.get("card_id"), rc.get("tag")) in e.rail_gm_tags()
            if not refusal_valid:
                e.violation("GM", "§4", f"refusal cost not built from a face-up GM tag: {rc}")
        self.cost_records.append({"event": f"compel:{reason}", "scene": e.scene, "draw_id": cid, "valid": tag_ok,
                                  "tag": tag, "text": offer.get("complication", "")[:300], "improvised": False,
                                  "accepted": res["accepted"], "refusal_valid": refusal_valid,
                                  "owner": e.name(pid), "placebo": card.origin == "placebo"})
        self.mech(f"{e.name(pid)} {'accepts' if res['accepted'] else 'refuses'} the compel on '{card.title}'.")
        e.surface(cid)
        return {"accepted": res["accepted"], "answer": ans.get("answer", ""), "offer": offer}

    def run_beat(self, beat: dict, plan: dict) -> dict:
        e = self.engine
        frame = e.pick_frame(beat.get("frame_id"))
        pulled = beat.get("cards") if beat.get("guarantee") else None
        filled = e.fill_beat(frame, pulled=pulled)
        self.engine.scene_flags["beat"] = frame
        for cid in filled["cards"]:
            if not e.is_player_deck_card(cid):
                e.place_drawn_gm_card(cid)
        fills_view = {b: (e.cards[c].brief() if c else None) for b, c in filled["fills"].items()}
        out = self.gm.ask("gm_beat_fill", self.gm_prompt(
            f"Beat Frame {frame['name']} triggers ({beat['reason']}): \"{frame['sentence']}\". Open blanks were "
            "filled by these cards (null = use the default). For each filled blank choose a tag and write it. "
            "For each PLAYER card, ask its owner one question and write the compel.",
            {"frame": {k: frame[k] for k in ("id", "name", "sentence", "open", "defaults", "stakes")},
             "fills": fills_view}),
            self.base_ctx(call="beat_fill", filled=filled))
        texts = {}
        for f in out.get("fills", []):
            b, cid, tag = f.get("blank"), f.get("card_id"), f.get("tag_used")
            if b in filled["fills"] and filled["fills"][b] == cid:
                ok = tag in e.cards[cid].tags()
                if not ok:
                    e.violation("GM", "§5", f"blank {b} filled with a tag not on {cid}: {tag!r}")
                texts[b] = f.get("text", "")
                self.cost_records.append({"event": "beat_fill", "scene": e.scene, "draw_id": cid, "valid": ok,
                                          "tag": tag, "text": f.get("text", "")[:300], "improvised": False})
        for b, cid in filled["fills"].items():
            if cid and b not in texts:
                e.violation("GM", "§5", f"blank {b} filled by {cid} was not written")
                self.cost_records.append({"event": "beat_fill", "scene": e.scene, "draw_id": cid, "valid": False,
                                          "tag": "", "text": "", "improvised": False})
        answers = {}
        for cid in filled["cards"]:
            if not e.is_player_deck_card(cid):
                continue
            pid = e.deck_player_cards[cid]
            q = next((x for x in out.get("questions", []) if x.get("card_id") == cid), None)
            c = next((x for x in out.get("compels", []) if x.get("card_id") == cid), None)
            offer = ({"tag_used": c.get("tag_used"), "complication": c.get("complication"),
                      "refusal_cost": c.get("refusal_cost")} if c else None)
            if q is None:
                e.violation("GM", "§5", f"no question asked for {cid}")
            r = self.player_card_compel(cid, reason="beat frame", question=q or {"question": "What is this to you?"},
                                        offer=offer)
            answers[e.name(pid)] = r["answer"]
        # Spec 0.2.0 §4: pulled cards beyond the frame's open blanks surface at once (memory, messenger, news, omen).
        for cid in (pulled or []):
            if cid not in filled["cards"] and cid not in e.surfaced:
                self.player_card_compel(cid, reason="backstory guarantee (extra card)")
        values = dict(frame["defaults"])
        values.update({b: t for b, t in texts.items() if t})
        try:
            sentence = frame["sentence"].format(**values)
        except (KeyError, IndexError):
            sentence = frame["sentence"]
        self.mech(f"Beat: {sentence}")
        return self.gm.ask("gm_frame", self.gm_prompt(
            "Frame the scene that opens with this Beat Frame, using the completed sentence and the players' answers "
            "(which are canon).",
            {"completed_sentence": sentence, "answers": answers, "stakes": frame["stakes"]}),
            self.base_ctx(call="beat_frame"))

    # ------------------------------------------------------------------ rounds
    def play_round(self, rnd: int, final: bool) -> tuple[bool, dict | None]:
        e = self.engine
        active = [pid for pid in e.order if not e.chars[pid].out_of_scene]
        if not active:
            n = self.narrate(final=True, results=[], story=[])
            return True, n.get("end") or {}
        conflict = any(n.hostile and not n.out for n in e.npcs.values())

        def declare(pid):
            task = ("Declare what your character does this round. action: pass (do nothing notable), roleplay "
                    "(talk/act without a roll), overcome, create_advantage (name the aspect in advantage_name), "
                    "attack (target_npc)" + (", or concede this conflict (optionally name a card in sacrifice_card "
                                              "to give up for an extra fate point)" if conflict else "")
                    + ". Pick the skill you'd roll. target_card is a face-up card ID your action works against, if any.")
            return self.players[pid].ask("player_declare", self.p_prompt(pid, task),
                                         self.base_ctx(pid, call="declare", conflict=conflict))
        decls = dict(zip(active, self._pmap(declare, active)))
        self.addressed = set()
        story_this_round: list[str] = []
        for pid, d in decls.items():
            act = d.get("action", "pass")
            if act != "pass":
                self.turns[pid] = self.turns.get(pid, 0) + 1
            text = d.get("description", "")
            if d.get("speech"):
                e.say(e.name(pid), d["speech"], kind="speech")
            if act != "pass" and text:
                e.say(e.name(pid), f"({text})", kind="action")
            e.log(event_type="declare", actor=e.name(pid), action=act, skill=d.get("skill", "") if act in ROLL_ACTIONS else "",
                  notes=text[:160])
            if act == "concede":
                if not conflict:
                    e.violation(e.name(pid), "§8", "conceded outside a conflict")
                    continue
                r = e.concede(pid, d.get("sacrifice_card") or None)
                self.mech(f"{e.name(pid)} concedes (+{r['gain']} FP).")
                if r["story"]:
                    story_this_round.append(r["story"])
                self._handle_empty_story()
        rolling = {pid: d for pid, d in decls.items() if d.get("action") in ROLL_ACTIONS
                   and not e.chars[pid].out_of_scene}
        results = []
        adj = {"rolls": [], "npc_actions": [], "compels": []}
        if rolling or conflict or any(d.get("action") == "roleplay" for d in decls.values()):
            adj = self.gm.ask("gm_adjudicate", self.gm_prompt(
                "Adjudicate this round's declared actions (see the Details). Set opposition for each rolling action, "
                "choose any invokes, NPC attacks and compels.",
                {"declared": {e.name(p): d for p, d in decls.items()}, "npcs": [n.__dict__ for n in e.npcs.values()],
                 "central_question": getattr(self, "central_question", "")}),
                self.base_ctx(call="adjudicate", decls=decls))
        # Free (non-deck) compels.
        for c in adj.get("compels", [])[:2]:
            pid = e.pid_by_name(c.get("player", ""))
            if not pid or e.chars[pid].out_of_scene:
                continue
            cid = c.get("card_id") or None
            if cid and not e.compel_card_ok(pid, cid):
                e.violation("GM", "§3/§11", f"compel names card {cid}, which is not in play for {e.name(pid)} "
                            "(not theirs, or in the Session Deck / set aside)")
                continue
            ans = self.players[pid].ask("player_compel", self.p_prompt(
                pid, f"The GM offers a compel on '{c.get('tag', '')}': \"{c.get('complication', '')}\". Accept (gain 1 "
                "fate point) or refuse (pay 1)?"), self.base_ctx(pid, call="compel", from_deck=False))
            res = e.resolve_compel(pid, bool(ans.get("accept", True)), card_id=cid, tag=c.get("tag", ""),
                                   from_deck=False, text=c.get("complication", ""))
            self.cost_records.append({"event": "free_compel", "scene": e.scene, "draw_id": "", "valid": None,
                                      "tag": c.get("tag", ""), "text": c.get("complication", "")[:300],
                                      "improvised": True, "accepted": res["accepted"], "owner": e.name(pid)})
            if ans.get("speech"):
                e.say(e.name(pid), ans["speech"], kind="speech")
            self.mech(f"{e.name(pid)} {'accepts' if res['accepted'] else 'refuses'} a compel.")
            if res["accepted"] and self.arm["story_piles"]:
                sc = e.story_draw(pid, trigger="free_compel_accepted", free_to="GM")
                if sc:
                    story_this_round.append(sc)
                self._handle_empty_story()
        # Rolls.
        adj_by = {}
        for r in adj.get("rolls", []):
            p = e.pid_by_name(r.get("player", ""))
            if p:
                adj_by[p] = r
        pending_costs = []
        for pid in e.order:
            if pid not in rolling or e.chars[pid].out_of_scene:
                continue
            d = rolling[pid]
            a = adj_by.get(pid)
            if a is None:
                e.violation("GM", "§3", f"no adjudication for {e.name(pid)}'s declared roll")
                a = {"needs_roll": True, "opposing_tags": []}
            if not a.get("needs_roll", True):
                e.log(event_type="auto_success", actor=e.name(pid), action=d.get("action"), result="success (no roll)")
                results.append({"player": e.name(pid), "action": d.get("action"), "outcome": "success (no roll needed)",
                                "description": d.get("description", "")})
                continue
            results.append(self.resolve_roll(pid, d, a, pending_costs, story_this_round))
        # NPC attacks.
        for na in adj.get("npc_actions", [])[:4]:
            results.extend(self.npc_attack(na, story_this_round))
        # Costs for ties / major costs.
        if pending_costs:
            self.resolve_costs(pending_costs)
        # Spec 0.2.0 §4: a guarantee pull during the final scene is revealed and resolved at once.
        while e.immediate_surface:
            cid = e.immediate_surface.pop(0)
            if cid not in e.surfaced:
                self.player_card_compel(cid, reason="backstory guarantee (final scene)")
                results.append({"player": e.name(e.deck_player_cards[cid]), "action": "backstory guarantee",
                                "outcome": f"card {cid} surfaced"})
        n = self.narrate(final=final, results=results, story=story_this_round)
        over = bool(n.get("scene_over")) or final
        return over, (n.get("end") or {}) if over else None

    def resolve_roll(self, pid, d, a, pending_costs, story_this_round) -> dict:
        e = self.engine
        name = e.name(pid)
        target_npc = d.get("target_npc") or a.get("npc") or None
        if target_npc and target_npc not in e.npcs:
            target_npc = next((n for n in e.npcs if n.lower() == str(target_npc).lower()), None)
        opp = {"kind": "active" if a.get("npc") else "passive", "npc": a.get("npc", ""),
               "opposing_tags": a.get("opposing_tags", []), "gm_invokes": a.get("gm_invokes", []),
               "hostile_invokes": a.get("hostile_invokes", [])}
        target_card = d.get("target_card") or a.get("target_card") or None
        ctx = e.begin_roll(pid, action=d["action"], skill=d.get("skill", ""), target_card=target_card,
                           target_npc=target_npc if d["action"] == "attack" or a.get("npc") else None, opp=opp,
                           description=d.get("description", ""), advantage_name=d.get("advantage_name", ""))
        inv_opts = e.invokable_for(pid)
        post = {"invokes": [], "take_major_cost": False}
        if ctx.shifts < 3 and (inv_opts and (e.chars[pid].fp > 0 or any(o["free"] for o in inv_opts)) or ctx.shifts < 0):
            info = {"your_skill": f"{ctx.skill} {ctx.skill_rating:+d}", "dice": fmt_dice(ctx.dice),
                    "your_total": ladder(ctx.total), "opposition": ladder(ctx.opp_total),
                    "gm_invoked": [f"{t} [{c}]" for c, t in ctx.gm_invokes + ctx.hostile_invokes],
                    "currently": ("fail" if ctx.shifts < 0 else "tie" if ctx.shifts == 0 else "success"),
                    "invokable_tags": inv_opts[:40], "your_fate_points": e.chars[pid].fp}
            post = self.players[pid].ask("player_post_roll", self.p_prompt(
                pid, "Your roll is in (see Details). Each invoke adds +2 and costs 1 fate point unless you have a free "
                "invoke on that source. Choose invokes (source_id + exact tag), and if you still fail, whether to take "
                "success at a major cost." + (" If this becomes success with style on create_advantage you may set "
                                              "use_story_ally to bring in an ally or lead instead of the aspect."
                                              if self.arm["story_piles"] and d["action"] == "create_advantage" else ""),
                info), self.base_ctx(pid, call="post_roll", roll=ctx, options=inv_opts))
        applied = e.apply_player_invokes(ctx, post.get("invokes", [])[:4])
        res = e.finalize_roll(ctx, take_major_cost=bool(post.get("take_major_cost")),
                              use_story_ally=bool(post.get("use_story_ally")))
        if res["effects"].get("story_card"):
            story_this_round.append(res["effects"]["story_card"])
        self._handle_empty_story()
        opp_desc = ladder(ctx.opp_total)
        self.mech(f"{name} — {ctx.action.replace('_', ' ')} with {ctx.skill}: dice {fmt_dice(ctx.dice)}"
                  + (f", invoking {', '.join(applied)}" if applied else "")
                  + f" → {ladder(ctx.total)} vs {opp_desc}: {res['outcome'].replace('_', ' ').upper()}"
                  + (f" ({res['effects']['npc_harm']})" if res["effects"].get("npc_harm") else ""))
        if res["drawn"]:
            if e.is_player_deck_card(res["drawn"]):
                pending_costs.append({"event_id": res["event_id"], "card_id": res["drawn"], "mode": "player_card_compel",
                                      "outcome": res["outcome"], "roller": name})
            else:
                e.place_drawn_gm_card(res["drawn"])
                pending_costs.append({"event_id": res["event_id"], "card_id": res["drawn"], "mode": "gm_card",
                                      "outcome": res["outcome"], "roller": name})
        elif res["cost_mode"] in ("face_up_gm_tag", "improvised"):
            pending_costs.append({"event_id": res["event_id"], "card_id": "", "mode": res["cost_mode"],
                                  "outcome": res["outcome"], "roller": name})
        if res["outcome"] == "success_with_style" and self.arm["deck"] and e.deck:
            top = e.peek()
            pk = self.players[pid].ask("player_peek", self.p_prompt(
                pid, "Success with style: you may look at the top card of the Session Deck and leave it or move it to "
                "the bottom.", {"top_card": e.cards[top].brief()}), self.base_ctx(pid, call="peek", top=top))
            if ctx.action == "create_advantage":
                e.fire("AMB-27", f"event {res['event_id']}")
            if pk.get("move_to_bottom"):
                e.peek_move_to_bottom()
            e.log(event_type="peek", actor=name, action="Peek", draw_id=top,
                  notes="moved to bottom" if pk.get("move_to_bottom") else "left on top")
        return {"player": name, "action": ctx.action, "description": ctx.description, "outcome": res["outcome"],
                "effects": {k: v for k, v in res["effects"].items() if k != "note"}, "event_id": res["event_id"]}

    def npc_attack(self, na: dict, story_this_round: list) -> list[dict]:
        e = self.engine
        npc = e.npcs.get(na.get("npc", ""))
        pid = e.pid_by_name(na.get("target", ""))
        if not npc or npc.out or not pid or e.chars[pid].out_of_scene:
            if not npc or not pid:
                e.violation("GM", "§3", f"NPC action with unknown NPC or target: {na}")
            return []
        track = na.get("harm", "physical")
        att = e.roll4df()
        skill, rating = e.skill_rating(pid, DEFENSE_SKILL[track])
        dfn = e.roll4df()
        shifts = (npc.rating + sum(att)) - (rating + sum(dfn))
        name = e.name(pid)
        e.log(event_type="defend", actor=name, action=f"Defend vs {npc.name}", skill=f"{skill} {rating:+d}",
              dice=fmt_dice(dfn), total=f"{rating + sum(dfn):+d}", opposition=f"{npc.rating + sum(att):+d}",
              result="hit" if shifts > 0 else "defended", notes=na.get("description", "")[:120])
        self.mech(f"{npc.name} attacks {name} ({track}): {ladder(npc.rating + sum(att))} vs {name}'s {skill} "
                  f"{ladder(rating + sum(dfn))} — " + (f"hit for {shifts}" if shifts > 0 else "defended"))
        out = {"player": name, "action": f"defend vs {npc.name}", "description": na.get("description", ""),
               "outcome": f"hit for {shifts} shifts" if shifts > 0 else "defended"}
        if shifts <= 0:
            return [out]
        opts = e.absorb_options(pid, track, shifts)
        if not opts:
            sc = e.taken_out(pid, npc.name)
            self.mech(f"{name} is taken out.")
            out["outcome"] += " — TAKEN OUT"
            if sc:
                story_this_round.append(sc)
            self._handle_empty_story()
            return [out]
        choice = self.players[pid].ask("player_absorb", self.p_prompt(
            pid, f"You take a {shifts}-shift {track} hit. Choose how to absorb it (option index). If it includes a "
            "consequence, name it (consequence_text) and pick one of your available cards to carry it (strain_card_id; "
            "for a mild consequence also a power tag in strain_tag).", {"options": opts}),
            self.base_ctx(pid, call="absorb", options=opts))
        idx = choice.get("option", 0)
        if not isinstance(idx, int) or not 0 <= idx < len(opts):
            e.violation(name, "§8", f"invalid absorb option {idx}")
            idx = 0
        opt = opts[idx]
        texts = {lvl: choice.get("consequence_text") or f"{lvl} harm" for lvl in opt["consequences"]}
        strain = {lvl: {"card_id": choice.get("strain_card_id"), "tag": choice.get("strain_tag")}
                  for lvl in opt["consequences"]}
        e.apply_absorb(pid, track, shifts, opt, texts, strain)
        out["outcome"] += f" — absorbed ({'box ' + str(opt['box']) if opt['box'] else ''} {' '.join(opt['consequences'])})"
        return [out]

    def resolve_costs(self, pending: list[dict]) -> None:
        e = self.engine
        view = []
        for p in pending:
            item = {"event_id": p["event_id"], "outcome": p["outcome"], "roller": p["roller"], "mode": p["mode"]}
            if p["card_id"]:
                item["drawn_card"] = e.cards[p["card_id"]].brief()
                if p["mode"] == "player_card_compel":
                    item["owner"] = e.name(e.deck_player_cards[p["card_id"]])
            view.append(item)
        guide = {
            "gm_card": "build the cost from the drawn card's tags (major cost: its weakness or a GM THREAT tag)",
            "player_card_compel": "text = the compel you offer the card's owner; refusal_cost = a face-up GM tag",
            "face_up_gm_tag": "deck is empty: build the cost from a face-up GM tag (card_id + tag_used)",
            "improvised": "invent the cost; card_id and tag_used may be empty",
        }
        out = self.gm.ask("gm_costs", self.gm_prompt(
            "Write one item per pending cost (match event_id). " + " | ".join(f"{k}: {v}" for k, v in guide.items()
                                                                            if any(p["mode"] == k for p in pending)),
            {"pending": view}), self.base_ctx(call="costs", items=pending))
        items = {it.get("event_id"): it for it in out.get("items", [])}
        for p in pending:
            it = items.get(p["event_id"])
            if it is None:
                e.violation("GM", "§3", f"no cost written for event {p['event_id']}")
                it = {}
            if p["mode"] == "player_card_compel":
                self.player_card_compel(p["card_id"], reason=p["outcome"], offer={
                    "tag_used": it.get("tag_used"), "complication": it.get("text", ""),
                    "refusal_cost": it.get("refusal_cost") or {}})
                continue
            tag, cid = it.get("tag_used", ""), it.get("card_id", "")
            if p["mode"] == "gm_card":
                card = e.cards[p["card_id"]]
                allowed = set(card.tags())
                if p["outcome"] == "success_major_cost":
                    allowed = {card.weakness} | {t for c, t in e.rail_gm_tags() if e.cards[c].type == "THREAT"}
                valid = tag in allowed
            elif p["mode"] == "face_up_gm_tag":
                valid = (cid, tag) in e.rail_gm_tags()
            else:
                valid = None
            if valid is False:
                e.violation("GM", "§3", f"cost for event {p['event_id']} did not use an allowed tag: {tag!r}")
            self.cost_records.append({"event": p["outcome"], "scene": e.scene, "draw_id": p["card_id"],
                                      "valid": valid, "tag": tag, "text": it.get("text", "")[:300],
                                      "improvised": p["mode"] == "improvised", "mode": p["mode"]})
            e.log(event_type="cost", actor="GM", action=f"Cost ({p['outcome']})", draw_id=p["card_id"],
                  tags_invoked=tag, notes=it.get("text", "")[:200], improvised=p["mode"] == "improvised",
                  cost_valid=valid, for_event=p["event_id"])
            e.say("GM", it.get("text", ""))

    def _handle_empty_story(self) -> None:
        """§6A empty pile: the pile's owner writes a card on the spot."""
        e = self.engine
        for d in e.scene_flags["story_drawn"]:
            if not d.get("empty") or d.get("handled"):
                continue
            d["handled"] = True
            owner = d["owner"]
            if owner is None or self.arm["placebo"]:
                if self.arm["placebo"] and owner is not None:
                    pool = [c["id"] for c in PLACEBO["story_cards"] if c["id"] not in e.chars[owner].story_pile]
                    cid = e.rng["placebo"].choice(sorted(pool))
                    e.chars[owner].story_pile.append(cid)
                else:
                    sc = self.gm.ask("write_story", self.gm_prompt("The GM Story Pile is empty. Write a new NPC or "
                                                                   "THREAD story card (3 power tags, 1 weakness)."),
                                     self.base_ctx(call="write_story"))
                    cid = e.add_story_card(None, sc)
            else:
                sc = self.players[owner].ask("write_story", self.p_prompt(
                    owner, "Your character's story pile is empty. Write a new NPC or THREAD tied to one of your ROOTS or "
                    "REACH tags: title, 3 power tags (2-5 words), 1 weakness."),
                    self.base_ctx(owner, call="write_story"))
                cid = e.add_story_card(owner, sc)
            if cid:
                e.place_on_rail(cid, reason=f"new story card ({d['trigger']})")
                e.free_invokes[(d["free_to"], cid)] = e.free_invokes.get((d["free_to"], cid), 0) + 1
                d["card"] = cid

    def narrate(self, final: bool, results: list, story: list) -> dict:
        e = self.engine
        extra = {"results": results, "central_question": getattr(self, "central_question", "")}
        if story:
            extra["story_cards_to_feature"] = [e.cards[c].brief() for c in story if c]
        n = self.gm.ask("gm_narrate", self.gm_prompt(
            "Narrate this round's results." + (" This is the FINAL round of the scene: set scene_over true and fill "
                                               "'end'." if final else " Set scene_over if the scene is done (then fill 'end')."),
            extra), self.base_ctx(call="narrate", final=final, results=results))
        e.say("GM", n.get("narration", ""))
        self.addressed = set(n.get("address", []))
        return n

    # ------------------------------------------------------------------ referee
    def referee_scene(self) -> None:
        e = self.engine
        rows = [r for r in e.events if r["scene"] == e.scene and r["session"] == e.session]
        cost_rows = [c for c in self.cost_records if c["scene"] == e.scene]
        for c in cost_rows:
            if c.get("draw_id") and c["draw_id"] in e.cards:
                c["card"] = e.cards[c["draw_id"]].brief()
        eng_v = [v for v in e.violations if v["scene"] == e.scene]
        fired = [a for a in e.rulings.fired if a["scene"] == e.scene]
        prompt = ("Log fields: fp_change = the actor's fate point change from this event; fp_balances = every "
                  "player's fate points after it; gm_fp = the GM's remaining fate points; gm_fp_spent = GM points paid on "
                  "that roll (free invokes cost none); caused_by = the event_id of the roll that caused this row. Story "
                  "Weight changes, module deployments and GM free-invoke grants ('GM +1 free invoke' in rail notes) are "
                  "logged as their own rows.\n\n"
                  f"Scene {e.scene} event log (one row per event):\n{j(rows)}\n\nCosts, compels and Beat Frame fills "
                  f"with the drawn card:\n{j(cost_rows)}\n\nEngine refusals already recorded:\n{j(eng_v)}\n\n"
                  f"Interim rulings the engine applied:\n{j([{k: a[k] for k in ('id', 'section', 'interim_ruling')} for a in fired])}"
                  "\n\nReport violations, ambiguities (not already covered by the interim rulings above), a cost_check per "
                  "cost/compel/fill with a draw_id, and up to 3 friction points.")
        out = self.ref_agent.ask("referee", prompt, self.base_ctx(call="referee", rows=rows, costs=cost_rows))
        for v in out.get("violations", []):
            self.referee["violations"].append({**v, "scene": e.scene, "source": "referee"})
        for a in out.get("ambiguities", []):
            self.referee["ambiguities"].append({**a, "scene": e.scene, "source": "referee"})
        for c in out.get("cost_checks", []):
            self.referee["cost_checks"].append({**c, "scene": e.scene})
        self.referee["friction"] += [{"scene": e.scene, "text": f} for f in out.get("friction", [])]

    # ------------------------------------------------------------------ after the session
    def post_session(self) -> None:
        e = self.engine
        rep = {"summary": "", "threats_left_play": []}
        rep = self.gm.ask("gm_post", self.gm_prompt(
            "The session is over. Write a 3-sentence Chronicle summary, and for each GM card that left play this "
            "session say whether the fiction left it alive (it mutates; give a new tag reflecting what the party did "
            "to it) or destroyed.", {"left_play": e.left_play}), self.base_ctx(call="post"))
        self.chronicle = e.post_session(rep)

    def run_surveys(self) -> None:
        e = self.engine
        self.surveys = []

        def survey(pid):
            task = ("The session is over. The GM asks everyone for honest, quick feedback about how it went for you. "
                    "Score 1-7 (1 = not at all, 7 = extremely): fun (how much fun was it), involvement (how involved in "
                    "the story did your character feel), connection (how much did events feel connected to YOUR "
                    "character specifically), control (how much control did you feel over what happened to you), "
                    "play_again (would you play a second session with this group). Then answer briefly: best_moment "
                    "(and why), most_frustrating, background_used (was something from your background used by the GM? "
                    "how did it land: good, unfair, or forced?), wanted_but_couldnt (what you wanted to do that the game "
                    "didn't let you), one_sentence (did your backstory feel used well, ignored, or used against you "
                    "unfairly?). Be candid; low scores are fine.")
            sys_prompt = self.players[pid].system
            p = (f"== Your character sheet ==\n{j(e.player_sheet(pid))}\n\n== The whole session ==\n"
                 f"{render_transcript(e.transcript, pid, 40000)}\n\n== Feedback ==\n{task}")
            ans = Agent(self.client, "player", e.name(pid) + "#survey", sys_prompt).ask(
                "survey", p, self.base_ctx(pid, call="survey"))
            return {"character_id": pid, "personality_id": e.chars[pid].personality,
                    "scores": {k: ans.get(k) for k in ("fun", "involvement", "connection", "control", "play_again")},
                    "free_text": {k: ans.get(k, "") for k in ("best_moment", "most_frustrating", "background_used",
                                                              "wanted_but_couldnt", "one_sentence")},
                    "synthetic": self.backend == "scripted"}
        self.surveys = self._pmap(survey, e.order)
        tr = render_transcript(e.transcript, None, 60000)
        names = [c.name for c in e.chars.values()]
        iv = self.interviewer.ask("interviewer", (
            f"Transcript:\n{tr}\n\nPlayers: {names}. For each player count (a) turns: the number of times the player "
            "spoke or acted (lines attributed to them; do not count [table] lines), and (b) how many times the player "
            "referred to ANOTHER player character's background, past, people or places. Return one entry per player."),
            self.base_ctx(call="interviewer", names=names))
        self.interview = iv

    # ------------------------------------------------------------------ output
    def write(self, status: str, error: str | None = None) -> dict:
        e = self.engine
        rec = {
            "run_id": self.run_id, "batch_id": self.batch_id, "arm": self.arm_key, "seed": self.seed,
            "spec_version": SPEC_VERSION, "status": status, "error": error, "backend": self.backend,
            "run_index": self.run_index, "cohort_id": self.cohort_id,
            "assignments": [{"character_id": pid, "name": e.chars[pid].name, "personality_id": e.chars[pid].personality,
                             "seat": i} for i, pid in enumerate(e.order)],
            "prep_packet": {"anchors": self.prep["anchors"], "environment": self.prep["environment"],
                            "modules": self.prep["modules"],
                            "beat_frames": [{k: b.get(k) for k in ("id", "name", "trigger", "used")}
                                            for b in e.prep["beat_frames"]]},
            "events": e.events,
            "scenes": self.scenes,
            "transcript": e.transcript,
            "costs": self.cost_records,
            "referee": {"violations": e.violations + self.referee["violations"],
                        "ambiguities": e.rulings.fired + self.referee["ambiguities"],
                        "cost_checks": self.referee["cost_checks"], "friction": self.referee["friction"]},
            "surveys": getattr(self, "surveys", []),
            "interview": getattr(self, "interview", None),
            "chronicle": getattr(self, "chronicle", None),
            "state_end": {"tension": e.tension, "fp": {e.chars[p].name: e.chars[p].fp for p in e.order},
                          "surfaced": sorted(e.surfaced), "deck_player_cards": {k: e.name(v) for k, v in e.deck_player_cards.items()},
                          "guarantee_pulled": e.guarantee_pulled, "guarantee_failed": e.guarantee_failed,
                          "deck_left": list(e.deck), "draws": e.draws_this_session,
                          "turns": {e.name(p): self.turns.get(p, 0) for p in e.order}},
            "notes": self.notes,
            "metrics": {},
            "tokens": self.meter.as_dict(),
            "llm_calls": len(self.client.calls),
            "models": {r: self.client.model_for(r) for r in ("gm", "player", "referee", "interviewer")},
            "elapsed_s": round(time.time() - self.started, 1),
        }
        if status != "partial":
            from analyze import run_metrics
            rec["metrics"] = run_metrics(rec)
        self.out_path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.out_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(rec, indent=1, ensure_ascii=False, default=str))
        tmp.replace(self.out_path)
        return rec


def main() -> None:
    ap = argparse.ArgumentParser(description="Run one Scene-Deck session.")
    ap.add_argument("--arm", required=True)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--run-index", type=int, default=0)
    ap.add_argument("--batch-id", default="adhoc")
    ap.add_argument("--backend", default="scripted", choices=["scripted", "claude_cli"])
    ap.add_argument("--token-cap", type=int, default=3_000_000)
    ap.add_argument("--cohort-id", default=None)
    a = ap.parse_args()
    s = Session(arm_key=a.arm, seed=a.seed, run_index=a.run_index, batch_id=a.batch_id, backend=a.backend,
                out_dir=ROOT / "runs" / a.batch_id, cache_dir=ROOT / "cache" / a.batch_id, token_cap=a.token_cap,
                cohort_id=a.cohort_id)
    rec = s.run()
    print(json.dumps({"run_id": rec["run_id"], "status": rec["status"], "error": (rec["error"] or "")[-1500:],
                      "metrics": rec["metrics"], "tokens": rec["tokens"]}, indent=1))


if __name__ == "__main__":
    main()
