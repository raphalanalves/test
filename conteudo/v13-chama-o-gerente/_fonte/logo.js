// Marca oficial Malvora (geometria do SVG do portal: malvora-core/portal/malvora_portal/templates/_marca.html)
// stage 1: nós | 2: + triângulo | 3: + núcleo (V e ponto central) | 4: + arco (símbolo completo)
let __g=0;
function logoSVG(stage=4){
  const id='mg'+(__g++);
  let s=`<defs><linearGradient id="${id}" x1="18" y1="10" x2="49" y2="53" gradientUnits="userSpaceOnUse"><stop stop-color="#00D4AA"/><stop offset="1" stop-color="#7B68EE"/></linearGradient>
  <filter id="${id}f" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="1.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><g filter="url(#${id}f)">`;
  if(stage>=4) s+=`<path d="M49.5 21.5A24 24 0 1 0 51 43" fill="none" stroke="#00D4AA" stroke-linecap="round" stroke-width="1.6" opacity=".6"/>`;
  if(stage>=2) s+=`<path d="M32 11 11 50h42L32 11Z" fill="none" stroke="url(#${id})" stroke-linejoin="round" stroke-width="2.4"/>`;
  if(stage>=3) s+=`<path d="M24.5 30.5 32 38.5 39.5 30.5" fill="none" stroke="#7B68EE" stroke-width="1.1" opacity=".9"/><circle cx="32" cy="38.5" r="1.6" fill="#7B68EE"/>`;
  s+=`<g fill="#0E0E16" stroke-width="2.2"><circle cx="32" cy="11" r="4.2" stroke="#00D4AA"/><circle cx="11" cy="50" r="4.2" stroke="#00D4AA"/><circle cx="53" cy="50" r="4.2" stroke="#00D4AA"/></g>
  <circle cx="32" cy="11" r="1.6" fill="#00D4AA"/><circle cx="11" cy="50" r="1.6" fill="#00D4AA"/><circle cx="53" cy="50" r="1.6" fill="#00D4AA"/></g>`;
  return `<svg viewBox="0 0 64 64">${s}</svg>`;
}
function logoFull(){return `<img class="logo-img" src="marca/logo-horizontal-compacto-crop.png" alt="Malvora">`}
function symImg(px){return `<img class="sym-img" src="marca/simbolo-triangulo-crop.png" style="width:${px}px">`}
