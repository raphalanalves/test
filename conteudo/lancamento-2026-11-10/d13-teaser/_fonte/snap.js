// uso: node snap.js pagina.html saida.png t1 t2 ...  (folha de contato)
const {chromium}=require('playwright'),path=require('path'),{execSync}=require('child_process');
(async()=>{const [f,out,...ts]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
 p.on('pageerror',e=>console.log('ERR',e.message));
 await p.goto('file://'+path.resolve(f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
 const fs=[];for(const t of ts){await p.evaluate(t=>window.render(t),+t);const n=`/tmp/claude-0/-home-user/83659f5d-752c-53ab-985c-20c71f1c8e89/scratchpad/snap_${t}.png`;await p.screenshot({path:n});fs.push(n);}
 await b.close();execSync(`ffmpeg -loglevel error -y ${fs.map(x=>'-i '+x).join(' ')} -filter_complex "${fs.map((_,i)=>`[${i}]scale=270:-1[s${i}]`).join(';')};${fs.map((_,i)=>`[s${i}]`).join('')}hstack=${fs.length}" ${out}`);})();
