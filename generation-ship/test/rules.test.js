// Rule tests: each test sets up a small board state and checks one GDD rule.
//   node --test test/
import { test } from "node:test";
import assert from "node:assert/strict";
import { loadData } from "../sim/load.js";
import { createGame, makeContext, seed, grow, collapse, resolveCard, runPhase, checkVictory,
  activeDestination, legalTargets, houseStats, applyPlan } from "../src/engine/game.js";
import { damageThreat, placeDecay, gainPurpose, vent, winConditionMet, applySectionEffects } from "../src/engine/rules.js";

const DATA = loadData();
// Agent that always takes the first option (deterministic).
const first = { choose: (G, st, h, kind, options) => {
  if (kind === "commit") return { play: [], nominee: null, fast: [] };
  if (kind === "clone") return [];
  return Array.isArray(options) ? options[0] : options;
} };

function fresh(cfg = {}) {
  const { st, cfg: full } = createGame(DATA, { players: 2, houses: ["galvan", "keel"], ...cfg }, 1);
  const G = makeContext(DATA, full, [first, first]);
  // clear the board so each test controls it
  for (const s of Object.values(st.sections)) {
    Object.assign(s, { glitch: 0, fault: 0, failure: 0, crew: 0, decay: 0, brace: 0, quarantine: 0,
      patch: 0, lockout: 0, unrest: 0, isolate: 0, dmg: 0, influence: {} });
  }
  st.sections.A1.influence = { 0: 1 }; st.sections.B1.influence = { 1: 1 }; // keep houses alive
  return { G, st, S: st.sections };
}
// Register a one-off event card for a test.
function event(types, twist = null) {
  const id = `T-${types.join("+")}-${twist?.rule ?? "none"}`;
  DATA.eventById[id] = { id, stage: 1, types, twist };
  return id;
}

// ------------------------------------------------------------------ Dawn seed
test("seed: matching Hull section gains a Glitch", () => {
  const { G, st, S } = fresh();
  seed(G, st, event([S.A1.type]));
  assert.equal(S.A1.glitch, 1); // A1 is on the Outer Hull
});
test("seed: Core section needs an adjacent Fault or Failure as a source", () => {
  const { G, st, S } = fresh();
  const core = Object.values(S).find((s) => !s.hull && s.board === "A");
  seed(G, st, event([core.type]));
  assert.equal(core.glitch, 0);
  S[core.adj[0]].fault = 1;
  seed(G, st, event([core.type]));
  assert.equal(core.glitch, 1);
});
test("seed: Lockout skips the seed and is removed; Quarantine blocks it", () => {
  const { G, st, S } = fresh();
  S.A1.lockout = 1;
  seed(G, st, event([S.A1.type]));
  assert.equal(S.A1.glitch, 0); assert.equal(S.A1.lockout, 0);
  S.A1.quarantine = 1;
  seed(G, st, event([S.A1.type]));
  assert.equal(S.A1.glitch, 0);
});

// ------------------------------------------------------------------ Day grow
test("grow: a section with threat gains a Fault; with 2+ Faults, a Failure instead", () => {
  const { G, st, S } = fresh();
  S.A1.glitch = 1;
  grow(G, st, event([S.A1.type])); assert.equal(S.A1.fault, 1);
  S.A1.fault = 2;
  grow(G, st, event([S.A1.type])); assert.equal(S.A1.failure, 1); assert.equal(S.A1.fault, 2);
});
test("grow: sections without threat don't grow; Patch skips once", () => {
  const { G, st, S } = fresh();
  grow(G, st, event([S.A1.type])); assert.equal(S.A1.fault, 0);
  S.A1.glitch = 1; S.A1.patch = 1;
  grow(G, st, event([S.A1.type])); assert.equal(S.A1.fault, 0); assert.equal(S.A1.patch, 0);
});

// ------------------------------------------------------------------ Dusk collapse
test("collapse: damage = Glitch 1 + Fault 2 + Failure 3; 2+ damage places Decay", () => {
  const { G, st, S } = fresh();
  S.A1.glitch = 1; S.A1.fault = 1; // 3 damage
  const pool = st.decayPool;
  collapse(G, st, event([S.A1.type]));
  assert.equal(S.A1.decay, 1); assert.equal(st.decayPool, pool - 1);
});
test("collapse: 1 damage does not place Decay", () => {
  const { G, st, S } = fresh();
  S.A1.glitch = 1;
  collapse(G, st, event([S.A1.type]));
  assert.equal(S.A1.decay, 0);
});
test("collapse: Brace and Isolate reduce damage before the Decay check", () => {
  const { G, st, S } = fresh();
  S.A1.fault = 1; S.A1.brace = 1; // 2 - 1 = 1
  collapse(G, st, event([S.A1.type]));
  assert.equal(S.A1.decay, 0);
  const { G: G2, st: st2, S: S2 } = fresh();
  S2.A1.fault = 1; S2.A1.isolate = 2;
  collapse(G2, st2, event([S2.A1.type]));
  assert.equal(S2.A1.decay, 0); assert.equal(S2.A1.isolate, 0);
});
test("collapse: the full damage also hits Crew (2 health each); survivors deal 2 damage each", () => {
  const { G, st, S } = fresh();
  S.A1.fault = 1; S.A1.crew = 3; // 2 damage -> 1 Crew dies, 2 survive -> 4 damage
  collapse(G, st, event([S.A1.type]));
  assert.equal(S.A1.crew, 2);
  assert.equal(S.A1.fault, 0); // destroyed by the counter-attack
});
test("collapse: Unrest adds +1 damage", () => {
  const { G, st, S } = fresh();
  S.A1.glitch = 1; S.A1.unrest = 1; // 1 + 1 = 2 -> Decay
  collapse(G, st, event([S.A1.type]));
  assert.equal(S.A1.decay, 1);
});
test("collapse twists: Power surge (Faults +1) and Panic (extra Crew loss)", () => {
  const { G, st, S } = fresh();
  S.A1.fault = 1; S.A1.crew = 2; // 3 damage with surge -> 1 Crew dies
  collapse(G, st, event([S.A1.type], { rule: "faults_plus_one" }));
  assert.equal(S.A1.crew, 1);
  const f = fresh();
  f.S.A1.glitch = 1; f.S.A1.crew = 2; // 1 damage kills none, Panic kills 1
  collapse(f.G, f.st, event([f.S.A1.type], { rule: "extra_crew_loss" }));
  assert.equal(f.S.A1.crew, 1);
});

// ------------------------------------------------------------------ Decay
test("decay: each house loses 1 influence where Decay lands", () => {
  const { G, st, S } = fresh();
  S.A2.influence = { 0: 2, 1: 1 };
  placeDecay(G, st, S.A2);
  assert.deepEqual(S.A2.influence, { 0: 1, 1: 0 });
});
test("decay: Decay on existing Decay cascades to an adjacent section", () => {
  const { G, st, S } = fresh();
  S.A2.decay = 1;
  placeDecay(G, st, S.A2);
  const spilled = S.A2.adj.reduce((n, a) => n + S[a].decay, 0);
  assert.equal(S.A2.decay, 2); assert.equal(spilled, 1);
});
test("decay: cascades neither enter nor leave a Quarantined section", () => {
  const { G, st, S } = fresh();
  S.A2.decay = 1; S.A2.quarantine = 1;
  placeDecay(G, st, S.A2);
  assert.equal(S.A2.adj.reduce((n, a) => n + S[a].decay, 0), 0);
  const f = fresh();
  f.S.A2.decay = 1;
  for (const a of f.S.A2.adj) f.S[a].quarantine = 1;
  placeDecay(f.G, f.st, f.S.A2);
  assert.equal(f.S.A2.adj.reduce((n, a) => n + f.S[a].decay, 0), 0);
});
test("decay: empty pool flips Ship in Crisis (+1 per player); empty again loses", () => {
  const { G, st, S } = fresh();
  st.decayPool = 0; st.crisisId = "X1";
  placeDecay(G, st, S.A5);
  assert.equal(st.crisisFlipped, true); assert.equal(st.decayPool, 1); assert.equal(st.result, null);
  st.decayPool = 0;
  placeDecay(G, st, S.A6);
  assert.equal(st.result.outcome, "loss"); assert.equal(st.result.cause, "decay");
});
test("loss: a house with no influence loses the game", () => {
  const { G, st, S } = fresh();
  placeDecay(G, st, S.A1); // house 0's only influence
  assert.equal(st.result?.cause, "influence");
});

// ------------------------------------------------------------------ damage and Purpose
test("player damage kills the most damage output; Faults/Failures give Purpose", () => {
  const { G, st, S } = fresh();
  S.A3.glitch = 2; S.A3.fault = 1;
  damageThreat(G, st, S.A3, 2);
  assert.equal(S.A3.fault, 0); assert.equal(S.A3.glitch, 2); assert.equal(st.purpose, 1);
  S.A3.failure = 1;
  damageThreat(G, st, S.A3, 3);
  assert.equal(S.A3.failure, 0); assert.equal(st.purpose, 3);
});
test("leftover damage persists in the section this generation", () => {
  const { G, st, S } = fresh();
  S.A3.fault = 1;
  damageThreat(G, st, S.A3, 1); assert.equal(S.A3.fault, 1);
  damageThreat(G, st, S.A3, 1); assert.equal(S.A3.fault, 0);
});
test("Purpose: filling the pool earns a Discovery; every 3 raise Understanding", () => {
  const { G, st } = fresh();
  gainPurpose(G, st, st.purposeCap * 3);
  assert.equal(st.discoveriesEarned, 3); assert.equal(st.tier, 2); assert.equal(st.pendingDiscoveries.length, 3);
});

// ------------------------------------------------------------------ vent and Quarantine
test("vent: moves threat to an adjacent section, but not out of a Quarantined one", () => {
  const { G, st, S } = fresh();
  S.A6.glitch = 1;
  vent(G, st, 0, S.A6, "glitch", 1);
  assert.equal(S.A6.glitch, 0);
  const f = fresh();
  f.S.A6.glitch = 1; f.S.A6.quarantine = 1;
  vent(f.G, f.st, 0, f.S.A6, "glitch", 1);
  assert.equal(f.S.A6.glitch, 1);
});

// ------------------------------------------------------------------ win conditions
test("win (shifted): I no threat + no Decay, II no threat, III no Faults/Failures", () => {
  const { st, S } = fresh();
  S.A3.decay = 1;
  st.tier = 1; assert.equal(winConditionMet(st), false);
  st.tier = 2; assert.equal(winConditionMet(st), true);
  S.A3.glitch = 1;
  assert.equal(winConditionMet(st), false);
  st.tier = 3; assert.equal(winConditionMet(st), true);
});
test("Landfall card: meeting the condition schedules Landfall instead of winning", () => {
  const { G, st } = fresh({ landfallCard: true });
  st.tier = 2;
  checkVictory(G, st);
  assert.equal(st.result, null); assert.equal(st.landfallPending, true);
});

// ------------------------------------------------------------------ houses
test("Voidwardens' Airlock destroys threat vented from an Outer Hull section", () => {
  const { G, st, S } = fresh({ houses: ["voidwardens", "keel"] });
  S.A1.fault = 1;
  const c0 = st.houses[0].credits;
  vent(G, st, 0, S.A1, "fault", 1);
  assert.equal(S.A1.fault, 0);
  assert.equal(S.A1.adj.reduce((n, a) => n + S[a].fault, 0), 0);
  assert.equal(st.houses[0].credits, c0); // credits only for Failures
});
test("Tellers' Spin: damage becomes 2 Purpose per point and Isolates", () => {
  const { G, st, S } = fresh({ houses: ["tellers", "keel"] });
  S.A3.fault = 1;
  applySectionEffects(G, st, 0, S.A3, { damage: 2 });
  assert.equal(S.A3.fault, 1); assert.equal(st.purpose, 4); assert.equal(S.A3.isolate, 2);
});
test("Gardeners' Rooted: Decay removes Gardener influence instead", () => {
  const { G, st, S } = fresh({ houses: ["gardeners", "keel"] });
  S.A2.influence = { 0: 2 };
  placeDecay(G, st, S.A2);
  assert.equal(S.A2.decay, 0); assert.equal(S.A2.influence[0], 1);
});
test("Foremen's Crew Captains: Crew deal +1 damage fighting back in Foremen sections", () => {
  const { G, st, S } = fresh({ houses: ["foremen", "keel"] });
  S.A3.failure = 1; S.A3.crew = 1; S.A3.influence = { 0: 1 }; S.A3.brace = 3; // no Crew loss
  collapse(G, st, event([S.A3.type]));
  assert.equal(S.A3.failure, 0); // 1 Crew x (2 + 1) = 3 damage
});
test("Keel's Load-Bearing: Brace 1 where Keel has influence, 2 in its Havens, at Dusk", () => {
  const { G, st, S } = fresh();
  S.A5.influence = { 1: 1 }; S.A6.influence = { 1: 2 };
  st.slots.dusk = null; st.pendingDiscoveries = [];
  runPhase(G, st, "dusk");
  assert.equal(S.A5.brace, 1); assert.equal(S.A6.brace, 2);
});

// ------------------------------------------------------------------ destinations
test("destinations: levels are cumulative", () => {
  const d = activeDestination(DATA, { destination: "cinder", destinationLevel: 3 });
  assert.equal(d.texts.filter((t) => t.startsWith("L")).length, 3);
  assert.equal(d.discoveriesPerTier, 3);
  assert.equal(d.requirement.noDecayIn, "Infrastructure");
  assert.equal(d.escalation.length, 1);
});
test("destinations: an unmet Landfall requirement blocks the win", () => {
  const { G, st, S } = fresh({ destination: "cinder", destinationLevel: 1 });
  const infra = Object.values(S).find((s) => s.type === "Infrastructure");
  infra.decay = 1; st.tier = 2;
  checkVictory(G, st);
  assert.equal(st.result, null);
});

// ------------------------------------------------------------------ leaders and the clock
test("commit: the nominee is free; other plays cost credits", () => {
  const { G, st } = fresh();
  const H = st.houses[0];
  const cards = DATA.people.filter((c) => c.tier === "Common" && c.cost === 2).slice(0, 2).map((c) => c.id);
  H.hand = [...cards]; H.credits = 2;
  applyPlan(G, st, 0, { play: cards, nominee: cards[0], fast: [] });
  assert.equal(H.credits, 0); assert.deepEqual(H.fast, [cards[0]]);
  const f = fresh(); f.st.houses[0].hand = [...cards]; f.st.houses[0].credits = 1;
  assert.throws(() => applyPlan(f.G, f.st, 0, { play: cards, nominee: cards[0], fast: [] }));
});
test("vote: a tie goes to the house with fewer leaders on the conveyor, then the Steward decides", () => {
  const { st } = fresh();
  const [a, b] = DATA.people.filter((c) => c.tier === "Common").slice(0, 2).map((c) => c.id);
  const votes = { 0: a, 1: b };
  const agents = [0, 1].map((h) => ({ choose: (G, st, hh, kind, o) => (kind === "vote" ? votes[hh] : kind === "tiebreak" ? o[o.length - 1] : Array.isArray(o) ? o[0] : o) }));
  const G = makeContext(DATA, { ...createGame(DATA, { players: 2, houses: ["galvan", "keel"] }, 1).cfg }, agents);
  // house 1 holds the Steward: the tie goes to house 0's nominee
  st.houses[0].nominee = a; st.houses[1].nominee = b;
  st.slots.day = { leader: a, event: "E1-1", house: 1 };
  runPhase(G, st, "dawn");
  assert.equal(st.slots.dawn.leader, a);
  // one leader each on the conveyor: the Steward's house (1) breaks the tie (this agent picks the last option)
  const f = fresh();
  f.st.houses[0].nominee = a; f.st.houses[1].nominee = b;
  f.st.slots.day = { leader: a, event: "E1-1", house: 1 }; f.st.slots.dusk = { leader: b, event: "E1-2", house: 0 };
  runPhase(G, f.st, "dawn");
  assert.equal(f.st.slots.dawn.leader, b);
});
test("threshold: a card's own guilds count, but no card meets its threshold alone", () => {
  const { G, st, S } = fresh();
  for (const c of DATA.people.filter((x) => x.threshold)) {
    const own = Object.fromEntries(c.guilds.map((g) => [g, 1]));
    assert.ok(!Object.entries(c.threshold.elements).every(([g, n]) => (own[g] || 0) >= n), `${c.id} unlocks itself`);
  }
  const c = DATA.people.find((x) => x.threshold && x.target.kind === "section" && x.effects.brace === undefined && x.threshold.effects.brace);
  st.houses[0].elements = { ...c.threshold.elements };
  resolveCard(G, st, 0, c.id);
  assert.ok(Object.values(S).some((s) => s.brace >= c.threshold.effects.brace));
});
test("vent and gather are optional", () => {
  const { st, S } = fresh();
  const stay = makeContext(DATA, createGame(DATA, { players: 2, houses: ["galvan", "keel"] }, 1).cfg,
    [0, 1].map(() => ({ choose: (G, st, h, kind, o) => (kind === "ventTo" ? "stay" : kind === "gatherFrom" ? "none" : o[0]) })));
  S.A1.fault = 1;
  vent(stay, st, 0, S.A1, "fault", 1);
  assert.equal(S.A1.fault, 1);
});
test("Discoveries earned while resolving Discoveries wait for the next Dusk", () => {
  const { G, st } = fresh();
  st.purposeCap = 1;
  const d = DATA.discoveries.find((x) => x.tiers.I.effects.purpose);
  st.pendingDiscoveries = [d.id];
  st.slots.day = null;
  runPhase(G, st, "dusk");
  assert.ok(st.pendingDiscoveries.length >= 1);
  assert.equal(st.stats.discoveryApplied, 1);
});
test("Breakthroughs switch on only when their leader reaches the Wall", () => {
  const { G, st } = fresh();
  const d = DATA.discoveries.find((x) => x.breakthrough.effects.credits_per_growth);
  const leader = DATA.people[0].id;
  st.slots.dusk = { leader, event: null, house: 0, bt: d.id };
  st.houses[0].credits = 0;
  const before = houseStats(G, st, 0).income;
  runPhase(G, st, "time");
  assert.equal(houseStats(G, st, 0).income, before + 1);
});
test("Legacy becomes ongoing in the Elder's event sections; tempering drops its costliest drawback", () => {
  const { G, st, S } = fresh();
  const c = DATA.people.find((x) => x.legacy.effects.collapse_plus && x.tier === "Common");
  const ev = event(["Residential"]);
  st.slots.dusk = { leader: c.id, event: ev, house: 0 };
  st.pendingDiscoveries = [];
  runPhase(G, st, "dusk");
  st.result = null; // the empty test board counts as a win
  const res = Object.values(S).find((s) => s.type === "Residential" && !s.hull);
  const other = Object.values(S).find((s) => s.type !== "Residential" && !s.hull);
  res.glitch = 1; other.glitch = 1;
  collapse(G, st, event(["ALL"]));
  // the Legacy's +1 Collapse damage applies only in Residential sections: 2 damage there places Decay
  assert.equal(res.decay, 1);
  assert.equal(other.decay, 0);
  const f = fresh();
  f.st.slots.dusk = { leader: c.id, event: ev, house: 0, tempered: true };
  f.st.pendingDiscoveries = [];
  runPhase(f.G, f.st, "dusk");
  assert.equal(f.st.legacies[0].effects.collapse_plus, undefined);
});
test("the nominee is discounted by 3: Commons are free, Remarkables pay the rest", () => {
  const { G, st } = fresh();
  const r = DATA.people.find((x) => x.tier === "Remarkable" && x.cost === 6);
  st.houses[0].hand = [r.id]; st.houses[0].credits = 3;
  applyPlan(G, st, 0, { play: [r.id], nominee: r.id, fast: [] });
  assert.equal(st.houses[0].credits, 0);
});
test("cards: damage per Crew deals 1 damage for each Crew in the section", () => {
  const { G, st, S } = fresh();
  S.A1.crew = 3; S.A1.glitch = 3;
  applySectionEffects(G, st, 0, S.A1, { damage_per_crew: 1 });
  assert.equal(S.A1.glitch, 0);
});
test("clock: drawing from an empty event deck loses the game", () => {
  const { G, st } = fresh();
  st.decks.events = [];
  st.houses.forEach((H) => (H.nominee = null));
  runPhase(G, st, "dawn");
  assert.equal(st.result?.cause, "time");
});
