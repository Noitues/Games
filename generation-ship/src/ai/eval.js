// State evaluation for the bots. Higher is better for the (cooperative) table.
import { allSections, matches, threatCount, totalInfluence } from "../engine/rules.js";
import { eventTypes } from "../engine/game.js";

// Weights tuned by self-play (sim/tune-weights.js): fault 2.5 -> 4, decay 6 -> 9.6.
export const W = {
  glitch: 1, fault: 4, failure: 4.5,
  decay: 9.6, crew: 2, influence: 1.5, haven: 0.5,
  purposeFill: 4, discovery: 5, tier: 8, credits: 0.5,
  predictedDecay: 8, predictedCrewLoss: 3, growThreat: 2.5,
  lowInfluence: 30, win: 10000,
};

// Which events act next, from the current phase's point of view.
export function upcoming(G, st) {
  // "time" counts as early: Time passes shifts the slots first, so the next Collapse is the Dusk slot.
  const early = ["setup", "growth", "commit", "fast", "time"].includes(st.phase);
  const beforeDay = early || st.phase === "dusk";
  return {
    collapse: early ? eventTypes(G, st.slots.dusk?.event) : eventTypes(G, st.slots.day?.event),
    grow: beforeDay ? eventTypes(G, st.slots.day?.event) : eventTypes(G, st.slots.dawn?.event),
  };
}

export function predictedCollapse(s) {
  const d = s.glitch + 2 * s.fault + 3 * s.failure + (s.unrest > 0 && threatCount(s) ? 1 : 0)
    - s.isolate - s.brace;
  return Math.max(0, d);
}

export function evaluate(G, st, up = upcoming(G, st)) {
  if (st.result) return st.result.outcome === "win" ? W.win - st.gen : -W.win + st.gen;
  let v = 0;
  for (const s of allSections(st)) {
    const t = threatCount(s);
    v -= s.glitch * W.glitch + s.fault * W.fault + s.failure * W.failure;
    v -= s.decay * W.decay;
    v += s.crew * W.crew;
    for (const n of Object.values(s.influence)) { v += n * W.influence; if (n >= 2) v += W.haven; }
    if (t && matches(s, up.collapse)) {
      const d = predictedCollapse(s);
      v -= d;
      if (d >= G.cfg.decayThreshold) v -= W.predictedDecay * (s.decay > 0 ? 2 : 1);
      v -= Math.min(s.crew, Math.floor(d / G.cfg.crewHealth)) * W.predictedCrewLoss;
    }
    if (t && matches(s, up.grow) && s.patch === 0) v -= s.fault >= 2 ? W.failure - W.fault : W.growThreat;
    v += Math.min(s.lockout, 1) * 0.3;
  }
  st.houses.forEach((H, h) => {
    const inf = totalInfluence(st, h);
    if (inf <= 1) v -= W.lowInfluence * (2 - inf);
    v += H.credits * W.credits;
  });
  v -= 10 / (st.decayPool + 1 + (st.crisisFlipped ? 0 : st.houses.length));
  // destination Landfall requirements
  const req = st.dest?.requirement || {};
  if (req.minCrewPerPlayer) {
    const crew = allSections(st).reduce((n, s) => n + s.crew, 0);
    v -= Math.max(0, req.minCrewPerPlayer * st.houses.length + 2 - crew) * 3;
  }
  if (req.noDecayIn) v -= allSections(st).filter((s) => s.type === req.noDecayIn).reduce((n, s) => n + s.decay, 0) * 8;
  v += (st.purpose / st.purposeCap) * W.purposeFill;
  v += (st.discoveriesEarned + st.pendingDiscoveries.length * 0.2) * W.discovery;
  v += st.tier * W.tier;
  return v;
}
