// Linha do tempo determinística (v2): animações por palavra, legenda dinâmica, câmera e tremida.
const clamp=x=>Math.min(Math.max(x,0),1), ease=x=>1-Math.pow(1-clamp(x),3), back=x=>{x=clamp(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
window.render=function(t){
 let cam=1,shake=0;
 document.querySelectorAll('.scene').forEach(s=>{const a=+s.dataset.from,b=+s.dataset.to,on=t>=a&&t<b;s.style.display=on?'block':'none';
  if(on){const k=Math.min(ease((t-a)/.25),ease((b-t)/.25));s.style.opacity=k;const z=1+0.035*clamp((t-a)/(b-a));s.style.transform=`scale(${z})`;}});
 document.querySelectorAll('[data-in]').forEach(e=>{
  const i=+e.dataset.in,o=e.dataset.out?+e.dataset.out:1e9,an=e.dataset.anim||'up';
  if(t<i||t>=o){e.style.display='none';return;} e.style.display='';
  const raw=(t-i)/.32,p=ease(raw),pb=back(raw);
  const tr={up:`translateY(${(1-p)*60}px)`,drop:`translateY(${(1-p)*-200}px)`,pop:`scale(${.6+.4*pb})`,fade:'none',
   slide:`translateX(${(1-p)*260}px)`,slideL:`translateX(${(1-p)*-260}px)`,
   stamp:`scale(${2.2-1.2*p}) rotate(${-14+4*p}deg)`,zoom:`scale(${1.25-.25*p})`,grow:`scaleY(${p})`}[an];
  e.style.opacity=an==='stamp'?Math.min(1,raw*2):p; e.style.transform=tr+(e.dataset.rot?` rotate(${e.dataset.rot}deg)`:'');
  if(e.dataset.shake&&t-i<.25) shake=Math.max(shake,(1-(t-i)/.25)*14);
 });
 document.querySelectorAll('[data-count]').forEach(e=>{const[a,b,v0,v1]=e.dataset.count.split(',').map(Number);e.textContent=e.dataset.pre+Math.round(v0+(v1-v0)*ease((t-a)/(b-a))).toLocaleString('pt-BR')+(e.dataset.pos||'')});
 document.querySelectorAll('[data-pulse]').forEach(e=>e.style.boxShadow=`0 0 ${30+28*Math.sin(t*6)}px rgba(0,212,170,.65)`);
 document.querySelectorAll('[data-ring]').forEach((e,j)=>{const ph=((t*0.9+j*0.33)%1);e.style.transform=`translate(-50%,-50%) scale(${.4+ph*1.6})`;e.style.opacity=1-ph;});
 const st=document.getElementById('stage');
 st.style.transform=shake?`translate(${Math.sin(t*90)*shake}px,${Math.cos(t*77)*shake*.6}px)`:'none';
 // legenda dinâmica
 const C=window.CAP||[];let cur=null;for(const c of C){if(t>=c.a&&t<c.b){cur=c;break;}}
 const cap=document.getElementById('cap');
 if(!cur){cap.style.opacity=0;return;} cap.style.opacity=1;
 cap.innerHTML=cur.w.map(w=>`<span class="${t>=w.t?'on':''}${t>=w.t&&t<w.t+w.d+.05?' now':''}">${w.w}</span>`).join(' ');
 const k=ease((t-cur.a)/.12);cap.style.transform=`translateX(-50%) scale(${.92+.08*k})`;
};
