"""Choose a smaller people deck for physical playtests (data/playtest_deck.json).

The full deck is 400 cards (about 45 printed sheets). The playtest deck keeps the full deck's shape:
- the same cost curve, scaled down (120 Commons, 30 Remarkables);
- guilds as even as possible (thresholds and innates depend on them);
- no weak outliers: the fifth of each cost that the bots play least is left out (strong cards stay:
  dropping the top 5 % made the deck 9 points harder)
  (data/card_stats.json from sim/cards.js);
- a spread of effect types (every verb that appears in the full deck stays represented).

    python3 tools/playtest_deck.py [--commons 120] [--remarkables 30]
Deterministic: the same data gives the same deck.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUILDS = ["Engineers", "Medics", "Keepers", "Scholars", "Laborers", "Farmers", "Navigators", "Bureaucrats"]


def quotas(cards, total):
    """Cost buckets scaled to `total` (largest remainders)."""
    by = Counter(c["cost"] for c in cards)
    raw = {k: v * total / len(cards) for k, v in by.items()}
    q = {k: int(v) for k, v in raw.items()}
    for k in sorted(raw, key=lambda k: raw[k] - q[k], reverse=True)[: total - sum(q.values())]:
        q[k] += 1
    return q


def verbs(c):
    v = set(c["effects"]) | set((c.get("threshold") or {}).get("effects", {}))
    return v


def choose(cards, total, pick):
    q = quotas(cards, total)
    chosen, guild = [], Counter()
    all_verbs = set().union(*(verbs(c) for c in cards))
    for cost in sorted(q):
        bucket = [c for c in cards if c["cost"] == cost]
        rates = sorted(pick.get(c["id"], 0) for c in bucket)
        lo, hi = rates[len(rates) // 5], rates[-1]   # drop the least-played fifth; keep the strong cards
        mid = rates[len(rates) // 2]
        pool = [c for c in bucket if lo <= pick.get(c["id"], 0) <= hi] or bucket
        for _ in range(q[cost]):
            # prefer the card that most evens out the guild counts, then a typical pick rate
            def score(c):
                after = guild + Counter(c["guilds"])
                spread = max(after[g] for g in GUILDS) - min(after[g] for g in GUILDS)
                return (spread, abs(pick.get(c["id"], 0) - mid), c["id"])
            best = min((c for c in pool if c not in chosen), key=score)
            chosen.append(best)
            guild.update(best["guilds"])
    # keep every effect type represented: swap in a card for any verb that dropped out
    have = set().union(*(verbs(c) for c in chosen))
    for v in sorted(all_verbs - have):
        cand = next((c for c in cards if v in verbs(c) and c not in chosen), None)
        if not cand:
            continue
        same = [c for c in chosen if c["cost"] == cand["cost"] and not (verbs(c) - set().union(*(verbs(x) for x in chosen if x is not c)))]
        if same:
            chosen[chosen.index(same[0])] = cand
    return sorted(chosen, key=lambda c: c["id"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commons", type=int, default=120)
    ap.add_argument("--remarkables", type=int, default=30)
    a = ap.parse_args()
    people = json.loads((ROOT / "data" / "people.json").read_text())
    stats = json.loads((ROOT / "data" / "card_stats.json").read_text())
    pick = {r["id"]: r["pick"] for r in stats.get("rows", [])}
    com = choose([c for c in people if c["tier"] == "Common"], a.commons, pick)
    rem = choose([c for c in people if c["tier"] == "Remarkable"], a.remarkables, pick)
    out = {"about": "Curated people deck for physical playtests (tools/playtest_deck.py). Use it with the "
                    "game option peopleDeck = common + remarkable.",
           "common": [c["id"] for c in com], "remarkable": [c["id"] for c in rem]}
    (ROOT / "data" / "playtest_deck.json").write_text(json.dumps(out, indent=1))
    for name, deck in (("Common", com), ("Remarkable", rem)):
        g = Counter(x for c in deck for x in c["guilds"])
        print(f"{name}: {len(deck)} cards | cost {dict(sorted(Counter(c['cost'] for c in deck).items()))} | "
              f"guilds {min(g.values())}-{max(g.values())} | thresholds {sum('threshold' in c for c in deck)}")


if __name__ == "__main__":
    main()
