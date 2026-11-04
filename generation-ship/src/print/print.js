// Print-and-play sheets rendered from data/*.json. Cards are poker size (63 x 88 mm), nine per A4 page.
const get = async (f) => (await fetch(`data/${f}`)).json();
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const [people, events, discoveries, crisis, boards, houses] = await Promise.all(
  ["people.json", "events.json", "discoveries.json", "crisis.json", "boards.json", "houses.json"].map(get));

const VERB = { gather_crew: "gather {n} Crew", brace: "Brace {n}", damage: "{n} damage", lockout: "Lockout",
  downgrade_failure: "downgrade {n} Failure", vent_glitch: "vent {n} Glitch", vent_glitch_or_fault: "vent {n} Glitch/Fault",
  vent_failure: "vent {n} Failure", patch: "Patch", quarantine_source: "Quarantine the source", quarantine: "Quarantine",
  isolate_fault: "Isolate {n} Fault", isolate_failure: "Isolate {n} Failure", restore_decay: "restore {n} Decay",
  add_crew: "add {n} Crew", purpose: "+{n} Purpose", foresee: "foresee", temper_legacy: "temper the Elder's Legacy",
  crew_strike: "every Crew there deals its damage now" };
const fx = (e) => Object.entries(e).map(([k, v]) => (VERB[k] ?? k).replace("{n}", v)).join("; ");

function personCard(c) {
  const t = c.target.kind === "house" ? "Another house" : `Range ${c.target.range} · ${c.target.type}`;
  const th = c.threshold ? `<div class="th"><b>If ${Object.entries(c.threshold.elements).map(([g, n]) => `${g} ${n}`).join(" + ")}:</b> also ${esc(c.threshold.text)}</div>` : "";
  return `<div class="card ${c.tier === "Remarkable" ? "rem" : ""}">
    <div class="hd"><span>${c.id}${c.tier === "Remarkable" ? " ★" : ""}</span><span>${c.cost} ¢</span></div>
    <div>${c.guilds.map((g) => `<span class="g">${g}</span>`).join("")}</div>
    <div class="tgt">${esc(t)}</div><div>${esc(c.text)}</div>${th}
    <div class="reign"><b>Reign</b> (Day): ${esc(c.reign.text)}</div>
    <div class="legacy"><b>Legacy</b> (Dusk, in its event's sections): ${esc(c.legacy.text)}</div></div>`;
}
function eventCard(e) {
  return `<div class="card event"><div class="hd"><span>${e.id}</span><span class="stage">Stage ${e.stage === 4 ? "Landfall" : e.stage}</span></div>
    <div class="types">${e.types.join(" + ")}</div>
    ${e.twist ? `<div><b>Twist:</b> ${esc(e.twist.text)}</div>` : ""}${e.note ? `<div class="stage">${esc(e.note)}</div>` : ""}
    <div class="reign"><b>Dawn</b> Seed · <b>Day</b> Grow · <b>Dusk</b> Collapse</div></div>`;
}
function discoveryCard(d) {
  const tiers = ["I", "II", "III"].map((t) => `<div><b>${t}:</b> ${esc(d.tiers[t].text)}</div>`).join("");
  return `<div class="card"><div class="hd"><span>${d.id}</span><span class="stage">${d.family}</span></div>
    <div class="stage">Apply now at your Understanding tier, or…</div>${tiers}
    <div class="reign"><b>…Breakthrough</b> (tuck under the Steward, permanent): ${esc(d.breakthrough.text)}</div></div>`;
}
function crisisCard(x) {
  return `<div class="card"><div class="hd"><span>Ship in Crisis</span><span>${x.id}</span></div>
    <div class="types" style="font-size:11pt;font-weight:700">${esc(x.name)}</div><div>${esc(x.text)}</div>
    <div class="reign">Flip when the Decay pool first runs out; add 1 Decay per player to the pool.</div></div>`;
}
const FILL = { Infrastructure: "#c9d4e0", Residential: "#e8d6c0", Government: "#d9cfe6", Agricultural: "#cfe3c4" };
function boardHTML(b) {
  const [W, H] = boards.size || [420, 280];
  const secs = b.sections.map((s) => {
    const set = Object.entries(s.setup).filter(([, n]) => n).map(([k, n]) => `${n} ${k}`).join(", ");
    const [cx, cy] = s.center;
    return `<polygon points="${s.poly.map((p) => p.join(",")).join(" ")}" fill="${FILL[s.type]}" stroke="#1f1b16" stroke-width="${s.hull ? 2.4 : 0.8}" stroke-linejoin="round"/>
      <text x="${cx}" y="${cy - 6}" text-anchor="middle" font-size="11" font-weight="700">${s.id}</text>
      <text x="${cx}" y="${cy + 7}" text-anchor="middle" font-size="8">${s.type}</text>
      <text x="${cx}" y="${cy + 19}" text-anchor="middle" font-size="7">${set}</text>`;
  }).join("");
  const links = Object.entries(boards.links || {}).filter(([k]) => k.includes(b.id)).map(([k, v]) => `${k}: ${v.map((p) => p.join("–")).join(", ")}`).join(" · ");
  return `<div class="board"><b>Ship board ${b.id}</b> · heavy outline = Outer Hull · joins: ${esc(links)}
    <svg viewBox="-4 -4 ${W + 8} ${H + 8}" width="100%" role="img" aria-label="Ship board ${b.id}">${secs}</svg></div>`;
}
function slot(v) {
  if (typeof v === "object") { const [k, n] = Object.entries(v)[0]; return k === "element" ? `+${n}` : k === "fast_play" ? "+fast" : "+clone"; }
  return v;
}
function houseBoard(h) {
  const tiers = h.innate.tiers.map((t) => `<tr><td>${t.tier}</td><td>${Object.entries(t.threshold).map(([g, n]) => `${g} ${n}`).join(" + ")}</td><td>${esc(fx(t.effects))}${t.range !== null ? ` (range ${t.range}, ${t.target})` : ""}</td></tr>`).join("");
  return `<div class="house"><b style="font-size:13pt">${esc(h.name)}</b> <span class="stage">(${esc(h.template)})</span>
    <div>Guilds: <b>${h.guilds.primary}</b> / ${h.guilds.secondary} · Hand = plays + ${h.hand_bonus} · Clone ${h.clone}</div>
    <div><b>Credits per generation</b> (cover with influence; uncover left to right)</div><div class="track">${h.tracks.credits.map((v) => `<span>${slot(v)}</span>`).join("")}</div>
    <div><b>Card plays</b></div><div class="track">${h.tracks.plays.map((v) => `<span>${slot(v)}</span>`).join("")}</div>
    <div><b>Special rule:</b> ${esc(h.special.text)}</div>
    <table><tr><th>Tier</th><th>${esc(h.innate.name)} (${h.innate.speed}) threshold</th><th>Effect (cumulative)</th></tr>${tiers}</table>
    <div><b>Growth (pick one):</b> A place 1 influence${h.growth_overrides?.A?.range ? ` (range ${h.growth_overrides.A.range})` : " (range 1)"}${h.growth_overrides?.A?.influence ? ` ×${h.growth_overrides.A.influence}` : ""} and uncover a track slot · B gain 2 credits${h.growth_perk?.B ? ` + ${esc(h.growth_perk.B.text)}` : ""} · C draw +2 cards and gain 1 credit${h.growth_overrides?.C ? ` (${esc(h.growth_overrides.C.text)})` : ""}</div>
    <div><b>Starting influence:</b> ${esc(h.starting_influence.text)}</div></div>`;
}
const REF = `<div class="ref">
  <h3>Each generation</h3><ol>
  <li><b>Growth:</b> draw a fresh hand (plays + bonus; keep cloned cards), pick growth A/B/C, gain credits.</li>
  <li><b>Commit:</b> choose plays (pay credits). Mark one as your <b>nominee</b>: free, fast, may become heir.</li>
  <li><b>Fast:</b> nominees resolve (plus house fast plays / fast innates).</li>
  <li><b>Dusk:</b> resolve earned Discoveries (apply, or Breakthrough on the Steward). The Elder's <b>Legacy</b>, then the Elder's event <b>Collapses</b>.</li>
  <li><b>Day:</b> the Steward's <b>Reign</b>, then its event <b>Grows</b>.</li>
  <li><b>Dawn:</b> vote an heir from the nominees (tie: Steward's house). Draw the next event, pair it, <b>Seed</b>.</li>
  <li><b>Slow:</b> other plays and slow innates resolve.</li>
  <li><b>Time passes:</b> Dusk → Wall, Day → Dusk, Dawn → Day. Clear damage, Brace, Quarantine. Discard hands except clones.</li></ol>
  <h3>Event actions (cards name section types)</h3>
  <p><b>Seed:</b> +1 Glitch in each matching section on the Outer Hull or next to a Fault/Failure. <b>Grow:</b> +1 Fault in each matching section with threat (Failure instead if it has 2+ Faults). <b>Collapse:</b> each matching section takes Glitch 1 + Fault 2 + Failure 3 damage (+1 Unrest, − Brace/Isolate). 2+ damage places Decay. The same damage hits Crew (2 health each). Surviving Crew deal 2 damage each.</p>
  <h3>Decay</h3><p>Taken from the pool. Each house loses 1 influence there. Decay where Decay already is cascades to a neighbor. Pool empty: flip Ship in Crisis. Empty again: lose.</p>
  <h3>Purpose and Understanding</h3><p>Destroy a Fault +1, a Failure +2 Purpose. A full pool (5 per player) earns a Discovery. Every 3 Discoveries raise Understanding.</p>
  <h3>Winning (at any moment)</h3><p><b>I:</b> no threat and no Decay · <b>II:</b> no threat · <b>III:</b> no Faults or Failures, plus the destination's Landfall requirement.</p>
  <h3>Losing</h3><p>The event deck is empty at Dawn; the Decay pool runs out after the crisis flip; or any house has no influence.</p>
  <h3>Tokens</h3><p><b>Brace X:</b> prevent X damage · <b>Quarantine:</b> nothing seeds, vents or cascades in or out · <b>Patch:</b> skip next Grow · <b>Lockout:</b> skip next Seed · <b>Unrest:</b> +1 damage from every source · <b>Isolate:</b> negate damage at next Collapse.</p>
  <h3>Setup (2 players)</h3><p>Boards A–B. Decay pool 3 per player − 1; Purpose pool 5 per player; event deck 3 Stage I / 4 Stage II / 5 Stage III (Stage I on top). Draw the first event and a random Common leader into Dawn, Seed, then move them to Day.</p></div>`;

const parts = {
  ref: `<h1>Generation Ship: rules reference</h1>${REF}`,
  houses: `<h2>House boards</h2>${houses.houses.map(houseBoard).join("")}`,
  boards: `<h2>Ship boards</h2>${boards.boards.map(boardHTML).join("")}`,
  events: `<h2>Event cards</h2><div class="sheet">${[...events.cards, events.landfall].map(eventCard).join("")}</div>`,
  disc: `<h2>Discoveries and Ship in Crisis</h2><div class="sheet">${discoveries.map(discoveryCard).join("")}${crisis.cards.map(crisisCard).join("")}</div>`,
  rem: `<h2>Remarkable people</h2><div class="sheet">${people.filter((c) => c.tier === "Remarkable").map(personCard).join("")}</div>`,
  common: `<h2>Common people</h2><div class="sheet">${people.filter((c) => c.tier === "Common").map(personCard).join("")}</div>`,
};
function render() {
  const on = [...document.querySelectorAll("[data-part]")].filter((x) => x.checked).map((x) => x.dataset.part);
  document.getElementById("out").innerHTML = on.map((p) => parts[p]).join("");
}
document.querySelectorAll("[data-part]").forEach((x) => x.addEventListener("change", render));
render();
