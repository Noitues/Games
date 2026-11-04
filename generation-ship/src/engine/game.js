// Setup, round phases and the game loop.
import { DEFAULT_CONFIG } from "./config.js";
import { shuffle, pick, nextRandom as nextRand } from "./rng.js";
import {
  allSections, matches, threatCount, inRange, influenceSections, targetFilter, distances,
  damageThreat, placeDecay, gainPurpose, losePurpose, gatherCrew, applySectionEffects,
  applyHouseEffects, drawFrom, checkWin, lose, log, downgrade, restoreDecay, totalInfluence,
  winConditionMet, stewardHouse, wallBonuses,
} from "./rules.js";

const BOARD_IDS = ["A", "B", "C", "D"];

// ============================================================== setup
export function createGame(data, cfgIn = {}, seed = 1) {
  const cfg = { ...DEFAULT_CONFIG, ...cfgIn };
  const P = cfg.players;
  const st = {
    rng: seed | 0, gen: 0, phase: "setup", log: [], result: null,
    sections: {}, order: [], houses: [],
    decks: {}, slots: { dawn: null, day: null, dusk: null }, wall: [],
    decayPool: cfg.decayPerPlayer * P + cfg.decayBase, crisisFlipped: false, crisisId: null,
    purpose: 0, purposeCap: cfg.purposePerPlayer * P, discoveriesEarned: 0, tier: 1,
    pendingDiscoveries: [], breakthroughs: [],
    stats: { destroyed: { glitch: 0, fault: 0, failure: 0 }, decayPlaced: 0, crewLost: 0,
             purposeBy: {}, foresee: 0, discoveryApplied: 0, discoveryBreakthrough: 0,
             legacyTempered: 0, houses: [] },
  };
  // boards
  // Layout: which boards, where, and which sections link across docked sides.
  const layouts = data.boards.layouts || {};
  const layoutName = cfg.layout || data.boards.default_layout?.[String(P)];
  const layout = !cfg.boards && layouts[layoutName] ? layouts[layoutName] : null;
  const ids = layout ? layout.boards : (cfg.boards || BOARD_IDS.slice(0, P));
  st.layout = layout ? layoutName : null;
  const boards = ids.map((b) => data.boards.boards.find((x) => x.id === b));
  const extra = {};
  const pairs = layout ? layout.links : ids.flatMap((b, i) => (data.boards.links || {})[`${b}-${ids[i + 1]}`] || []);
  for (const [x, y] of pairs) { (extra[x] ??= []).push(y); (extra[y] ??= []).push(x); }
  boards.forEach((b, bi) => {
    for (const s of b.sections) {
      const adj = [...s.adjacent, ...(extra[s.id] || [])];
      if (!data.boards.links) {
        if (s.col === 3 && bi + 1 < P) adj.push(`${BOARD_IDS[bi + 1]}${s.row * 4 + 1}`);
        if (s.col === 0 && bi > 0) adj.push(`${BOARD_IDS[bi - 1]}${s.row * 4 + 4}`);
      }
      st.sections[s.id] = {
        id: s.id, board: b.id, type: s.type, hull: s.hull, adj,
        glitch: s.setup.glitch, fault: s.setup.fault, failure: s.setup.failure,
        crew: s.setup.crew, decay: s.setup.decay, influence: {},
        brace: 0, quarantine: 0, patch: 0, lockout: 0, unrest: 0, isolate: 0, dmg: 0,
      };
      st.order.push(s.id);
    }
  });
  // houses
  cfg.houses.slice(0, P).forEach((hid, i) => {
    const hd = data.houses.houses.find((x) => x.id === hid);
    if (!hd) throw new Error(`unknown house ${hid}`);
    st.houses.push({
      id: hid, credits: cfg.startCredits, track: { credits: 0, plays: 0 },
      hand: [], cloned: [], played: [], nominee: null, fast: [], extraDraw: 0, perkFast: 0,
      elements: {}, innateTier: 0,
    });
    st.stats.houses.push({ id: hid, innateTiers: [0, 0, 0, 0], thresholdMet: 0, thresholdTried: 0,
      played: 0, creditsSpent: 0, uncoverGens: [], remarkables: 0, nominated: 0, chosenLeader: 0,
      overclockFast: 0, growth: { A: 0, B: 0, C: 0 }, gensValue: [] });
    placeStartingInfluence(st, i, hd, boards[i]);
  });
  // decks
  const people = data.people;
  st.decks.common = shuffle(st, people.filter((c) => c.tier === "Common").map((c) => c.id));
  st.decks.remarkable = shuffle(st, people.filter((c) => c.tier === "Remarkable").map((c) => c.id));
  st.decks.commonDiscard = []; st.decks.remarkableDiscard = [];
  const ev = data.events.cards;
  const dest = activeDestination(data, cfg);
  st.dest = dest;
  st.landfallMode = cfg.landfallCard === "shuffled" ? "shuffled" : cfg.landfallCard ? "choice" : null;
  const counts = { ...cfg.stageCounts };
  for (const [k, v] of Object.entries(dest.deck)) counts[k] = Math.max(0, (counts[k] || 0) + v);
  let deck = [];
  for (const stage of [3, 2, 1]) {
    const pool = shuffle(st, ev.filter((e) => e.stage === stage).map((e) => e.id));
    const dealt = pool.slice(0, counts[stage]);
    if (stage === 2 && dealt.length) st.escalationEvent = dealt[0]; // one dealt Stage II card carries Escalation
    if (stage === 3 && cfg.landfallCard === "shuffled") {
      // Landfall variant: the Landfall card is shuffled into the Stage III events.
      dealt.splice(Math.floor(nextRand(st) * (dealt.length + 1)), 0, "LANDFALL");
    }
    deck.push(...dealt);
  }
  st.decks.events = deck; // pop() draws from the end: Stage I first
  applyDestinationSetup(st, dest, boards);
  if (cfg.crewRequirementPerPlayer)
    dest.requirement.minCrewPerPlayer = Math.max(dest.requirement.minCrewPerPlayer || 0, cfg.crewRequirementPerPlayer);
  st.decks.discoveries = shuffle(st, data.discoveries.map((d) => d.id));
  st.crisisId = pick(st, data.crisis.cards).id;
  st.wallSize = deck.length + 1;
  return { st, cfg };
}

// ============================================================== destinations
// Collects the cumulative effects of levels 1..L of the chosen destination.
export function activeDestination(data, cfg) {
  const out = { id: null, rules: {}, requirement: {}, escalation: [], deck: {}, setup: [], texts: [] };
  const d = (data.destinations?.destinations || []).find((x) => x.id === cfg.destination);
  if (!d || !cfg.destinationLevel) return out;
  out.id = d.id; out.name = d.name;
  for (const lv of d.levels.filter((l) => l.level <= cfg.destinationLevel)) {
    out.texts.push(`L${lv.level}: ${lv.text}`);
    for (const r of lv.rules || []) out.rules[r] = (out.rules[r] || 0) + 1;
    Object.assign(out.requirement, lv.requirement || {});
    if (lv.escalation) out.escalation.push(lv.escalation);
    for (const [k, v] of Object.entries(lv.deck || {})) out.deck[k] = (out.deck[k] || 0) + v;
    out.setup.push(...(lv.setup || []));
  }
  return out;
}
function applyDestinationSetup(st, dest, boards) {
  for (const sp of dest.setup) {
    for (const b of boards) {
      if (sp.boards && !sp.boards.includes(b.id)) continue;
      const secs = b.sections.map((x) => st.sections[x.id])
        .filter((x) => (sp.type === "Hull" ? x.hull : x.type === sp.type) && (!sp.hullOnly || x.hull));
      const list = sp.all ? secs : secs.slice(0, sp.perBoard ?? 1);
      for (const x of list) x[sp.piece] += 1;
    }
  }
}
export function destinationRequirementMet(st) {
  const r = st.dest?.requirement || {};
  if (r.minCrewPerPlayer && allSections(st).reduce((n, s) => n + s.crew, 0) < r.minCrewPerPlayer * st.houses.length) return false;
  if (r.noDecayIn && allSections(st).some((s) => s.type === r.noDecayIn && s.decay > 0)) return false;
  if (r.minTier && st.tier < r.minTier) return false;
  return true;
}
function escalate(G, st) {
  for (const e of st.dest.escalation) {
    if (e.addGlitchType) for (const s of allSections(st)) if (e.addGlitchType === "Hull" ? s.hull : s.type === e.addGlitchType) s.glitch += 1;
    if (e.unrestHullThreat) for (const s of allSections(st)) if (s.hull && threatCount(s) > 0) s.unrest += 1;
    if (e.losePurpose) losePurpose(st, e.losePurpose);
  }
  log(G, st, "Escalation");
}

// Starting influence goes where the house's rule allows, choosing the sections a player would:
// the most threat and Crew within reach (the section plus its in-board neighbors).
function placeStartingInfluence(st, h, hd, board) {
  const secs = board.sections.map((s) => st.sections[s.id]);
  const add = (s, n = 1) => { s.influence[h] = (s.influence[h] || 0) + n; };
  const near = (s) => [s, ...s.adj.map((a) => st.sections[a]).filter((x) => x.board === board.id)];
  const value = (s) => near(s).reduce((n, x) => n + x.glitch + 2 * x.fault + 3 * x.failure + 0.5 * x.crew, 0) + s.id.charCodeAt(1) * 1e-3;
  const best = (list) => list.slice().sort((x, y) => value(y) - value(x));
  const r = hd.starting_influence.rule;
  if (r.hull) best(secs.filter((s) => s.hull)).slice(0, r.count).forEach((s) => add(s));
  else if (r.first_type) {
    const first = best(secs.filter((s) => s.type === r.first_type))[0]; add(first);
    add(best(first.adj.map((a) => st.sections[a]).filter((x) => x.board === board.id))[0]);
  } else if (r.same_section) add(best(secs.filter((s) => s.type === r.type))[0], r.count);
  else if (r.types) r.types.forEach((t) => add(best(secs.filter((s) => s.type === t))[0]));
}

// ============================================================== helpers
function cardStat(st, cid) {
  st.stats.cards ??= {};
  return (st.stats.cards[cid] ??= { drawn: 0, played: 0, nominated: 0, leader: 0 });
}
export const houseData = (G, st, h) => G.data.houseById[st.houses[h].id];
export const card = (G, id) => G.data.cardById[id];

function trackValue(track, pos) {
  let v = 0;
  for (let i = 0; i <= pos; i++) if (typeof track[i] === "number") v = track[i];
  return v;
}
function trackSpecials(track, pos) {
  return track.slice(0, pos + 1).filter((x) => typeof x === "object");
}
export function houseStats(G, st, h) {
  const hd = houseData(G, st, h), H = st.houses[h];
  const specials = [...trackSpecials(hd.tracks.credits, H.track.credits),
                    ...trackSpecials(hd.tracks.plays, H.track.plays)];
  const raw = {};
  let fastPlays = 0, clone = hd.clone, draw = 0;
  for (const sp of specials) {
    if (sp.element) raw[sp.element] = (raw[sp.element] || 0) + 1;
    if (sp.fast_play) fastPlays += sp.fast_play;
    if (sp.clone) clone += sp.clone;
    if (sp.draw) draw += sp.draw;
  }
  // Wall bonuses (Breakthroughs on retired leaders) apply to every house.
  const wb = wallBonuses(G, st);
  for (const [g, n] of Object.entries(wb.elements)) raw[g] = (raw[g] || 0) + n;
  fastPlays += wb.fast_play;
  draw += wb.extra_draw;
  const plays = trackValue(hd.tracks.plays, H.track.plays);
  return { income: trackValue(hd.tracks.credits, H.track.credits) + wb.credits_per_growth, plays,
           hand: plays + hd.hand_bonus + draw, raw, fastPlays, clone, draw };
}
export function canUncover(G, st, h, track) {
  const hd = houseData(G, st, h);
  return st.houses[h].track[track] < hd.tracks[track].length - 1;
}

export function eventOf(slot) { return slot ? slot.event : null; }
export const eventTypes = (G, eid) => (eid ? G.data.eventById[eid].types : null);

// Legal target sections for a card / innate for house h.
export function legalTargets(G, st, h, tgt) {
  if (tgt.kind === "house") return st.houses.map((_, i) => i).filter((i) => i !== h || st.houses.length === 1);
  if (tgt.range === null || tgt.range === undefined) return ["global"];
  let ids = inRange(st, h, tgt.range);
  if (G.cfg.havenRangeBonus) {
    const meridian = st.houses[h].id === "meridian";
    const havens = st.order.filter((id) => (st.sections[id].influence[h] || 0) >= 2 ||
      (meridian && st.sections[id].type === "Agricultural" && (st.sections[id].influence[h] || 0) > 0));
    if (havens.length) {
      const d = distances(st, havens);
      for (const id of st.order) if (d[id] !== undefined && d[id] <= tgt.range + G.cfg.havenRangeBonus && !ids.includes(id)) ids.push(id);
    }
  }
  if (st.houses[h].id === "vigil" && st.houses[h].credits >= 1) {
    const crewSecs = st.order.filter((id) => st.sections[id].crew > 0);
    const d = distances(st, crewSecs);
    const extra = st.order.filter((id) => d[id] !== undefined && d[id] <= tgt.range && !ids.includes(id));
    ids = ids.concat(extra.map((id) => `${id}*`)); // * = pay 1 credit (Voices Among the Crew)
  }
  return ids.filter((id) => targetFilter(st, st.sections[id.replace("*", "")], tgt.type || "ANY"));
}

// ============================================================== card play
export function elementsMet(H, req) {
  return Object.entries(req).every(([g, n]) => (H.elements[g] || 0) >= n);
}

// A card's own guilds never count toward its own threshold: the bonus needs help from
// other cards, track slots or the Wall.
export function thresholdMet(G, H, c) {
  if (!c.threshold) return false;
  const el = { ...H.elements };
  for (const g of c.guilds) el[g] = (el[g] || 0) - 1;
  return Object.entries(c.threshold.elements).every(([g, n]) => (el[g] || 0) >= n);
}
// Verbs that act on the playing house or the whole ship, so need no target.
const GLOBAL_VERBS = new Set(["purpose", "credits", "foresee", "temper_legacy"]);
const HOUSE_GLOBAL_VERBS = new Set(["purpose"]);
export function needsTarget(c, effects) {
  const g = c.target.kind === "house" ? HOUSE_GLOBAL_VERBS : GLOBAL_VERBS;
  return Object.keys(effects).some((v) => !g.has(v));
}
export function cardEffects(G, st, h, cid) {
  const c = card(G, cid);
  const effects = { ...c.effects };
  const met = thresholdMet(G, st.houses[h], c);
  if (met) for (const [v, n] of Object.entries(c.threshold.effects)) effects[v] = (effects[v] || 0) + n;
  return { effects, met };
}

export function resolveCard(G, st, h, cid) {
  const c = card(G, cid);
  const H = st.houses[h], HS = st.stats.houses[h];
  const { effects, met } = cardEffects(G, st, h, cid);
  if (c.threshold) {
    HS.thresholdTried += 1;
    const need = Object.values(c.threshold.elements).reduce((x, y) => x + y, 0);
    const byN = (st.stats.thresholdByN ??= {});
    byN[need] ??= [0, 0]; byN[need][0] += 1;
    if (met) { byN[need][1] += 1; HS.thresholdMet += 1; }
  }
  if (!needsTarget(c, effects)) {
    log(G, st, `${H.id} plays ${cid}`);
    if (c.target.kind === "house") applyHouseEffects(G, st, h, h, effects);
    else applySectionEffects(G, st, h, null, effects);
    return;
  }
  const opts = legalTargets(G, st, h, c.target);
  if (!opts.length) return;
  const t = G.choose(st, h, "cardTarget", opts, { card: cid });
  log(G, st, `${H.id} plays ${cid} → ${c.target.kind === "house" ? st.houses[t].id : t}`);
  if (c.target.kind === "house") applyHouseEffects(G, st, h, t, effects);
  else {
    let id = t;
    if (id.endsWith("*")) { id = id.slice(0, -1); H.credits -= 1; }
    applySectionEffects(G, st, h, st.sections[id], effects);
  }
}

export function resolveInnate(G, st, h) {
  const hd = houseData(G, st, h), H = st.houses[h];
  let best = null;
  for (const t of hd.innate.tiers) if (elementsMet(H, t.threshold)) best = t;
  st.stats.houses[h].innateTiers[best ? best.tier : 0] += 1;
  if (!best) return;
  log(G, st, `${H.id} innate ${hd.innate.name} tier ${best.tier}`);
  if (best.range === null) {
    for (const [v, n] of Object.entries(best.effects)) {
      if (v === "purpose") gainPurpose(G, st, n, "innate");
      else if (v === "foresee") st.stats.foresee += 1;
      else if (v === "temper_legacy") { if (st.slots.dusk) st.slots.dusk.tempered = true; }
    }
    return;
  }
  const opts = legalTargets(G, st, h, { kind: "section", range: best.range, type: best.target });
  if (!opts.length) return;
  let id = G.choose(st, h, "innateTarget", opts, { tier: best.tier });
  if (id.endsWith("*")) { id = id.slice(0, -1); H.credits -= 1; }
  applySectionEffects(G, st, h, st.sections[id], best.effects);
}

// ============================================================== threat actions
function seedSection(G, st, s) {
  if (s.quarantine) return;
  if (s.lockout > 0) { s.lockout -= 1; return; }
  s.glitch += G.cfg.seedGlitches + (s.hull && st.dest?.rules.hull_seed_extra ? 1 : 0);
}
export function seed(G, st, eid) {
  const ev = G.data.eventById[eid];
  const targets = new Set();
  for (const s of allSections(st)) {
    if (!matches(s, ev.types)) continue;
    const src = s.hull || s.adj.some((a) => !st.sections[a].quarantine && st.sections[a].fault + st.sections[a].failure > 0);
    if (src) targets.add(s.id);
    if (ev.twist?.rule === "seed_adjacent" && threatCount(s) > 0) s.adj.forEach((a) => targets.add(a));
  }
  for (const id of targets) seedSection(G, st, st.sections[id]);
}
export function grow(G, st, eid) {
  const ev = G.data.eventById[eid];
  for (const s of allSections(st)) {
    if (!matches(s, ev.types) || threatCount(s) === 0) continue;
    if (s.patch > 0) { s.patch -= 1; continue; }
    if (s.fault >= 2) s.failure += 1;
    else {
      s.fault += 1;
      if (ev.twist?.rule === "grow_adds_glitch") s.glitch += 1;
      if (st.dest?.rules.agri_grow_spread && s.type === "Agricultural") {
        const tgt = s.adj.map((a) => st.sections[a]).filter((x) => !x.quarantine)
          .sort((a, b) => threatCount(a) - threatCount(b))[0];
        if (tgt) tgt.glitch += 1;
      }
    }
  }
  if (st.crisisFlipped && st.crisisId === "X4")
    for (const s of allSections(st)) if (s.decay > 0 && threatCount(s) === 0) s.glitch += 1;
}
export function collapse(G, st, eid) {
  const ev = G.data.eventById[eid];
  const surge = ev.twist?.rule === "faults_plus_one" ? 1 : 0;
  for (const s of allSections(st)) {
    if (st.result) return;
    if (!matches(s, ev.types) || threatCount(s) === 0) continue;
    let dmg = s.glitch + s.fault * (2 + surge) + s.failure * 3 + (s.unrest > 0 ? 1 : 0)
      + (s.hull && st.dest?.rules.hull_collapse_plus ? 1 : 0);
    const neg = Math.min(dmg, s.isolate); dmg -= neg; s.isolate = 0;
    const br = Math.min(dmg, s.brace); dmg -= br; s.brace -= br;
    log(G, st, `Collapse in ${s.id}: ${dmg} damage${dmg >= G.cfg.decayThreshold ? ", Decay" : ""}`);
    if (dmg >= G.cfg.decayThreshold) placeDecay(G, st, s);
    let killed = Math.min(s.crew, Math.floor(dmg / G.cfg.crewHealth));
    if (ev.twist?.rule === "extra_crew_loss") killed = Math.min(s.crew, killed + 1);
    if (st.dest?.rules.agri_collapse_crew && s.type === "Agricultural") killed = Math.min(s.crew, killed + st.dest.rules.agri_collapse_crew);
    s.crew -= killed; st.stats.crewLost += killed;
    if (s.crew > 0) {
      // Foremen's Crew Captains: Crew in sections with Foremen influence deal +1 damage each.
      const fi = st.houses.findIndex((H) => H.id === "foremen");
      const bonus = fi >= 0 && (s.influence[fi] || 0) > 0 ? 1 : 0;
      damageThreat(G, st, s, s.crew * (G.cfg.crewDamage + bonus), "crew");
    }
  }
}

// ============================================================== leaders
export function applyReign(G, st) {
  const L = st.slots.day; if (!L) return;
  const c = card(G, L.leader), types = eventTypes(G, L.event);
  for (const [v, n] of Object.entries(c.reign.effects)) {
    if (v === "purpose") gainPurpose(G, st, n, "reign");
    else if (v === "credits_each_house") st.houses.forEach((H) => (H.credits += n));
    else for (const s of allSections(st)) {
      if (!matches(s, types)) continue;
      if (v === "brace") s.brace += n;
      else if (v === "patch") s.patch += n;
      else if (v === "lockout") s.lockout += n;
      else if (v === "gather_crew") gatherCrew(G, st, stewardHouse(st), s, n);
      else if (v === "damage") damageThreat(G, st, s, n, "reign");
    }
  }
}
export function applyLegacy(G, st) {
  const L = st.slots.dusk; if (!L) return;
  const c = card(G, L.leader), types = eventTypes(G, L.event);
  const eff = { ...c.legacy.effects };
  if (L.tempered) {
    // ignore the costliest effect
    const PRICE = { add_glitch: 1, add_fault: 2, add_failure: 3, destroy_crew: 3, add_decay: 4,
      lose_influence: 2, add_unrest: 1.5, lose_purpose: 1, lose_credits_each_house: 1 };
    const worst = Object.keys(eff).sort((a, b) => PRICE[b] * eff[b] - PRICE[a] * eff[a])[0];
    if (worst) delete eff[worst];
    st.stats.legacyTempered += 1;
  }
  for (const [v, n] of Object.entries(eff)) {
    if (st.result) return;
    if (v === "lose_purpose") losePurpose(st, n);
    else if (v === "lose_credits_each_house") st.houses.forEach((H) => (H.credits = Math.max(0, H.credits - n)));
    else for (const s of allSections(st)) {
      if (!matches(s, types) || st.result) continue;
      if (v === "add_glitch") s.glitch += n;
      else if (v === "add_fault") s.fault += n;
      else if (v === "add_failure") s.failure += n;
      else if (v === "destroy_crew") { const k = Math.min(n, s.crew); s.crew -= k; st.stats.crewLost += k; }
      else if (v === "add_decay") for (let i = 0; i < n; i++) placeDecay(G, st, s);
      else if (v === "lose_influence") {
        for (const hh of Object.keys(s.influence)) s.influence[hh] = Math.max(0, s.influence[hh] - n);
        st.houses.forEach((_, i) => { if (totalInfluence(st, i) <= 0) lose(st, "influence"); });
      } else if (v === "add_unrest") s.unrest += n;
    }
  }
}

// ============================================================== discoveries
const D_REMOVE = (G, st, s, piece, n) => {
  const k = Math.min(n, s[piece]); s[piece] -= k;
  if (piece === "fault") gainPurpose(G, st, k * G.cfg.purposeFault, "discovery");
};
export function applyDiscoveryEffects(G, st, effects, sections, h = 0) {
  for (const [v, n] of Object.entries(effects)) {
    if (["add_crew", "restore_decay"].includes(v)) {
      const opts = v === "restore_decay" ? st.order.filter((id) => st.sections[id].decay > 0) : st.order;
      if (!opts.length) continue;
      const id = G.choose(st, h, v === "add_crew" ? "addCrewAt" : "restoreAt", opts, { n });
      if (v === "add_crew") st.sections[id].crew += n; else restoreDecay(st, st.sections[id], n);
      continue;
    }
    if (v === "purpose") { gainPurpose(G, st, n, "discovery"); continue; }
    if (v === "credits_each") { st.houses.forEach((H) => (H.credits += n)); continue; }
    if (v === "foresee") { st.stats.foresee += 1; continue; }
    for (const s of sections) {
      if (v === "remove_glitch") D_REMOVE(G, st, s, "glitch", n);
      else if (v === "remove_fault") D_REMOVE(G, st, s, "fault", n);
      else if (v === "downgrade_fault") downgrade(s, "fault", n);
      else if (v === "downgrade_failure") downgrade(s, "failure", n);
      else if (v === "damage") damageThreat(G, st, s, n, "discovery");
      else if (v === "skip_grow") s.patch += 1;
      else if (v === "skip_seed") s.lockout += 1;
      else if (v === "brace") s.brace += n;
      else if (v === "gather_crew") gatherCrew(G, st, h, s, n);
    }
  }
}
// Discoveries earned while resolving Discoveries wait for the next Dusk.
// The Steward's house decides: apply now, or put it under the Steward as a Breakthrough
// (a passive Wall bonus once that leader retires to the Wall).
function resolveDiscoveries(G, st) {
  const batch = st.pendingDiscoveries.splice(0);
  const who = stewardHouse(st);
  for (const did of batch) {
    if (st.result) { st.pendingDiscoveries.push(did); continue; }
    const canBT = st.slots.day && !st.slots.day.bt;
    const choice = canBT ? G.choose(st, who, "discovery", ["apply", "breakthrough"], { id: did }) : "apply";
    log(G, st, `Discovery ${did}: ${choice}`);
    if (choice === "breakthrough") {
      st.slots.day.bt = did; st.breakthroughs.push(did); st.stats.discoveryBreakthrough += 1;
    } else {
      applyDiscovery(G, st, did, who);
      st.stats.discoveryApplied += 1;
    }
  }
}
export const discoveryTier = (G, st, did) => G.data.discoveryById[did].tiers[["I", "II", "III"][st.tier - 1]];
const LOCAL_D = new Set(["remove_glitch", "remove_fault", "downgrade_fault", "downgrade_failure", "damage", "skip_grow", "skip_seed", "brace", "gather_crew"]);
// Section effects land in one section of the Steward's choice on each board.
function applyDiscovery(G, st, did, who) {
  const t = discoveryTier(G, st, did);
  const local = Object.fromEntries(Object.entries(t.effects).filter(([v]) => LOCAL_D.has(v)));
  const other = Object.fromEntries(Object.entries(t.effects).filter(([v]) => !LOCAL_D.has(v)));
  applyDiscoveryEffects(G, st, other, [], who);
  if (!Object.keys(local).length) return;
  const boards = [...new Set(st.order.map((id) => st.sections[id].board))];
  for (const b of boards) {
    if (st.result) return;
    const opts = st.order.filter((id) => st.sections[id].board === b);
    const id = G.choose(st, who, "discoveryAt", opts, { id: did, board: b, effects: local });
    applyDiscoveryEffects(G, st, local, [st.sections[id]], who);
  }
}

// ============================================================== phases
function growthPhase(G, st) {
  st.houses.forEach((H, h) => {
    const HS = st.stats.houses[h], hd = houseData(G, st, h);
    H.extraDraw = 0; H.perkFast = 0;
    const choice = G.choose(st, h, "growth", ["A", "B", "C"], {});
    HS.growth[choice] += 1;
    log(G, st, `${H.id} growth ${choice}`);
    if (choice === "A") {
      const tracks = ["credits", "plays"].filter((t) => canUncover(G, st, h, t));
      const range = hd.growth_overrides?.A?.range ?? 1;
      const count = hd.growth_overrides?.A?.influence ?? 1;
      let opts = inRange(st, h, range);
      if (H.id === "voidwardens") opts = opts.filter((id) => nearHull(st, st.sections[id]));
      for (let k = 0; k < count && opts.length; k++) {
        const id = G.choose(st, h, "growthInfluence", opts, {});
        st.sections[id].influence[h] = (st.sections[id].influence[h] || 0) + 1;
      }
      if (tracks.length) {
        const t = G.choose(st, h, "track", tracks, {});
        H.track[t] += 1; HS.uncoverGens.push(st.gen);
      }
    } else if (choice === "B") {
      H.credits += 2;
      if (H.id === "galvan") H.perkFast = 1;
      if (H.id === "keel") for (const s of allSections(st)) if ((s.influence[h] || 0) >= 2) s.brace += 1;
    } else {
      H.extraDraw = 2;
      if (H.id === "vigil") gainPurpose(G, st, 1, "growth"); else H.credits += 1;
    }
    const hs = houseStats(G, st, h);
    H.credits += hs.income;
    // draw
    let n = hs.hand + H.extraDraw;
    const canRem = G.cfg.remarkableAccess !== "growthC" || choice === "C";
    const rem = canRem ? Math.min(G.cfg.remarkablePerGeneration,
      G.choose(st, h, "remarkables", [0, 1], { handSize: n })) : 0;
    H.hand = [...H.cloned]; H.cloned = [];
    for (let i = 0; i < rem && n >= 2; i++) { H.hand.push(drawFrom(st, "remarkable", "remarkableDiscard")); n -= 2; HS.remarkables += 1; }
    for (let i = 0; i < n; i++) H.hand.push(drawFrom(st, "common", "commonDiscard"));
    if (G.cfg.trackCards) for (const cid of H.hand) cardStat(st, cid).drawn += 1;
  });
}

// Voidwardens may only add influence on or next to the Outer Hull.
export const nearHull = (st, s) => s.hull || s.adj.some((a) => st.sections[a].hull);

function costOf(G, cid) { return card(G, cid).cost; }

// Apply a commit plan {play, nominee, fast} for house h (also used by bot rollouts).
export function applyPlan(G, st, h, plan) {
  const H = st.houses[h], hs = houseStats(G, st, h), HS = st.stats.houses[h];
  let spend = 0;
  for (const cid of plan.play) if (!(G.cfg.nomineeFree && cid === plan.nominee)) spend += costOf(G, cid);
  if (plan.play.length > hs.plays || spend > H.credits) throw new Error(`illegal commit by ${H.id}`);
  H.credits -= spend; HS.creditsSpent += spend; HS.played += plan.play.length;
  if (G.cfg.trackCards) for (const cid of plan.play) { cardStat(st, cid).played += 1; if (cid === plan.nominee) cardStat(st, cid).nominated += 1; }
  H.played = plan.play; H.nominee = plan.nominee;
  H.hand = H.hand.filter((c) => !plan.play.includes(c));
  H.elements = { ...hs.raw };
  for (const cid of plan.play) for (const g of card(G, cid).guilds) H.elements[g] = (H.elements[g] || 0) + 1;
  let fastCount = 1 + hs.fastPlays + H.perkFast;
  if (H.id === "galvan") fastCount += H.elements.Engineers || 0;
  const others = plan.play.filter((c) => c !== plan.nominee);
  const extra = (plan.fast || []).filter((c) => others.includes(c)).slice(0, fastCount - 1);
  HS.overclockFast += extra.length;
  H.fast = plan.nominee ? [plan.nominee, ...extra] : extra;
  if (plan.nominee) HS.nominated += 1;
}

function commitPhase(G, st) {
  st.houses.forEach((H, h) => {
    const hs = houseStats(G, st, h);
    const plan = G.choose(st, h, "commit", null, { plays: hs.plays });
    applyPlan(G, st, h, plan);
  });
}

// Each house resolves its cards (and its innate, in its speed) in the order it chooses.
function speedPhase(G, st, fast) {
  st.houses.forEach((H, h) => {
    const left = fast ? [...H.fast] : H.played.filter((c) => !H.fast.includes(c));
    if ((houseData(G, st, h).innate.speed === "fast") === fast) left.push("innate");
    while (left.length && !st.result) {
      const next = left.length > 1 ? G.choose(st, h, "playOrder", [...left], { fast }) : left[0];
      left.splice(left.indexOf(next), 1);
      if (next === "innate") resolveInnate(G, st, h); else resolveCard(G, st, h, next);
    }
  });
}

function duskPhase(G, st) {
  resolveDiscoveries(G, st);
  const wb = wallBonuses(G, st);
  if (wb.hull_brace) for (const s of allSections(st)) if (s.hull) s.brace += wb.hull_brace;
  if (wb.purpose_per_gen) gainPurpose(G, st, wb.purpose_per_gen, "wall");
  // Keel: Load-Bearing
  st.houses.forEach((H, h) => {
    if (H.id === "keel") for (const s of allSections(st)) {
      const n = s.influence[h] || 0;
      if (n >= 2) s.brace += 2; else if (n === 1) s.brace += 1;
    }
  });
  applyLegacy(G, st);
  if (st.slots.dusk?.event && !st.result) collapse(G, st, st.slots.dusk.event);
}
function dayPhase(G, st) {
  if (st.dest?.rules.purpose_drain) losePurpose(st, st.dest.rules.purpose_drain);
  if (st.crisisFlipped && st.crisisId === "X1") st.houses.forEach((H) => (H.credits = Math.max(0, H.credits - 1)));
  applyReign(G, st);
  if (st.slots.day?.event) grow(G, st, st.slots.day.event);
}
function drawEvent(st) {
  if (st.landfallPending) { st.landfallPending = false; st.landfallPlaced = true; return "LANDFALL"; }
  if (!st.decks.events.length) {
    if (st.landfallPlaced && st.landfallMode !== "shuffled") return "NONE"; // the voyage is ending: no new events
    lose(st, "time"); return null;
  }
  const e = st.decks.events.pop();
  if (e === "LANDFALL") st.landfallPlaced = true;
  return e;
}
function dawnPhase(G, st) {
  let eid = null;
  if (G.cfg.eventPairing === "direct") { eid = drawEvent(st); if (!eid) return; st.upcomingEvent = eid === "NONE" ? null : eid; }
  const noms = st.houses.map((H, h) => ({ h, cid: H.nominee })).filter((x) => x.cid);
  let chosen = null;
  if (noms.length) {
    const votes = st.houses.map((_, h) => G.choose(st, h, "vote", noms.map((n) => n.cid), {}));
    const tally = {};
    votes.forEach((v) => (tally[v] = (tally[v] || 0) + 1));
    const max = Math.max(...Object.values(tally));
    let top = Object.keys(tally).filter((k) => tally[k] === max);
    if (top.length > 1) {
      // Ties: the nominee whose house holds the fewest leaders on the conveyor (Day + Dusk);
      // if still tied, the Steward's house decides.
      const held = (cid) => { const hh = noms.find((n) => n.cid === cid).h;
        return ["day", "dusk"].filter((k) => st.slots[k]?.house === hh).length; };
      const least = Math.min(...top.map(held));
      top = top.filter((c) => held(c) === least);
    }
    chosen = top.length === 1 ? top[0] : G.choose(st, stewardHouse(st), "tiebreak", top, { votes });
    const winner = noms.find((n) => n.cid === chosen);
    st.stats.houses[winner.h].chosenLeader += 1;
    if (G.cfg.trackCards) cardStat(st, chosen).leader += 1;
    for (const n of noms) if (n.cid !== chosen) discard(G, st, n.cid);
  } else {
    chosen = drawFrom(st, "common", "commonDiscard");
  }
  if (G.cfg.eventPairing !== "direct") { eid = drawEvent(st); if (!eid) return; }
  if (eid === "NONE") eid = null;
  st.upcomingEvent = null;
  const house = noms.find((n) => n.cid === chosen)?.h ?? 0;
  st.slots.dawn = { leader: chosen, event: eid, house, bt: null, tempered: false };
  log(G, st, `New heir ${chosen} (${st.houses[house]?.id}); ${eid ? `event ${eid} (${G.data.eventById[eid].types.join("+")}) seeds` : "no event"}`);
  if (eid) seed(G, st, eid);
  if (eid && eid === st.escalationEvent && st.dest?.escalation.length) escalate(G, st);
}
function discard(G, st, cid) {
  const c = card(G, cid);
  st.decks[c.tier === "Common" ? "commonDiscard" : "remarkableDiscard"].push(cid);
}
function timePasses(G, st) {
  if (st.slots.dusk) {
    st.wall.push(st.slots.dusk);
    if (st.slots.dusk.bt) log(G, st, `Wall bonus on: ${G.data.discoveryById[st.slots.dusk.bt].breakthrough.text}`);
    if (st.slots.dusk.event === "LANDFALL" && !st.result) {
      // Landfall retires: chosen Landfall wins outright; shuffled Landfall wins if the ship is ready.
      if (st.landfallMode !== "shuffled" || (winConditionMet(st, G.cfg.tierConditions) && destinationRequirementMet(st)))
        st.result = { outcome: "win", cause: "Landfall", gen: st.gen };
      else log(G, st, "Landfall passes: the ship is not ready to land");
    }
  }
  st.slots.dusk = st.slots.day; st.slots.day = st.slots.dawn; st.slots.dawn = null;
  for (const s of allSections(st)) { s.brace = 0; s.quarantine = 0; s.dmg = 0; }
  st.houses.forEach((H, h) => {
    // the nominee was either chosen as leader or discarded during the Dawn vote
    for (const cid of H.played) if (cid !== H.nominee) discard(G, st, cid);
    const hs = houseStats(G, st, h);
    const keep = G.choose(st, h, "clone", H.hand, { slots: hs.clone }) || [];
    H.cloned = keep.slice(0, hs.clone);
    for (const cid of H.hand) if (!H.cloned.includes(cid)) discard(G, st, cid);
    H.hand = []; H.played = []; H.nominee = null; H.fast = [];
  });
}

// ============================================================== loop
export function setupRamp(G, st) {
  st.phase = "setup";
  const eid = drawEvent(st);
  const leader = drawFrom(st, "common", "commonDiscard");
  st.slots.dawn = { leader, event: eid, house: 0, bt: null, tempered: false, start: true };
  seed(G, st, eid);
  log(G, st, `Voyage begins: starting Steward ${leader} carries event ${eid} (${G.data.eventById[eid].types.join("+")}), which has Seeded; it Grows this Day and Collapses next Dusk`);
  st.slots.day = st.slots.dawn; st.slots.dawn = null;
}

export const PHASES = ["growth", "commit", "fast", "dusk", "day", "dawn", "slow", "time"];
export function runPhase(G, st, phase) {
  st.phase = phase;
  if (phase === "growth") log(G, st, `── Generation ${st.gen} ──`);
  switch (phase) {
    case "growth": growthPhase(G, st); break;
    case "commit": commitPhase(G, st); break;
    case "fast": speedPhase(G, st, true); break;
    case "dusk": duskPhase(G, st); break;
    case "day": dayPhase(G, st); break;
    case "dawn": dawnPhase(G, st); break;
    case "slow": speedPhase(G, st, false); break;
    case "time": timePasses(G, st); break;
  }
  checkVictory(G, st);
}

// Base win, or with the Landfall card toggle: meeting the condition schedules the Landfall event.
export function checkVictory(G, st) {
  if (st.result) return;
  if (!winConditionMet(st, G.cfg.tierConditions) || !destinationRequirementMet(st)) return;
  if (!G.cfg.landfallCard) { st.result = { outcome: "win", cause: `tier ${st.tier}`, gen: st.gen }; return; }
  if (G.cfg.landfallCard === "shuffled") return; // the Landfall card arrives with the events
  if (!st.landfallPending && !st.landfallPlaced && !st.landfallDeclinedGen?.includes?.(st.gen)) {
    const go = G.choose(st, stewardHouse(st), "landfall", ["begin", "wait"], {});
    if (go === "begin") { st.landfallPending = true; log(G, st, "Landfall will begin at the next Dawn"); }
    else (st.landfallDeclinedGen ??= []).push(st.gen);
  }
}

export function playGame(data, agents, cfgIn = {}, seed = 1, verbose = false) {
  const { st, cfg } = createGame(data, cfgIn, seed);
  const G = makeContext(data, cfg, agents, verbose);
  setupRamp(G, st);
  while (!st.result) {
    st.gen += 1;
    if (st.gen > cfg.maxGenerations) { lose(st, "stalled"); break; }
    for (const p of PHASES) { runPhase(G, st, p); if (st.result) break; }
  }
  return st;
}

export function makeContext(data, cfg, agents, verbose = false) {
  const G = { data, cfg, agents, verbose };
  G.choose = (st, h, kind, options, ctx) => agents[h % agents.length].choose(G, st, h, kind, options, ctx);
  return G;
}
