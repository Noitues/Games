-- Hex-Nexus HP counter: champions, towers, the Nexus and monsters.
-- Left-click removes 1 HP, right-click adds 1. The starting numbers come from
-- the exporter (script state), never from this file.
local st = {}

function onLoad(saved)
  local ok, t = pcall(JSON.decode, saved or "")
  if ok and type(t) == "table" then st = t end
  st.hp = st.hp or 0
  st.max = st.max or st.hp
  draw()
end

function onSave()
  return JSON.encode(st)
end

function hnGet()
  return st
end

function hnSet(t)
  for k, v in pairs(t or {}) do st[k] = v end
  draw()
end

local function label()
  if st.kind == "champion" then
    return st.hp .. "/" .. st.max
  elseif st.kind == "structure" then
    return st.hp .. " (min " .. (st.floor or 0) .. ")"
  elseif st.kind == "monster" and st.hp <= 0 then
    return "down"
  end
  return tostring(st.hp)
end

function draw()
  self.clearButtons()
  local s = self.getScale()
  local k = 1 / math.max(s.x, 0.01)
  -- local half-depth of the token, so the label sits on its lower edge
  -- (local +z is the bottom of the image) and leaves the art readable
  local b = self.getBoundsNormalized()
  local half = 0.5
  if b and b.size and s.z > 0 then half = b.size.z / s.z / 2 end
  local colour = {0, 0, 0, 0.75}
  if st.kind == "champion" and st.hp > st.max then colour = {0.55, 0.42, 0.05, 0.85} end
  if st.hp <= 0 then colour = {0.45, 0.05, 0.05, 0.85} end
  local text = label()
  self.createButton({
    click_function = "hnClick", function_owner = self, label = text,
    position = {0, 0.2, half * 0.72}, rotation = {0, 0, 0}, scale = {k * 0.5, 1, k * 0.5},
    width = 110 * #text + 160, height = 260, font_size = 200,
    color = colour, font_color = {1, 1, 1},
    tooltip = (st.label or "") .. ": left-click -1, right-click +1",
  })
end

function hnClick(_, player_colour, alt)
  st.hp = math.max(0, st.hp + (alt and 1 or -1))
  draw()
end
