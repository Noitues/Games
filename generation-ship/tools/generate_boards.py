"""Generate the ship boards and their layouts (data/boards.json).

Every board has the SAME outline, like Spirit Island: a hexagonal hull module (flat-top hexagon).
  - Side 4 (the top) is the Outer Hull, facing the void: a faceted profile with two fins.
  - Sides 0, 1, 2, 3, 5 are docking sides. Each carries the same angular tab-and-slot profile,
    which is point-symmetric, so any docking side mates with any other docking side.
Interiors differ per board: 8 sections from hand-placed Voronoi seeds, internal borders bent
with one angular kink each (shared by both neighbors). Layouts place 1-4 boards on a hex grid
with rotations chosen so every Hull side faces the void; docking links between sections are
computed from where their borders overlap along a shared side.

    python3 tools/generate_boards.py
"""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
R = 180.0                                   # circumradius = side length
HULL = 4                                    # side index of the Outer Hull
I, Rs, G, A = "Infrastructure", "Residential", "Government", "Agricultural"
VERTS = [(R * math.cos(math.radians(60 * k)), R * math.sin(math.radians(60 * k))) for k in range(6)]
# side k runs from VERTS[k] to VERTS[k+1]; outward normal at angle 30 + 60k (SVG y-down: side 4 is the top)

# Profiles: (t, outward offset) breakpoints along a side, t in [0, 1].
DOCK = [(0, 0), (0.13, 0), (0.17, 22), (0.21, 24), (0.29, 24), (0.33, 22), (0.37, 0),
        (0.63, 0), (0.67, -22), (0.71, -24), (0.79, -24), (0.83, -22), (0.87, 0), (1, 0)]   # dovetail clamp + socket
HULL_PROFILE = [(0, 0), (0.05, 12), (0.13, 18), (0.155, 58), (0.175, 58), (0.2, 20), (0.3, 26), (0.36, 42),
                (0.45, 46), (0.5, 66), (0.55, 46), (0.64, 42), (0.7, 26), (0.8, 20), (0.825, 58), (0.845, 58),
                (0.87, 18), (0.95, 12), (1, 0)]   # armor plating, prow and two fins

# Seeds per board (x, y, type) in local coordinates (hexagon centred on 0,0; hull at the top).
BOARDS = {
    "A": [(-95, -120, I), (0, -135, Rs), (95, -120, A),
          (-120, 10, G), (-35, -35, A), (60, -20, I), (130, 30, G), (0, 105, Rs)],
    "B": [(-60, -125, Rs), (60, -125, G),
          (-140, -20, A), (-50, 20, I), (40, -40, I), (140, -5, A), (-40, 120, Rs), (80, 95, G)],
    "C": [(-110, -115, A), (-15, -130, I), (70, -110, Rs), (130, -90, G),
          (-70, 30, G), (40, 10, A), (-10, 120, I), (110, 90, Rs)],
    "D": [(-75, -120, G), (75, -120, A),
          (0, -40, I), (-140, 15, Rs), (140, 15, I), (-60, 105, A), (60, 105, Rs), (0, 150, G)],
}
SETUP_PLAN = {"A": (I, [Rs, G], A), "B": (Rs, [G, A], I), "C": (G, [A, I], Rs), "D": (A, [I, Rs], G)}

# Layouts: board -> hex-grid cell centre. Rotations are chosen automatically.
STEP = math.sqrt(3) * R
DIRS = {d: (STEP * math.cos(math.radians(d)), STEP * math.sin(math.radians(d))) for d in (30, 90, 150, 210, 270, 330)}


def walk(*steps):
    x = y = 0.0
    for d in steps:
        x += DIRS[d][0]; y += DIRS[d][1]
    return (x, y)


LAYOUTS = {
    "solo":    {"A": walk()},
    "pair":    {"A": walk(), "B": walk(330)},
    "line3":   {"A": walk(), "B": walk(330), "C": walk(330, 330)},
    "triad":   {"A": walk(), "B": walk(330), "C": walk(30)},
    "arc3":    {"A": walk(), "B": walk(330), "C": walk(330, 30)},
    "line4":   {"A": walk(), "B": walk(330), "C": walk(330, 330), "D": walk(330, 330, 330)},
    "diamond": {"A": walk(), "B": walk(330), "C": walk(30), "D": walk(330, 30)},
    "arc4":    {"A": walk(), "B": walk(330), "C": walk(330, 30), "D": walk(330, 30, 330)},
    "fan":     {"A": walk(), "B": walk(330), "C": walk(210), "D": walk(90)},
}
DEFAULT_LAYOUT = {1: "solo", 2: "pair", 3: "arc3", 4: "diamond"}  # mid-difficulty layouts (sim/boards.js)


def clip(poly, a, b, c):
    out, n = [], len(poly)
    for i in range(n):
        p, q = poly[i], poly[(i + 1) % n]
        fp, fq = a * p[0] + b * p[1] - c, a * q[0] + b * q[1] - c
        if fp <= 0:
            out.append(p)
        if (fp < 0 < fq) or (fq < 0 < fp):
            t = fp / (fp - fq)
            out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out


def cell(seeds, i):
    poly = list(VERTS)
    xi, yi = seeds[i][0], seeds[i][1]
    for j, (xj, yj, _) in enumerate(seeds):
        if j != i:
            poly = clip(poly, 2 * (xj - xi), 2 * (yj - yi), xj * xj + yj * yj - xi * xi - yi * yi)
    return poly


def on_side(p, k, eps=0.6):
    """t along side k if p lies on it, else None."""
    a, b = VERTS[k], VERTS[(k + 1) % 6]
    L = math.dist(a, b)
    cross = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
    if abs(cross) / L >= eps:
        return None
    t = ((p[0] - a[0]) * (b[0] - a[0]) + (p[1] - a[1]) * (b[1] - a[1])) / (L * L)
    return min(1.0, max(0.0, t)) if -0.01 <= t <= 1.01 else None


def profile_at(prof, t):
    for (t0, d0), (t1, d1) in zip(prof, prof[1:]):
        if t0 <= t <= t1:
            return d0 + (d1 - d0) * (0 if t1 == t0 else (t - t0) / (t1 - t0))
    return 0.0


def side_point(k, t):
    a, b = VERTS[k], VERTS[(k + 1) % 6]
    prof = HULL_PROFILE if k == HULL else DOCK
    ang = math.radians(30 + 60 * k)
    d = profile_at(prof, t)
    return (a[0] + (b[0] - a[0]) * t + d * math.cos(ang), a[1] + (b[1] - a[1]) * t + d * math.sin(ang))


def shaped(p):
    """A point on the hexagon moved onto its side's profile; interior points unchanged."""
    for k in range(6):
        t = on_side(p, k)
        if t is not None:
            return side_point(k, t)
    return p


def kink(a, b):
    """Angular kink for an internal border, identical whichever cell draws it."""
    key = tuple(sorted([(round(a[0]), round(a[1])), (round(b[0]), round(b[1]))]))
    h = int(hashlib.md5(str(key).encode()).hexdigest(), 16)
    sgn = 1 if h % 2 else -1
    amt = 6 + (h >> 3) % 7
    pos = 0.35 + ((h >> 7) % 30) / 100
    p, q = key
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy) or 1
    amt = min(amt, 0.12 * L)   # short borders get a small kink, so it can't cross a neighbor
    return (p[0] + dx * pos - dy / L * amt * sgn, p[1] + dy * pos + dx / L * amt * sgn)


def shape_cell(poly):
    """Boundary edges follow the side profiles exactly; internal edges get an angular kink."""
    out, n = [], len(poly)
    for i in range(n):
        p, q = poly[i], poly[(i + 1) % n]
        side = None
        for k in range(6):
            ta, tb = on_side(p, k), on_side(q, k)
            if ta is not None and tb is not None and abs(ta - tb) > 1e-3:
                side = (k, ta, tb)
                break
        if side:
            k, ta, tb = side
            prof = HULL_PROFILE if k == HULL else DOCK
            inner = sorted((t for t, _ in prof if min(ta, tb) < t < max(ta, tb)), reverse=tb < ta)
            for t in [ta] + inner:
                out.append(side_point(k, t))
        else:
            a, b = shaped(p), shaped(q)
            out.append(a)
            out.append(kink(a, b))
    return out


FLAT_EDGES = [0.13, 0.37, 0.63, 0.87]   # where the docking profile leaves / rejoins the straight side


def side_t(p):
    for k in range(6):
        if k == HULL:
            continue
        t = on_side(p, k)
        if t is not None and 0.0 < t < 1.0:
            return k, t
    return None


def crosses(p1, p2, p3, p4):
    o = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return o(p1, p2, p3) * o(p1, p2, p4) < -1e-9 and o(p3, p4, p1) * o(p3, p4, p2) < -1e-9


def snap_cell(poly):
    """Move each section border that meets a docking side inside a dovetail tab or socket to the end
    of that feature nearest the border's inner end, so no tab or socket is split between sections and
    the border cannot cut across it (that made sliver and overlapping shapes)."""
    out, n = [], len(poly)
    for i, p in enumerate(poly):
        st = side_t(p)
        if st is None or profile_at(DOCK, st[1]) == 0:
            out.append(p)
            continue
        k, t = st
        inner = [q for q in (poly[i - 1], poly[(i + 1) % n]) if on_side(q, k) is None]
        a, b = VERTS[k], VERTS[(k + 1) % 6]
        if inner:
            q = inner[0]
            L2 = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
            tq = ((q[0] - a[0]) * (b[0] - a[0]) + (q[1] - a[1]) * (b[1] - a[1])) / L2
        else:
            tq = t
        lo = max(f for f in FLAT_EDGES if f <= t)
        hi = min(f for f in FLAT_EDGES if f >= t)
        t2 = lo if abs(tq - lo) < abs(tq - hi) else hi
        if inner:
            # never let the border cut across the tab or socket: take the other end if it would
            feat = [side_point(k, x) for x, _ in DOCK if lo <= x <= hi]
            pt = (a[0] + (b[0] - a[0]) * t2, a[1] + (b[1] - a[1]) * t2)
            if any(crosses(pt, inner[0], feat[j], feat[j + 1]) for j in range(len(feat) - 1)):
                t2 = hi if t2 == lo else lo
        out.append((a[0] + (b[0] - a[0]) * t2, a[1] + (b[1] - a[1]) * t2))
    return out


def dedupe(poly):
    out = []
    for p in poly:
        if not out or math.dist(p, out[-1]) > 1e-6:
            out.append(p)
    while len(out) > 1 and math.dist(out[0], out[-1]) <= 1e-6:
        out.pop()
    return out


def build_board(bid, seeds):
    cells = [dedupe(snap_cell(cell(seeds, i))) for i in range(len(seeds))]
    secs = []
    for i, (x, y, t) in enumerate(seeds):
        c = cells[i]
        sides = {}
        for j in range(len(c)):
            p, q = c[j], c[(j + 1) % len(c)]
            for k in range(6):
                a, b = on_side(p, k), on_side(q, k)
                if a is not None and b is not None and abs(a - b) > 0.02:
                    sides.setdefault(k, []).append(sorted([round(a, 3), round(b, 3)]))
        cx = sum(p[0] for p in c) / len(c); cy = sum(p[1] for p in c) / len(c)
        secs.append({"id": f"{bid}{i + 1}", "type": t,
                     "hull": HULL in sides and sum(h - l for l, h in sides[HULL]) > 0.12,
                     "poly": [[round(px, 1), round(py, 1)] for px, py in shape_cell(c)],
                     "center": [round(cx, 1), round(cy, 1)],
                     "sides": {str(k): v for k, v in sides.items()}, "adjacent": []})
    for i in range(len(seeds)):
        for j in range(i + 1, len(seeds)):
            xi, yi, _ = seeds[i]; xj, yj, _ = seeds[j]
            on = [p for p in cells[i] if abs(math.dist(p, (xi, yi)) - math.dist(p, (xj, yj))) < 0.6]
            if len(on) >= 2 and max(math.dist(a, b) for a in on for b in on) > 8:
                secs[i]["adjacent"].append(secs[j]["id"]); secs[j]["adjacent"].append(secs[i]["id"])
    for s in secs:
        s["adjacent"].sort()
    apply_setup(bid, secs)
    return {"id": bid, "sections": secs}


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
    crewable = sorted([s for s in secs if not s["setup"]["failure"] and not s["setup"]["decay"]],
                      key=lambda s: (threat(s), s["hull"], s["id"]))
    for s, n in zip(crewable[:4], [2, 2, 1, 1]):
        s["setup"]["crew"] = n


def void_zone():
    """A crescent of open space printed beyond the Outer Hull side of every board, like Spirit
    Island's ocean. Not a section yet; reserved for future houses and effects that use the void."""
    inner = [side_point(HULL, t) for t, _ in HULL_PROFILE]
    a, b = VERTS[HULL], VERTS[(HULL + 1) % 6]
    ang = math.radians(30 + 60 * HULL)
    outer = []
    for i in range(40, -1, -1):
        t = i / 40
        d = max(profile_at(HULL_PROFILE, t) + 28, 105 * math.sin(math.pi * t) ** 0.55)
        outer.append((a[0] + (b[0] - a[0]) * t + d * math.cos(ang), a[1] + (b[1] - a[1]) * t + d * math.sin(ang)))
    return [[round(x, 1), round(y, 1)] for x, y in inner + outer]


def outline():
    pts = []
    for k in range(6):
        prof = HULL_PROFILE if k == HULL else DOCK
        pts += [side_point(k, t) for t, _ in prof[:-1]]
    return [[round(x, 1), round(y, 1)] for x, y in pts]


def joins_and_links(ids, cells, rots, by_id):
    joins, links = [], []
    for x in range(len(ids)):
        for y in range(x + 1, len(ids)):
            X, Y = ids[x], ids[y]
            dx, dy = cells[Y][0] - cells[X][0], cells[Y][1] - cells[X][1]
            if abs(math.hypot(dx, dy) - STEP) > 1:
                continue
            ang = math.degrees(math.atan2(dy, dx)) % 360
            i = round((ang - 30 - rots[X]) / 60) % 6
            j = round((ang + 180 - 30 - rots[Y]) / 60) % 6
            if i == HULL or j == HULL:
                return None, None
            joins.append([X, i, Y, j])
            for sx in by_id[X]["sections"]:
                for sy in by_id[Y]["sections"]:
                    for t0, t1 in sx["sides"].get(str(i), []):
                        for u0, u1 in sy["sides"].get(str(j), []):
                            if min(t1, 1 - u0) - max(t0, 1 - u1) > 0.05:
                                links.append([sx["id"], sy["id"]])
    return joins, links


def build_layout(name, cells, boards):
    """Try every rotation combination with each Hull facing the void; keep the one with the most
    docking links (ties: Hulls pointing outward from the cluster)."""
    import itertools
    ids = list(cells)
    by_id = {bd["id"]: bd for bd in boards}
    cen = (sum(cells[b][0] for b in ids) / len(ids), sum(cells[b][1] for b in ids) / len(ids))
    occupied = lambda x, y: any(math.dist((x, y), cells[o]) < 1 for o in ids)
    def hull_ok(b, rot):
        d = math.radians(30 + 60 * HULL + rot)
        return not occupied(cells[b][0] + STEP * math.cos(d), cells[b][1] + STEP * math.sin(d))
    def outward(b, rot):
        d = math.radians(30 + 60 * HULL + rot)
        return math.cos(d) * (cells[b][0] - cen[0]) + math.sin(d) * (cells[b][1] - cen[1])
    options = [[r for r in range(0, 360, 60) if hull_ok(b, r)] for b in ids]
    best = None
    for combo in itertools.product(*options):
        rots = dict(zip(ids, combo))
        joins, links = joins_and_links(ids, cells, rots, by_id)
        if joins is None:
            continue
        score = (len(links), sum(outward(b, rots[b]) for b in ids), -sum(combo))
        if best is None or score > best[0]:
            best = (score, rots, joins, links)
    _, rots, joins, links = best
    place = {b: [round(cells[b][0], 1), round(cells[b][1], 1), rots[b]] for b in ids}
    return {"boards": ids, "place": place, "joins": joins, "links": links}


def main():
    boards = [build_board(b, s) for b, s in BOARDS.items()]
    layouts = {n: build_layout(n, c, boards) for n, c in LAYOUTS.items()}
    out = {"layout": "Every board shares one outline: a hexagonal hull module (circumradius 180, centre 0,0). Side 4 (top) is the Outer Hull; sides 0-3 and 5 are docking sides with a point-symmetric tab/slot profile, so any docking side mates with any other. `layouts` place boards on a hex grid ([x, y, rotation in degrees]) with each Hull facing the void; `links` join sections across docked sides.",
           "shape": "hex", "radius": R, "hull_side": HULL, "outline": outline(), "void_zone": void_zone(),
           "default_layout": {str(k): v for k, v in DEFAULT_LAYOUT.items()},
           "setup_rule": "Per board: 1 Failure, 2 Faults and 1 Glitch, each in a different section type (rotated between boards), 1 Decay next to the Failure, 6 Crew (2,2,1,1) across 4 sections away from the Failure and Decay.",
           "boards": boards, "layouts": layouts}
    (ROOT / "data" / "boards.json").write_text(json.dumps(out, indent=1))
    for b in boards:
        print(b["id"], "hull", sum(s["hull"] for s in b["sections"]), "neighbors",
              sorted(len(s["adjacent"]) for s in b["sections"]), "types", sorted({s["type"][:3] for s in b["sections"]}))
    for n, l in layouts.items():
        print(f"{n:8} rot {[l['place'][b][2] for b in l['boards']]} joins {len(l['joins'])} links {len(l['links'])}")


if __name__ == "__main__":
    main()
