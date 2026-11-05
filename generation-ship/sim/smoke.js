// Smoke test: every bot level plays full games with every house, without errors.
import { loadData } from "./load.js";
import { playGame } from "../src/engine/game.js";
import { Bot } from "../src/ai/bots.js";

const data = loadData();
const houses = ["galvan", "meridian", "keel", "vigil", "foremen", "gardeners", "voidwardens", "tellers"];
let n = 0;
for (let level = 0; level <= 3; level++) for (let p = 1; p <= 4; p++) for (const pairing of ["offset"]) {
  const hs = houses.slice((level * 2) % 5, (level * 2) % 5 + p);
  const st = playGame(data, hs.map((_, i) => new Bot(level, 11 + i)), { players: p, houses: hs, eventPairing: pairing }, 42 + level * 10 + p);
  if (!st.result) throw new Error("game did not finish");
  n++;
}
console.log(`smoke ok: ${n} games`);
