// Linha do tempo determinística: render(t) posiciona tudo para o instante t (segundos).
const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
window.render=function(t){
 document.querySelectorAll('.scene').forEach(s=>{const a=+s.dataset.from,b=+s.dataset.to; s.style.display=(t>=a&&t<b)?'block':'none';
   const k=Math.min(ease((t-a)/.3),ease((b-t)/.3)); s.style.opacity=k;});
 document.querySelectorAll('[data-in]').forEach(e=>{
   const i=+e.dataset.in, o=e.dataset.out?+e.dataset.out:1e9, anim=e.dataset.anim||'up';
   if(t<i||t>=o){ if(e.dataset.keep!=='1'||t<i){e.style.display='none';} else {e.style.display='';} return;}
   e.style.display='';
   const p=ease((t-i)/.35);
   const tr={up:`translateY(${(1-p)*40}px)`,drop:`translateY(${(1-p)*-260}px)`,pop:`scale(${.85+.15*p})`,fade:'none',zoom:`scale(${1.15-.15*p})`}[anim];
   e.style.opacity=p; e.style.transform=tr;
 });
 document.querySelectorAll('.typing i').forEach((d,j)=>d.style.opacity=.35+.65*Math.max(0,Math.sin(t*9-j*.9)));
 document.querySelectorAll('[data-blink]').forEach(e=>e.style.opacity=(Math.floor(t*2)%2)?.25:1);
 document.querySelectorAll('[data-pulse]').forEach(e=>e.style.boxShadow=`0 0 ${30+25*Math.sin(t*5)}px rgba(69,154,118,.6)`);
 if(window.extra) window.extra(t);
};
