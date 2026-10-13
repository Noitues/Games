--[[ Hex-Nexus rules core: pure Lua 5.2, no Tabletop Simulator calls.

A port of the engine's round bookkeeping, so the table runs the same rules the
simulations were balanced on:

  Core.upkeep(state)   engine.game.upkeep (steps 1-8), with abilities.respawn,
                       move_waves, spawn_waves, decay_structures
  Core.world(state)    engine.game.world_phase, then the flip checkpoint
  Core.refresh(state)  engine.state.refresh_visibility / place_units_on_flip
  Core.killChampion    engine.resolve.kill_champion (+ the designer's Baron rule)
  Core.tiebreak(state) engine.run.Game._tiebreak

The Global script reads the table into a `state` table, calls these, and
writes the result back. tts/tests/run.lua replays engine scenarios through the
same functions (the parity harness), so a rules difference shows up there,
not at the table.

State shape (every list keeps the engine's order; hexes are {q, r}):
  round, priority ("north"|"south"), next_uid, winner, end_reason
  hidden    = {[tile name] = true}       hidden hexgroups
  wards     = {[tile name] = round}      Control Wards
  champs    = {{uid, cid, team, hp, max_hp, hex, alive, track, shield,
                shield_until, items = {name = true}}}
  waves     = {{uid, team, lane, chips, path_idx (0-based), hex, empowered}}
  structures= {{uid, team, stype, lane, tier, chips, hex, alive}}
  monsters  = {{uid, mtype, chips, max_chips, hex, alive, respawn_round}}
  teams     = {north = {ap, kills, towers_lost, baron, dragons,
                         dragon_track = {..}, cards = {name = n}}, south = ..}

Options (designer rulings that the engine does not have yet):
  kill_includes_baron  a kill by a Baron holder pays two Empowered waves
  monster_heal         a monster that survives a round is back to full HP
]]

local Core = {}
Core.__index = Core

local TEAMS = {"north", "south"}
local DIRS = {{1, 0}, {1, -1}, {0, -1}, {-1, 0}, {-1, 1}, {0, 1}}
local DEATH_BANDS = {{4, 2}, {8, 3}, {math.huge, 4}}       -- engine.resolve.DEATH_BANDS

local function key(h) return h[1] .. "," .. h[2] end
local function other(team) if team == "north" then return "south" end return "north" end
Core.other = other
Core.key = key

local function hexDistance(a, b)
  local dq, dr = a[1] - b[1], a[2] - b[2]
  return math.max(math.abs(dq), math.abs(dr), math.abs(-dq - dr))
end
Core.hexDistance = hexDistance

local function sortHexes(list)
  table.sort(list, function(a, b)
    if a[1] ~= b[1] then return a[1] < b[1] end
    return a[2] < b[2]
  end)
  return list
end

-- Stable sort (Python's sorted is stable; table.sort is not).
local function stableSort(list, less)
  local idx = {}
  for i, v in ipairs(list) do idx[v] = i end
  table.sort(list, function(a, b)
    if less(a, b) then return true end
    if less(b, a) then return false end
    return idx[a] < idx[b]
  end)
  return list
end

-- ------------------------------------------------------------------- board
function Core.new(map, config, opts)
  local self = setmetatable({map = map, cfg = config, opts = opts or {}}, Core)
  self.tileNames, self.tileOf, self.tileHexes, self.onBoard = {}, {}, {}, {}
  for name in pairs(map.hexgroups) do self.tileNames[#self.tileNames + 1] = name end
  table.sort(self.tileNames)
  for _, name in ipairs(self.tileNames) do
    local hs = {}
    for _, h in ipairs(map.hexgroups[name]) do
      hs[#hs + 1] = {h[1], h[2]}
      self.tileOf[key(h)] = name
      self.onBoard[key(h)] = true
    end
    self.tileHexes[name] = sortHexes(hs)
  end
  self.lanes = map.lane_order or {"top", "mid", "bot"}
  self.fountain, self.paths, self.baseTile = {}, {}, {}
  for _, team in ipairs(TEAMS) do
    local side = map[team]
    self.fountain[team] = {side.fountain[1], side.fountain[2]}
    self.baseTile[team] = self.tileOf[key(side.fountain)]
    self.paths[team] = {}
    for _, lane in ipairs(self.lanes) do
      local p = {}
      for _, h in ipairs(side.lane_paths[lane]) do p[#p + 1] = {h[1], h[2]} end
      self.paths[team][lane] = p
    end
  end
  return self
end

function Core:neighbors(h)
  local out = {}
  for _, d in ipairs(DIRS) do
    local n = {h[1] + d[1], h[2] + d[2]}
    if self.onBoard[key(n)] then out[#out + 1] = n end
  end
  return out
end

function Core:tile(h) return self.tileOf[key(h)] end

-- World (x, z) <-> hex, for the table adapter. North (negative r) is +Z.
function Core.hexToWorld(h, size)
  local q, r = h[1], h[2]
  return 1.5 * size * q, -math.sqrt(3) * size * (r + q / 2)
end

function Core:worldToHex(x, z, size)
  local q = x / (1.5 * size)
  local r = -z / (math.sqrt(3) * size) - q / 2
  -- cube rounding
  local cx, cz = q, r
  local cy = -cx - cz
  local rx, ry, rz = math.floor(cx + 0.5), math.floor(cy + 0.5), math.floor(cz + 0.5)
  local dx, dy, dz = math.abs(rx - cx), math.abs(ry - cy), math.abs(rz - cz)
  if dx > dy and dx > dz then rx = -ry - rz
  elseif dy > dz then ry = -rx - rz
  else rz = -rx - ry end
  local h = {rx + 0, rz + 0}          -- + 0 turns a rounded -0 into 0 for the key
  if self.onBoard[key(h)] then return h end
  return nil
end

-- ------------------------------------------------------------------- units
function Core:allUnits(s)
  local out = {}
  for _, c in ipairs(s.champs) do c.kind = "champion"; out[#out + 1] = c end
  for _, w in ipairs(s.waves) do w.kind = "wave"; w.alive = true; out[#out + 1] = w end
  for _, x in ipairs(s.structures) do x.kind = "structure"; out[#out + 1] = x end
  for _, m in ipairs(s.monsters) do m.kind = "monster"; out[#out + 1] = m end
  return out
end

local function isHidden(s, tile) return s.hidden[tile] == true end

function Core:nodeOf(s, h)
  local t = self:tile(h)
  if isHidden(s, t) then return "T:" .. t end
  return "H:" .. key(h)
end

function Core:unitsAtNode(s, node)
  local out = {}
  for _, u in ipairs(self:allUnits(s)) do
    if u.alive and self:nodeOf(s, u.hex) == node then out[#out + 1] = u end
  end
  return out
end

function Core:canStop(s, node, team)
  local us = self:unitsAtNode(s, node)
  if node:sub(1, 2) == "T:" then
    for _, u in ipairs(us) do if u.team ~= team then return false end end
    return true
  end
  return #us == 0
end

-- -------------------------------------------------------------- visibility
function Core:tileTeamSets(s)
  local out = {}
  for _, u in ipairs(self:allUnits(s)) do
    if u.alive and u.kind ~= "monster" then
      local t = self:tile(u.hex)
      out[t] = out[t] or {}
      out[t][u.team] = true
    end
  end
  return out
end

local function setSize(set)
  local n = 0
  for _ in pairs(set or {}) do n = n + 1 end
  return n
end

function Core:watched(s, sets)
  local w = {}
  if self.cfg.adjacency_reveal == false then return w end
  local radius = self.cfg.reveal_radius or 1
  for _, c in ipairs(s.champs) do
    if c.alive then
      local near, list = {}, {}
      for _, n in ipairs(self:neighbors(c.hex)) do
        if not near[key(n)] then near[key(n)] = true; list[#list + 1] = n end
      end
      for _ = 1, radius - 1 do
        local snapshot = {}
        for i = 1, #list do snapshot[i] = list[i] end
        for _, h in ipairs(snapshot) do
          for _, n in ipairs(self:neighbors(h)) do
            if not near[key(n)] then near[key(n)] = true; list[#list + 1] = n end
          end
        end
      end
      for _, nb in ipairs(list) do
        local t = self:tile(nb)
        if t and not w[t] then
          for team in pairs(sets[t] or {}) do
            if team ~= c.team then w[t] = true; break end
          end
        end
      end
    end
  end
  return w
end

-- Rules 3.3 step 3 / 3.4: champions inside a newly visible tile take hexes.
function Core:placeOnFlip(s, tile, events)
  local hexes = self.tileHexes[tile]
  local fixed, movable = {}, {}
  for _, u in ipairs(self:allUnits(s)) do
    if u.alive and self:tile(u.hex) == tile then
      if u.kind == "champion" then movable[#movable + 1] = u else fixed[key(u.hex)] = u end
    end
  end
  if #movable == 0 then return end
  local free = {}
  for _, h in ipairs(hexes) do if not fixed[key(h)] then free[#free + 1] = h end end
  local isFree = {}
  for _, h in ipairs(free) do isFree[key(h)] = true end
  local assigned, taken = {}, {}
  for _, c in ipairs(movable) do
    if isFree[key(c.hex)] and not taken[key(c.hex)] then
      assigned[c] = c.hex; taken[key(c.hex)] = true
    end
  end
  for _, c in ipairs(movable) do
    if not assigned[c] then
      local spot
      for _, h in ipairs(free) do if not taken[key(h)] then spot = h; break end end
      if not spot then
        for _, h in ipairs(hexes) do
          for _, nb in ipairs(self:neighbors(h)) do
            if self:tile(nb) ~= tile and not spot and not taken[key(nb)]
                and #self:unitsAtNode(s, self:nodeOf(s, nb)) == 0 then
              spot = nb
            end
          end
        end
        spot = spot or c.hex
      end
      assigned[c] = spot; taken[key(spot)] = true
    end
  end
  for _, c in ipairs(movable) do
    if key(assigned[c]) ~= key(c.hex) and events then
      events[#events + 1] = {t = "place", uid = c.uid, from = c.hex, to = assigned[c]}
    end
    c.hex = assigned[c]
  end
end

function Core:forceVisible(s, tile, events)
  if isHidden(s, tile) then
    s.hidden[tile] = nil
    if events then events[#events + 1] = {t = "flip", tile = tile, visible = true} end
    self:placeOnFlip(s, tile, events)
  end
end

function Core:refresh(s, allowFlipBack, events)
  local sets = self:tileTeamSets(s)
  local watched = self:watched(s, sets)
  local newly = {}
  for _, t in ipairs(self.tileNames) do
    local contested = setSize(sets[t]) > 1 or watched[t]
    local warded = (s.wards and s.wards[t] or -1) >= s.round
    local hidden = isHidden(s, t)
    if hidden and (contested or warded) then
      s.hidden[t] = nil
      newly[#newly + 1] = t
      if events then events[#events + 1] = {t = "flip", tile = t, visible = true} end
    elseif not hidden and allowFlipBack ~= false and not contested and not warded then
      s.hidden[t] = true
      if events then events[#events + 1] = {t = "flip", tile = t, visible = false} end
    end
  end
  for _, t in ipairs(newly) do self:placeOnFlip(s, t, events) end
end

-- ----------------------------------------------------------------- numbers
function Core:waveSize(round)
  local c = self.cfg
  if c.wave_growth_round2 and round >= c.wave_growth_round2 then return c.wave_chips_late2 end
  if round >= c.wave_growth_round then return c.wave_chips_late end
  return c.wave_chips
end

function Core:deathPosition(round)
  local band = 3
  if round <= DEATH_BANDS[1][1] then band = 1 elseif round <= DEATH_BANDS[2][1] then band = 2 end
  local pos = self.cfg.death_track_positions
  if pos then return pos[band] end
  return DEATH_BANDS[band][2] + (self.cfg.death_band_bonus or 0)
end

function Core:killReward(s, team)
  local mult = self.cfg.kill_ap_waves or 0
  if mult > 0 then
    local size = self:waveSize(s.round)
    if self.opts.kill_includes_baron and team and s.teams[team].baron then
      size = size + self.cfg.baron_wave_bonus
    end
    return math.floor(mult * size + 0.5)
  end
  return self.cfg.kill_ap or 1
end

-- ------------------------------------------------------------- kill / hits
function Core:killChampion(s, victim, killerTeam, events)
  victim.alive = false
  victim.hp = 0
  victim.shield = 0
  victim.track = self:deathPosition(s.round)
  local reward = 0
  if killerTeam then
    reward = self:killReward(s, killerTeam)
    s.teams[killerTeam].ap = s.teams[killerTeam].ap + reward
    s.teams[killerTeam].kills = s.teams[killerTeam].kills + 1
  end
  if events then
    events[#events + 1] = {t = "kill", uid = victim.uid, team = killerTeam, ap = reward,
                           track = victim.track}
  end
end

function Core:monsterReward(s, m, team, events)
  local ts = s.teams[team]
  ts.cards = ts.cards or {}
  if m.mtype == "blue_buff" or m.mtype == "red_buff" then
    ts.cards[m.mtype] = (ts.cards[m.mtype] or 0) + 1
  elseif m.mtype == "dragon" then
    ts.dragons = (ts.dragons or 0) + 1
    if self.cfg.dragon_card and ts.dragons <= (self.cfg.dragon_cap or 2) then
      ts.cards.dragon = (ts.cards.dragon or 0) + 1
    end
  elseif m.mtype == "baron" then
    ts.baron = true
  end
  if events then events[#events + 1] = {t = "reward", mtype = m.mtype, team = team} end
end

function Core:destroy(s, target, team, events)
  target.alive = false
  if target.kind == "wave" then
    for i, w in ipairs(s.waves) do if w == target then table.remove(s.waves, i); break end end
    if events then events[#events + 1] = {t = "wave_down", uid = target.uid} end
  elseif target.kind == "structure" then
    if target.stype == "nexus" then
      s.winner = other(target.team)
      s.end_reason = "nexus"
    else
      s.teams[target.team].towers_lost = s.teams[target.team].towers_lost + 1
      local reward = self.cfg.tower_kill_ap or 0
      if team and reward > 0 then s.teams[team].ap = s.teams[team].ap + reward end
    end
    if events then events[#events + 1] = {t = "structure_down", uid = target.uid, team = team} end
  elseif target.kind == "monster" then
    if team then self:monsterReward(s, target, team, events) end
    target.respawn_round = s.round + self.cfg.monsters[target.mtype].respawn
    if events then events[#events + 1] = {t = "monster_down", uid = target.uid, team = team} end
  end
end

-- World Phase damage (no champion source: chips go to the supply).
function Core:dealHits(s, team, target, k, events)
  if k <= 0 or not target.alive then return end
  if target.kind == "champion" then
    local absorbed = 0
    if (target.shield or 0) > 0 and (target.shield_until or 0) >= s.round then
      absorbed = math.min(target.shield, k)
      target.shield = target.shield - absorbed
    end
    local dmg = k - absorbed
    if dmg <= 0 then return end
    target.hp = target.hp - dmg
    if events then events[#events + 1] = {t = "hit", uid = target.uid, k = dmg} end
    if target.hp <= 0 then self:killChampion(s, target, team, events) end
    return
  end
  local chips = math.min(k, target.chips)
  target.chips = target.chips - chips
  if events then events[#events + 1] = {t = "hit", uid = target.uid, k = chips} end
  if target.chips <= 0 then self:destroy(s, target, team, events) end
end

-- ------------------------------------------------------------------ Upkeep
function Core:respawn(s, c)
  local home = self.fountain[c.team]
  local baseTile = self.baseTile[c.team]
  local baseHexes = {home}
  for _, h in ipairs(self.tileHexes[baseTile]) do
    if key(h) ~= key(home) then baseHexes[#baseHexes + 1] = h end
  end
  local ring, inRing = {}, {}
  for _, h in ipairs(self.tileHexes[baseTile]) do
    for _, nb in ipairs(self:neighbors(h)) do
      if self:tile(nb) ~= baseTile and not inRing[key(nb)] then
        ring[#ring + 1] = nb; inRing[key(nb)] = true
      end
    end
  end
  local units = self:allUnits(s)
  local function empty(h)
    for _, u in ipairs(units) do
      if u.alive and key(u.hex) == key(h) then return false end
    end
    return true
  end
  local function legal(h) return self:canStop(s, self:nodeOf(s, h), c.team) end
  local spot
  if legal(home) then spot = home end
  if not spot then
    for _, h in ipairs(baseHexes) do if empty(h) and legal(h) then spot = h; break end end
  end
  if not spot and isHidden(s, baseTile) then
    for _, h in ipairs(baseHexes) do if legal(h) then spot = h; break end end
  end
  if not spot then
    for _, h in ipairs(ring) do if empty(h) and legal(h) then spot = h; break end end
  end
  if not spot then return false end
  c.hex = {spot[1], spot[2]}
  c.alive = true
  c.hp = c.max_hp
  c.shield = 0
  return true
end

function Core:decay(s, events)
  local c = self.cfg
  local step = c.structure_decay or 0
  local every = math.max(1, c.structure_decay_every or 1)
  if step == 0 or s.round < 2 or (s.round - 1) % every ~= 0 then return end
  local base = c.structure_decay_floor or 1
  local floors = {tower = c.tower_decay_floor or base, nexus = c.nexus_decay_floor or base}
  for _, x in ipairs(s.structures) do
    local floor = floors[x.stype]
    if x.alive and x.chips > floor then
      local before = x.chips
      x.chips = math.max(floor, x.chips - step)
      if events then events[#events + 1] = {t = "decay", uid = x.uid, from = before, to = x.chips} end
    end
  end
end

function Core:moveWaves(s, team, events)
  local mine = {}
  for _, w in ipairs(s.waves) do if w.team == team then mine[#mine + 1] = w end end
  stableSort(mine, function(a, b) return a.path_idx > b.path_idx end)
  for _, w in ipairs(mine) do
    local path = self.paths[team][w.lane]
    local steps = self.cfg.wave_speed
    local landed, pos = w.path_idx, w.path_idx
    for _ = 1, steps do
      if pos + 1 >= #path then break end
      local nxt = path[pos + 2]
      local node = self:nodeOf(s, nxt)
      local isTile = node:sub(1, 2) == "T:"
      local units = {}
      for _, u in ipairs(self:unitsAtNode(s, node)) do
        if u ~= w and (isTile or key(u.hex) == key(nxt)) then units[#units + 1] = u end
      end
      local enemyInside = false
      for _, u in ipairs(units) do
        if u.team ~= nil and u.team ~= team then enemyInside = true end
      end
      if isTile and enemyInside then
        self:forceVisible(s, self:tile(nxt), events)
        break
      end
      local blocked = false
      for _, u in ipairs(units) do
        if (u.team ~= nil and u.team ~= team) or u.kind == "monster" then blocked = true end
      end
      if blocked then break end
      pos = pos + 1
      local friend = false
      for _, u in ipairs(self:unitsAtNode(s, self:nodeOf(s, nxt))) do
        if u ~= w and key(u.hex) == key(nxt) and u.team == team then friend = true end
      end
      if not friend then landed = pos end
    end
    if landed ~= w.path_idx then
      if events then
        events[#events + 1] = {t = "wave_move", uid = w.uid, from = w.hex, to = path[landed + 1]}
      end
      w.path_idx = landed
      w.hex = {path[landed + 1][1], path[landed + 1][2]}
    end
  end
end

function Core:spawnWaves(s, events)
  local size = self:waveSize(s.round)
  for _, team in ipairs(TEAMS) do
    local bonus = s.teams[team].baron and self.cfg.baron_wave_bonus or 0
    for _, lane in ipairs(self.lanes) do
      local hex = self.paths[team][lane][1]
      local node = self:nodeOf(s, hex)
      local occupants, friendly = {}, nil
      for _, u in ipairs(self:unitsAtNode(s, node)) do
        if key(u.hex) == key(hex) then
          occupants[#occupants + 1] = u
          if u.kind == "wave" and u.team == team and not friendly then friendly = u end
        end
      end
      if friendly then
        friendly.chips = friendly.chips + size + bonus
        if events then events[#events + 1] = {t = "wave_merge", uid = friendly.uid, add = size + bonus} end
      elseif #occupants == 0 then
        local uid = "w" .. s.next_uid
        s.next_uid = s.next_uid + 1
        local w = {uid = uid, team = team, lane = lane, chips = size + bonus, path_idx = 0,
                   hex = {hex[1], hex[2]}, empowered = s.teams[team].baron == true,
                   kind = "wave", alive = true}
        s.waves[#s.waves + 1] = w
        if events then events[#events + 1] = {t = "wave_spawn", uid = uid} end
      end
    end
  end
end

function Core:upkeep(s)
  local cfg, events = self.cfg, {}
  -- Designer: a monster that was hit but not killed is back to full at the
  -- end of the round (the start of this Upkeep).
  if self.opts.monster_heal then
    for _, m in ipairs(s.monsters) do
      if m.alive and m.chips < m.max_chips then
        events[#events + 1] = {t = "monster_heal", uid = m.uid, from = m.chips, to = m.max_chips}
        m.chips = m.max_chips
      end
    end
  end
  s.round = s.round + 1                                   -- step 1
  if s.round > 1 then s.priority = other(s.priority) end
  for _, c in ipairs(s.champs) do                         -- step 2
    if (c.track or 0) > 0 then c.track = c.track - 1 end
    if c.track == 0 and not c.alive then
      if self:respawn(s, c) then events[#events + 1] = {t = "respawn", uid = c.uid, hex = c.hex} end
    end
    if (c.shield_until or 0) < s.round then c.shield = 0 end
  end
  for _, team in ipairs(TEAMS) do
    local ts = s.teams[team]
    if ts.dragon_track and #ts.dragon_track > 0 then
      local keep, back = {}, 0
      for _, p in ipairs(ts.dragon_track) do
        if p - 1 > 0 then keep[#keep + 1] = p - 1 else back = back + 1 end
      end
      ts.dragon_track = keep
      ts.cards = ts.cards or {}
      if back > 0 then ts.cards.dragon = (ts.cards.dragon or 0) + back end
    end
  end
  for _, c in ipairs(s.champs) do                         -- step 3
    if c.alive and self:tile(c.hex) == self.baseTile[c.team] and c.hp ~= c.max_hp then
      events[#events + 1] = {t = "heal", uid = c.uid, from = c.hp, to = c.max_hp}
      c.hp = c.max_hp
    end
  end
  self:decay(s, events)
  for _, team in ipairs(TEAMS) do                         -- step 4
    local ts = s.teams[team]
    ts.ap = cfg.ap_base + math.min(ts.dragons or 0, cfg.dragon_cap) * (cfg.dragon_ap_each or 1)
  end
  self:moveWaves(s, s.priority, events)                   -- step 5
  self:moveWaves(s, other(s.priority), events)
  self:refresh(s, true, events)
  if s.round % 2 == 1 or not cfg.wave_spawn_odd_rounds_only then  -- step 6
    self:spawnWaves(s, events)
  end
  for _, m in ipairs(s.monsters) do                       -- step 7
    if not m.alive and s.round >= m.respawn_round then
      local blocked = false
      for _, u in ipairs(self:allUnits(s)) do
        if u.alive and u ~= m and key(u.hex) == key(m.hex) then blocked = true end
      end
      if not blocked then
        m.alive = true
        m.chips = m.max_chips
        events[#events + 1] = {t = "monster_spawn", uid = m.uid}
      end
    end
  end
  self:refresh(s, true, events)                           -- step 8
  return events
end

-- --------------------------------------------------------------- World
function Core:concealed(s, u, srcTile)
  if u.kind ~= "champion" then return false end
  local t = self:tile(u.hex)
  return t ~= srcTile and isHidden(s, t)
end

function Core:effectAdjacent(s, u)
  local tile = self:tile(u.hex)
  local units = self:allUnits(s)
  local out, seen = {}, {}
  for _, o in ipairs(units) do
    if o ~= u and o.alive and self:tile(o.hex) == tile then out[#out + 1] = o; seen[o] = true end
  end
  for dq = -1, 1 do
    for dr = math.max(-1, -dq - 1), math.min(1, -dq + 1) do
      if dq ~= 0 or dr ~= 0 then
        local h = {u.hex[1] + dq, u.hex[2] + dr}
        for _, o in ipairs(units) do
          if o.alive and o ~= u and key(o.hex) == key(h) and not seen[o]
              and not self:concealed(s, o, tile) then
            out[#out + 1] = o; seen[o] = true
          end
        end
      end
    end
  end
  return out
end

function Core:structureTargetable(s, x)
  if x.stype == "tower" then
    if x.tier == 1 then return true end
    for _, y in ipairs(s.structures) do
      if y.team == x.team and y.stype == "tower" and y.lane == x.lane and y.tier == 1 then
        return not y.alive
      end
    end
    return true
  end
  local lanes = {}
  for _, y in ipairs(s.structures) do
    if y.team == x.team and y.stype == "tower" then
      lanes[y.lane] = lanes[y.lane] or {}
      table.insert(lanes[y.lane], y)
    end
  end
  for _, ts in pairs(lanes) do
    local down = true
    for _, y in ipairs(ts) do if y.alive then down = false end end
    if down then return true end
  end
  return false
end

function Core:canBeHitByWave(s, u, team)
  if not u.alive or u.team == team then return false end
  if u.kind == "structure" then return self:structureTargetable(s, u) end
  return true
end

function Core:world(s)
  local cfg, events, pending = self.cfg, {}, {}
  for _, w in ipairs(s.waves) do
    for _, u in ipairs(self:effectAdjacent(s, w)) do
      if self:canBeHitByWave(s, u, w.team) then
        local hits = 1
        if w.empowered and u.kind == "structure" then hits = 2 end
        pending[#pending + 1] = {u, hits, w.team}
      end
    end
  end
  for _, x in ipairs(s.structures) do
    if x.alive and x.stype == "tower" then
      for _, u in ipairs(self:effectAdjacent(s, x)) do
        if u.team ~= x.team and u.team ~= nil then
          if u.kind == "champion" then pending[#pending + 1] = {u, cfg.tower_hits_champion, x.team}
          elseif u.kind == "wave" then pending[#pending + 1] = {u, cfg.tower_hits_wave, x.team} end
        end
      end
    end
  end
  for _, m in ipairs(s.monsters) do
    if m.alive then
      for _, u in ipairs(self:effectAdjacent(s, m)) do
        if u.kind == "champion" then pending[#pending + 1] = {u, cfg.monster_hits, nil} end
      end
    end
  end
  local order, totals = {}, {}
  for _, p in ipairs(pending) do
    local u, k, team = p[1], p[2], p[3]
    if u.items and u.items.cloth_armor then k = math.max(0, k - 1) end
    if k > 0 then
      local cur = totals[u]
      if cur then cur[2] = cur[2] + k
      else totals[u] = {u, k, team}; order[#order + 1] = u end
    end
  end
  for _, u in ipairs(order) do
    local t = totals[u]
    if u.alive then self:dealHits(s, t[3], u, t[2], events) end
  end
  self:refresh(s, true, events)
  return events
end

-- ---------------------------------------------------------------- end
function Core:tiebreak(s)
  local lost = {north = s.teams.north.towers_lost, south = s.teams.south.towers_lost}
  if lost.north ~= lost.south then
    if lost.south > lost.north then return "north", "round_limit_towers" end
    return "south", "round_limit_towers"
  end
  local hp = {north = 0, south = 0}
  for _, x in ipairs(s.structures) do hp[x.team] = hp[x.team] + x.chips end
  if hp.north ~= hp.south then
    if hp.north > hp.south then return "north", "round_limit_hp" end
    return "south", "round_limit_hp"
  end
  local k = {north = s.teams.north.kills, south = s.teams.south.kills}
  if k.north ~= k.south then
    if k.north > k.south then return "north", "round_limit_kills" end
    return "south", "round_limit_kills"
  end
  return nil, "round_limit_draw"
end

return Core
