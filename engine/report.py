"""Sim report builder (Prompts Part 3.5). Evidence only, never fixes."""
from __future__ import annotations

import json
import time
from collections import Counter, defaultdict
from typing import Dict, List, Optional

from engine.items import ALL_ITEMS
from engine.stats import (bootstrap, holm, median, percentile, two_prop_z,
                          verdict, wilson)

ABIL = ("Q", "W", "E", "R")


def summarise(results: List[dict], spec: dict, tests: Optional[dict] = None,
              baseline: Optional[dict] = None) -> dict:
    n = len(results)
    champ_w: Dict[str, List[int]] = defaultdict(list)
    champ_ap: Dict[str, List[float]] = defaultdict(list)
    champ_uses: Dict[str, Counter] = defaultdict(Counter)
    champ_opp: Dict[str, Counter] = defaultdict(Counter)
    champ_kda: Dict[str, List[List[int]]] = defaultdict(list)
    champ_dead: Dict[str, List[int]] = defaultdict(list)
    champ_cd: Dict[str, List[int]] = defaultdict(list)
    champ_apshare: Dict[str, List[float]] = defaultdict(list)
    champ_items: Dict[str, Counter] = defaultdict(Counter)
    role_w: Dict[str, List[int]] = defaultdict(list)
    role_ap: Dict[str, List[float]] = defaultdict(list)
    item_games: Counter = Counter()
    item_win: Dict[str, List[int]] = defaultdict(list)
    item_nonwin: Dict[str, List[int]] = defaultdict(list)
    lengths: List[int] = []
    end_reasons: Counter = Counter()
    prio_wins = prio_games = 0
    north_wins = north_games = 0
    draws = 0
    ap_src: Counter = Counter()
    ap_use: Counter = Counter()
    team_rounds = 0
    obj_rounds: Dict[str, List[int]] = defaultdict(list)
    obj_secured_win: Dict[str, List[int]] = defaultdict(list)
    camp_cleared: Counter = Counter()
    first_tower_rounds: List[int] = []
    first_tower_win: List[int] = []
    anomalies: Counter = Counter()

    for r in results:
        w = r["winner"]
        lengths.append(r["rounds"])
        end_reasons[r["end_reason"]] += 1
        if w is None:
            draws += 1
        else:
            prio_games += 1
            prio_wins += 1 if w == r["first"] else 0
            north_games += 1
            north_wins += 1 if w == "north" else 0
        team_rounds += r["rounds"] * 2
        for team, src in r["team_ap_source"].items():
            for k, v in src.items():
                ap_src[k] += v
        for team, use in r["team_ap_spent"].items():
            for k, v in use.items():
                ap_use[k] += v
            ap_use["wasted"] += 0
        team_ap_total = {t: sum(v.values()) for t, v in r["team_ap_source"].items()}
        for uid, d in r["champ"].items():
            cid = d["cid"]
            win = None if w is None else int(d["team"] == w)
            if win is not None:
                champ_w[cid].append(win)
                role_w[d["role"]].append(win)
            champ_ap[cid].append(d["ap"] / max(1, r["rounds"]))
            role_ap[d["role"]].append(d["ap"] / max(1, r["rounds"]))
            for k in ("L0",) + ABIL:
                champ_uses[cid][k] += d["uses"][k]
                champ_opp[cid][k] += d["opp"][k]
            champ_kda[cid].append([d["kills"], d["deaths"], d.get("assists", 0)])
            champ_dead[cid].append(d["rounds_dead"])
            champ_cd[cid].append(d["rounds_cd"])
            champ_apshare[cid].append(d["ap"] / max(1, team_ap_total.get(d["team"], 1)))
            for it in d["items"]:
                champ_items[cid][it] += 1
                if win is not None:
                    item_win[it].append(win)
            if win is not None:
                for it in ALL_ITEMS:
                    if it not in d["items"]:
                        item_nonwin[it].append(win)
        for team, items in r["items"].items():
            for it in items:
                item_games[it] += 1
        for ev in r["objectives"]:
            mt = ev["mtype"]
            camp_cleared[mt] += 1
            if mt in ("dragon", "baron"):
                obj_rounds[mt].append(ev["round"])
                if w is not None:
                    obj_secured_win[mt].append(int(ev["team"] == w))
        if r["first_tower"]:
            rnd, team = r["first_tower"]
            first_tower_rounds.append(rnd)
            if w is not None:
                first_tower_win.append(int(team == w))
        for a in r["anomalies"]:
            anomalies[a.split("(")[0].strip()] += 1

    # ------------------------------------------------------------ scorecard
    cards = []
    champ_rows = []
    ap_means = {cid: sum(v) / len(v) for cid, v in champ_ap.items()}
    roster_ap_mean = sum(ap_means.values()) / max(1, len(ap_means))
    usage_rates = {}
    for cid in sorted(champ_w):
        wins = sum(champ_w[cid])
        games = len(champ_w[cid])
        p, lo, hi = wilson(wins, games)
        use = {}
        for k in ABIL:
            opp = champ_opp[cid][k]
            use[k] = None if opp == 0 else 100 * champ_uses[cid][k] / opp
        usage_rates[cid] = use
        champ_rows.append({
            "id": cid, "wr": p, "wr_lo": lo, "wr_hi": hi, "games": games,
            "ap_per_round": ap_means[cid],
            "ap_rel": ap_means[cid] / roster_ap_mean if roster_ap_mean else 0,
            "usage": use,
            "kills": sum(k for k, _, _ in champ_kda[cid]) / games,
            "deaths": sum(d for _, d, _ in champ_kda[cid]) / games,
            "rounds_dead": sum(champ_dead[cid]) / games,
            "rounds_cd": sum(champ_cd[cid]) / games,
            "ap_share": 100 * sum(champ_apshare[cid]) / games,
            "items": champ_items[cid].most_common(3),
        })

    wr_fail = [c for c in champ_rows if verdict(c["wr_lo"], c["wr_hi"], 45, 55) == "FAIL"]
    wr_inc = [c for c in champ_rows if verdict(c["wr_lo"], c["wr_hi"], 45, 55) == "INCONCLUSIVE"]
    cards.append({"check": "Champion win rate within 45-55%",
                  "value": f"{len(wr_fail)} FAIL / {len(wr_inc)} INCONCLUSIVE of {len(champ_rows)}",
                  "verdict": "PASS" if not wr_fail and not wr_inc else
                             ("FAIL" if wr_fail else "INCONCLUSIVE")})

    paid = [(cid, k, v) for cid, u in usage_rates.items() for k, v in u.items()
            if v is not None and _cost_of(spec, cid, k) > 0]
    off_band = [(cid, k, v) for cid, k, v in paid if not 40 <= v <= 70]
    mean_use = sum(v for _, _, v in paid) / max(1, len(paid))
    champ_means = {}
    for cid in usage_rates:
        vals = [v for k, v in usage_rates[cid].items()
                if v is not None and _cost_of(spec, cid, k) > 0]
        if vals:
            champ_means[cid] = sum(vals) / len(vals)
    far = [c for c, v in champ_means.items() if abs(v - mean_use) > 15]
    cards.append({"check": "AP-cost ability usage 40-70% of affordable rounds",
                  "value": f"{len(off_band)}/{len(paid)} abilities outside the band; "
                           f"roster mean {mean_use:.1f}%; {len(far)} champions >15pp from it",
                  "verdict": "PASS" if not off_band and not far else "FAIL"})

    pr_p, pr_lo, pr_hi = wilson(prio_wins, max(1, prio_games))
    cards.append({"check": "Priority (first player) win rate 48-52%",
                  "value": f"{pr_p:.1f}% [{pr_lo:.1f}, {pr_hi:.1f}]",
                  "verdict": verdict(pr_lo, pr_hi, 48, 52)})
    med, mlo, mhi = bootstrap(lengths, median)
    cards.append({"check": "Median game length 13-18 rounds",
                  "value": f"{med:.1f} [{mlo:.1f}, {mhi:.1f}]",
                  "verdict": verdict(mlo, mhi, 13, 18)})
    nexus = end_reasons["nexus"]
    p2, lo2, hi2 = wilson(nexus, n)
    cards.append({"check": ">=95% of games end by Nexus kill before round 20",
                  "value": f"{p2:.1f}% [{lo2:.1f}, {hi2:.1f}]",
                  "verdict": verdict(lo2, hi2, 95, 100)})
    econ_out = [c["id"] for c in champ_rows if c["ap_rel"] > 1.5]
    cards.append({"check": "No champion above 1.5x roster-mean AP per round",
                  "value": (", ".join(f"{c}" for c in econ_out) or "none") +
                           f" (roster mean {roster_ap_mean:.2f} AP/round)",
                  "verdict": "PASS" if not econ_out else "FAIL"})
    n_p, n_lo, n_hi = wilson(north_wins, max(1, north_games))
    cards.append({"check": "North vs South win rate 48-52%",
                  "value": f"north {n_p:.1f}% [{n_lo:.1f}, {n_hi:.1f}]",
                  "verdict": verdict(n_lo, n_hi, 48, 52)})

    role_rows = []
    for role in sorted(role_w):
        rp, rlo, rhi = wilson(sum(role_w[role]), len(role_w[role]))
        role_rows.append({"role": role, "wr": rp, "lo": rlo, "hi": rhi,
                          "ap_per_round": sum(role_ap[role]) / len(role_ap[role])})

    item_rows = []
    for it in sorted(ALL_ITEMS):
        owners = item_win.get(it, [])
        others = item_nonwin.get(it, [])
        owr = 100 * sum(owners) / len(owners) if owners else None
        nwr = 100 * sum(others) / len(others) if others else None
        item_rows.append({
            "item": it, "cost": ALL_ITEMS[it]["cost"],
            "purchases_per_game": item_games[it] / n,
            "owner_wr": owr, "non_owner_wr": nwr,
            "wr_diff": None if owr is None or nwr is None else owr - nwr,
        })

    flags = _top_flags(cards, champ_rows, usage_rates, spec, roster_ap_mean, anomalies)

    summary = {
        "header": {
            "batch_id": spec["batch_id"], "rules": spec["rules"], "roster": spec["roster"],
            "ai": spec["ai"], "games": n, "seed": spec["seed"],
            "matchup": {"p1": spec["p1"], "p2": spec["p2"],
                        "temperature": spec.get("temperature", 0.3)},
            "seat_swap": spec.get("seat_swap", True),
            "team_sampling": spec.get("team_sampling", "random_by_role_no_duplicates"),
            "runtime_s": spec.get("runtime_s"), "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
            "engine_tests": tests or {},
        },
        "scorecard": cards,
        "champions": champ_rows,
        "roles": role_rows,
        "game": {
            "length_median": med, "length_p10": percentile(lengths, 0.1),
            "length_p90": percentile(lengths, 0.9),
            "histogram": dict(sorted(Counter(lengths).items())),
            "end_reasons": dict(end_reasons), "draws": draws,
            "priority_wr": pr_p, "priority_ci": [pr_lo, pr_hi],
            "north_wr": n_p, "north_ci": [n_lo, n_hi],
        },
        "objectives": {
            "dragon_rounds_median": median(obj_rounds["dragon"]),
            "baron_rounds_median": median(obj_rounds["baron"]),
            "takes_per_game": {k: len(v) / n for k, v in obj_rounds.items()},
            "win_rate_if_secured": {
                k: (100 * sum(v) / len(v) if v else None)
                for k, v in obj_secured_win.items()},
            "camp_clears_per_game": {k: v / n for k, v in camp_cleared.items()},
        },
        "structures": {
            "first_tower_round_median": median(first_tower_rounds),
            "first_tower_round_p10": percentile(first_tower_rounds, 0.1),
            "first_tower_round_p90": percentile(first_tower_rounds, 0.9),
            "games_with_a_tower_down": len(first_tower_rounds) / n,
            "first_tower_wr": (100 * sum(first_tower_win) / len(first_tower_win)
                               if first_tower_win else None),
        },
        "economy": {
            "ap_per_team_round_by_source": {k: v / max(1, team_rounds) for k, v in ap_src.items()},
            "ap_per_team_round_by_use": {k: v / max(1, team_rounds) for k, v in ap_use.items()},
            "roster_mean_ap_per_round": roster_ap_mean,
        },
        "items": item_rows,
        "anomalies": dict(anomalies),
        "top_flags": flags,
    }
    if baseline:
        summary["delta"] = _delta(summary, baseline)
    return summary


def _cost_of(spec: dict, cid: str, key: str) -> int:
    return spec.get("costs", {}).get(cid, {}).get(key, 1)


def _top_flags(cards, champ_rows, usage, spec, ap_mean, anomalies) -> List[dict]:
    flags = []
    for c in champ_rows:
        if c["wr_lo"] > 55 or c["wr_hi"] < 45:
            flags.append({"severity": abs(c["wr"] - 50), "flag": f"champion win rate: {c['id']}",
                          "evidence": f"WR {c['wr']:.1f}% [{c['wr_lo']:.1f}, {c['wr_hi']:.1f}]"})
        if c["ap_rel"] > 1.5:
            flags.append({"severity": 20 * (c["ap_rel"] - 1.5),
                          "flag": f"economy outlier: {c['id']}",
                          "evidence": f"{c['ap_per_round']:.2f} AP/round = {c['ap_rel']:.2f}x roster mean"})
    for cid, u in usage.items():
        for k, v in u.items():
            if v is None or _cost_of(spec, cid, k) == 0:
                continue
            if not 40 <= v <= 70:
                flags.append({"severity": min(30, abs(v - 55)) / 2,
                              "flag": f"ability usage: {cid}.{k}",
                              "evidence": f"used in {v:.1f}% of affordable rounds with a legal target"})
    for card in cards:
        if card["verdict"] == "FAIL" and card["check"].startswith((">=95", "Median", "Priority", "North")):
            flags.append({"severity": 25, "flag": card["check"], "evidence": card["value"]})
    for a, cnt in anomalies.items():
        flags.append({"severity": 40, "flag": f"anomaly: {a}", "evidence": f"{cnt} games"})
    flags.sort(key=lambda f: -f["severity"])
    return flags[:5]


def _delta(cur: dict, base: dict) -> dict:
    out = {"baseline": base["header"]["batch_id"], "champions": {}, "game": {}}
    bmap = {c["id"]: c for c in base["champions"]}
    pvals = {}
    for c in cur["champions"]:
        b = bmap.get(c["id"])
        if not b:
            continue
        k1, n1 = round(c["wr"] * c["games"] / 100), c["games"]
        k2, n2 = round(b["wr"] * b["games"] / 100), b["games"]
        pvals[c["id"]] = two_prop_z(k1, n1, k2, n2)
        out["champions"][c["id"]] = {"wr_delta": c["wr"] - b["wr"],
                                     "ap_delta": c["ap_per_round"] - b["ap_per_round"]}
    sig = holm(pvals)
    for cid, d in out["champions"].items():
        d["significant_holm"] = sig.get(cid, False)
    out["game"] = {
        "length_median_delta": cur["game"]["length_median"] - base["game"]["length_median"],
        "nexus_rate_delta": (cur["game"]["end_reasons"].get("nexus", 0) / max(1, cur["header"]["games"])
                             - base["game"]["end_reasons"].get("nexus", 0) / max(1, base["header"]["games"])) * 100,
    }
    return out


def _pct(v):
    return "-" if v is None else f"{v:.1f}%"


# ------------------------------------------------------------------ markdown
def to_markdown(s: dict) -> str:
    h = s["header"]
    L = [f"# Sim report {h['batch_id']}", ""]
    L += ["## 1. Header", "",
          f"| field | value |", "|---|---|",
          f"| rules | {h['rules']} |", f"| roster | {h['roster']} |", f"| ai | {h['ai']} |",
          f"| matchup | {h['matchup']['p1']} vs {h['matchup']['p2']} (temperature {h['matchup']['temperature']}) |",
          f"| games | {h['games']} |", f"| seed | {h['seed']} |",
          f"| seat swap | {h['seat_swap']} |", f"| team sampling | {h['team_sampling']} |",
          f"| runtime | {h.get('runtime_s', 0):.1f}s |",
          f"| engine tests | {h['engine_tests'].get('summary', 'not run')} |",
          f"| generated | {h['generated']} |", ""]
    L += ["## 2. Balance scorecard", "", "| check | value | verdict |", "|---|---|---|"]
    for c in s["scorecard"]:
        L.append(f"| {c['check']} | {c['value']} | **{c['verdict']}** |")
    L += ["", "## 3. Champions", "",
          "| champion | WR% [95% CI] | games | AP/round | xmean | Q | W | E | R | K | D | dead | on CD | AP share | top items |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in sorted(s["champions"], key=lambda x: -x["wr"]):
        u = c["usage"]
        us = [f"{u[k]:.0f}%" if u[k] is not None else "-" for k in ABIL]
        items = ", ".join(f"{i}x{n}" for i, n in c["items"]) or "-"
        L.append(f"| {c['id']} | {c['wr']:.1f} [{c['wr_lo']:.1f}, {c['wr_hi']:.1f}] | {c['games']} | "
                 f"{c['ap_per_round']:.2f} | {c['ap_rel']:.2f} | " + " | ".join(us) +
                 f" | {c['kills']:.2f} | {c['deaths']:.2f} | {c['rounds_dead']:.1f} | "
                 f"{c['rounds_cd']:.1f} | {c['ap_share']:.0f}% | {items} |")
    L += ["", "## 4. Roles", "",
          "Under `random_by_role_no_duplicates` both teams field exactly one champion "
          "of each role, so role win rate is 50% by construction. Read the AP column, "
          "and read win rates from the champion table.", "",
          "| role | WR% [95% CI] | AP/round |", "|---|---|---|"]
    for r in s["roles"]:
        L.append(f"| {r['role']} | {r['wr']:.1f} [{r['lo']:.1f}, {r['hi']:.1f}] | {r['ap_per_round']:.2f} |")
    g = s["game"]
    L += ["", "## 5. Games", "",
          f"- length: median {g['length_median']:.1f}, p10 {g['length_p10']:.0f}, p90 {g['length_p90']:.0f}",
          f"- end reasons: {g['end_reasons']} (draws {g['draws']})",
          f"- priority win rate: {g['priority_wr']:.1f}% [{g['priority_ci'][0]:.1f}, {g['priority_ci'][1]:.1f}]",
          f"- north win rate: {g['north_wr']:.1f}% [{g['north_ci'][0]:.1f}, {g['north_ci'][1]:.1f}]",
          f"- length histogram: {g['histogram']}", ""]
    o = s["objectives"]
    L += ["## 6. Objectives", "",
          f"- takes per game: {o['takes_per_game']}",
          f"- median round taken: dragon {o['dragon_rounds_median']}, baron {o['baron_rounds_median']}",
          f"- win rate when secured: {o['win_rate_if_secured']}",
          f"- camp clears per game: {o['camp_clears_per_game']}", ""]
    st = s["structures"]
    L += ["## 7. Structures", "",
          f"- first tower falls: median round {st['first_tower_round_median']}, "
          f"p10 {st['first_tower_round_p10']}, p90 {st['first_tower_round_p90']}",
          f"- games with at least one tower down: {100 * st['games_with_a_tower_down']:.1f}%",
          f"- first-tower win rate: {_pct(st['first_tower_wr'])}", ""]
    e = s["economy"]
    L += ["## 8. Economy (AP per team-round)", "", "| source | AP |", "|---|---|"]
    for k, v in sorted(e["ap_per_team_round_by_source"].items(), key=lambda kv: -kv[1]):
        L.append(f"| {k} | {v:.2f} |")
    L += ["", "| use | AP |", "|---|---|"]
    for k, v in sorted(e["ap_per_team_round_by_use"].items(), key=lambda kv: -kv[1]):
        L.append(f"| {k} | {v:.2f} |")
    L += ["", "## 9. Items", "",
          "| item | cost | purchases/game | owner WR | non-owner WR | diff |", "|---|---|---|---|---|---|"]
    for i in s["items"]:
        ow = "-" if i["owner_wr"] is None else f"{i['owner_wr']:.1f}%"
        nw = "-" if i["non_owner_wr"] is None else f"{i['non_owner_wr']:.1f}%"
        df = "-" if i["wr_diff"] is None else f"{i['wr_diff']:+.1f}"
        L.append(f"| {i['item']} | {i['cost']} | {i['purchases_per_game']:.2f} | {ow} | {nw} | {df} |")
    L += ["", "## 10. Anomalies", ""]
    L.append("None." if not s["anomalies"] else
             "\n".join(f"- {k}: {v} games" for k, v in s["anomalies"].items()))
    L += ["", "## 11. Top 5 flags (evidence only)", ""]
    if not s["top_flags"]:
        L.append("None.")
    for i, f in enumerate(s["top_flags"], 1):
        L.append(f"{i}. **{f['flag']}** - {f['evidence']}")
    if "delta" in s:
        L += ["", f"## 12. Delta vs {s['delta']['baseline']}", "",
              "| champion | WR delta | AP/round delta | significant (Holm) |", "|---|---|---|---|"]
        for cid, d in sorted(s["delta"]["champions"].items()):
            L.append(f"| {cid} | {d['wr_delta']:+.1f} | {d['ap_delta']:+.2f} | "
                     f"{'yes' if d['significant_holm'] else 'no'} |")
        L += ["", f"- median length delta: {s['delta']['game']['length_median_delta']:+.1f}",
              f"- nexus-kill rate delta: {s['delta']['game']['nexus_rate_delta']:+.1f} pts"]
    L.append("")
    return "\n".join(L)
