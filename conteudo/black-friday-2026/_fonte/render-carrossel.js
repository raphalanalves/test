// Renderiza os slides do carrossel (1080x1350) a partir de carrossel.html.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(__dirname, 'carrossel.html')); await p.waitForTimeout(1500);
  const ids = await p.$$eval('section.s', (s) => s.map((e) => e.id));
  for (const [i, id] of ids.entries()) { const el = await p.$('#' + id); await el.screenshot({ path: path.join(__dirname, '..', `bf-carrossel-${i + 1}.png`) }); }
  await b.close(); console.log(ids.length, 'slides');
})();
