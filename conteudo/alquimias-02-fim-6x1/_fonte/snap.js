// uso: node snap.js arquivo.html saida.png t1 t2 ...  (folha de contato em 1/3 do tamanho)
const {chromium}=require('playwright');(async()=>{const [f,out,...ts]=process.argv.slice(2);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+require('path').resolve(f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const fs=require('fs');const shots=[];for(const t of ts){await p.evaluate(x=>window.render(x),+t);shots.push(await p.screenshot({type:'jpeg',quality:80}));}
const dir=fs.mkdtempSync('/tmp/claude-0/-home-user/83659f5d-752c-53ab-985c-20c71f1c8e89/scratchpad/snap-');shots.forEach((s,i)=>fs.writeFileSync(`${dir}/${i}.jpg`,s));
await b.close();require('child_process').execSync(`ffmpeg -loglevel error -y ${ts.map((_,i)=>`-i ${dir}/${i}.jpg`).join(' ')} -filter_complex "${ts.map((_,i)=>`[${i}]scale=360:-1[v${i}];`).join('')}${ts.map((_,i)=>`[v${i}]`).join('')}hstack=${ts.length}" ${out}`);})();
