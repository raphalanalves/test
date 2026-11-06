// uso: node render.js arquivo.html largura altura nSlides prefixo_saida
const {chromium}=require('playwright');
(async()=>{
 const [f,w,h,n,out]=process.argv.slice(2);
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:+w*+n,height:+h}});
 await p.goto('file://'+require('path').resolve(f)); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(400);
 for(let i=0;i<+n;i++) await p.screenshot({path:`${out}-${String(i+1).padStart(2,'0')}.png`,clip:{x:i*+w,y:0,width:+w,height:+h}});
 await b.close();
})();
