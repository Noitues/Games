-- Hex-Nexus hexgroup tile. Two states: 1 = hidden side, 2 = visible side.
-- Flipping swaps the state; the Global script re-fits the new state.
function onLoad()
  self.addContextMenuItem("Flip hexgroup", function()
    Global.call("hnFlipTile", {guid = self.getGUID()})
  end)
end
