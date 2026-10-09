// uso: node reel-render.js arquivo.html segundos saida.mp4
const {chromium}=require('playwright'),fs=require('fs'),path=require('path'),{execSync}=require('child_process');
(async()=>{
 const [f,dur,out,capa]=process.argv.slice(2), fps=30, dir=fs.mkdtempSync('/tmp/claude-0/-home-user-test/83659f5d-752c-53ab-985c-20c71f1c8e89/scratchpad/frames-');
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+path.resolve(f)); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(300);
 const n=Math.round(+dur*fps);
 for(let i=0;i<n;i++){ await p.evaluate(t=>window.render(t),i/fps); await p.screenshot({path:`${dir}/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:92}); }
 await b.close();
 execSync(`ffmpeg -loglevel error -y -framerate ${fps} -i ${dir}/f%04d.jpg -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart ${out}`);
 // capa = quadro escolhido
 fs.copyFileSync(`${dir}/f${String(Math.round((capa?+capa:dur*0.08)*fps)).padStart(4,'0')}.jpg`, out.replace('.mp4','-capa.jpg'));
 fs.rmSync(dir,{recursive:true});
})();
