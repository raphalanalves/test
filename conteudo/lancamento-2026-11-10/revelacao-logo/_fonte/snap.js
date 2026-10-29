const {chromium}=require('playwright'),path=require('path');(async()=>{const b=await chromium.launch(),p=await b.newPage({viewport:{width:1080,height:1920}});p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file://'+path.resolve('video.html'));await p.evaluate(()=>document.fonts.ready);
for(const t of process.argv.slice(2)){await p.evaluate(t=>render(t),+t);await p.screenshot({path:`${process.env.S}/s${t}.jpg`,type:'jpeg',quality:70});}await b.close();})();
