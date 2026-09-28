--[[ A minimal fake of the Tabletop Simulator scripting API, enough to run the
mod's scripts headless in plain Lua 5.2 (tts/tests/smoke_m0.py drives it).

It fakes what TTS does that the scripts depend on: objects with GM notes,
scale and bounds, Wait callbacks, the XML UI, and JSON. A fake custom object
measures BASE world units across at scale 1 (TTS picks its own base size;
the Global script's calibration must not care what it is).
]]
local Stub = {BASE = 2.0, PIVOT_OFFSET = 0.13}

-- -------------------------------------------------------------------- JSON
local function encode(v)
  local t = type(v)
  if t == "nil" then return "null"
  elseif t == "boolean" or t == "number" then return tostring(v)
  elseif t == "string" then
    return '"' .. v:gsub('[%c"\\]', function(c)
      return string.format("\\u%04x", c:byte()) end) .. '"'
  end
  local n = 0
  for _ in pairs(v) do n = n + 1 end
  if n == #v and n > 0 then
    local parts = {}
    for i = 1, #v do parts[i] = encode(v[i]) end
    return "[" .. table.concat(parts, ",") .. "]"
  end
  local parts = {}
  for k, x in pairs(v) do parts[#parts + 1] = encode(tostring(k)) .. ":" .. encode(x) end
  return "{" .. table.concat(parts, ",") .. "}"
end

local function decode(s)
  local i = 1
  local function ws() i = s:find("[^ \t\r\n]", i) or #s + 1 end
  local value
  local function str()
    local out, j = {}, i + 1
    while true do
      local c = s:sub(j, j)
      if c == '"' then i = j + 1; return table.concat(out) end
      if c == "\\" then
        local e = s:sub(j + 1, j + 1)
        if e == "u" then
          local cp = tonumber(s:sub(j + 2, j + 5), 16)
          if cp < 128 then out[#out + 1] = string.char(cp)
          elseif cp < 2048 then
            out[#out + 1] = string.char(192 + math.floor(cp / 64), 128 + cp % 64)
          else
            out[#out + 1] = string.char(224 + math.floor(cp / 4096),
              128 + math.floor(cp / 64) % 64, 128 + cp % 64)
          end
          j = j + 6
        else
          local map = {n = "\n", t = "\t", r = "\r", b = "\b", f = "\f"}
          out[#out + 1] = map[e] or e
          j = j + 2
        end
      else out[#out + 1] = c; j = j + 1 end
    end
  end
  function value()
    ws()
    local c = s:sub(i, i)
    if c == "{" then
      local t = {}; i = i + 1; ws()
      if s:sub(i, i) == "}" then i = i + 1; return t end
      while true do
        ws(); local k = str(); ws(); i = i + 1
        t[k] = value(); ws()
        local d = s:sub(i, i); i = i + 1
        if d == "}" then return t end
      end
    elseif c == "[" then
      local t = {}; i = i + 1; ws()
      if s:sub(i, i) == "]" then i = i + 1; return t end
      while true do
        t[#t + 1] = value(); ws()
        local d = s:sub(i, i); i = i + 1
        if d == "]" then return t end
      end
    elseif c == '"' then return str()
    elseif s:sub(i, i + 3) == "true" then i = i + 4; return true
    elseif s:sub(i, i + 4) == "false" then i = i + 5; return false
    elseif s:sub(i, i + 3) == "null" then i = i + 4; return nil
    else
      local num = s:match("^-?[%d.eE+-]+", i)
      i = i + #num
      return tonumber(num)
    end
  end
  return value()
end

Stub.JSON = {encode = encode, decode = decode}

-- ----------------------------------------------------------------- objects
Stub.objects, Stub.byGuid, Stub.ui, Stub.attrs, Stub.log = {}, {}, {}, {}, {}
Stub.queue = {}

function Stub.newObject(spec)
  local o = {}
  local scale = {x = 1, y = 1, z = 1}
  local pos = {x = spec.x or 0, y = spec.y or 1, z = spec.z or 0}
  local rot = {x = 0, y = 0, z = 0}
  local aspect = spec.aspect or 1
  o._spec, o._buttons, o._menu = spec, {}, {}
  o.loading_custom = false
  o.getGUID = function() return spec.guid end
  o.getGMNotes = function() return spec.tag or "" end
  o.getName = function() return spec.nick or "" end
  o.getLock = function() return spec.locked or false end
  o.setLock = function(v) spec.locked = v end
  o.getQuantity = function() return spec.quantity or -1 end
  o.getScale = function() return {x = scale.x, y = scale.y, z = scale.z} end
  o.setScale = function(v) scale = {x = v[1] or v.x, y = v[2] or v.y, z = v[3] or v.z} end
  o.getPosition = function() return {x = pos.x, y = pos.y, z = pos.z} end
  o.setPosition = function(v) pos = {x = v[1] or v.x, y = v[2] or v.y, z = v[3] or v.z} end
  o.setPositionSmooth = function(v) o.setPosition(v) end
  o.getRotation = function() return rot end
  o.setRotation = function(v) rot = {x = v[1] or v.x, y = v[2] or v.y, z = v[3] or v.z} end
  local function size()
    if not spec.custom then return {x = 2, y = 0.2, z = 3} end
    return {x = Stub.BASE * scale.x, y = 0.1 * scale.y, z = Stub.BASE * aspect * scale.z}
  end
  o.getBoundsNormalized = function() return {size = size(), center = o.getPosition(), offset = {x = 0, y = 0, z = 0}} end
  o.getBounds = function()
    local p = o.getPosition()
    return {size = size(), center = {x = p.x + Stub.PIVOT_OFFSET * scale.x, y = p.y, z = p.z}}
  end
  o.isDestroyed = function() return spec.destroyed or false end
  o.getStateId = function() return spec.state_id or 1 end
  o.setState = function(n)
    local ns = spec.states and spec.states[n]
    if not ns then return nil end
    spec.destroyed = true
    Stub.remove(o)
    ns.state_id, ns.states = n, spec.states
    local no = Stub.add(ns)
    no.setPosition(o.getPosition()); no.setRotation(o.getRotation())
    return no
  end
  o.getObjects = function() return spec.contents and spec.contents() or {} end
  o.clearButtons = function() o._buttons = {} end
  o.createButton = function(b) o._buttons[#o._buttons + 1] = b end
  o.addContextMenuItem = function(label, fn) o._menu[label] = fn end
  o.call = function(fname, arg)
    if o._env and o._env[fname] then return o._env[fname](arg) end
  end
  return o
end

function Stub.add(spec)
  local o = Stub.newObject(spec)
  Stub.objects[#Stub.objects + 1] = o
  Stub.byGuid[spec.guid] = o
  return o
end

function Stub.remove(o)
  for i, x in ipairs(Stub.objects) do
    if x == o then table.remove(Stub.objects, i); break end
  end
  Stub.byGuid[o.getGUID()] = nil
end

-- A script environment: TTS globals plus `self` for object scripts.
function Stub.env(self_obj)
  local env = setmetatable({}, {__index = _G})
  env.self = self_obj
  env.JSON = Stub.JSON
  env.getObjects = function() return Stub.objects end
  env.getAllObjects = env.getObjects
  env.getObjectFromGUID = function(g) return Stub.byGuid[g] end
  env.broadcastToAll = function(msg) Stub.log[#Stub.log + 1] = msg end
  env.broadcastToColor = function(msg) Stub.log[#Stub.log + 1] = msg end
  env.printToAll = env.broadcastToAll
  env.UI = {
    setValue = function(id, v) Stub.ui[id] = v end,
    getValue = function(id) return Stub.ui[id] end,
    setAttribute = function(id, k, v) Stub.attrs[id .. "." .. k] = v end,
  }
  env.Wait = {
    frames = function(f) Stub.queue[#Stub.queue + 1] = f end,
    time = function(f, _, reps)
      if reps == -1 then Stub.repeating = Stub.repeating or {}; table.insert(Stub.repeating, f)
      else Stub.queue[#Stub.queue + 1] = f end
    end,
    condition = function(f, cond, _, timeout_f)
      Stub.queue[#Stub.queue + 1] = function()
        if cond() then f() elseif timeout_f then timeout_f() end
      end
    end,
  }
  env.Global = {call = function(fname, arg) return Stub.global[fname](arg) end}
  return env
end

function Stub.flush()
  local guard = 0
  while #Stub.queue > 0 do
    local f = table.remove(Stub.queue, 1)
    f()
    guard = guard + 1
    assert(guard < 10000, "Wait queue does not drain")
  end
end

function Stub.tick()
  for _, f in ipairs(Stub.repeating or {}) do f() end
  Stub.flush()
end

function Stub.runScript(code, self_obj, name)
  local env = Stub.env(self_obj)
  local chunk = assert(load(code, name, "t", env))
  chunk()
  if self_obj then self_obj._env = env end
  return env
end

return Stub
