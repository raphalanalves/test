const { chromium } = require('playwright');const path=require('path');const C=require('./capas.json');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.join(__dirname,'capas.html'));await p.waitForTimeout(2500);
for(let i=0;i<C.length;i++){await (await p.$('#c'+i)).screenshot({path:path.join(__dirname,'..',`capa-${C[i][0]}-${C[i][1]}.jpg`),type:'jpeg',quality:92})}
await b.close()})();
