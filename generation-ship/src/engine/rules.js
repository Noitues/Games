// Core rules: board queries, effects, threat actions, Decay, Purpose.
// All functions take (G, st): G = {data, cfg, agents}, st = plain-JSON game state.
import { shuffle } from "./rng.js";

// ------------------------------------------------------------ board queries
export const threatCount = (s) => s.glitch + s.fault + s.failure;
export const sec = (st, id) => st.sections[id];
export const allSections = (st) => st.order.map((id) => st.sections[id]);

export function matches(s, types) {
  if (!types) return false;
  return types.some((t) => t === "ALL" || t === s.type || (t === "Hull" && s.hull));
}

export function distances(st, fromIds) {
  const dist = {};
  const q = [];
  for (const id of fromIds) { dist[id] = 0; q.push(id); }
  while (q.length) {
    const id = q.shift();
    for (const a of st.sections[id].adj) {
      if (dist[a] === undefined) { dist[a] = dist[id] + 1; q.push(a); }
    }
  }
  return dist;
}

export const influenceSections = (st, h) =>
  st.order.filter((id) => (st.sections[id].influence[h] || 0) > 0);
export const totalInfluence = (st, h) =>
  st.order.reduce((n, id) => n + (st.sections[id].influence[h] || 0), 0);

export function inRange(st, h, range, extraSources = []) {
  const d = distances(st, [...influenceSections(st, h), ...extraSources]);
  return st.order.filter((id) => d[id] !== undefined && d[id] <= range);
}

export function targetFilter(st, s, type) {
  switch (type) {
    case "ANY": return true;
    case "Hull": return s.hull;
    case "section with Crew": return s.crew > 0;
    case "section with Decay": return s.decay > 0;
    case "section with a Failure": return s.failure > 0;
    default: return s.type === type;
  }
}

// The Steward's house makes the table's shared decisions (Discoveries, cascades, Landfall, ties).
// The starting Steward belongs to no house; while it reigns, the first seat decides.
export const stewardHouse = (st) => st.slots?.day?.house ?? 0;

// Passive Wall bonuses: Breakthroughs switch on when their leader retires to the Wall.
export function wallBonuses(G, st) {
  const out = { elements: {}, credits_per_growth: 0, extra_draw: 0, hull_brace: 0, decay_ward: 0, fast_play: 0, purpose_per_gen: 0 };
  for (const L of st.wall || []) {
    if (!L.bt) continue;
    const eff = G.data.discoveryById[L.bt]?.breakthrough?.effects || {};
    for (const [k, v] of Object.entries(eff)) {
      if (k === "element") out.elements[v] = (out.elements[v] || 0) + 1;
      else if (k in out) out[k] += v;
    }
  }
  return out;
}

// Ongoing Legacies: each retired Elder's Legacy stays in force, centred on the sections matching
// its paired event (global drawbacks like credits_tax apply everywhere: pass s = null).
export const LEGACY_GLOBAL = new Set(["credits_tax", "purpose_tax"]);
export function legacyMod(st, s, key) {
  let n = 0;
  for (const L of st.legacies || []) {
    const v = L.effects[key];
    if (!v) continue;
    if (s === null ? LEGACY_GLOBAL.has(key) : !LEGACY_GLOBAL.has(key) && matches(s, L.types)) n += v;
  }
  return n;
}

// ---------------------------------------------------------------- logging
export function log(G, st, msg) {
  if (G.verbose) st.log.push(`G${st.gen} ${st.phase}: ${msg}`);
}

// ---------------------------------------------------------------- results
export function lose(st, cause) {
  if (!st.result) st.result = { outcome: "loss", cause, gen: st.gen };
}
export function checkInfluenceLoss(st) {
  st.houses.forEach((h, i) => { if (totalInfluence(st, i) <= 0) lose(st, "influence"); });
}
export function winConditionMet(st, mode = "shifted") {
  let glitch = 0, fault = 0, failure = 0, decay = 0;
  for (const s of allSections(st)) { glitch += s.glitch; fault += s.fault; failure += s.failure; decay += s.decay; }
  if (mode === "classic") {
    if (st.tier >= 3) return failure === 0;
    if (st.tier === 2) return fault + failure === 0;
    return glitch + fault + failure === 0;
  }
  if (st.tier >= 3) return fault + failure === 0;
  if (st.tier === 2) return glitch + fault + failure === 0;
  return glitch + fault + failure + decay === 0;
}
export function checkWin(st, mode) {
  if (!st.result && winConditionMet(st, mode)) st.result = { outcome: "win", cause: `tier ${st.tier}`, gen: st.gen };
}

// ---------------------------------------------------------------- Purpose
export function gainPurpose(G, st, n, source = "other") {
  if (n <= 0) return;
  st.purpose += n;
  st.stats.purposeBy[source] = (st.stats.purposeBy[source] || 0) + n;
  while (st.purpose >= st.purposeCap) {
    st.purpose -= st.purposeCap;
    if (!st.decks.discoveries.length) break;
    st.pendingDiscoveries.push(st.decks.discoveries.pop());
    st.discoveriesEarned += 1;
    st.tier = Math.min(3, 1 + Math.floor(st.discoveriesEarned / (st.discoveriesPerTier ?? G.cfg.discoveriesPerTier)));
  }
}
export const losePurpose = (st, n) => { st.purpose = Math.max(0, st.purpose - n); };

// ---------------------------------------------------------------- damage
// Player-side damage to threat in a section. Picks the kill set that removes the
// most threat damage output (ties: most Purpose). Leftover damage persists this generation.
export function damageThreat(G, st, s, n, source = "card") {
  if (n <= 0 || threatCount(s) === 0) return;
  if (s.unrest > 0) n += 1;
  if (source !== "crew") n += legacyMod(st, s, "repair_plus");
  let total = n + s.dmg;
  let best = [0, 0, 0], bestScore = -1;
  for (let a = 0; a <= s.failure; a++) for (let b = 0; b <= s.fault; b++) {
    const used = 3 * a + 2 * b;
    if (used > total) break;
    const c = Math.min(s.glitch, total - used);
    const score = (3 * a + 2 * b + c) * 10 + (2 * a + b);
    if (score > bestScore) { bestScore = score; best = [a, b, c]; }
  }
  const [a, b, c] = best;
  s.failure -= a; s.fault -= b; s.glitch -= c;
  s.dmg = threatCount(s) ? total - (3 * a + 2 * b + c) : 0;
  st.stats.destroyed.glitch += c; st.stats.destroyed.fault += b; st.stats.destroyed.failure += a;
  gainPurpose(G, st, b * G.cfg.purposeFault + a * G.cfg.purposeFailure + (a + b) * legacyMod(st, s, "purpose_plus"), source);
}
// Crew in a section strike: each surviving Crew deals its damage (Legacies can make them fiercer).
export const crewDamage = (G, st, s) => G.cfg.crewDamage + legacyMod(st, s, "crew_fierce");

// ---------------------------------------------------------------- Decay
export function placeDecay(G, st, s, depth = 0) {
  if (st.result) return;
  // Gardeners' Rooted: Decay that would land where the Gardeners have influence removes 1 of it instead.
  const gi = st.houses.findIndex((H) => H.id === "gardeners");
  if (gi >= 0 && (s.influence[gi] || 0) > 0 && st.rootedGen !== st.gen) {
    st.rootedGen = st.gen; // once per generation
    s.influence[gi] -= 1;
    st.stats.rooted = (st.stats.rooted || 0) + 1;
    checkInfluenceLoss(st);
    return;
  }
  // Wall bonus: the first Decay(s) each generation go back to the pool.
  const ward = G.data.discoveryById ? wallBonuses(G, st).decay_ward : 0;
  if (ward > 0) {
    if (st.wardGen !== st.gen) { st.wardGen = st.gen; st.wardUsed = 0; }
    if (st.wardUsed < ward) { st.wardUsed += 1; st.stats.warded = (st.stats.warded || 0) + 1; log(G, st, `Decay in ${s.id} warded`); return; }
  }
  if (st.decayPool <= 0) {
    if (!st.crisisFlipped) {
      st.crisisFlipped = true;
      st.decayPool += G.cfg.crisisRefillPerPlayer * st.houses.length;
      log(G, st, `Ship in Crisis flips (${st.crisisId})`);
    } else { lose(st, "decay"); return; }
  }
  st.decayPool -= 1;
  st.stats.decayPlaced += 1;
  log(G, st, `Decay placed in ${s.id}${s.decay > 0 ? " (cascade)" : ""}`);
  const had = s.decay > 0;
  s.decay += 1;
  for (const h of Object.keys(s.influence)) s.influence[h] = Math.max(0, s.influence[h] - 1);
  if (st.crisisFlipped && st.crisisId === "X3") losePurpose(st, 1);
  checkInfluenceLoss(st);
  if (had && !s.quarantine && depth < 20) { // Quarantine: no cascade out of the section
    const n = st.crisisFlipped && st.crisisId === "X2" ? 2 : 1;
    for (let k = 0; k < n; k++) {
      const opts = s.adj.filter((a) => !st.sections[a].quarantine);
      if (!opts.length) break;
      const tgt = G.choose(st, stewardHouse(st), "cascade", opts, { from: s.id });
      placeDecay(G, st, st.sections[tgt], depth + 1);
      if (st.result) return;
    }
  }
}

export function restoreDecay(st, s, n) {
  const k = Math.min(n, s.decay);
  s.decay -= k; st.decayPool += k;
}

// ---------------------------------------------------------------- crew
export function gatherCrew(G, st, h, s, n) {
  for (let i = 0; i < n; i++) {
    const opts = s.adj.filter((a) => st.sections[a].crew > 0);
    if (!opts.length) return;
    const from = G.choose(st, h, "gatherFrom", [...opts, "none"], { to: s.id });
    if (from === "none" || !st.sections[from]) return; // gathering is optional
    st.sections[from].crew -= 1; s.crew += 1;
  }
}

// ---------------------------------------------------------------- vent
export function vent(G, st, h, s, kind, n) {
  if (s.quarantine) return; // Quarantine: nothing vents out of the section
  for (let i = 0; i < n; i++) {
    let piece = kind;
    if (kind === "glitch_or_fault") piece = s.fault > 0 ? "fault" : "glitch";
    if (s[piece] <= 0) return;
    // Voidwardens' Airlock: threat vented from an Outer Hull section goes into the void.
    if (st.houses[h]?.id === "voidwardens" && s.hull) {
      s[piece] -= 1;
      st.stats.destroyed[piece] += 1;
      if (piece === "failure") st.houses[h].credits += 1;
      continue;
    }
    const opts = s.adj.filter((a) => !st.sections[a].quarantine);
    if (!opts.length) return;
    const to = G.choose(st, h, "ventTo", [...opts, "stay"], { from: s.id, piece });
    if (to === "stay" || !st.sections[to]) return; // venting is optional
    s[piece] -= 1; st.sections[to][piece] += 1;
  }
}

export function downgrade(s, which = "any", n = 1) {
  for (let i = 0; i < n; i++) {
    if ((which === "any" || which === "failure") && s.failure > 0) { s.failure--; s.fault++; }
    else if ((which === "any" || which === "fault") && s.fault > 0) { s.fault--; s.glitch++; }
    else return;
  }
}

// --------------------------------------------- effect verbs (cards & innates)
// Applies a {verb: n} map to target section `s` for house h.
export function applySectionEffects(G, st, h, s, effects) {
  for (const [v, n] of Object.entries(effects)) {
    if (st.result) return;
    switch (v) {
      case "damage":
        // Tellers' Spin: their damage becomes Purpose instead of destroying threat.
        if (st.houses[h]?.id === "tellers" && threatCount(s) > 0) { gainPurpose(G, st, 2 * n, "spin"); s.isolate += n; }
        else damageThreat(G, st, s, n, "card");
        break;
      case "crew_strike": damageThreat(G, st, s, s.crew * crewDamage(G, st, s) * n, "crew"); break;
      case "damage_per_crew": damageThreat(G, st, s, s.crew * n, "card"); break;
      case "downgrade": downgrade(s, "any", n); break;
      case "downgrade_failure": downgrade(s, "failure", n); break;
      case "vent_glitch": vent(G, st, h, s, "glitch", n); break;
      case "vent_fault": vent(G, st, h, s, "fault", n); break;
      case "vent_failure": vent(G, st, h, s, "failure", n); break;
      case "vent_glitch_or_fault": vent(G, st, h, s, "glitch_or_fault", n); break;
      case "patch": s.patch += n; break;
      case "lockout": s.lockout += n; break;
      case "isolate_fault": s.isolate += 2 * n; break;
      case "isolate_failure": s.isolate += 3 * n; break;
      case "brace": s.brace += n; break;
      case "quarantine": case "quarantine_source": s.quarantine = 1; break;
      case "gather_crew": case "move_crew": gatherCrew(G, st, h, s, n); break;
      case "add_crew": s.crew += n; break;
      case "restore_decay": restoreDecay(st, s, n); break;
      case "add_influence":
        if (st.houses[h]?.id === "voidwardens" && !(s.hull || s.adj.some((a) => st.sections[a].hull))) break;
        s.influence[h] = (s.influence[h] || 0) + n; break;
      case "move_influence": moveInfluence(G, st, h, s, n); break;
      case "purpose": gainPurpose(G, st, n, "card"); break;
      case "credits": st.houses[h].credits += n; break;
      case "foresee": st.stats.foresee += 1; break;
      case "temper_legacy": if (st.slots.dusk) st.slots.dusk.tempered = true; break;
      default: throw new Error(`unknown verb ${v}`);
    }
  }
}

export function moveInfluence(G, st, h, s, n) {
  for (let i = 0; i < n; i++) {
    const opts = influenceSections(st, h).filter((id) => id !== s.id && st.sections[id].influence[h] > 1);
    if (!opts.length) return;
    const from = G.choose(st, h, "moveInfluenceFrom", opts, { to: s.id });
    st.sections[from].influence[h] -= 1;
    s.influence[h] = (s.influence[h] || 0) + 1;
  }
}

// Effects on another house (cooperative cards).
export function applyHouseEffects(G, st, h, target, effects) {
  for (const [v, n] of Object.entries(effects)) {
    if (v === "credits") st.houses[target].credits += n;
    else if (v === "purpose") gainPurpose(G, st, n, "card");
    else if (v === "add_influence" || v === "move_influence") {
      const opts = inRange(st, target, 1);
      if (!opts.length) continue;
      const id = G.choose(st, h, "influenceFor", opts, { house: target });
      if (v === "add_influence") st.sections[id].influence[target] = (st.sections[id].influence[target] || 0) + n;
      else moveInfluence(G, st, target, st.sections[id], n);
    } else throw new Error(`unknown house verb ${v}`);
  }
}

// ---------------------------------------------------------------- decks
export function drawFrom(st, deck, discard) {
  if (!st.decks[deck].length) {
    st.decks[deck] = shuffle(st, st.decks[discard]);
    st.decks[discard] = [];
  }
  return st.decks[deck].pop();
}
