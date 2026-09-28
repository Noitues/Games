--[[ Hex-Nexus Global script (milestone M0: static mod).

The generated tables above this line (VERSION, CONFIG, MAP, ROSTER, ITEMS,
ROUNDS, LAYOUT, ...) come from tools/tts_export.py. This file holds no game
numbers of its own.

M0 duties:
  * calibration: fit every generated object to the size it was drawn for and
    put it where it belongs (TTS decides how big a custom image is; the
    exporter decides how big it should be);
  * the always-visible panel: versions, round, phase, priority, the round's
    wave / decay / kill / death numbers, and each team's AP pool count;
  * hexgroup flips (tile context menu).
The rules themselves are played by hand in M0; the referee arrives in M1.
]]

local TEAMS = {"north", "south"}
local S = {round = 1, phase = 1, calibrated = false, flip = 0, panel = true}

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
  if S.round % 2 == 1 then return FIRST_PLAYER end
  return other(FIRST_PLAYER)
end

-- ------------------------------------------------------------ calibration
-- Scale an object so its measured footprint matches the exporter's w x d,
-- then move it so its bounds (not its pivot) are centred on the target.
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
    o.setRotation({0, (spec.rot or 0) + (S.flip or 0), 0})
    o.setPosition({spec.x, spec.y, spec.z})
    if spec.art then
      -- re-centre on the bounds once TTS has applied the new scale
      Wait.frames(function()
        if o == nil or o.isDestroyed and o.isDestroyed() then return end
        local c = o.getBounds().center
        local p = o.getPosition()
        local dx, dz = c.x - spec.x, c.z - spec.z
        if math.abs(dx) > 0.02 or math.abs(dz) > 0.02 then
          o.setPosition({p.x - dx, spec.y, p.z - dz})
        end
      end, 3)
    end
    if spec.lock then o.setLock(true) end
  end
  local t = tagOf(o)
  if t:find("^hn:struct") or t:find("^hn:monster") or t:find("^hn:champ") then
    pcall(function() o.call("draw") end)       -- counter buttons follow the new scale
  end
end

local function loadingDone()
  for _, o in ipairs(allObjects()) do
    if o.loading_custom then return false end
  end
  return true
end

local function doCalibrate(placeAll)
  local n = 0
  for _, o in ipairs(allObjects()) do
    local spec = LAYOUT[tagOf(o)]
    if spec then
      fitObject(o, spec, placeAll and spec.start)
      n = n + 1
    end
  end
  S.calibrated = true
  refreshUI()
  broadcastToAll("Hex-Nexus: laid out " .. n .. " objects.", {0.85, 0.77, 0.6})
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

-- -------------------------------------------------------------- pool count
local function chipCount(o)
  local tag = tagOf(o)
  local nick = (o.getName and o.getName() or ""):lower()
  if tag:sub(1, 7) ~= "hn:chip" and not nick:find("chip") then return 0 end
  if o.getLock() then return 0 end
  local q = o.getQuantity() or -1
  if q < 1 then q = 1 end
  return q
end

local AP = {north = 0, south = 0}

function countPools()
  for _, team in ipairs(TEAMS) do
    local z = findTag("hn:zone:pool:" .. team)
    local n = 0
    if z then
      for _, o in ipairs(z.getObjects()) do n = n + chipCount(o) end
    end
    AP[team] = n
  end
  UI.setValue("hnAP", "AP pool:  " .. seat("north") .. " " .. AP.north .. "   ·   "
    .. seat("south") .. " " .. AP.south)
end

-- ------------------------------------------------------------------- panel
function refreshUI()
  local row = ROUNDS[S.round] or {}
  local phase = PHASES[S.phase] or "?"
  UI.setValue("hnRound", "Round " .. S.round .. " / " .. CONFIG.round_limit .. "   ·   " .. phase)
  local p = priorityTeam()
  UI.setValue("hnPrio", "Priority (Player 1): " .. seat(p) .. " (" .. p .. ")")
  local bits = {}
  if row.spawn then bits[#bits + 1] = "waves spawn +" .. row.wave_size
  else bits[#bits + 1] = "no wave spawn" end
  if row.decays then
    bits[#bits + 1] = "decay -" .. CONFIG.structure_decay .. " (floors T" .. FLOORS.tower
      .. " / N" .. FLOORS.nexus .. ")"
  end
  bits[#bits + 1] = "kill = " .. row.kill_ap .. " AP (" .. row.kill_ap_baron .. " with Baron)"
  bits[#bits + 1] = "death → track " .. row.death_pos .. " (" .. (row.death_pos - 1) .. " rnd)"
  if row.monsters and row.monsters ~= "" then bits[#bits + 1] = "spawns: " .. row.monsters end
  UI.setValue("hnInfo", table.concat(bits, "   ·   "))
  local hint = ""
  if phase == "Action" then
    hint = "Snake: 1 2 2 1 1 2 2 1 1 2   (1 = " .. seat(p) .. ")"
  elseif phase == "Upkeep" then
    hint = "Round tracker → cooldown tracks -1 → fountain heal → decay → AP "
      .. CONFIG.ap_base .. " → waves move → spawn → monsters → flip-back"
  elseif phase == "World" then
    hint = "Waves 1 hit; towers " .. CONFIG.tower_hits_champion .. " on champions, "
      .. CONFIG.tower_hits_wave .. " on waves; monsters " .. CONFIG.monster_hits
  elseif phase == "Shop" then
    hint = "Player 1 then Player 2 spend leftover AP on items"
  else
    hint = "Nexus at 0? Otherwise next round. Round " .. CONFIG.round_limit .. " tiebreak: towers, structure HP, kills"
  end
  UI.setValue("hnHint", hint)
  UI.setAttribute("hnBody", "active", S.panel and "true" or "false")
end

local function moveMarkers()
  local m = findTag("hn:marker:round")
  local slot = ROUND_SLOTS[S.round]
  if m and slot then m.setPositionSmooth({slot.x, 2.2, slot.z}, false, true) end
  local pm = findTag("hn:marker:priority")
  local ps = PRIO_SLOTS[priorityTeam()]
  if pm and ps then pm.setPositionSmooth({ps.x, 2.2, ps.z}, false, true) end
end

function uiNextPhase()
  S.phase = S.phase + 1
  if S.phase > #PHASES then
    if S.round < CONFIG.round_limit then S.round = S.round + 1 end
    S.phase = 1
    moveMarkers()
  end
  refreshUI()
end

function uiNextRound()
  if S.round < CONFIG.round_limit then S.round = S.round + 1 end
  S.phase = 1
  moveMarkers()
  refreshUI()
end

function uiPrevRound()
  if S.round > 1 then S.round = S.round - 1 end
  S.phase = 1
  moveMarkers()
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

-- ---------------------------------------------------------------- lifecycle
function onSave()
  return JSON.encode(S)
end

function onLoad(saved)
  if saved and saved ~= "" then
    local ok, t = pcall(JSON.decode, saved)
    if ok and type(t) == "table" then for k, v in pairs(t) do S[k] = v end end
  end
  Wait.frames(refreshUI, 5)
  Wait.time(countPools, 1, -1)
  if not S.calibrated then
    Wait.time(function() calibrate(true) end, 1)
  end
end
