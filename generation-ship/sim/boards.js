// Board asymmetry check: solo games on each board (all 8 houses) and 2-player games on each
// consecutive board pair (a fixed sample of house pairings).
//   node sim/boards.js --games 30
import { Worker } from "node:worker_threads";
import { fileURLToPath } from "node:url";
import { readFileSync } from "node:fs";

const argv = process.argv.slice(2);
const games = Number(argv[argv.indexOf("--games") + 1] || 30);
const H = JSON.parse(readFileSync(new URL("../data/houses.json", import.meta.url))).houses.map((h) => h.id);
const worker = fileURLToPath(new URL("./parallel.js", import.meta.url));
const runJob = (job) => new Promise((res, rej) => { const w = new Worker(worker, { workerData: { job } }); w.on("message", (m) => res(m.agg)); w.on("error", rej); });
async function batch(jobs) { const out = []; for (let k = 0; k < jobs.length; k += 4) out.push(...await Promise.all(jobs.slice(k, k + 4).map(runJob))); return out; }
const summarize = (aggs) => {
  const G = aggs.reduce((n, a) => n + a.games, 0), W = aggs.reduce((n, a) => n + a.wins, 0);
  const dec = aggs.reduce((n, a) => n + (a.causes["loss: decay"] || 0), 0);
  return `${(100 * W / G).toFixed(0)}% wins | win gen ${(aggs.reduce((n, a) => n + a.winGens, 0) / Math.max(1, W)).toFixed(1)} | Decay loss ${(100 * dec / G).toFixed(0)}%`;
};
console.log("Solo, one board, all 8 houses:");
for (const b of ["A", "B", "C", "D"]) {
  const aggs = await batch(H.map((h) => ({ games, players: 1, houses: [h], bot: "house", seed: 77, cfg: { boards: [b] } })));
  console.log(`  board ${b}: ${summarize(aggs)}`);
}
const pairs = [["galvan", "keel"], ["meridian", "vigil"], ["foremen", "tellers"], ["gardeners", "voidwardens"],
  ["galvan", "tellers"], ["keel", "vigil"], ["meridian", "voidwardens"], ["foremen", "gardeners"]];
console.log("Two players, consecutive board pairs, 8 house pairings:");
for (const bp of [["A", "B"], ["B", "C"], ["C", "D"]]) {
  const aggs = await batch(pairs.map((houses) => ({ games, players: 2, houses, bot: "house", seed: 78, cfg: { boards: bp } })));
  console.log(`  boards ${bp.join("-")}: ${summarize(aggs)}`);
}
