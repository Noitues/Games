// Browser prototype: renders the engine state and lets humans and bots share the table.
// Human input uses phase replay: each phase runs from a snapshot; when a human decision is
// needed the run stops, the player answers, and the phase re-runs with the recorded answers.
import { createGame, makeContext, runPhase, PHASES, setupRamp, houseStats, houseData, card, eventTypes, needsTarget, discoveryTier, nomineeCost } from "../engine/game.js";
import { allSections, totalInfluence, wallBonuses, stewardHouse, legacyMod } from "../engine/rules.js";
import { Bot, BOT_LEVELS } from "../ai/bots.js";
import { predictedCollapse } from "../ai/eval.js";

const HOUSE_COLORS = ["#c0392b", "#2471a3", "#1e8449", "#8e44ad"];
const TYPE_FILL = { Infrastructure: "var(--infra)", Residential: "var(--resi)", Government: "var(--gov)", Agricultural: "var(--agri)" };
const SECTION_KINDS = new Set(["cardTarget", "innateTarget", "ventTo", "gatherFrom", "cascade", "moveInfluenceFrom",
  "growthInfluence", "influenceFor", "addCrewAt", "restoreAt", "discoveryAt"]);
// Non-section answers that can appear among section options.
const SKIP_TEXT = { stay: "Don't vent (leave it here)", none: "Don't gather", global: "Resolve" };
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
  // Undo the most recent decision in this phase by replaying the phase without it.
  undoDecision() {
    if (!this.snapshot || !this.answers.length) return false;
    this.answers.pop();
    this.pending = null;
    return this.step();
  }
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

function targetText(c) {
  const base = needsTarget(c, c.effects);
  const full = c.threshold ? needsTarget(c, { ...c.effects, ...c.threshold.effects }) : base;
  const where = c.target.kind === "house" ? "another house" : `range ${c.target.range}, ${c.target.type}`;
  if (base) return where;
  if (full) return `no target (bonus: ${where})`;
  return "no target";
}
function cardHTML(cid, extra = "") {
  const c = DATA.cardById[cid]; if (!c) return "";
  const th = c.threshold ? `<div class="th">If ${Object.entries(c.threshold.elements).map(([g, n]) => `${g} ${n}`).join(" + ")}: also ${esc(c.threshold.text)}</div>` : "";
  return `<div class="card ${c.tier === "Remarkable" ? "rem" : ""} ${extra}" data-card="${cid}">
    <div class="hd"><span>${cid} ${c.tier === "Remarkable" ? "★" : ""}</span><span>${c.cost}¢</span></div>
    <div>${c.guilds.map((g) => `<span class="g">${g}</span>`).join("")}</div>
    <div><i>${esc(targetText(c))}</i>: ${esc(c.text)}</div>${th}
    <div class="rl"><div class="r">Reign: ${esc(c.reign.text)}</div><div class="l">Legacy: ${esc(c.legacy.text)}</div></div></div>`;
}

function eventText(eid) {
  if (!eid) return "no event (the voyage is ending)";
  const e = DATA.eventById[eid];
  return `${e.id}: <b>${e.types.join(" + ")}</b>${e.twist ? ` <i>(${esc(e.twist.text)})</i>` : ""}`;
}

// What each phase does, shown in the status line and the idle prompt.
const PHASE_GUIDE = {
  growth: "Growth: each house picks A/B/C, gains credits, and draws a fresh hand.",
  commit: "Commit: choose your plays and pay for them. One card is your fast nominee (a candidate heir); it costs 3 credits less, so Commons are free.",
  fast: "Fast: nominees (and other fast plays) resolve before Dusk.",
  dusk: "Dusk: Discoveries earned before this Dusk resolve, Wall bonuses apply, then the Elder's Legacy, then the Elder's event Collapses.",
  day: "Day: the Steward's Reign applies, then the Steward's event Grows.",
  dawn: "Dawn: vote an heir from the nominees; the next event is drawn and Seeds.",
  slow: "Slow: all other played cards and slow innates resolve, in the order each house chooses.",
  time: "Time passes: Dusk → Wall (its Breakthrough switches on), Day → Dusk, Dawn → Day; hands are discarded (except clones).",
};

// Which events act next, judged by the phase about to run (or running).
function forecastEvents() {
  const st = D.st, idx = D.phaseIdx, ev = (slot) => slot && slot.event && DATA.eventById[slot.event];
  if (idx <= 3) return { collapse: ev(st.slots.dusk), grow: ev(st.slots.day), when: "this Dusk" };
  if (idx === 4) return { collapse: ev(st.slots.day), grow: ev(st.slots.day), when: "next Dusk" };
  return { collapse: ev(st.slots.day), grow: ev(st.slots.dawn), when: "next Dusk" };
}
const matchesEv = (s, e) => e && e.types.some((t) => t === "ALL" || t === s.type || (t === "Hull" && s.hull));
function forecast() {
  const st = D.st, { collapse, grow, when } = forecastEvents(), out = {};
  for (const id of st.order) {
    const s = st.sections[id], threat = s.glitch + s.fault + s.failure, f = {};
    if (threat && matchesEv(s, collapse)) {
      let d = predictedCollapse(s, st);
      if (collapse.twist?.rule === "faults_plus_one") d += s.fault;
      if (s.hull && st.dest?.rules?.hull_collapse_plus) d += 1;
      f.collapse = d; f.decay = d >= D.G.cfg.decayThreshold; f.crew = Math.min(s.crew, Math.floor(d / D.G.cfg.crewHealth));
    }
    if (threat && matchesEv(s, grow)) f.grow = s.patch ? "patched" : s.fault >= 2 ? "Failure" : "Fault";
    if (Object.keys(f).length) out[id] = f;
  }
  return { out, collapse, grow, when };
}

function render() {
  const st = D.st, G = D.G;
  const phase = D.snapshot ? PHASES[D.phaseIdx] : (st.result ? "end" : `next: ${PHASES[D.phaseIdx]}`);
  const cond = st.tier >= 3 ? "no Faults or Failures" : st.tier === 2 ? "no threat" : "no threat and no Decay";
  const nowPhase = PHASES[D.phaseIdx];
  $("phase-guide").textContent = st.result ? "" : (D.snapshot ? "Now — " : "Next — ") + PHASE_GUIDE[nowPhase];
  $("status").innerHTML = `Generation ${st.gen} · ${phase} · Events left ${st.decks.events.length} · Decay pool ${st.decayPool}${st.crisisFlipped ? ` (crisis ${st.crisisId})` : ""} · Understanding ${["I", "II", "III"][st.tier - 1]} → win: ${cond}${st.landfallPlaced ? " · Landfall under way" : ""}`;
  renderPurpose(); renderConveyor(); renderEffects(); renderForecast(); renderMap(); renderHouses(); renderWall(); renderPrompt();
  $("log").innerHTML = st.log.slice(-80).map((l) => `<li>${esc(l)}</li>`).join("");
  $("log").scrollTop = 1e9;
}

// Purpose meter: progress to the next Discovery, Discoveries toward the next Understanding.
function renderPurpose() {
  const st = D.st, per = st.discoveriesPerTier ?? D.G.cfg.discoveriesPerTier;
  const pct = Math.round((100 * st.purpose) / st.purposeCap);
  const toTier = st.tier >= 3 ? "Understanding III (max)" : `${per * st.tier - st.discoveriesEarned} more for Understanding ${["II", "III"][st.tier - 1]}`;
  $("purpose").innerHTML = `<div class="meter"><div style="width:${pct}%"></div><span>Purpose ${st.purpose} / ${st.purposeCap}</span></div>
    <div class="muted">${st.purposeCap - st.purpose} more Purpose earns a Discovery · Discoveries earned ${st.discoveriesEarned} (${toTier})${st.pendingDiscoveries.length ? ` · <b>${st.pendingDiscoveries.length} waiting for Dusk</b>` : ""}<br>
    Purpose comes from destroying Faults (+${D.G.cfg.purposeFault}) and Failures (+${D.G.cfg.purposeFailure}), cards, Reigns and innates. It is shared by the whole ship.</div>`;
}

// Which house put a leader forward (the starting leader has none).
function houseTag(h) {
  return h == null ? `<span class="htag" style="--hc:var(--muted)">no house</span>` : `<span class="htag" style="--hc:${HOUSE_COLORS[h]}">${esc(D.st.houses[h]?.id ?? "")}</span>`;
}
const LEGACY_WORDS = { crew_fierce: "Crew +{n} damage", brace_dusk: "Brace {n} each Dusk", repair_plus: "+{n} damage from powers", purpose_plus: "+{n} Purpose per Fault/Failure destroyed",
  collapse_plus: "Collapse +{n} damage", seed_plus: "Seed +{n} Glitch", grow_glitch: "Grow adds {n} Glitch", crew_frail: "Crew {n} less health", credits_tax: "every house -{n} credit each Growth", purpose_tax: "-{n} Purpose each Dusk" };
const legacyText = (eff) => Object.entries(eff).map(([k, n]) => (LEGACY_WORDS[k] || k).replace("{n}", n)).join("; ");

// Everything in effect right now that isn't on a card in someone's hand.
function renderEffects() {
  const st = D.st, G = D.G, wb = wallBonuses(G, st), rows = [];
  const el = Object.entries(wb.elements).map(([g, n]) => `+${n} ${g}`).join(", ");
  if (el) rows.push(`<b>Wall:</b> every house counts ${el} element${Object.keys(wb.elements).length > 1 ? "s" : ""}`);
  if (wb.credits_per_growth) rows.push(`<b>Wall:</b> +${wb.credits_per_growth} credit each Growth (every house)`);
  if (wb.extra_draw) rows.push(`<b>Wall:</b> draw +${wb.extra_draw} card each Growth (every house)`);
  if (wb.fast_play) rows.push(`<b>Wall:</b> +${wb.fast_play} fast play (every house)`);
  if (wb.hull_brace) rows.push(`<b>Wall:</b> Brace ${wb.hull_brace} in every Outer Hull section each Dusk`);
  if (wb.decay_ward) rows.push(`<b>Wall:</b> the first ${wb.decay_ward} Decay each generation returns to the pool`);
  if (wb.purpose_per_gen) rows.push(`<b>Wall:</b> +${wb.purpose_per_gen} Purpose each Dusk`);
  for (const [k, name] of [["dawn", "Heir"], ["day", "Steward"], ["dusk", "Elder"]]) {
    const L = st.slots[k];
    if (L?.bt) rows.push(`<span class="muted"><b>Waiting (${name} ${L.leader}):</b> ${esc(DATA.discoveryById[L.bt].breakthrough.text)} — switches on when this leader reaches the Wall</span>`);
  }
  const day = st.slots.day, dusk = st.slots.dusk;
  if (day) rows.push(`<b>Steward ${day.leader}</b> ${houseTag(day.house)} ${day.house == null ? "(no house: the first seat decides shared choices)" : "decides shared choices"} · Reign this Day: ${esc(card(G, day.leader).reign.text)}`);
  if (dusk) rows.push(`<b>Elder ${dusk.leader}</b> ${houseTag(dusk.house)}: its Legacy takes hold this Dusk${dusk.tempered ? " (tempered)" : ""}: <span class="loss">${esc(card(G, dusk.leader).legacy.text)}</span>`);
  for (const L of st.legacies || []) {
    const where = L.types ? L.types.join(" + ") : "no event";
    rows.push(`<b>Legacy of ${L.leader}</b> ${houseTag(L.house)} in ${esc(where)}: ${esc(legacyText(L.effects))}`);
  }
  if (st.crisisFlipped) { const x = DATA.crisis.cards.find((c) => c.id === st.crisisId); rows.push(`<b class="loss">Ship in Crisis — ${esc(x.name)}:</b> ${esc(x.text)}`); }
  if (st.dest?.id) rows.push(`<b>${esc(st.dest.name)}:</b> ${st.dest.texts.map(esc).join(" · ")}`);
  if (G.cfg.landfallCard) rows.push(`<b>Landfall:</b> ${st.landfallMode === "shuffled" ? "shuffled into the Stage III events; you win if it retires to the Wall while the win condition holds" : "when the win condition is met, the Steward may begin Landfall; you win when it retires to the Wall"}${st.landfallPlaced ? " (under way)" : ""}`);
  st.houses.forEach((H, h) => {
    const raw = houseStats(G, st, h).raw;
    const e = Object.entries(raw).filter(([, n]) => n).map(([g, n]) => `${g} ${n}`).join(", ");
    if (e) rows.push(`<span style="color:${HOUSE_COLORS[h]}">●</span> ${esc(H.id)} gets <b>${e}</b> free each generation (track slots + Wall)`);
  });
  $("effects").innerHTML = rows.length ? rows.map((r) => `<div class="eff">${r}</div>`).join("") : "<i class=\"muted\">nothing yet</i>";
}

function renderConveyor() {
  const st = D.st;
  const slot = (name, L) => `<div class="slot"><b>${name}</b>${L ? " " + houseTag(L.house) : ""}${L?.start ? ` <span class="muted">(starting leader)</span>` : ""}<br>${L ? `${eventText(L.event)}${L.tempered ? " · tempered" : ""}${L.bt ? ` · Breakthrough ${L.bt} (on the Wall later)` : ""}${cardHTML(L.leader)}` : "<i>empty</i>"}</div>`;
  $("conveyor").innerHTML = slot("Dusk: Elder (Legacy, then Collapse)", st.slots.dusk) + slot("Day: Steward (Reign, then Grow)", st.slots.day) +
    slot("Dawn: Heir (Seed)", st.slots.dawn);
  const dest = st.dest?.id ? `<div class="slot"><b>${esc(st.dest.name)}</b><br>${st.dest.texts.map(esc).join("<br>")}${st.escalationEvent ? `<br><i>Escalation card: ${st.escalationEvent}</i>` : ""}</div>` : "";
  $("conveyor").innerHTML += dest;
}

function renderForecast() {
  const { out, collapse, grow, when } = forecast();
  const rows = Object.entries(out);
  const col = rows.filter(([, f]) => f.collapse !== undefined).sort((a, b) => b[1].collapse - a[1].collapse);
  const gr = rows.filter(([, f]) => f.grow);
  $("forecast").innerHTML = `<div class="slot"><b>Collapse ${when}</b>${collapse ? ` (${collapse.types.join(" + ")})` : ""}<br>` +
    (col.length ? col.map(([id, f]) => `${id}: ${f.collapse} dmg${f.decay ? " → <b class=\"loss\">Decay</b>" : ""}${f.crew ? `, ${f.crew} Crew lost` : ""}`).join("<br>") : "<i>nothing threatened</i>") +
    `</div><div class="slot"><b>Grow</b>${grow ? ` (${grow.types.join(" + ")})` : ""}<br>` +
    (gr.length ? gr.map(([id, f]) => `${id}: ${f.grow === "patched" ? "Patch stops it" : "+1 " + f.grow}`).join("<br>") : "<i>nothing grows</i>") + "</div>";
}

// Section geometry from data/boards.json: each board's polygons rotated and placed by the layout.
const SCALE = 0.95;
function geometry() {
  const st = D.st, geo = {};
  const ids = [...new Set(st.order.map((id) => st.sections[id].board))];
  const L = st.layout && DATA.boards.layouts?.[st.layout];
  const place = (b, i) => (L ? L.place[b] : [i * 340, 0, 0]);
  const tf = ([x, y], [px, py, rot]) => {
    const r = (rot * Math.PI) / 180;
    return [x * Math.cos(r) - y * Math.sin(r) + px, x * Math.sin(r) + y * Math.cos(r) + py];
  };
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  const raw = {};
  ids.forEach((b, i) => {
    const bd = DATA.boards.boards.find((x) => x.id === b), pl = place(b, i);
    for (const s of bd.sections) {
      const poly = s.poly.map((p) => tf(p, pl));
      for (const [x, y] of poly) { minX = Math.min(minX, x); minY = Math.min(minY, y); maxX = Math.max(maxX, x); maxY = Math.max(maxY, y); }
      raw[s.id] = { poly, c: tf(s.center, pl) };
    }
  });
  const m = 16;
  const map = ([x, y]) => [m + (x - minX) * SCALE, m + (y - minY) * SCALE];
  for (const [id, g] of Object.entries(raw)) geo[id] = { poly: g.poly.map(map), c: map(g.c) };
  geo.$outlines = ids.map((b, i) => (DATA.boards.outline || []).map((p) => map(tf(p, place(b, i)))));
  // The Outer Hull side of each board (side 4 of the hull module) faces the void.
  const per = 13, hullN = 18, start = 4 * per;
  geo.$hulls = ids.map((b, i) => (DATA.boards.outline || []).slice(start, start + hullN + 1).map((p) => map(tf(p, place(b, i)))));
  return { geo, width: 2 * m + (maxX - minX) * SCALE, height: 2 * m + (maxY - minY) * SCALE };
}

function renderMap() {
  const st = D.st;
  const opts = D.pending && SECTION_KINDS.has(D.pending.kind) ? new Set(D.pending.options.map((o) => String(o).replace("*", ""))) : new Set();
  const { geo, width, height } = geometry();
  const fc = $("show-forecast")?.checked !== false ? forecast().out : {};
  let svg = `<defs><pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" stroke="var(--hullhatch)" stroke-width="2.5"/></pattern></defs>
    <rect x="0" y="0" width="${width}" height="${height}" fill="var(--void)"/>`;
  for (let i = 0; i < 60; i++) { const x = (i * 97.3) % width, y = (i * 53.7 + (i % 7) * 31) % height; svg += `<circle cx="${x}" cy="${y}" r="${i % 5 ? 0.8 : 1.4}" fill="var(--star)"/>`; }
  svg += `<text x="10" y="${height - 10}" class="voidlbl">THE VOID</text>`;
  const seen = new Set();
  for (const id of st.order) for (const a of st.sections[id].adj) {
    if (st.sections[id].board === st.sections[a].board) continue; // in-board neighbors share an edge already
    const k = [id, a].sort().join("-"); if (seen.has(k)) continue; seen.add(k);
    const p = geo[id].c, q = geo[a].c;
    svg += `<line class="edge" x1="${p[0]}" y1="${p[1]}" x2="${q[0]}" y2="${q[1]}" stroke-dasharray="4 4"/>`;
  }
  for (const id of st.order) {
    const s = st.sections[id], g = geo[id], [cx, cy] = g.c;
    const inf = Object.entries(s.influence).filter(([, n]) => n > 0)
      .map(([h, n]) => `<tspan fill="${HOUSE_COLORS[h]}">●${n > 1 ? n : ""}</tspan>`).join(" ");
    const tok = [s.brace && `Br${s.brace}`, s.quarantine && "Q", s.patch && `P${s.patch}`, s.lockout && `L${s.lockout}`,
      s.unrest && `U${s.unrest}`, s.isolate && `I${s.isolate}`].filter(Boolean).join(" ");
    const threat = [s.glitch && `▲${s.glitch}`, s.fault && `■${s.fault}`, s.failure && `⬢${s.failure}`].filter(Boolean).join(" ");
    const pts = g.poly.map((p) => p.join(",")).join(" ");
    const hinted = hint && SECTION_KINDS.has(D.pending?.kind) && String(hint.value).replace("*", "") === id;
    svg += `<g class="sec ${opts.has(id) ? "opt" : ""} ${hinted ? "hinted" : ""}" data-id="${id}">
      <polygon points="${pts}" fill="${TYPE_FILL[s.type]}" class="${s.hull ? "hullsec" : ""}"/>${s.hull ? `<polygon points="${pts}" fill="url(#hatch)" pointer-events="none"/>` : ""}
      <text x="${cx}" y="${cy - 20}" text-anchor="middle" font-size="11"><tspan font-weight="700">${id}</tspan> ${s.type.slice(0, 3)}</text>
      <text x="${cx}" y="${cy - 4}" text-anchor="middle" font-size="14">${threat || "·"}</text>
      <text x="${cx}" y="${cy + 12}" text-anchor="middle" font-size="11">${s.crew ? `☺${s.crew}` : ""} ${s.decay ? `✸${s.decay}` : ""}</text>
      <text x="${cx}" y="${cy + 27}" text-anchor="middle" font-size="13">${inf}</text>
      <text x="${cx}" y="${cy + 40}" text-anchor="middle" font-size="10">${tok}</text></g>`;
    const f = fc[id];
    if (f) {
      if (f.collapse !== undefined) svg += `<polygon points="${pts}" class="fc-collapse ${f.decay ? "fc-decay" : ""}" pointer-events="none"/>`;
      const badge = [f.collapse !== undefined ? `⚠${f.collapse}${f.decay ? " Decay!" : ""}` : "", f.grow && f.grow !== "patched" ? `↑${f.grow === "Failure" ? "⬢" : "■"}` : ""].filter(Boolean).join(" ");
      if (badge) svg += `<text x="${cx}" y="${cy - 34}" text-anchor="middle" class="fc-badge ${f.decay ? "fc-bad" : ""}" pointer-events="none">${badge}</text>`;
    }
  }
  for (const o of geo.$outlines) svg += `<polygon points="${o.map((p) => p.join(",")).join(" ")}" fill="none" stroke="var(--ink)" stroke-opacity=".8" stroke-width="2" stroke-linejoin="round" pointer-events="none"/>`;
  for (const h of geo.$hulls) svg += `<polyline points="${h.map((p) => p.join(",")).join(" ")}" class="hullplate" pointer-events="none"/>`;
  const map = $("map");
  map.setAttribute("viewBox", `0 0 ${width} ${height}`);
  map.setAttribute("width", width); map.setAttribute("height", height);
  map.innerHTML = svg;
  map.querySelectorAll(".sec").forEach((g) => {
    g.addEventListener("mousemove", (e) => showTip(e, sectionTip(g.dataset.id)));
    g.addEventListener("mouseleave", hideTip);
  });
  map.querySelectorAll(".sec.opt").forEach((g) => g.addEventListener("click", () => {
    const id = g.dataset.id;
    const o = D.pending.options.find((x) => String(x).replace("*", "") === id);
    act(o);
  }));
}

function sectionTip(id) {
  const st = D.st, s = st.sections[id], G = D.G;
  const inf = Object.entries(s.influence).filter(([, n]) => n > 0).map(([h, n]) => `${esc(houseData(G, st, +h).name.split(",")[0])} ${n}${n >= 2 ? " (Haven)" : ""}`).join(", ") || "none";
  const toks = [["Brace", s.brace], ["Quarantine", s.quarantine], ["Patch", s.patch], ["Lockout", s.lockout], ["Unrest", s.unrest], ["Isolate", s.isolate], ["damage taken", s.dmg]]
    .filter(([, n]) => n).map(([k, n]) => `${k} ${n}`).join(", ") || "none";
  const fc = forecast().out[id];
  const fcText = fc ? `<br><b>Forecast:</b> ${fc.collapse !== undefined ? `Collapse ${fc.collapse} damage${fc.decay ? " → Decay" : ""}${fc.crew ? `, ${fc.crew} Crew lost` : ""}` : ""}${fc.grow ? `${fc.collapse !== undefined ? "; " : ""}${fc.grow === "patched" ? "Grow blocked by Patch" : "Grow +1 " + fc.grow}` : ""}` : "";
  const ev = ["dusk", "day", "dawn"].filter((k) => st.slots[k]?.event && G.data.eventById[st.slots[k].event].types.some((t) => t === "ALL" || t === s.type || (t === "Hull" && s.hull)));
  const lm = Object.keys(LEGACY_WORDS).map((k) => [k, legacyMod(st, s, k)]).filter(([, n]) => n);
  const lmText = lm.length ? `<br><b>Legacies here:</b> ${esc(legacyText(Object.fromEntries(lm)))}` : "";
  return `<b>${id}</b> ${s.type}${s.hull ? " · Outer Hull (faces the void: Seeds always reach it)" : ""}<br>Glitch ${s.glitch} · Fault ${s.fault} · Failure ${s.failure} → collapse damage ${s.glitch + 2 * s.fault + 3 * s.failure}<br>Crew ${s.crew} · Decay ${s.decay}<br>Influence: ${inf}<br>Tokens: ${toks}<br>Adjacent: ${s.adj.join(", ")}${lmText}${fcText}${ev.length ? `<br><b>Targeted by:</b> ${ev.map((k) => ({ dusk: "Dusk (Collapse)", day: "Day (Grow)", dawn: "Dawn" })[k]).join(", ")}` : ""}`;
}
function showTip(e, html) {
  let t = $("tip"); if (!t) { t = document.createElement("div"); t.id = "tip"; document.body.appendChild(t); }
  t.innerHTML = html; t.style.display = "block";
  t.style.left = Math.min(e.clientX + 14, innerWidth - 300) + "px"; t.style.top = (e.clientY + 14) + "px";
}
function hideTip() { const t = $("tip"); if (t) t.style.display = "none"; }

// ------------------------------------------------------------------ save / load
function snapshot() {
  return { v: 1, cfg: D.cfgIn, seats, st: D.st, phaseIdx: D.phaseIdx, answers: D.answers,
    snapshot: D.snapshot, seeds: D.botSeeds(), pending: D.pending };
}
function save() {
  const text = JSON.stringify(snapshot());
  // A file download where the browser allows it; the hosted page blocks downloads, so also copy it.
  try {
    const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([text], { type: "application/json" }));
    a.download = `generation-ship-g${D.st.gen}.json`; a.click(); URL.revokeObjectURL(a.href);
  } catch { /* downloads blocked */ }
  navigator.clipboard?.writeText(text).then(
    () => flash("Saved: game file downloaded (if allowed) and copied to the clipboard. Paste it into a .json file to keep it."),
    () => flash("Saved as a file download (clipboard copy was not allowed here)."));
}
function flash(msg) {
  let t = $("toast"); if (!t) { t = document.createElement("div"); t.id = "toast"; document.body.appendChild(t); }
  t.textContent = msg; t.hidden = false; clearTimeout(flash.tm); flash.tm = setTimeout(() => { t.hidden = true; }, 4000);
}
function restore(obj) {
  seats = obj.seats;
  D = new Driver(DATA, obj.cfg, seats, 1);
  D.cfgIn = obj.cfg; D.st = obj.st; D.phaseIdx = obj.phaseIdx; D.answers = obj.answers || [];
  D.snapshot = obj.snapshot; D.pending = obj.pending; D.history = obj.snapshot ? [obj.snapshot] : [];
  D.agents.forEach((a, i) => { if (a instanceof Bot) a.seed = obj.seeds[i]; });
  $("setup").hidden = true; $("game").hidden = false;
  afterStep(D.pending ? "input" : null);
}
function autosave() { try { localStorage.setItem("gs-autosave", JSON.stringify(snapshot())); } catch { /* storage unavailable */ } }

function trackHTML(track, pos) {
  return track.map((v, i) => {
    const t = typeof v === "object" ? "★" + (v.element || (v.fast_play ? "fast" : v.clone ? "clone" : v.draw ? "draw" : "")) : v;
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
      hand = H.hand.map((c) => cardHTML(c, (commitSel.play.has(c) ? "sel" : "") + (c === commitSel.nominee ? " nom" : ""))).join("");
    } else if (pend && D.pending.kind === "clone") {
      hand = H.hand.map((c) => cardHTML(c, cloneSel.has(c) ? "sel" : "")).join("");
    } else {
      hand = H.hand.map((c) => cardHTML(c)).join("") + (H.played.length ? `<div class="stats">Played: ${H.played.join(", ")}${H.nominee ? ` (nominee ${H.nominee})` : ""}</div>` : "");
    }
    return `<div class="house ${pend ? "active" : ""}" data-h="${h}" style="--hc:${HOUSE_COLORS[h]}"><b>${esc(hd.name)}</b> <span class="stats">${human ? "Human" : seats[h]}</span>
      <div class="stats">Credits ${H.credits} (+${hs.income}/gen) · plays ${hs.plays} · hand ${hs.hand} · clone ${hs.clone} · influence ${totalInfluence(st, h)}${st.slots.day?.house === h ? " · <b>Steward's house</b>" : ""}</div>
      <div class="stats">Credits track: ${trackHTML(hd.tracks.credits, H.track.credits)}<br>Plays track: ${trackHTML(hd.tracks.plays, H.track.plays)}</div>
      <div class="stats">Elements: ${el}</div>
      <details><summary class="stats">${esc(hd.innate.name)} (${hd.innate.speed}) · ${esc(hd.special.text)}</summary><div class="stats">${tiers}</div></details>
      <div class="hand">${hand}</div></div>`;
  }).join("");
  document.querySelectorAll("#houses .card[data-card]").forEach((el) => el.addEventListener("click", () => {
    if (!D.pending) return;
    if (+el.closest(".house")?.dataset.h !== D.pending.h) return; // only the deciding house's hand responds
    const cid = el.dataset.card;
    if (D.pending.kind === "commit") { commitSel.play.has(cid) ? commitSel.play.delete(cid) : commitSel.play.add(cid); if (!commitSel.play.has(commitSel.nominee)) commitSel.nominee = [...commitSel.play].sort((a, b) => card(D.G, b).cost - card(D.G, a).cost)[0] ?? null; commitSel.fast.delete(commitSel.nominee); render(); }
    if (D.pending.kind === "clone") { cloneSel.has(cid) ? cloneSel.delete(cid) : cloneSel.size < D.pending.ctx.slots && cloneSel.add(cid); render(); }
  }));
}

function renderWall() {
  const st = D.st;
  const n = st.wallSize ?? 13;
  let html = "";
  for (let i = 0; i < n; i++) {
    const w = st.wall[i];
    html += w ? `<div class="ws full ${w.bt ? "bonus" : ""}" style="border-left:4px solid ${w.house == null ? "var(--line)" : HOUSE_COLORS[w.house]}" title="${w.bt ? esc(DATA.discoveryById[w.bt].breakthrough.text) : ""}">${i + 1}. ${w.leader}<br>${w.event ? DATA.eventById[w.event].types.join("+") : "—"}${w.bt ? `<br>★ ${esc(DATA.discoveryById[w.bt].breakthrough.text.replace("On the Wall: ", ""))}` : ""}</div>` : `<div class="ws">${i + 1}.</div>`;
  }
  $("wall").innerHTML = html;
}

const KIND_TEXT = {
  growth: "Choose a growth option", track: "Uncover which track?", remarkables: "Take a Remarkable instead of 2 Commons?",
  commit: "Choose your plays", cardTarget: "Choose a target for", innateTarget: "Choose a target for your innate power",
  ventTo: "Vent to which adjacent section?", gatherFrom: "Gather Crew from which section?", cascade: "Decay cascades: choose an adjacent section",
  moveInfluenceFrom: "Move influence from which section?", growthInfluence: "Place influence where?", influenceFor: "Place that house's influence where?",
  addCrewAt: "Add Crew where?", restoreAt: "Restore Decay where?", discoveryAt: "Discovery: choose a section",
  vote: "Vote for the next heir", discovery: "Discovery", clone: "Clone cards into the next generation", landfall: "Begin Landfall?",
  playOrder: "Which of your plays resolves next?", tiebreak: "Break the tie",
};

// Human-readable description of a house's next track slot.
function slotDesc(h, track) {
  const st = D.st, G = D.G, hd = houseData(G, st, h), H = st.houses[h], hs = houseStats(G, st, h);
  const t = hd.tracks[track], pos = H.track[track];
  if (pos >= t.length - 1) return "track complete";
  const v = t[pos + 1];
  if (typeof v === "object") return v.element ? `+1 ${v.element} element every generation` : v.fast_play ? "+1 fast play every generation" : v.draw ? "+1 card drawn every generation" : "+1 clone slot";
  return track === "credits" ? `${v} credits per generation (now ${hs.income})` : `${v} card plays (now ${hs.plays}; hand ${v + hd.hand_bonus})`;
}
const fx = (e) => Object.entries(e).map(([k, v]) => `${k.replace(/_/g, " ")} ${v}`).join(", ");

// The commit planner: selected cards, cost, nominee, fast slots, elements, thresholds and innate tier.
function commitPlanHTML(h, ctx) {
  const st = D.st, G = D.G, H = st.houses[h], hs = houseStats(G, st, h), hd = houseData(G, st, h);
  const sel = [...commitSel.play];
  const el = { ...hs.raw };
  for (const c of sel) for (const g of card(G, c).guilds) el[g] = (el[g] || 0) + 1;
  const met = (req) => Object.entries(req).every(([g, n]) => (el[g] || 0) >= n);
  const fastCap = 1 + hs.fastPlays + (H.perkFast || 0) + (H.id === "galvan" ? Math.floor((el.Engineers || 0) / 2) : 0);
  const cost = sel.reduce((n, c) => n + (c === commitSel.nominee ? nomineeCost(G, c) : card(G, c).cost), 0);
  const fastUsed = 1 + [...commitSel.fast].filter((c) => sel.includes(c) && c !== commitSel.nominee).length;
  const rows = sel.map((c) => {
    const k = card(G, c), nom = c === commitSel.nominee;
    const th = k.threshold ? (met(k.threshold.elements) ? `<span class="ok">✓ bonus: ${esc(k.threshold.text)}</span>` : `<span class="muted">✗ needs ${Object.entries(k.threshold.elements).map(([g, n]) => `${g} ${n}`).join(" + ")} (this card's own guilds count)</span>`) : "<span class=\"muted\">—</span>";
    const canFast = !nom && (commitSel.fast.has(c) || fastUsed < fastCap);
    return `<tr><td><b>${c}</b></td><td>${nom ? "<s>" + k.cost + "</s> " + nomineeCost(G, c) : k.cost}¢</td>
      <td><label><input type="radio" name="nomr" class="nomr" value="${c}" ${nom ? "checked" : ""}> nominee</label></td>
      <td><label><input type="checkbox" class="fx" value="${c}" ${nom ? "checked disabled" : commitSel.fast.has(c) ? "checked" : ""} ${canFast || nom ? "" : "disabled"}> fast</label></td><td>${th}</td></tr>`;
  }).join("");
  let tier = null;
  for (const t of hd.innate.tiers) if (met(t.threshold)) tier = t;
  const next = hd.innate.tiers.find((t) => !met(t.threshold));
  const innate = tier ? `<span class="ok">Tier ${tier.tier}: ${esc(fx(tier.effects))}</span>` : `<span class="muted">no tier</span>`;
  const nextTxt = next ? ` · next tier ${next.tier} needs ${Object.entries(next.threshold).map(([g, n]) => `${g} ${n}`).join(" + ")}` : "";
  const elTxt = Object.entries(el).filter(([, n]) => n).map(([g, n]) => `${g} ${n}`).join(", ") || "none";
  const over = sel.length > ctx.plays || cost > H.credits;
  return `<div class="plan">
    <div>Click cards in your hand to add or remove them. <b>Plays ${sel.length}/${ctx.plays}</b> · <b class="${cost > H.credits ? "loss" : ""}">Cost ${cost}¢ of ${H.credits}¢</b> · Fast ${Math.min(fastUsed, fastCap)}/${fastCap} (nominee counts)</div>
    ${sel.length ? `<table>${rows}</table>` : "<div class=\"muted\">No cards selected yet.</div>"}
    <div>Elements: ${elTxt}</div>
    <div>${esc(hd.innate.name)} (${hd.innate.speed}): ${innate}${nextTxt}</div>
    <button id="commit-ok" class="primary" ${over ? "disabled" : ""}>Commit ${sel.length ? "these plays" : "no plays"}</button></div>`;
}

// Hint: what the strongest bot would choose here (computed on a copy of the game).
let hint = null;
function computeHint() {
  const { h, kind, options, ctx } = D.pending;
  const bot = new Bot(BOT_LEVELS.house, 4242);
  try { return bot.choose(D.G, clone(D.st), h, kind, options, clone(ctx)); } catch (e) { console.warn(e); return null; }
}
function describeHint(v) {
  const { kind } = D.pending;
  if (v === null || v === undefined) return "no suggestion";
  if (kind === "commit") return v.play.length ? `play ${v.play.join(", ")}; nominee ${v.nominee}${v.fast?.length ? `; also fast: ${v.fast.join(", ")}` : ""}` : "play nothing";
  if (kind === "clone") return v.length ? `keep ${v.join(", ")}` : "keep nothing";
  if (kind === "remarkables") return v ? "take a Remarkable" : "draw Commons only";
  if (SKIP_TEXT[v]) return SKIP_TEXT[v];
  if (SECTION_KINDS.has(kind)) return typeof v === "number" ? `give it to ${D.st.houses[v].id}` : `section ${String(v).replace("*", "")}`;
  if (kind === "playOrder") return v === "innate" ? "resolve your innate next" : `resolve ${v} next`;
  return String(v);
}
function applyHint() {
  const v = hint.value, { kind } = D.pending;
  if (kind === "commit") {
    commitSel.play = new Set(v.play); commitSel.nominee = v.nominee;
    commitSel.fast = new Set((v.fast || []).filter((c) => c !== v.nominee));
    hint = null; render(); return;
  }
  if (kind === "clone") { cloneSel = new Set(v); hint = null; render(); return; }
  hint = null; act(v);
}

// End of game: summary, notes, and a playtest record (copy + kept in this browser).
const CAUSE = { decay: "the Decay pool ran out", influence: "a house lost all its influence", time: "the event deck ran out", stalled: "the game stalled" };
function playtestRecord() {
  const st = D.st;
  return { when: new Date().toISOString(), cfg: D.cfgIn, seats, seed: D.cfgIn?.seed ?? null, layout: st.layout,
    result: st.result, tier: st.tier, discoveries: st.discoveriesEarned, wall: st.wall.map((w) => ({ leader: w.leader, house: w.house == null ? null : st.houses[w.house]?.id, event: w.event, bt: w.bt })),
    stats: { decayPlaced: st.stats.decayPlaced, crewLost: st.stats.crewLost, destroyed: st.stats.destroyed, discoveryApplied: st.stats.discoveryApplied,
      discoveryBreakthrough: st.stats.discoveryBreakthrough, warded: st.stats.warded || 0, houses: st.stats.houses.map((x) => ({ id: x.id, played: x.played, creditsSpent: x.creditsSpent,
        innateTiers: x.innateTiers, leaders: x.chosenLeader, remarkables: x.remarkables })) },
    notes: $("pt-notes")?.value ?? "", log: st.log };
}
function storedRecords() { try { return JSON.parse(localStorage.getItem("gs-playtests") || "[]"); } catch { return []; } }
function summaryHTML() {
  const st = D.st, r = st.result, win = r.outcome === "win";
  const houses = st.stats.houses.map((x, h) => `<tr><td style="color:${HOUSE_COLORS[h]}"><b>${esc(houseData(D.G, st, h).name.split(",")[0])}</b> (${esc(seats[h])})</td><td>${x.played}</td><td>${x.creditsSpent}</td><td>${x.innateTiers.slice(1).join(" / ")}</td><td>${x.chosenLeader}</td></tr>`).join("");
  const wall = st.wall.map((w, i) => `${i + 1}. ${w.leader} · ${w.event ? DATA.eventById[w.event].types.join("+") : "—"}${w.bt ? " ★" + w.bt : ""}`).join("<br>") || "—";
  return `<div class="summary"><div class="banner ${r.outcome}">${win ? "Victory" : "Defeat"} in generation ${r.gen}: ${esc(win ? (r.cause === "Landfall" ? "Landfall reached" : `the ${r.cause} win condition was met`) : CAUSE[r.cause] || r.cause)}</div>
    <div class="sumgrid"><div><b>The voyage</b><br>Understanding ${["I", "II", "III"][st.tier - 1]} · ${st.discoveriesEarned} Discoveries (${st.stats.discoveryApplied} applied, ${st.stats.discoveryBreakthrough} Breakthroughs)<br>
      Threat destroyed: ${st.stats.destroyed.glitch} Glitches, ${st.stats.destroyed.fault} Faults, ${st.stats.destroyed.failure} Failures<br>
      Decay placed ${st.stats.decayPlaced} · Crew lost ${st.stats.crewLost} · events left ${st.decks.events.length}</div>
      <div><b>Wall of Leaders</b><br>${wall}</div></div>
    <table class="sumt"><tr><th>House</th><th>Cards played</th><th>Credits spent</th><th>Innate tier I / II / III (generations)</th><th>Heirs chosen</th></tr>${houses}</table>
    <label for="pt-notes"><b>Playtest notes</b> (what felt good, confusing or broken)</label>
    <textarea id="pt-notes" rows="3"></textarea>
    <div class="opts"><button id="pt-save" class="primary">Save playtest record</button><button id="pt-copy">Copy record</button><button id="pt-copy-all">Copy all saved records (${storedRecords().length})</button><button id="pt-again">New game, same setup</button></div></div>`;
}
function wireSummary() {
  const copy = (text, what) => navigator.clipboard?.writeText(text).then(() => flash(`${what} copied to the clipboard.`), () => flash("The clipboard is not available here."));
  $("pt-save").addEventListener("click", () => {
    try { const all = storedRecords(); all.push(playtestRecord()); localStorage.setItem("gs-playtests", JSON.stringify(all)); flash(`Saved in this browser (${all.length} records).`); }
    catch { flash("This browser blocked local storage; use Copy record instead."); }
    render();
  });
  $("pt-copy").addEventListener("click", () => copy(JSON.stringify(playtestRecord(), null, 1), "Playtest record"));
  $("pt-copy-all").addEventListener("click", () => copy(JSON.stringify(storedRecords(), null, 1), "All saved records"));
  $("pt-again").addEventListener("click", () => { const cfg = D.cfgIn; D = new Driver(DATA, cfg, seats, (cfg.seed || 1) + 1); D.cfgIn = { ...cfg, seed: (cfg.seed || 1) + 1 }; render(); });
}

function renderPrompt() {
  const p = $("prompt"), st = D.st, G = D.G;
  if (st.result) { p.className = ""; p.innerHTML = summaryHTML(); wireSummary(); return; }
  if (!D.pending) { p.className = "idle"; p.textContent = autoTimer ? "Running…" : "Press Step (or Auto) to continue."; return; }
  p.className = "";
  const { h, kind, options, ctx } = D.pending;
  const hd = houseData(G, st, h), H = st.houses[h];
  const who = `<b style="color:${HOUSE_COLORS[h]}">${esc(hd.name)}</b>: `;
  const sec = (id) => `${id} (${st.sections[id].type})`;
  let title = KIND_TEXT[kind] ?? kind, body = "";
  if (kind === "growth") {
    const perk = hd.growth_perk?.B ? ` + ${hd.growth_perk.B.text}` : "";
    const aInf = hd.growth_overrides?.A?.influence ?? 1, aRange = hd.growth_overrides?.A?.range ?? 1;
    const cTxt = hd.growth_overrides?.C?.text ?? "Draw +2 cards this generation and gain 1 credit";
    body = `<button data-o="A">A · Place ${aInf} influence (range ${aRange}) and uncover a track slot<br><small>Credits next: ${slotDesc(h, "credits")} · Plays next: ${slotDesc(h, "plays")}</small></button>
      <button data-o="B">B · Gain 2 credits${esc(perk)}<br><small>You have ${H.credits}¢</small></button>
      <button data-o="C">C · ${esc(cTxt)}</button>`;
  } else if (kind === "track") {
    body = options.map((o) => `<button data-o="${o}">${o === "credits" ? "Credits" : "Plays"} track → ${esc(slotDesc(h, o))}</button>`).join("");
  } else if (kind === "remarkables") {
    const n = ctx.handSize;
    title = "Draw a Remarkable person this generation?";
    body = `<button data-o="0">No — draw ${n} Common cards</button><button data-o="1">Yes — 1 Remarkable + ${Math.max(0, n - 2)} Commons<br><small>Remarkables cost more but are stronger, with harsher Legacies</small></button>`;
  } else if (kind === "commit") {
    body = commitPlanHTML(h, ctx);
  } else if (kind === "clone") {
    title = `Clone up to ${ctx.slots} card(s): click them in your hand to keep them for next generation`;
    body = `<button id="clone-ok" class="primary">Keep ${cloneSel.size ? [...cloneSel].join(", ") : "nothing"}</button>`;
  } else if (kind === "vote") {
    const upcoming = "Its event is revealed only after the vote. ";
    title = "Vote for the next heir";
    body = `<div class="muted">${upcoming}The heir reigns next generation (Reign) and leaves its Legacy the one after, in its event's sections. Ties go to the house with fewer leaders on the conveyor; if still tied, the Steward's house decides.</div>` +
      options.map((o) => { const nh = st.houses.findIndex((x) => x.nominee === o); return `<div class="votec">${cardHTML(o)}<button data-o="${o}">Vote ${o}${nh >= 0 ? ` (${esc(st.houses[nh].id)})` : ""}</button></div>`; }).join("");
  } else if (kind === "discovery") {
    const d = DATA.discoveryById[ctx.id], tl = ["I", "II", "III"][st.tier - 1], t = d.tiers[tl];
    title = `Discovery ${d.id} (${d.family}) — the Steward's house decides: apply it now, or keep it as a Breakthrough`;
    body = `<button data-o="apply">Apply now (Understanding ${tl}):<br><small>${esc(t.text)}</small></button>
      <button data-o="breakthrough">Breakthrough under Steward ${st.slots.day?.leader ?? ""}:<br><small>${esc(d.breakthrough.text)} — switches on when this leader reaches the Wall (2 generations), then lasts all voyage</small></button>`;
  } else if (kind === "playOrder") {
    title = `Choose what resolves next (${ctx.fast ? "fast" : "slow"} phase)`;
    body = options.map((o) => o === "innate"
      ? `<button data-o="innate">Innate: ${esc(hd.innate.name)}<br><small>uses the elements you committed</small></button>`
      : `<div class="votec">${cardHTML(o)}<button data-o="${o}">Resolve ${o} now</button></div>`).join("");
  } else if (kind === "tiebreak") {
    title = "The vote is tied — as Steward's house, choose the heir";
    body = options.map((o) => { const nh = st.houses.findIndex((x) => x.nominee === o); return `<div class="votec">${cardHTML(o)}<button data-o="${o}">Choose ${o}${nh >= 0 ? ` (${esc(st.houses[nh].id)})` : ""}</button></div>`; }).join("");
  } else if (kind === "landfall") {
    title = "The win condition is met. Begin Landfall?";
    body = `<div class="muted">Landfall replaces the next event. It matches every section, travels down the conveyor, and you win when it retires to the Wall (survive about 3 more generations).</div>
      <button data-o="begin">Begin Landfall</button><button data-o="wait">Not yet (ask again next generation)</button>`;
  } else if (SECTION_KINDS.has(kind)) {
    const ctxText = {
      cardTarget: () => `Play <b>${ctx.card}</b> — choose its target section.${cardHTML(ctx.card)}`,
      innateTarget: () => { const t = hd.innate.tiers.find((x) => x.tier === ctx.tier); return `${esc(hd.innate.name)} tier ${ctx.tier}: ${esc(fx(t?.effects || {}))} — choose a section.`; },
      ventTo: () => `Vent a ${ctx.piece} out of ${sec(ctx.from)} into which neighbor?`,
      gatherFrom: () => `Gather 1 Crew into ${sec(ctx.to)} from which neighbor?`,
      cascade: () => `Decay was already in ${sec(ctx.from)}, so it cascades: choose a neighbor to receive 1 Decay (each house loses 1 influence there).`,
      moveInfluenceFrom: () => `Move 1 influence into ${sec(ctx.to)} from which section?`,
      growthInfluence: () => "Place 1 influence in a highlighted section (within range of your influence).",
      influenceFor: () => `Place influence for ${esc(st.houses[ctx.house]?.id ?? "")}.`,
      addCrewAt: () => `Add ${ctx.n ?? 1} Crew to which section?`,
      restoreAt: () => "Restore (remove) Decay from which section?",
      discoveryAt: () => `Discovery ${ctx.id}: ${esc(fx(ctx.effects || {}))} — choose one section on board ${ctx.board}.`,
    }[kind]?.() ?? "";
    title = "";
    const nonSec = options.filter((o) => typeof o === "number" || SKIP_TEXT[o]);
    body = `${ctxText}<div class="muted">Click a highlighted section on the map${options.some((o) => String(o).endsWith("*")) ? " (targets marked by Voices Among the Crew cost 1 credit)" : ""}.</div>` +
      nonSec.map((o) => `<button data-o="${o}">${typeof o === "number" ? "Give it to " + esc(st.houses[o].id) : SKIP_TEXT[o]}</button>`).join("");
  } else {
    body = options.map((o) => `<button data-o="${o}">${esc(String(o))}</button>`).join("");
  }
  const hintBox = hint ? `<div class="hint">Hint: ${esc(describeHint(hint.value))} <button id="hint-use">${kind === "commit" || kind === "clone" ? "Select it" : "Do it"}</button></div>` :
    `<button id="hint-btn" class="hintb" title="Ask the house bot what it would do">Hint</button>`;
  p.innerHTML = `${who}${title}<div class="opts">${body}</div>${hintBox}`;
  $("hint-btn")?.addEventListener("click", () => { $("hint-btn").textContent = "Thinking…"; setTimeout(() => { hint = { value: computeHint() }; render(); }, 20); });
  $("hint-use")?.addEventListener("click", applyHint);
  p.querySelectorAll("button[data-o]").forEach((b) => b.addEventListener("click", () => {
    const raw = b.dataset.o; const o = options.find((x) => String(x) === raw);
    act(o);
  }));
  p.querySelectorAll(".nomr").forEach((x) => x.addEventListener("change", () => { commitSel.nominee = x.value; commitSel.fast.delete(x.value); render(); }));
  p.querySelectorAll(".fx").forEach((x) => x.addEventListener("change", () => { x.checked ? commitSel.fast.add(x.value) : commitSel.fast.delete(x.value); render(); }));
  $("commit-ok")?.addEventListener("click", () => {
    const play = [...commitSel.play];
    act({ play, nominee: play.length ? commitSel.nominee : null, fast: [...commitSel.fast].filter((c) => play.includes(c) && c !== commitSel.nominee) });
  });
  $("clone-ok")?.addEventListener("click", () => act([...cloneSel]));
}

function act(value) {
  const r = D.give(value);
  afterStep(r);
}
function afterStep(r) {
  commitSel = null; cloneSel = null; hint = null;
  if (D) autosave();
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
function renderLayouts() {
  const P = +$("players").value;
  const L = DATA.boards.layouts || {};
  const def = DATA.boards.default_layout?.[String(P)];
  $("layout").innerHTML = Object.entries(L).filter(([, l]) => l.boards.length === P)
    .map(([n]) => `<option value="${n}" ${n === def ? "selected" : ""}>${n}${n === def ? " (default)" : ""}</option>`).join("");
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
  const cfg = { players: P, houses, layout: $("layout").value || null, tierConditions: $("tiers").value,
    destination: $("destination").value || null, destinationLevel: +$("level").value,
    landfallCard: { off: false, choice: true, shuffled: "shuffled" }[$("landfall").value] ?? false };
  cfg.seed = +$("seed").value || 1;
  D = new Driver(DATA, cfg, seats, cfg.seed);
  D.cfgIn = cfg;
  $("setup").hidden = true; $("game").hidden = false;
  render();
}

async function main() {
  DATA = await loadData();
  renderSeats(); renderDestinations(); renderLayouts();
  $("players").addEventListener("change", () => { renderSeats(); renderLayouts(); });
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
  $("btn-undo-dec").addEventListener("click", () => {
    if (!D) return;
    stopAuto();
    const r = D.undoDecision();
    if (r === false) { D.undo(); afterStep(null); flash("No earlier decision in this phase; went back to the start of the previous phase."); }
    else afterStep(r);
  });
  $("btn-mute").addEventListener("click", () => { muted = !muted; $("btn-mute").textContent = muted ? "🔇" : "🔊"; });
  const setCompact = (on) => { document.body.classList.toggle("compact", on); $("btn-compact").textContent = on ? "Roomy view" : "Compact view"; try { localStorage.setItem("gs-compact", on ? "1" : "0"); } catch { /* storage unavailable */ } };
  let compact = true; try { compact = localStorage.getItem("gs-compact") !== "0"; } catch { /* storage unavailable */ }
  setCompact(compact);
  $("btn-compact").addEventListener("click", () => setCompact(!document.body.classList.contains("compact")));
  $("btn-save").addEventListener("click", () => { if (D) save(); });
  $("show-forecast").addEventListener("change", () => { if (D) render(); });
  $("file-load").addEventListener("change", async (e) => { const f = e.target.files[0]; if (f) { stopAuto(); restore(JSON.parse(await f.text())); } });
  try {
    const saved = localStorage.getItem("gs-autosave");
    if (saved) {
      const b = document.createElement("button"); b.textContent = "Resume last game"; b.style.marginLeft = "8px";
      b.addEventListener("click", () => restore(JSON.parse(saved)));
      $("btn-start").after(b);
    }
  } catch { /* storage unavailable */ }
}
// Test hook: the decision currently waiting for a human (used by test/ui-playthrough.cjs).
window.__gsPendingKind = () => D?.pending?.kind ?? null;
main();
