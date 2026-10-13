-- Hex-Nexus AP counter: one per team, one big number.
-- Left-click -1, right-click +1. The Global script sets it in Upkeep, on
-- kills and rewards, and when an ability or item is paid for.
local st = {team = "north", ap = 0}

function onLoad(saved)
  local ok, t = pcall(JSON.decode, saved or "")
  if ok and type(t) == "table" then st = t end
  st.ap = st.ap or 0
  draw()
end

function onSave() return JSON.encode(st) end
function hnGet() return st.ap end

function hnSet(n)
  st.ap = math.max(0, math.floor(n or 0))
  draw()
end

function draw()
  self.clearButtons()
  local s = self.getScale()
  local k = 1 / math.max(s.x, 0.01)
  self.createButton({
    click_function = "hnClick", function_owner = self, label = tostring(st.ap),
    position = {0, 0.2, 0.08}, rotation = {0, 0, 0}, scale = {k, 1, k},
    width = 1300, height = 1100, font_size = 1000,
    color = {0, 0, 0, 0}, font_color = {0.92, 0.77, 0.24},
    tooltip = "AP pool: left-click -1, right-click +1",
  })
end

function hnClick(_, _, alt)
  hnSet(st.ap + (alt and 1 or -1))
  Global.call("hnRefresh")
end
