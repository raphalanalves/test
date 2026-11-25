const { chromium } = require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.join(__dirname,'stories.html'));await p.waitForTimeout(2500);
for(const i of [1,2,3,4,5]){await (await p.$('#st'+i)).screenshot({path:path.join(__dirname,'..',`duvidas-${i}.png`)})}
await b.close()})();
