"""Scene-Deck Engine state machine.

Pure, deterministic game state for RULES_SPEC.md v0.1.0. Agents never touch this state directly:
the orchestrator (run.py) asks agents for *choices*, and this module validates and applies them.
Illegal choices are refused and recorded as VIOLATIONs against the agent that made them.

All randomness comes from seeded ``random.Random`` streams owned by the engine. The dice stream is
separate from the deck, scene-test and story streams, so the k-th 4dF roll of a seed is identical
in every arm (common random numbers).
"""

from __future__ import annotations

import copy
import hashlib
import itertools
import random
from dataclasses import dataclass, field
from typing import Any

from rulings import Rulings

SPEC_VERSION = "0.1.0"

LADDER = {-2: "Terrible", -1: "Poor", 0: "Mediocre", 1: "Average", 2: "Fair", 3: "Good",
          4: "Great", 5: "Superb", 6: "Fantastic", 7: "Epic", 8: "Legendary"}

BLANK_FOR_TYPE = {"ROOTS": "WHO", "REACH": "WHY", "THREAT": "HOW", "FACTION": "WHO",
                  "HAZARD": "HOW", "LOCATION": "WHERE", "CULTURE": "WHY", "NPC": "WHO",
                  "THREAD": "WHY"}
GM_TYPES = {"THREAT", "FACTION", "HAZARD", "LOCATION", "CULTURE"}
PLAYER_TYPES = {"ROOTS", "REACH"}
RAIL_LIMIT = 5
ROLL_ACTIONS = {"overcome", "create_advantage", "attack"}


class EngineError(Exception):
    """Raised for harness bugs (not agent mistakes)."""


class InvalidRun(Exception):
    """Raised when a run must be discarded, e.g. an agent claimed a dice result."""


def ladder(n: int) -> str:
    return f"{LADDER.get(n, 'Beyond Legendary' if n > 8 else 'Abysmal')} ({n:+d})"


def fmt_dice(d: list[int]) -> str:
    return " ".join({-1: "-", 0: "0", 1: "+"}[x] for x in d)


def derive_seed(seed: int, stream: str) -> int:
    return int(hashlib.sha256(f"{seed}:{stream}".encode()).hexdigest()[:16], 16)


@dataclass
class Card:
    id: str
    type: str
    owner: str
    title: str
    power_tags: list[str]
    weakness: str
    track_kind: str = "none"
    track_size: int = 0
    marks: int = 0
    origin: str = "world"          # world | player | placebo | story | scene
    assigned_player: str | None = None   # placebo cards: which player it stands in for
    blurb: str = ""
    growth: int = 0
    owner_display: str | None = None

    @classmethod
    def from_json(cls, d: dict, origin: str = "world") -> "Card":
        tr = d.get("track", {})
        return cls(id=d["id"], type=d["type"], owner=d["owner"], title=d["title"],
                   power_tags=list(d["power_tags"]), weakness=d.get("weakness", ""),
                   track_kind=tr.get("kind", "none"), track_size=tr.get("size", 0),
                   origin=origin, blurb=d.get("blurb", ""))

    def tags(self) -> list[str]:
        return self.power_tags + ([self.weakness] if self.weakness else [])

    def brief(self) -> dict:
        owner = self.owner
        if self.origin == "placebo":   # never reveal the placebo source to any agent
            owner = self.owner_display or "GM"
        d = {"id": self.id, "type": self.type, "owner": owner, "title": self.title,
             "power_tags": self.power_tags, "weakness": self.weakness}
        if self.track_kind == "clock":
            d["clock"] = f"{self.marks}/{self.track_size}"
        if self.track_kind == "weight":
            d["weight"] = self.track_size
        return d


@dataclass
class Character:
    id: str
    name: str
    pronouns: str
    concept: str
    skills: dict[str, int]
    binder: list[str]                      # card ids (4 theme cards, or 5 FAE aspect pseudo-cards)
    personality: str = ""
    refresh: int = 3
    fp: int = 0
    stress: dict[str, list[list]] = field(default_factory=dict)   # track -> [[value, checked], ...]
    consequences: dict[str, dict | None] = field(default_factory=lambda: {"mild": None, "moderate": None, "severe": None})
    card_state: dict[str, str] = field(default_factory=dict)       # binder | deck | setaside | rail | sacrificed
    strained: dict[str, dict] = field(default_factory=dict)        # card_id -> {"level", "tag"}
    out_of_scene: bool = False
    conceded_scene: int | None = None
    taken_out_scene: int | None = None
    story_pile: list[str] = field(default_factory=list)

    def code(self) -> str:
        return f"PC-{self.name.split()[0].upper()}"


@dataclass
class NPC:
    name: str
    rating: int
    stress: list[list]
    hostile: bool = True
    card_id: str | None = None
    mild_free: bool = True
    out: bool = False


@dataclass
class RollCtx:
    event_id: int
    actor: str
    action: str
    skill: str
    skill_rating: int
    target_card: str | None
    target_npc: str | None
    dice: list[int]
    opposition: int
    opp_kind: str
    opp_dice: list[int] | None
    opposing_tags: list[tuple[str, str]]
    gm_invokes: list[tuple[str, str]]
    hostile_invokes: list[tuple[str, str]]
    player_invokes: list[tuple[str, str]] = field(default_factory=list)
    fp_spent: int = 0
    bonus: int = 0
    gm_bonus: int = 0
    description: str = ""
    advantage_name: str = ""

    @property
    def total(self) -> int:
        return self.skill_rating + sum(self.dice) + self.bonus

    @property
    def opp_total(self) -> int:
        return self.opposition + self.gm_bonus

    @property
    def shifts(self) -> int:
        return self.total - self.opp_total


class Engine:
    """One table: a cohort, a prep packet, an arm config and a seed."""

    def __init__(self, *, arm: dict, characters: list[dict], prep: dict, world: dict,
                 placebo: dict, seed: int, tension: int = 3, max_scenes: int = 5):
        self.arm = arm
        self.seed = seed
        self.rng = {s: random.Random(derive_seed(seed, s)) for s in
                    ("dice", "deck", "scene_test", "story", "offscreen", "misc", "placebo")}
        self.rulings = Rulings()
        self.events: list[dict] = []
        self.transcript: list[dict] = []
        self.violations: list[dict] = []
        self.cards: dict[str, Card] = {}
        self.world = world
        self.placebo = placebo
        self.prep = copy.deepcopy(prep)
        self.tension = tension
        self.max_scenes = max_scenes
        self.session = 0
        self.scene = 0
        self.scene_in_session = 0
        self.climax_scene: int | None = None
        self.session_over = False
        self.deck: list[str] = []
        self.discard: list[str] = []
        self.surfaced: set[str] = set()          # player/placebo cards surfaced this session
        self.deck_player_cards: dict[str, str] = {}   # deck card id -> player id it represents
        self.setaside: dict[str, str] = {}       # player id -> binder card set aside (Arm C)
        self.guarantee_pulled: list[str] = []
        self.guarantee_failed: list[str] = []
        self.rail: list[str] = []
        self.gm_fp = 0
        self.free_invokes: dict[tuple[str, str], int] = {}   # (holder, source_id) -> n
        self.hostile_payouts: list[str] = []
        self.scene_aspects: list[str] = []
        self.npcs: dict[str, NPC] = {}
        self.queued_beats: list[dict] = []
        self.queued_modules: list[dict] = []
        self.growth_ledger: list[dict] = []
        self.gm_story_pile: list[str] = []
        self.retired: list[dict] = []
        self.left_play: list[dict] = []
        self.clock_filled: list[dict] = []
        self.chronicle: list[dict] = []
        self.appeared_this_session: set[str] = set()
        self.rolled_against_this_session: set[str] = set()
        self.scene_flags: dict[str, Any] = {}
        self._eid = itertools.count(1)
        self._aid = itertools.count(1)
        self.story_featured: set[str] = set()
        self.draws_this_session = 0

        for c in world["cards"]:
            self.cards[c["id"]] = Card.from_json(c)
        for c in world.get("gm_story_pile", []):
            self.cards[c["id"]] = Card.from_json(c, origin="story")
            self.gm_story_pile.append(c["id"])
        for c in placebo["deck_cards"] + placebo["story_cards"]:
            self.cards[c["id"]] = Card.from_json(c, origin="placebo")

        self.chars: dict[str, Character] = {}
        for ch in characters:
            self._add_character(ch)
        self.order = [c["id"] for c in characters]

        if arm["deck"] and arm.get("attention_listed"):
            self.rulings.fire("AMB-01", "Arm definition lists Attention; not modelled.")
        self.rulings.fire("AMB-12", "stress boxes built with Fate Core values")

    # ------------------------------------------------------------------ setup helpers
    def _add_character(self, ch: dict) -> None:
        pid = ch["id"]
        if self.arm["cards"]:
            binder = []
            for c in ch["binder"]:
                card = Card.from_json(c, origin="player")
                self.cards[card.id] = card
                binder.append(card.id)
        else:   # Arm B: FAE aspects as single-tag pseudo-cards
            fae = ch["fae"]
            initials = ch["binder"][0]["id"].split("-")[0]
            code = f"PC-{ch['name'].split()[0].upper()}"
            entries = [("HC", "HIGH CONCEPT", fae["high_concept"]), ("TR", "TROUBLE", fae["trouble"])]
            entries += [(f"A{i+1}", "ASPECT", a) for i, a in enumerate(fae["aspects"])]
            binder = []
            for suffix, typ, text in entries:
                cid = f"{initials}-{suffix}"
                self.cards[cid] = Card(id=cid, type=typ, owner=code, title=text, power_tags=[text],
                                       weakness=text if typ == "TROUBLE" else "", origin="player")
                binder.append(cid)
        skills = dict(ch["skills"])
        if self.arm.get("resolution") == "fae":
            skills = dict(ch["approaches"])
        c = Character(id=pid, name=ch["name"], pronouns=ch.get("pronouns", "they/them"),
                      concept=ch["concept"], skills=skills, binder=binder,
                      personality=ch.get("personality", ""))
        c.card_state = {cid: "binder" for cid in binder}
        c.stress = {"physical": self._stress_boxes(skills.get("Physique", 0)),
                    "mental": self._stress_boxes(skills.get("Will", 0))}
        if self.arm["story_piles"]:
            if self.arm["placebo"]:
                taken = {x for other in self.chars.values() for x in other.story_pile}
                pool = [s["id"] for s in self.placebo["story_cards"] if s["id"] not in taken]
                picks = self.rng["placebo"].sample(pool, 2)
                for x in picks:
                    self.cards[x].owner_display = f"PC-{ch['name'].split()[0].upper()}"
                c.story_pile = picks
            else:
                for s in ch.get("story_cards", []):
                    self.cards[s["id"]] = Card.from_json(s, origin="story")
                    c.story_pile.append(s["id"])
        self.chars[pid] = c

    def _stress_boxes(self, rating: int) -> list[list]:
        boxes = [[1, False], [2, False]]
        if rating >= 1:
            boxes.append([3, False])
            if rating >= 3:
                boxes.append([4, False])
        return boxes

    # ------------------------------------------------------------------ logging
    def log(self, **row) -> dict:
        base = {"event_id": next(self._eid), "session": self.session, "scene": self.scene,
                "actor": "", "action": "", "skill": "", "tags_invoked": "", "fp_spent": 0,
                "dice": "", "total": "", "opposition": "", "result": "", "draw_id": "",
                "compel": "", "clock_change": "", "tension": self.tension if self.arm["tension"] else "",
                "notes": "", "event_type": "", "improvised": False}
        base.update(row)
        self.events.append(base)
        return base

    def say(self, speaker: str, text: str, kind: str = "narration", visible_to: str = "all") -> None:
        self.transcript.append({"session": self.session, "scene": self.scene, "speaker": speaker,
                                "kind": kind, "text": text, "visible_to": visible_to})

    def violation(self, agent: str, section: str, issue: str) -> None:
        self.violations.append({"session": self.session, "scene": self.scene, "agent": agent,
                                "section": section, "issue": issue, "source": "engine"})

    def fire(self, rid: str, detail: str = "") -> None:
        self.rulings.fire(rid, detail, self.scene)

    # ------------------------------------------------------------------ queries
    def name(self, pid: str) -> str:
        return self.chars[pid].name

    def pid_by_name(self, name: str) -> str | None:
        if name in self.chars:
            return name
        n = (name or "").strip().lower()
        for pid, c in self.chars.items():
            if c.name.lower() == n or c.name.split()[0].lower() == n:
                return pid
        return None

    def owner_pid(self, card: Card) -> str | None:
        if card.origin == "placebo" and card.assigned_player:
            return card.assigned_player
        for pid, c in self.chars.items():
            if card.id in c.binder:
                return pid
        return None

    def card_live_for_owner(self, pid: str, cid: str, tag: str | None = None) -> bool:
        ch = self.chars[pid]
        if cid not in ch.binder:
            return False
        if ch.card_state.get(cid) not in ("binder", "rail"):
            return False
        st = ch.strained.get(cid)
        if st:
            if st["level"] in ("moderate", "severe"):
                return False
            if st["level"] == "mild" and tag is not None and st.get("tag") == tag:
                return False
        return True

    def on_rail(self, cid: str) -> bool:
        return cid in self.rail

    def rail_gm_tags(self) -> list[tuple[str, str]]:
        out = []
        for cid in self.rail:
            c = self.cards[cid]
            if c.owner in ("GM", "GLOBAL") and c.origin == "world":
                out += [(cid, t) for t in c.tags()]
        return out

    def deck_card_for(self, pid: str) -> str | None:
        for cid, owner in self.deck_player_cards.items():
            if owner == pid:
                return cid
        return None

    # ------------------------------------------------------------------ session lifecycle
    def start_session(self) -> None:
        self.session += 1
        self.scene_in_session = 0
        self.session_over = False
        self.climax_scene = None
        self.surfaced = set()
        self.deck, self.discard = [], []
        self.deck_player_cards = {}
        self.setaside = {}
        self.guarantee_pulled, self.guarantee_failed = [], []
        self.appeared_this_session = set()
        self.rolled_against_this_session = set()
        self.growth_ledger = []
        self.draws_this_session = 0
        for c in self.chars.values():
            c.fp = max(c.refresh, c.fp)
            c.out_of_scene = False
        self.log(event_type="session_start", action="Session start",
                 notes=f"FP: " + ", ".join(f"{c.name}={c.fp}" for c in self.chars.values()))
        # Anchors onto the rail (GLOBAL cards already on the rail from earlier sessions stay).
        for cid in self.prep["anchors"]:
            if cid not in self.rail:
                self.place_on_rail(cid, reason="anchor", gm_free_invoke=True)
        if self.arm["deck"]:
            self._build_deck()

    def _build_deck(self) -> None:
        env = list(self.prep["environment"])
        deck = list(env)
        drng = self.rng["deck"]
        placebo_pool = [c["id"] for c in self.placebo["deck_cards"]]
        for pid in self.order:
            ch = self.chars[pid]
            candidates = [cid for cid in ch.binder if ch.card_state.get(cid) == "binder"]
            pick = drng.choice(sorted(candidates))
            if self.arm["placebo"]:
                ch.card_state[pick] = "setaside"
                self.setaside[pid] = pick
                typ = self.cards[pick].type
                pool = [p for p in placebo_pool if self.cards[p].type == typ
                        and p not in self.deck_player_cards]
                pc = drng.choice(sorted(pool))
                self.cards[pc].assigned_player = pid
                self.cards[pc].owner_display = ch.code()
                self.deck_player_cards[pc] = pid
                deck.append(pc)
            else:
                ch.card_state[pick] = "deck"
                self.deck_player_cards[pick] = pid
                deck.append(pick)
        drng.shuffle(deck)
        self.deck = deck
        self.log(event_type="deck_built", action="Build Session Deck",
                 notes=f"{len(deck)} cards: {len(env)} GM + {len(self.order)} player")

    def start_scene(self) -> dict:
        """Begin a scene. Returns what the orchestrator must handle before framing."""
        self.scene += 1
        self.scene_in_session += 1
        self.scene_flags = {"clock_advanced": False, "failed_against": set(), "compel_refused": False,
                            "rolls_against": set(), "story_drawn": [], "draws": [],
                            "is_climax": self.climax_scene == self.scene}
        self.scene_aspects = []
        self.npcs = {}
        for c in self.chars.values():
            c.out_of_scene = False
        self.gm_fp = len(self.chars) * self.arm.get("gm_fp_per_player", 1)
        if self.arm.get("gm_fp_flat") is not None:
            self.gm_fp = self.arm["gm_fp_flat"]
        # Deploy modules that fired at the previous cleanup.
        for m in self.queued_modules:
            for cid in m["cards"]:
                self.place_on_rail(cid, reason=f"module {m['id']}", gm_free_invoke=True)
        self.queued_modules = []
        self.log(event_type="scene_start", action=f"Scene {self.scene} start",
                 notes=("CLIMAX" if self.scene_flags["is_climax"] else ""))
        return {"scene": self.scene, "is_climax": self.scene_flags["is_climax"]}

    def scene_test(self) -> dict:
        """§6 scene test. Returns {'result': 'as_planned'|'altered'|'interrupt'|'skipped', 'roll': d6}."""
        if not self.arm["tension"] or self.scene_in_session == 1:
            return {"result": "skipped", "roll": None}
        r = self.rng["scene_test"].randint(1, 6)
        if r > self.tension or r == 6:
            res = "as_planned"
        elif r % 2 == 1:
            res = "altered"
        else:
            res = "interrupt"
        self.log(event_type="scene_test", action="Scene test", dice=str(r), result=res,
                 notes=f"d6={r} vs Tension {self.tension}")
        return {"result": res, "roll": r}

    # ------------------------------------------------------------------ rail
    def place_on_rail(self, cid: str, reason: str, gm_free_invoke: bool = False) -> None:
        if cid in self.rail:
            return
        card = self.cards[cid]
        self.rail.append(cid)
        self.appeared_this_session.add(cid)
        if gm_free_invoke and self.arm["deck"] and card.owner in ("GM", "GLOBAL"):
            if card.owner == "GLOBAL":
                self.fire("AMB-22", cid)
            self.free_invokes[("GM", cid)] = self.free_invokes.get(("GM", cid), 0) + 1
        while len(self.rail) > RAIL_LIMIT:
            victim = next((x for x in self.rail if self.cards[x].owner == "GM"
                           and self.cards[x].origin == "world" and x != cid), None)
            if victim is None:
                victim = next((x for x in self.rail if self.cards[x].owner != "GLOBAL" and x != cid), None)
                self.fire("AMB-05", f"evicted {victim}")
            if victim is None:
                raise EngineError("rail full of GLOBAL cards")
            self.remove_from_rail(victim, to="discard", why="rail limit")
        self.log(event_type="rail_add", action=f"Rail + {cid}", draw_id=cid, notes=reason)

    def remove_from_rail(self, cid: str, to: str, why: str = "") -> None:
        if cid not in self.rail:
            return
        self.rail.remove(cid)
        card = self.cards[cid]
        if card.origin == "player":
            pid = self.owner_pid(card)
            if pid:
                self.chars[pid].card_state[cid] = "binder"
        elif card.origin == "placebo" and card.type in PLAYER_TYPES:
            pass   # placebo deck card simply leaves
        elif card.type in ("NPC", "THREAD") or card.origin == "story" or (
                card.origin == "placebo" and card.type in ("NPC", "THREAD")):
            pass   # returned to its pile at cleanup (pile membership never changes on draw)
        elif to == "discard":
            self.discard.append(cid)
        self.free_invokes.pop(("GM", cid), None)
        self.log(event_type="rail_remove", action=f"Rail - {cid}", draw_id=cid, notes=f"{to}: {why}")

    # ------------------------------------------------------------------ Session Deck
    ALLOWED_DRAWS = {"tie", "major_cost", "beat_frame", "altered_scene"}

    def draw(self, reason: str, actor: str = "GM") -> str | None:
        """Draw the top card of the Session Deck. Returns None if the deck is empty."""
        if reason not in self.ALLOWED_DRAWS:
            self.violation(actor, "§4", f"draw attempted for non-trigger reason '{reason}'")
            return None
        if reason == "altered_scene":
            self.fire("AMB-20")
        if not self.arm["deck"]:
            return None
        if not self.deck:
            return None
        cid = self.deck.pop(0)
        self.draws_this_session += 1
        self.scene_flags["draws"].append(cid)
        self.log(event_type="draw", action=f"Draw ({reason})", draw_id=cid,
                 notes=f"deck now {len(self.deck)}")
        self._after_draw()
        return cid

    def _after_draw(self) -> None:
        if not self.deck and self.climax_scene is None:
            self.climax_scene = self.scene + 1
            self.fire("AMB-03", f"deck exhausted in scene {self.scene}; climax = scene {self.scene + 1}")
            self.log(event_type="deck_exhausted", action="Deck exhausted",
                     notes=f"climax is scene {self.scene + 1}")
        if len(self.deck) <= 2:
            unsurfaced = [cid for cid in self.deck if cid in self.deck_player_cards]
            for cid in unsurfaced:
                self.deck.remove(cid)
                self.guarantee_pulled.append(cid)
                self.log(event_type="guarantee_pull", action="Backstory guarantee pull", draw_id=cid,
                         notes=f"owner {self.name(self.deck_player_cards[cid])}")
            if unsurfaced:
                self.fire("AMB-02", f"pulled {unsurfaced}")
                if not self.deck and self.climax_scene is None:
                    self.climax_scene = self.scene + 1

    def peek(self) -> str | None:
        return self.deck[0] if self.deck else None

    def peek_move_to_bottom(self) -> None:
        if len(self.deck) > 1:
            self.deck.append(self.deck.pop(0))

    def is_player_deck_card(self, cid: str) -> bool:
        return cid in self.deck_player_cards

    def surface(self, cid: str) -> None:
        """§4.5: the drawn player (or placebo stand-in) card goes face-up, is live, owner gets a free invoke."""
        pid = self.deck_player_cards[cid]
        ch = self.chars[pid]
        self.surfaced.add(cid)
        if self.arm["placebo"]:
            orig = self.setaside.get(pid)
            if orig and ch.card_state.get(orig) == "setaside":
                ch.card_state[orig] = "binder"
        else:
            ch.card_state[cid] = "rail"
        self.place_on_rail(cid, reason=f"surfaced ({ch.name})")
        n = self.arm.get("surface_free_invokes", 1)
        if n:
            self.free_invokes[(pid, cid)] = self.free_invokes.get((pid, cid), 0) + n
        self.log(event_type="surface", actor=ch.name, action="Card surfaces", draw_id=cid,
                 notes=f"{n} free invoke(s)")

    def place_drawn_gm_card(self, cid: str) -> None:
        self.place_on_rail(cid, reason="drawn from Session Deck", gm_free_invoke=True)

    # ------------------------------------------------------------------ compels
    def resolve_compel(self, pid: str, accept: bool, *, card_id: str | None, tag: str,
                       from_deck: bool, text: str) -> dict:
        ch = self.chars[pid]
        forced = False
        if not accept and ch.fp < 1:
            accept, forced = True, True
            self.violation(ch.name, "§11", "tried to refuse a compel with 0 fate points (forced accept)")
        if accept:
            ch.fp += 1
            if card_id and card_id in ch.binder:
                self.growth_ledger.append({"card": card_id, "why": "compel accepted", "scene": self.scene})
        else:
            ch.fp -= 1
            self.scene_flags["compel_refused"] = True
        ev = self.log(event_type="compel", actor=ch.name, action="Compel" + (" (deck)" if from_deck else ""),
                      tags_invoked=tag, compel="accepted" if accept else "refused",
                      fp_spent=0 if accept else 1, draw_id=card_id or "",
                      notes=text[:200], improvised=not from_deck,
                      compel_forced=forced)
        return {"accepted": accept, "forced": forced, "event": ev}

    # ------------------------------------------------------------------ rolls
    def skill_rating(self, pid: str, skill: str) -> tuple[str, int]:
        ch = self.chars[pid]
        for k, v in ch.skills.items():
            if k.lower() == (skill or "").lower():
                return k, v
        return (skill or "Unskilled"), 0

    def roll4df(self) -> list[int]:
        return [self.rng["dice"].choice((-1, 0, 1)) for _ in range(4)]

    def begin_roll(self, pid: str, *, action: str, skill: str, target_card: str | None,
                   target_npc: str | None, opp: dict, description: str = "",
                   advantage_name: str = "") -> RollCtx:
        ch = self.chars[pid]
        skill_name, rating = self.skill_rating(pid, skill)
        opposing: list[tuple[str, str]] = []
        gm_inv: list[tuple[str, str]] = []
        hostile: list[tuple[str, str]] = []
        opp_dice = None
        kind = opp.get("kind", "passive")
        if target_npc and target_npc in self.npcs and not self.npcs[target_npc].out:
            kind = "active"
        rail_tags = set(self.rail_gm_tags())
        for t in opp.get("opposing_tags", []):
            key = (t.get("card_id"), t.get("tag"))
            if key in rail_tags and key not in opposing:
                opposing.append(key)
            else:
                self.violation("GM", "§3", f"opposing tag not a face-up GM/GLOBAL tag: {key}")
        if kind == "active":
            npc = self.npcs.get(target_npc or opp.get("npc", ""))
            if npc is None:
                self.violation("GM", "§3", f"active opposition from unknown NPC {opp.get('npc')}")
                kind = "passive"
        if kind == "active":
            opp_dice = self.roll4df()
            base = npc.rating + sum(opp_dice)
            if npc.card_id:
                self.scene_flags["rolls_against"].add(npc.card_id)
        else:
            base = min(1 + len(opposing), self.arm.get("max_passive", 4))
        for cid, _ in opposing:
            self.scene_flags["rolls_against"].add(cid)
            self.rolled_against_this_session.add(cid)
        if target_card and target_card in self.rail and self.cards[target_card].origin == "world":
            self.rolled_against_this_session.add(target_card)
        ctx = RollCtx(event_id=0, actor=pid, action=action, skill=skill_name, skill_rating=rating,
                      target_card=target_card, target_npc=target_npc, dice=self.roll4df(),
                      opposition=base, opp_kind=kind, opp_dice=opp_dice, opposing_tags=opposing,
                      gm_invokes=[], hostile_invokes=[], description=description,
                      advantage_name=advantage_name)
        # GM invokes, committed before the roll is revealed (AMB-11).
        for inv in opp.get("gm_invokes", []):
            key = (inv.get("card_id"), inv.get("tag"))
            if key in opposing:
                self.violation("GM", "§3", f"tag used for difficulty also invoked: {key}")
                continue
            if key in gm_inv:
                self.violation("GM", "§3", f"tag invoked twice on one roll: {key}")
                continue
            if not self._gm_can_invoke(key):
                self.violation("GM", "§3", f"GM invoke on a tag not in play: {key}")
                continue
            if not self._pay("GM", key[0], prefer_free=inv.get("pay", "free") == "free"):
                self.violation("GM", "§3", f"GM cannot pay for invoke {key}")
                continue
            gm_inv.append(key)
            ctx.gm_bonus += 2
            wcard = self.cards[key[0]]
            wowner = self.owner_pid(wcard) if wcard.origin in ("player", "placebo") else None
            if wowner == pid and key[1] == wcard.weakness:
                self.hostile_payouts.append(pid)   # §3: invoking a player's weakness against them is hostile
            self.scene_flags["rolls_against"].add(key[0])
            self.rolled_against_this_session.add(key[0])
        for h in opp.get("hostile_invokes", []):
            tpid = self.pid_by_name(h.get("player", ""))
            cid = h.get("card_id")
            if not tpid or cid not in self.cards:
                self.violation("GM", "§3", f"hostile invoke on unknown target {h}")
                continue
            card = self.cards[cid]
            tch = self.chars[tpid]
            if cid not in tch.binder or tch.card_state.get(cid) in ("deck", "setaside", "sacrificed"):
                self.violation("GM", "§11", f"hostile invoke on a card not in play ({cid})")
                continue
            if not card.weakness:
                self.violation("GM", "§3", f"hostile invoke on card without weakness ({cid})")
                continue
            if self.gm_fp < 1:
                self.violation("GM", "§3", "hostile invoke with no GM fate points")
                continue
            self.gm_fp -= 1
            hostile.append((cid, card.weakness))
            self.hostile_payouts.append(tpid)
            ctx.gm_bonus += 2
        ctx.gm_invokes, ctx.hostile_invokes = gm_inv, hostile
        return ctx

    def _gm_can_invoke(self, key: tuple[str, str]) -> bool:
        cid, tag = key
        if cid in self.rail and tag in self.cards[cid].tags():
            return True
        if cid in self.scene_aspects and tag in self.cards[cid].tags():
            return True
        return False

    def _pay(self, holder: str, source: str, prefer_free: bool = True) -> bool:
        k = (holder, source)
        if prefer_free and self.free_invokes.get(k, 0) > 0:
            self.free_invokes[k] -= 1
            if self.free_invokes[k] == 0:
                del self.free_invokes[k]
            return True
        if holder == "GM":
            if self.gm_fp > 0:
                self.gm_fp -= 1
                return True
            return False
        ch = self.chars[holder]
        if ch.fp > 0:
            ch.fp -= 1
            return True
        return False

    def invokable_for(self, pid: str) -> list[dict]:
        """Every (source, tag) the player could legally invoke right now, with its price."""
        out = []
        ch = self.chars[pid]
        for cid in ch.binder:
            if ch.card_state.get(cid) not in ("binder", "rail"):
                continue
            card = self.cards[cid]
            tags = card.power_tags if card.type not in ("TROUBLE",) else card.power_tags
            for t in tags:
                if self.card_live_for_owner(pid, cid, t):
                    out.append({"source_id": cid, "tag": t, "free": self.free_invokes.get((pid, cid), 0)})
        for cid in self.rail:
            if cid in ch.binder:
                continue
            card = self.cards[cid]
            if card.origin == "placebo" and card.type in PLAYER_TYPES and card.assigned_player == pid:
                for t in card.power_tags:
                    out.append({"source_id": cid, "tag": t, "free": self.free_invokes.get((pid, cid), 0)})
                continue
            for t in card.tags():
                out.append({"source_id": cid, "tag": t, "free": self.free_invokes.get((pid, cid), 0)})
        for aid in self.scene_aspects:
            card = self.cards[aid]
            out.append({"source_id": aid, "tag": card.title, "free": self.free_invokes.get((pid, aid), 0)})
        return out

    def apply_player_invokes(self, ctx: RollCtx, invokes: list[dict]) -> list[str]:
        pid = ctx.actor
        name = self.name(pid)
        legal = {(o["source_id"], o["tag"]) for o in self.invokable_for(pid)}
        applied = []
        for inv in invokes:
            key = (inv.get("source_id"), inv.get("tag"))
            if key in ctx.player_invokes:
                self.violation(name, "§3", f"tag invoked twice on one roll: {key}")
                continue
            if key not in legal:
                self.violation(name, "§3", f"invoke on a tag that is not live for them: {key}")
                continue
            paid_free = self.free_invokes.get((pid, key[0]), 0) > 0
            if not self._pay(pid, key[0], prefer_free=True):
                self.violation(name, "§3", f"cannot pay for invoke {key}")
                continue
            if not paid_free:
                ctx.fp_spent += 1
            ctx.player_invokes.append(key)
            ctx.bonus += 2
            applied.append(f"{key[1]} [{key[0]}]")
            card = self.cards[key[0]]
            if card.type == "BOOST":
                self._remove_scene_aspect(key[0])
        return applied

    def finalize_roll(self, ctx: RollCtx, *, take_major_cost: bool, use_story_ally: bool = False) -> dict:
        """Apply §3's outcome table. Returns the outcome and any deck draw needed."""
        pid = ctx.actor
        name = self.name(pid)
        s = ctx.shifts
        if s < 0:
            outcome = "success_major_cost" if take_major_cost else "fail"
        elif s == 0:
            outcome = "tie"
        elif s <= 2:
            outcome = "success"
        else:
            outcome = "success_with_style"
        needs_cost = outcome in ("tie", "success_major_cost")
        draw_reason = {"tie": "tie", "success_major_cost": "major_cost"}.get(outcome)
        drawn = None
        cost_mode = None
        if needs_cost:
            if not self.arm["deck"]:
                cost_mode = "improvised"
            elif self.scene_flags.get("is_climax"):
                cost_mode = "face_up_gm_tag"
            else:
                drawn = self.draw(draw_reason, actor="engine")
                if drawn is None:
                    self.fire("AMB-16", f"{draw_reason} with empty deck in scene {self.scene}")
                    cost_mode = "face_up_gm_tag"
                else:
                    cost_mode = "player_card_compel" if self.is_player_deck_card(drawn) else "gm_card"
        # Growth (§9): roll failed or major cost after the owner invoked one of their own cards.
        if outcome in ("fail", "success_major_cost"):
            for cid, _ in ctx.player_invokes:
                if self.arm["growth"] and cid in self.chars[pid].binder:
                    self.growth_ledger.append({"card": cid, "why": f"{outcome} after invoke", "scene": self.scene})
                    self.fire("AMB-10", cid)
        # Clocks (§7): a failed roll directly against a face-up GM card marks it.
        clock_notes = []
        if outcome == "fail":
            against = {c for c, _ in ctx.opposing_tags} | {c for c, _ in ctx.gm_invokes}
            if ctx.target_card and ctx.target_card in self.rail:
                against.add(ctx.target_card)
            if ctx.target_npc and ctx.target_npc in self.npcs and self.npcs[ctx.target_npc].card_id:
                against.add(self.npcs[ctx.target_npc].card_id)
            for cid in sorted(against):
                if cid in self.rail and self.cards[cid].track_kind == "clock" and self.cards[cid].owner in ("GM", "GLOBAL"):
                    clock_notes.append(self.mark_clock(cid, 1, why=f"failed roll by {name}"))
                    self.scene_flags["failed_against"].add(cid)
        effects = self._apply_action_effects(ctx, outcome, use_story_ally)
        tags_str = "; ".join(f"{t} [{c}]" for c, t in ctx.player_invokes)
        opp_str = f"{ctx.opp_total:+d}"
        if ctx.opp_kind == "active":
            opp_str += f" (NPC {fmt_dice(ctx.opp_dice or [])})"
        gm_note = ""
        if ctx.gm_invokes or ctx.hostile_invokes:
            gm_note = "GM invokes: " + "; ".join(f"{t} [{c}]" for c, t in ctx.gm_invokes + ctx.hostile_invokes)
        ev = self.log(event_type="roll", actor=name,
                      action=f"{ctx.action.replace('_', ' ').title()}: {ctx.description[:60]}",
                      skill=f"{ctx.skill} {ctx.skill_rating:+d}", tags_invoked=tags_str,
                      fp_spent=ctx.fp_spent, dice=fmt_dice(ctx.dice), total=f"{ctx.total:+d}",
                      opposition=opp_str, result=outcome, draw_id=drawn or "",
                      clock_change="; ".join(n for n in clock_notes if n),
                      notes="; ".join(x for x in [gm_note, effects.get("note", "")] if x),
                      opposing_tags=[f"{t} [{c}]" for c, t in ctx.opposing_tags],
                      target_card=ctx.target_card or "", target_npc=ctx.target_npc or "",
                      shifts=s, cost_mode=cost_mode or "")
        ctx.event_id = ev["event_id"]
        return {"outcome": outcome, "shifts": s, "drawn": drawn, "cost_mode": cost_mode,
                "event_id": ev["event_id"], "effects": effects, "clock_notes": clock_notes}

    def _apply_action_effects(self, ctx: RollCtx, outcome: str, use_story_ally: bool) -> dict:
        pid = ctx.actor
        out: dict[str, Any] = {}
        success = outcome in ("tie", "success", "success_with_style", "success_major_cost")
        if ctx.action == "create_advantage" and success:
            if outcome == "success_with_style" and use_story_ally and self.arm["story_piles"]:
                sc = self.story_draw(pid, trigger="sws_create_advantage", free_to=pid)
                out["note"] = f"story ally {sc}"
                out["story_card"] = sc
            else:
                n = 2 if outcome == "success_with_style" else 1
                aid = self.add_scene_aspect(ctx.advantage_name or ctx.description[:40] or "Advantage", pid, n)
                out["aspect"] = aid
                out["note"] = f"aspect {aid} ({n} free)"
        elif ctx.action == "attack":
            harm = 0
            if outcome in ("success", "success_with_style"):
                harm = ctx.shifts
            elif outcome == "success_major_cost":
                harm = 1
                self.fire("AMB-23")
            elif outcome == "tie":
                self.fire("AMB-19")
                aid = self.add_scene_aspect("Boost: " + (ctx.description[:30] or "opening"), pid, 1, boost=True)
                out["aspect"] = aid
            if harm and ctx.target_npc in self.npcs:
                out.update(self.harm_npc(ctx.target_npc, harm))
                out["note"] = out.get("note", "")
        elif ctx.action == "overcome" and outcome == "success_with_style":
            tc = ctx.target_card
            if tc and tc in self.rail and self.cards[tc].origin == "world" and self.cards[tc].owner == "GM":
                self.card_leaves_play(tc, "overcome with success with style")
                out["note"] = f"{tc} overcome with style"
        return out

    # ------------------------------------------------------------------ aspects, NPCs, harm
    def add_scene_aspect(self, name: str, holder: str, free: int, boost: bool = False) -> str:
        aid = f"A-{self.session}.{self.scene}.{next(self._aid)}"
        self.cards[aid] = Card(id=aid, type="BOOST" if boost else "SITUATION", owner="SCENE",
                               title=name, power_tags=[name], weakness="", origin="scene")
        self.scene_aspects.append(aid)
        if free:
            self.free_invokes[(holder, aid)] = free
        return aid

    def _remove_scene_aspect(self, aid: str) -> None:
        if aid in self.scene_aspects:
            self.scene_aspects.remove(aid)
        for k in [k for k in self.free_invokes if k[1] == aid]:
            del self.free_invokes[k]

    def add_npc(self, name: str, rating: int, stress: int = 2, hostile: bool = True,
                card_id: str | None = None) -> None:
        rating = max(0, min(int(rating), 5))
        stress = max(1, min(int(stress), 4))
        if card_id and card_id not in self.rail:
            card_id = None
        self.npcs[name] = NPC(name=name, rating=rating, stress=[[i + 1, False] for i in range(stress)],
                              hostile=hostile, card_id=card_id)

    def harm_npc(self, name: str, shifts: int) -> dict:
        npc = self.npcs[name]
        box = next((b for b in npc.stress if not b[1] and b[0] >= shifts), None)
        if box:
            box[1] = True
            return {"npc_harm": f"{name} stress {box[0]}"}
        if npc.mild_free and shifts <= 2 + max((b[0] for b in npc.stress if not b[1]), default=0):
            npc.mild_free = False
            rest = shifts - 2
            if rest > 0:
                b = next((b for b in npc.stress if not b[1] and b[0] >= rest), None)
                if b:
                    b[1] = True
            return {"npc_harm": f"{name} mild consequence"}
        npc.out = True
        res = {"npc_harm": f"{name} taken out"}
        if npc.card_id and npc.card_id in self.rail:
            self.card_leaves_play(npc.card_id, f"taken out in conflict ({name})")
        return res

    def card_leaves_play(self, cid: str, how: str) -> None:
        self.left_play.append({"card": cid, "how": how, "session": self.session, "scene": self.scene})
        self.remove_from_rail(cid, to="left_play", why=how)
        self.log(event_type="card_leaves_play", action=f"{cid} leaves play", draw_id=cid, notes=how)

    def mark_clock(self, cid: str, n: int, why: str) -> str:
        card = self.cards[cid]
        if card.track_kind != "clock" or card.track_size <= 0:
            return ""
        card.marks = min(card.track_size, card.marks + n)
        self.scene_flags["clock_advanced"] = True
        note = f"{cid} {card.marks}/{card.track_size}"
        if card.marks >= card.track_size:
            self.clock_filled.append({"card": cid, "session": self.session, "scene": self.scene})
            self.fire("AMB-24", cid)
            self.queue_beat(reason=f"clock filled: {cid}", clock_card=cid)
            if cid in self.rail:
                self.card_leaves_play(cid, "clock filled")
            note += " FILLED"
        self.log(event_type="clock", action=f"Clock {cid}", clock_change=note, notes=why)
        return note

    def absorb_options(self, pid: str, track: str, shifts: int) -> list[dict]:
        ch = self.chars[pid]
        boxes = [b for b in ch.stress[track] if not b[1]]
        free_cons = [k for k in ("mild", "moderate", "severe") if ch.consequences[k] is None]
        size = {"mild": 2, "moderate": 4, "severe": 6}
        opts = []
        for r in range(0, len(free_cons) + 1):
            for combo in itertools.combinations(free_cons, r):
                rest = shifts - sum(size[c] for c in combo)
                if rest <= 0:
                    if r and any(shifts - sum(size[c] for c in combo if c != x) <= 0 for x in combo):
                        continue   # a consequence in the combo is unnecessary
                    opts.append({"box": None, "consequences": list(combo)})
                    continue
                box = min((b[0] for b in boxes if b[0] >= rest), default=None)
                if box is not None:
                    opts.append({"box": box, "consequences": list(combo)})
        opts.sort(key=lambda o: (len(o["consequences"]), o["box"] or 0))
        return opts

    def apply_absorb(self, pid: str, track: str, shifts: int, option: dict,
                     consequence_texts: dict[str, str], strain: dict[str, dict]) -> dict:
        ch = self.chars[pid]
        if option["box"] is not None:
            for b in ch.stress[track]:
                if b[0] == option["box"] and not b[1]:
                    b[1] = True
                    break
        notes = []
        for level in option["consequences"]:
            text = consequence_texts.get(level) or f"{level.title()} wound"
            s = strain.get(level) or {}
            cid = s.get("card_id")
            valid_cards = [c for c in ch.binder if ch.card_state.get(c) in ("binder", "rail")]
            if cid not in valid_cards:
                if cid is not None:
                    self.violation(ch.name, "§11", f"strained a card not in their binder ({cid})")
                cid = valid_cards[0] if valid_cards else None
            tag = s.get("tag")
            if level == "mild" and cid and tag not in self.cards[cid].power_tags:
                tag = self.cards[cid].power_tags[0]
            ch.consequences[level] = {"aspect": text, "card_id": cid, "tag": tag,
                                      "session": self.session, "scene": self.scene}
            if cid and self.arm["cards"]:
                ch.strained[cid] = {"level": level, "tag": tag if level == "mild" else None}
                if level == "severe":
                    self.growth_ledger.append({"card": cid, "why": "severe consequence", "scene": self.scene})
            notes.append(f"{level}: {text}" + (f" (strains {cid})" if cid and self.arm["cards"] else ""))
        ev = self.log(event_type="harm", actor=ch.name, action=f"Absorb {shifts} {track}",
                      notes="; ".join(notes) + (f"; box {option['box']}" if option["box"] else ""))
        return {"event": ev}

    def taken_out(self, pid: str, by: str) -> str | None:
        ch = self.chars[pid]
        ch.out_of_scene = True
        ch.taken_out_scene = self.scene
        self.log(event_type="taken_out", actor=ch.name, action="Taken out", notes=f"by {by}")
        if self.arm["story_piles"]:
            return self.story_draw(None, trigger="taken_out", free_to="GM")
        return None

    def concede(self, pid: str, sacrifice: str | None = None) -> dict:
        ch = self.chars[pid]
        cons_this = sum(1 for v in ch.consequences.values()
                        if v and v["session"] == self.session and v["scene"] == self.scene)
        gain = 1 + cons_this
        sac = None
        if sacrifice and self.arm["cards"]:
            if sacrifice in ch.binder and ch.card_state.get(sacrifice) in ("binder", "rail"):
                sac = sacrifice
                ch.card_state[sacrifice] = "sacrificed"
                if sacrifice in self.rail:
                    self.rail.remove(sacrifice)
                self.retired.append({"card": sacrifice, "how": "sacrificed in concession",
                                     "session": self.session})
                gain += 1
            else:
                self.violation(ch.name, "§8", f"invalid sacrifice {sacrifice}")
        ch.fp += gain
        ch.out_of_scene = True
        ch.conceded_scene = self.scene
        self.log(event_type="concede", actor=ch.name, action="Concede", fp_spent=-gain,
                 notes=f"+{gain} FP" + (f"; sacrificed {sac}" if sac else ""))
        story = None
        if self.arm["story_piles"]:
            story = self.story_draw(pid, trigger="concede", free_to=pid)
        return {"gain": gain, "sacrificed": sac, "story": story}

    # ------------------------------------------------------------------ Story Piles (§6A)
    def story_pile(self, owner: str | None) -> list[str]:
        return self.gm_story_pile if owner is None else self.chars[owner].story_pile

    def story_draw(self, owner: str | None, *, trigger: str, free_to: str) -> str | None:
        pile = self.story_pile(owner)
        slips = []
        for cid in pile:
            if cid in self.rail:
                continue
            slips += [cid] * max(1, min(3, self.cards[cid].track_size))
        if not slips:
            self.scene_flags["story_drawn"].append({"card": None, "owner": owner, "trigger": trigger,
                                                    "empty": True, "free_to": free_to})
            self.log(event_type="story_draw", action=f"Story draw ({trigger})",
                     actor=self.name(owner) if owner else "GM", notes="pile empty: owner must write a card")
            return None
        cid = self.rng["story"].choice(sorted(slips))
        self.place_on_rail(cid, reason=f"story draw ({trigger})")
        self.free_invokes[(free_to, cid)] = self.free_invokes.get((free_to, cid), 0) + 1
        self.story_featured.add(cid)
        self.scene_flags["story_drawn"].append({"card": cid, "owner": owner, "trigger": trigger,
                                                "free_to": free_to})
        self.log(event_type="story_draw", action=f"Story draw ({trigger})",
                 actor=self.name(owner) if owner else "GM", draw_id=cid)
        return cid

    def add_story_card(self, owner: str | None, d: dict) -> str | None:
        """Pile maintenance 'Add' (or an empty-pile write). Enforces the size limit."""
        prefix = "SN" if owner is None else f"S{self.chars[owner].binder[0].split('-')[0]}"
        n = sum(1 for k in self.cards if k.startswith(prefix + "-")) + 1
        cid = f"{prefix}-{n:02d}"
        typ = d.get("type", "NPC").upper()
        if typ not in ("NPC", "THREAD"):
            typ = "NPC"
        tags = [str(t) for t in (d.get("power_tags") or [])][:3]
        while len(tags) < 3:
            tags.append("(unwritten tag)")
        self.cards[cid] = Card(id=cid, type=typ, owner="GM" if owner is None else self.chars[owner].code(),
                               title=str(d.get("title", "Untitled"))[:80], power_tags=tags,
                               weakness=str(d.get("weakness", "Complicated"))[:60], track_kind="weight",
                               track_size=1, origin="story")
        pile = self.story_pile(owner)
        pile.append(cid)
        limit = 12 if owner is None else 5
        while len(pile) > limit:
            victim = min(pile, key=lambda x: (self.cards[x].track_size, pile.index(x)))
            pile.remove(victim)
            self.retired.append({"card": victim, "how": "story pile over limit", "session": self.session})
        self.log(event_type="story_add", action="Story card added", draw_id=cid,
                 actor=self.name(owner) if owner else "GM", notes=self.cards[cid].title)
        return cid

    def retire_story_card(self, cid: str, how: str) -> bool:
        for pile in [self.gm_story_pile] + [c.story_pile for c in self.chars.values()]:
            if cid in pile:
                if cid not in self.appeared_this_session and cid not in self.story_featured:
                    self.violation("GM", "§10", f"retired story card {cid} that never appeared in play")
                    return False
                pile.remove(cid)
                if cid in self.rail:
                    self.rail.remove(cid)
                self.retired.append({"card": cid, "how": how, "session": self.session})
                self.log(event_type="story_retire", action="Story card retired", draw_id=cid, notes=how)
                return True
        return False

    # ------------------------------------------------------------------ Beat Frames (§5)
    def queue_beat(self, reason: str, frame_id: str | None = None, clock_card: str | None = None,
                   guarantee: bool = False) -> None:
        self.queued_beats.append({"reason": reason, "frame_id": frame_id, "clock_card": clock_card,
                                  "guarantee": guarantee})

    def pick_frame(self, preferred: str | None) -> dict:
        prepared = [b for b in self.prep["beat_frames"] if not b.get("used")]
        if preferred:
            for b in prepared:
                if b["id"] == preferred:
                    return b
        if prepared:
            return prepared[0]
        used_ids = {b["id"] for b in self.prep["beat_frames"]}
        lib = [b for b in self.world["beat_frames"] if b["id"] not in used_ids]
        self.fire("AMB-06", "no unused prepared frame")
        pick = copy.deepcopy(self.rng["misc"].choice(lib or self.world["beat_frames"]))
        pick["trigger"] = "interrupt (library fallback)"
        self.prep["beat_frames"].append(pick)
        return pick

    def fill_beat(self, frame: dict, pulled: list[str] | None = None) -> dict:
        """§5 steps 2-3: draw one card per open blank and assign each to a blank."""
        frame["used"] = True
        open_blanks = list(frame["open"])
        cards: list[str] = list(pulled or [])
        if self.arm["deck"]:
            while len(cards) < len(open_blanks):
                if not self.deck:
                    break
                cid = self.draw("beat_frame", actor="engine")
                if cid is None:
                    break
                cards.append(cid)
        fills: dict[str, str | None] = {b: None for b in open_blanks}
        for cid in cards:
            want = BLANK_FOR_TYPE.get(self.cards[cid].type)
            if want in fills and fills[want] is None:
                fills[want] = cid
            else:
                empty = next((b for b in open_blanks if fills[b] is None), None)
                if empty is None:
                    break
                fills[empty] = cid
        self.log(event_type="beat_frame", action=f"Beat Frame {frame['name']}",
                 draw_id=",".join(c for c in fills.values() if c),
                 notes=f"fills {fills}; defaults for rest")
        return {"frame": frame, "fills": fills, "cards": [c for c in fills.values() if c]}

    # ------------------------------------------------------------------ triggers & cleanup
    def check_triggers(self, fiction_fired: list[str]) -> list[str]:
        fired = []
        items = [("module", m) for m in self.prep["modules"] if not m.get("used")]
        items += [("beat", b) for b in self.prep["beat_frames"] if not b.get("used") and not b.get("queued")]
        for kind, it in items:
            trig = it.get("trigger", "")
            key, _, arg = trig.partition(":")
            hit = False
            if key == "clock_fills":
                hit = any(c["card"] == arg for c in self.clock_filled)
            elif key == "roll_fails_against":
                hit = arg in self.scene_flags["failed_against"]
            elif key == "scene_start":
                hit = self.scene + 1 == int(arg)
            elif key == "tension_at_least":
                hit = self.arm["tension"] and self.tension >= int(arg)
            elif key == "compel_refused":
                hit = self.scene_flags["compel_refused"]
            elif key == "deck_at_most":
                hit = self.arm["deck"] and len(self.deck) <= int(arg)
            elif key == "fiction":
                hit = it["id"] in fiction_fired
            if hit:
                fired.append(it["id"])
                if kind == "module":
                    it["used"] = True
                    self.queued_modules.append(it)
                else:
                    it["queued"] = True
                    self.queue_beat(reason=f"trigger {trig}", frame_id=it["id"])
                self.log(event_type="trigger", action=f"Trigger fired: {it['id']}", notes=trig)
        for fid in fiction_fired:
            if fid not in fired:
                self.violation("GM", "§7", f"reported fictional trigger {fid} that is not an unused fictional trigger")
        return fired

    def end_scene(self, report: dict) -> dict:
        """§7 cleanup, in the spec's order. ``report`` comes from the GM agent (validated here)."""
        delta = 0
        parts = []
        if self.arm["tension"]:
            fled = [c for c in report.get("fled_or_bypassed", []) if c in self.appeared_this_session
                    and self.cards.get(c) and self.cards[c].type in ("THREAT", "FACTION")]
            resolved = [c for c in report.get("resolved_threats", []) if self.cards.get(c)
                        and self.cards[c].type == "THREAT"]
            if fled:
                delta += 1
                parts.append("fled/bypassed +1")
            if self.scene_flags["clock_advanced"]:
                delta += 1
                parts.append("clock +1")
            if resolved or report.get("goal_filled"):
                delta -= 1
                parts.append("resolved -1")
            if len(parts) > 1:
                self.fire("AMB-04", ", ".join(parts))
            before = self.tension
            self.tension = max(1, min(6, self.tension + delta))
            for c in resolved:
                if c in self.rail:
                    self.card_leaves_play(c, "resolved")
            self.log(event_type="tension", action="Adjust tension", result=f"{before}->{self.tension}",
                     notes=", ".join(parts) or "no change")
        # Stakes clock for the scene's beat, if the GM says it went badly.
        beat = self.scene_flags.get("beat")
        if beat and beat.get("stakes_clock") and report.get("beat_went_badly"):
            self.fire("AMB-14", beat["id"])
            sc = beat["stakes_clock"]
            if self.cards.get(sc) and self.cards[sc].track_kind == "clock":
                self.mark_clock(sc, 1, why=f"beat {beat['id']} stakes")
        # 2. Surfaced player cards return to binders.
        for cid in list(self.rail):
            card = self.cards[cid]
            if card.origin == "player" or (card.origin == "placebo" and card.type in PLAYER_TYPES):
                self.remove_from_rail(cid, to="binder", why="scene cleanup")
        # 3. GM cards no longer present -> discard (anchors and kept cards stay).
        keep = set(report.get("keep_on_rail", [])) | set(self.prep["anchors"])
        for cid in list(self.rail):
            card = self.cards[cid]
            if card.owner == "GLOBAL":
                continue
            if card.origin == "world" and cid not in keep:
                self.remove_from_rail(cid, to="discard", why="no longer present")
        # 4. Story piles: story cards on the rail return; weights; add/retire.
        for cid in list(self.rail):
            if self.cards[cid].type in ("NPC", "THREAD"):
                self.rail.remove(cid)
        if self.arm["story_piles"]:
            for d in self.scene_flags["story_drawn"]:
                if d["card"]:
                    c = self.cards[d["card"]]
                    c.track_size = min(3, c.track_size + 1)
            for sc in report.get("new_story_cards", [])[:3]:
                owner = self.pid_by_name(sc.get("pile", "")) if sc.get("pile", "GM") != "GM" else None
                if self.arm["placebo"] and owner is not None:
                    owner = None   # Arm C: no backstory-linked player piles; world story goes to GM
                self.add_story_card(owner, sc)
            for cid in report.get("retire_story_cards", []):
                self.retire_story_card(cid, "retired at scene cleanup")
        # 5. Triggers.
        fired = self.check_triggers(report.get("fiction_triggers_fired", []))
        # Hostile invoke payouts (§3), mild consequence recovery (§8), free invokes expire (§4).
        for pid in self.hostile_payouts:
            self.chars[pid].fp += 1
        if self.hostile_payouts:
            self.log(event_type="fp", action="Hostile invoke payouts",
                     notes=", ".join(self.name(p) for p in self.hostile_payouts))
        self.hostile_payouts = []
        for ch in self.chars.values():
            m = ch.consequences["mild"]
            if m and (m["session"], m["scene"]) < (self.session, self.scene):
                ch.consequences["mild"] = None
                if m["card_id"] in ch.strained and ch.strained[m["card_id"]]["level"] == "mild":
                    del ch.strained[m["card_id"]]
            for t in ch.stress.values():
                for b in t:
                    b[1] = False
        self.free_invokes = {}
        self.scene_aspects = []
        is_last = (self.scene_flags.get("is_climax") or self.scene_in_session >= self.max_scenes)
        if self.scene_flags.get("is_climax") or self.scene_in_session >= self.max_scenes:
            self.session_over = True
        if self.session_over and self.guarantee_pulled:
            for cid in self.guarantee_pulled:
                if cid not in self.surfaced:
                    self.guarantee_failed.append(cid)
                    self.fire("AMB-25", cid)
        self.log(event_type="scene_end", action=f"Scene {self.scene} end",
                 notes=f"triggers fired: {fired}" if fired else "")
        return {"tension_delta": delta, "triggers_fired": fired, "session_over": is_last}

    def next_beat_for_scene(self) -> dict | None:
        """Pops the beat (if any) that must open the next scene. Guarantee frames go first."""
        if self.guarantee_pulled and not any(b.get("guarantee") for b in self.queued_beats):
            pending = [c for c in self.guarantee_pulled if c not in self.surfaced]
            if pending:
                self.queued_beats.insert(0, {"reason": "backstory guarantee", "frame_id": None,
                                             "clock_card": None, "guarantee": True, "cards": pending})
        if not self.queued_beats:
            return None
        self.queued_beats.sort(key=lambda b: not b.get("guarantee"))
        b = self.queued_beats.pop(0)
        if self.queued_beats:
            self.fire("AMB-26", f"{len(self.queued_beats)} beat(s) carried over")
        return b

    # ------------------------------------------------------------------ post-session (§9, §10)
    def post_session(self, gm_report: dict) -> dict:
        out: dict[str, Any] = {"growth": {}, "clocks": [], "mutations": [], "retired": []}
        if self.arm["cards"] and self.arm.get("growth", True):
            per_card: dict[str, int] = {}
            for g in self.growth_ledger:
                per_card[g["card"]] = per_card.get(g["card"], 0) + 1
            for cid, n in per_card.items():
                add = min(2, n)
                self.cards[cid].growth += add
                out["growth"][cid] = {"added": add, "total": self.cards[cid].growth,
                                      "evolve": self.cards[cid].growth >= 3}
        if self.arm["clocks"]:
            for cid in sorted(self.appeared_this_session):
                c = self.cards[cid]
                if c.type in ("THREAT", "FACTION") and c.origin == "world" \
                        and cid not in self.rolled_against_this_session \
                        and not any(l["card"] == cid for l in self.left_play):
                    out["clocks"].append(self.mark_clock(cid, 1, why="bypassed (post-session)"))
            for c in self.world["cards"]:
                cid = c["id"]
                if c["type"] == "FACTION" and cid not in self.appeared_this_session:
                    r = self.rng["offscreen"].randint(1, 6)
                    if r >= 5:
                        out["clocks"].append(self.mark_clock(cid, 1, why=f"off-screen d6={r}"))
                    else:
                        self.log(event_type="clock", action=f"Off-screen {cid}", dice=str(r), notes="no change")
            decisions = {d.get("card_id"): d for d in gm_report.get("threats_left_play", [])}
            for lp in self.left_play:
                if lp["session"] != self.session:
                    continue
                cid = lp["card"]
                d = decisions.get(cid, {"alive": lp["how"] != "resolved"})
                if d.get("alive"):
                    card = self.cards[cid]
                    base, _, ver = cid.partition("v")
                    newid = f"{base}v{int(ver or 1) + 1}"
                    new = copy.deepcopy(card)
                    new.id = newid
                    if new.power_tags:
                        new.power_tags[0] = str(d.get("new_tag") or f"scarred by the party")[:60]
                    new.marks = min(new.track_size, new.marks + 1)
                    self.cards[newid] = new
                    out["mutations"].append({"from": cid, "to": newid})
                    self.log(event_type="mutation", action=f"{cid} -> {newid}", notes=new.power_tags[0])
                else:
                    self.retired.append({"card": cid, "how": lp["how"], "session": self.session})
                    out["retired"].append(cid)
        entry = {"session": self.session, "summary": gm_report.get("summary", ""),
                 "closing_tension": self.tension if self.arm["tension"] else None,
                 "reverberations": out, "retired": [r for r in self.retired if r["session"] == self.session]}
        self.chronicle.append(entry)
        self.log(event_type="session_end", action="Session end",
                 notes=f"FP: " + ", ".join(f"{c.name}={c.fp}" for c in self.chars.values()))
        return entry

    # ------------------------------------------------------------------ snapshots for agents
    def public_state(self) -> dict:
        """What everyone at the table can see (no deck contents, no GM notes)."""
        return {
            "scene": self.scene,
            "tension": self.tension if self.arm["tension"] else None,
            "rail": [self.cards[c].brief() for c in self.rail],
            "scene_aspects": [{"id": a, "name": self.cards[a].title} for a in self.scene_aspects],
            "npcs": [{"name": n.name, "hostile": n.hostile, "out": n.out,
                      "stress_marked": sum(1 for b in n.stress if b[1])} for n in self.npcs.values()],
            "deck_remaining": len(self.deck) if self.arm["deck"] else None,
            "players": [{"name": c.name, "fate_points": c.fp, "out_of_scene": c.out_of_scene,
                         "consequences": {k: v["aspect"] for k, v in c.consequences.items() if v}}
                        for c in self.chars.values()],
        }

    def player_sheet(self, pid: str) -> dict:
        ch = self.chars[pid]
        cards = []
        for cid in ch.binder:
            card = self.cards[cid]
            st = ch.card_state.get(cid)
            status = {"binder": "available", "rail": "in play (face-up)", "deck": "set aside",
                      "setaside": "set aside", "sacrificed": "gone"}.get(st, st)
            if cid in ch.strained:
                status += f" — strained ({ch.strained[cid]['level']})"
            cards.append({**card.brief(), "status": status,
                          "free_invokes": self.free_invokes.get((pid, cid), 0)})
        return {"name": ch.name, "pronouns": ch.pronouns, "concept": ch.concept,
                "skills": dict(sorted(ch.skills.items(), key=lambda kv: -kv[1])),
                "fate_points": ch.fp,
                "cards" if self.arm["cards"] else "aspects": cards,
                "stress": {k: [f"{b[0]}{'x' if b[1] else ''}" for b in v] for k, v in ch.stress.items()},
                "consequences": {k: v["aspect"] for k, v in ch.consequences.items() if v},
                "free_invokes": [{"source_id": k[1], "n": v} for k, v in self.free_invokes.items()
                                 if k[0] == pid]}

    def gm_state(self) -> dict:
        s = self.public_state()
        s.update({
            "gm_fate_points": self.gm_fp,
            "gm_free_invokes": [{"card_id": k[1], "n": v} for k, v in self.free_invokes.items() if k[0] == "GM"],
            "deck_remaining": len(self.deck) if self.arm["deck"] else None,
            "climax": bool(self.scene_flags.get("is_climax")),
            "clocks": {c: f"{self.cards[c].marks}/{self.cards[c].track_size}" for c in self.rail
                       if self.cards[c].track_kind == "clock"},
            "unused_triggers": [{"id": x["id"], "trigger": x.get("trigger")} for x in
                                self.prep["modules"] + self.prep["beat_frames"] if not x.get("used")],
            "player_cards": {self.chars[p].name: [self.cards[c].brief() for c in self.chars[p].binder
                                                  if self.chars[p].card_state.get(c) != "sacrificed"]
                             for p in self.order},
        })
        return s
