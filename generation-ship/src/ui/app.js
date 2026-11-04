// Browser prototype: renders the engine state and lets humans and bots share the table.
// Human input uses phase replay: each phase runs from a snapshot; when a human decision is
// needed the run stops, the player answers, and the phase re-runs with the recorded answers.
import { createGame, makeContext, runPhase, PHASES, setupRamp, houseStats, houseData, card, eventTypes } from "../engine/game.js";
import { allSections, totalInfluence } from "../engine/rules.js";
import { Bot, BOT_LEVELS } from "../ai/bots.js";

const HOUSE_COLORS = ["#c0392b", "#2471a3", "#1e8449", "#8e44ad"];
const TYPE_FILL = { Infrastructure: "var(--infra)", Residential: "var(--resi)", Government: "var(--gov)", Agricultural: "var(--agri)" };
const SECTION_KINDS = new Set(["cardTarget", "innateTarget", "ventTo", "gatherFrom", "cascade", "moveInfluenceFrom",
  "growthInfluence", "influenceFor", "addCrewAt", "restoreAt", "breakthroughAt"]);
const $ = (id) => document.getElementById(id);
const clone = (x) => structuredClone(x);
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

// ------------------------------------------------------------------ data
async function loadData() {
  const get = async (f) => (await fetch(`data/${f}`)).json();
  const [people, events, discoveries, crisis, boards, houses] = await Promise.all(
    ["people.json", "events.json", "discoveries.json", "crisis.json", "boards.json", "houses.json"].map(get));
  let destinations = { destinations: [] };
  try { destinations = await get("destinations.json"); } catch { /* optional */ }
  const data = { people, events, discoveries, crisis, boards, houses, destinations };
  data.cardById = Object.fromEntries(people.map((c) => [c.id, c]));
  data.eventById = Object.fromEntries([...events.cards, events.landfall].map((e) => [e.id, e]));
  data.discoveryById = Object.fromEntries(discoveries.map((d) => [d.id, d]));
  data.houseById = Object.fromEntries(houses.houses.map((h) => [h.id, h]));
  return data;
}

// ------------------------------------------------------------------ human agent
class NeedInput { constructor(req) { this.req = req; } }
class Human {
  constructor(driver) { this.driver = driver; }
  choose(G, st, h, kind, options, ctx) { return this.driver.answer(h, kind, options, ctx); }
}

// ------------------------------------------------------------------ driver
class Driver {
  constructor(data, cfg, seats, seed) {
    this.data = data;
    this.agents = seats.map((s, i) => (s === "human" ? new Human(this) : new Bot(BOT_LEVELS[s], 100 + i)));
    const { st, cfg: full } = createGame(data, cfg, seed);
    this.G = makeContext(data, full, this.agents, true);
    setupRamp(this.G, st);
    this.st = st; this.phaseIdx = 0; this.answers = []; this.ptr = 0; this.pending = null;
    this.history = [];
  }
  botSeeds() { return this.agents.map((a) => a.seed); }
  answer(h, kind, options, ctx) {
    if (this.ptr < this.answers.length) return this.answers[this.ptr++];
    throw new NeedInput({ h, kind, options, ctx });
  }
  step() {
    if (this.st.result) return "done";
    if (!this.snapshot) {
      if (this.phaseIdx === 0) this.st.gen += 1;
      this.snapshot = { st: clone(this.st), seeds: this.botSeeds(), phaseIdx: this.phaseIdx };
      this.history.push(this.snapshot);
    }
    const st = clone(this.snapshot.st);
    this.agents.forEach((a, i) => { if (a instanceof Bot) a.seed = this.snapshot.seeds[i]; });
    this.ptr = 0;
    try {
      runPhase(this.G, st, PHASES[this.phaseIdx]);
    } catch (e) {
      if (!(e instanceof NeedInput)) throw e;
      this.st = st; this.pending = e.req;
      return "input";
    }
    this.st = st; this.pending = null; this.answers = []; this.snapshot = null;
    this.phaseIdx = (this.phaseIdx + 1) % PHASES.length;
    sfx(PHASES[this.phaseIdx]);
    return this.st.result ? "done" : "ok";
  }
  give(value) { this.answers.push(value); this.pending = null; return this.step(); }
  undo() {
    // drop the current (possibly partial) phase, then go back one more phase
    if (this.snapshot) this.history.pop();
    const prev = this.history.pop();
    if (!prev) return;
    this.st = clone(prev.st); this.phaseIdx = prev.phaseIdx; this.snapshot = null;
    this.agents.forEach((a, i) => { if (a instanceof Bot) a.seed = prev.seeds[i]; });
    if (this.phaseIdx === 0) this.st.gen -= 1;
    this.answers = []; this.pending = null;
  }
}

// ------------------------------------------------------------------ audio
let audio = null, muted = false;
function tone(freq, dur = 0.12, type = "sine", vol = 0.05) {
  if (muted) return;
  try {
    audio ??= new AudioContext();
    const o = audio.createOscillator(), g = audio.createGain();
    o.type = type; o.frequency.value = freq; g.gain.value = vol;
    o.connect(g); g.connect(audio.destination); o.start();
    g.gain.exponentialRampToValueAtTime(0.0001, audio.currentTime + dur); o.stop(audio.currentTime + dur);
  } catch { /* no audio */ }
}
function sfx(nextPhase) {
  const f = { growth: 440, commit: 494, fast: 523, dusk: 196, day: 330, dawn: 392, slow: 587, time: 262 }[nextPhase];
  if (f) tone(f, 0.1, nextPhase === "day" ? "triangle" : "sine");
}

// ------------------------------------------------------------------ rendering
let D = null, DATA = null, seats = [], autoTimer = null;
let commitSel = null; // {play:Set, nominee, fast:Set} for a human commit
let cloneSel = null;

function cardHTML(cid, extra = "") {
  const c = DATA.cardById[cid]; if (!c) return "";
  const t = c.target.kind === "house" ? "another house" : `range ${c.target.range}, ${c.target.type}`;
  const th = c.threshold ? `<div class="th">If ${Object.entries(c.threshold.elements).map(([g, n]) => `${g} ${n}`).join(" + ")}: also ${esc(c.threshold.text)}</div>` : "";
  return `<div class="card ${c.tier === "Remarkable" ? "rem" : ""} ${extra}" data-card="${cid}">
    <div class="hd"><span>${cid} ${c.tier === "Remarkable" ? "★" : ""}</span><span>${c.cost}¢</span></div>
    <div>${c.guilds.map((g) => `<span class="g">${g}</span>`).join("")}</div>
    <div><i>${esc(t)}</i>: ${esc(c.text)}</div>${th}
    <div class="r">Reign: ${esc(c.reign.text)}</div><div class="l">Legacy: ${esc(c.legacy.text)}</div></div>`;
}

function eventText(eid) {
  if (!eid) return "—";
  const e = DATA.eventById[eid];
  return `${e.id}: <b>${e.types.join(" + ")}</b>${e.twist ? ` <i>(${esc(e.twist.text)})</i>` : ""}`;
}

function render() {
  const st = D.st, G = D.G;
  const phase = D.snapshot ? PHASES[D.phaseIdx] : (st.result ? "end" : `next: ${PHASES[D.phaseIdx]}`);
  const cond = st.tier >= 3 ? "no Faults or Failures" : st.tier === 2 ? "no threat" : "no threat and no Decay";
  $("status").innerHTML = `Generation ${st.gen} · ${phase} · Events left ${st.decks.events.length} · Decay pool ${st.decayPool}${st.crisisFlipped ? ` (crisis ${st.crisisId})` : ""} · Purpose ${st.purpose}/${st.purposeCap} · Understanding ${["I", "II", "III"][st.tier - 1]} → win: ${cond}${st.landfallPlaced ? " · Landfall under way" : ""}`;
  renderConveyor(); renderMap(); renderHouses(); renderWall(); renderPrompt();
  $("log").innerHTML = st.log.slice(-80).map((l) => `<li>${esc(l)}</li>`).join("");
  $("log").scrollTop = 1e9;
}

function renderConveyor() {
  const st = D.st;
  const slot = (name, L) => `<div class="slot"><b>${name}</b><br>${L ? `${eventText(L.event)}${L.tempered ? " · tempered" : ""}${L.bt ? ` · Breakthrough ${L.bt}` : ""}${cardHTML(L.leader)}` : "<i>empty</i>"}</div>`;
  $("conveyor").innerHTML = slot("Dusk: Elder (Legacy, then Collapse)", st.slots.dusk) + slot("Day: Steward (Reign, then Grow)", st.slots.day) +
    slot("Dawn: Heir (Seed)", st.slots.dawn) + (st.upcomingEvent ? `<div class="slot">Next event: ${eventText(st.upcomingEvent)}</div>` : "");
  const dest = st.dest?.id ? `<div class="slot"><b>${esc(st.dest.name)}</b><br>${st.dest.texts.map(esc).join("<br>")}${st.escalationEvent ? `<br><i>Escalation card: ${st.escalationEvent}</i>` : ""}</div>` : "";
  $("conveyor").innerHTML += dest;
  $("discoveries").innerHTML = `Earned ${st.discoveriesEarned}; pending ${st.pendingDiscoveries.length}<br>` +
    (st.breakthroughs.length ? "Breakthroughs: " + st.breakthroughs.map((d) => `<div class="slot">${esc(DATA.discoveryById[d].breakthrough.text)}</div>`).join("") : "");
}

function renderMap() {
  const st = D.st, W = 150, H = 118, gap = 24;
  const P = st.houses.length;
  const opts = D.pending && SECTION_KINDS.has(D.pending.kind) ? new Set(D.pending.options.map((o) => String(o).replace("*", ""))) : new Set();
  const pos = {};
  for (const id of st.order) {
    const s = st.sections[id], bi = "ABCD".indexOf(s.board);
    const col = (+id.slice(1) - 1) % 4, row = Math.floor((+id.slice(1) - 1) / 4);
    pos[id] = { x: 10 + bi * (4 * W + gap) + col * W, y: 10 + row * H };
  }
  let svg = "";
  const seen = new Set();
  for (const id of st.order) for (const a of st.sections[id].adj) {
    const k = [id, a].sort().join("-"); if (seen.has(k)) continue; seen.add(k);
    const p = pos[id], q = pos[a];
    svg += `<line class="edge" x1="${p.x + W / 2}" y1="${p.y + H / 2}" x2="${q.x + W / 2}" y2="${q.y + H / 2}"/>`;
  }
  for (const id of st.order) {
    const s = st.sections[id], p = pos[id];
    const inf = Object.entries(s.influence).filter(([, n]) => n > 0)
      .map(([h, n]) => `<tspan fill="${HOUSE_COLORS[h]}">●${n > 1 ? n : ""}</tspan>`).join(" ");
    const tok = [s.brace && `Br${s.brace}`, s.quarantine && "Q", s.patch && `P${s.patch}`, s.lockout && `L${s.lockout}`,
      s.unrest && `U${s.unrest}`, s.isolate && `I${s.isolate}`].filter(Boolean).join(" ");
    const threat = [s.glitch && `▲${s.glitch}`, s.fault && `■${s.fault}`, s.failure && `⬢${s.failure}`].filter(Boolean).join(" ");
    svg += `<g class="sec ${opts.has(id) ? "opt" : ""}" data-id="${id}">
      <rect x="${p.x + 3}" y="${p.y + 3}" width="${W - 6}" height="${H - 6}" rx="6" fill="${TYPE_FILL[s.type]}"/>
      ${s.hull ? `<line class="hull" x1="${p.x + 6}" y1="${p.y + 4}" x2="${p.x + W - 6}" y2="${p.y + 4}"/>` : ""}
      <text x="${p.x + 10}" y="${p.y + 22}"><tspan font-weight="700">${id}</tspan> ${s.type.slice(0, 5)}</text>
      <text x="${p.x + 10}" y="${p.y + 44}" font-size="15">${threat || "·"}</text>
      <text x="${p.x + 10}" y="${p.y + 64}">${s.crew ? `☺${s.crew}` : ""} ${s.decay ? `✸${s.decay}` : ""}</text>
      <text x="${p.x + 10}" y="${p.y + 84}" font-size="14">${inf}</text>
      <text x="${p.x + 10}" y="${p.y + 104}" font-size="11">${tok}</text></g>`;
  }
  const map = $("map");
  map.setAttribute("width", 20 + P * (4 * W + gap)); map.setAttribute("height", 20 + 2 * H);
  map.innerHTML = svg;
  map.querySelectorAll(".sec.opt").forEach((g) => g.addEventListener("click", () => {
    const id = g.dataset.id;
    const o = D.pending.options.find((x) => String(x).replace("*", "") === id);
    act(o);
  }));
}

function trackHTML(track, pos) {
  return track.map((v, i) => {
    const t = typeof v === "object" ? "★" + (v.element || (v.fast_play ? "fast" : v.clone ? "clone" : "")) : v;
    return i <= pos ? `<b>${t}</b>` : `<span style="opacity:.5">${t}</span>`;
  }).join(" → ");
}

function renderHouses() {
  const st = D.st, G = D.G;
  $("houses").innerHTML = st.houses.map((H, h) => {
    const hd = houseData(G, st, h), hs = houseStats(G, st, h);
    const el = Object.entries(H.elements || {}).filter(([, n]) => n).map(([g, n]) => `${g} ${n}`).join(", ") || "—";
    const tiers = hd.innate.tiers.map((t) => `T${t.tier}: ${Object.entries(t.threshold).map(([g, n]) => `${g} ${n}`).join("+")} → ${Object.entries(t.effects).map(([k, v]) => `${k} ${v}`).join(", ")}`).join("<br>");
    const human = seats[h] === "human";
    const pend = D.pending && D.pending.h === h;
    let hand = "";
    if (pend && D.pending.kind === "commit") {
      hand = H.hand.map((c) => cardHTML(c, commitSel.play.has(c) ? "sel" : "")).join("");
    } else if (pend && D.pending.kind === "clone") {
      hand = H.hand.map((c) => cardHTML(c, cloneSel.has(c) ? "sel" : "")).join("");
    } else {
      hand = H.hand.map((c) => cardHTML(c)).join("") + (H.played.length ? `<div class="stats">Played: ${H.played.join(", ")}${H.nominee ? ` (nominee ${H.nominee})` : ""}</div>` : "");
    }
    return `<div class="house" style="--hc:${HOUSE_COLORS[h]}"><b>${esc(hd.name)}</b> <span class="stats">${human ? "Human" : seats[h]}</span>
      <div class="stats">Credits ${H.credits} (+${hs.income}/gen) · plays ${hs.plays} · hand ${hs.hand} · clone ${hs.clone} · influence ${totalInfluence(st, h)}</div>
      <div class="stats">Credits track: ${trackHTML(hd.tracks.credits, H.track.credits)}<br>Plays track: ${trackHTML(hd.tracks.plays, H.track.plays)}</div>
      <div class="stats">Elements: ${el}</div>
      <details><summary class="stats">${esc(hd.innate.name)} (${hd.innate.speed}) · ${esc(hd.special.text)}</summary><div class="stats">${tiers}</div></details>
      <div class="hand">${hand}</div></div>`;
  }).join("");
  document.querySelectorAll("#houses .card[data-card]").forEach((el) => el.addEventListener("click", () => {
    if (!D.pending) return;
    const cid = el.dataset.card;
    if (D.pending.kind === "commit") { commitSel.play.has(cid) ? commitSel.play.delete(cid) : commitSel.play.add(cid); if (!commitSel.play.has(commitSel.nominee)) commitSel.nominee = [...commitSel.play][0] ?? null; render(); }
    if (D.pending.kind === "clone") { cloneSel.has(cid) ? cloneSel.delete(cid) : cloneSel.size < D.pending.ctx.slots && cloneSel.add(cid); render(); }
  }));
}

function renderWall() {
  const st = D.st;
  const n = st.wallSize ?? 13;
  let html = "";
  for (let i = 0; i < n; i++) {
    const w = st.wall[i];
    html += w ? `<div class="ws full">${i + 1}. ${w.leader}<br>${DATA.eventById[w.event].types.join("+")}${w.bt ? `<br>★ ${w.bt}` : ""}</div>` : `<div class="ws">${i + 1}.</div>`;
  }
  $("wall").innerHTML = html;
}

const KIND_TEXT = {
  growth: "Choose a growth option", track: "Uncover which track?", remarkables: "Take a Remarkable instead of 2 Commons?",
  commit: "Choose your plays", cardTarget: "Choose a target for", innateTarget: "Choose a target for your innate power",
  ventTo: "Vent to which adjacent section?", gatherFrom: "Gather Crew from which section?", cascade: "Decay cascades: choose an adjacent section",
  moveInfluenceFrom: "Move influence from which section?", growthInfluence: "Place influence where?", influenceFor: "Place that house's influence where?",
  addCrewAt: "Add Crew where?", restoreAt: "Restore Decay where?", breakthroughAt: "Breakthrough: choose a section",
  vote: "Vote for the next heir", discovery: "Discovery", clone: "Clone cards into the next generation", landfall: "Begin Landfall?",
};

function renderPrompt() {
  const p = $("prompt"), st = D.st, G = D.G;
  if (st.result) {
    p.className = ""; p.innerHTML = `<span class="banner ${st.result.outcome}">${st.result.outcome === "win" ? "Victory" : "Defeat"}: ${esc(st.result.cause)} in generation ${st.result.gen}</span>`;
    return;
  }
  if (!D.pending) { p.className = "idle"; p.textContent = autoTimer ? "Running…" : "Press Step (or Auto) to continue."; return; }
  p.className = "";
  const { h, kind, options, ctx } = D.pending;
  const who = `<b style="color:${HOUSE_COLORS[h]}">${esc(houseData(G, st, h).name)}</b>: `;
  let body = "";
  if (kind === "growth") {
    const hd = houseData(G, st, h);
    const desc = { A: `Place influence (range ${hd.growth_overrides?.A?.range ?? 1}) and uncover a track slot`, B: "Gain 2 credits + house perk", C: "Draw +2 cards and gain 1 credit (Vigil: +1 Purpose)" };
    body = options.map((o) => `<button data-o="${o}">${o}: ${desc[o]}</button>`).join("");
  } else if (kind === "commit") {
    const H = st.houses[h];
    const sel = [...commitSel.play];
    const cost = sel.reduce((n, c) => n + (c === commitSel.nominee ? 0 : card(G, c).cost), 0);
    body = `Select up to ${ctx.plays} cards in your hand (click them). Cost ${cost}¢ of ${H.credits}¢ (the nominee is free).<br>
      Nominee (fast, may become heir): <select id="nom">${sel.map((c) => `<option ${c === commitSel.nominee ? "selected" : ""}>${c}</option>`).join("")}</select>
      Extra fast: ${sel.filter((c) => c !== commitSel.nominee).map((c) => `<label><input type="checkbox" class="fx" value="${c}" ${commitSel.fast.has(c) ? "checked" : ""}>${c}</label>`).join(" ") || "—"}
      <button id="commit-ok" class="primary" ${sel.length > ctx.plays || cost > H.credits ? "disabled" : ""}>Commit</button>`;
  } else if (kind === "clone") {
    body = `Select up to ${ctx.slots} card(s) in your hand to keep. <button id="clone-ok" class="primary">Done</button>`;
  } else if (kind === "vote") {
    body = options.map((o) => `<div style="max-width:260px">${cardHTML(o)}<button data-o="${o}">Vote ${o}</button></div>`).join("");
  } else if (kind === "discovery") {
    const d = DATA.discoveryById[ctx.id], t = d.tiers[["I", "II", "III"][st.tier - 1]];
    body = `${d.id} (${d.family}).<br><button data-o="apply">Apply now: ${esc(t.text)}</button> <button data-o="breakthrough">Breakthrough on the Steward: ${esc(d.breakthrough.text)}</button>`;
  } else if (SECTION_KINDS.has(kind)) {
    const extra = kind === "cardTarget" ? ` <b>${ctx.card}</b>: ${esc(card(G, ctx.card).text)}` : "";
    const nonSec = options.filter((o) => typeof o === "number" || o === "global");
    body = `${extra}<br>Click a highlighted section on the map${options.some((o) => String(o).endsWith("*")) ? " (Voices Among the Crew targets cost 1 credit)" : ""}.` +
      nonSec.map((o) => `<button data-o="${o}">${typeof o === "number" ? esc(st.houses[o].id) : "Resolve"}</button>`).join("");
  } else {
    body = options.map((o) => `<button data-o="${o}">${esc(String(o))}</button>`).join("");
  }
  p.innerHTML = `${who}${KIND_TEXT[kind] ?? kind}<div class="opts">${body}</div>`;
  p.querySelectorAll("button[data-o]").forEach((b) => b.addEventListener("click", () => {
    const raw = b.dataset.o; const o = options.find((x) => String(x) === raw);
    act(o);
  }));
  $("nom")?.addEventListener("change", (e) => { commitSel.nominee = e.target.value; render(); });
  p.querySelectorAll(".fx").forEach((x) => x.addEventListener("change", () => { x.checked ? commitSel.fast.add(x.value) : commitSel.fast.delete(x.value); }));
  $("commit-ok")?.addEventListener("click", () => {
    const play = [...commitSel.play];
    act({ play, nominee: play.length ? commitSel.nominee : null, fast: [...commitSel.fast].filter((c) => play.includes(c)) });
  });
  $("clone-ok")?.addEventListener("click", () => act([...cloneSel]));
}

function act(value) {
  const r = D.give(value);
  afterStep(r);
}
function afterStep(r) {
  commitSel = null; cloneSel = null;
  if (r === "input") {
    if (D.pending.kind === "commit") commitSel = { play: new Set(), nominee: null, fast: new Set() };
    if (D.pending.kind === "clone") cloneSel = new Set();
    stopAuto();
  }
  if (r === "done") { stopAuto(); tone(D.st.result.outcome === "win" ? 660 : 150, 0.6, "triangle", 0.08); }
  render();
}
function stopAuto() { if (autoTimer) { clearInterval(autoTimer); autoTimer = null; $("btn-auto").textContent = "Auto"; } }

// ------------------------------------------------------------------ setup screen
function renderSeats() {
  const P = +$("players").value;
  const houses = DATA.houses.houses;
  const prev = [...document.querySelectorAll(".seat")].map((s) => [s.querySelector(".h").value, s.querySelector(".c").value]);
  $("seats").innerHTML = Array.from({ length: P }, (_, i) => `<div class="seat"><span style="color:${HOUSE_COLORS[i]}">●</span> Seat ${i + 1}
    <select class="h">${houses.map((h, j) => `<option value="${h.id}" ${(prev[i]?.[0] ?? houses[i].id) === h.id ? "selected" : ""}>${esc(h.name)} (${h.template})</option>`).join("")}</select>
    <select class="c">${["human", "team", "house", "planner", "tactician"].map((c) => `<option ${(prev[i]?.[1] ?? (i === 0 ? "human" : "team")) === c ? "selected" : ""}>${c}</option>`).join("")}</select></div>`).join("");
}
function renderDestinations() {
  const ds = DATA.destinations.destinations || [];
  $("destination").innerHTML = `<option value="">None (level 0)</option>` + ds.map((d) => `<option value="${d.id}">${esc(d.name)}</option>`).join("");
  $("level").innerHTML = [0, 1, 2, 3, 4, 5, 6].map((l) => `<option>${l}</option>`).join("");
}

function start() {
  const P = +$("players").value;
  const seatEls = [...document.querySelectorAll(".seat")];
  const houses = seatEls.map((s) => s.querySelector(".h").value);
  seats = seatEls.map((s) => s.querySelector(".c").value);
  const cfg = { players: P, houses, eventPairing: $("pairing").value, tierConditions: $("tiers").value,
    destination: $("destination").value || null, destinationLevel: +$("level").value, landfallCard: $("landfall").checked };
  D = new Driver(DATA, cfg, seats, +$("seed").value || 1);
  $("setup").hidden = true; $("game").hidden = false;
  render();
}

async function main() {
  DATA = await loadData();
  renderSeats(); renderDestinations();
  $("players").addEventListener("change", renderSeats);
  $("btn-start").addEventListener("click", start);
  $("btn-new").addEventListener("click", () => { stopAuto(); $("setup").hidden = false; $("game").hidden = true; });
  $("btn-step").addEventListener("click", () => { if (D && !D.pending) afterStep(D.step()); });
  $("btn-auto").addEventListener("click", () => {
    if (!D) return;
    if (autoTimer) return stopAuto();
    $("btn-auto").textContent = "Pause";
    autoTimer = setInterval(() => { if (D.pending || D.st.result) return stopAuto(); afterStep(D.step()); }, 350);
  });
  $("btn-undo").addEventListener("click", () => { if (D) { stopAuto(); D.undo(); afterStep(null); } });
  $("btn-mute").addEventListener("click", () => { muted = !muted; $("btn-mute").textContent = muted ? "🔇" : "🔊"; });
}
main();
