--[[ Hex-Nexus Global script: table layout, panel and the referee.

Above this line: the generated tables (VERSION, CONFIG, MAP, ROSTER, ITEMS,
ROUNDS, LAYOUT, DASH, ...) from tools/tts_export.py, then the rules core
(tts/lua/core.lua) as `Core`. This file holds no game numbers of its own.

  * calibration: fit every generated object to the size it was drawn for and
    put it where it belongs;
  * the panel: versions, round, phase, priority, whose activation, AP;
  * the referee: Start game, then Next phase runs Upkeep and the World Phase
    through the core (the same rules as the Python engine, checked by
    tts/tests/run.lua) and writes the result back onto the table;
  * table events: HP clicks bank AP and handle kills, tower falls and
    monster rewards; card menus use abilities, play buffs, buy items;
  * hotkeys: flip the hexgroup under the cursor, map camera.
]]

local TEAMS = {"north", "south"}
local S = {round = 0, phase = 1, calibrated = false, flip = 0, panel = true, act = 1,
           started = false, priority = FIRST_PLAYER, next_uid = 1, picks = {north = {}, south = {}},
           teams = {}}

-- ------------------------------------------------------------------ utils
local function allObjects()
  if getObjects then return getObjects() end
  return getAllObjects()
end

local function tagOf(o)
  local ok, t = pcall(function() return o.getGMNotes() end)
  if ok and t then return t end
  return ""
end

local function findTag(tag)
  for _, o in ipairs(allObjects()) do
    if tagOf(o) == tag then return o end
  end
  return nil
end

local function other(team) if team == "north" then return "south" end return "north" end

local function seat(team) return SEATS[team] or team end

-- The designer fixed round 1 priority (FIRST_PLAYER); it alternates after.
local function priorityTeam()
  return S.priority or FIRST_PLAYER
end

-- ------------------------------------------------------------ calibration
-- Scale an object so its measured footprint matches the exporter's w x d,
-- then move it so its bounds (not its pivot) are centred on the target.
-- Height: objects that sit on another generated object (tiles on the mat,
-- pieces on the tiles) are stacked on its measured top surface, because TTS
-- decides how thick a custom tile or token really is.
function targetY(o, spec)
  if not spec.on then return spec.y end
  local base = findTag(spec.on)
  if not base then return spec.y end
  local bb = base.getBounds()
  local top = bb.center.y + bb.size.y / 2
  return top + o.getBounds().size.y / 2 + (spec.lift or 0.01)
end

local function fitObject(o, spec, place)
  if not o or not spec then return end
  if spec.w and spec.w > 0 then
    local b = o.getBoundsNormalized()
    local s = o.getScale()
    if b and b.size and b.size.x > 0.001 then
      local fx = spec.w / b.size.x
      local fz = fx
      if spec.d and spec.d > 0 and b.size.z > 0.001 then fz = spec.d / b.size.z end
      if math.abs(fx - 1) > 0.01 or math.abs(fz - 1) > 0.01 then
        o.setScale({s.x * fx, s.y, s.z * fz})
      end
    end
  end
  if place then
    local y = targetY(o, spec)
    o.setRotation({0, (spec.rot or 0) + (S.flip or 0), 0})
    o.setPosition({spec.x, y, spec.z})
    if spec.art then
      -- re-centre on the bounds once TTS has applied the new scale
      Wait.frames(function()
        if o == nil or o.isDestroyed and o.isDestroyed() then return end
        local c = o.getBounds().center
        local p = o.getPosition()
        local dx, dz = c.x - spec.x, c.z - spec.z
        if math.abs(dx) > 0.02 or math.abs(dz) > 0.02 then
          o.setPosition({p.x - dx, y, p.z - dz})
        end
      end, 3)
    end
    if spec.lock then o.setLock(true) end
  end
  local t = tagOf(o)
  if t:find("^hn:struct") or t:find("^hn:monster") or t:find("^hn:champ") or t:find("^hn:ap:")
      or t:find("^hn:wave:") then
    pcall(function() o.call("draw") end)       -- counter buttons follow the new scale
  end
end

local function loadingDone()
  for _, o in ipairs(allObjects()) do
    if o.loading_custom then return false end
  end
  return true
end

-- Pass `level` places the objects stacked `level` deep: 0 = on the table
-- (mat, dashboards, tracker), 1 = on the mat (tiles), 2 = on a tile (pieces).
-- Each level waits a few frames so the one below has its final size.
local function calibrateLevel(placeAll, level, n)
  for _, o in ipairs(allObjects()) do
    local spec = LAYOUT[tagOf(o)]
    if spec and (spec.level or 0) == level then
      fitObject(o, spec, placeAll and spec.start)
      n = n + 1
    end
  end
  if level < 2 then
    Wait.frames(function() calibrateLevel(placeAll, level + 1, n) end, 5)
    return
  end
  S.calibrated = true
  refreshUI()
  broadcastToAll("Hex-Nexus: laid out " .. n .. " objects.", {0.85, 0.77, 0.6})
end

local function doCalibrate(placeAll)
  calibrateLevel(placeAll, 0, 0)
end

function calibrate(placeAll)
  Wait.condition(function() doCalibrate(placeAll) end, loadingDone, 30,
    function() doCalibrate(placeAll) end)
end

-- Chips, standees and cards leave their bags at TTS's default size.
function onObjectLeaveContainer(_, o)
  local spec = LAYOUT[tagOf(o)]
  if spec and spec.w and spec.w > 0 then
    Wait.condition(function()
      if o and not o.isDestroyed() and (o.getQuantity() or -1) < 2 then fitObject(o, spec, false) end
    end, function() return o == nil or o.isDestroyed() or not o.loading_custom end, 10)
  end
end

-- Hexgroup flip: swap the tile's state and fit the new face.
function hnFlipTile(p)
  local o = getObjectFromGUID(p.guid)
  if not o then return end
  local id = o.getStateId()
  local n = o.setState(id == 1 and 2 or 1)
  if n then
    Wait.frames(function()
      local spec = LAYOUT[tagOf(n)]
      if spec then fitObject(n, spec, true) end
    end, 2)
  end
end

-- ------------------------------------------------------------------ helpers
local CORE = Core.new(MAP, CONFIG, {kill_includes_baron = true, monster_heal = true})
local HEX_SIZE = HEX
local ACTION, WORLD, SHOP, WINCHECK, UPKEEP = 2, 3, 4, 5, 1

local function tagged(prefix)
  local out = {}
  for _, o in ipairs(allObjects()) do
    if tagOf(o):sub(1, #prefix) == prefix then out[#out + 1] = o end
  end
  return out
end

local function get(o) return o and o.call("hnGet") or nil end

local function seatTeam(colour)
  if colour == SEATS.north then return "north" end
  if colour == SEATS.south then return "south" end
  return nil
end

-- Who a click helps: the clicker's team when they sit Blue or Red, otherwise
-- (hot-seat, spectators) whoever's activation it is.
local function actingTeam(colour)
  local t = seatTeam(colour)
  if t then return t end
  if S.phase == ACTION and SNAKE[S.act] == 2 then return other(priorityTeam()) end
  return priorityTeam()
end

local function apObj(team) return findTag("hn:ap:" .. team) end
local function getAP(team) local o = apObj(team); return o and o.call("hnGet") or 0 end
local function setAP(team, n) local o = apObj(team); if o then o.call("hnSet", n) end end
local function addAP(team, n) if team and n ~= 0 then setAP(team, getAP(team) + n) end end

local function teamState(team)
  S.teams[team] = S.teams[team] or {kills = 0, towers_lost = 0, baron = false, dragons = 0}
  return S.teams[team]
end

local function tileObj(name)
  return findTag("hn:tile:" .. name .. ":hidden") or findTag("hn:tile:" .. name .. ":visible")
end

-- Top surface height at a hex (its tile), so pieces are put down, not into.
local function surfaceY(hex)
  local t = tileObj(CORE:tile(hex))
  if t then local b = t.getBounds(); return b.center.y + b.size.y / 2 end
  return 1.3
end

local function moveToHex(o, hex)
  if not o then return end
  local x, z = Core.hexToWorld(hex, HEX_SIZE)
  o.setPositionSmooth({x, surfaceY(hex) + 0.4, z}, false, true)
end

local function dashY(team)
  local d = findTag("hn:art:dash:" .. team)
  if d then local b = d.getBounds(); return b.center.y + b.size.y / 2 end
  return 1.3
end

local function structureHex(team, key)
  if key == "nexus" then return MAP[team].nexus end
  return MAP[team].towers[key]
end

-- ---------------------------------------------------- table -> core state
local function readState()
  local s = {round = S.round, priority = priorityTeam(), next_uid = S.next_uid,
             winner = S.winner, end_reason = S.end_reason, hidden = {}, wards = {},
             champs = {}, waves = {}, structures = {}, monsters = {}, teams = {}}
  for _, o in ipairs(tagged("hn:tile:")) do
    local name, side = tagOf(o):match("^hn:tile:(.+):(%a+)$")
    if name and side == "hidden" then s.hidden[name] = true end
  end
  for _, team in ipairs(TEAMS) do
    for _, cid in ipairs(S.picks[team] or {}) do
      local so = findTag("hn:champ:" .. team .. ":" .. cid)
      local co = findTag("hn:card:champ:" .. team .. ":" .. cid)
      local cs, card = get(so) or {hp = 0, max = 1}, get(co) or {track = 0}
      local hex
      if so then local p = so.getPosition(); hex = CORE:worldToHex(p.x, p.z, HEX_SIZE) end
      local alive = so ~= nil and cs.hp > 0 and hex ~= nil and not card.dead
      s.champs[#s.champs + 1] = {
        uid = team .. ":" .. cid, cid = cid, team = team, hp = cs.hp, max_hp = cs.max,
        hex = hex or {CORE.fountain[team][1], CORE.fountain[team][2]}, alive = alive,
        track = card.track or 0, shield = 0, shield_until = 0, items = {},
        _obj = so, _card = co, _wasAlive = alive, _hexKey = hex and Core.key(hex) or "",
      }
    end
  end
  for _, o in ipairs(tagged("hn:wave:")) do
    local w = get(o)
    if w and w.uid then
      local path = CORE.paths[w.team][w.lane]
      local h = path[(w.path_idx or 0) + 1]
      s.waves[#s.waves + 1] = {uid = w.uid, team = w.team, lane = w.lane, chips = w.hp,
                               path_idx = w.path_idx or 0, hex = {h[1], h[2]},
                               empowered = w.empowered == true, _obj = o}
    end
  end
  table.sort(s.waves, function(a, b)
    return tonumber(a.uid:sub(2)) < tonumber(b.uid:sub(2))
  end)
  for _, o in ipairs(tagged("hn:struct:")) do
    local x = get(o)
    local team, key = tagOf(o):match("^hn:struct:(%a+):(.+)$")
    local h = structureHex(team, key)
    s.structures[#s.structures + 1] = {uid = x.uid, team = team, stype = x.stype, lane = x.lane,
                                       tier = x.tier, chips = x.hp, hex = {h[1], h[2]},
                                       alive = x.hp > 0, _obj = o}
  end
  table.sort(s.structures, function(a, b) return a.uid < b.uid end)
  for _, o in ipairs(tagged("hn:monster:")) do
    local m = get(o)
    local mtype, i = tagOf(o):match("^hn:monster:(.+):(%d+)$")
    local h = MAP.monsters[mtype][tonumber(i) + 1]
    s.monsters[#s.monsters + 1] = {uid = m.uid, mtype = mtype, chips = m.hp, max_chips = m.max,
                                   hex = {h[1], h[2]}, alive = m.hp > 0,
                                   respawn_round = m.respawn_round or 0, _obj = o}
  end
  for _, team in ipairs(TEAMS) do
    local ts = teamState(team)
    s.teams[team] = {ap = getAP(team), kills = ts.kills, towers_lost = ts.towers_lost,
                     baron = ts.baron, dragons = ts.dragons, dragon_track = {}, cards = {}}
  end
  return s
end

-- For tests and debugging: the table as the core sees it.
function hnDebugState() return readState() end

-- ---------------------------------------------------- core state -> table
local function handSpot(team)
  local d = DASH[team]
  S.hand = S.hand or {north = 0, south = 0}
  local i = S.hand[team] % 4
  S.hand[team] = S.hand[team] + 1
  local dx = (i - 1.5) * 1.35 * (d.rot == 0 and -1 or 1)
  return {d.hand.x + dx, dashY(team) + 0.5, d.hand.z}
end

local function dealCard(kind, team)
  local deck = findTag("hn:deck:buff:" .. kind)
  if not deck then
    broadcastToAll(seat(team) .. " takes a " .. kind .. " card (supply is out: take one by hand).",
      {1, 0.8, 0.4})
    return
  end
  deck.takeObject({position = handSpot(team), rotation = {0, DASH[team].rot, 0}, smooth = true,
                   callback_function = function(c) c.call("hnSet", {team = team}) end})
end

local function spawnWave(w)
  local tpl = WAVE_TEMPLATE[w.team][w.lane]
  local data = {}
  for k, v in pairs(tpl) do data[k] = v end
  data.GMNotes = "hn:wave:" .. w.uid
  data.LuaScriptState = JSON.encode({kind = "wave", label = SEATS[w.team] .. " " .. w.lane .. " wave",
                                     team = w.team, lane = w.lane, uid = w.uid, hp = w.chips,
                                     max = w.chips, path_idx = w.path_idx,
                                     empowered = w.empowered})
  local x, z = Core.hexToWorld(w.hex, HEX_SIZE)
  spawnObjectData({data = data, position = {x, surfaceY(w.hex) + 0.6, z},
                   rotation = {0, ART_ROT_Y, 0},
                   callback_function = function(o)
                     Wait.condition(function()
                       fitObject(o, {w = SIZES.wave, d = SIZES.wave}, false)
                     end, function() return o.isDestroyed() or not o.loading_custom end, 10)
                   end})
end

local function writeState(s, events)
  S.round, S.priority, S.next_uid = s.round, s.priority, s.next_uid
  S.winner, S.end_reason = s.winner, s.end_reason
  for _, team in ipairs(TEAMS) do
    local ts, t = teamState(team), s.teams[team]
    ts.kills, ts.towers_lost, ts.baron, ts.dragons = t.kills, t.towers_lost, t.baron, t.dragons
    setAP(team, t.ap)
  end
  for _, o in ipairs(tagged("hn:tile:")) do
    local name, side = tagOf(o):match("^hn:tile:(.+):(%a+)$")
    if name and (side == "hidden") ~= (s.hidden[name] == true) then
      hnFlipTile({guid = o.getGUID()})
    end
  end
  for _, c in ipairs(s.champs) do
    if c._card then c._card.call("hnSet", {track = c.track, dead = not c.alive}) end
    if c._obj then
      c._obj.call("hnSet", {hp = c.alive and c.hp or 0})
      if c.alive and (not c._wasAlive or Core.key(c.hex) ~= c._hexKey) then
        moveToHex(c._obj, c.hex)
      elseif not c.alive and c._wasAlive then
        local b = DASH[c.team].bench[ROSTER[c.cid].role]
        c._obj.setPositionSmooth({b.x, dashY(c.team) + 0.5, b.z}, false, true)
      end
    end
  end
  local keep = {}
  for _, w in ipairs(s.waves) do
    keep[w.uid] = true
    if w._obj then
      w._obj.call("hnSet", {hp = w.chips, path_idx = w.path_idx, empowered = w.empowered})
      moveToHex(w._obj, w.hex)
    else
      spawnWave(w)
    end
  end
  for _, o in ipairs(tagged("hn:wave:")) do
    local w = get(o)
    if w and w.uid and not keep[w.uid] then o.destruct() end
  end
  for _, x in ipairs(s.structures) do x._obj.call("hnSet", {hp = x.chips}) end
  for _, m in ipairs(s.monsters) do
    m._obj.call("hnSet", {hp = m.alive and m.chips or 0, respawn_round = m.respawn_round})
  end
  for _, e in ipairs(events or {}) do
    if e.t == "reward" then
      if e.mtype == "dragon" then
        if teamState(e.team).dragons <= (CONFIG.dragon_cap or 2) then dealCard("dragon", e.team) end
      else
        dealCard(e.mtype, e.team)
      end
    end
  end
end

local function summarise(title, events)
  local n = {}
  for _, e in ipairs(events) do n[e.t] = (n[e.t] or 0) + 1 end
  local bits = {}
  local names = {respawn = "respawned", heal = "healed at the fountain", decay = "structures decayed",
                 wave_spawn = "waves spawned", wave_move = "waves moved", wave_merge = "waves merged",
                 monster_spawn = "monsters up", monster_heal = "monsters healed", flip = "tiles flipped",
                 hit = "hits", kill = "champions killed", wave_down = "waves destroyed",
                 structure_down = "structures fell", monster_down = "monsters killed"}
  for k, label in pairs(names) do
    if n[k] then bits[#bits + 1] = n[k] .. " " .. label end
  end
  table.sort(bits)
  broadcastToAll(title .. (#bits > 0 and (": " .. table.concat(bits, ", ")) or ": nothing happened"),
    {0.85, 0.77, 0.6})
end

-- ---------------------------------------------------------------- phases
local function dragonCooldowns()
  for _, o in ipairs(tagged("hn:card:buff:dragon")) do
    local c = get(o)
    if c and c.track and c.track > 0 then o.call("hnSet", {track = c.track - 1}) end
  end
end

function doUpkeep()
  local s = readState()
  local events = CORE:upkeep(s)
  writeState(s, events)
  dragonCooldowns()
  S.phase, S.act = UPKEEP, 1
  summarise("Upkeep, round " .. S.round, events)
end

function doWorld()
  local s = readState()
  local events = CORE:world(s)
  writeState(s, events)
  summarise("World Phase", events)
end

local function announceWinner()
  if S.winner then
    broadcastToAll("GAME OVER: " .. seat(S.winner) .. " (" .. S.winner .. ") wins by "
      .. (S.end_reason or "?") .. " in round " .. S.round .. ".", {1, 0.9, 0.3})
  end
end

function doWinCheck()
  if S.winner then announceWinner(); return end
  if S.round >= CONFIG.round_limit then
    local w, why = CORE:tiebreak(readState())
    S.winner, S.end_reason = w, why
    if w then announceWinner()
    else broadcastToAll("GAME OVER: a draw at the round limit.", {1, 0.9, 0.3}); S.winner = "draw" end
  end
end

-- ------------------------------------------------------------ start game
local function basePlaces(team)
  local taken = {}
  local side = MAP[team]
  taken[Core.key(side.nexus)] = true
  for _, h in pairs(side.towers) do taken[Core.key(h)] = true end
  local out = {CORE.fountain[team]}
  for _, h in ipairs(CORE.tileHexes[CORE.baseTile[team]]) do
    if not taken[Core.key(h)] and Core.key(h) ~= Core.key(CORE.fountain[team]) then out[#out + 1] = h end
  end
  return out
end

local function takeFrom(container, tag, params)
  if not container then return false end
  for _, e in ipairs(container.getObjects()) do
    if e.gm_notes == tag then
      params.guid = e.guid
      container.takeObject(params)
      return true
    end
  end
  return false
end

local function nearXZ(o, p, r)
  local q = o.getPosition()
  return (q.x - p.x) ^ 2 + (q.z - p.z) ^ 2 <= r * r
end

function uiStartGame(player)
  if S.started then
    broadcastToAll("The game has started. Load a fresh copy of the save to start again.", {1, 0.6, 0.4})
    return
  end
  pcall(function() math.randomseed(os.time()) end)
  local picks, used = {north = {}, south = {}}, {}
  -- cards already put in a role slot are the draft; the rest is random
  for _, team in ipairs(TEAMS) do
    for _, o in ipairs(tagged("hn:card:champ:" .. team .. ":")) do
      local cid = tagOf(o):match(":([%w_]+)$")
      local role = ROSTER[cid] and ROSTER[cid].role
      if role and nearXZ(o, DASH[team].roles[role], 1.4) and not picks[team][role] then
        picks[team][role] = cid; used[cid] = true
      end
    end
  end
  for _, team in ipairs(TEAMS) do
    for _, role in ipairs(ROLES) do
      if not picks[team][role] then
        local pool = {}
        for cid, k in pairs(ROSTER) do
          if k.role == role and not used[cid] then pool[#pool + 1] = cid end
        end
        table.sort(pool)
        local cid = pool[math.random(#pool)]
        picks[team][role] = cid; used[cid] = true
      end
    end
  end
  for _, team in ipairs(TEAMS) do
    local d, rot, y = DASH[team], DASH[team].rot, dashY(team)
    local places = basePlaces(team)
    S.picks[team] = {}
    for i, role in ipairs(ROLES) do
      local cid = picks[team][role]
      S.picks[team][i] = cid
      local slot = d.roles[role]
      local ctag = "hn:card:champ:" .. team .. ":" .. cid
      local card = findTag(ctag)
      if card then
        card.setPositionSmooth({slot.x, y + 0.3, slot.z}, false, true)
        card.setRotation({0, rot, 0})
      else
        takeFrom(findTag("hn:deck:champ:" .. team), ctag,
          {position = {slot.x, y + 0.3, slot.z}, rotation = {0, rot, 0}, smooth = false})
      end
      local stag = "hn:champ:" .. team .. ":" .. cid
      local h = places[i] or places[1]
      local x, z = Core.hexToWorld(h, HEX_SIZE)
      local standee = findTag(stag)
      if standee then
        standee.setPositionSmooth({x, surfaceY(h) + 0.4, z}, false, true)
      else
        takeFrom(findTag("hn:bag:standees:" .. team), stag,
          {position = {x, surfaceY(h) + 0.6, z}, rotation = {0, rot, 0}, smooth = false})
      end
    end
    S.teams[team] = {kills = 0, towers_lost = 0, baron = false, dragons = 0}
  end
  S.started, S.round, S.priority, S.next_uid, S.winner = true, 0, FIRST_PLAYER, 1, nil
  broadcastToAll("Hex-Nexus: " .. seat("north") .. " " .. table.concat(S.picks.north, ", ")
    .. "  vs  " .. seat("south") .. " " .. table.concat(S.picks.south, ", "), {0.85, 0.77, 0.6})
  -- let the cards and standees land, then round 1's Upkeep
  Wait.time(function() doUpkeep(); moveMarkers(); refreshUI() end, 1.5)
end

-- ------------------------------------------------------------ table events
function hnCounterChanged(p)
  local o = getObjectFromGUID(p.guid)
  if not o then return end
  local st, tag = get(o), tagOf(o)
  local team = actingTeam(p.colour)
  local delta = p.after - p.before
  if not S.started then refreshUI(); return end
  if st.kind == "monster" or (st.kind == "wave" and team ~= st.team) then
    if delta < 0 then addAP(team, -delta) end             -- chips are AP (Rules 7)
  end
  if st.kind == "structure" and delta < 0 then
    local s = readState()
    for _, x in ipairs(s.structures) do
      if x.uid == st.uid then
        x.alive = true
        if not CORE:structureTargetable(s, x) then
          broadcastToAll("Careful: " .. (st.label or "that structure") .. " is protected "
            .. "(T1 before T2; a whole lane before the Nexus).", {1, 0.6, 0.4})
        end
      end
    end
  end
  if p.after == 0 and p.before > 0 then
    local s, events = readState(), {}
    if st.kind == "champion" then
      for _, c in ipairs(s.champs) do
        if c._obj == o then
          c._wasAlive = true
          CORE:killChampion(s, c, other(c.team), events)
          broadcastToAll(seat(c.team) .. " " .. ROSTER[c.cid].name .. " is down: " .. seat(other(c.team))
            .. " +" .. events[#events].ap .. " AP; back in " .. (c.track - 1) .. " rounds.", {1, 0.6, 0.4})
        end
      end
    elseif st.kind == "monster" then
      for _, m in ipairs(s.monsters) do
        if m._obj == o then
          m.alive, m.kind = true, "monster"
          CORE:destroy(s, m, team, events)
          broadcastToAll(seat(team) .. " takes the " .. st.label .. ".", {0.85, 0.77, 0.6})
        end
      end
    elseif st.kind == "structure" then
      for _, x in ipairs(s.structures) do
        if x._obj == o then
          x.alive, x.kind = true, "structure"
          CORE:destroy(s, x, team ~= x.team and team or nil, events)
          broadcastToAll(seat(x.team) .. " " .. st.label .. " falls.", {1, 0.6, 0.4})
        end
      end
    elseif st.kind == "wave" then
      for i, w in ipairs(s.waves) do
        if w._obj == o then table.remove(s.waves, i); break end
      end
    end
    writeState(s, events)
    if S.winner then announceWinner() end
  end
  refreshUI()
end

function hnUseAbility(p)
  local o = getObjectFromGUID(p.guid)
  local c = get(o)
  if not c then return end
  local a = c.ab[p.key]
  local who = seat(c.team) .. " " .. c.name
  if c.dead then broadcastToAll(who .. " is dead.", {1, 0.6, 0.4}); return end
  if c.track > 0 then broadcastToAll(who .. " is on cooldown (" .. c.track .. ").", {1, 0.6, 0.4}); return end
  if getAP(c.team) < a.cost then
    broadcastToAll(who .. ": " .. p.key .. " costs " .. a.cost .. " AP, the pool has " .. getAP(c.team) .. ".",
      {1, 0.6, 0.4})
    return
  end
  if S.phase ~= ACTION then broadcastToAll("(Not the Action Phase.)", {1, 0.8, 0.4}) end
  addAP(c.team, -a.cost)
  o.call("hnSet", {track = a.cd})
  broadcastToAll(who .. " uses " .. p.key .. " (" .. a.cost .. " AP): card out for " .. a.cd
    .. (a.cd == 1 and " round." or " rounds."), {0.85, 0.77, 0.6})
  refreshUI()
end

function hnPlayBuff(p)
  local o = getObjectFromGUID(p.guid)
  local c = get(o)
  if not c then return end
  local team = c.team or seatTeam(p.colour) or actingTeam(p.colour)
  if c.buff == "blue_buff" then
    local n = tonumber((ITEMS.buff.blue_buff.effect or ""):match("%+(%d+)%s*AP")) or 0
    addAP(team, n)
    broadcastToAll(seat(team) .. " plays Blue Buff: +" .. n .. " AP.", {0.85, 0.77, 0.6})
    o.destruct()
  elseif c.buff == "red_buff" then
    broadcastToAll(seat(team) .. " plays Red Buff: " .. ITEMS.buff.red_buff.effect
      .. " (click the target's HP).", {0.85, 0.77, 0.6})
    o.destruct()
  elseif c.buff == "dragon" then
    if (c.track or 0) > 0 then broadcastToAll("That Dragon card is on cooldown.", {1, 0.6, 0.4}); return end
    o.call("hnSet", {track = c.cd})
    broadcastToAll(seat(team) .. " plays a Dragon card: " .. (CONFIG.dragon_card and CONFIG.dragon_card.hits or 0)
      .. " hits on an adjacent unit (click its HP).", {0.85, 0.77, 0.6})
  else
    broadcastToAll("The Baron card is permanent: its waves are Empowered.", {0.85, 0.77, 0.6})
  end
  refreshUI()
end

function hnBuyItem(p)
  local o = getObjectFromGUID(p.guid)
  local c = get(o)
  if not c or c.bought then return end
  if S.phase ~= SHOP then broadcastToAll("(Items are bought in the Shop Phase.)", {1, 0.8, 0.4}) end
  if getAP(c.team) < c.cost then
    broadcastToAll(seat(c.team) .. " cannot afford " .. c.name .. " (" .. c.cost .. " AP).", {1, 0.6, 0.4})
    return
  end
  addAP(c.team, -c.cost)
  o.call("hnSet", {bought = true})
  broadcastToAll(seat(c.team) .. " buys " .. c.name .. " (" .. c.cost .. " AP).", {0.85, 0.77, 0.6})
  refreshUI()
end

function hnRefresh() refreshUI() end

-- ------------------------------------------------------------------- panel
function refreshUI()
  local row = ROUNDS[math.max(1, S.round)] or {}
  local phase = PHASES[S.phase] or "?"
  local p = priorityTeam()
  if not S.started then
    UI.setValue("hnRound", "Not started · press Start game")
  else
    UI.setValue("hnRound", "Round " .. S.round .. " / " .. CONFIG.round_limit .. "   ·   " .. phase)
  end
  local prio = "Priority (Player 1): " .. seat(p)
  if S.phase == ACTION and S.started then
    local who = SNAKE[S.act] == 1 and p or other(p)
    prio = prio .. "   ·   activation " .. S.act .. "/10: " .. seat(who)
  end
  if S.winner then prio = "GAME OVER: " .. (S.winner == "draw" and "draw" or (seat(S.winner) .. " wins")) end
  UI.setValue("hnPrio", prio)
  local bits = {}
  if row.spawn then bits[#bits + 1] = "waves spawn +" .. row.wave_size
  else bits[#bits + 1] = "no wave spawn" end
  if row.decays then
    bits[#bits + 1] = "decay -" .. CONFIG.structure_decay .. " (floors T" .. FLOORS.tower
      .. " / N" .. FLOORS.nexus .. ")"
  end
  bits[#bits + 1] = "kill = " .. row.kill_ap .. " AP (" .. row.kill_ap_baron .. " with Baron)"
  bits[#bits + 1] = "death: out " .. (row.death_pos - 1) .. " rnd"
  if row.monsters and row.monsters ~= "" then bits[#bits + 1] = "spawns: " .. row.monsters end
  UI.setValue("hnInfo", table.concat(bits, "   ·   "))
  local hint
  if not S.started then
    hint = "Put champion cards in your role slots to draft, or leave them empty: Start game fills the rest at random."
  elseif phase == "Upkeep" then
    hint = "Upkeep done automatically. Next phase ▶ starts the Action Phase."
  elseif phase == "Action" then
    hint = "Right-click a card to use an ability; click HP to hit. Next activation ▶ when done."
  elseif phase == "World" then
    hint = "World Phase resolved automatically. Next phase ▶ for the Shop."
  elseif phase == "Shop" then
    hint = "Player 1 then Player 2: right-click an item card → Buy."
  else
    hint = "Next phase ▶ starts the next round (its Upkeep runs automatically)."
  end
  UI.setValue("hnHint", hint)
  UI.setValue("hnAP", "AP:  " .. seat("north") .. " " .. getAP("north") .. "   ·   "
    .. seat("south") .. " " .. getAP("south"))
  UI.setAttribute("hnBody", "active", S.panel and "true" or "false")
end

function moveMarkers()
  local m = findTag("hn:marker:round")
  local slot = ROUND_SLOTS[math.max(1, S.round)]
  if m and slot then m.setPositionSmooth({slot.x, 2.2, slot.z}, false, true) end
  local pm = findTag("hn:marker:priority")
  local ps = PRIO_SLOTS[priorityTeam()]
  if pm and ps then pm.setPositionSmooth({ps.x, 2.2, ps.z}, false, true) end
end

function uiNextPhase()
  if S.winner then announceWinner(); return end
  if not S.started then broadcastToAll("Press Start game first.", {1, 0.8, 0.4}); return end
  if S.phase == UPKEEP then S.phase, S.act = ACTION, 1
  elseif S.phase == ACTION then S.phase = WORLD; doWorld()
  elseif S.phase == WORLD then S.phase = SHOP
  elseif S.phase == SHOP then S.phase = WINCHECK; doWinCheck()
  else doUpkeep() end
  moveMarkers()
  refreshUI()
end

function uiNextActivation()
  if S.phase ~= ACTION then return end
  if S.act < #SNAKE then S.act = S.act + 1 end
  refreshUI()
end

function uiRelayout(player)
  if player and not player.admin then
    broadcastToColor("Only the host or a promoted player can re-lay out the table.", player.color, {1, 0.5, 0.5})
    return
  end
  calibrate(true)
end

function uiFlipArt(player)
  if player and not player.admin then return end
  S.flip = ((S.flip or 0) + 180) % 360
  calibrate(true)
end

function uiTogglePanel()
  S.panel = not S.panel
  refreshUI()
end

-- ----------------------------------------------------------- camera / keys
local function mapView(colour)
  local pl = Player[colour]
  if not pl then return end
  local yaw = (colour == SEATS.north) and 180 or 0
  pl.lookAt({position = {x = 0, y = 1, z = 0}, pitch = 90, yaw = yaw, distance = 34})
end

function uiMapView(player) if player then mapView(player.color) end end

local function flipUnder(colour, hovered, pointer)
  local o = hovered
  if o and tagOf(o):find("^hn:tile:") then hnFlipTile({guid = o.getGUID()}); return end
  local p = (o and o.getPosition()) or pointer
  if not p then return end
  local h = CORE:worldToHex(p.x, p.z, HEX_SIZE)
  local t = h and tileObj(CORE:tile(h))
  if t then hnFlipTile({guid = t.getGUID()}) end
end

-- ---------------------------------------------------------------- lifecycle
function onSave()
  return JSON.encode(S)
end

function onLoad(saved)
  if saved and saved ~= "" then
    local ok, t = pcall(JSON.decode, saved)
    if ok and type(t) == "table" then for k, v in pairs(t) do S[k] = v end end
  end
  if addHotkey then
    addHotkey("Hex-Nexus: flip hexgroup", function(colour, hovered, pointer) flipUnder(colour, hovered, pointer) end)
    addHotkey("Hex-Nexus: map view", function(colour) mapView(colour) end)
  end
  Wait.frames(refreshUI, 5)
  Wait.time(refreshUI, 2, -1)
  if not S.calibrated then
    Wait.time(function() calibrate(true) end, 1)
  end
end
