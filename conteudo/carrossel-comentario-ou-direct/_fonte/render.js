const { chromium } = require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.join(__dirname,'carrossel.html'));await p.waitForTimeout(2500);
for(const i of [1,2,3,4,5,6]){await (await p.$('#c'+i)).screenshot({path:path.join(__dirname,'..',`carrossel-${i}.jpg`),type:'jpeg',quality:92})}
await b.close()})();
