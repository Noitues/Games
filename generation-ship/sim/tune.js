// Parameter grid: node sim/tune.js --games 60 --grid purposePerPlayer=4,6,8 discoveriesPerTier=3,4
import { runBatch } from "./run.js";

const argv = process.argv.slice(2);
const games = Number(argv[argv.indexOf("--games") + 1] ?? 60);
const gi = argv.indexOf("--grid");
const axes = argv.slice(gi + 1).filter((a) => a.includes("=")).map((a) => {
  const [k, v] = a.split("="); return [k, v.split(",").map(Number)];
});
const pairings = [["galvan", "keel"], ["meridian", "vigil"], ["keel", "vigil"], ["galvan", "meridian"]];
const combos = axes.reduce((acc, [k, vs]) => acc.flatMap((c) => vs.map((v) => ({ ...c, [k]: v }))), [{}]);
console.log("config | win% | avg gens | win gen | wins at tier I/II/III");
for (const cfg of combos) {
  let G = 0, W = 0, gens = 0, wg = 0; const tiers = [0, 0, 0, 0];
  for (const houses of pairings) {
    const a = runBatch({ games, players: 2, houses, bot: "house", seed: 5, cfg });
    G += a.games; W += a.wins; gens += a.gens; wg += a.winGens;
    for (const [k, v] of Object.entries(a.causes)) { const m = k.match(/tier (\d)/); if (m) tiers[m[1]] += v; }
  }
  console.log(`${JSON.stringify(cfg)} | ${(100 * W / G).toFixed(0)}% | ${(gens / G).toFixed(1)} | ${(wg / Math.max(1, W)).toFixed(1)} | ${tiers.slice(1).map((t) => (100 * t / Math.max(1, W)).toFixed(0) + "%").join("/")}`);
}
