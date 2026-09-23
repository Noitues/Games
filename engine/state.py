"""Mutable game state for Hex-Nexus (Rules sections 3-9, 11, 12).

Design notes
------------
* Every unit stores a *hex*. While its tile is hidden the hex is only a
  nominal placeholder (Rules 3.5: units inside a hidden tile have no
  individual hex); the flip procedure hands out real hexes.
* ``hidden_mask`` is a bitmask over tile indices. It is refreshed at the
  checkpoints named in Rules 3.5 (after every activation, after minion
  movement) and immediately on a flip caused by entry (Rules 3.3).
* Chips are HP *and* AP (Rules 7): every chip a champion removes is added to
  that champion's team pool straight away.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Set, Tuple

from .hexmap import Board, Hex, Node

TEAMS = ("north", "south")


def other(team: str) -> str:
    return "south" if team == "north" else "north"


@dataclass
class Champion:
    uid: str
    cid: str          # kit id
    name: str
    role: str
    team: str
    max_hp: int
    hp: int
    speed: int
    hexpos: Hex
    alive: bool = True
    track: int = 0                 # 0 == in hand (Rules 5.1/5.2)
    activated: bool = False
    items: Set[str] = field(default_factory=set)
    shield: int = 0                # hits ignored (Rules 6.3 SHIELD)
    shield_until: int = 0          # round number it expires after
    slow: int = 0                  # -Speed on the next activation
    rooted: bool = False           # cannot move on its next activation
    # bookkeeping
    kills: int = 0
    deaths: int = 0
    assists: int = 0
    ap_earned: int = 0
    rounds_dead: int = 0
    rounds_cd: int = 0
    dmg_to_structures: int = 0
    conceal_attacks: int = 0        # abilities used from a hidden tile on something outside it
    snipe_attacks: int = 0          # ...and from two or more hexes away: true sniping
    champ_snipes: int = 0           # ...of those, the ones aimed at a champion
    edge_rounds: int = 0            # activations ended on a hexgroup border (RQ-036)
    activations: int = 0
    ap_by_ability: Dict[str, int] = field(default_factory=dict)
    ap_by_target: Dict[str, int] = field(default_factory=dict)
    damaged_by: Dict[str, int] = field(default_factory=dict)   # uid -> round

    kind: str = "champion"

    def clone(self) -> "Champion":
        c = Champion.__new__(Champion)
        c.__dict__.update(self.__dict__)
        c.items = set(self.items)
        c.damaged_by = dict(self.damaged_by)
        c.ap_by_ability = dict(self.ap_by_ability)
        c.ap_by_target = dict(self.ap_by_target)
        return c


@dataclass
class Wave:
    uid: str
    team: str
    lane: str
    chips: int
    path_idx: int
    hexpos: Hex
    empowered: bool = False
    kind: str = "wave"
    alive: bool = True

    def clone(self) -> "Wave":
        w = Wave.__new__(Wave)
        w.__dict__.update(self.__dict__)
        return w


@dataclass
class Structure:
    uid: str
    team: str
    stype: str        # "tower" | "nexus"
    lane: str         # "top" | "mid" | "bot" | "" for nexus
    tier: int         # 1 | 2 | 0 for nexus
    chips: int
    hexpos: Hex
    alive: bool = True
    kind: str = "structure"

    def clone(self) -> "Structure":
        s = Structure.__new__(Structure)
        s.__dict__.update(self.__dict__)
        return s


@dataclass
class Monster:
    uid: str
    mtype: str
    chips: int
    max_chips: int
    hexpos: Hex
    alive: bool = True
    respawn_round: int = 0     # round in which it (re)appears
    kind: str = "monster"
    team: Optional[str] = None

    def clone(self) -> "Monster":
        m = Monster.__new__(Monster)
        m.__dict__.update(self.__dict__)
        return m


@dataclass
class TeamState:
    team: str
    ap: int = 0
    cards: List[str] = field(default_factory=list)   # buff + item cards in hand
    dragons: int = 0
    baron_track: int = 0                              # 0 == no Baron card
    towers_lost: int = 0
    kills: int = 0
    ap_by_source: Dict[str, int] = field(default_factory=dict)
    ap_spent: Dict[str, int] = field(default_factory=dict)
    items_bought: Dict[str, int] = field(default_factory=dict)

    def clone(self) -> "TeamState":
        t = TeamState.__new__(TeamState)
        t.__dict__.update(self.__dict__)
        t.cards = list(self.cards)
        t.ap_by_source = dict(self.ap_by_source)
        t.ap_spent = dict(self.ap_spent)
        t.items_bought = dict(self.items_bought)
        return t

    def gain(self, n: int, source: str) -> None:
        self.ap += n
        self.ap_by_source[source] = self.ap_by_source.get(source, 0) + n

    def spend(self, n: int, use: str) -> None:
        self.ap -= n
        self.ap_spent[use] = self.ap_spent.get(use, 0) + n


class GameState:
    __slots__ = (
        "board", "kits", "round", "priority", "hidden_mask", "champs", "waves",
        "structures", "monsters", "teams", "wards", "_by_node", "_by_hex", "_by_tile", "_dirty",
        "winner", "end_reason", "log", "anomalies", "next_uid", "shadow",
        "activation_seq", "config", "turn_order", "turn_index",
    )

    def __init__(self, board: Board, kits: dict, config: dict):
        self.board = board
        self.kits = kits
        self.config = config
        self.round = 0
        self.priority = "north"
        self.hidden_mask = (1 << board.n_tiles) - 1
        self.champs: Dict[str, Champion] = {}
        self.waves: Dict[str, Wave] = {}
        self.structures: Dict[str, Structure] = {}
        self.monsters: Dict[str, Monster] = {}
        self.teams: Dict[str, TeamState] = {t: TeamState(t) for t in TEAMS}
        self.wards: Dict[int, int] = {}      # tile -> round it stops forcing visible
        self._by_node: Dict[Node, List[str]] = {}
        self._by_hex: Dict[Hex, List[str]] = {}
        self._by_tile: Dict[int, List[str]] = {}
        self._dirty = True
        self.winner: Optional[str] = None
        self.end_reason: str = ""
        self.log: List[dict] = []
        self.anomalies: List[str] = []
        self.next_uid = 0
        self.activation_seq = 0
        self.shadow = False       # True for AI look-ahead copies: no logging
        self.turn_order: List[str] = []    # this round's snake order (Rules 5.2)
        self.turn_index = 0                # slot being taken right now

    def event(self, kind: str, **kw) -> None:
        if not self.shadow:
            self.log.append({"t": kind, **kw})

    def note(self, msg: str) -> None:
        if not self.shadow and msg not in self.anomalies:
            self.anomalies.append(msg)

    # ------------------------------------------------------------------ clone
    def clone(self) -> "GameState":
        s = GameState.__new__(GameState)
        s.board = self.board
        s.kits = self.kits
        s.config = self.config
        s.round = self.round
        s.priority = self.priority
        s.hidden_mask = self.hidden_mask
        s.champs = {k: v.clone() for k, v in self.champs.items()}
        s.waves = {k: v.clone() for k, v in self.waves.items()}
        s.structures = {k: v.clone() for k, v in self.structures.items()}
        s.monsters = {k: v.clone() for k, v in self.monsters.items()}
        s.teams = {k: v.clone() for k, v in self.teams.items()}
        s.wards = dict(self.wards)
        s._by_node = {}
        s._by_hex = {}
        s._by_tile = {}
        s._dirty = True
        s.winner = self.winner
        s.end_reason = self.end_reason
        s.log = []
        s.anomalies = []
        s.next_uid = self.next_uid
        s.activation_seq = self.activation_seq
        s.turn_order = self.turn_order
        s.turn_index = self.turn_index
        s.shadow = True
        return s

    # ------------------------------------------------------------- unit index
    def all_units(self):
        yield from self.champs.values()
        yield from self.waves.values()
        yield from self.structures.values()
        yield from self.monsters.values()

    def unit(self, uid: str):
        for d in (self.champs, self.waves, self.structures, self.monsters):
            u = d.get(uid)
            if u is not None:
                return u
        return None

    def touch(self) -> None:
        self._dirty = True

    def reindex(self) -> None:
        idx: Dict[Node, List[str]] = {}
        by_hex: Dict[Hex, List[str]] = {}
        by_tile: Dict[int, List[str]] = {}
        nod = self.board.node_of
        tof = self.board.tile_of
        mask = self.hidden_mask
        for u in self.all_units():
            if not u.alive:
                continue
            idx.setdefault(nod(u.hexpos, mask), []).append(u.uid)
            by_hex.setdefault(u.hexpos, []).append(u.uid)
            by_tile.setdefault(tof[u.hexpos], []).append(u.uid)
        self._by_node = idx
        self._by_hex = by_hex
        self._by_tile = by_tile
        self._dirty = False

    @property
    def by_hex(self) -> Dict[Hex, List[str]]:
        if self._dirty:
            self.reindex()
        return self._by_hex

    @property
    def by_tile(self) -> Dict[int, List[str]]:
        if self._dirty:
            self.reindex()
        return self._by_tile

    @property
    def by_node(self) -> Dict[Node, List[str]]:
        if self._dirty:
            self.reindex()
        return self._by_node

    def node_of_unit(self, u) -> Node:
        return self.board.node_of(u.hexpos, self.hidden_mask)

    def units_at(self, node: Node) -> List:
        return [self.unit(uid) for uid in self.by_node.get(node, ())]

    def teams_at(self, node: Node) -> Set[str]:
        return {u.team for u in self.units_at(node) if u.team is not None}

    # ------------------------------------------------------- visibility rules
    def tile_team_sets(self) -> Dict[int, Set[str]]:
        """Teams of *flip-causing* units per tile (Rules 3.2: champions,
        minions and structures; monsters are neutral)."""
        out: Dict[int, Set[str]] = {}
        tof = self.board.tile_of
        for u in self.all_units():
            if not u.alive or u.kind == "monster":
                continue
            out.setdefault(tof[u.hexpos], set()).add(u.team)
        return out

    def refresh_visibility(self, allow_flip_back: bool = True, placer=None) -> None:
        """Rules 3.2/3.5. Tiles with both teams inside must be visible; tiles
        with at most one team flip back (only at the checkpoints that pass
        allow_flip_back=True). Control Wards pin a tile visible (Rules 12).

        RQ-036: an occupied hexgroup is also revealed while an enemy champion
        stands adjacent to it. You cannot lurk next to someone - cover works at
        a distance, and standing on the edge of a hexgroup is how you look into
        it.
        """
        sets = self.tile_team_sets()
        mask = self.hidden_mask
        newly_visible = []
        watched = self._tiles_watched_by_enemies(sets)
        for t in range(self.board.n_tiles):
            contested = len(sets.get(t, ())) > 1 or t in watched
            warded = self.wards.get(t, -1) >= self.round
            hidden_now = bool(mask >> t & 1)
            if hidden_now and (contested or warded):
                mask &= ~(1 << t)
                newly_visible.append(t)
            elif not hidden_now and allow_flip_back and not contested and not warded:
                mask |= 1 << t
        if mask != self.hidden_mask:
            self.hidden_mask = mask
            self.touch()
        for t in newly_visible:
            place_units_on_flip(self, t, placer)

    def _tiles_watched_by_enemies(self, sets) -> set:
        """Occupied hexgroups with an enemy champion on an adjacent hex."""
        if not self.config.get("adjacency_reveal", True):
            return set()
        board = self.board
        radius = self.config.get("reveal_radius", 1)
        watched = set()
        for c in self.champs.values():
            if not c.alive:
                continue
            near = set(board.neighbors.get(c.hexpos, ()))
            for _ in range(radius - 1):
                near |= {n for h in tuple(near) for n in board.neighbors.get(h, ())}
            for nb in near:
                t = board.tile_of.get(nb)
                if t is None or t in watched:
                    continue
                occupants = sets.get(t, ())
                if occupants and any(team != c.team for team in occupants):
                    watched.add(t)
        return watched

    def force_visible(self, tile: int, placer=None) -> None:
        """Flip one tile face up now (Rules 3.3 step 2)."""
        if self.hidden_mask >> tile & 1:
            self.hidden_mask &= ~(1 << tile)
            self.touch()
            place_units_on_flip(self, tile, placer)

    # --------------------------------------------------------------- movement
    def occupant(self, node: Node):
        us = self.units_at(node)
        return us[0] if us else None

    def can_stop(self, node: Node, team: str) -> bool:
        """Rules 4.2/4.3. A visible hex holds one unit; a hidden tile holds any
        number of units from one team."""
        units = self.units_at(node)
        if node[0] == "T":
            return all(u.team == team for u in units)
        return not units

    def can_pass(self, node: Node, team: str) -> bool:
        units = self.units_at(node)
        if not units:
            return True
        if node[0] == "T":
            return all(u.team == team for u in units)
        u = units[0]
        if u.kind == "monster":
            return False            # monsters block everything (Rules 4.3)
        if u.team != team:
            return False            # enemy units block
        return True                 # friendly units may be passed through


def place_units_on_flip(state: GameState, tile: int, placer=None) -> None:
    """Rules 3.3 step 3 and 3.4 (overflow). Champions inside the tile take
    individual hexes; minions, structures and monsters keep their own hex."""
    board = state.board
    hexes = list(board.tile_hexes[tile])
    fixed = {}
    movable: List[Champion] = []
    for u in state.all_units():
        if not u.alive or board.tile_of[u.hexpos] != tile:
            continue
        if u.kind == "champion":
            movable.append(u)
        else:
            fixed[u.hexpos] = u
    if not movable:
        state.touch()
        return
    free = [h for h in hexes if h not in fixed]
    # Keep a champion where it already stands if that hex is free.
    assigned: Dict[str, Hex] = {}
    taken: Set[Hex] = set()
    if placer is not None:
        choice = placer(state, tile, movable, free)
        if choice:
            for uid, h in choice.items():
                assigned[uid] = h
                taken.add(h)
    for c in movable:
        if c.uid in assigned:
            continue
        if c.hexpos in free and c.hexpos not in taken:
            assigned[c.uid] = c.hexpos
            taken.add(c.hexpos)
    for c in movable:
        if c.uid in assigned:
            continue
        spot = next((h for h in free if h not in taken), None)
        if spot is None:
            # Rules 3.4 overflow: empty hexes adjacent to the hexgroup.
            cand = []
            for h in hexes:
                for nb in board.neighbors[h]:
                    if board.tile_of[nb] == tile:
                        continue
                    cand.append(nb)
            spot = next(
                (h for h in cand
                 if h not in taken and not state.units_at(board.node_of(h, state.hidden_mask))),
                c.hexpos,
            )
        assigned[c.uid] = spot
        taken.add(spot)
    for c in movable:
        c.hexpos = assigned[c.uid]
    state.touch()
