// Print-and-play kit for Stewards of the Long Voyage, rendered from data/*.json with the Retro art
// (art/source/retro) and the icon language (art/icons/*.svg, art/icons/effects.json, both owned by
// the art tools). Cards are poker size (63 x 88 mm), nine per A4 page.
const get = async (f) => (await fetch(f)).json();
const exists0 = async (url) => { try { return (await fetch(url, { method: "HEAD" })).ok; } catch { return false; } };
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const [allPeople, events, discoveries, crisis, boards, houses, destinations, ICONS, PLAYTEST] = await Promise.all(
  ["people.json", "events.json", "discoveries.json", "crisis.json", "boards.json", "houses.json", "destinations.json"]
    .map((f) => get(`data/${f}`)).concat([get("art/icons/effects.json"), get("data/playtest_deck.json")]));
// The curated playtest deck (tools/playtest_deck.py) unless "all 400" is chosen.
const ptIds = new Set([...PLAYTEST.common, ...PLAYTEST.remarkable]);
const peopleFor = () => (document.getElementById("fulldeck")?.checked ? allPeople : allPeople.filter((c) => ptIds.has(c.id)));
const ART = "art/source/retro/";
// Ink saver (default on): pale windows and washed frames from tools/inksaver_assets.py (print/assets).
const inkSaver = () => document.getElementById("inksaver")?.checked;
const FRAME = (full, saver) => (inkSaver() ? `print/assets/${saver}` : `${ART}${full}`);
const exists = async (url) => { try { return (await fetch(url, { method: "HEAD" })).ok; } catch { return false; } };

// ---------------------------------------------------------------- icons
// Until the art tools ship a "contain" glyph, Contain borrows the old Isolate one.
const ICON_ALIAS = (await exists0("art/icons/contain.svg")) ? {} : { contain: "isolate" };
const I = (name, cls = "ic") => `<img class="${cls}" src="art/icons/${ICON_ALIAS[name] || name}.svg" alt="${name.replace(/_/g, " ")}">`;
const TYPE_ICON = { Infrastructure: "type_infrastructure", Residential: "type_residential", Government: "type_government", Agricultural: "type_agricultural" };
const ROMAN = ["", "I", "II", "III", "L"];

// One effect key + amount -> icon items (art/icons/effects.json), with a text fallback.
function items(key, n, ctx) {
  const tpl = (ctx === "wall" && ICONS.wall[key]) || ICONS.effects[key] || ICONS.effects[key.replace(/^contain_/, "isolate_")];
  if (tpl) return { kind: tpl.kind, html: tpl.items.map(([t, v]) => (t === "icon" ? I(v) : `<b>${esc(String(v).replace("{n}", n))}</b>`)).join("") };
  if (key === "element") return { kind: "benefit", html: `${I(`guild_${n}`)}<b>+1</b>${I("each_house")}` };
  const verb = ICONS.verbs[key] || (key === "downgrade_fault" ? ICONS.verbs.downgrade : null);
  if (verb) {
    const num = n !== 1 || ICONS.count_always.includes(key) ? `<b>${n}</b>` : "";
    return { kind: "", html: num + verb.map((v) => (v === "/" ? `<b>/</b>` : I(v))).join("") };
  }
  return { kind: "", html: `<span class="tx">${esc(key.replace(/_/g, " "))} ${n}</span>` };
}
const fxRow = (effects, ctx) => Object.entries(effects).map(([k, n]) => {
  const it = items(k, n, ctx);
  return `<span class="fx ${it.kind}">${it.html}</span>`;
}).join(`<span class="sep"></span>`);
const req = (els) => Object.entries(els).map(([g, n]) => `<span class="fx"><b>${n}</b>${I(`guild_${g}`)}</span>`).join("");

// ---------------------------------------------------------------- people cards
function targetHTML(c) {
  const t = c.target;
  if (t.kind === "house") return `${I("each_house")}<span class="tx">another house</span>`;
  const type = TYPE_ICON[t.type] ? I(TYPE_ICON[t.type]) : t.type === "Hull" ? I("hull") : `<span class="tx">${esc(t.type === "ANY" ? "any section" : t.type)}</span>`;
  return `${I("range")}<b>${t.range}</b>${type}`;
}
// guild column (Spirit Island style): all eight, fixed order, the card's own in colour
const GUILD_ORDER = ["Engineers", "Navigators", "Bureaucrats", "Farmers", "Medics", "Laborers", "Keepers", "Scholars"];
function personCard(c) {
  const rem = c.tier === "Remarkable";
  const th = c.threshold ? `<div class="row th">${req(c.threshold.elements)}<span class="arrow">→</span>${fxRow(c.threshold.effects)}</div>` : "";
  return `<div class="card person ${rem ? "rem" : ""}">
    <img class="frame" src="${FRAME("card_frame_v4a_exact.png", "card_frame_inksaver.png")}" alt="">
    <div class="name"><span>${c.id}${rem ? " ★" : ""}</span><span class="cost"><b>${c.cost}</b>${I("credits")}</span></div>
    <div class="gcol">${GUILD_ORDER.map((g, i) => `<img class="g ${c.guilds.includes(g) ? "on" : "off"}" style="top:${(13.9 + i * 6.6 - 3).toFixed(2)}mm" src="art/icons/guild_${g}.svg" alt="${g}">`).join("")}</div>
    <div class="panel"><div class="row eff"><span class="target">${targetHTML(c)}</span>${fxRow(c.effects)}</div>${th}
      <div class="row reign">${I("day")}<span class="lbl">Reign</span>${fxRow(c.reign.effects)}</div></div>
    <div class="plaque"><span class="lbl">Legacy</span>${fxRow(c.legacy.effects)}</div></div>`;
}

// ---------------------------------------------------------------- event cards (tuck below the leader)
function eventCard(e) {
  const types = e.types[0] === "ALL" ? Object.keys(TYPE_ICON) : e.types;
  const icon = (t) => (TYPE_ICON[t] ? I(TYPE_ICON[t], "ic huge") : t === "Hull" ? I("hull", "ic huge") : "");
  const name = e.types[0] === "ALL" ? "Every section" : e.types.map((t) => (t === "Hull" ? "Outer Hull" : t)).join(" + ");
  return `<div class="card event">
    <img class="frame" src="${FRAME("event_frame_b.png", "event_frame_inksaver.png")}" alt="">
    <div class="ev-art">${types.map(icon).join("")}</div>
    <div class="ev-once"><span class="lbl">When revealed</span><span class="muted">no one-time effect</span></div>
    <div class="ev-stage">${ROMAN[e.stage] || e.stage}</div>
    <div class="ev-icons">${[0, 1].map((i) => (types[i] && i < 2 ? `<span>${TYPE_ICON[types[i]] ? I(TYPE_ICON[types[i]]) : I("hull")}</span>` : `<span class="empty"></span>`)).join("")}</div>
    <div class="ev-name">${esc(e.id === "LANDFALL" ? "LANDFALL · " + name : name)}</div>
    <div class="ev-twist">${e.twist ? esc(e.twist.text) : `${I("seed")} Dawn · ${I("grow")} Day · ${I("collapse")} Dusk`}</div></div>`;
}

// ---------------------------------------------------------------- discoveries, crisis, destinations
function discoveryCard(d) {
  const tiers = ["I", "II", "III"].map((t) => `<div class="row"><span class="tier">${t}</span>${fxRow(d.tiers[t].effects)}</div>`).join("");
  return `<div class="card plain">
    <div class="hd"><span>Discovery ${d.id}</span><span>${esc(d.family)}</span></div>
    <div class="note">Apply now at your Understanding tier, in one section of your choice per board:</div>${tiers}
    <div class="bt"><span class="lbl">…or Breakthrough</span><div class="note">Tuck under the Steward. Switches on when it reaches the Wall.</div>
      <div class="row">${fxRow(d.breakthrough.effects, "wall")}</div></div></div>`;
}
function crisisCard(x) {
  return `<div class="card plain crisis"><div class="hd"><span>Ship in Crisis</span><span>${x.id}</span></div>
    <div class="big">${esc(x.name)}</div><div>${esc(x.text)}</div>
    <div class="bt note">Flip when the Decay pool first runs out; add 1 ${I("decay")} per player to the pool.</div></div>`;
}
function destinationSheet(d) {
  return `<div class="house plain"><div class="hd"><span>Destination: ${esc(d.name)}</span><span>Understanding every ${d.discoveries_per_tier ?? 3} ${I("purpose")}Discoveries</span></div>
    <p class="note">${esc(d.flavor || "")}</p><ol>${d.levels.map((l) => `<li><b>Level ${l.level}:</b> ${esc(l.text)}</li>`).join("")}</ol></div>`;
}

// ---------------------------------------------------------------- house boards
function slot(v) {
  if (typeof v !== "object") return `<b>${v}</b>`;
  const [k, n] = Object.entries(v)[0];
  return k === "element" ? I(`guild_${n}`) : k === "fast_play" ? I("fast") : k === "draw" ? I("draw") : I("clone");
}
function houseBoardHTML(h) {
  const tiers = h.innate.tiers.map((t) => `<tr><td>${ROMAN[t.tier]}</td><td>${req(t.threshold)}</td><td>${fxRow(t.effects)}${t.range !== null ? ` ${I("range")}<b>${t.range}</b>` : ""}</td></tr>`).join("");
  return `<div class="house" style="--hc:${HOUSE_COLOURS[h.id] || "#0F3A48"}"><div class="banner">${I(`crest_${h.id}`, "ic crest")}</div>
    <div class="hd"><span>${esc(h.name)}</span><span>${I(`guild_${h.guilds.primary}`)}${I(`guild_${h.guilds.secondary}`)}</span></div>
    <div class="row">${I("credits")}<span class="track">${h.tracks.credits.map((v) => `<span>${slot(v)}</span>`).join("")}</span></div>
    <div class="row">${I("card")}<span class="track">${h.tracks.plays.map((v) => `<span>${slot(v)}</span>`).join("")}</span></div>
    <table><tr><th></th><th>${esc(h.innate.name)} ${I(h.innate.speed === "fast" ? "fast" : "slow")}</th><th></th></tr>${tiers}</table>
    <div class="note"><b>Special:</b> ${esc(h.special.text)}</div>
    <div class="note"><b>Growth</b> A: place influence and uncover a track slot · B: +2 ${I("credits")}${h.growth_perk?.B ? ` and ${esc(h.growth_perk.B.text)}` : ""} · C: draw +2 and +1 ${I("credits")}${h.growth_overrides?.C ? ` (${esc(h.growth_overrides.C.text)})` : ""}</div>
    <div class="note"><b>Hand</b> = plays + ${h.hand_bonus} · <b>Clone</b> ${h.clone} · <b>Start:</b> ${esc(h.starting_influence.text)}</div></div>`;
}
const HOUSE_COLOURS = { galvan: "#3A6FD8", meridian: "#2A9D8F", keel: "#7A8C96", vigil: "#E8A23A", foremen: "#C9482A", gardeners: "#8FB04A", voidwardens: "#6A4A9A", tellers: "#D86A8A" };
async function houseBoard(h) {
  const png = `${ART}house_${h.id}_v3_typeset.png`;
  if (await exists(png)) return `<div class="house art"><img src="${png}" alt="${esc(h.name)} house board"></div>`;
  return houseBoardHTML(h);
}

// ---------------------------------------------------------------- ship boards (Retro art at real scale)
// Same frame as tools/retro_templates.py board_frame(): the art's px <-> board units.
const BOARD_PX = [1296, 1536], BOARD_MARGIN = 10;
// True scale is 100 mm per 180 units (a 216 x 256 mm sheet: A3). On A4 every board prints at 90 %,
// so boards still dock with each other; Crew and tokens are unaffected.
const boardMode = () => document.getElementById("boardmode")?.value || "a4";   // a4 (90 %) · a3 (100 %) · halves (100 % on two A4 sheets)
const boardScale = () => (boardMode() === "a4" ? 0.9 : 1);
const mmPerUnit = () => (100 / boards.radius) * boardScale();
function boardFrame() {
  const pts = boards.outline.concat(boards.void_zone);
  const xs = pts.map((p) => p[0]), ys = pts.map((p) => p[1]);
  const x0 = Math.min(...xs) - BOARD_MARGIN, x1 = Math.max(...xs) + BOARD_MARGIN, y0 = Math.min(...ys) - BOARD_MARGIN, y1 = Math.max(...ys) + BOARD_MARGIN;
  const s = Math.min(BOARD_PX[0] / (x1 - x0), BOARD_PX[1] / (y1 - y0));
  return { s, ox: (BOARD_PX[0] - s * (x1 - x0)) / 2 - s * x0, oy: (BOARD_PX[1] - s * (y1 - y0)) / 2 - s * y0 };
}
const SETUP_ICON = { glitch: "glitch", fault: "fault", failure: "failure", crew: "crew", decay: "decay" };
async function boardHTML(b) {
  const { s, ox, oy } = boardFrame();
  const P = (poly) => poly.map(([x, y]) => `${(ox + s * x).toFixed(1)},${(oy + s * y).toFixed(1)}`).join(" ");
  const art = `${ART}board_${b.id.toLowerCase()}_v2_toned.png`;
  // Board art painted for an older geometry is not used (D was reshaped 2026-11-06; waiting on new art).
  const STALE_ART = new Set(["D"]);
  const hasArt = !STALE_ART.has(b.id) && (await exists(art));
  const wmm = (BOARD_PX[0] / s) * mmPerUnit(), hmm = (BOARD_PX[1] / s) * mmPerUnit();
  const labels = b.sections.map((sec) => {
    const [cx, cy] = sec.center, X = ox + s * cx, Y = oy + s * cy;
    const setup = Object.entries(sec.setup).filter(([, n]) => n).flatMap(([k, n]) => Array(n).fill(SETUP_ICON[k]));
    const ic = (name, i, n) => `<image href="art/icons/${name}.svg" x="${X - (n * 36) / 2 + i * 36}" y="${Y + 16}" width="34" height="34"/>`;
    return `<g><circle cx="${X}" cy="${Y - 30}" r="30" fill="#FBEFD6" fill-opacity="0.92" stroke="#0F3A48" stroke-width="3"/>
      <image href="art/icons/${TYPE_ICON[sec.type]}.svg" x="${X - 24}" y="${Y - 54}" width="48" height="48"/>
      <text x="${X}" y="${Y + 8}" text-anchor="middle" font-family="Righteous, sans-serif" font-size="26" fill="#0F3A48" stroke="#FBEFD6" stroke-width="5" paint-order="stroke">${sec.id}</text>
      ${setup.map((n, i) => ic(n, i, setup.length)).join("")}</g>`;
  }).join("");
  const body = (attrs) => `<svg ${attrs}>
      <defs><clipPath id="clip${b.id}${attrs.length}"><polygon points="${P(boards.outline)}"/><polygon points="${P(boards.void_zone)}"/></clipPath></defs>
      ${hasArt ? `<image href="${art}" width="${BOARD_PX[0]}" height="${BOARD_PX[1]}" clip-path="url(#clip${b.id}${attrs.length})"/>` : `<polygon points="${P(boards.void_zone)}" fill="#0F3A48"/><polygon points="${P(boards.outline)}" fill="#C9D1D6"/>${b.sections.map((sec) => `<polygon points="${P(sec.poly)}" fill="${FILL[sec.type]}" fill-opacity="0.75"/>`).join("")}`}
      ${b.sections.map((sec) => `<polygon points="${P(sec.poly)}" fill="none" stroke="#FBEFD6" stroke-width="4" stroke-linejoin="round"/>`).join("")}
      <polygon points="${P(boards.outline)}" fill="none" stroke="#0F3A48" stroke-width="5" stroke-linejoin="round"/>
      <polygon points="${P(boards.void_zone)}" fill="none" stroke="#0F3A48" stroke-width="3" stroke-dasharray="14 10"/>
      ${labels}</svg>`;
  const cap = (extra) => `<div class="cap"><b>Ship board ${b.id}</b>${extra} · cut along the outline and around the void · ${wmm.toFixed(0)} × ${hmm.toFixed(0)} mm (${Math.round(boardScale() * 100)} % scale) · the top edge (fins and prow) is the Outer Hull; the other five sides dock with any board · printed pieces show the setup</div>`;
  if (boardMode() !== "halves") return `<div class="shipboard">${cap("")}${body(`viewBox="0 0 ${BOARD_PX[0]} ${BOARD_PX[1]}" style="width:${wmm.toFixed(1)}mm;height:${hmm.toFixed(1)}mm"`)}</div>`;
  // 100 % on A4: top and bottom halves on landscape sheets, overlapping by 8 mm; trim the top half at the dashed line and tape
  const ov = (8 / hmm) * BOARD_PX[1], mid = BOARD_PX[1] / 2;
  const half = (y0, y1, label, cut) => `<div class="shipboard half">${cap(` · ${label}`)}<div class="halfwrap">${body(`viewBox="0 ${y0.toFixed(1)} ${BOARD_PX[0]} ${(y1 - y0).toFixed(1)}" style="width:${wmm.toFixed(1)}mm;height:${(((y1 - y0) / BOARD_PX[1]) * hmm).toFixed(1)}mm"`)}${cut}</div></div>`;
  return half(0, mid + ov, "top half: trim at the dashed line", `<div class="cutline" style="top:${((mid / BOARD_PX[1]) * hmm).toFixed(1)}mm"></div>`)
    + half(mid - ov, BOARD_PX[1], "bottom half: slide under the top half to the dashed line and tape on the back", `<div class="cutline" style="top:${((ov / BOARD_PX[1]) * hmm).toFixed(1)}mm"></div>`);
}
const tfp = ([x, y], [px, py, rot]) => { const r = (rot * Math.PI) / 180; return [x * Math.cos(r) - y * Math.sin(r) + px, x * Math.sin(r) + y * Math.cos(r) + py]; };
const FILL = { Infrastructure: "#3AB0A8", Residential: "#F2A060", Government: "#E88AA0", Agricultural: "#A8C860" };
function layoutsHTML() {
  const B = Object.fromEntries(boards.boards.map((b) => [b.id, b]));
  return Object.entries(boards.layouts || {}).filter(([, l]) => l.boards.length > 1).map(([name, l]) => {
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    const parts = l.boards.map((bid) => {
      const pl = l.place[bid];
      return B[bid].sections.map((s) => {
        const pts = s.poly.map((p) => tfp(p, pl));
        pts.forEach(([x, y]) => { minX = Math.min(minX, x); minY = Math.min(minY, y); maxX = Math.max(maxX, x); maxY = Math.max(maxY, y); });
        return `<polygon points="${pts.map((p) => p.join(",")).join(" ")}" fill="${FILL[s.type]}" stroke="#0F3A48" stroke-width="2"/>`;
      }).join("") + (([cx, cy]) => `<text x="${cx}" y="${cy + 14}" text-anchor="middle" font-size="44" font-family="Righteous, sans-serif" fill="#0F3A48">${bid}</text>`)(tfp([0, 0], pl));
    }).join("");
    return `<div class="layout"><b>${name}</b> · ${l.boards.length} boards, ${l.links.length} docking links
      <svg viewBox="${minX - 10} ${minY - 10} ${maxX - minX + 20} ${maxY - minY + 20}">${parts}</svg></div>`;
  }).join("");
}

// ---------------------------------------------------------------- Wall of Leaders (dual layer)
const wallHTML = () => [1, 2, 3].map((p) => `<div class="wall"><div class="cap"><b>Wall of Leaders, panel ${p} of 3 (top layer)</b> · 290 × 120 mm, on card stock · cut out the two windows of each slot and a slit along the top edge of each slot · slots ${(p - 1) * 4 + 1}–${p * 4}</div>
    <div class="wallpanel"><img src="${FRAME("wall_panel_v4b_exact.png", "wall_panel_inksaver.png")}" alt="Wall panel">
      ${[0, 1, 2, 3].map((i) => `<span class="slotno" style="left:${36.25 + i * 72.5}mm">${["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"][(p - 1) * 4 + i]}</span>`).join("")}</div></div>`).join("")
  + `<div class="wall"><div class="cap"><b>Backing layer</b> (print 3) · glue to the back of each top layer along the sides and bottom only, so cards slide in from the top</div><div class="backing"></div></div>`;

// ---------------------------------------------------------------- tokens (punch sheet)
// Counts from sim/components.js (the most on the table at once in 4-player games, plus a margin).
// Brace stacks, so it comes in values; Patch and Lockout stack too (up to 7). Contain is a marker on one threat piece.
const TOKENS = [["glitch", 45, "#2E6FD8"], ["fault", 25, "#F6C85A"], ["failure", 8, "#D8332A"], ["crew", 55, "#D9B98A"], ["decay", 15, "#7A4A30"],
  ["brace", 24, "#FBEFD6", 1], ["brace", 16, "#FBEFD6", 2], ["brace", 8, "#FBEFD6", 5],
  ["contain", 12, "#FBEFD6"],
  ["patch", 30, "#FBEFD6"], ["lockout", 30, "#FBEFD6"], ["quarantine", 4, "#FBEFD6"], ["unrest", 6, "#FBEFD6"]];
const tok = (n, c, v) => `<span class="tok" style="--c:${c}">${I(n)}${v ? `<b class="tv">${v}</b>` : ""}</span>`;
const tokensHTML = () => `<div class="tokens">${TOKENS.flatMap(([n, k, c, v]) => Array(k).fill(tok(n, c, v))).join("")}
  ${Object.keys(HOUSE_COLOURS).flatMap((h) => Array(26).fill(`<span class="tok inf" style="--c:${HOUSE_COLOURS[h]}">${I(`crest_${h}`)}</span>`)).join("")}
  ${Array(12).fill(`<span class="tok" style="--c:#F6C85A">${I("purpose")}</span>`).join("")}</div>
  <p class="note">16 mm tokens, sized from simulated games (sim/components.js: the most of each on the table at once in 4-player games, plus a margin).
  45 Glitch, 25 Fault, 8 Failure, 55 Crew, 15 Decay, 26 influence banners per house, and 12 starbursts (Breakthrough markers).
  Brace comes in values 1, 2 and 5 (make change). Patch and Lockout stack: use several. Contain markers sit on one threat piece each and move with it.
  Damage: tip a token over at 1 damage; turn a Failure face down at 2. Only print the house banners you play with.</p>`;

// ---------------------------------------------------------------- playtest record sheet
// Mirrors the browser prototype's playtest record, so paper and digital playtests compare.
const field = (label, w = "100%") => `<div class="fld" style="width:${w}"><span>${label}</span></div>`;
const recordHTML = () => `<div class="record">
  <h3>Game</h3><div class="flds">${field("Date", "24%")}${field("Players", "24%")}${field("Seed / setup notes", "48%")}
    ${field("Houses (seat order)", "64%")}${field("Ship layout", "32%")}
    ${field("Destination + level", "32%")}${field("Landfall: off / when ready / shuffled", "40%")}${field("Deck: playtest / full", "24%")}</div>
  <h3>Result</h3><div class="flds">${field("Win / loss", "24%")}${field("Cause (tier, Landfall, time, Decay, influence)", "48%")}${field("Ended in generation", "24%")}
    ${field("Understanding tier at the end", "32%")}${field("Discoveries earned / applied / Breakthroughs", "64%")}</div>
  <h3>Each generation</h3>
  <table class="gens"><tr><th>Gen</th><th>Heir (house)</th><th>Event</th><th>Decay pool</th><th>Purpose</th><th>Discoveries</th><th>Crisis?</th><th>Notes</th></tr>
    ${Array.from({ length: 13 }, (_, i) => `<tr><td>${i + 1}</td>${"<td></td>".repeat(7)}</tr>`).join("")}</table>
  <h3>Per house</h3>
  <table class="gens"><tr><th>House</th><th>Heirs chosen</th><th>Remarkables taken</th><th>Innate tier reached most</th><th>Felt strong / weak?</th></tr>
    ${Array.from({ length: 4 }, () => `<tr>${"<td></td>".repeat(5)}</tr>`).join("")}</table>
  <h3>Your notes</h3><div class="flds">${field("Fun, 1–5", "24%")}${field("Length felt: short / right / long", "48%")}${field("Would play again?", "24%")}
    ${["What felt good?", "What was confusing?", "What felt broken or pointless?", "Rules you had to look up (page or topic)"].map((q) => `<div class="fld big"><span>${q}</span></div>`).join("")}</div>
  <p class="note">Enter the same details in the browser prototype's playtest record (end-of-game screen), or photograph this sheet and send it back.</p></div>`;

// ---------------------------------------------------------------- rules reference
const REF = `<div class="ref">
  <h3>Each generation</h3><ol>
  <li>${I("growth")} <b>Growth:</b> draw a fresh hand (plays + bonus; keep cloned cards), pick growth A/B/C, gain credits.</li>
  <li><b>Commit:</b> choose plays (pay ${I("credits")}). Mark one as your <b>nominee</b>: 3 credits off (Commons free), fast, may become heir.</li>
  <li>${I("fast")} <b>Fast:</b> nominees resolve (plus house fast plays / fast innates), in the order each house chooses.</li>
  <li>${I("dusk")} <b>Dusk:</b> resolve Discoveries earned before this Dusk (the Steward's house applies each in one section per board, or makes it a Breakthrough). Wall bonuses. The Elder's <b>Legacy</b> takes hold for the rest of the voyage, then the Elder's event ${I("collapse")} <b>Collapses</b>.</li>
  <li>${I("day")} <b>Day:</b> the Steward's <b>Reign</b>, then its event ${I("grow")} <b>Grows</b>.</li>
  <li>${I("dawn")} <b>Dawn:</b> vote an heir from the nominees (tie: the house with fewer leaders on the conveyor, then the Steward's house). Only then draw the next event, tuck it under the heir, and ${I("seed")} <b>Seed</b>.</li>
  <li>${I("slow")} <b>Slow:</b> other plays and slow innates resolve.</li>
  <li><b>Time passes:</b> Dusk → Wall (its Breakthrough switches on for the rest of the game), Day → Dusk, Dawn → Day. Stand damaged pieces back up; clear Brace and Quarantine. Discard hands except clones.</li></ol>
  <h3>Event actions (cards name section types)</h3>
  <p>${I("seed")} <b>Seed:</b> +1 ${I("glitch")} in each matching section on the Outer Hull or next to a ${I("fault")}/${I("failure")}. ${I("grow")} <b>Grow:</b> +1 ${I("fault")} in each matching section with threat (a ${I("failure")} instead if it has 2+ Faults). ${I("collapse")} <b>Collapse:</b> each matching section takes ${I("glitch")}1 + ${I("fault")}2 + ${I("failure")}3 damage (+1 ${I("unrest")}, − ${I("brace")}/${I("isolate")}). 2+ damage places ${I("decay")}. The same damage hits ${I("crew")} (2 health each); surviving Crew then strike for 2 damage each.</p>
  <h3>Threat and damage</h3><p>${I("glitch")} health 1 · ${I("fault")} health 2 · ${I("failure")} health 3. Damage that doesn't destroy a piece tips it over (a Failure at 2 damage turns face down). ${I("downgrade")} A downgrade swaps a piece for the next smaller one, undamaged.</p>
  <h3>Your choices</h3><p>A card's own guilds count toward its bonus, but every bonus needs at least one more element from another card, a track slot or the Wall. ${I("vent")} Venting and ${I("gather")} gathering are optional.</p>
  <h3>Decay</h3><p>${I("decay")} comes from the pool. Each house loses 1 ${I("influence")} there. Decay where Decay already is cascades to a neighbor. Pool empty: flip Ship in Crisis. Empty again: lose.</p>
  <h3>Purpose and Understanding</h3><p>Destroy a ${I("fault")} +1, a ${I("failure")} +2 ${I("purpose")}. A full pool (6 per player) earns a Discovery. The destination sets how many Discoveries raise Understanding (3 with no destination).</p>
  <h3>Winning (at any moment)</h3><p><b>I:</b> no threat and no Decay · <b>II:</b> no threat · <b>III:</b> no Faults or Failures, plus the destination's Landfall requirement.</p>
  <h3>Losing</h3><p>The event deck is empty at Dawn; the Decay pool runs out after the crisis flip; or any house has no influence.</p>
  <h3>Tokens</h3><p>${I("brace")} <b>Brace X:</b> prevent X damage · ${I("quarantine")} <b>Quarantine:</b> nothing seeds, vents or cascades in or out · ${I("patch")} <b>Patch:</b> skip next Grow · ${I("lockout")} <b>Lockout:</b> skip next Seed · ${I("unrest")} <b>Unrest:</b> +1 damage from every source · ${I("contain")} <b>Contain:</b> a marker on one threat piece, which moves with it; that piece deals no damage at the next Collapse there, then the marker comes off.</p>
  <h3>Setup (2 players)</h3><p>Boards A–B (pair layout). Decay pool 3 per player − 1; Purpose pool 6 per player; event deck 3 Stage I / 4 Stage II / 5 Stage III (Stage I on top). Draw the first event and a random Common leader into Day (the starting Steward belongs to no house), Seed, and begin.</p></div>
  <h2>Icon glossary</h2><img class="glossary" src="art/icons/icon_sheet.svg" alt="Icon glossary">`;

// ---------------------------------------------------------------- assemble
const sheet = (cards) => `<div class="sheet">${cards.join("")}</div>`;
// Card decks print one sheet per page, each with the same one-line header, so a backs page lines up
// behind its fronts page when printed double-sided (flip on the long edge). Every backs page is a full
// nine, so a short last fronts page is still covered.
const DECKS = {
  people: { label: "People", color: "#0F3A48", icon: "crew" },
  remarkable: { label: "Remarkable ★", color: "#B8862E", icon: "crew" },
  events: { label: "Event", color: "#E8603A", icon: "collapse" },
  disc: { label: "Discovery", color: "#3AB0A8", icon: "purpose" },
  crisis: { label: "Ship in Crisis", color: "#C8402A", icon: "decay" },
};
const duplex = () => document.getElementById("duplex")?.checked;
const backCard = (deck) => `<div class="card back"><img class="frame" src="${FRAME("card_back.png", "card_back_inksaver.png")}" alt="">
  <div class="bk-label" style="background:${DECKS[deck].color}">${I(DECKS[deck].icon)}<span>${DECKS[deck].label}</span></div></div>`;
const cardPage = (title, cards) => `<div class="cardpage"><div class="ph">${title}</div>${sheet(cards)}</div>`;
// fronts (and, double-sided, a backs page after each); `backsFor` collects the separate backs pages
const backsFor = [];
function deckPages(deck, title, cards) {
  const out = [], n = Math.ceil(cards.length / 9);
  for (let i = 0; i < n; i++) {
    const t = `${title} · sheet ${i + 1} of ${n}`;
    out.push(cardPage(t, cards.slice(i * 9, i * 9 + 9)));
    const back = cardPage(`${t} · backs`, Array(9).fill(backCard(deck)));
    if (duplex()) out.push(back); else backsFor.push(back);
  }
  return out.join("");
}
const parts = {
  ref: async () => `<h1>Stewards of the Long Voyage · rules reference</h1>${REF}`,
  houses: async () => `<h2>House boards</h2>${(await Promise.all(houses.houses.map(houseBoard))).join("")}`,
  boards: async () => `${boardMode() === "halves" ? "" : "<h2>Ship boards</h2>"}${(await Promise.all(boards.boards.map(boardHTML))).join("")}<h2>Ship layouts</h2><div class="layouts">${layoutsHTML()}</div>`,
  wall: async () => `<h2 class="land">Wall of Leaders</h2>${wallHTML()}`,
  events: async () => deckPages("events", "Event cards", [...events.cards, events.landfall].map(eventCard)),
  disc: async () => deckPages("disc", "Discoveries", discoveries.map(discoveryCard)) + deckPages("crisis", "Ship in Crisis", crisis.cards.map(crisisCard))
,
  dest: async () => `<h2>Destinations</h2>${destinations.destinations.map(destinationSheet).join("")}`,
  tokens: async () => `<h2>Tokens</h2>${tokensHTML()}`,
  rem: async () => deckPages("remarkable", "Remarkable people", peopleFor().filter((c) => c.tier === "Remarkable").map(personCard)),
  common: async () => deckPages("people", "Common people", peopleFor().filter((c) => c.tier === "Common").map(personCard)),
  record: async () => `<h2>Playtest record</h2>${recordHTML()}`,
  backs: async () => backsFor.join(""),   // filled by the card parts above (empty when double-sided)
};
async function render() {
  const on = [...document.querySelectorAll("[data-part]")].filter((x) => x.checked).map((x) => x.dataset.part);
  backsFor.length = 0;
  document.body.classList.toggle("ink", !!inkSaver());
  const html = [];
  for (const p of on) html.push(await parts[p]());   // in order: the card parts fill backsFor before "backs"
  document.getElementById("out").innerHTML = html.join("");
  document.body.dataset.ready = "1";
}
document.querySelectorAll("[data-part], #boardmode, #fulldeck, #inksaver, #duplex").forEach((x) => x.addEventListener("change", render));
for (const opt of location.hash.slice(1).split(",")) {
  if (opt === "duplex") document.getElementById("duplex").checked = true;
  if (opt === "fullink") document.getElementById("inksaver").checked = false;
  if (opt === "halves" || opt === "a3") document.getElementById("boardmode").value = opt;
  if (opt === "boardsonly") document.querySelectorAll("[data-part]").forEach((x) => { x.checked = x.dataset.part === "boards"; });
  if (opt === "cardsonly") document.querySelectorAll("[data-part]").forEach((x) => { x.checked = ["events", "disc", "rem", "common"].includes(x.dataset.part); });
}
render();
