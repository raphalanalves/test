const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'stories.html')); await p.waitForTimeout(1500);
  for (const id of ['st1', 'st2', 'st3']) { const el = await p.$('#' + id); await el.screenshot({ path: path.join(__dirname, '..', `bf-story-${id.slice(2)}.png`) }); }
  await b.close();
})();
