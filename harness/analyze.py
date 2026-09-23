"""Metrics, aggregation, paired comparisons, blinded analyst, report and human review packet.

    python analyze.py <batch_id> [--no-llm] [--review]

Per-run metrics (``run_metrics``) are computed from the log alone and stored in each run JSON.
Experiential judgment is blind per session: a Judge agent scores each session alone from a story-only,
de-vocabularied transcript under a random session ID (reports/<batch>_session_blinding.json holds the
key). Scores are joined to arms only afterwards, in ``compile_judgments``. The older arm-label Analyst
is opt-in (--analyst): with unequal arm counts its labels would be guessable from sample size.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import re
import statistics as st
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
SCORES = ["fun", "involvement", "connection", "control", "play_again"]


# ====================================================================== per-run
def gini(xs: list[float]) -> float:
    xs = sorted(x for x in xs if x is not None)
    n = len(xs)
    if n == 0 or sum(xs) == 0:
        return 0.0
    cum = sum((i + 1) * x for i, x in enumerate(xs))
    return round((2 * cum) / (n * sum(xs)) - (n + 1) / n, 4)


def run_metrics(rec: dict) -> dict:
    ev = rec["events"]
    names = [a["name"] for a in rec["assignments"]]
    pers = {a["name"]: a["personality_id"] for a in rec["assignments"]}
    arm = rec["arm"][0]
    se = rec["state_end"]
    # Backstory: an event driven by the player's OWN background (not a placebo card).
    own_cards = set()
    for a in rec["assignments"]:
        pass
    surfaced_owners = set()
    for cid in se.get("surfaced", []):
        owner = se["deck_player_cards"].get(cid)
        if owner and not cid.startswith("PX-"):
            surfaced_owners.add(owner)
    compel_owners = Counter()
    compel_acc = compel_ref = 0
    deck_compels = free_compels = 0
    for e in ev:
        if e.get("event_type") == "compel":
            if e.get("compel") == "accepted":
                compel_acc += 1
            else:
                compel_ref += 1
            if "(deck)" in e.get("action", ""):
                deck_compels += 1
            else:
                free_compels += 1
            if e.get("draw_id") and not str(e.get("draw_id")).startswith("PX-"):
                compel_owners[e["actor"]] += 1
            elif not e.get("draw_id") and e.get("improvised") and arm == "B":
                compel_owners[e["actor"]] += 1   # B: free compels are on the player's own aspects
    backstory_players = {n for n in names if n in surfaced_owners or compel_owners[n] > 0}
    # Free compels in A/C name a card only when the GM gave one; count those as backstory-driven too.
    # Turns & invokes.
    turns = se.get("turns", {})
    invokes = Counter()
    fp_spent = Counter()
    fp_earned = Counter()
    for e in ev:
        t = e.get("event_type")
        if t == "roll":
            k = len([x for x in str(e.get("tags_invoked", "")).split(";") if x.strip()])
            invokes[e["actor"]] += k
            fp_spent[e["actor"]] += int(e.get("fp_spent") or 0)
        elif t == "compel":
            if e.get("compel") == "accepted":
                fp_earned[e["actor"]] += 1
            else:
                fp_spent[e["actor"]] += 1
        elif t == "concede":
            fp_earned[e["actor"]] += -int(e.get("fp_spent") or 0)
        elif t == "fp" and "Hostile" in e.get("action", ""):
            if e.get("actor"):                      # spec 0.2.0+ logs: one row per player
                fp_earned[e["actor"]] += int(e.get("fp_change", 1))
            else:                                   # pilot-01 logs: names in notes
                for n in names:
                    fp_earned[n] += e.get("notes", "").split(", ").count(n)
    costs = rec.get("costs", [])
    drawn_costs = [c for c in costs if c.get("draw_id")]
    valid_drawn = [c for c in drawn_costs if c.get("valid")]
    ref_checks = rec["referee"].get("cost_checks", [])
    ref_yes = [c for c in ref_checks if c.get("used_drawn_card")]
    improvised = [c for c in costs if c.get("improvised")]
    card_supplied = [c for c in costs if c.get("draw_id")]
    viol = rec["referee"]["violations"]
    amb = rec["referee"]["ambiguities"]
    scenes = rec.get("scenes", [])
    tension = [s.get("tension_before") for s in scenes] + ([scenes[-1].get("tension_after")] if scenes else [])
    clocks = [e for e in ev if e.get("event_type") == "clock" and e.get("clock_change")]
    surveys = [s for s in rec.get("surveys", []) if not s.get("synthetic")]
    m = {
        "arm": rec["arm"], "status": rec["status"],
        "scenes": len(scenes),
        "backstory_players": sorted(backstory_players),
        "backstory_all_players": len(backstory_players) == len(names),
        "deck_surfaced_all_players": (len(surfaced_owners) == len(names)) if arm == "A" else None,
        "deck_draws": se.get("draws", 0),
        "draw_costs": len(drawn_costs),
        "draw_cost_used_card_rate_engine": round(len(valid_drawn) / len(drawn_costs), 3) if drawn_costs else None,
        "draw_cost_tag_in_text_rate": round(sum(1 for c in drawn_costs if c.get("tag_in_text")) / len(drawn_costs), 3)
        if drawn_costs else None,
        "draw_cost_repaired": sum(1 for c in drawn_costs if c.get("repaired")),
        "draw_cost_used_card_rate_referee": round(len(ref_yes) / len(ref_checks), 3) if ref_checks else None,
        "fp_end": se.get("fp", {}),
        "fp_end_mean": round(st.mean(se["fp"].values()), 2) if se.get("fp") else None,
        "fp_earned": dict(fp_earned), "fp_spent": dict(fp_spent),
        "compels_accepted": compel_acc, "compels_refused": compel_ref,
        "compels_deck": deck_compels, "compels_free": free_compels,
        "turns": turns, "turn_gini": gini([turns.get(n, 0) for n in names]),
        "invokes": dict(invokes), "invoke_gini": gini([invokes.get(n, 0) for n in names]),
        "tension_trajectory": tension,
        "clock_marks": len(clocks),
        "violations": len(viol), "violations_engine": sum(1 for v in viol if v.get("source") == "engine"),
        "violations_referee": sum(1 for v in viol if v.get("source") == "referee"),
        "ambiguities": len(amb), "ambiguity_ids": sorted({a.get("id", a.get("section", "?")) for a in amb}),
        "gm_improvised_complications": len(improvised), "card_supplied_complications": len(card_supplied),
        "improvisation_share": round(len(improvised) / (len(improvised) + len(card_supplied)), 3)
        if (improvised or card_supplied) else None,
        "guarantee_pulled": len(se.get("guarantee_pulled", [])), "guarantee_failed": len(se.get("guarantee_failed", [])),
        "dice_claim_retries": sum(1 for n in rec.get("notes", []) if n.get("kind") == "dice_claim_retry"),
        "survey_means": {k: round(st.mean(s["scores"][k] for s in surveys), 2) for k in SCORES
                         if surveys and all(isinstance(s["scores"].get(k), int) for s in surveys)},
        "involvement_var_within": round(st.pvariance([s["scores"]["involvement"] for s in surveys]), 3)
        if len(surveys) > 1 and all(isinstance(s["scores"].get("involvement"), int) for s in surveys) else None,
        "personality": pers,
        "elapsed_min": round(rec.get("elapsed_s", 0) / 60, 1),
        "cost_usd": rec.get("tokens", {}).get("cost_usd"),
    }
    return m


# ====================================================================== stats helpers
def mean_ci(xs: list[float], seed: int = 0, n_boot: int = 2000) -> dict:
    xs = [x for x in xs if isinstance(x, (int, float))]
    if not xs:
        return {"n": 0, "mean": None, "lo": None, "hi": None}
    m = st.mean(xs)
    if len(xs) < 2:
        return {"n": len(xs), "mean": round(m, 3), "lo": None, "hi": None}
    rng = random.Random(seed)
    boots = sorted(st.mean(rng.choices(xs, k=len(xs))) for _ in range(n_boot))
    return {"n": len(xs), "mean": round(m, 3), "lo": round(boots[int(0.025 * n_boot)], 3),
            "hi": round(boots[int(0.975 * n_boot) - 1], 3)}


def fmt_ci(c: dict) -> str:
    if not c or c["mean"] is None:
        return "—"
    if c["lo"] is None:
        return f"{c['mean']:.2f} (n={c['n']})"
    return f"{c['mean']:.2f} [{c['lo']:.2f}, {c['hi']:.2f}] (n={c['n']})"


# ====================================================================== batch
def load_runs(batch_id: str) -> list[dict]:
    d = ROOT / "runs" / batch_id
    runs = []
    for p in sorted(d.glob("*.json")):
        if p.name.startswith("_"):
            continue
        r = json.loads(p.read_text())
        if r.get("status") == "partial":
            continue
        if not r.get("metrics"):
            r["metrics"] = run_metrics(r)
        runs.append(r)
    return runs


COMPLAINT_BUCKETS = {
    "rules/confusion": ["rule", "unclear", "confus", "mechanic", "didn't understand", "arbitrary"],
    "agency/control": ["control", "railroad", "forced", "no choice", "couldn't", "wasn't allowed", "agency"],
    "spotlight/ignored": ["ignored", "spotlight", "sidelined", "background", "left out", "barely", "not used"],
    "pacing": ["slow", "rushed", "pacing", "dragged", "too fast", "abrupt"],
    "unfair/punishing": ["unfair", "punish", "against me", "harsh", "cheap"],
    "dice/luck": ["dice", "luck", "roll", "failed"],
    "story/coherence": ["coheren", "disconnected", "random", "contrived", "didn't make sense"],
}


def cluster_complaints(texts: list[str]) -> dict:
    out = Counter()
    for t in texts:
        low = (t or "").lower()
        hit = False
        for b, kws in COMPLAINT_BUCKETS.items():
            if any(k in low for k in kws):
                out[b] += 1
                hit = True
        if not hit and low.strip():
            out["other"] += 1
    return dict(out.most_common())


def aggregate(runs: list[dict], seed: int = 0) -> dict:
    by_arm: dict[str, list[dict]] = defaultdict(list)
    for r in runs:
        if r["status"] == "complete":
            by_arm[r["arm"]].append(r)
    agg: dict = {"arms": {}, "status_counts": Counter(r["status"] for r in runs)}
    for arm, rs in sorted(by_arm.items()):
        ms = [r["metrics"] for r in rs]
        a: dict = {"runs": len(rs)}
        a["backstory_all_players_rate"] = mean_ci([1.0 if m["backstory_all_players"] else 0.0 for m in ms], seed)
        if arm.startswith("A") or arm.startswith("C"):
            a["deck_surfaced_all_players_rate"] = mean_ci([1.0 if m["deck_surfaced_all_players"] else 0.0 for m in ms
                                                           if m["deck_surfaced_all_players"] is not None], seed)
        for k in ("deck_draws", "fp_end_mean", "turn_gini", "invoke_gini", "clock_marks", "violations",
                  "violations_engine", "violations_referee", "ambiguities", "scenes", "compels_accepted",
                  "compels_refused", "gm_improvised_complications", "card_supplied_complications",
                  "improvisation_share", "draw_cost_used_card_rate_engine", "draw_cost_tag_in_text_rate",
                  "draw_cost_repaired", "elapsed_min", "cost_usd", "draw_cost_used_card_rate_referee",
                  "guarantee_failed", "involvement_var_within"):
            a[k] = mean_ci([m.get(k) for m in ms], seed)
        acc = sum(m["compels_accepted"] for m in ms)
        ref = sum(m["compels_refused"] for m in ms)
        a["compel_accept_ratio"] = round(acc / (acc + ref), 3) if acc + ref else None
        # FP flow per personality
        flow = defaultdict(lambda: {"earned": [], "spent": [], "end": []})
        for m in ms:
            for n, p in m["personality"].items():
                flow[p]["earned"].append(m["fp_earned"].get(n, 0))
                flow[p]["spent"].append(m["fp_spent"].get(n, 0))
                flow[p]["end"].append(m["fp_end"].get(n, 0))
        a["fp_flow_by_personality"] = {p: {k: round(st.mean(v), 2) for k, v in d.items()} for p, d in sorted(flow.items())}
        tens = [t for m in ms for t in m["tension_trajectory"] if t is not None]
        a["tension_distribution"] = dict(sorted(Counter(tens).items()))
        # Surveys (non-synthetic only)
        sv = [s for r in rs for s in r.get("surveys", []) if not s.get("synthetic")]
        a["survey"] = {k: mean_ci([s["scores"].get(k) for s in sv], seed) for k in SCORES}
        per_p = defaultdict(lambda: defaultdict(list))
        for s in sv:
            for k in SCORES:
                per_p[s["personality_id"]][k].append(s["scores"].get(k))
        a["survey_by_personality"] = {p: {k: mean_ci(v, seed) for k, v in d.items()} for p, d in sorted(per_p.items())}
        a["complaints"] = cluster_complaints([s["free_text"].get("most_frustrating", "") for s in sv])
        a["ambiguity_ids"] = dict(Counter(i for m in ms for i in m["ambiguity_ids"]).most_common())
        agg["arms"][arm] = a
    agg["paired"] = paired(runs, seed)
    return agg


def paired(runs: list[dict], seed: int = 0) -> dict:
    """Same seed + same seat (so same character and personality) across arms."""
    idx = {}
    for r in runs:
        if r["status"] != "complete":
            continue
        for s in r.get("surveys", []):
            if s.get("synthetic"):
                continue
            idx[(r["arm"], r["seed"], s["character_id"])] = s
    out = {}
    for a, b in (("A", "B"), ("A", "C"), ("C", "B")):
        res = {}
        for k in ("involvement", "connection", "fun", "control"):
            diffs, by_p = [], defaultdict(list)
            for (arm, sd, cid), s in idx.items():
                if arm != a or (b, sd, cid) not in idx:
                    continue
                other = idx[(b, sd, cid)]
                x, y = s["scores"].get(k), other["scores"].get(k)
                if isinstance(x, int) and isinstance(y, int):
                    diffs.append(x - y)
                    by_p[s["personality_id"]].append(x - y)
            res[k] = {"all": mean_ci(diffs, seed), "by_personality": {p: mean_ci(v, seed) for p, v in sorted(by_p.items())}}
        out[f"{a}-{b}"] = res
    # Lurker involvement across arms
    lurk = defaultdict(list)
    for (arm, sd, cid), s in idx.items():
        if s["personality_id"] == "lurker":
            lurk[arm].append(s["scores"].get("involvement"))
    out["lurker_involvement"] = {arm: mean_ci(v, seed) for arm, v in sorted(lurk.items())}
    return out


def load_preferences(batch_id: str) -> dict | None:
    p = ROOT / "runs" / batch_id / "_preferences.json"
    return json.loads(p.read_text()) if p.exists() else None


def preference_summary(prefs: dict | None) -> dict:
    if not prefs:
        return {}
    tally = defaultdict(lambda: Counter())
    for item in prefs.get("items", []):
        pair = f"{item['arm_x']}-{item['arm_y']}"
        tally[pair][item["preferred_arm"]] += 1
    return {pair: dict(c) for pair, c in tally.items()}


# ====================================================================== blind per-session judge
JUDGE_REDACT = re.compile(r"(?i)\b(session deck|beat frames?|decks?|cards?|tension|surfac\w*|rail|placebo|story piles?"
                          r"|weakness(?: tags?)?|power tags?|theme|binder|growth)\b"
                          r"|\b[A-Z]{1,3}-\d{2}(?:v\d+)?\b")
JUDGE_SCORES = ["overall", "engagement", "coherence", "spotlight_fairness", "player_agency", "complication_quality"]


def judge_view(rec: dict) -> str:
    """Story only: no mechanics lines, and no words or IDs that would reveal the rule set."""
    from agents import render_transcript
    entries = [t for t in rec["transcript"] if t["kind"] != "mechanics"]
    return JUDGE_REDACT.sub("[…]", render_transcript(entries, None, 40000))


def session_blinding(batch_id: str, runs: list[dict]) -> dict:
    """session id -> run_id. The judge only ever sees the session id."""
    import hashlib
    p = ROOT / "reports" / f"{batch_id}_session_blinding.json"
    mp = json.loads(p.read_text()) if p.exists() else {}
    known = set(mp.values())
    for r in runs:
        if r["run_id"] not in known:
            sid = "S-" + hashlib.sha256(f"{batch_id}:{r['run_id']}".encode()).hexdigest()[:8]
            mp[sid] = r["run_id"]
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(mp, indent=1, sort_keys=True))
    return mp


def judge_batch(batch_id: str, runs: list[dict], parallel: int = 8) -> dict:
    """Blind judge, one call per session, in isolation (no arm, no run id, no other sessions)."""
    from concurrent.futures import ThreadPoolExecutor
    from agents import JUDGE_SYSTEM, Agent
    from llm import LLMClient, TokenMeter
    from scripted import Scripted
    done_runs = [r for r in runs if r["status"] == "complete"]
    mp = session_blinding(batch_id, done_runs)
    by_run = {v: k for k, v in mp.items()}
    path = ROOT / "runs" / batch_id / "_judgments.json"
    judged = json.loads(path.read_text()) if path.exists() else {}
    todo = [r for r in done_runs if by_run[r["run_id"]] not in judged]
    backend = "scripted" if all(r["backend"] == "scripted" for r in done_runs) else "claude_cli"

    def one(r):
        sid = by_run[r["run_id"]]
        client = LLMClient(backend, cache_dir=ROOT / "cache" / batch_id / "_judge", run_id=f"judge-{sid}",
                           run_meter=TokenMeter(None), scripted=Scripted(seed=0, run_id=sid))
        names = [a["name"] for a in r["assignments"]]
        out = Agent(client, "judge", f"judge-{sid}", JUDGE_SYSTEM).ask("judge", (
            f"Session {sid}. Player characters: {', '.join(names)}.\n\n== Transcript ==\n{judge_view(r)}\n\n"
            "Score 1-10: overall (would you want to have been at this table?), engagement, coherence (does the story "
            "hang together), spotlight_fairness (did every player get meaningful moments?), player_agency (did player "
            "choices change what happened?), complication_quality (were the problems that arose interesting and "
            "fitting?). For EACH character: did their personal background (their past, people, places, oaths) visibly "
            "drive events? used true/false, score 1-10, one-line note. Then best_moment, worst_moment, notes."),
            {"names": names})
        return sid, {**out, "synthetic": backend == "scripted", "tokens": client.meter.as_dict()}
    with ThreadPoolExecutor(max_workers=parallel) as ex:
        for sid, out in ex.map(one, todo):
            judged[sid] = out
            path.write_text(json.dumps(judged, indent=1))
    return judged


def compile_judgments(batch_id: str, runs: list[dict], judged: dict, seed: int = 0) -> dict:
    """Unblind: join each session's judgment to its run, then aggregate per arm."""
    mp = session_blinding(batch_id, [r for r in runs if r["status"] == "complete"])
    recs = {r["run_id"]: r for r in runs}
    rows = defaultdict(list)
    for sid, jd in judged.items():
        r = recs.get(mp.get(sid))
        if r:
            rows[r["arm"]].append((r, jd))
    out = {}
    for arm, items in sorted(rows.items()):
        a = {"sessions": len(items), "synthetic": any(jd.get("synthetic") for _, jd in items)}
        for k in JUDGE_SCORES:
            a[k] = mean_ci([jd.get(k) for _, jd in items], seed)
        used, score, lurk = [], [], []
        for r, jd in items:
            pers = {x["name"]: x["personality_id"] for x in r["assignments"]}
            for b in jd.get("backstory", []):
                used.append(1.0 if b.get("used") else 0.0)
                score.append(b.get("score"))
                if pers.get(b.get("name")) == "lurker":
                    lurk.append(b.get("score"))
        a["backstory_used_rate"] = mean_ci(used, seed)
        a["backstory_score"] = mean_ci(score, seed)
        a["lurker_backstory_score"] = mean_ci(lurk, seed)
        a["all_players_backstory_used"] = mean_ci(
            [1.0 if jd.get("backstory") and all(b.get("used") for b in jd["backstory"]) else 0.0 for _, jd in items], seed)
        out[arm] = a
    return out


# ====================================================================== blinding + analyst
def blinding(batch_id: str, arms: list[str], seed: int) -> dict:
    p = ROOT / "reports" / f"{batch_id}_blinding.json"
    if p.exists():
        return json.loads(p.read_text())
    labels = [f"Arm {i+1}" for i in range(len(arms))]
    rng = random.Random(seed ^ 0xB11D)
    shuffled = list(arms)
    rng.shuffle(shuffled)
    mp = dict(zip(shuffled, labels))
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(mp, indent=1))
    return mp


def blind_obj(obj, mp: dict):
    s = json.dumps(obj)
    for real, lab in mp.items():
        s = re.sub(rf'"{re.escape(real)}"', f'"{lab}"', s)
        s = re.sub(rf'"{re.escape(real)}-', f'"{lab}-', s)
        s = re.sub(rf'-{re.escape(real)}"', f'-{lab}"', s)
    return json.loads(s)


def analyst_conclusions(blinded: dict, use_llm: bool, batch_id: str) -> dict:
    if not use_llm:
        return {"conclusions": "(Analyst agent not run: --no-llm)", "key_findings": [], "caveats": []}
    from agents import ANALYST_SYSTEM, Agent
    from llm import LLMClient, TokenMeter
    client = LLMClient("claude_cli", cache_dir=ROOT / "cache" / batch_id / "_analyst", run_id=f"{batch_id}-analyst",
                       run_meter=TokenMeter(None))
    agent = Agent(client, "analyst", "Analyst", ANALYST_SYSTEM)
    return agent.ask("analyst", "Blinded batch results (arms are labelled Arm 1/2/3; the mapping is hidden from you). "
                     "Survey scores are 1-7 self-reports from LLM player agents, which compress toward the top; weight "
                     "paired preferences and behavioural counts more heavily. With small n, say so.\n\n"
                     + json.dumps(blinded, indent=1))


# ====================================================================== report
def write_report(batch_id: str, runs: list[dict], agg: dict, prefs: dict, concl: dict, mp: dict) -> Path:
    L = [f"# Batch report: {batch_id}", ""]
    total_tokens = sum(r["tokens"]["prompt"] + r["tokens"]["completion"] for r in runs)
    cost = sum(r["tokens"].get("cost_usd", 0) for r in runs)
    L += [f"Runs: {len(runs)} ({dict(agg['status_counts'])}). Spec version(s): "
          f"{sorted({r['spec_version'] for r in runs})}. Backend(s): {sorted({r['backend'] for r in runs})}. "
          f"Tokens: {total_tokens:,} (≈ ${cost:.2f}).", ""]
    jc = agg.get("judge") or {}
    if jc:
        jarms = sorted(jc)
        L += ["## Blind per-session judge (compiled after unblinding)", "",
              "_Each session was scored alone by a judge that saw only the story (no mechanics lines, and no deck, card or "
              "tension vocabulary or card IDs) under a random session ID. Scores were joined to arms only afterwards._", "",
              "| Score (1–10) | " + " | ".join(f"{a} ({jc[a]['sessions']} sessions)" for a in jarms) + " |",
              "| --- |" + " --- |" * len(jarms)]
        for k in JUDGE_SCORES + ["backstory_score", "backstory_used_rate", "all_players_backstory_used",
                                 "lurker_backstory_score"]:
            L.append(f"| {k} | " + " | ".join(fmt_ci(jc[a][k]) for a in jarms) + " |")
        if any(jc[a]["synthetic"] for a in jarms):
            L.append("")
            L.append("_Synthetic (scripted backend): these judge scores are random placeholders._")
        L.append("")
    if concl.get("conclusions"):
        L += ["## Blinded analyst conclusions (optional)", "", concl.get("conclusions", ""), ""]
    for k in concl.get("key_findings", []):
        L.append(f"- {k}")
    if concl.get("caveats"):
        L += ["", "Caveats:"] + [f"- {c}" for c in concl["caveats"]]
    if mp:
        L += ["", "## Unblinding (analyst labels)", "", "| Blinded label | Arm |", "| --- | --- |"]
        L += [f"| {lab} | {real} |" for real, lab in sorted(mp.items(), key=lambda kv: kv[1])]
    arms = sorted(agg["arms"])
    L += ["", "## Structural metrics (per session, mean [95% bootstrap CI])", "",
          "| Metric | " + " | ".join(arms) + " |", "| --- |" + " --- |" * len(arms)]
    rows = [("Every player's backstory drove an event", "backstory_all_players_rate"),
            ("Every player's own card surfaced from the deck", "deck_surfaced_all_players_rate"),
            ("Deck draws / session (target 5–8)", "deck_draws"),
            ("Draw costs using the drawn card: engine tag check", "draw_cost_used_card_rate_engine"),
            ("Draw costs whose text uses the tag (after rewrite)", "draw_cost_tag_in_text_rate"),
            ("Draw costs that needed a GM rewrite", "draw_cost_repaired"),
            ("Draw costs using the drawn card: referee judgment", "draw_cost_used_card_rate_referee"),
            ("Minutes per session", "elapsed_min"), ("Cost per session (USD)", "cost_usd"),
            ("Mean player FP at session end (target 1–5)", "fp_end_mean"),
            ("Spotlight Gini: turns", "turn_gini"), ("Spotlight Gini: invokes", "invoke_gini"),
            ("Scenes / session", "scenes"), ("Clock marks", "clock_marks"),
            ("Compels accepted", "compels_accepted"), ("Compels refused", "compels_refused"),
            ("GM-improvised complications", "gm_improvised_complications"),
            ("Card-supplied complications", "card_supplied_complications"),
            ("Improvisation share", "improvisation_share"),
            ("Rule violations (engine + referee)", "violations"), ("  — engine refusals", "violations_engine"),
            ("  — referee", "violations_referee"), ("Ambiguity records", "ambiguities"),
            ("Backstory guarantee failures", "guarantee_failed"),
            ("Within-session variance of involvement", "involvement_var_within")]
    for label, k in rows:
        L.append(f"| {label} | " + " | ".join(fmt_ci(agg["arms"][a].get(k)) for a in arms) + " |")
    L.append("| Compel accept ratio | " + " | ".join(str(agg["arms"][a]["compel_accept_ratio"]) for a in arms) + " |")
    L.append("| Tension values seen | " + " | ".join(str(agg["arms"][a]["tension_distribution"]) for a in arms) + " |")
    L += ["", "## Experiential (LLM player self-reports, 1–7; weak evidence)", "",
          "| Score | " + " | ".join(arms) + " |", "| --- |" + " --- |" * len(arms)]
    for k in SCORES:
        L.append(f"| {k} | " + " | ".join(fmt_ci(agg["arms"][a]["survey"][k]) for a in arms) + " |")
    L += ["", "### Paired differences (same seed, same character and personality)", ""]
    for pair, res in agg["paired"].items():
        if pair == "lurker_involvement":
            continue
        L.append(f"- **{pair}**: " + "; ".join(f"{k} {fmt_ci(v['all'])}" for k, v in res.items()))
    L += ["", "Lurker involvement by arm: " + "; ".join(f"{a} {fmt_ci(c)}" for a, c in agg["paired"]["lurker_involvement"].items())]
    L += ["", "### Survey means by personality", ""]
    pers = sorted({p for a in arms for p in agg["arms"][a]["survey_by_personality"]})
    L += ["| Personality | " + " | ".join(f"{a} involvement" for a in arms) + " | " + " | ".join(f"{a} connection" for a in arms) + " |",
          "| --- |" + " --- |" * (2 * len(arms))]
    for p in pers:
        cells = [fmt_ci(agg["arms"][a]["survey_by_personality"].get(p, {}).get("involvement", {})) for a in arms]
        cells += [fmt_ci(agg["arms"][a]["survey_by_personality"].get(p, {}).get("connection", {})) for a in arms]
        L.append(f"| {p} | " + " | ".join(cells) + " |")
    L += ["", "### Paired transcript preference (blinded, same cohort and seed)", ""]
    if prefs:
        for pair, c in prefs.items():
            L.append(f"- {pair}: {c}")
    else:
        L.append("- not run")
    L += ["", "### Fate point flow by personality (mean per session: earned / spent / end)", ""]
    for a in arms:
        L.append(f"- **{a}**: " + "; ".join(f"{p} {d['earned']}/{d['spent']}/{d['end']}"
                                          for p, d in agg["arms"][a]["fp_flow_by_personality"].items()))
    L += ["", "### Complaint clusters (keyword buckets over 'most frustrating')", ""]
    for a in arms:
        L.append(f"- **{a}**: {agg['arms'][a]['complaints']}")
    L += ["", "## Ambiguities", ""]
    amb_all = Counter()
    amb_text = {}
    for r in runs:
        for x in r["referee"]["ambiguities"]:
            key = x.get("id") or f"REF {x.get('section', '?')}: {x.get('issue', '')[:90]}"
            amb_all[key] += 1
            amb_text[key] = (x.get("section", ""), x.get("issue", ""), x.get("interim_ruling", ""))
    L += ["| Count | ID / section | Issue | Interim ruling |", "| --- | --- | --- | --- |"]
    for key, n in amb_all.most_common(40):
        sec, iss, rul = amb_text[key]
        L.append(f"| {n} | {key if key.startswith('AMB') else sec} | {iss[:140]} | {rul[:140]} |")
    L += ["", "## Referee friction points (all runs)", ""]
    fr = Counter(f["text"][:160] for r in runs for f in r["referee"].get("friction", []))
    for t, n in fr.most_common(10):
        L.append(f"- ({n}×) {t}")
    L += ["", "## Player one-sentence verdicts on backstory use", ""]
    for r in runs:
        for s in r.get("surveys", []):
            if not s.get("synthetic"):
                L.append(f"- [{r['arm']} s{r['seed']}] {s['personality_id']}: {s['free_text'].get('one_sentence', '')}")
    L += ["", "## Run status", "", "| Run | Status | Scenes | Draws | Tokens | Error |", "| --- | --- | --- | --- | --- | --- |"]
    for r in runs:
        L.append(f"| {r['run_id']} | {r['status']} | {r['metrics'].get('scenes')} | {r['metrics'].get('deck_draws')} | "
                 f"{r['tokens']['prompt'] + r['tokens']['completion']:,} | {(r.get('error') or '')[:80].replace('|', '/')} |")
    out = ROOT / "reports" / f"{batch_id}.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(L) + "\n")
    return out


# ====================================================================== human review packet
def review_packet(batch_id: str, runs: list[dict], seed: int = 0) -> Path:
    """The blocking human gate: 5+ readable transcripts, arm labels hidden, answers in ANSWERS.txt."""
    d = ROOT / "reports" / f"{batch_id}_review"
    d.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed ^ 0x5EED)
    done = [r for r in runs if r["status"] == "complete"]
    score = lambda r: st.mean([st.mean(v for v in s["scores"].values() if isinstance(v, int))
                               for s in r.get("surveys", [])] or [0])
    picks: list[tuple[str, dict]] = []
    if done:
        ranked = sorted(done, key=score)
        picks += [("highest-rated", ranked[-1]), ("lowest-rated", ranked[0])]
        for arm in sorted({r["arm"] for r in done}):
            pool = [r for r in done if r["arm"] == arm and r not in [p[1] for p in picks]]
            if pool:
                picks.append(("random for its arm", rng.choice(pool)))
    flagged = [r for r in runs if r["referee"]["violations"] or r["status"] in ("invalid", "crashed", "failed")]
    for r in flagged:
        if r not in [p[1] for p in picks]:
            picks.append(("referee-flagged", r))
    rng.shuffle(picks)
    answers = []
    for i, (why, r) in enumerate(picks, 1):
        name = f"transcript_{i:02d}.md"
        L = [f"# Transcript {i}", "", f"Selected as: {why}. Status: {r['status']}.", "",
             "Characters: " + "; ".join(f"{a['name']} ({a['personality_id']})" for a in r["assignments"]), ""]
        cur = None
        for t in r["transcript"]:
            if t["scene"] != cur:
                cur = t["scene"]
                L += ["", f"## Scene {cur}", ""]
            if t["kind"] == "mechanics":
                L.append(f"> _{t['text']}_")
            elif t["speaker"] == "GM":
                L.append(f"**GM:** {t['text']}")
            else:
                L.append(f"**{t['speaker']}:** {t['text']}")
            L.append("")
        L += ["", "## Player feedback", ""]
        for s in r.get("surveys", []):
            L.append(f"- **{s['personality_id']}** scores {s['scores']}: best — {s['free_text'].get('best_moment', '')} | "
                     f"frustrating — {s['free_text'].get('most_frustrating', '')} | background — "
                     f"{s['free_text'].get('background_used', '')}")
        v = r["referee"]["violations"]
        if v:
            L += ["", "## Referee / engine violations", ""] + [f"- S{x.get('scene')} {x.get('section')}: {x.get('issue')}" for x in v[:30]]
        (d / name).write_text("\n".join(L) + "\n")
        mechanics = [t for t in r["transcript"] if t["kind"] == "mechanics"]
        answers.append(f"{name}: arm {r['arm']} | seed {r['seed']} | run {r['run_id']} | {why}")
    (d / "ANSWERS.txt").write_text("\n".join(answers) + "\n")
    (d / "README.md").write_text(
        f"# Human review packet: {batch_id}\n\nRead the transcripts before looking at ANSWERS.txt. For each, note: which "
        "rules variant you think it was, where the prose felt forced, unfair or flat, and whether each character's "
        "background mattered. Metrics hide tonal failures; this packet exists to catch them.\n\n"
        "**This is a blocking gate: no spec patches and no further batches until a human replies.**\n")
    return d


def main() -> None:
    ap = argparse.ArgumentParser(description="Analyze a batch.")
    ap.add_argument("batch_id")
    ap.add_argument("--no-llm", action="store_true", help="skip every LLM step (judge and analyst)")
    ap.add_argument("--analyst", action="store_true",
                    help="also run the blinded arm-label Analyst (not meaningful with unequal arm counts)")
    ap.add_argument("--review", action="store_true", help="also emit the human review packet")
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    runs = load_runs(a.batch_id)
    agg = aggregate(runs, a.seed)
    prefs = preference_summary(load_preferences(a.batch_id))
    arms = sorted(agg["arms"])
    judged = judge_batch(a.batch_id, runs) if not a.no_llm or all(r["backend"] == "scripted" for r in runs) else {}
    agg["judge"] = compile_judgments(a.batch_id, runs, judged, a.seed) if judged else {}
    mp, concl = {}, {}
    if a.analyst:
        mp = blinding(a.batch_id, arms, a.seed)
        blinded = blind_obj({"aggregate": agg["arms"], "paired": agg["paired"], "preferences": prefs}, mp)
        concl = analyst_conclusions(blinded, use_llm=not a.no_llm, batch_id=a.batch_id)
    (ROOT / "reports").mkdir(exist_ok=True)
    (ROOT / "reports" / f"{a.batch_id}_analyst.json").write_text(json.dumps(concl, indent=1))
    (ROOT / "reports" / f"{a.batch_id}_aggregate.json").write_text(json.dumps(agg, indent=1, default=str))
    out = write_report(a.batch_id, runs, agg, prefs, concl, mp)
    print(f"report: {out}")
    if a.review:
        print(f"review packet: {review_packet(a.batch_id, runs, a.seed)}")


if __name__ == "__main__":
    main()
