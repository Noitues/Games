// How many of each piece a physical copy needs: the most of each on the table at once, per game,
// across player counts (house bots). Reports the 95th percentile and the maximum. Pieces (threat,
// Crew, Decay, influence) are counted; tokens (Brace, Patch, Lockout, Isolate, Quarantine, Unrest)
// are numbered markers, so the count is sections holding one, and <token>Max the largest value.
//   node sim/components.js [--games 20]
import { loadData } from "./load.js";
import { createGame, makeContext, setupRamp, runPhase, PHASES } from "../src/engine/game.js";
import { Bot } from "../src/ai/bots.js";

const argv = process.argv.slice(2);
const games = Number(argv[argv.indexOf("--games") + 1] || 20);
const data = loadData();
const H = data.houses.houses.map((h) => h.id);
const KEYS = ["glitch", "fault", "failure", "crew", "decay", "brace", "patch", "lockout", "quarantine", "unrest", "isolate"];
const PIECES = new Set(["glitch", "fault", "failure", "crew", "decay"]);
const TOKENS = ["brace", "patch", "lockout", "isolate"];

function peaks(players, g) {
  const houses = Array.from({ length: players }, (_, i) => H[(g * 3 + i * 5) % H.length]).filter((h, i, a) => a.indexOf(h) === i);
  const P = houses.length;
  const { st, cfg } = createGame(data, { players: P, houses }, 9000 + g * 7 + players);
  const G = makeContext(data, cfg, houses.map((_, i) => new Bot(3, g * 10 + i)));
  setupRamp(G, st);
  const peak = Object.fromEntries(KEYS.map((k) => [k, 0])); peak.influence = 0; peak.decayTotal = 0;
  const look = () => {
    const sum = Object.fromEntries(KEYS.map((k) => [k, 0]));
    const inf = Array(P).fill(0);
    for (const id of st.order) {
      const s = st.sections[id];
      // threat, Crew and Decay are pieces (count them); tokens are numbered markers (count sections)
      for (const k of KEYS) sum[k] += PIECES.has(k) ? s[k] : s[k] ? 1 : 0;
      for (const k of TOKENS) peak[`${k}Max`] = Math.max(peak[`${k}Max`] || 0, s[k]);
      for (const [h, n] of Object.entries(s.influence)) inf[h] += n;
    }
    for (const k of KEYS) peak[k] = Math.max(peak[k], sum[k]);
    peak.influence = Math.max(peak.influence, ...inf);
  };
  look();
  while (!st.result) {
    st.gen += 1;
    if (st.gen > cfg.maxGenerations) break;
    for (const p of PHASES) { runPhase(G, st, p); look(); if (st.result) break; }
  }
  return peak;
}

const pct = (arr, q) => { const a = [...arr].sort((x, y) => x - y); return a[Math.min(a.length - 1, Math.floor(q * a.length))]; };
const all = [];
const OUT = [...KEYS, "influence", ...TOKENS.map((k) => `${k}Max`)];
for (const players of [1, 2, 3, 4]) {
  const rows = Array.from({ length: games }, (_, g) => peaks(players, g));
  all.push(...rows);
  const line = OUT.map((k) => `${k} ${pct(rows.map((r) => r[k]), 0.95)}/${Math.max(...rows.map((r) => r[k]))}`).join(" · ");
  console.log(`${players}p (95th pct / max): ${line}`);
}
console.log(`\nAll (95th pct / max): ${OUT.map((k) => `${k} ${pct(all.map((r) => r[k]), 0.95)}/${Math.max(...all.map((r) => r[k]))}`).join(" · ")}`);
