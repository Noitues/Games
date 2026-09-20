"""Enumeration and execution of ability icon sequences (Rules 6.3)."""
from __future__ import annotations

from typing import List, Optional, Tuple

from .hexmap import DIRS, Node
from .resolve import (ability_range, can_be_hit, deal_hits, effect_context,
                      line_targets, move_unit, push_pull, step_choices,
                      units_within)
from .state import Champion, GameState

Plan = Tuple


def enumerate_plans(state: GameState, champ: Champion, node: Node, ability: str,
                    step_cap: int = 4, plan_cap: int = 8) -> List[Tuple[Plan, Node]]:
    """All target/placement choices for an ability used from ``node``.

    Enumeration reads the state as it is now: it does not model a step's own
    effect on later steps (for instance a HIT that kills its target before a
    follow-up step). Execution resolves steps for real, in order.
    """
    steps = state.kits[champ.cid]["abilities"][ability]["steps"]
    partial: List[Tuple[Plan, Node, Optional[str]]] = [((), node, None)]
    for step in steps:
        nxt = []
        for plan, nd, prev in partial:
            choices = step_choices(state, champ, nd, step, prev, ability, step_cap)
            if not choices:
                continue
            for ch in choices:
                nd2 = nd
                prev2 = prev
                if step["icon"] in ("MOVE", "DASH", "BLINK"):
                    nd2 = ch
                elif step["icon"] == "HIT":
                    prev2 = ch
                elif step["icon"] in ("PUSH", "PULL", "SLOW", "ROOT", "DELAY") and \
                        step.get("target") != "prev" and ch is not None:
                    prev2 = ch
                nxt.append((plan + (ch,), nd2, prev2))
            if len(nxt) > plan_cap * 4:
                break
        partial = nxt[: plan_cap * 4]
        if not partial:
            return []
    out = [(p, nd) for p, nd, _ in partial]
    if len(out) > plan_cap:
        stride = len(out) / plan_cap
        out = [out[int(i * stride)] for i in range(plan_cap)]
    return out


def apply_plan(state: GameState, champ: Champion, ability: str, plan: Plan) -> None:
    steps = state.kits[champ.cid]["abilities"][ability]["steps"]
    prev_uid: Optional[str] = None
    long_sword = "long_sword" in champ.items and ability == "L0"
    for i, step in enumerate(steps):
        ch = plan[i] if i < len(plan) else None
        ic = step["icon"]
        node = state.node_of_unit(champ)
        if ic == "HIT":
            tgt = state.unit(ch) if ch else None
            if tgt is None or not tgt.alive:
                continue
            k = step.get("k", 1) * (2 if long_sword else 1)
            deal_hits(state, champ.team, tgt, k, "chips_" + tgt.kind, champ)
            prev_uid = ch
        elif ic == "AREA":
            r = ability_range(champ, ability, step.get("range", 1))
            for u, _ in units_within(state, node, r, champ.team,
                                     step.get("target", "enemy_any"), champ.hexpos):
                deal_hits(state, champ.team, u, step.get("k", 1), "chips_" + u.kind, champ)
            prev_uid = None
        elif ic == "LINE":
            n = ability_range(champ, ability, step.get("n", 1))
            origin, src_tile = effect_context(state, node, champ.hexpos)
            d = DIRS[ch if ch is not None else 0]
            for u in line_targets(state, (origin[0], origin[1]), d, n, champ.team,
                                  step.get("target", "enemy_any"), src_tile):
                deal_hits(state, champ.team, u, step.get("k", 1), "chips_" + u.kind, champ)
            prev_uid = None
        elif ic in ("MOVE", "DASH", "BLINK"):
            if ch is not None and ch != node:
                move_unit(state, champ, ch, node)
        elif ic in ("PUSH", "PULL"):
            tgt = state.unit(prev_uid if step.get("target") == "prev" else ch)
            if tgt is not None and tgt.alive:
                push_pull(state, champ, tgt, step.get("n", 1), away=(ic == "PUSH"))
                prev_uid = tgt.uid
        elif ic == "SLOW":
            tgt = state.unit(prev_uid if step.get("target") == "prev" else ch)
            if tgt is not None and tgt.alive and tgt.kind == "champion":
                tgt.slow += step.get("n", 1)
        elif ic == "ROOT":
            if step.get("area"):
                for u, _ in units_within(state, node, ability_range(champ, ability, 1),
                                         champ.team, "enemy_champion", champ.hexpos):
                    u.rooted = True
            else:
                tgt = state.unit(prev_uid if step.get("target") == "prev" else ch)
                if tgt is not None and tgt.alive and tgt.kind == "champion":
                    tgt.rooted = True
        elif ic == "DELAY":
            tgt = state.unit(prev_uid if step.get("target") == "prev" else ch)
            if tgt is not None and tgt.alive and tgt.kind == "champion":
                tgt.track = min(4, max(1, tgt.track + 1))
        elif ic == "HEAL":
            tgt = champ if step.get("target") == "self" else state.unit(ch)
            if tgt is not None and tgt.alive:
                tgt.hp = min(tgt.max_hp, tgt.hp + step.get("n", 1))
        elif ic == "SHIELD":
            tgt = champ if step.get("target") == "self" else state.unit(ch)
            if tgt is not None and tgt.alive:
                tgt.shield = max(tgt.shield, step.get("n", 1))
                tgt.shield_until = state.round + 1
        elif ic == "HASTE":
            tgt = champ if step.get("target") == "self" else state.unit(ch)
            if tgt is not None and tgt.track > 0:
                tgt.track -= 1
                if tgt.track == 0 and not tgt.alive:
                    respawn(state, tgt)
        elif ic == "REVEAL":
            if ch is not None:
                state.wards[ch] = state.round
                state.refresh_visibility(allow_flip_back=False)
    state.touch()


def respawn(state: GameState, champ: Champion) -> None:
    """Rules 5.1 step 2 / 6.4: return to the fountain at full HP."""
    board = state.board
    home = board.fountain[champ.team]
    node = board.node_of(home, state.hidden_mask)
    spot = home
    if not state.can_stop(node, champ.team):
        base_tile = board.tile_of[home]
        for h in board.tile_hexes[base_tile]:
            nd = board.node_of(h, state.hidden_mask)
            if state.can_stop(nd, champ.team):
                spot = h
                break
    champ.hexpos = spot
    champ.alive = True
    champ.hp = champ.max_hp
    champ.shield = 0
    champ.slow = 0
    champ.rooted = False
    state.touch()
