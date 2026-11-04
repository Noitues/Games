// Win rate at each destination level (adversary-style difficulty curve).
//   node sim/destinations.js --games 30 [--bot house] [--levels 0,1,2,3,4,5,6] [--dest verdant,cinder,longdark] [--landfall [shuffled]]
import { Worker } from "node:worker_threads";
import { fileURLToPath } from "node:url";

const argv = process.argv.slice(2);
const arg = (k, d) => { const i = argv.indexOf(`--${k}`); return i >= 0 ? argv[i + 1] : d; };
const games = Number(arg("games", 30)), bot = arg("bot", "house");
const levels = arg("levels", "0,1,2,3,4,5,6").split(",").map(Number);
const dests = arg("dest", "verdant,cinder,longdark").split(",");
// --landfall (Begin Landfall when ready) or --landfall shuffled (shuffled into Stage III)
const landfall = argv.includes("--landfall") ? (arg("landfall", "") === "shuffled" ? "shuffled" : true) : false;
const pairings = [["galvan", "keel"], ["meridian", "vigil"], ["foremen", "tellers"], ["gardeners", "voidwardens"]];
const worker = fileURLToPath(new URL("./parallel.js", import.meta.url));
const runJob = (job) => new Promise((res, rej) => {
  const w = new Worker(worker, { workerData: { job } }); w.on("message", (m) => res(m.agg)); w.on("error", rej);
});

console.log(`destination | level | win | win gen | main loss${landfall ? ` | Landfall: ${landfall === true ? "begin when ready" : landfall}` : ""}`);
const results = {};
for (const d of dests) for (const L of levels) {
  if (L === 0 && d !== dests[0]) { results[`${d}:0`] = results[`${dests[0]}:0`]; continue; }
  const cfg = { destination: L ? d : null, destinationLevel: L, landfallCard: landfall };
  const aggs = await Promise.all(pairings.map((houses) => runJob({ games, players: 2, houses, bot, seed: 41, cfg })));
  const G = aggs.reduce((n, a) => n + a.games, 0), Wn = aggs.reduce((n, a) => n + a.wins, 0);
  const causes = {};
  for (const a of aggs) for (const [k, v] of Object.entries(a.causes)) causes[k] = (causes[k] || 0) + v;
  const loss = Object.entries(causes).filter(([k]) => k.startsWith("loss")).sort((x, y) => y[1] - x[1])[0];
  const wg = aggs.reduce((n, a) => n + a.winGens, 0) / Math.max(1, Wn);
  results[`${d}:${L}`] = Wn / G;
  console.log(`${d} | ${L} | ${(100 * Wn / G).toFixed(0)}% | ${wg.toFixed(1)} | ${loss ? `${loss[0]} ${(100 * loss[1] / G).toFixed(0)}%` : "-"}`);
}
