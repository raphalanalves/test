const fs=require('fs');
const rows=JSON.parse(fs.readFileSync('rows.json'));
const now=new Date().toISOString();
const C=(id,text)=>({id,text,timestamp:now,from:{username:'cliente'+id}});
const coments=[C('c1','amei'),C('c2','obrigado!'),C('c3','não gostei'),C('c4','eu ia comprar isso'),C('c5','IA'),C('c6','😢'),C('c7','😂😢'),C('c8','isso é golpe'),C('c9','Não vejo a hora!'),C('c10','caro demais?'),C('c11','top demais'),C('c12','👏👏'),C('c13','aceso'),C('c14','como funciona pra clinica?'),C('c15','cara, que top'),C('c16','quero entrar na lista vip'),C('c17','esperando resposta de vocês')];
const D=(id,uid,message,att)=>({id:'cv'+id,messages:{data:[{id,from:{id:uid,username:'dm'+uid},message,created_time:now,attachments:att}]}});
const dms=[D('d1','u1',''),D('d2','u2',''),D('d3','u3',''),D('d4','u4','🔥'),D('d5','u5','quanto custa?'),D('d6','u6','',{data:[{type:'sticker'}]}),D('d7','u7','me conta o que vocês fazem')];
const hist=[{usuario:'dmu2',tipo:'direct_midia',status:'respondido',createdAt:now,item_id:'x1'},{usuario:'dmu3',tipo:'direct_midia',status:'respondido',createdAt:now,item_id:'x2'},{usuario:'dmu3',tipo:'direct_midia',status:'respondido',createdAt:now,item_id:'x3'}];
const nodes={'Configuração':[{json:{modo_teste:true,ig_id:'IG',minha_conta:'malvora_hub',alerta:'x',instancia:'y',modelo_ia:'m',prompt_ia:'P {{FASE}}',fase_antes:'A',fase_depois:'B'}}],'Ler respostas':rows.map(j=>({json:j})),'Ler histórico':hist.map(j=>({json:j})),'Buscar comentários':[{json:{data:[{comments:{data:coments}}]}}],'Buscar direct':[{json:{data:dms}}]};
const $=n=>({first:()=>nodes[n][0],all:()=>nodes[n]});
const code=fs.readFileSync('decidir.js','utf8');
const out=new Function('$',code)($);
for(const o of out){const j=o.json;console.log((j.usuario+' '+j.texto).padEnd(42),'|',j.acao.padEnd(11),'|',(j.resposta_publica||j.resposta_direct||j.aviso||'').split('\n')[0].slice(0,70));}
