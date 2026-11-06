// Render the print-and-play PDFs from print.html and rulebook.html (Playwright's Chromium).
// Serve the generation-ship folder first:  python3 -m http.server 8765
//   node tools/build_pdfs.cjs [port]
// Writes print/:
//   stewards-print-and-play.pdf   everything, ink saver, backs pages at the end (one-sided printing)
//   stewards-cards-duplex.pdf     just the card decks, a backs page after each fronts page (double-sided)
//   stewards-boards-a4-100.pdf    ship boards at true scale, each as two A4 halves to tape together
//   stewards-rulebook.pdf
const { chromium } = require("playwright");
const port = process.argv[2] || 8765;
const JOBS = [
  ["print.html", "stewards-print-and-play.pdf"],
  ["print.html#duplex,cardsonly", "stewards-cards-duplex.pdf"],
  ["print.html#halves,boardsonly", "stewards-boards-a4-100.pdf"],
  ["rulebook.html", "stewards-rulebook.pdf"],
];
(async () => {
  const b = await chromium.launch();
  for (const [url, out] of JOBS) {
    const p = await b.newPage();
    const errs = [];
    p.on("pageerror", (e) => errs.push(e.message));
    await p.goto(`http://localhost:${port}/${url}`);
    if (url.startsWith("print")) await p.waitForSelector("body[data-ready]", { timeout: 120000 });
    await p.evaluate(async () => {
      await document.fonts.ready;
      await Promise.all([...document.images].map((i) => (i.complete ? 0 : new Promise((r) => { i.onload = i.onerror = r; }))));
    });
    await p.waitForTimeout(3000);
    await p.emulateMedia({ media: "print" });
    await p.pdf({ path: `print/${out}`, printBackground: true, preferCSSPageSize: true });
    console.log(out, errs.length ? errs : "ok");
    await p.close();
  }
  await b.close();
})();
