// Parallel pairing sweep over worker threads, with per-house strength summary.
//   node sim/parallel.js --houses galvan,meridian,keel,vigil --games 100 --players 2 --threads 4
//        [--bot house] [--seed 1] [--pairing offset] [--cfg '{"purposePerPlayer":4}'] [--json out.json]
import { Worker, isMainThread, parentPort, workerData } from "node:worker_threads";
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

if (!isMainThread) {
  const { runBatch } = await import("./run.js");
  const { job } = workerData;
  if (job.weights) Object.assign((await import("../src/ai/eval.js")).W, job.weights);
  parentPort.postMessage({ key: job.houses.join("+"), agg: runBatch(job) });
} else {
  const args = Object.fromEntries(process.argv.slice(2).reduce((acc, a, i, arr) => {
    if (a.startsWith("--")) acc.push([a.slice(2), arr[i + 1] && !arr[i + 1].startsWith("--") ? arr[i + 1] : true]);
    return acc;
  }, []));
  const H = (args.houses ?? "galvan,meridian,keel,vigil,foremen,gardeners,voidwardens,tellers").split(",");
  const P = Number(args.players ?? 2), games = Number(args.games ?? 100), threads = Number(args.threads ?? 4);
  const cfg = args.cfg ? JSON.parse(args.cfg) : {};
  const combos = [];
  const rec = (i, cur) => { if (cur.length === P) { combos.push([...cur]); return; }
    for (let j = i; j < H.length; j++) { cur.push(H[j]); rec(j + 1, cur); cur.pop(); } };
  rec(0, []);
  // --swap: also play every combination in reversed seat order (houses swap boards)
  if (args.swap) combos.push(...combos.map((c) => [...c].reverse()));
  if (args.sample) {
    // deterministic sample of combos (for 3-4 player runs with many combinations)
    let x = 12345;
    const rnd = () => ((x = (x * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff);
    for (let i = combos.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [combos[i], combos[j]] = [combos[j], combos[i]]; }
    combos.splice(Number(args.sample));
  }
  const weights = args.weights ? JSON.parse(args.weights.startsWith("{") ? args.weights : (await import("node:fs")).readFileSync(args.weights, "utf8")) : undefined;
  const jobs = combos.map((houses) => ({ games, players: P, houses, bot: args.bot ?? "house",
    pairing: args.pairing ?? "offset", seed: Number(args.seed ?? 1), cfg, weights }));
  const results = {};
  const t0 = Date.now();
  await new Promise((resolve) => {
    let next = 0, running = 0;
    const launch = () => {
      if (next >= jobs.length) { if (!running) resolve(); return; }
      const job = jobs[next++]; running++;
      const w = new Worker(fileURLToPath(import.meta.url), { workerData: { job } });
      w.on("message", (m) => {
        const key = m.key.split("+").sort().join("+");
        if (!results[key]) { results[key] = m.agg; return; }
        const a = results[key], b = m.agg;
        a.games += b.games; a.wins += b.wins; a.winGens += b.winGens; a.gens += b.gens;
        for (const [k, v] of Object.entries(b.causes)) a.causes[k] = (a.causes[k] || 0) + v;
        for (const [h, x] of Object.entries(b.houses)) {
          const y = (a.houses[h] ??= { ...x, innate: [...x.innate] });
          if (y === x) continue;
          y.gensPlayed += x.gensPlayed; y.played += x.played; y.creditsSpent += x.creditsSpent;
          x.innate.forEach((n, i) => (y.innate[i] += n));
        }
      });
      w.on("error", (e) => { console.error(job.houses.join("+"), e); });
      w.on("exit", () => { running--; launch(); });
    };
    for (let i = 0; i < threads; i++) launch();
  });
  const rows = Object.entries(results).map(([k, a]) => {
    const t3 = Object.entries(a.causes).filter(([c]) => c.includes("tier 3")).reduce((n, [, v]) => n + v, 0);
    const dec = a.causes["loss: decay"] || 0, time = a.causes["loss: time"] || 0;
    return { k, win: a.wins / a.games, gen: a.winGens / Math.max(1, a.wins), t3: t3 / Math.max(1, a.wins),
      dec: dec / a.games, time: time / a.games, a };
  }).sort((x, y) => y.win - x.win);
  const pct = (x) => (100 * x).toFixed(0) + "%";
  console.log(`players ${P} | ${games} games per combo | cfg ${JSON.stringify(cfg)} | ${args.pairing ?? "offset"}`);
  console.log("combo | win | win gen | wins at tier III | Decay loss | time loss");
  for (const r of rows) console.log(`${r.k} | ${pct(r.win)} | ${r.gen.toFixed(1)} | ${pct(r.t3)} | ${pct(r.dec)} | ${pct(r.time)}`);
  const strength = {};
  for (const r of rows) for (const h of r.k.split("+")) (strength[h] ??= []).push(r.win);
  const mean = rows.reduce((n, r) => n + r.win, 0) / rows.length;
  console.log(`\noverall win ${pct(mean)}`);
  console.log("house | avg win of its combos | vs overall | innate none/I/II/III | plays/gen | credits/gen");
  for (const [h, ws] of Object.entries(strength).sort((x, y) => y[1].reduce((a, b) => a + b) / y[1].length - x[1].reduce((a, b) => a + b) / x[1].length)) {
    const w = ws.reduce((a, b) => a + b) / ws.length;
    let inn = [0, 0, 0, 0], gp = 0, pl = 0, cr = 0;
    for (const r of rows) { const hs = r.a.houses[h]; if (!hs) continue; hs.innate.forEach((n, i) => (inn[i] += n)); gp += hs.gensPlayed; pl += hs.played; cr += hs.creditsSpent; }
    const tot = inn.reduce((a, b) => a + b);
    console.log(`${h} | ${pct(w)} | ${((w - mean) * 100).toFixed(1)} | ${inn.map((n) => pct(n / tot)).join("/")} | ${(pl / gp).toFixed(2)} | ${(cr / gp).toFixed(2)}`);
  }
  console.log(`\n(${((Date.now() - t0) / 1000).toFixed(0)}s)`);
  if (args.json) writeFileSync(args.json, JSON.stringify({ cfg, rows: rows.map(({ a, ...r }) => r), strength }, null, 1));
}
