import json
J=json.dumps
TAB={"__rl":True,"mode":"id","value":"0YwsOMv2xxHGCRBL","cachedResultName":"lista_vip_lancamento"}
EVO={"evolutionApi":{"id":"DgVs0waBspX3tug8","name":"Evolution Malvora"}}
def E(s): return f"expr({J(s)})"
def cond(left): return '{ options: { caseSensitive: true, leftValue: "", typeValidation: "loose" }, conditions: [{ leftValue: '+E(left)+', operator: { type: "boolean", operation: "true", singleValue: true } }], combinator: "and" }'
def resp(var,name,body,code=None):
    opts='{ responseHeaders: { entries: [{ name: "Access-Control-Allow-Origin", value: "https://bio.malvora.com.br" }] }'+(f', responseCode: {code}' if code else '')+' }'
    return f"const {var} = node({{ type: 'n8n-nodes-base.respondToWebhook', version: 1.5, config: {{ name: {J(name)}, parameters: {{ respondWith: 'json', responseBody: {body}, options: {opts} }} }} }});\n"
def ler(var,name): return f"const {var} = node({{ type: 'n8n-nodes-base.dataTable', version: 1.1, config: {{ name: {J(name)}, alwaysOutputData: true, executeOnce: true, parameters: {{ resource: 'row', operation: 'get', dataTableId: {J(TAB)}, returnAll: true }} }} }});\n"
C='$("Contar vagas").first().json'
assign=[("instancia","PREENCHER_INSTANCIA_MALVORA",None,"string"),("alerta","PREENCHER_WHATSAPP_RAPHAEL",None,"string"),("vagas",10,None,"number"),
 ("nome",None,'{{ String($json.body.nome || "").trim().slice(0,80) }}',"string"),
 ("empresa",None,'{{ String($json.body.empresa || "").trim().slice(0,80) }}',"string"),
 ("whatsapp",None,'{{ (function(){ var n=String($json.body.whatsapp||"").replace(/\\D/g,""); if(n.length<=11) n="55"+n; return n; })() }}',"string"),
 ("segmento",None,'{{ String($json.body.segmento || "").slice(0,60) }}',"string"),
 ("origem",None,'{{ String($json.body.origem || "").slice(0,120) }}',"string")]
a=",\n".join("{ id: %s, name: %s, value: %s, type: %s }"%(J('c%d'%i),J(n),E(e) if e else J(v),J(t)) for i,(n,v,e,t) in enumerate(assign))
schema=[{"id":k,"displayName":k,"type":"number" if k=="posicao" else "string","display":True,"required":False,"defaultMatch":False} for k in ["nome","empresa","whatsapp","segmento","origem","posicao","status"]]
vals="{ "+", ".join(f"{k}: {E('{{ $json.'+k+' }}')}" for k in ["nome","empresa","whatsapp","segmento","origem","posicao"])+", status: 'confirmado' }"
welcome='{{ "Oi, " + '+C+'.nome.split(" ")[0] + "! Aqui é da Malvora 💚💜\\n\\nSua vaga na lista VIP está garantida: a " + '+C+'.empresa + " é a empresa nº " + '+C+'.posicao + " de 10.\\n\\nO que vem agora:\\n• 09/11, à noite: você recebe aqui o acesso antecipado, antes do lançamento.\\n• 50% de desconto nos 3 primeiros meses da assinatura.\\n\\nQualquer dúvida, é só responder esta mensagem. Até lá!" }}'
alert='{{ "🔔 Nova empresa na lista VIP (" + '+C+'.posicao + "/10)\\n\\n" + '+C+'.nome + " · " + '+C+'.empresa + "\\n" + '+C+'.segmento + "\\nWhatsApp: +" + '+C+'.whatsapp + "\\nVagas restantes: " + '+C+'.restantes }}'
def evo(var,name,jid,text):
    return f"const {var} = node({{ type: 'n8n-nodes-evolution-api.evolutionApi', version: 1, config: {{ name: {J(name)}, credentials: {J(EVO)}, onError: 'continueRegularOutput', parameters: {{ resource: 'messages-api', operation: 'send-text', instanceName: {E('{{ '+C+'.instancia }}')}, remoteJid: {E(jid)}, messageText: {E(text)} }} }} }});\n"
code="import { workflow, node, trigger, ifElse, expr } from '@n8n/workflow-sdk';\n\n"
code+="const recebe = trigger({ type: 'n8n-nodes-base.webhook', version: 2.1, config: { name: 'Cadastro na lista VIP', parameters: { httpMethod: 'POST', path: 'lista-vip', responseMode: 'responseNode', options: { allowedOrigins: 'https://bio.malvora.com.br', ignoreBots: true } } } });\n"
code+="const config = node({ type: 'n8n-nodes-base.set', version: 3.4, config: { name: 'Configuração', parameters: { mode: 'manual', includeOtherFields: false, assignments: { assignments: [\n"+a+"\n] } } } });\n"
code+="const valido = ifElse({ version: 2.2, config: { name: 'Dados válidos?', parameters: { conditions: "+cond('{{ $json.nome.length > 1 && $json.empresa.length > 1 && $json.whatsapp.length >= 12 && $json.whatsapp.length <= 13 }}')+" } } });\n"
code+=ler("lerLista","Ler lista")
code+="const avaliar = node({ type: 'n8n-nodes-base.code', version: 2, config: { name: 'Contar vagas', parameters: { mode: 'runOnceForAllItems', jsCode: "+J("""const c = $('Configuração').first().json;
const linhas = $input.all().map(i => i.json).filter(r => r && r.whatsapp);
const ja = linhas.find(r => r.whatsapp === c.whatsapp);
const usadas = linhas.length;
return [{ json: { ...c, ja: !!ja, cheio: !ja && usadas >= c.vagas, posicao: ja ? ja.posicao : usadas + 1, restantes: Math.max(0, c.vagas - usadas - (ja ? 0 : 1)) } }];""")+" } } });\n"
code+="const cheio = ifElse({ version: 2.2, config: { name: 'Vagas esgotadas?', parameters: { conditions: "+cond('{{ $json.cheio }}')+" } } });\n"
code+="const repetido = ifElse({ version: 2.2, config: { name: 'Já cadastrado?', parameters: { conditions: "+cond('{{ $json.ja }}')+" } } });\n"
code+=f"const gravar = node({{ type: 'n8n-nodes-base.dataTable', version: 1.1, config: {{ name: 'Gravar na lista', parameters: {{ resource: 'row', operation: 'insert', dataTableId: {J(TAB)}, columns: {{ mappingMode: 'defineBelow', value: {vals}, matchingColumns: [], schema: {J(schema)} }} }} }} }});\n"
code+=resp("okResp","Responder vaga garantida",E('{{ JSON.stringify({ ok: true, restantes: '+C+'.restantes }) }}'))
code+=evo("boasVindas","Boas-vindas ao cliente",'{{ '+C+'.whatsapp }}',welcome)
code+=evo("alerta","Avisar o Raphael",'{{ '+C+'.alerta }}',alert)
code+=resp("cheioResp","Responder esgotado",J('{"cheio": true, "restantes": 0}'))
code+=resp("jaResp","Responder já cadastrado",E('{{ JSON.stringify({ ok: true, ja: true, restantes: $json.restantes }) }}'))
code+=resp("invalidoResp","Responder dados inválidos",J('{"ok": false, "erro": "dados_invalidos"}'),400)
code+="const consulta = trigger({ type: 'n8n-nodes-base.webhook', version: 2.1, config: { name: 'Consulta de vagas', parameters: { httpMethod: 'GET', path: 'lista-vip', responseMode: 'responseNode', options: { allowedOrigins: 'https://bio.malvora.com.br' } } } });\n"
code+=ler("lerLista2","Ler lista (consulta)")
code+="const contar2 = node({ type: 'n8n-nodes-base.code', version: 2, config: { name: 'Calcular restantes', parameters: { mode: 'runOnceForAllItems', jsCode: "+J("const n = $input.all().map(i => i.json).filter(r => r && r.whatsapp).length;\nreturn [{ json: { restantes: Math.max(0, 10 - n) } }];")+" } } });\n"
code+=resp("vagasResp","Responder vagas",E('{{ JSON.stringify({ restantes: $json.restantes }) }}'))
code+="""
export default workflow('lista-vip', 'Lançamento - Lista VIP (10 vagas)')
  .add(recebe).to(config).to(valido
    .onTrue(lerLista.to(avaliar).to(cheio
      .onTrue(cheioResp)
      .onFalse(repetido
        .onTrue(jaResp)
        .onFalse(gravar.to(okResp).to(boasVindas).to(alerta)))))
    .onFalse(invalidoResp))
  .add(consulta).to(lerLista2).to(contar2).to(vagasResp);
"""
open('lista-vip.js','w').write(code)
