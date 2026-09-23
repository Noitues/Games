"""Round structure, legal-option generation and the game loop (Rules 5-13)."""
from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

from .abilities import apply_plan, enumerate_plans, respawn
from .actions import PASS, Activation, CardPlay, Placement, Purchase
from .config import DEFAULT_CONFIG
from .hexmap import Board, Hex, Node
from .items import ALL_ITEMS, CARD_ITEMS, MAX_CARD_COPIES, STAT_ITEMS
from .kits import load_roster
from .resolve import (ability_cooldown, adjacent_units, can_be_hit, deal_hits,
                      effect_adjacent, movement_cost,
                      flip_entry_options, kill_champion, move_unit, reachable,
                      structure_targetable, units_within)
from .state import (Champion, GameState, Monster, Structure, TEAMS, TeamState,
                    Wave, other, place_units_on_flip)

SNAKE = (0, 1, 1, 0, 0, 1, 1, 0, 0, 1)      # Rules 5.2
ROLES = ("Top", "Jungle", "Mid", "ADC", "Support")


# ----------------------------------------------------------------- game setup
def new_game(board: Board, kits: dict, picks: Dict[str, List[str]], config: dict,
             first: str = "north") -> GameState:
    st = GameState(board, kits, config)
    st.priority = first
    for team in TEAMS:
        home = board.fountain[team]
        for cid in picks[team]:
            k = kits[cid]
            uid = f"{team[0]}_{cid}"
            st.champs[uid] = Champion(
                uid=uid, cid=cid, name=k["name"], role=k["role"], team=team,
                max_hp=k["stats"]["hp"], hp=k["stats"]["hp"], speed=k["stats"]["speed"],
                hexpos=home)
        for name, h in board.towers[team].items():
            lane, tier = name.split("_")
            st.structures[f"{team[0]}_{name}"] = Structure(
                uid=f"{team[0]}_{name}", team=team, stype="tower", lane=lane,
                tier=int(tier[1]), chips=config["tower_hp"], hexpos=h)
        nx = board.nexus[team]
        st.structures[f"{team[0]}_nexus"] = Structure(
            uid=f"{team[0]}_nexus", team=team, stype="nexus", lane="", tier=0,
            chips=config["nexus_hp"], hexpos=nx)
    for mtype, hexes in board.monsters.items():
        cfg = config["monsters"][mtype]
        for i, h in enumerate(hexes):
            uid = f"{mtype}_{i}"
            st.monsters[uid] = Monster(uid=uid, mtype=mtype, chips=0, max_chips=cfg["hp"],
                                       hexpos=h, alive=False, respawn_round=cfg["spawn"])
    st.touch()
    st.refresh_visibility(allow_flip_back=True)
    return st


# --------------------------------------------------------------------- Upkeep
def upkeep(state: GameState, game: "Game") -> None:
    cfg = state.config
    state.round += 1
    if state.round > 1:
        state.priority = other(state.priority)

    for c in state.champs.values():                      # step 2
        c.activated = False
        if c.track > 0:
            c.track -= 1
            if c.track == 0 and not c.alive:
                respawn(state, c)
        if c.shield_until < state.round:
            c.shield = 0
    for t in state.teams.values():
        if t.baron_track > 0:
            t.baron_track -= 1

    base_tiles = {t: state.board.tile_of[state.board.fountain[t]] for t in TEAMS}
    for c in state.champs.values():                      # step 3
        if c.alive and state.board.tile_of[c.hexpos] == base_tiles[c.team]:
            c.hp = c.max_hp

    for t in TEAMS:                                      # step 4
        ts = state.teams[t]
        ts.ap = 0
        ts.gain(cfg["ap_base"] + min(ts.dragons, cfg["dragon_cap"]), "base")

    order = [state.priority, other(state.priority)]
    for team in order:                                   # step 5
        move_waves(state, team)
    state.refresh_visibility(allow_flip_back=True, placer=game.placer)

    if state.round % 2 == 1 or not cfg["wave_spawn_odd_rounds_only"]:   # step 6
        spawn_waves(state)
    for m in state.monsters.values():                    # step 7
        if not m.alive and state.round >= m.respawn_round:
            # RQ-018: a monster only reappears when its own hex is clear.
            blocked = any(u.alive and u.uid != m.uid and u.hexpos == m.hexpos
                          for u in state.all_units())
            if not blocked:
                m.alive = True
                m.chips = m.max_chips
                state.touch()
    state.refresh_visibility(allow_flip_back=True, placer=game.placer)    # step 8


def spawn_waves(state: GameState) -> None:
    cfg = state.config
    if state.round >= cfg.get("wave_growth_round2", 10 ** 6):
        size = cfg["wave_chips_late2"]
    elif state.round >= cfg["wave_growth_round"]:
        size = cfg["wave_chips_late"]
    else:
        size = cfg["wave_chips"]
    for team in TEAMS:
        bonus = cfg["baron_wave_bonus"] if state.teams[team].baron_track > 0 else 0
        for lane, hexpos in state.board.spawn[team].items():
            node = state.board.node_of(hexpos, state.hidden_mask)
            occupants = [u for u in state.units_at(node) if u.hexpos == hexpos]
            friendly_wave = next((u for u in occupants if u.kind == "wave" and u.team == team), None)
            if friendly_wave is not None:
                friendly_wave.chips += size + bonus
                continue
            if occupants:
                # Rules 9.1 [DEFAULT] + RQ-027: any other unit on the spawn hex
                # (an enemy, or a friendly champion) skips that spawn.
                continue
            uid = f"w{state.next_uid}"
            state.next_uid += 1
            state.waves[uid] = Wave(uid=uid, team=team, lane=lane, chips=size + bonus,
                                    path_idx=0, hexpos=hexpos,
                                    empowered=state.teams[team].baron_track > 0)
            state.touch()


def move_waves(state: GameState, team: str) -> None:
    waves = sorted([w for w in state.waves.values() if w.team == team],
                   key=lambda w: -w.path_idx)
    for w in waves:
        path = state.board.lane_paths[team][w.lane]
        steps = state.config["wave_speed"]
        landed = w.path_idx
        pos = w.path_idx
        for _ in range(steps):
            if pos + 1 >= len(path):
                break
            nxt = path[pos + 1]
            node = state.board.node_of(nxt, state.hidden_mask)
            units = [u for u in state.units_at(node)
                     if u.uid != w.uid and (node[0] == "T" or u.hexpos == nxt)]
            if node[0] == "T" and any(u.team not in (None, team) for u in units):
                state.force_visible(state.board.tile_of[nxt])
                break                                   # Rules 3.3: mover stops
            blocked = any(u.team not in (None, team) or u.kind == "monster" for u in units)
            if blocked:
                break
            pos += 1
            occupied_by_friend = any(
                u.uid != w.uid and u.hexpos == nxt and u.team == team for u in state.units_at(
                    state.board.node_of(nxt, state.hidden_mask)))
            if not occupied_by_friend:
                landed = pos
        if landed != w.path_idx:
            w.path_idx = landed
            w.hexpos = path[landed]
            state.touch()


# --------------------------------------------------------------- Action Phase
def champion_speed(state: GameState, c: Champion, tonic: bool = False) -> int:
    sp = c.speed - c.slow + (2 if tonic else 0)
    if c.rooted:
        return 0
    return max(0, sp)


def ability_ready(state: GameState, c: Champion, key: str) -> bool:
    ab = state.kits[c.cid]["abilities"][key]
    return state.teams[c.team].ap >= ab.get("cost", 0)


def legal_activations(state: GameState, team: str,
                      record: Optional[dict] = None) -> List[Activation]:
    cfg = state.config["enum"]
    out: List[Activation] = []
    tonic_available = "swift_tonic" in state.teams[team].cards
    for c in state.champs.values():
        if c.team != team or not c.alive or c.track != 0 or c.activated:
            continue
        node = state.node_of_unit(c)
        speed = champion_speed(state, c)
        dests = reachable(state, c, node, speed, include_start=True)
        dests = _cap(dests, cfg["max_dest"])
        # Recall (Rules 5.2): 1 movement from inside a hidden tile.
        recall_dests: List[Node] = []
        hidden_nodes = [nd for nd in reachable(state, c, node, speed, include_start=True)
                        if nd[0] == "T"]
        if hidden_nodes:
            cost = 0 if node[0] == "T" else 1
            if cost + 1 <= speed or (node[0] == "T" and speed >= 1):
                home = state.board.node_of(state.board.fountain[team], state.hidden_mask)
                budget = speed - (1 if node[0] == "T" else 2)
                if budget >= 0:
                    recall_dests = _cap(reachable(state, c, home, budget, include_start=True),
                                        max(2, cfg["max_dest"] // 3))
        abilities = [k for k in ("L0", "Q", "W", "E", "R") if ability_ready(state, c, k)]
        # RQ-034 is enforced inside target enumeration: an untagged ability
        # simply finds no legal target outside its hexgroup, so it drops out.
        home_node = state.board.node_of(state.board.fountain[team], state.hidden_mask)
        keep: List[Activation] = []          # canonical options, never sampled away
        core: List[Activation] = []          # other movement-only options
        per_champ: List[Activation] = []     # ability options, sampled under the cap
        keep.append(Activation(champ=c.uid, dest=node))      # stand still
        if recall_dests and home_node in recall_dests:
            keep.append(Activation(champ=c.uid, dest=home_node, recall=True))
        for dest in dests:
            if dest != node:
                core.append(Activation(champ=c.uid, dest=dest))
        for dest, recall in [(d, False) for d in dests] + [(d, True) for d in recall_dests]:
            if recall and not (dest == home_node):
                core.append(Activation(champ=c.uid, dest=dest, recall=True))
            for key in abilities:
                plans = enumerate_plans(state, c, dest, key, cfg["step_cap"], cfg["plan_cap"])
                if plans and record is not None and not recall:
                    record.setdefault("opp", set()).add((state.round, c.uid, key))
                for plan, _ in plans:
                    per_champ.append(Activation(champ=c.uid, dest=dest, recall=recall,
                                                ability=key, when="after", plan=plan))
                    if tonic_available and key != "L0":
                        per_champ.append(Activation(champ=c.uid, dest=dest, recall=recall,
                                                    ability=key, when="after", plan=plan,
                                                    tonic=True))
        # Ability first, then move (Rules 5.2).
        for key in abilities:
            for plan, endnode in enumerate_plans(state, c, node, key, cfg["step_cap"],
                                                 max(2, cfg["plan_cap"] // 2)):
                if record is not None:
                    record.setdefault("opp", set()).add((state.round, c.uid, key))
                for dest in _cap(reachable(state, c, endnode, speed, include_start=True),
                                 max(3, cfg["max_dest"] // 3)):
                    per_champ.append(Activation(champ=c.uid, dest=dest, ability=key,
                                                when="before", plan=plan))
        for tile, stop in flip_entry_options(state, c, node, speed)[:4]:
            # Stop at the edge, or push on into the tile once it flips (RQ-016).
            core.append(Activation(champ=c.uid, dest=stop, flip_entry=tile))
            spent = movement_cost(state, c, node, stop, speed)
            if spent is not None and speed - spent > 0:
                for h in _cap(list(state.board.tile_hexes[tile]), 2):
                    core.append(Activation(champ=c.uid, dest=stop, flip_entry=tile,
                                           intent=("H", h[0], h[1])))
        n_avail = max(1, len([x for x in state.champs.values()
                              if x.team == team and x.alive and x.track == 0
                              and not x.activated]))
        budget = max(14, state.config["enum"]["max_options"] // n_avail)
        keep_core = _cap(core, max(5, budget // 3))
        out.extend(keep)
        out.extend(keep_core)
        out.extend(_cap(per_champ, max(6, budget - len(keep) - len(keep_core))))
    out.append(PASS)
    return out


def _cap(seq: List, cap: int) -> List:
    if len(seq) <= cap:
        return list(seq)
    stride = len(seq) / cap
    return [seq[int(i * stride)] for i in range(cap)]


def apply_activation(state: GameState, act: Activation, game: "Game") -> None:
    if act.is_pass:
        return
    c = state.champs[act.champ]
    origin_node = state.node_of_unit(c)
    c.slow = 0
    c.rooted = False
    if act.tonic:
        state.teams[c.team].cards.remove("swift_tonic")
    if act.when == "before" and act.ability:
        pay_and_use(state, c, act)
    if act.recall:
        move_unit(state, c, state.board.node_of(state.board.fountain[c.team],
                                                state.hidden_mask))
    if act.dest is not None and act.dest != state.node_of_unit(c):
        move_unit(state, c, act.dest, state.node_of_unit(c))
    c.activations += 1
    # RQ-036 predicts two behaviours. This counts the first: ending an
    # activation on the edge of a hexgroup that holds enemies, which is the
    # move that looks into it. Merely bordering some other hexgroup is not
    # interesting - nearly every hex does.
    own = state.board.tile_of[c.hexpos]
    sets = state.tile_team_sets()
    for nb in state.board.neighbors.get(c.hexpos, ()):
        t = state.board.tile_of.get(nb)
        if t is None or t == own:
            continue
        if any(team != c.team for team in sets.get(t, ())):
            c.edge_rounds += 1
            break
    if act.flip_entry is not None:
        start = state.node_of_unit(c) if act.dest is None else act.dest
        state.force_visible(act.flip_entry, placer=game.placer)
        # RQ-016: the mover stopped for the flip; it may spend what is left of
        # its movement, now paying 1 per hex inside the revealed tile.
        if act.intent is not None:
            speed = champion_speed(state, c, act.tonic)
            spent = movement_cost(state, c, origin_node, start, speed) or 0
            remaining = speed - spent
            if remaining > 0:
                goal = (act.intent[1], act.intent[2])
                options = reachable(state, c, state.node_of_unit(c), remaining)
                best = None
                for nd in options:
                    if nd[0] != "H":
                        continue
                    d = abs(nd[1] - goal[0]) + abs(nd[2] - goal[1])
                    if best is None or d < best[0]:
                        best = (d, nd)
                if best is not None and best[1] != state.node_of_unit(c):
                    move_unit(state, c, best[1], state.node_of_unit(c))
    if act.when == "after" and act.ability:
        pay_and_use(state, c, act)
    c.activated = True
    state.activation_seq += 1


def pay_and_use(state: GameState, c: Champion, act: Activation) -> None:
    ab = state.kits[c.cid]["abilities"][act.ability]
    cost = ab.get("cost", 0)
    if cost:
        state.teams[c.team].spend(cost, "abilities")
    apply_plan(state, c, act.ability, act.plan)
    c.track = ability_cooldown(c, ab)


# ---------------------------------------------------------------- Card plays
def legal_card_plays(state: GameState, act: Activation) -> List[CardPlay]:
    if act.is_pass or act.ability is None:
        return []
    c = state.champs[act.champ]
    team = state.teams[c.team]
    out: List[CardPlay] = []
    node = state.node_of_unit(c)
    for card in sorted(set(team.cards)):
        if card == "swift_tonic":
            continue                       # offered through the activation itself
        if card == "blue_buff":
            out.append(CardPlay(card))
        elif card == "red_buff":
            for u in adjacent_units(state, node, exclude=c.uid):
                if can_be_hit(state, u, c.team, "enemy_any"):
                    out.append(CardPlay(card, u.uid))
        elif card == "health_potion":
            if c.hp < c.max_hp:
                out.append(CardPlay(card))
        elif card == "control_ward":
            tiles = {state.board.node_tile(node)}
            for nb in state.board.graph_neighbors(node, state.hidden_mask):
                tiles.add(state.board.node_tile(nb))
            for t in sorted(tiles):
                out.append(CardPlay(card, t))
        elif card == "frost_charm":
            for u, _ in units_within(state, node, 2, c.team, "enemy_champion"):
                out.append(CardPlay(card, u.uid))
        elif card == "stopwatch":
            for m in state.champs.values():
                if m.team == c.team and m.track > 0:
                    out.append(CardPlay(card, m.uid))
    return out


def apply_card(state: GameState, act: Activation, play: CardPlay) -> None:
    c = state.champs[act.champ]
    team = state.teams[c.team]
    if play.card not in team.cards:
        return
    team.cards.remove(play.card)
    if play.card == "blue_buff":
        team.gain(2, "blue_buff")
    elif play.card == "red_buff":
        tgt = state.unit(play.target)
        if tgt is not None and tgt.alive:
            deal_hits(state, c.team, tgt, 2, "red_buff", c)
    elif play.card == "health_potion":
        c.hp = min(c.max_hp, c.hp + 3)
    elif play.card == "control_ward":
        state.wards[play.target] = state.round + 1
        state.refresh_visibility(allow_flip_back=False)
    elif play.card == "frost_charm":
        tgt = state.unit(play.target)
        if tgt is not None and tgt.kind == "champion":
            tgt.slow += 2
    elif play.card == "stopwatch":
        tgt = state.champs.get(play.target)
        if tgt is not None and tgt.track > 0:
            tgt.track -= 1
            if tgt.track == 0 and not tgt.alive:
                respawn(state, tgt)


# ---------------------------------------------------------------- World Phase
def world_phase(state: GameState) -> None:
    cfg = state.config
    pending: List[Tuple[object, int, Optional[str]]] = []
    for w in list(state.waves.values()):
        if not w.alive:
            continue
        for u in effect_adjacent(state, w):
            if not can_be_hit(state, u, w.team, "enemy_any"):
                continue
            hits = 1
            if w.empowered and u.kind == "structure":
                hits = 2
            pending.append((u, hits, w.team))
    for s in state.structures.values():
        if not s.alive or s.stype != "tower":
            continue
        for u in effect_adjacent(state, s):
            if u.team == s.team or u.team is None:
                continue
            if u.kind == "champion":
                pending.append((u, cfg["tower_hits_champion"], s.team))
            elif u.kind == "wave":
                pending.append((u, cfg["tower_hits_wave"], s.team))
    for m in state.monsters.values():
        if not m.alive:
            continue
        for u in effect_adjacent(state, m):
            if u.kind == "champion":
                pending.append((u, cfg["monster_hits"], None))
    # Simultaneous application (Rules 5.3).
    totals: Dict[str, Tuple[object, int, Optional[str]]] = {}
    for u, k, team in pending:
        if "cloth_armor" in getattr(u, "items", ()):    # Rules 12
            k = max(0, k - 1)
        if k == 0:
            continue
        cur = totals.get(u.uid)
        totals[u.uid] = (u, (cur[1] if cur else 0) + k, team if cur is None else cur[2])
    for uid, (u, k, team) in totals.items():
        if u.alive:
            deal_hits(state, team, u, k, "world", None)


# ----------------------------------------------------------------- Shop Phase
def legal_purchases(state: GameState, team: str) -> List[Purchase]:
    ts = state.teams[team]
    out: List[Purchase] = []
    for item, spec in STAT_ITEMS.items():
        if spec["cost"] > ts.ap:
            continue
        for c in state.champs.values():
            if c.team == team and item not in c.items:
                out.append(Purchase(item, c.uid))
    for item, spec in CARD_ITEMS.items():
        if spec["cost"] <= ts.ap and ts.cards.count(item) < MAX_CARD_COPIES:
            out.append(Purchase(item))
    return out


def apply_purchase(state: GameState, team: str, p: Purchase) -> bool:
    ts = state.teams[team]
    cost = ALL_ITEMS[p.item]["cost"]
    if cost > ts.ap:
        return False
    if p.item in STAT_ITEMS:
        c = state.champs.get(p.champ)
        if c is None or p.item in c.items:
            return False
        c.items.add(p.item)
        if p.item == "ruby_crystal":
            c.max_hp += 2
            c.hp = min(c.max_hp, c.hp + 2)
        elif p.item == "boots":
            c.speed = min(5, c.speed + 1)
    else:
        if ts.cards.count(p.item) >= MAX_CARD_COPIES:
            return False
        ts.cards.append(p.item)
    ts.spend(cost, "shop")
    ts.items_bought[p.item] = ts.items_bought.get(p.item, 0) + 1
    return True


# ----------------------------------------------------------------- assertions
def assert_state(state: GameState) -> List[str]:
    errs = []
    seen: Dict[Hex, str] = {}
    for u in state.all_units():
        if not u.alive:
            continue
        tile = state.board.tile_of[u.hexpos]
        if not (state.hidden_mask >> tile & 1):
            if u.hexpos in seen:
                errs.append(f"stacking: {u.uid} and {seen[u.hexpos]} on {u.hexpos}")
            seen[u.hexpos] = u.uid
        if u.kind == "champion":
            if not 0 < u.hp <= u.max_hp:
                errs.append(f"hp out of range: {u.uid} {u.hp}/{u.max_hp}")
            if not 0 <= u.track <= 4:
                errs.append(f"track out of range: {u.uid} {u.track}")
        elif getattr(u, "chips", 1) < 0:
            errs.append(f"negative chips: {u.uid}")
    for t in state.teams.values():
        if t.ap < 0:
            errs.append(f"negative AP: {t.team}")
    for t in range(state.board.n_tiles):
        if state.hidden_mask >> t & 1:
            teams = {u.team for u in state.all_units()
                     if u.alive and u.kind != "monster" and state.board.tile_of[u.hexpos] == t}
            if len(teams) > 1:
                errs.append(f"hidden tile {t} holds both teams")
    return errs
