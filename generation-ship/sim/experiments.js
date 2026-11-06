// Compare rule variants on the same seeds: all 28 two-house pairings per variant.
//   node sim/experiments.js --games 25
import { Worker } from "node:worker_threads";
import { fileURLToPath } from "node:url";
import { readFileSync } from "node:fs";

const argv = process.argv.slice(2);
const arg = (k, d) => { const i = argv.indexOf(`--${k}`); return i >= 0 ? argv[i + 1] : d; };
const games = Number(arg("games", 25));
const only = arg("only", null);
const H = JSON.parse(readFileSync(new URL("../data/houses.json", import.meta.url))).houses.map((h) => h.id);
const pairs = [];
for (let i = 0; i < H.length; i++) for (let j = i + 1; j < H.length; j++) pairs.push([H[i], H[j]]);
const worker = fileURLToPath(new URL("./parallel.js", import.meta.url));
const runJob = (job) => new Promise((res, rej) => {
  const w = new Worker(worker, { workerData: { job } }); w.on("message", (m) => res(m)); w.on("error", rej);
});

const VARIANTS = {
  baseline: { cfg: {} },
  "haven +1 range": { cfg: { havenRangeBonus: 1 } },
  "Remarkables only on growth C": { cfg: { remarkableAccess: "growthC" } },
  "Crew requirement 4/player": { cfg: { crewRequirementPerPlayer: 4 } },
};

console.log("variant | win | win gen | tier III share | Decay loss | Meridian strength | house spread (max-min)");
for (const [name, v] of Object.entries(VARIANTS)) {
  if (only && !name.includes(only)) continue;
  const res = [];
  for (let k = 0; k < pairs.length; k += 4) {
    res.push(...await Promise.all(pairs.slice(k, k + 4).map((houses) =>
      runJob({ games, players: 2, houses, bot: "house", seed: 202, cfg: v.cfg, pairing: v.pairing ?? "offset" }))));
  }
  let G = 0, W = 0, wg = 0, t3 = 0, dec = 0;
  const strength = {};
  for (const { key, agg: a } of res) {
    G += a.games; W += a.wins; wg += a.winGens;
    for (const [c, n] of Object.entries(a.causes)) { if (c.includes("tier 3")) t3 += n; if (c === "loss: decay") dec += n; }
    for (const h of key.split("+")) (strength[h] ??= []).push(a.wins / a.games);
  }
  const s = Object.fromEntries(Object.entries(strength).map(([h, xs]) => [h, xs.reduce((a, b) => a + b) / xs.length]));
  const vals = Object.values(s);
  const pct = (x) => `${(100 * x).toFixed(0)}%`;
  console.log(`${name} | ${pct(W / G)} | ${(wg / Math.max(1, W)).toFixed(1)} | ${pct(t3 / Math.max(1, W))} | ${pct(dec / G)} | ${pct(s.meridian)} | ${(100 * (Math.max(...vals) - Math.min(...vals))).toFixed(0)} pts`);
}
