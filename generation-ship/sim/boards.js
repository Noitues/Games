// Board and layout balance: solo games on each board (all 8 houses), then every multi-board
// layout with a fixed sample of house combinations.
//   node sim/boards.js --games 20
import { Worker } from "node:worker_threads";
import { fileURLToPath } from "node:url";
import { readFileSync } from "node:fs";

const argv = process.argv.slice(2);
const games = Number(argv[argv.indexOf("--games") + 1] || 20);
const H = JSON.parse(readFileSync(new URL("../data/houses.json", import.meta.url))).houses.map((h) => h.id);
const B = JSON.parse(readFileSync(new URL("../data/boards.json", import.meta.url)));
const worker = fileURLToPath(new URL("./parallel.js", import.meta.url));
const runJob = (job) => new Promise((res, rej) => { const w = new Worker(worker, { workerData: { job } }); w.on("message", (m) => res(m.agg)); w.on("error", rej); });
async function batch(jobs) { const out = []; for (let k = 0; k < jobs.length; k += 4) out.push(...await Promise.all(jobs.slice(k, k + 4).map(runJob))); return out; }
const summarize = (aggs) => {
  const G = aggs.reduce((n, a) => n + a.games, 0), W = aggs.reduce((n, a) => n + a.wins, 0);
  const dec = aggs.reduce((n, a) => n + (a.causes["loss: decay"] || 0), 0);
  return `${(100 * W / G).toFixed(0)}% wins | win gen ${(aggs.reduce((n, a) => n + a.winGens, 0) / Math.max(1, W)).toFixed(1)} | Decay loss ${(100 * dec / G).toFixed(0)}% | ${G} games`;
};
// a fixed rotation of houses so every house appears in every layout
const combo = (n, k) => Array.from({ length: n }, (_, i) => H[(k * 3 + i * 5) % H.length]).filter((h, i, a) => a.indexOf(h) === i);
if (!argv.includes("--layouts-only")) console.log("Solo, one board, all 8 houses:");
for (const b of argv.includes("--layouts-only") ? [] : B.boards.map((x) => x.id)) {
  const aggs = await batch(H.map((h) => ({ games, players: 1, houses: [h], bot: "house", seed: 77, cfg: { boards: [b] } })));
  console.log(`  board ${b}: ${summarize(aggs)}`);
}
console.log("Layouts (8 house combinations each):");
for (const [name, l] of Object.entries(B.layouts)) {
  const n = l.boards.length;
  if (n < 2) continue;
  const jobs = Array.from({ length: 8 }, (_, k) => combo(n, k)).filter((c) => c.length === n)
    .map((houses) => ({ games, players: n, houses, bot: "house", seed: 79, cfg: { layout: name } }));
  console.log(`  ${name.padEnd(8)} (${n} boards, ${l.links.length} links): ${summarize(await batch(jobs))}`);
}
