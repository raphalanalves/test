const { chromium } = require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.join(__dirname,'stories.html'));await p.waitForTimeout(2500);
const n={e1:'enquete-1',e2:'enquete-2',e3:'enquete-3',c1:'caixinha-1',c2:'caixinha-2'};
for(const id in n){await (await p.$('#'+id)).screenshot({path:path.join(__dirname,'..',n[id]+'.jpg'),type:'jpeg',quality:92})}
await b.close()})();
