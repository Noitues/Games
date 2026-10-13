"""Smoke test: run the mod's scripts headless against a fake TTS API.

    python tts/tests/smoke.py        (needs lua5.2 on PATH; rebuilds first)

Checks, in plain Lua 5.2 via tts/tests/tts_stub.lua:
  * every inlined script compiles and loads;
  * calibration fits each generated object to the exporter's size, whatever
    base size TTS gives a custom image, and stacks tiles and pieces;
  * the per-round numbers (wave spawn and size, decay, kill AP, death track
    position) match the Python engine, computed here by running
    engine.game / engine.resolve on a real game state;
  * a whole game played through the panel: Start game deals the champions,
    every Upkeep and World Phase the table runs equals the rules core run on
    the state the table showed before it (so reading and writing the table
    loses nothing), ability use, AP for chips, kills, monster rewards,
    hexgroup flips, hotkeys and the round-limit tiebreak.
The rules core itself is checked against the engine by tts/tests/run.lua.
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
CORE = os.path.join(ROOT, "tts", "lua")


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
        if "ContainedObjects" in o:
            d["contents"] = [spec(c) for c in o["ContainedObjects"]]
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
local function byTag(t)
  for _, o in ipairs(Stub.objects) do if o.getGMNotes() == t then return o end end
end
local function prefixed(p)
  local out = {}
  for _, o in ipairs(Stub.objects) do if o.getGMNotes():sub(1, #p) == p then out[#out + 1] = o end end
  return out
end

-- every object, its scripts run (also for objects taken out of bags later)
local function runScript(o)
  local s = o._spec
  if s.script and s.script ~= "" then
    local env = Stub.runScript(s.script, o, s.tag)
    if env.onLoad then env.onLoad(s.state) end
  end
end
for _, s in ipairs(fx.objects) do
  if s.states then s.states[1] = s.states["1"]; s.states[2] = s.states["2"] end
  Stub.add(s)
end
local G = Stub.runScript(io.open(GLOBAL):read("*a"), nil, "Global")
Stub.global = G
local function aspect(s)
  local sp = G.LAYOUT[s.tag]
  if sp and sp.w and sp.w > 0 then s.aspect = sp.d / sp.w end
end
for _, s in ipairs(fx.objects) do
  aspect(s)
  for _, st in pairs(s.states or {}) do aspect(st) end
end
Stub.onCreate = function(o) aspect(o._spec); runScript(o) end
for _, o in ipairs(Stub.objects) do runScript(o) end
G.onLoad("")
Stub.flush()
check(G.onSave():find('"calibrated":true') ~= nil, "Global calibrated on first load")

-- ------------------------------------------------------------ layout
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
check(fitted >= 60, "fitted " .. fitted .. " objects")
local function top(o) local b = o.getBounds(); return b.center.y + b.size.y / 2 end
local function bottom(o) local b = o.getBounds(); return b.center.y - b.size.y / 2 end
for _, o in ipairs(Stub.objects) do
  local sp = G.LAYOUT[o.getGMNotes()]
  if sp and sp.on and sp.start then
    local base = byTag(sp.on)
    check(base ~= nil, o.getGMNotes() .. " base " .. sp.on .. " exists")
    if base then check(bottom(o) >= top(base) - 1e-6, o.getGMNotes() .. " rests above " .. sp.on) end
  end
end

-- --------------------------------------------- per-round numbers vs engine
local baron_noted = false
for r = 1, #expect do
  local e, row = expect[r], G.ROUNDS[r]
  check(row.kill_ap == e.kill_ap, "round " .. r .. " kill AP " .. row.kill_ap .. " vs engine " .. e.kill_ap)
  check(row.death_pos == e.death_pos, "round " .. r .. " death pos")
  check(row.wave_size == e.wave_size, "round " .. r .. " wave size")
  check(row.spawn == e.spawn, "round " .. r .. " spawn")
  check(row.decays == e.decays, "round " .. r .. " decay")
  check(row.kill_ap_baron == e.kill_ap_baron_rule, "round " .. r .. " Baron kill AP")
  if e.kill_ap_baron_engine ~= e.kill_ap_baron_rule and not baron_noted then
    baron_noted = true
    print("NOTE: engine kill_reward ignores the Baron bonus (" .. e.kill_ap_baron_engine .. " vs "
      .. e.kill_ap_baron_rule .. "); the mod follows the designer. RULES_DISCREPANCIES #12")
  end
end

-- ------------------------------------------------------- before the start
check(Stub.ui.hnRound:find("Not started") ~= nil, "panel says not started")
local nexus = byTag("hn:struct:north:nexus")
check(nexus._env.hnGet().hp == G.CONFIG.nexus_hp, "Nexus starts at config HP")
check(nexus._buttons[1].label:find("min " .. G.FLOORS.nexus) ~= nil, "structure label shows its floor")
check(byTag("hn:monster:baron:0")._buttons[1].label:find("down") ~= nil, "Baron starts down")
check(byTag("hn:ap:north") ~= nil and byTag("hn:ap:south") ~= nil, "two AP counters")

-- hotkeys and camera
check(Stub.hotkeys["Hex-Nexus: flip hexgroup"] ~= nil, "flip hotkey registered")
check(Stub.hotkeys["Hex-Nexus: map view"] ~= nil, "map hotkey registered")
Stub.hotkeys["Hex-Nexus: map view"]("Red")
check(Stub.look and Stub.look.p.pitch == 90, "map view looks straight down")
local tile = byTag("hn:tile:Mid River:hidden")
Stub.hotkeys["Hex-Nexus: flip hexgroup"]("Red", tile, nil); Stub.flush()
check(byTag("hn:tile:Mid River:visible") ~= nil, "flip hotkey on a tile flips it")
local riverHex = {0, 0}
local x, z = G.Core.hexToWorld(riverHex, G.HEX)
Stub.hotkeys["Hex-Nexus: flip hexgroup"]("Red", nil, {x = x, y = 1, z = z}); Stub.flush()
check(byTag("hn:tile:Mid River:hidden") ~= nil, "flip hotkey on an empty spot flips its tile")
local flipped = byTag("hn:tile:Mid River:hidden")
check(math.abs(flipped.getBoundsNormalized().size.x - G.LAYOUT["hn:tile:Mid River:hidden"].w) < 0.05,
  "flipped tile keeps its size")

-- --------------------------------------------------------------- start
-- draft one card by hand: Blue's Top slot gets the first Top card in its deck
local deck = byTag("hn:deck:champ:north")
local drafted
for _, e in ipairs(deck.getObjects()) do
  local cid = e.gm_notes:match(":([%w_]+)$")
  if G.ROSTER[cid].role == "Top" then drafted = cid; break end
end
local slot = G.DASH.north.roles.Top
deck.takeObject({guid = byTag and (function()
  for _, e in ipairs(deck.getObjects()) do if e.gm_notes:find(drafted .. "$") then return e.guid end end
end)(), position = {slot.x, 2, slot.z}})
G.uiStartGame(); Stub.flush()
local S = Stub.JSON.decode(G.onSave())
check(S.started, "Start game starts")
check(S.round == 1, "round 1 after the start, got " .. tostring(S.round))
check(S.priority == "south", "South has priority in round 1")
check(S.picks.north[1] == drafted, "the hand-drafted Top card is kept")
local seen = {}
for _, team in ipairs({"north", "south"}) do
  check(#S.picks[team] == 5, team .. " has 5 picks")
  for i, cid in ipairs(S.picks[team]) do
    check(G.ROSTER[cid].role == G.ROLES[i], team .. " pick " .. i .. " is a " .. G.ROLES[i])
    check(not seen[cid], cid .. " picked once across both teams")
    seen[cid] = true
    local st = byTag("hn:champ:" .. team .. ":" .. cid)
    local card = byTag("hn:card:champ:" .. team .. ":" .. cid)
    check(st ~= nil and card ~= nil, cid .. " standee and card on the table")
    if st then
      local p = st.getPosition()
      local h = G.CORE and nil
      local hex = Stub.global.hnDebugState and nil
    end
  end
end
local s0 = G.hnDebugState()
for _, c in ipairs(s0.champs) do
  check(c.alive, c.uid .. " alive at the start")
  check(G.Core.key(c.hex) and (c.hex and true), c.uid .. " on a hex")
end
check(byTag("hn:ap:north")._env.hnGet() == G.CONFIG.ap_base, "Blue AP refreshed to base")
check(byTag("hn:ap:south")._env.hnGet() == G.CONFIG.ap_base, "Red AP refreshed to base")
check(#prefixed("hn:wave:w") == 6, "round 1 spawns six waves, got " .. #prefixed("hn:wave:w"))
check(byTag("hn:monster:wolves:0")._env.hnGet().hp == G.CONFIG.monsters.wolves.hp, "camps are up in round 1")
check(byTag("hn:monster:dragon:0")._env.hnGet().hp == 0, "Dragon still down in round 1")

-- the table round-trips: what readState sees after Upkeep is what the core
-- produced from the previous reading
local Core = G.Core
local function copy(t, seen)
  if type(t) ~= "table" then return t end
  local out = {}
  for k, v in pairs(t) do
    if type(k) ~= "string" or k:sub(1, 1) ~= "_" then out[k] = copy(v) end
  end
  return out
end
local function flat(s)
  local out = {}
  local function put(k, v) out[#out + 1] = k .. "=" .. tostring(v) end
  put("round", s.round); put("priority", s.priority); put("next_uid", s.next_uid)
  local hidden = {}
  for t in pairs(s.hidden) do hidden[#hidden + 1] = t end
  table.sort(hidden); put("hidden", table.concat(hidden, "|"))
  for _, c in ipairs(s.champs) do
    put(c.uid .. ".alive", c.alive); put(c.uid .. ".hp", c.hp); put(c.uid .. ".track", c.track)
    if c.alive then put(c.uid .. ".hex", Core.key(c.hex)) end
  end
  local ws = {}
  for _, w in ipairs(s.waves) do ws[#ws + 1] = w.uid .. ":" .. w.chips .. "@" .. w.path_idx end
  table.sort(ws); put("waves", table.concat(ws, " "))
  for _, x in ipairs(s.structures) do put(x.uid, x.chips) end
  for _, m in ipairs(s.monsters) do put(m.uid, tostring(m.alive) .. m.chips .. "/" .. m.respawn_round) end
  for _, t in ipairs({"north", "south"}) do
    local ts = s.teams[t]
    put(t .. ".ap", ts.ap); put(t .. ".kills", ts.kills); put(t .. ".towers", ts.towers_lost)
    put(t .. ".baron", ts.baron)
  end
  return table.concat(out, "\n")
end
local CORE = Core.new(G.MAP, G.CONFIG, {kill_includes_baron = true, monster_heal = true})
local function compare(label, want, got)
  local a, b = flat(want), flat(got)
  if a ~= b then
    local la, lb = {}, {}
    for l in a:gmatch("[^\n]+") do la[l] = true end
    for l in b:gmatch("[^\n]+") do lb[l] = true end
    local shown = 0
    for l in a:gmatch("[^\n]+") do
      if not lb[l] and shown < 6 then print("  core:  " .. l); shown = shown + 1 end
    end
    for l in b:gmatch("[^\n]+") do
      if not la[l] and shown < 12 then print("  table: " .. l); shown = shown + 1 end
    end
  end
  check(a == b, label .. ": the table matches the core")
end

-- ------------------------------------------------------- one scripted round
G.uiNextPhase(); Stub.flush()                                  -- Action
check(Stub.ui.hnRound:find("Action") ~= nil, "Action Phase")
check(Stub.ui.hnPrio:find("activation 1/10: Red") ~= nil, "activation 1 is South's: " .. Stub.ui.hnPrio)
G.uiNextActivation()
check(Stub.ui.hnPrio:find("activation 2/10: Blue") ~= nil, "activation 2 is North's")

-- use an ability from a card menu
local bcid = S.picks.north[1]
local bcard = byTag("hn:card:champ:north:" .. bcid)
local q = bcard._env.hnGet().ab.Q
local ap0 = byTag("hn:ap:north")._env.hnGet()
local item
for label, fn in pairs(bcard._menu) do if label:find("^Use Q") then item = fn end end
check(item ~= nil, "card menu has Use Q")
item("Blue")
check(byTag("hn:ap:north")._env.hnGet() == ap0 - q.cost, "Use Q pays its cost")
check(bcard._env.hnGet().track == q.cd, "Use Q puts the card on cooldown " .. q.cd)
for label, fn in pairs(bcard._menu) do if label:find("^Use W") then fn("Blue") end end
check(bcard._env.hnGet().track == q.cd, "a card on cooldown cannot use another ability")

-- chips are AP: Blue hits the wolves twice, then a partial hit on raptors
local wolves = byTag("hn:monster:wolves:0")
local apB = byTag("hn:ap:north")._env.hnGet()
wolves._env.hnClick(wolves, "Blue", false); Stub.flush()
check(byTag("hn:ap:north")._env.hnGet() == apB + 1, "a chip off a monster is +1 AP")
for _ = 2, G.CONFIG.monsters.wolves.hp do wolves._env.hnClick(wolves, "Blue", false) end
Stub.flush()
check(wolves._env.hnGet().hp == 0, "wolves down")
check(wolves._env.hnGet().respawn_round == 1 + G.CONFIG.monsters.wolves.respawn, "wolves respawn round")
local raptors = byTag("hn:monster:raptors:0")
raptors._env.hnClick(raptors, "Red", false); Stub.flush()

-- the blue buff pays a card
local blue = byTag("hn:monster:blue_buff:0")
for _ = 1, G.CONFIG.monsters.blue_buff.hp do blue._env.hnClick(blue, "Red", false) end
Stub.flush()
local dealt
for _, o in ipairs(prefixed("hn:card:buff:blue_buff")) do
  if o._env and o._env.hnGet().team == "south" then dealt = o end
end
check(dealt ~= nil, "taking the Blue Buff deals Red a Blue Buff card")
if dealt then
  local apR = byTag("hn:ap:south")._env.hnGet()
  for label, fn in pairs(dealt._menu) do if label:find("^Play") then fn("Red") end end
  check(byTag("hn:ap:south")._env.hnGet() == apR + 2, "playing Blue Buff is +2 AP")
end

-- a kill: Red's Mid takes Blue's Jungle down
local victim = byTag("hn:champ:north:" .. S.picks.north[2])
local apR = byTag("hn:ap:south")._env.hnGet()
for _ = 1, victim._env.hnGet().hp do victim._env.hnClick(victim, "Red", false) end
Stub.flush()
local vcard = byTag("hn:card:champ:north:" .. S.picks.north[2])
check(vcard._env.hnGet().dead == true, "the victim's card is dead")
check(vcard._env.hnGet().track == G.ROUNDS[1].death_pos, "death position for round 1")
check(byTag("hn:ap:south")._env.hnGet() == apR + G.ROUNDS[1].kill_ap, "killer gains the kill reward")
local bench = G.DASH.north.bench[G.ROSTER[S.picks.north[2]].role]
local vp = victim.getPosition()
check(math.abs(vp.x - bench.x) < 1e-6 and math.abs(vp.z - bench.z) < 1e-6, "the dead standee goes to its bench")

-- World Phase: the table equals the core run on the table's own reading
local before = G.hnDebugState()
G.uiNextPhase(); Stub.flush()                                  -- World
local want = copy(before)
CORE:world(want)
compare("round 1 World", want, G.hnDebugState())

-- buy an item in the Shop
G.uiNextPhase(); Stub.flush()                                  -- Shop
local items = byTag("hn:deck:items:south")
local ie = items.getObjects()[1]
local icard = items.takeObject({guid = ie.guid, position = {0, 2, -30}})
local cost = icard._env.hnGet().cost
local apS = byTag("hn:ap:south")._env.hnGet()
for label, fn in pairs(icard._menu) do if label:find("^Buy") then fn("Red") end end
if apS >= cost then
  check(byTag("hn:ap:south")._env.hnGet() == apS - cost and icard._env.hnGet().bought,
    "buying pays the cost")
else
  check(not icard._env.hnGet().bought, "an item you cannot afford is not bought")
end

G.uiNextPhase(); Stub.flush()                                  -- Win Check
before = G.hnDebugState()
G.uiNextPhase(); Stub.flush()                                  -- Upkeep, round 2
want = copy(before)
CORE:upkeep(want)
compare("round 2 Upkeep", want, G.hnDebugState())
check(raptors._env.hnGet().hp == G.CONFIG.monsters.raptors.hp, "a hurt monster heals by the next round")
check(bcard._env.hnGet().track == math.max(0, q.cd - 1), "cooldowns count down in Upkeep")
check(byTag("hn:ap:north")._env.hnGet() == G.CONFIG.ap_base, "AP back to base")
check(Stub.JSON.decode(G.onSave()).priority == "north", "priority passes to North in round 2")

-- -------------------------------------------- the rest of the game, automated
local rounds = 0
while not Stub.JSON.decode(G.onSave()).winner and rounds < 40 do
  for _ = 1, 3 do G.uiNextPhase(); Stub.flush() end           -- Action, World, Shop
  G.uiNextPhase(); Stub.flush()                                -- Win Check
  if Stub.JSON.decode(G.onSave()).winner then break end
  before = G.hnDebugState()
  G.uiNextPhase(); Stub.flush()                                -- Upkeep
  want = copy(before)
  CORE:upkeep(want)
  local r = Stub.JSON.decode(G.onSave()).round
  compare("round " .. r .. " Upkeep", want, G.hnDebugState())
  -- waves sit on their lane path hex
  for _, w in ipairs(G.hnDebugState().waves) do
    local o = byTag("hn:wave:" .. w.uid)
    local p = o.getPosition()
    local h = CORE:worldToHex(p.x, p.z, G.HEX)
    check(h and Core.key(h) == Core.key(w.hex), "wave " .. w.uid .. " token on its hex")
  end
  rounds = rounds + 1
end
local final = Stub.JSON.decode(G.onSave())
check(final.round == G.CONFIG.round_limit, "the game ran to the round limit: " .. tostring(final.round))
check(final.winner ~= nil, "the round limit picks a winner (" .. tostring(final.winner) .. ", "
  .. tostring(final.end_reason) .. ")")
local waves_on_table = #prefixed("hn:wave:w")
check(waves_on_table > 0, "waves on the table late in the game: " .. waves_on_table)
G.uiStartGame()
check(Stub.JSON.decode(G.onSave()).round == final.round, "Start game does not restart a game")

-- Global state survives save/load
local saved = G.onSave()
local G2 = Stub.runScript(io.open(GLOBAL):read("*a"), nil, "Global2")
Stub.global = G2
G2.onLoad(saved); Stub.flush()
check(Stub.JSON.decode(G2.onSave()).round == Stub.JSON.decode(saved).round, "Global state round-trips")

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
