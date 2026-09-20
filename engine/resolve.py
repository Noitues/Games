"""Targeting, ability resolution and damage (Rules 4, 6.3, 7, 8, 11)."""
from __future__ import annotations

from functools import lru_cache
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from .hexmap import DIRS, Board, Hex, Node, add, hex_distance
from .state import Champion, GameState, Monster, Structure, TeamState, Wave, other

DEATH_BANDS = ((4, 2), (8, 3), (10 ** 9, 4))      # Rules 6.4
MONSTER_REWARD_CARDS = {"blue_buff": "blue_buff", "red_buff": "red_buff"}


# --------------------------------------------------------------------- basics
def death_track_pos(rnd: int) -> int:
    for upper, pos in DEATH_BANDS:
        if rnd <= upper:
            return pos
    return 4


@lru_cache(maxsize=16)
def ring_offsets(radius: int) -> Tuple[Tuple[int, int, int], ...]:
    """(dq, dr, distance) for every hex within ``radius``, centre excluded."""
    out = []
    for dq in range(-radius, radius + 1):
        for dr in range(max(-radius, -dq - radius), min(radius, -dq + radius) + 1):
            if dq or dr:
                out.append((dq, dr, max(abs(dq), abs(dr), abs(-dq - dr))))
    return tuple(out)


def effect_distance(state: GameState, src_hex: Hex, src_tile: int, u) -> Optional[int]:
    """Distance for *effects*, in hexes (RQ-001 / RQ-002).

    A hidden hexgroup is a shortcut for movement, not for effects:

    * everything inside one hidden tile is adjacent to everything else in it,
      as before (Rules 4.1) - that is how a jungler reaches a camp;
    * a champion inside a hidden tile cannot be reached from outside it: the
      tile is a refuge (RQ-001);
    * every other unit keeps its own hex, so a tower, camp or wave inside a
      hidden tile reaches, and is reached at, plain hex range (RQ-002).

    Concealment is one-way, as ruled: a champion may still act out of a hidden
    tile. Whether that needs an answer is RQ-032, open with the lead designer.

    Returns None when the effect cannot reach the target at all.
    """
    board = state.board
    tgt_tile = board.tile_of[u.hexpos]
    tgt_hidden = bool(state.hidden_mask >> tgt_tile & 1)
    if tgt_tile == src_tile:
        return 1 if tgt_hidden else hex_distance(src_hex, u.hexpos)
    if tgt_hidden and u.kind == "champion":
        return None
    return hex_distance(src_hex, u.hexpos)


def effect_context(state: GameState, node: Node, fallback_hex: Optional[Hex] = None):
    """(hex, tile) for an effect used from ``node``. A champion inside a hidden
    tile acts from its own hex; only incoming effects are blocked."""
    tile = state.board.node_tile(node)
    if node[0] == "H":
        return ((node[1], node[2]), tile)
    return (fallback_hex or state.board.tile_hexes[tile][0], tile)


def effect_adjacent(state: GameState, u) -> List:
    """Units ``u`` reaches in the World Phase (Rules 5.3).

    RQ-002: a minion wave, tower or monster inside a hidden hexgroup reaches
    its own hex's neighbours, not the whole tile edge. A champion hidden in a
    hexgroup is not reached at all, unless the source shares the hexgroup.
    """
    tile = state.board.tile_of[u.hexpos]
    by_hex = state.by_hex
    out = []
    for uid in state.by_tile.get(tile, ()):                  # same hexgroup: adjacent
        if uid == u.uid:
            continue
        other_unit = state.unit(uid)
        if other_unit is not None and other_unit.alive:
            out.append(other_unit)
    for dq, dr, _ in ring_offsets(1):
        for uid in by_hex.get((u.hexpos[0] + dq, u.hexpos[1] + dr), ()):
            other_unit = state.unit(uid)
            if other_unit is None or not other_unit.alive or other_unit.uid == u.uid:
                continue
            if concealed_from(state, other_unit, tile):
                continue
            if other_unit not in out:
                out.append(other_unit)
    return out


def adjacent_units(state: GameState, node: Node, exclude: Optional[str] = None,
                   src_hex: Optional[Hex] = None) -> List:
    """Effect-adjacency from a node (used for card targets and AI threat reads)."""
    origin, tile = effect_context(state, node, src_hex)
    out = []
    for u in state.all_units():
        if not u.alive or u.uid == exclude:
            continue
        d = effect_distance(state, origin, tile, u)
        if d is not None and d <= 1:
            out.append(u)
    return out


def can_be_hit(state: GameState, u, attacker_team: str, spec: str) -> bool:
    """Target legality, including the Rules 8 protection order."""
    if not u.alive:
        return False
    if spec in ("ally_champion", "self"):
        return u.kind == "champion" and u.team == attacker_team
    if u.team == attacker_team:
        return False
    if spec == "enemy_champion":
        return u.kind == "champion"
    if u.kind == "structure":
        return structure_targetable(state, u)
    return True


def structure_targetable(state: GameState, s: Structure) -> bool:
    """Rules 8: T1 before T2 in the same lane; both towers of one lane before
    the Nexus."""
    if s.stype == "tower":
        if s.tier == 1:
            return True
        t1 = next((x for x in state.structures.values()
                   if x.team == s.team and x.stype == "tower" and x.lane == s.lane and x.tier == 1), None)
        return t1 is None or not t1.alive
    lanes = {}
    for x in state.structures.values():
        if x.team == s.team and x.stype == "tower":
            lanes.setdefault(x.lane, []).append(x)
    return any(all(not t.alive for t in ts) for ts in lanes.values())


def concealed_from(state: GameState, u, src_tile: int) -> bool:
    """RQ-001: a champion inside a hidden hexgroup is out of reach from outside
    it. Everything else keeps its own hex and stays reachable."""
    if u.kind != "champion":
        return False
    tile = state.board.tile_of[u.hexpos]
    return tile != src_tile and bool(state.hidden_mask >> tile & 1)


def units_within(state: GameState, node: Node, radius: int, attacker_team: str,
                 spec: str, src_hex: Optional[Hex] = None) -> List[Tuple[object, int]]:
    """Legal targets within ``radius`` of ``node``.

    Range is board distance, as Rules 4.1 always had it: a hidden hexgroup is
    one space. The ruling that changed is *who* can be reached, not how far -
    a champion hiding in a hexgroup is simply not a legal target from outside.
    """
    src_tile = state.board.node_tile(node)
    seen = state.board.nodes_within(node, radius, state.hidden_mask)
    out = []
    for nd, dist in seen.items():
        for u in state.units_at(nd):
            if not can_be_hit(state, u, attacker_team, spec):
                continue
            if concealed_from(state, u, src_tile):
                continue
            out.append((u, dist))
    return out


# --------------------------------------------------------------------- damage
def deal_hits(state: GameState, team: Optional[str], target, k: int, source: str,
              attacker: Optional[Champion] = None) -> int:
    """Apply k hits. Returns the number of chips removed.

    ``source`` is the AP bucket (Rules 7): champion sources bank the chips as
    AP, World Phase sources send them to the supply.
    """
    if k <= 0 or not target.alive:
        return 0
    champ_source = attacker is not None
    if target.kind == "champion":
        if attacker is not None and attacker.team != target.team:
            target.damaged_by[attacker.uid] = state.round
        absorbed = 0
        if target.shield > 0 and target.shield_until >= state.round:
            absorbed = min(target.shield, k)
            target.shield -= absorbed
        dmg = k - absorbed
        if dmg <= 0:
            return 0
        target.hp -= dmg
        if target.hp <= 0:
            kill_champion(state, target, team, attacker)
        return 0

    chips = min(k, target.chips)
    target.chips -= chips
    if chips and champ_source and team is not None:
        state.teams[team].gain(chips, source)
        attacker.ap_earned += chips
        if "vampiric_blade" in attacker.items:
            attacker.hp = min(attacker.max_hp, attacker.hp + chips)
        if target.kind == "structure":
            attacker.dmg_to_structures += chips
    if target.chips <= 0:
        destroy(state, target, team, attacker)
    return chips


def kill_champion(state: GameState, victim: Champion, killer_team: Optional[str],
                  attacker: Optional[Champion]) -> None:
    victim.alive = False
    victim.hp = 0
    victim.deaths += 1
    victim.shield = 0
    victim.track = death_track_pos(state.round)
    if killer_team is not None:
        state.teams[killer_team].gain(1, "champion_kill")
        state.teams[killer_team].kills += 1
        killer_uid = attacker.uid if attacker is not None else None
        for uid, rnd in victim.damaged_by.items():
            helper = state.champs.get(uid)
            if helper is not None and uid != killer_uid and helper.team == killer_team \
                    and rnd >= state.round - 1:
                helper.assists += 1
    victim.damaged_by.clear()
    if attacker is not None:
        attacker.kills += 1
    state.touch()
    state.event("kill", victim=victim.uid, team=killer_team, round=state.round)


def destroy(state: GameState, target, team: Optional[str], attacker: Optional[Champion]) -> None:
    target.alive = False
    if target.kind == "wave":
        state.waves.pop(target.uid, None)
    elif target.kind == "structure":
        if target.stype == "nexus":
            state.winner = other(target.team)
            state.end_reason = "nexus"
        else:
            state.teams[target.team].towers_lost += 1
        state.event("structure_down", uid=target.uid, round=state.round)
    elif target.kind == "monster":
        if team is not None:
            monster_reward(state, target, team)
        cfg = state.config["monsters"][target.mtype]
        target.respawn_round = state.round + cfg["respawn"]
        state.event("monster_killed", mtype=target.mtype, team=team, round=state.round)
    state.touch()


def monster_reward(state: GameState, m: Monster, team: str) -> None:
    ts = state.teams[team]
    if m.mtype in MONSTER_REWARD_CARDS:
        ts.cards.append(MONSTER_REWARD_CARDS[m.mtype])
    elif m.mtype == "dragon":
        ts.dragons += 1
    elif m.mtype == "baron":
        ts.baron_track = 3           # Rules 11 [DEFAULT timing]


# ------------------------------------------------------------------ movement
def move_unit(state: GameState, u, node: Node, from_node: Optional[Node] = None) -> None:
    """Place a unit on a node. A hidden tile gets a nominal hex (Rules 3.1).

    A node chosen during enumeration can go stale inside an ability: REVEAL or a
    Control Ward can turn a tile face up between the choice and the movement.
    A stale tile node is then resolved to a legal hex inside that tile.
    """
    if node[0] == "T" and not (state.hidden_mask >> node[1] & 1):
        tile_hexes = state.board.tile_hexes[node[1]]
        prev = (from_node[1], from_node[2]) if from_node is not None and from_node[0] == "H" else None
        ranked = sorted(tile_hexes,
                        key=lambda h: (0 if prev is not None and h in state.board.neighbors[prev] else 1))
        for h in ranked:
            if state.can_stop(("H", h[0], h[1]), u.team):
                u.hexpos = h
                state.touch()
                return
        return                      # no legal hex: the unit stays put
    if node[0] == "H":
        # The hex can have been taken since the option was enumerated (an
        # earlier step of the same ability pushed a unit into it, or a flip
        # placed one there). Movement is optional, so the unit stays put.
        if any(x.alive and x.uid != u.uid and x.hexpos == (node[1], node[2])
               for x in state.all_units()):
            return
        u.hexpos = (node[1], node[2])
    else:
        hexes = state.board.tile_hexes[node[1]]
        cand = hexes
        if from_node is not None:
            prev = from_node[1:] if from_node[0] == "H" else None
            if prev is not None:
                adj = [h for h in hexes if h in state.board.neighbors[(prev[0], prev[1])]]
                if adj:
                    cand = adj
        free = [h for h in cand
                if not any(x.hexpos == h and x.kind != "champion" for x in state.all_units() if x.alive)]
        u.hexpos = (free or cand)[0]
    state.touch()


def push_pull(state: GameState, champ: Champion, target, n: int, away: bool) -> None:
    """PUSH / PULL along the board-distance gradient (Rules 6.3)."""
    if target.kind in ("structure", "monster"):
        return                               # immovable
    board = state.board
    for _ in range(n):
        src = state.node_of_unit(champ)
        cur = state.node_of_unit(target)
        field = board.nodes_within(src, 8, state.hidden_mask)
        d0 = field.get(cur, 99)
        best = None
        # Prefer the hex that continues the straight line away from / toward src.
        for nb in board.graph_neighbors(cur, state.hidden_mask):
            d = field.get(nb, 99)
            ok = d > d0 if away else d < d0
            if not ok or not state.can_stop(nb, target.team):
                continue
            score = _line_bonus(board, src, cur, nb, away)
            if best is None or score > best[0]:
                best = (score, nb)
        if best is None:
            break
        move_unit(state, target, best[1], cur)


def _line_bonus(board: Board, src: Node, cur: Node, nb: Node, away: bool) -> float:
    if src[0] != "H" or cur[0] != "H" or nb[0] != "H":
        return 0.0
    v = (cur[1] - src[1], cur[2] - src[2])
    w = (nb[1] - cur[1], nb[2] - cur[2])
    if v == (0, 0):
        return 0.0
    return 1.0 if (w in DIRS and _same_dir(v, w)) else 0.0


def _same_dir(v, w) -> bool:
    for d in DIRS:
        if w == d:
            k = max(abs(v[0]), abs(v[1]), abs(-v[0] - v[1]))
            if k and (v[0] == d[0] * k and v[1] == d[1] * k):
                return True
    return False


# --------------------------------------------------------- ability execution
def ability_range(champ: Champion, ability: str, base: int) -> int:
    if ability != "L0" and "longbow" in champ.items:
        return base + 1
    return base


def ability_cooldown(champ: Champion, ab: dict) -> int:
    cd = ab.get("cooldown", 1)
    if "ionian_charm" in champ.items:
        cd = max(1, cd - 1)
    return cd


def step_choices(state: GameState, champ: Champion, node: Node, step: dict,
                 prev_uid: Optional[str], ability: str, cap: int) -> List:
    """Legal choices for one icon step from ``node``. [] means unusable."""
    ic = step["icon"]
    team = champ.team
    if ic in ("HIT", "AREA", "LINE"):
        if ic == "HIT":
            r = ability_range(champ, ability, step.get("range", 1))
            cands = [u for u, _ in units_within(state, node, r, team,
                                                step.get("target", "enemy_any"), champ.hexpos)]
            return _cap([u.uid for u in cands], cap)
        if ic == "AREA":
            r = ability_range(champ, ability, step.get("range", 1))
            hits = units_within(state, node, r, team, step.get("target", "enemy_any"),
                                champ.hexpos)
            return [None] if hits else []
        r = ability_range(champ, ability, step.get("n", 1))
        src_hex, src_tile = effect_context(state, node, champ.hexpos)
        origin = src_hex
        out = []
        for i, d in enumerate(DIRS):
            if line_targets(state, (origin[0], origin[1]), d, r, team,
                            step.get("target", "enemy_any"), src_tile):
                out.append(i)
        return _cap(out, cap)
    if ic in ("MOVE", "DASH", "BLINK"):
        return _cap(self_move_options(state, champ, node, ic, step.get("n", 1)), cap)
    if ic in ("PUSH", "PULL", "SLOW", "ROOT", "DELAY"):
        if step.get("area"):
            return [None]
        if step.get("target") == "prev":
            return [None] if prev_uid else []
        spec = step.get("target", "enemy_any")
        r = ability_range(champ, ability, step.get("range", 1))
        cands = [u for u, _ in units_within(state, node, r, team, spec, champ.hexpos)]
        if ic in ("PUSH", "PULL"):
            cands = [u for u in cands if u.kind in ("champion", "wave")]
        if ic == "DELAY":
            cands = [u for u in cands if u.kind == "champion"]
        return _cap([u.uid for u in cands], cap)
    if ic in ("HEAL", "SHIELD", "HASTE"):
        if step.get("target") == "self":
            return [None]
        r = ability_range(champ, ability, step.get("range", 1))
        allies = [u for u, _ in units_within(state, node, r, team, "ally_champion",
                                             champ.hexpos)]
        if ic == "HEAL":
            allies = [u for u in allies if u.hp < u.max_hp] or allies
        if ic == "HASTE":
            allies = [u for u in allies if u.track > 0]
        return _cap([u.uid for u in allies], cap)
    if ic == "REVEAL":
        r = ability_range(champ, ability, step.get("range", 1))
        seen = state.board.nodes_within(node, r, state.hidden_mask)
        tiles = sorted({state.board.node_tile(n) for n in seen
                        if state.hidden_mask >> state.board.node_tile(n) & 1})
        return _cap(tiles, cap)
    raise ValueError(f"unknown icon {ic}")


def _cap(seq: List, cap: int) -> List:
    if len(seq) <= cap:
        return list(seq)
    stride = len(seq) / cap
    return [seq[int(i * stride)] for i in range(cap)]


def line_targets(state: GameState, origin: Hex, d: Hex, n: int, team: str, spec: str,
                 src_tile: Optional[int] = None) -> List:
    """Units caught by a LINE, walking hexes and collecting whatever sits on the
    node each hex belongs to. A champion concealed in a hidden hexgroup is
    skipped (RQ-001)."""
    if src_tile is None:
        src_tile = state.board.tile_of[origin]
    nodes = []
    for h in state.board.line_hexes(origin, d, n):
        nd = state.board.node_of(h, state.hidden_mask)
        if nd not in nodes:
            nodes.append(nd)
    out = []
    for nd in nodes:
        for u in state.units_at(nd):
            if can_be_hit(state, u, team, spec) and not concealed_from(state, u, src_tile) \
                    and u not in out:
                out.append(u)
    return out


def self_move_options(state: GameState, champ: Champion, node: Node, ic: str, n: int) -> List[Node]:
    board = state.board
    if ic == "BLINK":
        seen = board.nodes_within(node, n, state.hidden_mask)
        return [nd for nd in seen
                if nd != node and _free_for(state, nd, champ)]
    if ic == "MOVE":
        return reachable(state, champ, node, n, include_start=True)
    # DASH: straight line, passes through units, must end in an empty hex.
    origin = node[1:] if node[0] == "H" else board.tile_hexes[node[1]][0]
    out = []
    for d in DIRS:
        for h in board.line_hexes((origin[0], origin[1]), d, n):
            nd = board.node_of(h, state.hidden_mask)
            if nd != node and _free_for(state, nd, champ) and nd not in out:
                out.append(nd)
    return out


def _free_for(state: GameState, nd: Node, champ: Champion) -> bool:
    units = [u for u in state.units_at(nd) if u.uid != champ.uid]
    if nd[0] == "T":
        return all(u.team == champ.team for u in units if u.kind != "monster") and \
               all(u.kind != "monster" or True for u in units)
    return not units


def reachable(state: GameState, champ: Champion, start: Node, budget: int,
              include_start: bool = False) -> List[Node]:
    """Movement graph search (Rules 4.3). Friendly hexes may be passed
    through but not stopped in; hidden tiles holding enemies are blocked (a
    bump into one is offered separately as a flip entry)."""
    board = state.board
    seen = {start: 0}
    frontier = [start]
    stops = []
    for d in range(1, budget + 1):
        nxt = []
        for nd in frontier:
            for nb in board.graph_neighbors(nd, state.hidden_mask):
                if nb in seen:
                    continue
                if not _passable(state, nb, champ):
                    continue
                seen[nb] = d
                nxt.append(nb)
                if _free_for(state, nb, champ):
                    stops.append(nb)
        frontier = nxt
        if not frontier:
            break
    if include_start:
        stops.insert(0, start)
    return stops


def _passable(state: GameState, nd: Node, champ: Champion) -> bool:
    units = [u for u in state.units_at(nd) if u.uid != champ.uid]
    if not units:
        return True
    if nd[0] == "T":
        return all(u.team == champ.team or u.kind == "monster" for u in units)
    u = units[0]
    if u.kind == "monster":
        return False
    return u.team == champ.team


def movement_cost(state: GameState, champ: Champion, start: Node, dest: Node,
                   budget: int) -> Optional[int]:
    """Movement spent walking from ``start`` to ``dest`` (Rules 4.1/4.3)."""
    if start == dest:
        return 0
    board = state.board
    seen = {start: 0}
    frontier = [start]
    for d in range(1, budget + 1):
        nxt = []
        for nd in frontier:
            for nb in board.graph_neighbors(nd, state.hidden_mask):
                if nb in seen or not _passable(state, nb, champ):
                    continue
                seen[nb] = d
                if nb == dest:
                    return d
                nxt.append(nb)
        frontier = nxt
    return None


def flip_entry_options(state: GameState, champ: Champion, start: Node, budget: int) -> List[Tuple[int, Node]]:
    """(tile, stop-node) pairs for bumping into a hidden tile that holds
    enemy units (Rules 3.3)."""
    board = state.board
    out = []
    stops = reachable(state, champ, start, budget, include_start=True)
    for nd in stops:
        for nb in board.graph_neighbors(nd, state.hidden_mask):
            if nb[0] != "T":
                continue
            t = nb[1]
            units = state.units_at(nb)
            if any(u.team not in (None, champ.team) for u in units):
                pair = (t, nd)
                if pair not in out:
                    out.append(pair)
    return out
