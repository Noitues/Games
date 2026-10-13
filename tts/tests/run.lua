--[[ Parity harness: replay engine scenarios through the Lua rules core.

    lua5.2 tts/tests/run.lua [scenarios.json] [data.lua]

Each scenario (from tools/tts_parity.py) is a state taken from a real engine
game just before an Upkeep or a World Phase, plus the state the engine
produced. The core runs the same step on `before`, and every field the core
models is compared with `after`. Exit status 0 only when all scenarios match.

The core runs with the designer's table-only rulings switched off
(kill_includes_baron, monster_heal), because the engine does not have them
yet; tts/tests/smoke_m0.py checks those separately.
]]
local here = (arg and arg[0] or ""):match("^(.*)/[^/]*$") or "."
package.path = here .. "/?.lua;" .. here .. "/../lua/?.lua;" .. package.path
local Stub = require("tts_stub")
local Core = require("core")

local scen_path = arg[1] or (here .. "/scenarios.json")
local data_path = arg[2] or (here .. "/../build/data.lua")
local env = setmetatable({}, {__index = _G})
assert(loadfile(data_path, "t", env))()

local fh = assert(io.open(scen_path))
local file = Stub.JSON.decode(fh:read("*a"))
fh:close()

local core = Core.new(env.MAP, env.CONFIG, {kill_includes_baron = false, monster_heal = false})

local function prepare(s)
  local hidden = {}
  for _, t in ipairs(s.hidden or {}) do hidden[t] = true end
  s.hidden = hidden
  s.wards = s.wards or {}
  for _, c in ipairs(s.champs) do
    local items = {}
    for _, i in ipairs(c.items or {}) do items[i] = true end
    c.items = items
  end
  for _, t in pairs(s.teams) do t.cards = t.cards or {}; t.dragon_track = t.dragon_track or {} end
  return s
end

-- Flatten the fields the core models into "path = value" lines.
local function flat(s)
  local out = {}
  local function put(k, v) out[#out + 1] = k .. " = " .. tostring(v) end
  put("round", s.round); put("priority", s.priority); put("next_uid", s.next_uid)
  put("winner", s.winner); put("end_reason", s.end_reason)
  local hidden = {}
  for t in pairs(s.hidden) do hidden[#hidden + 1] = t end
  table.sort(hidden)
  put("hidden", table.concat(hidden, "|"))
  for _, c in ipairs(s.champs) do
    local p = "champ " .. c.uid .. "."
    put(p .. "alive", c.alive); put(p .. "hp", c.hp); put(p .. "track", c.track)
    put(p .. "shield", c.shield)
    if c.alive then put(p .. "hex", c.hex[1] .. "," .. c.hex[2]) end
  end
  for _, w in ipairs(s.waves) do
    local p = "wave " .. w.uid .. "."
    put(p .. "team", w.team); put(p .. "lane", w.lane); put(p .. "chips", w.chips)
    put(p .. "path_idx", w.path_idx); put(p .. "hex", w.hex[1] .. "," .. w.hex[2])
    put(p .. "empowered", w.empowered)
  end
  for _, x in ipairs(s.structures) do
    put("struct " .. x.uid .. ".chips", x.chips); put("struct " .. x.uid .. ".alive", x.alive)
  end
  for _, m in ipairs(s.monsters) do
    local p = "monster " .. m.uid .. "."
    put(p .. "alive", m.alive); put(p .. "chips", m.chips); put(p .. "respawn_round", m.respawn_round)
  end
  for _, team in ipairs({"north", "south"}) do
    local t = s.teams[team]
    local p = "team " .. team .. "."
    put(p .. "ap", t.ap); put(p .. "kills", t.kills); put(p .. "towers_lost", t.towers_lost)
    put(p .. "baron", t.baron); put(p .. "dragons", t.dragons)
    put(p .. "dragon_track", table.concat(t.dragon_track, ","))
    local names = {}
    for k, n in pairs(t.cards) do if n > 0 then names[#names + 1] = k .. "x" .. n end end
    table.sort(names)
    put(p .. "cards", table.concat(names, ","))
  end
  return out
end

local function diff(a, b)
  local set, out = {}, {}
  for _, l in ipairs(b) do set[l] = true end
  local seen = {}
  for _, l in ipairs(a) do seen[l] = true; if not set[l] then out[#out + 1] = "  lua:    " .. l end end
  for _, l in ipairs(b) do if not seen[l] then out[#out + 1] = "  engine: " .. l end end
  return out
end

local pass, fail, by_step = 0, 0, {upkeep = {0, 0}, world = {0, 0}}
for i, sc in ipairs(file.scenarios) do
  local s = prepare(sc.before)
  if sc.step == "upkeep" then core:upkeep(s) else core:world(s) end
  local d = diff(flat(s), flat(prepare(sc.after)))
  local tally = by_step[sc.step]
  if #d == 0 then
    pass = pass + 1; tally[1] = tally[1] + 1
  else
    fail = fail + 1; tally[2] = tally[2] + 1
    if fail <= 5 then
      print(string.format("MISMATCH scenario %d (%s, round %d -> %s):", i, sc.step,
        sc.before.round, tostring(sc.after.round)))
      for j = 1, math.min(#d, 12) do print(d[j]) end
    end
  end
end
print(string.format("parity: %d scenarios, %d match, %d differ  (upkeep %d/%d, world %d/%d)",
  pass + fail, pass, fail, by_step.upkeep[1], by_step.upkeep[1] + by_step.upkeep[2],
  by_step.world[1], by_step.world[1] + by_step.world[2]))
os.exit(fail == 0 and 0 or 1)
