"""M0 smoke test: run the mod's scripts headless against a fake TTS API.

    python tts/tests/smoke_m0.py        (needs lua5.2 on PATH; rebuilds first)

Checks, in plain Lua 5.2 via tts/tests/tts_stub.lua:
  * every inlined script compiles and loads;
  * calibration fits each generated object to the exporter's size, whatever
    base size TTS gives a custom image, and centres art on its bounds;
  * the panel's per-round numbers (wave spawn and size, decay, kill AP, death
    track position) match the Python engine, computed here by running
    engine.game / engine.resolve on a real game state, not re-derived;
  * AP pool counting, hexgroup flips, HP counters and save/load of the Global
    state.
The Lua referee parity harness (tts/tests/run.lua) is milestone M2.
"""
from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)

from engine.config import make_config                     # noqa: E402
from engine.game import decay_structures, new_game, wave_size  # noqa: E402
from engine.hexmap import Board                            # noqa: E402
from engine.kits import load_roster                        # noqa: E402
from engine.resolve import kill_champion, kill_reward      # noqa: E402

CONFIG = os.path.join(ROOT, "reports", "requests", "batch_0075.json")
ROSTER = os.path.join(ROOT, "roster", "roster_v1.9.0.json")
SAVE = os.path.join(ROOT, "tts", "build", "HexNexus_1.9.0_1.9.0.json")


def engine_rounds(config_path: str) -> list:
    """Per-round numbers straight from the engine."""
    with open(config_path) as fh:
        cfg = make_config(**json.load(fh).get("config_overrides", {}))
    board = Board.load()
    kits = load_roster(ROSTER)
    by_role = {}
    for k in kits.values():
        by_role.setdefault(k["role"], k["id"])
    picks = {"north": list(by_role.values()), "south": list(by_role.values())}
    base = new_game(board, kits, picks, cfg)
    out = []
    for rnd in range(1, cfg["round_limit"] + 1):
        st = copy.deepcopy(base)
        st.round = rnd
        victim = next(c for c in st.champs.values() if c.team == "north")
        kill_champion(st, victim, "south", None)
        for s in st.structures.values():
            s.chips = 12                       # above any floor, so decay shows
        before = {u: s.chips for u, s in st.structures.items()}
        decay_structures(st)
        decays = any(st.structures[u].chips != before[u] for u in before)
        # a kill by a team holding the Baron card: the designer's rule is two
        # Empowered waves; the engine currently leaves the bonus out (bug)
        st.teams["south"].baron_track = 10 ** 6
        baron_engine = kill_reward(st)
        baron_rule = int(cfg["kill_ap_waves"] * (wave_size(st) + cfg["baron_wave_bonus"]) + 0.5)
        out.append({"round": rnd, "kill_ap": kill_reward(st), "death_pos": victim.track,
                    "wave_size": wave_size(st),
                    "spawn": rnd % 2 == 1 or not cfg["wave_spawn_odd_rounds_only"],
                    "decays": decays, "kill_ap_baron_rule": baron_rule,
                    "kill_ap_baron_engine": baron_engine})
    return out


def fixture(save: dict) -> dict:
    objs = []

    def spec(o, extra=None):
        ci = o.get("CustomImage")
        d = {"guid": o["GUID"], "tag": o.get("GMNotes", ""), "nick": o.get("Nickname", ""),
             "name": o["Name"], "locked": o.get("Locked", False), "custom": ci is not None,
             "script": o.get("LuaScript", ""), "state": o.get("LuaScriptState", "")}
        d.update(extra or {})
        return d
    for o in save["ObjectStates"]:
        d = spec(o)
        if "States" in o:
            d["states"] = {"1": spec(o), "2": spec(o["States"]["2"])}
        objs.append(d)
    return {"objects": objs}


LUA_TEST = r'''
package.path = HERE .. "/?.lua;" .. package.path
local Stub = require("tts_stub")
local fx = Stub.JSON.decode(io.open(FIXTURE):read("*a"))
local expect = fx.expect
local fails, checks = 0, 0
local function check(cond, msg)
  checks = checks + 1
  if not cond then fails = fails + 1; print("FAIL: " .. msg) end
end

-- objects; aspect from the layout so a fitted object has the right footprint
local objs = {}
for _, s in ipairs(fx.objects) do
  if s.states then
    s.states[1] = s.states["1"]; s.states[2] = s.states["2"]
  end
  objs[#objs + 1] = Stub.add(s)
end
local G = Stub.runScript(io.open(GLOBAL):read("*a"), nil, "Global")
Stub.global = G
for _, s in ipairs(fx.objects) do
  local sp = G.LAYOUT[s.tag]
  if sp and sp.w and sp.w > 0 then s.aspect = sp.d / sp.w end
  if s.states then
    for _, st in pairs(s.states) do
      local sp2 = G.LAYOUT[st.tag]
      if sp2 and sp2.w > 0 then st.aspect = sp2.d / sp2.w end
    end
  end
end
-- object scripts
for _, o in ipairs(objs) do
  local s = o._spec
  if s.script ~= "" then
    local env = Stub.runScript(s.script, o, s.tag)
    if env.onLoad then env.onLoad(s.state) end
  end
end
G.onLoad("")
Stub.flush()
check(G.onSave():find('"calibrated":true') ~= nil, "Global calibrated on first load")

-- fitting and placement
local fitted = 0
for _, o in ipairs(Stub.objects) do
  local sp = G.LAYOUT[o.getGMNotes()]
  if sp then
    if sp.w and sp.w > 0 then
      local b = o.getBoundsNormalized().size
      check(math.abs(b.x - sp.w) < 0.01 * sp.w, o.getGMNotes() .. " width " .. b.x .. " ~= " .. sp.w)
      check(math.abs(b.z - sp.d) < 0.01 * sp.d, o.getGMNotes() .. " depth " .. b.z .. " ~= " .. sp.d)
      fitted = fitted + 1
    end
    if sp.start then
      local c = sp.art and o.getBounds().center or o.getPosition()
      check(math.abs(c.x - sp.x) < 0.03 and math.abs(c.z - sp.z) < 0.03,
        o.getGMNotes() .. " placed at " .. c.x .. "," .. c.z .. " not " .. sp.x .. "," .. sp.z)
    end
    if sp.lock then check(o.getLock(), o.getGMNotes() .. " locked") end
  end
end
check(fitted >= 59, "fitted " .. fitted .. " objects")

-- stacking: tiles rest on the mat's measured top, pieces on their tile's
local function byTag(t)
  for _, o in ipairs(Stub.objects) do if o.getGMNotes() == t then return o end end
end
local function top(o) local b = o.getBounds(); return b.center.y + b.size.y / 2 end
local function bottom(o) local b = o.getBounds(); return b.center.y - b.size.y / 2 end
local mat = byTag("hn:art:mat")
for _, o in ipairs(Stub.objects) do
  local sp = G.LAYOUT[o.getGMNotes()]
  if sp and sp.on and sp.start then
    local base = byTag(sp.on)
    check(base ~= nil, o.getGMNotes() .. " base " .. sp.on .. " exists")
    if base then
      check(bottom(o) >= top(base) - 1e-6, o.getGMNotes() .. " rests above " .. sp.on)
    end
  end
end
check(bottom(byTag("hn:tile:Mid River:hidden")) >= top(mat) - 1e-6, "tiles sit on top of the mat")

-- per-round numbers against the engine
for r = 1, #expect do
  local e = expect[r]
  local row = G.ROUNDS[r]
  check(row.kill_ap == e.kill_ap, "round " .. r .. " kill AP " .. row.kill_ap .. " vs engine " .. e.kill_ap)
  check(row.death_pos == e.death_pos, "round " .. r .. " death pos " .. row.death_pos .. " vs engine " .. e.death_pos)
  check(row.wave_size == e.wave_size, "round " .. r .. " wave size")
  check(row.spawn == e.spawn, "round " .. r .. " spawn")
  check(row.kill_ap_baron == e.kill_ap_baron_rule,
    "round " .. r .. " Baron kill AP " .. row.kill_ap_baron .. " vs rule " .. e.kill_ap_baron_rule)
  if e.kill_ap_baron_engine ~= e.kill_ap_baron_rule and not baron_noted then
    baron_noted = true
    print("NOTE: engine kill_reward ignores the Baron bonus (" .. e.kill_ap_baron_engine .. " vs "
      .. e.kill_ap_baron_rule .. "); the mod follows the designer. RULES_DISCREPANCIES #12")
  end
  check(row.decays == e.decays, "round " .. r .. " decay " .. tostring(row.decays) .. " vs engine " .. tostring(e.decays))
end

-- panel walk-through
check(Stub.ui.hnRound:find("Round 1 / 20") ~= nil, "panel round 1: " .. tostring(Stub.ui.hnRound))
check(Stub.ui.hnPrio:find("Red") ~= nil, "round 1 priority is South (Red)")
for r = 2, #expect do
  G.uiNextRound()
  local info = Stub.ui.hnInfo
  local e = expect[r]
  check(Stub.ui.hnRound:find("Round " .. r .. " ") ~= nil, "panel shows round " .. r)
  check(info:find("kill = " .. e.kill_ap .. " AP", 1, true) ~= nil, "round " .. r .. " panel kill: " .. info)
  check(info:find("track " .. e.death_pos, 1, true) ~= nil, "round " .. r .. " panel death: " .. info)
  check((info:find("decay", 1, true) ~= nil) == e.decays, "round " .. r .. " panel decay: " .. info)
  local want = (r % 2 == 1) and "Red" or "Blue"
  check(Stub.ui.hnPrio:find(want) ~= nil, "round " .. r .. " priority " .. Stub.ui.hnPrio)
end
G.uiNextRound()
check(Stub.ui.hnRound:find("Round " .. #expect .. " ") ~= nil, "round stops at the limit")
for _ = 1, 5 do G.uiNextPhase() end
check(Stub.ui.hnRound:find("Upkeep") ~= nil, "phase wraps to Upkeep")
G.uiPrevRound()
local m = G.ROUND_SLOTS[#expect - 1]
local marker
for _, o in ipairs(Stub.objects) do if o.getGMNotes() == "hn:marker:round" then marker = o end end
local p = marker.getPosition()
check(math.abs(p.x - m.x) < 1e-6 and math.abs(p.z - m.z) < 1e-6, "round marker follows the round")

-- AP pool counting
local zone
for _, o in ipairs(Stub.objects) do if o.getGMNotes() == "hn:zone:pool:north" then zone = o end end
local chips = {
  Stub.newObject({guid = "c1", tag = "hn:chip:neutral", quantity = 5}),
  Stub.newObject({guid = "c2", tag = "hn:chip:neutral"}),
  Stub.newObject({guid = "c3", tag = "hn:art:dash:north", locked = true}),
}
zone._spec.contents = function() return chips end
Stub.tick()
check(Stub.ui.hnAP:find("Blue 6", 1, true) ~= nil, "pool count: " .. tostring(Stub.ui.hnAP))

-- hexgroup flip
local tile
for _, o in ipairs(Stub.objects) do if o.getGMNotes() == "hn:tile:Baron Pit:hidden" then tile = o end end
G.hnFlipTile({guid = tile.getGUID()})
Stub.flush()
local flipped
for _, o in ipairs(Stub.objects) do if o.getGMNotes() == "hn:tile:Baron Pit:visible" then flipped = o end end
check(flipped ~= nil, "flip swaps to the visible state")
if flipped then
  local sp = G.LAYOUT["hn:tile:Baron Pit:visible"]
  check(math.abs(flipped.getBoundsNormalized().size.x - sp.w) < 0.01 * sp.w, "flipped tile fitted")
  G.hnFlipTile({guid = flipped.getGUID()}); Stub.flush()
end

-- HP counters
for _, o in ipairs(Stub.objects) do
  if o.getGMNotes() == "hn:struct:north:nexus" then
    local st = o._env.hnGet()
    check(st.hp == G.CONFIG.nexus_hp and st.floor == G.FLOORS.nexus, "Nexus starts at config HP and floor")
    o._env.hnClick(o, "Blue", false)
    check(o._env.hnGet().hp == G.CONFIG.nexus_hp - 1, "left-click removes 1 HP")
    check(o._buttons[1].label:find("min " .. G.FLOORS.nexus) ~= nil, "structure label shows its floor")
    o._env.hnClick(o, "Blue", true)
    check(o._env.hnGet().hp == G.CONFIG.nexus_hp, "right-click adds 1 HP")
    check(Stub.JSON.decode(o._env.onSave()).hp == G.CONFIG.nexus_hp, "counter saves its HP")
  end
  if o.getGMNotes() == "hn:monster:baron:0" then
    check(o._env.hnGet().hp == 0 and o._buttons[1].label == "down", "Baron starts down (spawns later)")
  end
end

-- Global state survives save/load
local saved = G.onSave()
local G2 = Stub.runScript(io.open(GLOBAL):read("*a"), nil, "Global2")
Stub.global = G2
G2.onLoad(saved); Stub.flush()
check(G2.onSave() == saved or Stub.JSON.decode(G2.onSave()).round == Stub.JSON.decode(saved).round,
  "Global state round-trips")

print(string.format("%d checks, %d failed", checks, fails))
os.exit(fails == 0 and 0 or 1)
'''


def main() -> int:
    subprocess.check_call([sys.executable, os.path.join(ROOT, "tools", "tts_export.py"),
                           "--config", CONFIG], stdout=subprocess.DEVNULL)
    with open(SAVE) as fh:
        save = json.load(fh)
    fx = fixture(save)
    fx["expect"] = engine_rounds(CONFIG)
    with tempfile.TemporaryDirectory() as tmp:
        fpath = os.path.join(tmp, "fixture.json")
        gpath = os.path.join(tmp, "global.lua")
        tpath = os.path.join(tmp, "test.lua")
        with open(fpath, "w") as fh:
            json.dump(fx, fh)
        with open(gpath, "w") as fh:
            fh.write(save["LuaScript"])
        with open(tpath, "w") as fh:
            fh.write(f"HERE = {json.dumps(HERE)}\nFIXTURE = {json.dumps(fpath)}\n"
                     f"GLOBAL = {json.dumps(gpath)}\n" + LUA_TEST)
        lua = next((p for p in ("lua5.2", "lua") if subprocess.call(
            ["which", p], stdout=subprocess.DEVNULL) == 0), None)
        if lua is None:
            print("lua5.2 not found: apt-get install lua5.2")
            return 2
        return subprocess.call([lua, tpath])


if __name__ == "__main__":
    sys.exit(main())
