// uso: node render-mosaico.js arquivo.html saida.png largura
const {chromium}=require('playwright');
(async()=>{const [f,o,w]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:+w,height:1350}});
await p.goto('file://'+require('path').resolve(f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
await p.screenshot({path:o});await b.close();})();
