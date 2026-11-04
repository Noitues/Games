// Self-play tuning of the bots' evaluation weights (coordinate search, common random numbers).
//   node sim/tune-weights.js --games 40 --bot house --passes 1
import { Worker } from "node:worker_threads";
import { fileURLToPath } from "node:url";
import { writeFileSync } from "node:fs";
import { W } from "../src/ai/eval.js";

const argv = process.argv.slice(2);
const arg = (k, d) => { const i = argv.indexOf(`--${k}`); return i >= 0 ? argv[i + 1] : d; };
const games = Number(arg("games", 40)), bot = arg("bot", "house"), passes = Number(arg("passes", 1));
const pairings = [["galvan", "keel"], ["meridian", "vigil"], ["keel", "vigil"], ["galvan", "meridian"]];
const worker = fileURLToPath(new URL("./parallel.js", import.meta.url));

function runJob(job) {
  return new Promise((res, rej) => {
    const w = new Worker(worker, { workerData: { job } });
    w.on("message", (m) => res(m.agg)); w.on("error", rej);
  });
}
async function score(weights) {
  const aggs = await Promise.all(pairings.map((houses) => runJob({ games, players: 2, houses, bot, seed: 77, weights })));
  return aggs.reduce((n, a) => n + a.wins, 0) / aggs.reduce((n, a) => n + a.games, 0);
}

let best = { ...W };
let bestScore = await score(best);
console.log(`baseline ${(100 * bestScore).toFixed(1)}%`);
const keys = Object.keys(W).filter((k) => k !== "win");
for (let p = 0; p < passes; p++) for (const k of keys) {
  for (const f of [0.6, 1.6]) {
    const cand = { ...best, [k]: +(best[k] * f).toFixed(3) };
    const s = await score(cand);
    const mark = s > bestScore + 0.02 ? "  <- keep" : "";
    console.log(`${k} x${f}: ${(100 * s).toFixed(1)}%${mark}`);
    if (mark) { best = cand; bestScore = s; break; }
  }
}
console.log("best", JSON.stringify(best), `${(100 * bestScore).toFixed(1)}%`);
writeFileSync(new URL("./weights.json", import.meta.url), JSON.stringify(best, null, 1));
