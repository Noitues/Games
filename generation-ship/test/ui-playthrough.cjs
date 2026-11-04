// Human-style browser playthrough: plays complete games in the prototype making random (but legal)
// choices for every decision kind, and fails on page errors, stuck prompts or unfinished games.
//   python3 -m http.server 8765 &   (from generation-ship/)
//   NODE_PATH=$(npm root -g) node test/ui-playthrough.cjs [http://localhost:8765/index.html]
const { chromium } = require("playwright");

const URL = process.argv[2] || "http://localhost:8765/index.html";
const GAMES = [
  { name: "2p humans, pair", players: 2, houses: ["tellers", "meridian"], seats: ["human", "human"], seed: 3 },
  { name: "3p humans, direct, Cinder 3, Landfall", players: 3, houses: ["vigil", "voidwardens", "gardeners"], seats: ["human", "human", "human"], pairing: "direct", destination: "cinder", level: "3", landfall: "choice", seed: 5 },
  { name: "4p mixed, diamond, Verdant 2", players: 4, houses: ["galvan", "foremen", "keel", "tellers"], seats: ["human", "planner", "human", "planner"], destination: "verdant", level: "2", seed: 7 },
  { name: "1p human solo, Landfall shuffled", players: 1, houses: ["vigil"], seats: ["human"], landfall: "shuffled", seed: 9 },
];
let rs = 12345;
const HINT_RATE = 0.75;
const exactKinds = {};
let hints = 0, undos = 0;
const rnd = () => ((rs = (rs * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff);
const pick = (a) => a[Math.floor(rnd() * a.length)];

(async () => {
  const browser = await chromium.launch();
  let failures = 0;
  const kinds = {};
  for (const g of GAMES) {
    const page = await browser.newPage({ viewport: { width: 1500, height: 1000 } });
    const errors = [];
    page.on("pageerror", (e) => errors.push(e.message));
    page.on("console", (m) => { if (m.type() === "error" && !m.text().includes("favicon")) errors.push(m.text()); });
    await page.goto(URL); await page.waitForTimeout(600);
    await page.selectOption("#players", String(g.players)); await page.waitForTimeout(100);
    for (let i = 0; i < g.players; i++) {
      await page.selectOption(`.seat:nth-child(${i + 1}) .h`, g.houses[i]);
      await page.selectOption(`.seat:nth-child(${i + 1}) .c`, g.seats[i]);
    }
    if (g.pairing) await page.selectOption("#pairing", g.pairing);
    if (g.destination) { await page.selectOption("#destination", g.destination); await page.selectOption("#level", g.level); }
    if (g.landfall) await page.selectOption("#landfall", g.landfall);
    await page.fill("#seed", String(g.seed));
    await page.click("#btn-start");
    let actions = 0, stuck = 0, lastHTML = "";
    let result = null;
    while (actions < 4000) {
      result = await page.evaluate(() => document.querySelector(".banner")?.textContent || null);
      if (result) break;
      const idle = await page.evaluate(() => document.querySelector("#prompt").className === "idle");
      if (idle) { await page.click("#btn-step"); actions++; continue; }
      const html = await page.evaluate(() => document.querySelector("#prompt").innerText);
      if (html === lastHTML) { if (++stuck > 25) { errors.push("stuck on prompt: " + html.slice(0, 200)); break; } } else stuck = 0;
      lastHTML = html;
      const exact = await page.evaluate(() => window.__gsPendingKind?.());
      if (exact) exactKinds[exact] = (exactKinds[exact] || 0) + 1;
      // sometimes take back the last decision (exercises Undo decision)
      if (rnd() < 0.04 && await page.$("#btn-undo-dec")) { await page.click("#btn-undo-dec"); undos++; actions++; continue; }
      // usually follow the hint, so games last long enough to reach late-game decisions
      if (rnd() < HINT_RATE && await page.$("#hint-btn")) {
        await page.click("#hint-btn");
        await page.waitForSelector("#hint-use", { timeout: 60000 });
        await page.click("#hint-use");
        hints++;
        if (await page.$("#commit-ok")) { if (!(await page.$eval("#commit-ok", (b) => b.disabled))) { await page.click("#commit-ok"); } }
        else if (await page.$("#clone-ok")) await page.click("#clone-ok");
        actions++;
        continue;
      }
      const kind = await page.evaluate(() => {
        if (document.querySelector("#commit-ok")) return "commit";
        if (document.querySelector("#clone-ok")) return "clone";
        if (document.querySelector("#map .sec.opt")) return "section";
        return "buttons";
      });
      kinds[kind] = (kinds[kind] || 0) + 1;
      if (kind === "commit") {
        // re-query after every click: each click re-renders the hand
        const ids = await page.$$eval("#houses .house.active .card[data-card]", (els) => els.map((e) => e.dataset.card));
        for (let k = 0; k < 6 && ids.length; k++) await page.click('#houses .card[data-card="' + pick(ids) + '"]');
        for (let k = 0; k < 8 && await page.$eval("#commit-ok", (b) => b.disabled); k++) {
          const sel = await page.$$eval("#houses .house.active .card.sel", (els) => els.map((e) => e.dataset.card));
          if (!sel.length) break;
          await page.click('#houses .card[data-card="' + pick(sel) + '"]');
        }
        const noms = await page.$$eval(".nomr", (els) => els.map((e) => e.value));
        if (noms.length && rnd() < 0.5) await page.check('.nomr[value="' + pick(noms) + '"]');
        const fx = await page.$$eval(".fx:not([disabled])", (els) => els.map((e) => e.value));
        if (fx.length && rnd() < 0.5) await page.check('.fx[value="' + pick(fx) + '"]');
        while (await page.$eval("#commit-ok", (b) => b.disabled)) {
          const sel = await page.$$eval("#houses .house.active .card.sel", (els) => els.map((e) => e.dataset.card));
          if (!sel.length) break;
          await page.click('#houses .card[data-card="' + sel[0] + '"]');
        }
        await page.click("#commit-ok");
      } else if (kind === "clone") {
        const ids = await page.$$eval("#houses .house.active .card[data-card]", (els) => els.map((e) => e.dataset.card));
        if (ids.length && rnd() < 0.7) await page.click('#houses .card[data-card="' + pick(ids) + '"]');
        await page.click("#clone-ok");
      } else if (kind === "section") {
        const opts = await page.$$eval("#map .sec.opt", (els) => els.map((e) => e.dataset.id));
        const btns = await page.$$eval("#prompt button[data-o]", (els) => els.map((e) => e.dataset.o));
        if (btns.length && (rnd() < 0.3 || !opts.length)) await page.click('#prompt button[data-o="' + pick(btns) + '"]');
        else await page.dispatchEvent('#map .sec.opt[data-id="' + pick(opts) + '"]', "click");
      } else {
        const btns = await page.$$eval("#prompt button[data-o]", (els) => els.map((e) => e.dataset.o));
        if (!btns.length) { errors.push("no options on prompt: " + html.slice(0, 200)); break; }
        await page.click('#prompt button[data-o="' + pick(btns) + '"]');
      }
      actions++;
    }
    if (result) {
      if (!(await page.$("#pt-save"))) errors.push("no end-of-game summary");
      else { await page.fill("#pt-notes", "automated playthrough"); await page.click("#pt-save"); }
      const saved = await page.evaluate(() => { try { return JSON.parse(localStorage.getItem("gs-playtests") || "[]").length; } catch { return -1; } });
      if (saved < 1) errors.push("playtest record not saved");
    }
    const status = await page.evaluate(() => document.querySelector("#status").innerText);
    const ok = result && !errors.length;
    if (!ok) failures++;
    console.log(`${ok ? "PASS" : "FAIL"} ${g.name}: ${result || "no result"} after ${actions} actions | ${status.slice(0, 90)}`);
    for (const e of errors.slice(0, 5)) console.log("   error:", e);
    await page.close();
  }
  console.log("decision screens seen:", JSON.stringify(kinds));
  console.log("decision kinds seen:", JSON.stringify(exactKinds));
  console.log(`hints followed: ${hints}, decisions undone: ${undos}`);
  await browser.close();
  process.exit(failures ? 1 : 0);
})();
