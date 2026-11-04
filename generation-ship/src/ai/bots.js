// Layered bots.
//   level 0  RandomBot     - legal random choices everywhere.
//   level 1  Tactician     - best single-state choice for every target / placement (1-step lookahead).
//   level 2  Planner       - + whole-round choices: growth, track, commit (plays, nominee, fast), Remarkables, clone.
//   level 3  HouseBot      - + table-level judgement: succession vote, Discovery apply-vs-Breakthrough,
//                            house-aware track pacing and credit reserve, whole-round rollouts.
//   level 4  TeamBot       - + team lookahead: rollouts include teammates' likely plays.
import { nextRandom, randInt } from "../engine/rng.js";
import {
  placeDecay, applySectionEffects, threatCount, matches, inRange, totalInfluence,
} from "../engine/rules.js";
import {
  resolveCard, resolveInnate, houseStats, houseData, card, canUncover, applyDiscoveryEffects,
  legalTargets, eventTypes, applyPlan, runPhase, applyReign, applyLegacy, discoveryTier,
} from "../engine/game.js";
import { evaluate, upcoming, predictedCollapse } from "./eval.js";

const clone = (st) => structuredClone(st);

// Bot-internal RNG so bot randomness never perturbs the game's RNG stream.
function botRand(bot) { bot.seed = (bot.seed * 1103515245 + 12345) & 0x7fffffff; return bot.seed / 0x7fffffff; }
const bPick = (bot, arr) => arr[Math.floor(botRand(bot) * arr.length)];

// --------------------------------------------------------- quick heuristics
// Cheap choices used inside lookahead simulations (no cloning, no recursion).
export function heuristicChoose(G, st, h, kind, options, ctx) {
  const S = st.sections;
  const up = upcoming(G, st);
  const danger = (id) => (matches(S[id], up.collapse) ? 2 : 0) + (matches(S[id], up.grow) ? 1 : 0);
  switch (kind) {
    case "ventTo": {
      // venting is optional: only push threat somewhere less dangerous than where it is
      const score = (id) => threatCount(S[id]) * 2 + danger(id) * 3 + S[id].decay;
      const real = options.filter((o) => S[o]);
      const best = minBy(real, score);
      return best && score(best) < score(ctx.from) + 1 ? best : "stay";
    }
    case "gatherFrom": { const real = options.filter((o) => S[o]); return real.length ? maxBy(real, (id) => S[id].crew - (threatCount(S[id]) && matches(S[id], up.collapse) ? 0 : 0.5)) : "none"; }
    case "landfall": return "begin";
    case "discoveryAt": return maxBy(options, (id) => threatCount(S[id]) * 2 + danger(id) + S[id].crew * 0.2);
    case "cascade": return minBy(options, (id) => Object.values(S[id].influence).reduce((a, b) => a + b, 0) * 2 + S[id].decay * 5 + S[id].crew);
    case "moveInfluenceFrom": return maxBy(options, (id) => S[id].influence[h]);
    case "discovery": return "apply";
    case "clone": return [];
    case "remarkables": return 0;
    case "vote": return options[0];
    default:
      if (Array.isArray(options)) return options[0];
      return null;
  }
}
const wallCredit = (G, st) => { let n = 0; for (const L of st.wall || []) if (L.bt) n += G.data.discoveryById[L.bt]?.breakthrough?.effects?.credits_per_growth || 0; return n; };
const maxBy = (arr, f) => arr.reduce((b, x) => (f(x) > f(b) ? x : b), arr[0]);
const minBy = (arr, f) => arr.reduce((b, x) => (f(x) < f(b) ? x : b), arr[0]);

// A context whose first choice of `kind` is forced, later choices heuristic.
function forcedContext(G, kind, forced) {
  let used = false;
  return { ...G, choose: (st, h, k, o, c) => {
    if (!used && k === kind) { used = true; return forced; }
    return heuristicChoose(G, st, h, k, o, c);
  } };
}
const heuristicContext = (G) => ({ ...G, choose: (st, h, k, o, c) => heuristicChoose(G, st, h, k, o, c) });

// --------------------------------------------------------- bot
export class Bot {
  constructor(level = 3, seed = 7, opts = {}) {
    this.level = level; this.seed = seed; this.rolloutK = opts.rolloutK ?? 6;
  }

  choose(G, st, h, kind, options, ctx) {
    const L = this.level;
    if (L === 0) return this.random(G, st, h, kind, options, ctx);
    switch (kind) {
      // ---- level 1: single-state targeting
      case "cardTarget": return this.bestByRerun(G, st, h, kind, options, (G2, s2) => resolveCard(G2, s2, h, ctx.card));
      case "innateTarget": return this.bestByRerun(G, st, h, kind, options, (G2, s2) => resolveInnate(G2, s2, h));
      case "ventTo": case "gatherFrom": case "cascade": case "moveInfluenceFrom":
      case "growthInfluence": case "influenceFor": case "addCrewAt": case "restoreAt": case "discoveryAt":
        return this.bestMutation(G, st, h, kind, options, ctx);
      case "playOrder": return options[0];
      case "landfall": return "begin";
    }
    if (L === 1) return this.random(G, st, h, kind, options, ctx);
    switch (kind) {
      // ---- level 2: round planning
      case "growth": return this.growth(G, st, h);
      case "track": return this.track(G, st, h, options);
      case "commit": return this.commit(G, st, h, ctx);
      case "remarkables": return this.remarkables(G, st, h);
      case "clone": return this.cloneChoice(G, st, h, options, ctx);
    }
    if (L === 2) return this.random(G, st, h, kind, options, ctx);
    switch (kind) {
      // ---- level 3: table judgement
      case "vote": case "tiebreak": return this.vote(G, st, h, options);
      case "discovery": return this.discovery(G, st, h, ctx);
    }
    return this.random(G, st, h, kind, options, ctx);
  }

  // ------------------------------------------------------ random baseline
  random(G, st, h, kind, options, ctx) {
    if (kind === "commit") return this.randomCommit(G, st, h, ctx);
    if (kind === "clone") return options.length && ctx.slots ? [bPick(this, options)] : [];
    if (kind === "remarkables") return botRand(this) < 0.3 ? 1 : 0;
    return bPick(this, options);
  }
  randomCommit(G, st, h, ctx) {
    const H = st.houses[h];
    const hand = [...H.hand].sort(() => botRand(this) - 0.5);
    const play = [];
    let nominee = null, credits = H.credits;
    for (const cid of hand) {
      if (play.length >= ctx.plays) break;
      const c = card(G, cid).cost;
      if (!nominee && G.cfg.nomineeFree) { nominee = cid; play.push(cid); continue; }
      if (c <= credits) { credits -= c; play.push(cid); }
    }
    return { play, nominee: nominee ?? play[0] ?? null, fast: play.slice(1) };
  }

  // ------------------------------------------------------ level 1
  bestByRerun(G, st, h, kind, options, run) {
    if (options.length === 1) return options[0];
    const up = upcoming(G, st);
    let best = options[0], bestV = -Infinity;
    for (const o of options) {
      const s2 = clone(st);
      run(forcedContext(G, kind, o), s2);
      const v = evaluate(G, s2, up);
      if (v > bestV) { bestV = v; best = o; }
    }
    return best;
  }
  bestMutation(G, st, h, kind, options, ctx) {
    if (options.length === 1) return options[0];
    const up = upcoming(G, st);
    const HG = heuristicContext(G);
    const mutate = {
      ventTo: (s2, o) => { if (o === "stay") return; s2.sections[ctx.from][ctx.piece] -= 1; s2.sections[o][ctx.piece] += 1; },
      gatherFrom: (s2, o) => { if (o === "none") return; s2.sections[o].crew -= 1; s2.sections[ctx.to].crew += 1; },
      cascade: (s2, o) => placeDecay(HG, s2, s2.sections[o], 1),
      moveInfluenceFrom: (s2, o) => { s2.sections[o].influence[h] -= 1; },
      growthInfluence: (s2, o) => { const S = s2.sections[o]; S.influence[h] = (S.influence[h] || 0) + 1; },
      influenceFor: (s2, o) => { const S = s2.sections[o]; S.influence[ctx.house] = (S.influence[ctx.house] || 0) + 1; },
      addCrewAt: (s2, o) => { s2.sections[o].crew += 1; },
      restoreAt: (s2, o) => { s2.sections[o].decay -= 1; s2.decayPool += 1; },
      discoveryAt: (s2, o) => applyDiscoveryEffects(HG, s2, ctx.effects, [s2.sections[o]]),
    }[kind];
    // influence placement also values future reach toward threat
    const reach = (s2, o) => (kind === "growthInfluence" || kind === "influenceFor") && s2.sections[o]
      ? s2.sections[o].adj.reduce((n, a) => n + threatCount(s2.sections[a]), threatCount(s2.sections[o])) * 0.3 : 0;
    let best = options[0], bestV = -Infinity;
    for (const o of options) {
      const s2 = clone(st);
      mutate(s2, o);
      const v = evaluate(G, s2, up) + reach(s2, o);
      if (v > bestV) { bestV = v; best = o; }
    }
    return best;
  }

  // ------------------------------------------------------ level 2
  remainingGens(st) { return st.decks.events.length + 1; }

  slotValue(G, st, h, track) {
    // Value per generation of uncovering the next slot: the special it grants (if any), plus the
    // next real numeric increase on this track divided by the uncovers it takes to get there.
    const hd = houseData(G, st, h), H = st.houses[h];
    const t = hd.tracks[track], pos = H.track[track];
    if (pos >= t.length - 1) return -1;
    const next = t[pos + 1];
    const SPECIAL = { element: 0.4, draw: 0.5, fast_play: 0.8, clone: 0.6 };
    const special = typeof next === "object" ? Object.keys(next).reduce((v, k) => v + (SPECIAL[k] ?? 0.5), 0) : 0;
    const hs = houseStats(G, st, h);
    const base = track === "credits" ? hs.income - (wallCredit(G, st)) : hs.plays;
    let steps = 0, delta = 0;
    for (let i = pos + 1; i < t.length; i++) {
      steps++;
      if (typeof t[i] === "number" && t[i] !== base) { delta = t[i] - base; break; }
    }
    const unit = track === "credits"
      ? (hs.income < 1.5 * hs.plays ? 1.3 : 0.6)
      : 2 * Math.min(1, (H.credits + hs.income + 1) / (1.5 * hs.plays));
    return special + (delta ? (delta * unit) / steps : 0);
  }
  track(G, st, h, options) { return maxBy(options, (t) => this.slotValue(G, st, h, t)); }

  growth(G, st, h) {
    const R = this.remainingGens(st), H = st.houses[h];
    const slot = Math.max(this.slotValue(G, st, h, "credits"), this.slotValue(G, st, h, "plays"));
    const vA = 2 + (slot > 0 ? slot * R * 0.6 : 0);
    const hs = houseStats(G, st, h);
    const short = H.credits + hs.income < 1.5 * hs.plays ? 1.5 : 0;
    const perk = H.id === "galvan" ? 0.9 : H.id === "keel" ? 0.75 : 0;
    const vB = 2 + perk + short;
    const vC = 2.5 + (hs.hand <= 4 ? 0.5 : 0);
    return vA >= vB && vA >= vC ? "A" : vB >= vC ? "B" : "C";
  }

  remarkables(G, st, h) {
    const H = st.houses[h], hs = houseStats(G, st, h);
    return H.credits + hs.income >= 5 && hs.hand >= 4 ? 1 : 0;
  }

  cardValue(G, st, h, cid) {
    // value of playing this card now (best target), as evaluation delta
    const up = upcoming(G, st), base = evaluate(G, st, up);
    const opts = legalTargets(G, st, h, card(G, cid).target);
    if (!opts.length) return 0;
    let best = -Infinity;
    for (const o of opts) {
      const s2 = clone(st);
      s2.houses[h].elements = {}; // threshold bonuses are scored separately in commit()
      resolveCard(forcedContext(G, "cardTarget", o), s2, h, cid);
      best = Math.max(best, evaluate(G, s2, up) - base);
    }
    return best;
  }

  commit(G, st, h, ctx) {
    const H = st.houses[h], hd = houseData(G, st, h), hs = houseStats(G, st, h);
    const hand = H.hand;
    const vals = Object.fromEntries(hand.map((cid) => [cid, this.cardValue(G, st, h, cid)]));
    const creditValue = this.level >= 3 ? this.creditValue(G, st, h) : 0.6;
    let best = null, bestScore = -Infinity;
    const ranked = [];
    const n = hand.length, maxK = Math.min(ctx.plays, n);
    const subsets = [];
    const rec = (i, cur) => {
      if (cur.length) subsets.push([...cur]);
      if (cur.length === maxK) return;
      for (let j = i; j < n; j++) { cur.push(hand[j]); rec(j + 1, cur); cur.pop(); }
    };
    rec(0, []);
    for (const set of subsets) {
      const cards = set.map((c) => card(G, c));
      const nomIdx = cards.reduce((bi, c, i) => (c.cost > cards[bi].cost || (c.cost === cards[bi].cost && vals[set[i]] > vals[set[bi]]) ? i : bi), 0);
      const cost = cards.reduce((a, c) => a + c.cost, 0) - (G.cfg.nomineeFree ? cards[nomIdx].cost : 0);
      if (cost > H.credits) continue;
      const el = { ...hs.raw };
      for (const c of cards) for (const g of c.guilds) el[g] = (el[g] || 0) + 1;
      const met = (req) => Object.entries(req).every(([g, k]) => (el[g] || 0) >= k);
      let score = set.reduce((a, c) => a + vals[c], 0) - cost * creditValue;
      for (const c of cards) if (c.threshold && met(c.threshold.elements)) score += c.threshold.pp;
      let tierPP = 0;
      for (const t of hd.innate.tiers) if (met(t.threshold)) tierPP = t.pp;
      score += tierPP;
      ranked.push({ set, nominee: set[nomIdx], score, reserve: (H.credits - cost) * creditValue });
      if (score > bestScore) { bestScore = score; best = { set, nominee: set[nomIdx] }; }
    }
    if (!best) return { play: [], nominee: null, fast: [] };
    const toPlan = (b) => ({ play: b.set, nominee: b.nominee,
      fast: b.set.filter((c) => c !== b.nominee).sort((x, y) => vals[y] - vals[x]) });
    if (this.level < 3) return toPlan(best);
    // Level 3: whole-round rollout of the top candidates.
    ranked.sort((a, b) => b.score - a.score);
    let pick = toPlan(best), pickV = -Infinity;
    for (const cand of ranked.slice(0, this.rolloutK)) {
      const plan = toPlan(cand);
      const v = this.rollout(G, st, h, plan) + cand.reserve;
      if (v > pickV) { pickV = v; pick = plan; }
    }
    return pick;
  }

  // Simulate this house's plan through fast -> Dusk -> Day -> slow with tactician-level choices.
  rollout(G, st, h, plan) {
    const s2 = clone(st);
    const inner = this.inner ??= new RolloutBot();
    const G2 = { ...G, choose: (ss, hh, k, o, c) => inner.choose(G, ss, hh, k, o, c) };
    applyPlan(G2, s2, h, plan);
    if (this.level >= 4) {
      // Team lookahead: teammates who haven't committed yet play their planner-level plan.
      const mate = this.mate ??= new Bot(2, 3);
      for (let j = h + 1; j < s2.houses.length; j++) {
        const hs = houseStats(G, s2, j);
        const p2 = mate.commit(G, s2, j, { plays: hs.plays });
        if (p2.play.length) applyPlan(G2, s2, j, p2);
      }
    }
    for (const p of ["fast", "dusk", "day", "slow"]) { if (s2.result) break; runPhase(G2, s2, p); }
    s2.phase = "slow";
    return evaluate(G, s2);
  }

  cloneChoice(G, st, h, options, ctx) {
    if (!ctx.slots || !options.length) return [];
    const score = (cid) => { const c = card(G, cid); return c.pp_target + (c.tier === "Remarkable" ? 2 : 0) + (c.threshold ? 0.5 : 0); };
    return [...options].sort((a, b) => score(b) - score(a)).slice(0, ctx.slots);
  }

  // ------------------------------------------------------ level 3
  creditValue(G, st, h) {
    // Rich, steep houses save toward Remarkables; front-loaded houses spend freely.
    const R = this.remainingGens(st);
    const curve = houseData(G, st, h).curve;
    const base = curve === "steep" ? 0.8 : curve === "front-loaded" ? 0.45 : 0.6;
    return R <= 2 ? 0.1 : base;
  }

  vote(G, st, h, options) {
    if (G.cfg.smartVote && st.upcomingEvent) return this.smartVote(G, st, options);
    const direct = st.upcomingEvent ? eventTypes(G, st.upcomingEvent) : null;
    const score = (cid) => {
      const c = card(G, cid);
      let s = c.reign.pp - 1.2 * c.legacy.pp;
      if (direct) {
        // Legacy will land in these sections two generations from now; punish Decay/threat legacies where threat already is
        const hot = Object.values(st.sections).filter((x) => matches(x, direct) && threatCount(x) > 0).length;
        const harsh = ["add_decay", "add_failure", "add_fault", "destroy_crew"].some((k) => c.legacy.effects[k]);
        if (harsh) s -= hot * 0.5;
      }
      return s;
    };
    return maxBy(options, score);
  }

  // Direct pairing: simulate each heir's Reign and Legacy on the event they will carry.
  smartVote(G, st, options) {
    const HG = heuristicContext(G);
    const base = evaluate(G, st);
    const score = (cid) => {
      const r = clone(st); r.slots.day = { leader: cid, event: st.upcomingEvent, house: 0 }; applyReign(HG, r);
      const l = clone(st); l.slots.dusk = { leader: cid, event: st.upcomingEvent, house: 0 }; applyLegacy(HG, l);
      return (evaluate(G, r) - base) + (evaluate(G, l) - base);
    };
    return maxBy(options, score);
  }

  discovery(G, st, h, ctx) {
    const d = G.data.discoveryById[ctx.id];
    const R = this.remainingGens(st);
    // the Breakthrough switches on when the Steward retires to the Wall (two generations from now)
    const btValue = d.breakthrough.pp_per_generation * Math.max(0, R - 2) * 0.8;
    const t = discoveryTier(G, st, ctx.id);
    return t.pp >= btValue ? "apply" : "breakthrough";
  }
}

export const BOT_LEVELS = { random: 0, tactician: 1, planner: 2, house: 3, team: 4 };

// Inner bot for rollouts: tactician targeting, cheap heuristics for everything else.
class RolloutBot extends Bot {
  constructor() { super(1, 1); }
  choose(G, st, h, kind, options, ctx) {
    if (["cardTarget", "innateTarget"].includes(kind)) return super.choose(G, st, h, kind, options, ctx);
    return heuristicChoose(G, st, h, kind, options, ctx);
  }
}
