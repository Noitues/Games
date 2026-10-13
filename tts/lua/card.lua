-- Hex-Nexus card: champion cards count their own cooldown, buff and item
-- cards are played or bought from their right-click menu.
--   champ: READY / CD n / DEAD n. "Use <ability>" pays its AP and puts the
--          whole card on cooldown (Rules 5.2). Click: -1 / +1 cooldown.
--   buff:  Dragon is reusable (cooldown); Blue and Red Buff are one use.
--   item:  "Buy" pays its cost in the Shop Phase.
local st = {}

function onLoad(saved)
  local ok, t = pcall(JSON.decode, saved or "")
  if ok and type(t) == "table" then st = t end
  st.track = st.track or 0
  build()
end

function onSave() return JSON.encode(st) end
function hnGet() return st end

function hnSet(t)
  for k, v in pairs(t or {}) do st[k] = v end
  build()
end

local function status()
  if st.kind == "item" then
    if st.bought then return "OWNED", {0.15, 0.35, 0.15, 0.9} end
    return st.cost .. " AP", {0, 0, 0, 0.75}
  end
  if st.kind == "buff" and st.buff ~= "dragon" then
    if st.buff == "baron" then return "BARON", {0.35, 0.15, 0.45, 0.9} end
    return "PLAY", {0, 0, 0, 0.75}
  end
  if st.dead then return "DEAD " .. st.track, {0.5, 0.05, 0.05, 0.9} end
  if st.track > 0 then return "CD " .. st.track, {0.45, 0.3, 0.05, 0.9} end
  return "READY", {0.1, 0.4, 0.15, 0.9}
end

function build()
  self.clearButtons()
  self.clearContextMenu()
  local text, colour = status()
  local s = self.getScale()
  local k = 1 / math.max(s.x, 0.01)
  self.createButton({
    click_function = "hnClick", function_owner = self, label = text,
    position = {0, 0.3, -0.6}, rotation = {0, 0, 0}, scale = {k * 0.5, 1, k * 0.5},
    width = 1500, height = 380, font_size = 300, color = colour, font_color = {1, 1, 1},
    tooltip = "Left-click -1, right-click +1 (cooldown)",
  })
  if st.kind == "champ" then
    for _, key in ipairs(st.order or {}) do
      local a = st.ab[key]
      self.addContextMenuItem("Use " .. key .. " · " .. a.cost .. " AP · CD" .. a.cd, function(colour)
        Global.call("hnUseAbility", {guid = self.getGUID(), key = key, colour = colour})
      end)
    end
  elseif st.kind == "buff" then
    self.addContextMenuItem("Play " .. (st.name or "card"), function(colour)
      Global.call("hnPlayBuff", {guid = self.getGUID(), colour = colour})
    end)
  elseif st.kind == "item" and not st.bought then
    self.addContextMenuItem("Buy · " .. st.cost .. " AP", function(colour)
      Global.call("hnBuyItem", {guid = self.getGUID(), colour = colour})
    end)
  end
end

function hnClick(_, _, alt)
  if st.kind == "item" or (st.kind == "buff" and st.buff ~= "dragon") then return end
  st.track = math.max(0, st.track + (alt and 1 or -1))
  if st.track == 0 then st.dead = false end
  build()
end
