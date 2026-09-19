"""Board geometry for Hex-Nexus.

Implements Rules sections 2 (map), 3 (hidden hexgroups) and 4.1 (distance).

Positions are axial (q, r) with flat-top hexes, s = -q - r, north = negative r.

The movement/range graph has two node kinds (Rules 3.1 / 4.1):
  ("H", q, r)  a hex inside a *visible* tile
  ("T", t)     a whole *hidden* tile, which counts as one single space
"""
from __future__ import annotations

import json
import os
from functools import lru_cache
from typing import Dict, Iterable, List, Sequence, Tuple

Hex = Tuple[int, int]
Node = Tuple

# Axial neighbour directions, canonical order (used for LINE/DASH/PUSH geometry).
DIRS: Tuple[Hex, ...] = ((1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1))

RULES_MAP = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "rules", "map_v1.json")


def add(a: Hex, d: Hex) -> Hex:
    return (a[0] + d[0], a[1] + d[1])


def hex_distance(a: Hex, b: Hex) -> int:
    dq, dr = a[0] - b[0], a[1] - b[1]
    ds = -dq - dr
    return max(abs(dq), abs(dr), abs(ds))


class Board:
    """Static map data plus the tile-aware graph primitives."""

    def __init__(self, data: dict):
        self.data = data
        self.tile_names: List[str] = sorted(data["hexgroups"].keys())
        self.tile_hexes: List[Tuple[Hex, ...]] = [
            tuple(sorted((q, r) for q, r in data["hexgroups"][n])) for n in self.tile_names
        ]
        self.tile_index: Dict[str, int] = {n: i for i, n in enumerate(self.tile_names)}
        self.tile_of: Dict[Hex, int] = {}
        for i, hexes in enumerate(self.tile_hexes):
            for h in hexes:
                assert h not in self.tile_of, f"hex {h} in two tiles"
                self.tile_of[h] = i
        self.hexes: Tuple[Hex, ...] = tuple(sorted(self.tile_of))
        self.n_tiles = len(self.tile_hexes)

        self.neighbors: Dict[Hex, Tuple[Hex, ...]] = {
            h: tuple(add(h, d) for d in DIRS if add(h, d) in self.tile_of) for h in self.hexes
        }

        self.tile_adj: List[Tuple[int, ...]] = []
        for i, hexes in enumerate(self.tile_hexes):
            adj = set()
            for h in hexes:
                for nb in self.neighbors[h]:
                    t = self.tile_of[nb]
                    if t != i:
                        adj.add(t)
            self.tile_adj.append(tuple(sorted(adj)))

        # Team data: "north" / "south"
        self.fountain = {s: tuple(data[s]["fountain"]) for s in ("north", "south")}
        self.nexus = {s: tuple(data[s]["nexus"]) for s in ("north", "south")}
        self.towers = {
            s: {k: tuple(v) for k, v in data[s]["towers"].items()} for s in ("north", "south")
        }
        self.lane_paths = {
            s: {lane: [tuple(h) for h in path] for lane, path in data[s]["lane_paths"].items()}
            for s in ("north", "south")
        }
        self.monsters = {k: [tuple(h) for h in v] for k, v in data["monsters"].items()}
        self.terrain: Dict[Hex, str] = {}
        for kind, hs in data["terrain"].items():
            for h in hs:
                self.terrain[(h[0], h[1])] = kind
        for h in self.hexes:
            self.terrain.setdefault(h, "base")

        # Minion spawn hexes (Rules 9.1): the first hex of each lane path.
        self.spawn = {
            s: {lane: path[0] for lane, path in self.lane_paths[s].items()} for s in ("north", "south")
        }

    # ---------------------------------------------------------------- loading
    @staticmethod
    def load(path: str = RULES_MAP) -> "Board":
        with open(path) as fh:
            return Board(json.load(fh))

    # ------------------------------------------------------------ graph layer
    def node_of(self, h: Hex, hidden_mask: int) -> Node:
        t = self.tile_of[h]
        if hidden_mask >> t & 1:
            return ("T", t)
        return ("H", h[0], h[1])

    def node_hexes(self, node: Node) -> Tuple[Hex, ...]:
        if node[0] == "H":
            return ((node[1], node[2]),)
        return self.tile_hexes[node[1]]

    def node_tile(self, node: Node) -> int:
        if node[0] == "H":
            return self.tile_of[(node[1], node[2])]
        return node[1]

    def graph_neighbors(self, node: Node, hidden_mask: int) -> Tuple[Node, ...]:
        return _neighbors_cached(self, node, hidden_mask)

    def nodes_within(self, start: Node, radius: int, hidden_mask: int) -> Dict[Node, int]:
        """Board distance (Rules 4.1). Ignores blocking: range has no line of sight."""
        seen = {start: 0}
        frontier = [start]
        for d in range(1, radius + 1):
            nxt = []
            for node in frontier:
                for nb in self.graph_neighbors(node, hidden_mask):
                    if nb not in seen:
                        seen[nb] = d
                        nxt.append(nb)
            frontier = nxt
            if not frontier:
                break
        return seen

    def distance(self, a: Node, b: Node, hidden_mask: int, cap: int = 24) -> int:
        if a == b:
            return 0
        seen = self.nodes_within(a, cap, hidden_mask)
        return seen.get(b, 999)

    def line_hexes(self, origin: Hex, direction: Hex, n: int) -> List[Hex]:
        out = []
        cur = origin
        for _ in range(n):
            cur = add(cur, direction)
            if cur not in self.tile_of:
                break
            out.append(cur)
        return out


@lru_cache(maxsize=1 << 16)
def _neighbors_cached(board: Board, node: Node, hidden_mask: int) -> Tuple[Node, ...]:
    out = []
    if node[0] == "H":
        h = (node[1], node[2])
        own = board.tile_of[h]
        if hidden_mask >> own & 1:
            # The hex is inside a hidden tile: its node is the tile, not the hex.
            return (("T", own),)
        for nb in board.neighbors[h]:
            t = board.tile_of[nb]
            n = ("T", t) if hidden_mask >> t & 1 else ("H", nb[0], nb[1])
            if n not in out:
                out.append(n)
    else:
        t = node[1]
        for h in board.tile_hexes[t]:
            for nb in board.neighbors[h]:
                t2 = board.tile_of[nb]
                if t2 == t:
                    continue
                n = ("T", t2) if hidden_mask >> t2 & 1 else ("H", nb[0], nb[1])
                if n not in out:
                    out.append(n)
    return tuple(out)


def board_hash(board: Board) -> int:
    return id(board)


Board.__hash__ = lambda self: id(self)  # type: ignore[assignment]
Board.__eq__ = lambda self, other: self is other  # type: ignore[assignment]
