// Símbolo provisório (triângulo com nós dentro do círculo). Trocar pelo arquivo oficial de malvora-core/docs/marca.
function logoSVG(stage=4,color='#459A76',sw=6){
  const P=[[50,14],[86,76],[14,76]];
  let s='';
  if(stage>=4) s+=`<circle cx="50" cy="50" r="46" fill="none" stroke="${color}" stroke-width="${sw*.6}"/>`;
  if(stage>=1) s+=`<polygon points="${P.map(p=>p.join(',')).join(' ')}" fill="none" stroke="${color}" stroke-width="${sw}" stroke-linejoin="round"/>`;
  if(stage>=2) s+=`<line x1="50" y1="14" x2="50" y2="76" stroke="${color}" stroke-width="${sw*.6}"/><line x1="32" y1="45" x2="68" y2="45" stroke="${color}" stroke-width="${sw*.6}"/>`;
  if(stage>=3) s+=[[50,14],[86,76],[14,76],[50,45],[50,76]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="${sw*1.1}" fill="${color}"/>`).join('');
  return `<svg viewBox="0 0 100 100">${s}</svg>`;
}
function logoFull(){return `<div class="logo">${logoSVG(4)}<span>MALVORA</span></div>`}
