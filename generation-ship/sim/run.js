// Monte Carlo runner.
//   node sim/run.js --games 200 --players 2 --houses galvan,keel --bot house [--seed 1] [--json out.json]
//   node sim/run.js --sweep --games 100 --bot house      (every 2-house pairing)
//   node sim/run.js --ladder --games 100                  (compare bot levels)
import { writeFileSync } from "node:fs";
import { loadData } from "./load.js";
import { playGame } from "../src/engine/game.js";
import { Bot, BOT_LEVELS } from "../src/ai/bots.js";

const args = Object.fromEntries(process.argv.slice(2).reduce((acc, a, i, arr) => {
  if (a.startsWith("--")) acc.push([a.slice(2), arr[i + 1] && !arr[i + 1].startsWith("--") ? arr[i + 1] : true]);
  return acc;
}, []));
const data = loadData();

export function runBatch({ games = 100, players = 2, houses = ["galvan", "keel"], bot = "house", pairing = "offset", seed = 1, cfg = {} }) {
  const level = BOT_LEVELS[bot] ?? Number(bot);
  const agg = { games, wins: 0, causes: {}, gens: 0, winGens: 0, decayPlaced: 0, crewLost: 0,
    destroyed: { glitch: 0, fault: 0, failure: 0 }, discApplied: 0, discBT: 0, tierAtEnd: [0, 0, 0, 0],
    houses: {} };
  for (let g = 0; g < games; g++) {
    const agents = houses.slice(0, players).map((_, i) => new Bot(level, seed * 1000 + g * 10 + i + 1));
    const st = playGame(data, agents, { ...cfg, players, houses, eventPairing: pairing }, seed * 100003 + g);
    const r = st.result;
    if (r.outcome === "win") { agg.wins++; agg.winGens += r.gen; }
    const key = r.outcome === "win" ? `win (${r.cause})` : `loss: ${r.cause}`;
    agg.causes[key] = (agg.causes[key] || 0) + 1;
    agg.gens += r.gen; agg.decayPlaced += st.stats.decayPlaced; agg.crewLost += st.stats.crewLost;
    for (const k in agg.destroyed) agg.destroyed[k] += st.stats.destroyed[k];
    agg.discApplied += st.stats.discoveryApplied; agg.discBT += st.stats.discoveryBreakthrough;
    agg.tierAtEnd[st.tier] += 1;
    for (const [n, [t, m]] of Object.entries(st.stats.thresholdByN || {})) {
      agg.thresholdByN ??= {}; agg.thresholdByN[n] ??= [0, 0];
      agg.thresholdByN[n][0] += t; agg.thresholdByN[n][1] += m;
    }
    for (const hs of st.stats.houses) {
      const a = (agg.houses[hs.id] ??= { games: 0, gensPlayed: 0, played: 0, creditsSpent: 0, innate: [0, 0, 0, 0],
        thresholdMet: 0, thresholdTried: 0, remarkables: 0, chosenLeader: 0, overclockFast: 0,
        growth: { A: 0, B: 0, C: 0 }, uncover: {} });
      a.games++; a.gensPlayed += r.gen; a.played += hs.played; a.creditsSpent += hs.creditsSpent;
      hs.innateTiers.forEach((n, i) => (a.innate[i] += n));
      a.thresholdMet += hs.thresholdMet; a.thresholdTried += hs.thresholdTried;
      a.remarkables += hs.remarkables; a.chosenLeader += hs.chosenLeader; a.overclockFast += hs.overclockFast;
      for (const k in hs.growth) a.growth[k] += hs.growth[k];
      hs.uncoverGens.forEach((gen, i) => { (a.uncover[i + 1] ??= []).push(gen); });
    }
  }
  return agg;
}

const pct = (a, b) => (b ? ((100 * a) / b).toFixed(1) + "%" : "-");
const avg = (a, b) => (b ? (a / b).toFixed(2) : "-");
export function report(agg, label) {
  const G = agg.games;
  console.log(`\n=== ${label} ===`);
  console.log(`win rate ${pct(agg.wins, G)} | avg length ${avg(agg.gens, G)} gens | avg win gen ${avg(agg.winGens, agg.wins)}`);
  console.log("outcomes:", Object.entries(agg.causes).sort((a, b) => b[1] - a[1]).map(([k, v]) => `${k} ${pct(v, G)}`).join(", "));
  console.log(`per game: Decay placed ${avg(agg.decayPlaced, G)}, Crew lost ${avg(agg.crewLost, G)}, destroyed G/F/X ${avg(agg.destroyed.glitch, G)}/${avg(agg.destroyed.fault, G)}/${avg(agg.destroyed.failure, G)}`);
  console.log(`Discoveries per game: applied ${avg(agg.discApplied, G)}, Breakthrough ${avg(agg.discBT, G)} | Understanding at end I/II/III: ${agg.tierAtEnd.slice(1).map((n) => pct(n, G)).join(" / ")}`);
  for (const [id, a] of Object.entries(agg.houses)) {
    const gp = a.gensPlayed, inn = a.innate, tot = inn.reduce((x, y) => x + y, 0);
    const unc = Object.entries(a.uncover).slice(0, 8).map(([i, arr]) => `${i}:g${(arr.reduce((x, y) => x + y, 0) / arr.length).toFixed(1)}`).join(" ");
    console.log(`  ${id.padEnd(9)} plays/gen ${avg(a.played, gp)} | credits/gen ${avg(a.creditsSpent, gp)} | innate none/I/II/III ${inn.map((n) => pct(n, tot)).join("/")} | card thresholds met ${pct(a.thresholdMet, a.thresholdTried)} | Remarkables/game ${avg(a.remarkables, a.games)} | leaders/game ${avg(a.chosenLeader, a.games)}${id === "galvan" ? ` | overclocked/gen ${avg(a.overclockFast, gp)}` : ""}`);
    console.log(`  ${"".padEnd(9)} growth A/B/C ${pct(a.growth.A, gp)}/${pct(a.growth.B, gp)}/${pct(a.growth.C, gp)} | uncover #:avg gen ${unc}`);
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const games = Number(args.games ?? 100), seed = Number(args.seed ?? 1), pairing = args.pairing ?? "offset";
  const out = {};
  const t0 = Date.now();
  if (args.ladder) {
    const houses = (args.houses ?? "galvan,keel").split(",");
    for (const bot of ["random", "tactician", "planner", "house"]) {
      out[bot] = runBatch({ games, players: houses.length, houses, bot, pairing, seed });
      report(out[bot], `${bot} bots | ${houses.join("+")}`);
    }
  } else if (args.sweep) {
    const H = ["galvan", "meridian", "keel", "vigil"], bot = args.bot ?? "house";
    for (let i = 0; i < H.length; i++) for (let j = i + 1; j < H.length; j++) {
      const houses = [H[i], H[j]];
      out[houses.join("+")] = runBatch({ games, players: 2, houses, bot, pairing, seed });
      report(out[houses.join("+")], `${bot} bots | ${houses.join("+")}`);
    }
  } else {
    const houses = (args.houses ?? "galvan,keel").split(","), bot = args.bot ?? "house";
    out.run = runBatch({ games, players: Number(args.players ?? houses.length), houses, bot, pairing, seed });
    report(out.run, `${bot} bots | ${houses.join("+")} | ${pairing}`);
  }
  console.log(`\n(${((Date.now() - t0) / 1000).toFixed(1)}s)`);
  if (args.json) writeFileSync(args.json, JSON.stringify(out, null, 1));
}
