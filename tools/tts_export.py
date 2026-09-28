"""Build the Hex-Nexus Tabletop Simulator mod from the repository.

    python tools/tts_export.py --rules 1.9.0 --roster 1.9.0 \
        --config reports/requests/batch_0075.json

Reads the rulebook version, the map (rules/map_v1.json), the roster, the
engine's DEFAULT_CONFIG overlaid with the request's ``config_overrides``, and
the shop catalogue, and writes into ``tts/build/``:

* ``data.lua``                       every number the mod uses, as Lua tables
* ``assets/*.png``                   board tiles, cards, tokens, dashboards
* ``HexNexus_<rules>_<roster>.json`` the TTS save, scripts inlined

Nothing here is a game number. If a value exists in the repo it is read from
the repo; this file only decides where things sit on the table.
"""
from __future__ import annotations

import argparse
import copy
import datetime as _dt
import hashlib
import json
import math
import os
import subprocess
import sys
from typing import Dict, List, Optional, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))

from engine.config import make_config                      # noqa: E402
from engine.items import BUFF_CARDS, CARD_ITEMS, MAX_CARD_COPIES, STAT_ITEMS  # noqa: E402
from engine.kits import load_roster                         # noqa: E402
from engine.resolve import DEATH_BANDS                      # noqa: E402

import tts_art as art                                       # noqa: E402

TTS_DIR = os.path.join(ROOT, "tts")
LUA_DIR = os.path.join(TTS_DIR, "lua")
TEAMS = ("north", "south")
TEAM_SEAT = {"north": "Blue", "south": "Red"}              # Rules 2.4: blue North, red South
ROLES = ("Top", "Jungle", "Mid", "ADC", "Support")
DEFAULT_REPO_RAW = "https://raw.githubusercontent.com/Noitues/Games"

# ---------------------------------------------------------------- table scale
HEX = 1.15                  # world units, hex centre to corner
R_PX = 64                   # pixels, hex centre to corner, in every board image
PPU = R_PX / HEX            # pixels per world unit, shared by all flat art
ART_ROT_Y = 180.0           # rotY at which an image reads upright from the -Z (South) side
Y_MAT, Y_TILE, Y_PIECE = 1.05, 1.20, 1.60
SOURCE_PATHS = ["rules", "roster", "engine", "reports/requests", "tools/tts_export.py",
                "tools/tts_art.py", "tts/lua"]


# ======================================================================= util
def git(*args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True,
                                       stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def guid(tag: str) -> str:
    return hashlib.md5(tag.encode()).hexdigest()[:6]


def lua_value(v, indent: int = 0) -> str:
    """Serialise JSON-like Python data as a Lua table constructor."""
    pad, pad2 = "  " * indent, "  " * (indent + 1)
    if v is None:
        return "nil"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        if isinstance(v, float) and v.is_integer():
            return str(int(v))
        return repr(v)
    if isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    if isinstance(v, (list, tuple)):
        if not v:
            return "{}"
        if all(not isinstance(x, (dict, list, tuple)) for x in v):
            return "{" + ", ".join(lua_value(x) for x in v) + "}"
        return "{\n" + ",\n".join(pad2 + lua_value(x, indent + 1) for x in v) + "\n" + pad + "}"
    if isinstance(v, dict):
        if not v:
            return "{}"
        items = []
        for k, x in v.items():
            if x is None:
                continue
            key = k if isinstance(k, str) and k.isidentifier() else "[" + lua_value(k) + "]"
            items.append(f"{pad2}{key} = {lua_value(x, indent + 1)}")
        return "{\n" + ",\n".join(items) + "\n" + pad + "}"
    raise TypeError(type(v))


def hex_world(q: int, r: int) -> Tuple[float, float]:
    """World (x, z) of a hex centre. North (negative r) is +Z."""
    x, y = art.hex_px(q, r, HEX)
    return round(x, 4), round(-y, 4)


def px_to_world(cx: float, cz: float, px: float, py: float, facing: str) -> Tuple[float, float]:
    """A point ``(px, py)`` pixels from the centre of an image lying at world
    ``(cx, cz)``. ``facing`` is the seat the image reads upright for."""
    if facing == "south":
        return round(cx + px / PPU, 4), round(cz - py / PPU, 4)
    return round(cx - px / PPU, 4), round(cz + py / PPU, 4)


def rot_for(facing: str) -> float:
    return ART_ROT_Y if facing == "south" else (ART_ROT_Y + 180.0) % 360


# ================================================================ load sources
def load_sources(args) -> dict:
    rules_path = os.path.join(ROOT, "rules", f"Hex-Nexus_Rules_v{args.rules}.md")
    roster_path = os.path.join(ROOT, "roster", f"roster_v{args.roster}.json")
    for p in (rules_path, roster_path, args.config):
        if not os.path.exists(p):
            sys.exit(f"missing source: {p}")
    with open(os.path.join(ROOT, "rules", "map_v1.json")) as fh:
        map_data = json.load(fh)
    with open(roster_path) as fh:
        roster_meta = json.load(fh)
    kits = load_roster(roster_path)
    with open(args.config) as fh:
        request = json.load(fh)
    overrides = request.get("config_overrides", {})
    config = make_config(**overrides)
    commit = git("rev-parse", "--short", "HEAD") or "nogit"
    dirty = bool(git("status", "--porcelain", "--", *SOURCE_PATHS))
    config_id = request.get("batch_id") or os.path.splitext(os.path.basename(args.config))[0]
    versions = {
        "rules": args.rules, "roster": roster_meta.get("version", args.roster),
        "config": config_id, "config_path": os.path.relpath(args.config, ROOT),
        "commit": commit + ("-dirty" if dirty else ""),
        "built": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }
    positions = config.get("death_track_positions")
    versions["death"] = "/".join(str(p - 1) for p in positions) if positions else "bands"
    versions["stamp"] = (f"Rules {versions['rules']} \u00b7 Roster {versions['roster']} \u00b7 "
                         f"Config {config_id} \u00b7 death {versions['death']} rounds \u00b7 "
                         f"{versions['commit']}")
    return {"map": map_data, "kits": kits, "roster_meta": roster_meta, "config": config,
            "request": request, "versions": versions}


# ============================================================ derived numbers
def wave_size(cfg: dict, rnd: int) -> int:
    """engine.game.wave_size, for a round number rather than a state."""
    if rnd >= cfg.get("wave_growth_round2", 10 ** 6):
        return cfg["wave_chips_late2"]
    if rnd >= cfg["wave_growth_round"]:
        return cfg["wave_chips_late"]
    return cfg["wave_chips"]


def death_position(cfg: dict, rnd: int) -> int:
    """engine.resolve.kill_champion's track position for a death in ``rnd``."""
    positions = cfg.get("death_track_positions")
    band = 0 if rnd <= DEATH_BANDS[0][0] else 1 if rnd <= DEATH_BANDS[1][0] else 2
    if positions:
        return positions[band]
    return DEATH_BANDS[band][1] + cfg.get("death_band_bonus", 0)


def kill_reward(cfg: dict, rnd: int) -> int:
    mult = cfg.get("kill_ap_waves", 0)
    if mult:
        return int(mult * wave_size(cfg, rnd) + 0.5)
    return cfg.get("kill_ap", 1)


def decays(cfg: dict, rnd: int) -> bool:
    """engine.game.decay_structures' schedule."""
    step = cfg.get("structure_decay", 0)
    every = max(1, cfg.get("structure_decay_every", 1))
    return bool(step) and rnd >= 2 and (rnd - 1) % every == 0


def floors(cfg: dict) -> Dict[str, int]:
    base = cfg.get("structure_decay_floor", 1)
    t, n = cfg.get("tower_decay_floor"), cfg.get("nexus_decay_floor")
    return {"tower": base if t is None else t, "nexus": base if n is None else n}


def round_rows(cfg: dict) -> List[dict]:
    rows = []
    spawns = {m: v["spawn"] for m, v in cfg["monsters"].items()}
    for rnd in range(1, cfg["round_limit"] + 1):
        spawn_wave = rnd % 2 == 1 or not cfg["wave_spawn_odd_rounds_only"]
        mons = [m.replace("_", " ").title() for m, s in spawns.items() if s == rnd]
        if rnd == 1:
            mons = ["camps"] + [m for m in mons if m not in
                                ("Wolves", "Raptors", "Krugs", "Blue Buff", "Red Buff")]
        rows.append({
            "round": rnd,
            "prio": "1st" if rnd % 2 == 1 else "2nd",
            "waves": f"+{wave_size(cfg, rnd)}" if spawn_wave else "\u2014",
            "wave_size": wave_size(cfg, rnd), "spawn": spawn_wave,
            "decay": f"-{cfg['structure_decay']}" if decays(cfg, rnd) else "",
            "decays": decays(cfg, rnd),
            "kill": str(kill_reward(cfg, rnd)), "kill_ap": kill_reward(cfg, rnd),
            "death_pos": death_position(cfg, rnd),
            "death": f"{death_position(cfg, rnd) - 1} rnd",
            "monsters": ", ".join(mons),
        })
    return rows


# ================================================================ data.lua
def build_data(src: dict) -> dict:
    cfg, m = src["config"], src["map"]
    kits = {}
    for cid, k in src["kits"].items():
        kits[cid] = {
            "id": cid, "name": k["name"], "role": k["role"], "hp": k["stats"]["hp"],
            "speed": k["stats"]["speed"], "identity": k.get("identity", ""),
            "abilities": {key: {"cost": a["cost"], "cooldown": a["cooldown"],
                                "steps": a["steps"]}
                          for key, a in k["abilities"].items()},
        }
    items = {"stat": {k: dict(v) for k, v in STAT_ITEMS.items()},
             "card": {k: dict(v) for k, v in CARD_ITEMS.items()},
             "buff": {k: dict(v) for k, v in BUFF_CARDS.items()},
             "max_card_copies": MAX_CARD_COPIES}
    cfg_out = copy.deepcopy(cfg)
    cfg_out.pop("enum", None)
    return {
        "VERSION": src["versions"],
        "CONFIG": cfg_out,
        "MAP": {"hexgroups": m["hexgroups"], "north": m["north"], "south": m["south"],
                "monsters": m["monsters"], "terrain": m["terrain"]},
        "ROSTER": kits,
        "ROLES": list(ROLES),
        "ITEMS": items,
        "ROUNDS": round_rows(cfg),
        "FLOORS": floors(cfg),
        "SNAKE": [1, 2, 2, 1, 1, 2, 2, 1, 1, 2],
        "PHASES": ["Upkeep", "Action", "World", "Shop", "Win Check"],
        "SEATS": TEAM_SEAT,
        "HEX": HEX,
    }


# ================================================================ TTS objects
def transform(x, y, z, rot_y=0.0, scale=1.0, scale_y=None):
    return {"posX": x, "posY": y, "posZ": z, "rotX": 0.0, "rotY": rot_y, "rotZ": 0.0,
            "scaleX": scale, "scaleY": scale if scale_y is None else scale_y, "scaleZ": scale}


def base_obj(name: str, tag: str, nick: str, x, y, z, rot_y=0.0, scale=1.0, *,
             locked=False, desc="", script="", state="", colour=(1, 1, 1)) -> dict:
    return {
        "GUID": guid(tag), "Name": name, "Transform": transform(x, y, z, rot_y, scale),
        "Nickname": nick, "Description": desc, "GMNotes": tag,
        "ColorDiffuse": {"r": colour[0], "g": colour[1], "b": colour[2]},
        "Locked": locked, "Grid": False, "Snap": True, "IgnoreFoW": False,
        "Autoraise": True, "Sticky": True, "Tooltip": True, "GridProjection": False,
        "HideWhenFaceDown": False, "Hands": False,
        "LuaScript": script, "LuaScriptState": state, "XmlUI": "",
    }


def custom_token(tag, nick, url, x, y, z, rot_y=0.0, scale=1.0, *, thickness=0.1,
                 stackable=False, locked=False, desc="", script="", state="") -> dict:
    o = base_obj("Custom_Token", tag, nick, x, y, z, rot_y, scale, locked=locked, desc=desc,
                 script=script, state=state)
    o["CustomImage"] = {"ImageURL": url, "ImageSecondaryURL": "", "ImageScalar": 1.0,
                        "WidthScale": 0.0,
                        "CustomToken": {"Thickness": thickness, "MergeDistancePixels": 15.0,
                                        "StandUp": False, "Stackable": stackable}}
    return o


def custom_tile(tag, nick, url, x, y, z, rot_y=0.0, scale=1.0, *, thickness=0.1, locked=True,
                desc="", back_url="") -> dict:
    o = base_obj("Custom_Tile", tag, nick, x, y, z, rot_y, scale, locked=locked, desc=desc)
    o["CustomImage"] = {"ImageURL": url, "ImageSecondaryURL": back_url or url, "ImageScalar": 1.0,
                        "WidthScale": 0.0,
                        "CustomTile": {"Type": 0, "Thickness": thickness, "Stackable": False,
                                       "Stretch": True}}
    return o


def custom_deck(deck_key: int, face_url: str, back_url: str, cols: int, rows: int) -> dict:
    return {str(deck_key): {"FaceURL": face_url, "BackURL": back_url, "NumWidth": cols,
                            "NumHeight": rows, "BackIsHidden": True, "UniqueBack": False,
                            "Type": 0}}


def card(tag, nick, deck_key, index, cdeck, desc="", x=0.0, y=Y_PIECE, z=0.0, rot_y=0.0,
         scale=1.0) -> dict:
    o = base_obj("Card", tag, nick, x, y, z, rot_y, scale, desc=desc)
    o["CardID"] = deck_key * 100 + index
    o["CustomDeck"] = cdeck
    o["SidewaysCard"] = False
    return o


def deck(tag, nick, cards: List[dict], cdeck: dict, x, y, z, rot_y=0.0, scale=1.0,
         face_up=True) -> dict:
    o = base_obj("Deck", tag, nick, x, y, z, rot_y, scale)
    o["Transform"]["rotZ"] = 0.0 if face_up else 180.0
    o["DeckIDs"] = [c["CardID"] for c in cards]
    o["CustomDeck"] = {}
    for c in cards:
        o["CustomDeck"].update(c["CustomDeck"])
    o["ContainedObjects"] = cards
    o["SidewaysCard"] = False
    return o


def bag(tag, nick, contents: List[dict], x, y, z, colour=(0.8, 0.8, 0.8), infinite=False) -> dict:
    o = base_obj("Infinite_Bag" if infinite else "Bag", tag, nick, x, y, z, colour=colour)
    o["ContainedObjects"] = contents
    return o


def zone(tag, nick, x, y, z, sx, sy, sz) -> dict:
    o = base_obj("ScriptingTrigger", tag, nick, x, y, z, locked=True)
    o["Transform"].update({"scaleX": sx, "scaleY": sy, "scaleZ": sz})
    o["ColorDiffuse"] = {"r": 1, "g": 1, "b": 1, "a": 0.2}
    return o


def text_obj(tag, text, x, y, z, rot_y, size=48, colour=(1, 1, 1)) -> dict:
    o = base_obj("3DText", tag, "", x, y, z, locked=True)
    o["Transform"].update({"rotX": 90.0, "rotY": rot_y})
    o["Text"] = {"Text": text, "colorstate": {"r": colour[0], "g": colour[1], "b": colour[2]},
                 "fontSize": size}
    return o


# ================================================================== builder
class Builder:
    def __init__(self, src: dict, out_dir: str, asset_base: str):
        self.src, self.out, self.asset_base = src, out_dir, asset_base.rstrip("/")
        self.assets = os.path.join(out_dir, "assets")
        self.objects: List[dict] = []
        self.layout: Dict[str, dict] = {}       # tag -> where/how big (data.lua LAYOUT)
        self.snaps: List[dict] = []
        self.cfg = src["config"]
        self.v = src["versions"]
        self.fonts_ok = os.path.isdir(art.FONT_DIR)

    # --------------------------------------------------------------- helpers
    def url(self, name: str) -> str:
        return f"{self.asset_base}/{name}"

    def img(self, image, name: str) -> str:
        art.save(image, os.path.join(self.assets, name))
        return self.url(name)

    def place(self, tag: str, x: float, z: float, y: float, rot: float, *, w: float = 0.0,
              d: float = 0.0, lock: bool = False, art_obj: bool = False, start: bool = True):
        """Record where an object belongs and how wide it should be, for the
        Global script's calibration (it fits scale from measured bounds)."""
        self.layout[tag] = {"x": x, "z": z, "y": y, "rot": rot, "w": round(w, 4),
                            "d": round(d, 4), "lock": lock, "art": art_obj, "start": start}

    def load_lua(self, name: str) -> str:
        with open(os.path.join(LUA_DIR, name)) as fh:
            return fh.read()

    # ------------------------------------------------------------------ board
    def build_board(self):
        m = self.src["map"]
        base_tiles = {}
        for team, tile in (("north", "North Base"), ("south", "South Base")):
            for q, r in m["hexgroups"][tile]:
                base_tiles[(q, r)] = team
        terrain = {}
        for t, hexes in m["terrain"].items():
            for q, r in hexes:
                terrain[(q, r)] = t
        markers, lane_dot = {}, set()
        for team in TEAMS:
            side = m[team]
            markers[tuple(side["fountain"])] = "FOUNT"
            for lane, path in side["lane_paths"].items():
                markers.setdefault(tuple(path[0]), "SPAWN")
                for h in path:
                    lane_dot.add(tuple(h))
        for mtype, hexes in m["monsters"].items():
            for h in hexes:
                markers[tuple(h)] = {"blue_buff": "BLUE", "red_buff": "RED"}.get(
                    mtype, mtype.upper()[:6])
        ctx = {"terrain": terrain, "base_tiles": base_tiles, "markers": markers,
               "lane_dot": lane_dot}

        bw, bh = art.board_extent(R_PX)
        margin = int(R_PX * 1.6)
        mat_px = (int(bw) + 2 * margin, int(bh) + 2 * margin)
        url = self.img(art.render_mat(R_PX, m, self.v, mat_px), "mat.png")
        mw, md = mat_px[0] / PPU, mat_px[1] / PPU
        tag = "hn:art:mat"
        self.objects.append(custom_tile(tag, "Hex-Nexus board", url, 0.0, Y_MAT, 0.0,
                                        ART_ROT_Y, 1.0, thickness=0.2,
                                        desc=self.v["stamp"]))
        self.place(tag, 0.0, 0.0, Y_MAT, ART_ROT_Y, w=mw, d=md, lock=True, art_obj=True)
        self.mat_size = (mw, md)

        for name, hexes in sorted(m["hexgroups"].items()):
            hexes = [tuple(h) for h in hexes]
            x0, y0, x1, y1 = art.tile_bbox(hexes, R_PX)
            cx, cz = (x0 + x1) / 2 / PPU, -(y0 + y1) / 2 / PPU
            w, d = (x1 - x0) / PPU, (y1 - y0) / PPU
            slug = name.lower().replace(" ", "_")
            urls = {side: self.img(art.render_tile(name, hexes, side, R_PX, ctx, margin=2),
                                   f"tile_{slug}_{side}.png") for side in ("hidden", "visible")}
            desc = f"Hexgroup: {name} \u00b7 {len(hexes)} hexes. Right-click \u2192 Flip hexgroup."
            states = {}
            for sid, side in ((1, "hidden"), (2, "visible")):
                tag = f"hn:tile:{name}"
                o = custom_token(f"{tag}:{side}", f"{name} ({side})", urls[side], cx, Y_TILE, cz,
                                 ART_ROT_Y, 1.0, thickness=0.08, locked=True, desc=desc,
                                 script=self.load_lua("tile.lua"))
                o["GUID"] = guid(f"{tag}:{side}")
                states[sid] = o
                self.place(f"{tag}:{side}", round(cx, 4), round(cz, 4), Y_TILE, ART_ROT_Y,
                           w=w, d=d, lock=True, art_obj=True)
            root = states[1]
            root["States"] = {"2": states[2]}
            self.objects.append(root)

    # ------------------------------------------------------------ structures
    def counter_state(self, **kw) -> str:
        return json.dumps(kw)

    def build_structures(self):
        m, cfg = self.src["map"], self.cfg
        fl = floors(cfg)
        counter = self.load_lua("counter.lua")
        size = HEX * 1.55
        for team in TEAMS:
            side = m[team]
            facing = team if team == "south" else "north"
            rot = rot_for(facing)
            items = [("nexus", "NEXUS", side["nexus"], cfg["nexus_hp"], fl["nexus"])]
            for name, h in side["towers"].items():
                lane, tier = name.split("_")
                items.append((name, f"{lane.upper()} {tier}", h, cfg["tower_hp"], fl["tower"]))
            for key, label, h, hp, floor in items:
                url = self.img(art.render_structure(team, label, hp, floor),
                               f"struct_{team}_{key}.png")
                x, z = hex_world(*h)
                tag = f"hn:struct:{team}:{key}"
                st = self.counter_state(kind="structure", label=label, hp=hp, max=hp, floor=floor,
                                        team=team)
                self.objects.append(custom_token(
                    tag, f"{team.title()} {label}", url, x, Y_PIECE, z, rot, 1.0, thickness=0.3,
                    desc=f"Starts {hp} HP; decays to floor {floor}. Left-click -1, right-click +1.",
                    script=counter, state=st))
                self.place(tag, x, z, Y_PIECE, rot, w=size, d=size)

    def build_monsters(self):
        m, cfg = self.src["map"], self.cfg
        counter = self.load_lua("counter.lua")
        size = HEX * 1.45
        for mtype, hexes in m["monsters"].items():
            mc = cfg["monsters"][mtype]
            label = mtype.replace("_", " ").title()
            note = f"spawns R{mc['spawn']} \u00b7 back +{mc['respawn']}"
            url = self.img(art.render_monster(label, mc["hp"], note), f"monster_{mtype}.png")
            for i, h in enumerate(hexes):
                x, z = hex_world(*h)
                tag = f"hn:monster:{mtype}:{i}"
                start = mc["hp"] if mc["spawn"] <= 1 else 0
                st = self.counter_state(kind="monster", label=label, hp=start, max=mc["hp"],
                                        floor=0, spawn=mc["spawn"], respawn=mc["respawn"])
                self.objects.append(custom_token(
                    tag, label, url, x, Y_PIECE, z, ART_ROT_Y, 1.0, thickness=0.25,
                    desc=f"{mc['hp']} HP (chips = AP). Spawns round {mc['spawn']}, respawns "
                         f"{mc['respawn']} rounds after it dies.",
                    script=counter, state=st))
                self.place(tag, x, z, Y_PIECE, ART_ROT_Y, w=size, d=size)

    # --------------------------------------------------------------- cards
    def build_cards(self):
        kits = self.src["kits"]
        order = sorted(kits.values(), key=lambda k: (ROLES.index(k["role"]), k["name"]))
        self.champ_order = [k["id"] for k in order]
        faces = [art.render_champion_card(k, self.v["roster"]) for k in order]
        cols, rows = 10, math.ceil(len(faces) / 10)
        champ_face = self.img(art.sheet(faces, cols, rows), "sheet_champions.png")
        champ_back = self.img(art.render_card_back("CHAMPION", (90, 70, 50)), "back_champion.png")
        self.champ_deck = (1, custom_deck(1, champ_face, champ_back, cols, rows))

        entries = []
        for k, v in STAT_ITEMS.items():
            entries.append(("stat", k, v["cost"], v["effect"], (70, 90, 120), "Stat boost"))
        for k, v in CARD_ITEMS.items():
            entries.append(("card", k, v["cost"], v["effect"], (70, 120, 90), "Card in hand"))
        buff_desc = {
            "blue_buff": BUFF_CARDS["blue_buff"]["effect"],
            "red_buff": BUFF_CARDS["red_buff"]["effect"],
        }
        dc = self.cfg.get("dragon_card")
        dragon_eff = (f"Reusable: {dc['hits']} hits on an adjacent non-structure unit, then "
                      f"cooldown track {dc['cooldown']}") if dc else "+1 AP each Upkeep"
        baron_eff = (f"Empowered waves: +{self.cfg['baron_wave_bonus']} chips, 2 hits on "
                     f"structures" + (", for the rest of the game" if self.cfg.get("baron_permanent")
                                      else ""))
        entries += [("buff", "blue_buff", None, buff_desc["blue_buff"], (40, 90, 200), "Buff card"),
                    ("buff", "red_buff", None, buff_desc["red_buff"], (190, 50, 40), "Buff card"),
                    ("buff", "dragon", None, dragon_eff, (200, 110, 30), "Objective card"),
                    ("buff", "baron", None, baron_eff, (110, 50, 150), "Objective card")]
        faces = [art.render_text_card(k.replace("_", " ").title(), kind, cost, eff, col,
                                      f"{self.v['stamp']}") for _, k, cost, eff, col, kind in entries]
        cols, rows = 10, math.ceil(len(faces) / 10)
        face = self.img(art.sheet(faces, cols, rows), "sheet_items.png")
        back = self.img(art.render_card_back("ITEM / BUFF", (60, 80, 110)), "back_items.png")
        self.item_deck = (2, custom_deck(2, face, back, cols, rows))
        self.item_index = {k: i for i, (_, k, *_rest) in enumerate(entries)}
        self.item_entries = entries

    def champ_cards(self, team: str) -> List[dict]:
        key, cdeck = self.champ_deck
        out = []
        for i, cid in enumerate(self.champ_order):
            k = self.src["kits"][cid]
            desc = "\n".join(art.ability_text(a, k["abilities"][a]) for a in ("L0", "Q", "W", "E", "R"))
            desc = f"{k['role']} \u00b7 HP {k['stats']['hp']} \u00b7 Speed {k['stats']['speed']}\n" + desc
            out.append(card(f"hn:card:champ:{team}:{cid}", k["name"], key, i, cdeck, desc=desc))
        return out

    def item_cards(self, team: str) -> List[dict]:
        key, cdeck = self.item_deck
        out = []
        for kind, k, cost, eff, _c, _l in self.item_entries:
            if kind == "stat":
                n = len(ROLES)                     # one copy per champion (Rules 12)
            elif kind == "card":
                n = MAX_CARD_COPIES
            else:
                continue
            for j in range(n):
                out.append(card(f"hn:card:item:{team}:{k}:{j}", k.replace("_", " ").title(), key,
                                self.item_index[k], cdeck, desc=f"{cost} AP \u00b7 {eff}"))
        return out

    def buff_cards(self, k: str, n: int) -> List[dict]:
        key, cdeck = self.item_deck
        return [card(f"hn:card:buff:{k}:{j}", k.replace("_", " ").title(), key,
                     self.item_index[k], cdeck) for j in range(n)]

    # ----------------------------------------------------------- dashboards
    def build_dashboards(self):
        cfg = self.cfg
        dc = cfg.get("dragon_card") or {}
        cds = [a["cooldown"] for k in self.src["kits"].values() for a in k["abilities"].values()]
        top = max([death_position(cfg, r) for r in range(1, cfg["round_limit"] + 1)]
                  + cds + [dc.get("cooldown", 0)])
        self.track_top = top
        slot_w, slot_d, gap = 2.7, 3.8, 0.2
        W, D = (top + 1) * (slot_w + gap) + 7.6, 9.4
        Wp, Dp = int(W * PPU), int(D * PPU)
        sx0, sy0 = 0.5 * PPU, 1.9 * PPU
        slots = {}
        for i, pos in enumerate(range(top, -1, -1)):
            x0 = sx0 + i * (slot_w + gap) * PPU
            slots[pos] = (int(x0), int(sy0), int(x0 + slot_w * PPU), int(sy0 + slot_d * PPU))
        pool_x0 = sx0 + (top + 1) * (slot_w + gap) * PPU + 0.3 * PPU
        pool = (int(pool_x0), int(sy0), int(Wp - 0.4 * PPU), int(sy0 + slot_d * PPU))
        buffs = (int(Wp * 0.52), int(sy0 + slot_d * PPU + 0.25 * PPU), int(Wp - 0.4 * PPU),
                 int(Dp - 0.3 * PPU))
        death = {}
        for rnd in range(1, cfg["round_limit"] + 1):
            death.setdefault(death_position(cfg, rnd), []).append(rnd)
        slot_notes = {}
        for pos, rnds in death.items():
            slot_notes[pos] = f"death R{rnds[0]}-{rnds[-1]}" if rnds[-1] < cfg["round_limit"] \
                else f"death R{rnds[0]}+"
        if dc:
            slot_notes[dc["cooldown"]] = (slot_notes.get(dc["cooldown"], "") + " dragon").strip()
        rows = round_rows(cfg)
        notes = [
            f"Death: {self.v['death']} rounds missed (track {', '.join(str(p) for p in cfg.get('death_track_positions') or [])}).",
            f"Kill = {cfg.get('kill_ap_waves')} waves of AP: "
            + " / ".join(sorted({r['kill'] for r in rows}, key=int)) + ".",
            f"AP refresh {cfg['ap_base']} each Upkeep; tower kill +{cfg.get('tower_kill_ap', 0)} AP.",
            f"Whole card goes on the track at the ability's cooldown.",
        ]
        layout = {"size": (Wp, Dp), "slots": slots, "slot_notes": slot_notes, "pool": pool,
                  "buffs": buffs, "notes_y": int(sy0 + slot_d * PPU + 0.3 * PPU)}
        mat_d = self.mat_size[1]
        self.dash = {}
        for team in TEAMS:
            facing = team
            rot = rot_for(facing)
            cz = (mat_d / 2 + 0.6 + D / 2) * (1 if team == "north" else -1)
            cx = 0.0
            url = self.img(art.render_dashboard(team, TEAM_SEAT[team], top, (slot_w, slot_d), notes,
                                                self.v, PPU, layout), f"dash_{team}.png")
            tag = f"hn:art:dash:{team}"
            self.objects.append(custom_tile(tag, f"{TEAM_SEAT[team]} dashboard", url, cx, Y_MAT, cz,
                                            rot, 1.0, thickness=0.2))
            self.place(tag, cx, cz, Y_MAT, rot, w=W, d=D, lock=True, art_obj=True)

            def world(px, py, _cx=cx, _cz=cz, _f=facing):
                return px_to_world(_cx, _cz, px - Wp / 2, py - Dp / 2, _f)

            slot_world = {}
            for pos, (x0, y0, x1, y1) in slots.items():
                wx, wz = world((x0 + x1) / 2, (y0 + y1) / 2)
                slot_world[pos] = (wx, wz)
                self.snaps.append({"Position": {"x": wx, "y": Y_MAT + 0.2, "z": wz},
                                   "Rotation": {"x": 0, "y": rot, "z": 0}})
            px0, py0, px1, py1 = pool
            pwx, pwz = world((px0 + px1) / 2, (py0 + py1) / 2)
            pw, pd = (px1 - px0) / PPU, (py1 - py0) / PPU
            ztag = f"hn:zone:pool:{team}"
            self.objects.append(zone(ztag, f"{TEAM_SEAT[team]} AP pool", pwx, Y_MAT + 1.5, pwz,
                                     pw, 3.0, pd))
            self.place(ztag, pwx, pwz, Y_MAT + 1.5, 0.0, w=0, d=0)
            bx0, by0, bx1, by1 = buffs
            bwx, bwz = world((bx0 + bx1) / 2, (by0 + by1) / 2 + 0.3 * PPU)
            self.dash[team] = {"slots": slot_world, "pool": (pwx, pwz), "buffs": (bwx, bwz),
                               "rot": rot, "cz": cz, "depth": D, "width": W}
        self.dash_w = W
        # the priority marker sits just outside the left end of the priority
        # team's dashboard
        self.prio_slots = {t: {"x": -(W / 2 + 1.0), "z": self.dash[t]["cz"]} for t in TEAMS}

    # ------------------------------------------------------------ tracker
    def build_tracker(self):
        cfg = self.cfg
        rows = round_rows(cfg)
        W, row_h, head = 15.0, 0.95, 1.9
        D = head + row_h * len(rows) + 1.0
        Wp, Dp = int(W * PPU), int(D * PPU)
        cols = [int(x * PPU) for x in (0.4, 1.6, 3.0, 4.6, 6.1, 7.8, 9.6)]
        row_px = {r["round"]: (int((head + (r["round"] - 1) * row_h) * PPU),
                               int((head + r["round"] * row_h) * PPU) - 2) for r in rows}
        layout = {"size": (Wp, Dp), "cols": cols, "rows": row_px}
        url = self.img(art.render_round_track(rows, self.v, layout), "round_tracker.png")
        cx = self.mat_size[0] / 2 + 1.0 + W / 2
        cz = 0.0
        tag = "hn:art:tracker"
        self.objects.append(custom_tile(tag, "Round tracker", url, cx, Y_MAT, cz, ART_ROT_Y, 1.0,
                                        thickness=0.2, desc=self.v["stamp"]))
        self.place(tag, cx, cz, Y_MAT, ART_ROT_Y, w=W, d=D, lock=True, art_obj=True)
        self.round_slots = {}
        for rnd, (y0, y1) in row_px.items():
            wx, wz = px_to_world(cx, cz, W * PPU - 0.9 * PPU - Wp / 2, (y0 + y1) / 2 - Dp / 2, "south")
            self.round_slots[rnd] = {"x": wx, "z": wz}
        self.tracker = (cx, cz, W, D)

    # ------------------------------------------------------------- pieces
    def build_pieces(self):
        kits = self.src["kits"]
        counter = self.load_lua("counter.lua")
        size = HEX * 1.5
        mw, md = self.mat_size
        left = -(mw / 2 + 1.0)
        # standee bags, champion decks and item decks, one column per team
        for team in TEAMS:
            sgn = 1 if team == "north" else -1
            rot = self.dash[team]["rot"]
            standees = []
            for cid in self.champ_order:
                k = kits[cid]
                url = self.img(art.render_standee(k, team), f"standee_{team}_{cid}.png")
                tag = f"hn:champ:{team}:{cid}"
                st = self.counter_state(kind="champion", label=k["name"], hp=k["stats"]["hp"],
                                        max=k["stats"]["hp"], floor=0, team=team, cid=cid)
                o = custom_token(tag, f"{k['name']} ({TEAM_SEAT[team]})", url, 0, Y_PIECE, 0, rot,
                                 1.0, thickness=0.25,
                                 desc=f"{k['role']} \u00b7 HP {k['stats']['hp']} \u00b7 Speed "
                                      f"{k['stats']['speed']}. Left-click -1 HP, right-click +1.",
                                 script=counter, state=st)
                standees.append(o)
                self.place(tag, 0, 0, Y_PIECE, rot, w=size, d=size, start=False)
            col = [c / 255 for c in art.TEAM_COLOURS[team]]
            col_a, col_b = left - 2.2, left - 5.8
            self.objects.append(bag(f"hn:bag:standees:{team}", f"{TEAM_SEAT[team]} champions",
                                    standees, col_a, Y_PIECE, 10.0 * sgn, colour=col))
            self.place(f"hn:bag:standees:{team}", col_a, 10.0 * sgn, Y_PIECE, rot)
            cards = self.champ_cards(team)
            _, cdeck = self.champ_deck
            dtag = f"hn:deck:champ:{team}"
            self.objects.append(deck(dtag, f"{TEAM_SEAT[team]} champion cards", cards, cdeck,
                                     col_b, Y_PIECE, 10.0 * sgn, rot))
            self.place(dtag, col_b, 10.0 * sgn, Y_PIECE, rot)
            icards = self.item_cards(team)
            _, idk = self.item_deck
            itag = f"hn:deck:items:{team}"
            self.objects.append(deck(itag, f"{TEAM_SEAT[team]} items (shop)", icards, idk,
                                     col_b, Y_PIECE, 5.6 * sgn, rot))
            self.place(itag, col_b, 5.6 * sgn, Y_PIECE, rot)

        # chip supply: team minion chips and neutral chips (HP of monsters and
        # structures, and AP). Every chip is 1 HP and 1 AP (Rules 1).
        chip_size = HEX * 0.85
        for key, colour, nick in (("north", art.TEAM_COLOURS["north"], "Blue minion chips"),
                                  ("south", art.TEAM_COLOURS["south"], "Red minion chips"),
                                  ("neutral", art.NEUTRAL_CHIP, "AP / HP chips")):
            url = self.img(art.render_chip(colour), f"chip_{key}.png")
            ctag = f"hn:chip:{key}"
            chip = custom_token(ctag, nick[:-1], url, 0, Y_PIECE, 0, 0.0, 1.0, thickness=0.12,
                                stackable=True, desc="1 chip = 1 HP = 1 AP")
            self.place(ctag, 0, 0, Y_PIECE, 0.0, w=chip_size, d=chip_size, start=False)
            z = {"north": 4.5, "south": -4.5, "neutral": 0.0}[key]
            btag = f"hn:bag:chips:{key}"
            self.objects.append(bag(btag, nick, [chip], left - 2.2, Y_PIECE, z,
                                    colour=[c / 255 for c in colour], infinite=True))
            self.place(btag, left - 2.2, z, Y_PIECE, 0.0)

        # buff and objective cards (supply)
        dragon_n = 2 * self.cfg.get("dragon_cap", 2)
        for i, (k, n) in enumerate((("blue_buff", 8), ("red_buff", 8), ("dragon", dragon_n),
                                    ("baron", 2))):
            _, idk = self.item_deck
            tag = f"hn:deck:buff:{k}"
            x, z = left - 9.4, 6.3 - 4.2 * i
            self.objects.append(deck(tag, k.replace("_", " ").title() + " cards",
                                     self.buff_cards(k, n), idk, x, Y_PIECE, z, ART_ROT_Y))
            self.place(tag, x, z, Y_PIECE, ART_ROT_Y)

        # round and priority markers
        for key, label, colour in (("round", "ROUND", (235, 196, 60)),
                                   ("priority", "PRIO", (240, 240, 240))):
            url = self.img(art.render_marker(label, colour), f"marker_{key}.png")
            tag = f"hn:marker:{key}"
            if key == "round":
                x, z = self.round_slots[1]["x"], self.round_slots[1]["z"]
            else:
                x, z = self.prio_slots["north"]["x"], self.prio_slots["north"]["z"]
            self.objects.append(custom_token(tag, f"{label.title()} marker", url, x, Y_PIECE, z,
                                             ART_ROT_Y, 1.0, thickness=0.15))
            self.place(tag, x, z, Y_PIECE, ART_ROT_Y, w=HEX * 0.9, d=HEX * 0.9)

    # ------------------------------------------------------------- global
    def data_lua(self, data: dict) -> str:
        data = dict(data)
        data["LAYOUT"] = self.layout
        data["ROUND_SLOTS"] = self.round_slots
        data["DASH"] = {t: {"pool": {"x": v["pool"][0], "z": v["pool"][1]},
                            "cz": v["cz"], "rot": v["rot"],
                            "slots": {str(p): {"x": xz[0], "z": xz[1]}
                                      for p, xz in v["slots"].items()}}
                        for t, v in self.dash.items()}
        data["PRIO_SLOTS"] = self.prio_slots
        data["TRACK_TOP"] = self.track_top
        data["ART_ROT_Y"] = ART_ROT_Y
        lines = ["-- Generated by tools/tts_export.py. Do not edit: rebuild instead.",
                 f"-- {self.v['stamp']}", ""]
        for k, v in data.items():
            lines.append(f"{k} = {lua_value(v)}")
            lines.append("")
        return "\n".join(lines)

    def save_file(self, data_lua: str) -> dict:
        glob = data_lua + "\n" + self.load_lua("global.lua")
        with open(os.path.join(LUA_DIR, "ui.xml")) as fh:
            xml = fh.read()
        xml = xml.replace("{{STAMP}}", self.v["stamp"])
        rules = (f"Hex-Nexus playtest mod. {self.v['stamp']}. Built {self.v['built']}. "
                 f"Rules: rules/Hex-Nexus_Rules_v{self.v['rules']}.md")
        return {
            "SaveName": f"Hex-Nexus {self.v['rules']} / {self.v['roster']} ({self.v['config']})",
            "EpochTime": 0, "Date": self.v["built"], "VersionNumber": "v13.2.2",
            "GameMode": "Hex-Nexus", "GameType": "", "GameComplexity": "", "Tags": [],
            "Gravity": 0.5, "PlayArea": 0.5, "Table": "Table_RPG", "Sky": "Sky_Museum",
            "Note": rules, "TabStates": {}, "Grid": {"Type": 0, "Lines": False, "Snapping": False},
            "Hands": {"Enable": True, "DisableUnused": False, "Hiding": 0},
            "LuaScript": glob, "LuaScriptState": "", "XmlUI": xml,
            "SnapPoints": self.snaps, "ObjectStates": self.objects,
        }


# ====================================================================== main
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--rules", default="1.9.0")
    ap.add_argument("--roster", default="1.9.0")
    ap.add_argument("--config", default="reports/requests/batch_0075.json")
    ap.add_argument("--out", default=os.path.join(TTS_DIR, "build"))
    ap.add_argument("--asset-base", default=None,
                    help="URL prefix the images are served from (default: raw GitHub on the "
                         "current branch). Use file:///C:/path/to/tts/build/assets for local tests.")
    args = ap.parse_args(argv)
    if not os.path.isabs(args.config):
        args.config = os.path.join(ROOT, args.config)

    src = load_sources(args)
    branch = git("rev-parse", "--abbrev-ref", "HEAD") or "master"
    asset_base = args.asset_base or f"{DEFAULT_REPO_RAW}/{branch}/tts/build/assets"

    b = Builder(src, args.out, asset_base)
    b.build_board()
    b.build_structures()
    b.build_monsters()
    b.build_cards()
    b.build_dashboards()
    b.build_tracker()
    b.build_pieces()

    data = build_data(src)
    data["VERSION"] = dict(data["VERSION"], asset_base=asset_base)
    dl = b.data_lua(data)
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "data.lua"), "w") as fh:
        fh.write(dl)
    save = b.save_file(dl)
    name = f"HexNexus_{src['versions']['rules']}_{src['versions']['roster']}.json"
    with open(os.path.join(args.out, name), "w") as fh:
        json.dump(save, fh, indent=1, ensure_ascii=False)
    n_assets = len(os.listdir(b.assets))
    print(f"{src['versions']['stamp']}")
    print(f"wrote {os.path.relpath(os.path.join(args.out, name), ROOT)}: "
          f"{len(save['ObjectStates'])} top-level objects, {n_assets} images, "
          f"{len(save['SnapPoints'])} snap points")
    print(f"assets served from {asset_base}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
