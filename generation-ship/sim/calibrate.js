// Measures what the PP framework guesses: card-threshold hit rates by requirement size,
// innate tier reach rates, and each house's expected innate PP per generation.
// Writes data/calibration.json, which tools/generate_people.py reads to price threshold bonuses.
//   node sim/calibrate.js --games 30 --bot house
import { Worker } from "node:worker_threads";
import { fileURLToPath } from "node:url";
import { writeFileSync, readFileSync } from "node:fs";

const argv = process.argv.slice(2);
const arg = (k, d) => { const i = argv.indexOf(`--${k}`); return i >= 0 ? argv[i + 1] : d; };
const games = Number(arg("games", 30)), bot = arg("bot", "house");
const houses = JSON.parse(readFileSync(new URL("../data/houses.json", import.meta.url))).houses;
const H = houses.map((h) => h.id);
const combos = [];
for (let i = 0; i < H.length; i++) for (let j = i + 1; j < H.length; j++) combos.push([H[i], H[j]]);
const worker = fileURLToPath(new URL("./parallel.js", import.meta.url));
const runJob = (job) => new Promise((res, rej) => {
  const w = new Worker(worker, { workerData: { job } }); w.on("message", (m) => res(m.agg)); w.on("error", rej);
});

const aggs = [];
for (let k = 0; k < combos.length; k += 4) {
  aggs.push(...await Promise.all(combos.slice(k, k + 4).map((c) => runJob({ games, players: 2, houses: c, bot, seed: 31 }))));
}
const byN = {}, innate = {};
for (const a of aggs) {
  for (const [n, [t, m]] of Object.entries(a.thresholdByN || {})) { byN[n] ??= [0, 0]; byN[n][0] += t; byN[n][1] += m; }
  for (const [h, x] of Object.entries(a.houses)) { innate[h] ??= [0, 0, 0, 0]; x.innate.forEach((v, i) => (innate[h][i] += v)); }
}
const thresholdRate = Object.fromEntries(Object.entries(byN).map(([n, [t, m]]) => [n, +(m / t).toFixed(3)]));
const houseInnate = {};
for (const h of houses) {
  const v = innate[h.id], tot = v.reduce((a, b) => a + b, 0);
  const p = v.map((x) => x / tot);
  const expPP = h.innate.tiers.reduce((s, t) => s + p[t.tier] * t.pp, 0);
  houseInnate[h.id] = { reach: p.map((x) => +x.toFixed(3)), expectedPPPerGen: +expPP.toFixed(2) };
}
const out = { measured: new Date().toISOString().slice(0, 10), bot, gamesPerCombo: games, thresholdRate, houseInnate };
writeFileSync(new URL("../data/calibration.json", import.meta.url), JSON.stringify(out, null, 1));
console.log(JSON.stringify(out, null, 1));
