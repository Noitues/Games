"""Scripted (zero-token) agents.

Deterministic, personality-flavoured heuristics that return valid JSON for every call kind. They
exist to shake out the engine and orchestrator and to run structural Monte Carlo. They are not a
model of human fun: their survey answers are random and marked ``synthetic``, and analyze.py
excludes them from experiential results.
"""

from __future__ import annotations

import hashlib
import random

ACTION_BIAS = {
    "optimizer": {"create_advantage": 3, "overcome": 3, "attack": 2, "roleplay": 1, "pass": 1},
    "storyteller": {"roleplay": 4, "overcome": 2, "create_advantage": 2, "attack": 1, "pass": 1},
    "protector": {"overcome": 3, "attack": 3, "create_advantage": 2, "roleplay": 1, "pass": 1},
    "rules_lawyer": {"overcome": 3, "create_advantage": 3, "attack": 1, "roleplay": 1, "pass": 1},
    "instigator": {"attack": 5, "overcome": 2, "create_advantage": 1, "roleplay": 1, "pass": 0},
    "lurker": {"pass": 6, "roleplay": 1, "overcome": 1, "create_advantage": 1, "attack": 1},
    "tactician": {"create_advantage": 5, "overcome": 2, "attack": 1, "roleplay": 1, "pass": 1},
    "method_actor": {"roleplay": 3, "overcome": 2, "attack": 2, "create_advantage": 1, "pass": 1},
}
ACCEPT_COMPEL = {"optimizer": 0.5, "storyteller": 0.9, "protector": 0.85, "rules_lawyer": 0.1,
                 "instigator": 0.7, "lurker": 0.8, "tactician": 0.4, "method_actor": 0.9}


class Scripted:
    def __init__(self, seed: int, run_id: str):
        self.seed = seed
        self.run_id = run_id

    def _rng(self, agent: str, n: int) -> random.Random:
        h = hashlib.sha256(f"{self.run_id}:{agent}:{n}".encode()).hexdigest()[:16]
        return random.Random(int(h, 16))

    def respond(self, *, role: str, agent: str, kind: str, ctx: dict, n: int) -> dict:
        rng = self._rng(agent, n)
        fn = getattr(self, "k_" + kind)
        return fn(rng, ctx)

    # ------------------------------------------------------------------ GM
    def k_gm_frame(self, rng, ctx):
        e = ctx["engine"]
        gm_cards = [c for c in e.rail if e.cards[c].owner in ("GM",) and e.cards[c].origin == "world"]
        npcs = []
        if rng.random() < 0.55:
            npcs.append({"name": rng.choice(["Reed Raider", "Cartel Bruiser", "Hive-Touched Stalker", "Drowned Acolyte"]),
                         "rating": rng.choice([1, 2, 2, 3]), "stress": 2, "hostile": True,
                         "card_id": rng.choice(gm_cards) if gm_cards else ""})
        out = {"planned_scene": f"Scene {e.scene}: the party pushes on through the rain.",
               "narration": f"Scene {e.scene}. Rain hammers the reeds as the party presses on.",
               "central_question": "Will the party get through?", "npcs": npcs,
               "address": [e.chars[rng.choice(e.order)].name]}
        drawn = ctx.get("drawn")
        if ctx.get("call") == "altered":
            if drawn:
                out["used_card"] = {"card_id": drawn, "tag": rng.choice(e.cards[drawn].tags())}
            else:
                tags = e.rail_gm_tags()
                if tags:
                    c, t = rng.choice(tags)
                    out["used_card"] = {"card_id": c, "tag": t}
        return out

    def k_gm_beat_fill(self, rng, ctx):
        e = ctx["engine"]
        filled = ctx["filled"]
        fills, qs, comps = [], [], []
        gm_tags = e.rail_gm_tags()
        for b, cid in filled["fills"].items():
            if not cid:
                continue
            card = e.cards[cid]
            tag = rng.choice(card.power_tags)
            fills.append({"blank": b, "card_id": cid, "tag_used": tag, "text": f"{card.title} ({tag})"})
            if e.is_player_deck_card(cid):
                owner = e.name(e.deck_player_cards[cid])
                qs.append({"player": owner, "card_id": cid, "question": f"What does {card.title} mean to you?"})
                rc = rng.choice(gm_tags) if gm_tags else ("", "")
                comps.append({"card_id": cid, "player": owner, "tag_used": card.weakness,
                              "complication": f"{card.weakness} drags you in.",
                              "refusal_cost": {"card_id": rc[0], "tag": rc[1], "text": f"{rc[1]} bites instead."}})
        return {"fills": fills, "questions": qs, "compels": comps}

    def k_gm_adjudicate(self, rng, ctx):
        e = ctx["engine"]
        rolls = []
        gm_tags = e.rail_gm_tags()
        fi = {k[1] for k, v in e.free_invokes.items() if k[0] == "GM" and v > 0}
        for pid, d in ctx["decls"].items():
            if d.get("action") not in ("overcome", "create_advantage", "attack"):
                continue
            opp_tags = []
            pool = [t for t in gm_tags]
            rng.shuffle(pool)
            for c, t in pool[: rng.choice([0, 1, 1, 2])]:
                opp_tags.append({"card_id": c, "tag": t})
            inv = []
            used = {(o["card_id"], o["tag"]) for o in opp_tags}
            cand = [(c, t) for c, t in gm_tags if c in fi and (c, t) not in used]
            if cand and rng.random() < 0.35:
                c, t = rng.choice(cand)
                inv.append({"card_id": c, "tag": t})
            hostile = []
            if e.gm_fp > 1 and rng.random() < 0.08:
                ch = e.chars[pid]
                live = [c for c in ch.binder if ch.card_state.get(c) in ("binder", "rail") and e.cards[c].weakness]
                if live:
                    hostile.append({"player": ch.name, "card_id": rng.choice(live)})
            npc = ""
            if d.get("action") == "attack" or (e.npcs and rng.random() < 0.3):
                alive = [n for n, x in e.npcs.items() if not x.out]
                npc = d.get("target_npc") if d.get("target_npc") in alive else (rng.choice(alive) if alive else "")
            rolls.append({"player": e.name(pid), "needs_roll": rng.random() > 0.05, "opposing_tags": opp_tags,
                          "npc": npc, "gm_invokes": inv, "hostile_invokes": hostile, "target_card": ""})
        npc_actions = []
        for n, x in e.npcs.items():
            if x.hostile and not x.out and rng.random() < 0.6:
                tgt = [p for p in e.order if not e.chars[p].out_of_scene]
                if tgt:
                    npc_actions.append({"npc": n, "target": e.name(rng.choice(tgt)),
                                        "harm": rng.choice(["physical", "physical", "mental"]),
                                        "description": f"{n} strikes."})
        compels = []
        if rng.random() < 0.25:
            pid = rng.choice(e.order)
            ch = e.chars[pid]
            live = [c for c in ch.binder if ch.card_state.get(c) in ("binder", "rail") and e.cards[c].weakness]
            if live:
                cid = rng.choice(live)
                compels.append({"player": ch.name, "card_id": cid, "tag": e.cards[cid].weakness,
                                "complication": f"{e.cards[cid].weakness} gets in the way."})
        return {"rolls": rolls, "npc_actions": npc_actions, "compels": compels}

    def k_gm_costs(self, rng, ctx):
        e = ctx["engine"]
        items = []
        gm_tags = e.rail_gm_tags()
        threat_tags = [(c, t) for c, t in gm_tags if e.cards[c].type == "THREAT"]
        for p in ctx["items"]:
            cid = p.get("card_id", "")
            mode = p.get("mode")
            rc = rng.choice(gm_tags) if gm_tags else ("", "")
            if mode == "gm_card":
                card = e.cards[cid]
                if p.get("outcome") == "success_major_cost":
                    tag = card.weakness if (rng.random() < 0.8 or not threat_tags) else rng.choice(threat_tags)[1]
                else:
                    tag = rng.choice(card.tags())
                items.append({"event_id": p["event_id"], "card_id": cid, "tag_used": tag, "text": f"Cost: {tag}."})
            elif mode == "player_card_compel":
                card = e.cards[cid]
                items.append({"event_id": p["event_id"], "card_id": cid, "tag_used": card.weakness,
                              "text": f"{card.weakness} flares up.",
                              "refusal_cost": {"card_id": rc[0], "tag": rc[1], "text": f"{rc[1]} instead."}})
            elif mode == "face_up_gm_tag":
                items.append({"event_id": p["event_id"], "card_id": rc[0], "tag_used": rc[1], "text": f"Cost: {rc[1]}."})
            else:
                items.append({"event_id": p["event_id"], "card_id": "", "tag_used": "", "text": "Something goes wrong."})
        return {"items": items}

    def k_gm_narrate(self, rng, ctx):
        e = ctx["engine"]
        over = ctx.get("final") or rng.random() < 0.3
        out = {"narration": f"The round plays out in scene {e.scene}.", "scene_over": over,
               "address": [e.chars[rng.choice(e.order)].name] if rng.random() < 0.5 else []}
        if over:
            face = [c for c in e.rail if e.cards[c].type in ("THREAT", "FACTION") and e.cards[c].origin == "world"]
            gm_rail = [c for c in e.rail if e.cards[c].origin == "world" and e.cards[c].owner == "GM"]
            out["end"] = {
                "fled_or_bypassed": face[:1] if face and rng.random() < 0.3 else [],
                "resolved_threats": [c for c in face if e.cards[c].type == "THREAT"][:1] if rng.random() < 0.15 else [],
                "goal_filled": rng.random() < 0.1,
                "keep_on_rail": [c for c in gm_rail if rng.random() < 0.4],
                "new_story_cards": ([{"type": "NPC", "title": "A Grateful Survivor",
                                      "power_tags": ["knows a back path", "owes the party", "has dry rope"],
                                      "weakness": "Talks Too Much", "pile": "GM"}] if rng.random() < 0.2 else []),
                "retire_story_cards": [],
                "fiction_triggers_fired": [x["id"] for x in e.prep["modules"] + e.prep["beat_frames"]
                                           if not x.get("used") and str(x.get("trigger", "")).startswith("fiction:")
                                           and rng.random() < 0.15],
                "beat_went_badly": rng.random() < 0.4}
        return out

    def k_gm_post(self, rng, ctx):
        e = ctx["engine"]
        return {"summary": "The party survived the rain. Old debts surfaced. The marsh remembers.",
                "threats_left_play": [{"card_id": lp["card"], "alive": rng.random() < 0.5, "new_tag": "wary of the party"}
                                      for lp in e.left_play if lp["session"] == e.session]}

    def k_write_story(self, rng, ctx):
        return {"type": rng.choice(["NPC", "THREAD"]), "title": "A Face From the Past",
                "power_tags": ["knows old secrets", "owes a favour", "watches from afar"], "weakness": "Wants Something Back"}

    # ------------------------------------------------------------------ players
    def _pers(self, ctx):
        return ctx["engine"].chars[ctx["pid"]].personality

    def k_player_declare(self, rng, ctx):
        e = ctx["engine"]
        pid = ctx["pid"]
        ch = e.chars[pid]
        pers = self._pers(ctx)
        bias = dict(ACTION_BIAS[pers])
        if ch.name in ctx.get("addressed", set()):
            bias["pass"] = 0
        alive = [n for n, x in e.npcs.items() if x.hostile and not x.out]
        if not alive:
            bias["attack"] = 0
        acts = [a for a in bias for _ in range(bias[a])]
        act = rng.choice(acts)
        if ctx.get("conflict") and (ch.consequences["moderate"] or ch.consequences["severe"]) and rng.random() < 0.5:
            sac = None
            if rng.random() < 0.3:
                cands = [c for c in ch.binder if ch.card_state.get(c) == "binder"]
                sac = rng.choice(cands) if cands else None
            return {"action": "concede", "description": "I've had enough.", "sacrifice_card": sac or ""}
        top = sorted(ch.skills.items(), key=lambda kv: -kv[1])
        if act == "attack":
            skill = "Fight" if "Fight" in ch.skills else top[0][0]
        else:
            skill = rng.choice(top[:4])[0]
        gm_rail = [c for c in e.rail if e.cards[c].origin == "world"]
        return {"action": act, "skill": skill, "target_card": rng.choice(gm_rail) if gm_rail and rng.random() < 0.4 else "",
                "target_npc": rng.choice(alive) if act == "attack" and alive else "",
                "advantage_name": "Prepared Ground" if act == "create_advantage" else "",
                "description": f"{ch.name} tries something ({act}).", "speech": "Let's go." if act != "pass" else ""}

    def k_player_post_roll(self, rng, ctx):
        e = ctx["engine"]
        roll = ctx["roll"]
        pid = ctx["pid"]
        pers = self._pers(ctx)
        opts = ctx["options"]
        fp = e.chars[pid].fp
        shifts = roll.shifts
        invokes = []
        used = set()
        eagerness = {"optimizer": 0.9, "tactician": 0.8, "rules_lawyer": 0.7}.get(pers, 0.45)
        free = [o for o in opts if o["free"]]
        paid = [o for o in opts if not o["free"]]
        while shifts < 1 and rng.random() < eagerness:
            pick = next((o for o in free if (o["source_id"], o["tag"]) not in used
                         and o["source_id"] not in {u[0] for u in used}), None)
            if pick is None and fp > 0:
                pick = next((o for o in paid if (o["source_id"], o["tag"]) not in used), None)
                if pick:
                    fp -= 1
            if pick is None:
                break
            used.add((pick["source_id"], pick["tag"]))
            invokes.append({"source_id": pick["source_id"], "tag": pick["tag"]})
            shifts += 2
        return {"invokes": invokes, "take_major_cost": shifts < 0 and rng.random() < 0.5,
                "use_story_ally": rng.random() < 0.3}

    def k_player_compel(self, rng, ctx):
        pers = self._pers(ctx)
        acc = rng.random() < ACCEPT_COMPEL[pers]
        return {"accept": acc, "speech": "Fine." if acc else "No.", "answer": "I made a promise I did not keep."
                if ctx.get("question") else ""}

    def k_player_answer(self, rng, ctx):
        return {"answer": "It is complicated."}

    def k_player_absorb(self, rng, ctx):
        e = ctx["engine"]
        ch = e.chars[ctx["pid"]]
        cands = [c for c in ch.binder if ch.card_state.get(c) in ("binder", "rail")]
        cid = rng.choice(cands) if cands else ""
        return {"option": 0, "consequence_text": "Bruised and Rattled", "strain_card_id": cid,
                "strain_tag": e.cards[cid].power_tags[0] if cid else ""}

    def k_player_peek(self, rng, ctx):
        return {"move_to_bottom": rng.random() < 0.5}

    def k_survey(self, rng, ctx):
        s = lambda: rng.randint(3, 7)
        return {"fun": s(), "involvement": s(), "connection": s(), "control": s(), "play_again": s(),
                "best_moment": "synthetic", "most_frustrating": "synthetic", "background_used": "synthetic",
                "wanted_but_couldnt": "synthetic", "one_sentence": "synthetic"}

    def k_preference(self, rng, ctx):
        return {"choice": rng.choice(["1", "2"]), "reason": "synthetic"}

    # ------------------------------------------------------------------ others
    def k_referee(self, rng, ctx):
        return {"violations": [], "ambiguities": [],
                "cost_checks": [{"event_id": 0, "used_drawn_card": bool(c.get("valid"))} for c in ctx["costs"]
                                if c.get("draw_id")], "friction": []}

    def k_interviewer(self, rng, ctx):
        return {"players": [{"name": n, "turns": 0, "references_to_others_background": 0} for n in ctx["names"]]}

    def k_analyst(self, rng, ctx):
        return {"conclusions": "Scripted backend: no experiential conclusions.", "key_findings": [], "caveats": []}
