// V14 · "Cliente ligando..." — linha do tempo determinística: window.render(t), t em segundos.
// Cada versão define window.V antes deste arquivo (nome, segmento, mensagens).
const clamp=x=>Math.min(Math.max(x,0),1), ease=x=>1-Math.pow(1-clamp(x),3),
 back=x=>{x=clamp(x);const c=1.9;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)},
 inOut=x=>{x=clamp(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2},
 rnd=n=>{const s=Math.sin(n*127.1+311.7)*43758.5453;return s-Math.floor(s)};

// tempos (iguais aos do áudio em sfx.py)
const T={ring1:[0.15,1.35],ring2:[1.65,2.85],miss:3.0,stamp:3.45,words:4.3,beat:0.72,ring3:[9.45,10.25],
 shrink:10.3,typing1:10.45,reply1:10.95,hang:11.55,ans:12.2,typing2:12.65,reply2:13.25,end1:14.55,end2:15.55,logo:16.6,total:18.4};

const $=id=>document.getElementById(id);
function setup(){
 const V=window.V;
 document.querySelectorAll('[data-k]').forEach(e=>e.innerHTML=V[e.dataset.k]);
 $('words').innerHTML=V.words.map((w,i)=>`<div class="w" id="w${i}" style="font-size:${Math.min(300,Math.round(940/(w.length*0.43)))}px"><span class="ghost g1">${w}</span><span class="ghost g2">${w}</span><span class="main">${w}</span></div>`).join('');
 $('sym').innerHTML=logoSVG(4);
 // fatias da falha de imagem
 $('glitch').innerHTML=Array.from({length:14},(_,i)=>`<i style="top:${i*137}px"></i>`).join('');
}

function vib(t){ // tremida do celular durante o toque
 for(const [a,b] of [T.ring1,T.ring2,T.ring3]) if(t>=a&&t<b){const k=Math.sin((t-a)*Math.PI/(b-a));return Math.sin(t*95)*7*k;}
 return 0;
}

window.render=function(t){
 if(!window.__s){setup();window.__s=1;}
 const V=window.V, st=$('stage');
 let shake=vib(t), rot=0, scale=1;

 // ---------- cena A/B/D: tela de chamada ----------
 const callOn=t<T.words||(t>=T.ring3[0]-0.05&&t<T.shrink+0.4);
 const call=$('call'); call.style.display=callOn?'block':'none';
 if(callOn){
  // entrada da tela (zoom suave) e das ondas no avatar
  call.style.opacity=t<T.ring3[0]?Math.min(1,t/0.15):ease((t-T.ring3[0]+0.05)/0.2);
  document.querySelectorAll('.wave').forEach((e,j)=>{const ph=((t*0.85+j*0.33)%1);e.style.transform=`translate(-50%,-50%) scale(${1+ph*1.5})`;e.style.opacity=(1-ph)*0.55;});
  $('dots').textContent='.'.repeat(1+Math.floor(t*2.5)%3);
  $('shine').style.backgroundPosition=`${(-300+((t*420)%900))}px 0`;
  $('blob1').style.transform=`translate(${Math.sin(t*.7)*80}px,${Math.cos(t*.5)*60}px)`;
  $('blob2').style.transform=`translate(${Math.cos(t*.6)*90}px,${Math.sin(t*.8)*70}px)`;
  // notificação do WhatsApp parada (some no segundo toque)
  const n=$('notif'); const ni=ease((t-0.35)/0.35);
  n.style.display=t<T.ring3[0]?'flex':'none'; n.style.transform=`translateY(${(1-ni)*-260}px)`; n.style.opacity=ni;
  // chamada perdida
  const miss=t>=T.miss&&t<T.words;
  $('callmain').style.opacity=miss?0.18:1;
  $('missed').style.display=miss?'block':'none';
  if(miss){const k=back((t-T.miss)/0.3);$('missed').style.transform=`translate(-50%,-50%) scale(${0.7+0.3*k})`;}
  const s3=$('stamp3'); s3.style.display=t>=T.stamp&&t<T.words?'block':'none';
  if(t>=T.stamp){const p=ease((t-T.stamp)/0.22);s3.style.transform=`rotate(-8deg) scale(${2.4-1.4*p})`;s3.style.opacity=Math.min(1,(t-T.stamp)*6);
   if(t-T.stamp<0.25) shake+=(1-(t-T.stamp)/0.25)*18;}
  // segundo toque: a tela de chamada "minimiza" e vira uma pílula no topo
  if(t>=T.shrink){const p=inOut((t-T.shrink)/0.35); call.style.opacity=1-p; $('callmain').style.transform=`scale(${1-0.35*p}) translateY(${-p*200}px)`;}
  else {$('callmain').style.transform='none';}
 }
 const pill=$('pill'), pOn=t>=T.shrink&&t<T.hang+0.6; pill.style.display=pOn?'flex':'none';
 if(pOn){const hung=t>=T.hang; pill.classList.toggle('off',hung); $('pilltxt').innerHTML=hung?`${V.nome} desligou`:`${V.nome} ligando...`;
  const pin=back((t-T.shrink-0.1)/0.35), pout=ease((t-T.hang-0.25)/0.3);
  pill.style.opacity=Math.min(1,(t-T.shrink)*5)*(1-pout); pill.style.transform=`translateY(${(1-pin)*-120-pout*200}px) scale(${hung&&t<T.hang+0.12?1.05:1})`;
  if(hung&&t-T.hang<0.2) shake+=(1-(t-T.hang)/0.2)*10; }

 // ---------- falha de imagem ----------
 const gl=$('glitch'); const gOn=(t>=T.miss&&t<T.miss+0.32)||(t>=T.words-0.12&&t<T.words+0.08)||(t>=T.words+3*T.beat&&t<T.words+3*T.beat+0.14)||(t>=T.words+4*T.beat&&t<T.words+4*T.beat+0.14);
 gl.style.display=gOn?'block':'none';
 if(gOn){gl.querySelectorAll('i').forEach((e,j)=>{const r=rnd(j+Math.floor(t*30)*17);e.style.transform=`translateX(${(r-.5)*220}px)`;e.style.opacity=r>.62?.55:0;e.style.height=`${12+r*60}px`;
   e.style.background=r>.75?'rgba(255,40,90,.55)':r>.55?'rgba(0,212,170,.55)':'rgba(123,104,238,.5)';});
  st.style.filter=`hue-rotate(${(rnd(Math.floor(t*30))-.5)*80}deg) contrast(1.25)`; shake+=(rnd(Math.floor(t*60))-.5)*30;}
 else st.style.filter='none';

 // ---------- cena C: palavras no ritmo ----------
 const wOn=t>=T.words&&t<T.ring3[0]; $('kin').style.display=wOn?'block':'none';
 if(wOn){
  const i=Math.min(V.words.length-1,Math.floor((t-T.words)/T.beat)), lt=t-T.words-i*T.beat;
  const last=i===V.words.length-1;
  $('kin').className='kin bg'+(last?3:i%3);
  V.words.forEach((_,j)=>{$('w'+j).style.display=j===i?'block':'none';});
  const w=$('w'+i), pb=back(lt/0.28), p=ease(lt/0.2);
  const sc=last?1.0+0.06*ease((t-T.words-i*T.beat)/0.8):1;
  w.querySelector('.main').style.transform=`scale(${(1.7-0.7*pb)*sc})`;
  w.querySelector('.g1').style.transform=`translate(${(1-p)*-60-14}px,${(1-p)*20}px) scale(${1.9-0.9*p})`;
  w.querySelector('.g2').style.transform=`translate(${(1-p)*60+14}px,${(1-p)*-20}px) scale(${1.9-0.9*p})`;
  w.querySelectorAll('.ghost').forEach(g=>g.style.opacity=0.55*(1-p)+0.18);
  rot=(i%2?3:-3)*(1-ease(lt/0.4)); scale=1.06-0.06*ease(lt/0.3);
  $('flash').style.opacity=Math.max(0,0.45-lt*4);
  if(lt<0.12) shake+=(1-lt/0.12)*(last?22:10);
  $('wa').style.display=last?'flex':'none'; if(last){$('wa').style.transform=`translateX(-50%) scale(${back(lt/0.35)})`;}
  $('beatbar').style.width=`${((t-T.words)/(V.words.length*T.beat))*100}%`;
 } else $('flash').style.opacity=0;

 // ---------- cena D: conversa no WhatsApp ----------
 const chatOn=t>=T.shrink&&t<T.end1; $('chat').style.display=chatOn?'flex':'none';
 if(chatOn){
  $('chh').style.marginTop=`${290-170*inOut((t-T.hang-0.3)/0.45)}px`;
  const p=ease((t-T.shrink)/0.4); $('chat').style.transform=`scale(${0.92+0.08*p})`; $('chat').style.opacity=p;
  const show=(id,a,anim)=>{const e=$(id);if(t<a){e.style.display='none';return;}e.style.display='';const k=back((t-a)/0.3);e.style.transform=anim==='r'?`scale(${0.6+0.4*k}) `:`scale(${0.6+0.4*k})`;e.style.opacity=Math.min(1,(t-a)*6);};
  show('m0',T.shrink);
  $('ty1').style.display=t>=T.typing1&&t<T.reply1?'flex':'none';
  show('m1',T.reply1,'r'); show('m2',T.ans);
  $('ty2').style.display=t>=T.typing2&&t<T.reply2?'flex':'none';
  show('m3',T.reply2,'r');
  document.querySelectorAll('.typing i').forEach((e,j)=>e.style.transform=`translateY(${Math.sin(t*14-j*0.9)*7}px)`);
  $('iabadge').style.opacity=ease((t-T.typing1)/0.3);
  if(t>=T.reply2){const k=ease((t-T.reply2)/0.5);$('m3').style.boxShadow=`0 0 ${60*k}px rgba(0,212,170,${0.6*(1-ease((t-T.reply2-0.4)/0.8))})`;}
  // varredura de luz quando confirma
  const sw=(t-T.reply2)/0.6; $('sweep').style.display=sw>0&&sw<1?'block':'none'; $('sweep').style.transform=`translateX(${-1200+sw*2600}px) rotate(18deg)`;
  if(t>=T.end1-0.3){const q=ease((t-T.end1+0.3)/0.3);$('chat').style.filter=`blur(${q*18}px)`;$('chat').style.opacity=1-q;}else $('chat').style.filter='none';
 }

 // ---------- cena E: fecho digitado + marca ----------
 const endOn=t>=T.end1-0.05; $('fin').style.display=endOn?'block':'none';
 if(endOn){
  const type=(id,txt,a,cps)=>{const n=Math.max(0,Math.min(txt.length,Math.floor((t-a)*cps)));$(id).innerHTML=txt.slice(0,n)+(t>=a&&(n<txt.length||(id==='l2'&&t<T.logo))&&Math.floor(t*3)%2===0?'<b class="cur">|</b>':'');};
  type('l1',V.fim1,T.end1,22); type('l2',V.fim2,T.end2,22);
  const lk=back((t-T.logo)/0.45); $('brand').style.opacity=clamp((t-T.logo)*4); $('brand').style.transform=`translateX(-50%) scale(${0.7+0.3*lk})`;
  $('sym').style.filter=`drop-shadow(0 0 ${20+18*Math.sin(t*5)}px rgba(0,212,170,.55))`;
  $('l12').style.transform=`translateY(${-ease((t-T.logo)/0.5)*120}px)`;
 }

 st.style.transform=`translate(${shake}px,${shake*0.4}px) rotate(${rot}deg) scale(${scale})`;
};
