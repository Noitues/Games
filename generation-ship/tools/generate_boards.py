"""Generate asymmetric ship boards (data/boards.json) from hand-placed seeds.

Each board is a convex outline: a curved Outer Hull edge on top (its bulge differs per board),
vertical joining edges on the left/right (shared height, so boards chain A-B-C-D), and the
spine along the bottom. Sections are Voronoi cells of the seeds clipped to the outline, so
shapes, neighbor counts and the number of Hull sections all differ between boards.
Adjacency, Hull membership and inter-board links come from the geometry.

    python3 tools/generate_boards.py
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W, H, EDGE_TOP = 420.0, 280.0, 60.0          # board size; side edges run from y=EDGE_TOP to y=H
I, R, G, A = "Infrastructure", "Residential", "Government", "Agricultural"

# Per board: hull bulge (how far the hull curve rises above EDGE_TOP), and 8 seeds (x, y, type).
# Outline shape per board: hull bulge, spine bulge (downward), and corner tapers at the bottom-left/right.
BOARDS = {
    "A": {"bulge": 50, "spine": 22, "taper": (70, 0), "seeds": [
        (60, 70, I), (180, 40, R), (320, 55, A),               # 3 hull
        (40, 200, G), (150, 160, A), (260, 150, I), (380, 190, G), (200, 250, R)]},
    "B": {"bulge": 20, "spine": 0, "taper": (0, 40), "seeds": [
        (50, 90, R), (150, 75, G), (260, 70, I), (370, 85, A),   # 4 hull
        (90, 220, A), (210, 180, I), (330, 230, R), (390, 160, G)]},
    "C": {"bulge": 70, "spine": 34, "taper": (30, 0), "seeds": [
        (130, 30, A), (300, 45, I),                             # 2 hull
        (40, 175, G), (180, 140, R), (330, 160, G), (90, 245, I), (240, 240, A), (390, 250, R)]},
    "D": {"bulge": 35, "spine": 12, "taper": (0, 90), "seeds": [
        (70, 85, G), (210, 40, A), (360, 80, I),                # 3 hull
        (30, 230, I), (140, 180, R), (250, 190, R), (350, 240, A), (160, 260, G)]},
}

# Setup per board (as in Spirit Island, each board prints its own): 1 Failure, 2 Faults and
# 1 Glitch in four different section types, rotated between boards; Decay next to the Failure;
# 6 Crew (2, 2, 1, 1) in sections away from the Failure and the Decay.
SETUP_PLAN = {"A": (I, [R, G], A), "B": (R, [G, A], I), "C": (G, [A, I], R), "D": (A, [I, R], G)}


# Per-board setup extras that offset geometry (board C has only 2 Hull sections, so it is seeded
# less; it starts with an extra Fault on its largest Hull section).
BOARD_EXTRA = {"C": [("fault", "hull")]}


def outline(bulge, spine=0, taper=(0, 0), steps=10):
    """Convex outline, clockwise from the bottom of the west edge. Returns points and a label per segment.
    The bottom corners are cut by `taper` (bow/stern narrowing) and the spine bulges down by `spine`."""
    tl, tr = taper
    pts, labels = [(0.0, H - tl), (0.0, EDGE_TOP)], ["west"]
    for k in range(1, steps):
        t = k / steps
        pts.append((W * t, EDGE_TOP - bulge * math.sin(math.pi * t))); labels.append("hull")
    pts.append((W, EDGE_TOP)); labels.append("hull")
    pts.append((W, H - tr)); labels.append("east")
    # spine: from the east taper back to the west taper, bulging downward
    x0, x1 = W - tr * 0.8, tr * 0 + tl * 0.8
    if tr: pts.append((x0, H)); labels.append("spine")
    for k in range(1, steps):
        t = k / steps
        x = x0 + (x1 - x0) * t
        pts.append((x, H + spine * math.sin(math.pi * t))); labels.append("spine")
    if tl: pts.append((x1, H)); labels.append("spine")
    labels.append("spine")  # closing segment back to (0, H - tl)
    return pts, labels


# Smooth warp field over the whole ship (global x = board index * W + x), so shared borders and the
# seams between boards bend identically on both sides.
def warp(gx, y):
    dx = 9 * math.sin(gx / 61 + 1.3) * math.cos(y / 47 + 0.4) + 3.5 * math.sin(gx / 17 + y / 23)
    dy = 9 * math.cos(gx / 53 + 2.1) * math.sin(y / 59 + 0.9) + 3.5 * math.cos(gx / 19 - y / 21)
    edge = 1.0 + max(0.0, (EDGE_TOP + 20 - y) / 60)   # rougher along the hull
    return gx + dx * edge, y + dy * edge


def densify_warp(poly, gx0, step=5.0):
    """Subdivide each edge in a canonical direction (so neighbors get identical points) and warp it."""
    out = []
    n = len(poly)
    for i in range(n):
        p, q = poly[i], poly[(i + 1) % n]
        a, b = (p, q) if (round(p[0], 1), round(p[1], 1)) <= (round(q[0], 1), round(q[1], 1)) else (q, p)
        k = max(1, int(math.dist(a, b) / step))
        seg = [(a[0] + (b[0] - a[0]) * j / k, a[1] + (b[1] - a[1]) * j / k) for j in range(k + 1)]
        if (a, b) != (p, q):
            seg.reverse()
        for (x, y) in seg[:-1]:
            wx, wy = warp(gx0 + x, y)
            out.append((wx - gx0, wy))
    return out


def clip(poly, a, b, c):
    """Keep the part of poly where a*x + b*y <= c (Sutherland-Hodgman, one half-plane)."""
    out = []
    n = len(poly)
    for i in range(n):
        p, q = poly[i], poly[(i + 1) % n]
        fp, fq = a * p[0] + b * p[1] - c, a * q[0] + b * q[1] - c
        if fp <= 0:
            out.append(p)
        if (fp < 0 < fq) or (fq < 0 < fp):
            t = fp / (fp - fq)
            out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out


def cell(seeds, i, outl):
    poly = list(outl)
    xi, yi = seeds[i][0], seeds[i][1]
    for j, (xj, yj, _) in enumerate(seeds):
        if j == i:
            continue
        # |p - si|^2 <= |p - sj|^2  <=>  2(sj - si).p <= |sj|^2 - |si|^2
        poly = clip(poly, 2 * (xj - xi), 2 * (yj - yi), xj * xj + yj * yj - xi * xi - yi * yi)
    return poly


def on_segment(p, a, b, eps=0.5):
    cross = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
    if abs(cross) > eps * math.dist(a, b):
        return False
    return min(a[0], b[0]) - eps <= p[0] <= max(a[0], b[0]) + eps and min(a[1], b[1]) - eps <= p[1] <= max(a[1], b[1]) + eps


def boundary_length(poly, outl, labels, want):
    """Length of the cell's edges lying on outline segments labelled `want`."""
    total = 0.0
    n = len(poly)
    for k in range(n):
        p, q = poly[k], poly[(k + 1) % n]
        for s in range(len(outl)):
            if labels[s] != want:
                continue
            a, b = outl[s], outl[(s + 1) % len(outl)]
            if on_segment(p, a, b) and on_segment(q, a, b):
                total += math.dist(p, q)
                break
    return total


def side_interval(poly, x):
    ys = [p[1] for p in poly if abs(p[0] - x) < 0.5]
    return (min(ys), max(ys)) if len(ys) >= 2 else None


def build_board(bid, spec, index):
    outl, labels = outline(spec["bulge"], spec.get("spine", 0), spec.get("taper", (0, 0)))
    seeds = spec["seeds"]
    cells = [cell(seeds, i, outl) for i in range(len(seeds))]
    sections = []
    for i, (x, y, t) in enumerate(seeds):
        cx = sum(p[0] for p in cells[i]) / len(cells[i]); cy = sum(p[1] for p in cells[i]) / len(cells[i])
        wcx, wcy = warp(index * W + cx, cy)
        sections.append({"id": f"{bid}{i + 1}", "type": t,
                         "hull": boundary_length(cells[i], outl, labels, "hull") > 25,
                         "poly": [[round(px, 1), round(py, 1)] for px, py in densify_warp(cells[i], index * W)],
                         "center": [round(wcx - index * W, 1), round(wcy, 1)],
                         "west": side_interval(cells[i], 0.0), "east": side_interval(cells[i], W),
                         "adjacent": []})
    # adjacency: cells sharing a bisector edge longer than 8 units
    for i in range(len(seeds)):
        for j in range(i + 1, len(seeds)):
            xi, yi, _ = seeds[i]; xj, yj, _ = seeds[j]
            on = [p for p in cells[i] if abs(math.dist(p, (xi, yi)) - math.dist(p, (xj, yj))) < 0.6]
            if len(on) >= 2 and max(math.dist(a, b) for a in on for b in on) > 8:
                sections[i]["adjacent"].append(sections[j]["id"])
                sections[j]["adjacent"].append(sections[i]["id"])
    for s in sections:
        s["adjacent"].sort()
    apply_setup(bid, sections)
    return {"id": bid, "outline": [[round(x, 1), round(y, 1)] for x, y in densify_warp(outl, index * W)], "sections": sections}


def apply_setup(bid, secs):
    for s in secs:
        s["setup"] = {k: 0 for k in ("glitch", "fault", "failure", "crew", "decay")}
    by_type = lambda t, hull=None: [s for s in secs if s["type"] == t and (hull is None or s["hull"] == hull)]
    fail_t, fault_ts, gl_t = SETUP_PLAN[bid]
    fs = (by_type(fail_t, False) or by_type(fail_t))[0]
    fs["setup"]["failure"] = 1
    for k, t in enumerate(fault_ts):
        (by_type(t, k == 0) or by_type(t))[0]["setup"]["fault"] += 1
    (by_type(gl_t, True) or by_type(gl_t))[0]["setup"]["glitch"] += 1
    ids = {s["id"]: s for s in secs}
    threat = lambda s: s["setup"]["glitch"] + s["setup"]["fault"] + s["setup"]["failure"]
    cand = [ids[a] for a in fs["adjacent"] if threat(ids[a]) == 0] or [ids[a] for a in fs["adjacent"]]
    cand[0]["setup"]["decay"] = 1
    crewable = [s for s in secs if not s["setup"]["failure"] and not s["setup"]["decay"]]
    crewable.sort(key=lambda s: (threat(s), s["hull"], s["id"]))
    for s, n in zip(crewable[:4], [2, 2, 1, 1]):
        s["setup"]["crew"] = n
    for piece, where in BOARD_EXTRA.get(bid, []):
        pool = [s for s in secs if s["hull"]] if where == "hull" else secs
        pool.sort(key=lambda s: -area(s["poly"]))
        pool[0]["setup"][piece] += 1


def area(poly):
    return abs(sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1] for i in range(len(poly)))) / 2


def main():
    boards = [build_board(b, spec, i) for i, (b, spec) in enumerate(BOARDS.items())]
    # links between consecutive boards: east-edge cells of one meet west-edge cells of the next
    links = {}
    for left, right in zip(boards, boards[1:]):
        pairs = []
        for a in left["sections"]:
            for b in right["sections"]:
                if a["east"] and b["west"]:
                    lo, hi = max(a["east"][0], b["west"][0]), min(a["east"][1], b["west"][1])
                    if hi - lo > 10:
                        pairs.append([a["id"], b["id"]])
        links[f"{left['id']}-{right['id']}"] = pairs
    for b in boards:
        for s in b["sections"]:
            s.pop("west"); s.pop("east")
    out = {
        "layout": "Asymmetric boards: each section is a polygon (board coordinates, 420 x 280). The curved top edge is the Outer Hull; boards chain A-B-C-D along their side edges, joined by `links`.",
        "size": [W, H], "players_use": "Players 1-4 use boards A, A-B, A-B-C, A-B-C-D.",
        "setup_rule": "Per board: 1 Failure, 2 Faults and 1 Glitch, each in a different section type (rotated between boards), 1 Decay next to the Failure, 6 Crew (2,2,1,1) across 4 sections away from the Failure and Decay. Board C (2 Hull sections) adds 1 Fault on its largest Hull section.",
        "boards": boards, "links": links}
    (ROOT / "data" / "boards.json").write_text(json.dumps(out, indent=1))
    for b in boards:
        hull = sum(s["hull"] for s in b["sections"])
        deg = sorted(len(s["adjacent"]) for s in b["sections"])
        print(b["id"], "hull", hull, "neighbors", deg, "types", sorted(s["type"][:3] for s in b["sections"] if s["hull"]))
    print("links", {k: len(v) for k, v in links.items()})


if __name__ == "__main__":
    main()
