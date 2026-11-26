const { chromium } = require('playwright');const path=require('path');const fs=require('fs');
(async()=>{const dir=path.join(__dirname,'frames');fs.rmSync(dir,{recursive:true,force:true});fs.mkdirSync(dir);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.join(__dirname,'reel.html'));await p.waitForTimeout(2500);
const fps=30,N=Math.round(22.8*fps);for(let i=0;i<N;i++){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:path.join(dir,String(i).padStart(4,'0')+'.jpg'),type:'jpeg',quality:90})}
await b.close()})();
