"""Gera alquimias-02.html, tempos.json e efeitos.json a partir da narração (tempos por palavra)."""
import json

segs = json.load(open('../narracao.json'))
GAP, t0 = 0.22, 0.3
T, t = {}, t0
for s in segs:
    T[s['id']] = (t, t + s['dur'])
    t += s['dur'] + GAP
END = t + 1.2
P = {s['id']: s['palavras'] for s in segs}


def W(sid, palavra, n=1):
    """Tempo absoluto da n-ésima ocorrência de uma palavra na cena."""
    k = 0
    for w in P[sid]:
        if w['w'].lower().startswith(palavra.lower()):
            k += 1
            if k == n:
                return round(T[sid][0] + w['t'], 2)
    raise KeyError(f'{sid}:{palavra}')


def sc(sid, last=False):
    a, b = T[sid]
    nxt = END if last else b + GAP
    return f'data-from="{round(a - (0.15 if sid != "s1" else 0.3), 2)}" data-to="{round(nxt, 2)}"'


# legenda: blocos de até 4 palavras, quebrando em pausas
CAP = []
for s in segs:
    a0 = T[s['id']][0]
    bloco = []
    for i, w in enumerate(s['palavras']):
        wa = {'w': w['w'], 't': round(a0 + w['t'], 2), 'd': round(w['d'], 2)}
        if bloco and (len(bloco) >= 4 or wa['t'] - (bloco[-1]['t'] + bloco[-1]['d']) > 0.3):
            CAP.append(bloco)
            bloco = []
        bloco.append(wa)
    if bloco:
        CAP.append(bloco)
caps = []
for i, b in enumerate(CAP):
    fim = CAP[i + 1][0]['t'] if i + 1 < len(CAP) and CAP[i + 1][0]['t'] - (b[-1]['t'] + b[-1]['d']) < 0.6 else b[-1]['t'] + b[-1]['d'] + 0.25
    caps.append({'a': b[0]['t'], 'b': round(fim, 2), 'w': b})

DIAS = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB', 'DOM']


def semana(classes, extra='', top=560):
    tiles = ''.join(f'<div class="dia {classes.get(d, "")}">{d}{extra if d in classes and "x" in classes[d] else ""}</div>' for d in DIAS)
    return f'<div class="semana" style="top:{top}px">{tiles}</div>'


EF = []  # efeitos sonoros: (tempo, tipo)

def fx(tempo, tipo):
    EF.append([round(tempo, 2), tipo])
    return tempo


for sid in T:
    if sid != 's1':
        fx(T[sid][0] - 0.12, 'whoosh')

s1, s2, s3, s4, s5, s6, s7, s8 = (T[k] for k in ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8'])

html = f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><link rel="stylesheet" href="reel.css"><script src="logo.js"></script><script src="engine2.js"></script>
<style>
#stage{{position:absolute;inset:0}}
.scene{{transform-origin:50% 40%}}
.tag{{position:absolute;top:70px;left:60px;font-family:'Bebas Neue';font-size:34px;letter-spacing:5px;color:var(--g);z-index:9}}
.tag span{{color:var(--mut)}}
.semana{{position:absolute;left:50px;right:50px;display:grid;grid-template-columns:repeat(7,1fr);gap:12px}}
.dia{{height:300px;border-radius:22px;background:#1C1D29;border:2px solid #2A2B3A;display:flex;align-items:flex-end;justify-content:center;padding-bottom:22px;font-family:'Bebas Neue';font-size:44px;color:#C9CCD3;position:relative}}
.dia.on{{background:linear-gradient(180deg,#26283A,#1C1D29);color:#fff}}
.dia.hot{{border-color:var(--red);color:#fff;background:linear-gradient(180deg,rgba(229,72,77,.35),#1C1D29)}}
.dia.rest{{border-color:var(--g);color:#fff;background:linear-gradient(180deg,rgba(0,212,170,.35),#14202A)}}
.dia.ia{{border-color:var(--t2);color:#fff;background:linear-gradient(180deg,rgba(123,104,238,.45),#16162A)}}
.dia.full{{border-color:var(--g);background:repeating-linear-gradient(180deg,rgba(0,212,170,.55) 0 22px,transparent 22px 34px),#14202A;color:#fff}}
.dia small{{position:absolute;top:18px;left:0;right:0;text-align:center;font-family:Inter;font-size:19px;font-weight:700;letter-spacing:1px}}
.stamp{{position:absolute;border:7px solid var(--red);color:var(--red);font-family:'Bebas Neue';letter-spacing:6px;border-radius:14px;padding:0 26px;background:rgba(14,14,22,.75)}}
.big{{position:absolute;left:60px;right:60px;text-align:center}}
.chip{{display:inline-block;padding:16px 30px;border-radius:999px;border:3px solid var(--g);font-family:'Bebas Neue';font-size:58px;letter-spacing:2px;color:#fff;background:rgba(0,212,170,.10)}}
.seg{{position:absolute;left:50%;width:640px;margin-left:-320px;padding:34px 40px;border-radius:30px;background:#1C1D29;border:2px solid #2E3044;display:flex;align-items:center;gap:30px;font-family:'Bebas Neue';font-size:86px;color:#fff;box-shadow:0 30px 60px rgba(0,0,0,.45)}}
.seg i{{font-style:normal;font-family:Inter;font-size:24px;color:var(--mut);display:block;letter-spacing:0}}
.ico{{width:110px;height:110px;flex:none;border-radius:26px;background:linear-gradient(135deg,var(--t1),var(--t2));display:flex;align-items:center;justify-content:center}}
.ico svg{{width:64px;height:64px;stroke:#0E0E16;stroke-width:2.4;fill:none;stroke-linecap:round;stroke-linejoin:round}}
.opt{{position:absolute;left:70px;right:70px;height:250px;border-radius:30px;background:#1C1D29;border:2px solid #2E3044;padding:34px 40px}}
.opt .h{{font-size:84px}} .opt p{{font-size:32px;color:var(--mut);margin-top:6px}}
.opt .x{{position:absolute;right:40px;top:50%;margin-top:-70px;width:140px;height:140px;border-radius:50%;border:8px solid var(--red);color:var(--red);font-size:90px;font-weight:800;display:flex;align-items:center;justify-content:center;background:rgba(14,14,22,.7)}}
.porta{{position:absolute;left:50%;top:520px;width:640px;margin-left:-320px;height:560px}}
.loja{{position:absolute;inset:0;border-radius:30px 30px 10px 10px;background:#1C1D29;border:3px solid #34364A;overflow:hidden}}
.toldo{{position:absolute;left:-3px;right:-3px;top:0;height:90px;background:repeating-linear-gradient(90deg,var(--g) 0 64px,#E9EAEE 64px 128px);opacity:.85}}
.vao{{position:absolute;left:110px;right:110px;top:150px;bottom:0;background:#0A0A12;border-radius:16px 16px 0 0;overflow:hidden}}
.grade{{position:absolute;left:0;right:0;top:0;background:repeating-linear-gradient(180deg,#5A5D72 0 16px,#3B3D50 16px 30px);transform-origin:top}}
.placa{{position:absolute;left:50%;top:210px;transform:translateX(-50%);font-family:'Bebas Neue';font-size:60px;letter-spacing:4px;color:var(--red);border:5px solid var(--red);padding:0 24px;border-radius:12px;background:#0E0E16;white-space:nowrap}}
.ring{{position:absolute;left:50%;top:50%;width:420px;height:420px;border-radius:50%;border:5px solid var(--g)}}
.zap{{position:absolute;left:50%;top:430px;width:330px;height:330px;margin-left:-165px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#33F0C8,#00A884 60%,#06705A);display:flex;align-items:center;justify-content:center;box-shadow:0 0 120px rgba(0,212,170,.55)}}
.zap svg{{width:170px;height:170px;fill:none;stroke:#fff;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}}
.feat{{position:absolute;left:60px;right:60px;height:190px;border-radius:28px;background:#171826;border:2px solid #2E3044;display:flex;align-items:center;gap:26px;padding:0 30px}}
.feat .k{{font-family:'Bebas Neue';font-size:56px;color:#fff;width:330px;line-height:.95}}
.feat .v{{flex:1;display:flex;flex-direction:column;gap:8px}}
.b1,.b2{{font-size:26px;border-radius:18px;padding:12px 18px;max-width:420px}}
.b1{{background:#232537;color:#DDE;align-self:flex-start}} .b2{{background:#0B3A33;color:#E8FFF8;align-self:flex-end}}
.seglbl{{font-size:20px;color:var(--mut);letter-spacing:2px;font-weight:700}}
.tl{{position:absolute;left:90px;right:90px;top:820px;height:6px;background:#2E3044;border-radius:3px}}
.tl .fill{{position:absolute;left:0;top:0;bottom:0;background:linear-gradient(90deg,var(--t1),var(--t2));transform-origin:left}}
.pt{{position:absolute;top:-17px;width:40px;height:40px;border-radius:50%;background:#0E0E16;border:6px solid var(--g);margin-left:-20px}}
.ptl{{position:absolute;top:60px;width:300px;margin-left:-150px;text-align:center}}
.ptl b{{display:block;font-family:'Bebas Neue';font-size:64px;color:#fff;font-weight:400}} .ptl span{{font-size:28px;color:var(--mut)}}
.fonte{{position:absolute;left:60px;right:60px;top:1270px;text-align:center;font-size:22px;color:var(--mut)}}
#cap{{position:absolute;left:50%;top:1390px;transform:translateX(-50%);width:980px;text-align:center;font-family:'Bebas Neue';font-size:92px;line-height:1.02;letter-spacing:1px;z-index:20;text-shadow:0 6px 24px rgba(0,0,0,.6)}}
#cap span{{color:rgba(255,255,255,.38)}} #cap span.on{{color:#fff}} #cap span.now{{color:var(--g)}}
.sim{{top:70px;right:60px}}
</style></head><body>
<div id="stage">
<div class="tex"></div><div class="glow" style="right:-400px;top:-300px"></div>
<div class="tag">FIM DA 6x1 <span>· ALQUIMIAS #2</span></div>

<div class="scene" {sc('s1')}>
 <div class="big h" style="top:220px;font-size:120px" data-in="{W('s1','Congresso')}">ESCALA <span class="grad">6x1</span></div>
 {semana({'SEG':'on','TER':'on','QUA':'on','QUI':'on','SEX':'on','SÁB':'on'}, top=470)}
 <div class="stamp" style="left:300px;top:540px;font-size:150px" data-in="{fx(W('s1','acabou'),'stamp')}" data-anim="stamp" data-shake="1" data-rot="-10">FIM</div>
 <div style="position:absolute;left:50px;right:50px;top:470px;display:grid;grid-template-columns:repeat(7,1fr);gap:12px;pointer-events:none">
  <div></div><div></div><div></div><div></div><div></div><div class="dia hot" data-in="{fx(W('s1','sábado'),'pop')}" data-anim="pop" data-shake="1">SÁB<small>QUEM?</small></div><div></div></div>
 <div class="big h" style="top:860px;font-size:130px;line-height:.95" data-in="{W('s1','quem')}">QUEM ATENDE<br><span class="grad">NO SÁBADO?</span></div>
</div>

<div class="scene" {sc('s2')}>
 <div class="big" style="top:200px" data-in="{W('s2','emenda')}"><span class="chip">EMENDA CONSTITUCIONAL 141</span></div>
 <div class="big" style="top:330px;font-size:34px;color:#E9EAEE" data-in="{W('s2','16')}">promulgada em 16/10/2026</div>
 <div class="tl"><div class="fill" style="right:0" data-in="{W('s2','Em')}" data-anim="grow"></div>
  <div class="pt" style="left:0%"></div><div class="ptl" style="left:8%"><b>HOJE</b><span>6x1</span></div>
  <div class="pt" style="left:50%" data-in="{fx(W('s2','sessenta'),'pop')}" data-anim="pop"></div><div class="ptl" style="left:50%" data-in="{W('s2','sessenta')}"><b>+60 DIAS</b><span>5x2 · até 42h</span></div>
  <div class="pt" style="left:100%" data-in="{fx(W('s2','horas'),'pop')}" data-anim="pop"></div><div class="ptl" style="left:92%" data-in="{W('s2','horas')}"><b>+14 MESES</b><span>até 40h</span></div>
 </div>
 <div data-in="{fx(W('s2','dois'),'pop')}">{semana({'SEG':'on','TER':'on','QUA':'on','QUI':'on','SEX':'on','SÁB':'rest x','DOM':'rest x'}, extra='<small>DESCANSO</small>', top=1000)}</div>
 <div class="fonte" style="top:1330px">Fonte: Agência Brasil e Agência Senado, 16/10/2026</div>
</div>

<div class="scene" {sc('s3')}>
 <div class="seg" data-out="{W('s3','Pra')}" style="top:240px" data-in="{fx(W('s3','Barbearia'),'pop')}" data-anim="slide" data-rot="-3"><div class="ico"><svg viewBox="0 0 24 24"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.1 15.9M14.5 14.5 20 20M8.1 8.1 12 12"/></svg></div><div>BARBEARIA<i>“tem horário sábado?”</i></div></div>
 <div class="seg" data-out="{W('s3','Pra')}" style="top:420px" data-in="{fx(W('s3','salão'),'pop')}" data-anim="slideL" data-rot="2"><div class="ico"><svg viewBox="0 0 24 24"><path d="M12 3c3 4 3 8 0 12-3-4-3-8 0-12z"/><path d="M5 21h14"/></svg></div><div>SALÃO<i>“dá pra encaixar uma escova?”</i></div></div>
 <div class="seg" data-out="{W('s3','Pra')}" style="top:600px" data-in="{fx(W('s3','clínica'),'pop')}" data-anim="slide" data-rot="-2"><div class="ico"><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/><rect x="3" y="3" width="18" height="18" rx="5"/></svg></div><div>CLÍNICA<i>“preciso remarcar a consulta”</i></div></div>
 <div class="seg" data-out="{W('s3','Pra')}" style="top:780px" data-in="{fx(W('s3','pet'),'pop')}" data-anim="slideL" data-rot="3"><div class="ico"><svg viewBox="0 0 24 24"><circle cx="7" cy="8" r="2"/><circle cx="17" cy="8" r="2"/><circle cx="4.5" cy="13" r="1.6"/><circle cx="19.5" cy="13" r="1.6"/><path d="M8 18c0-3 2-5 4-5s4 2 4 5c0 2-8 2-8 0z"/></svg></div><div>PET SHOP<i>“tem banho hoje ainda?”</i></div></div>
 <div class="seg" data-out="{W('s3','Pra')}" style="top:960px" data-in="{fx(W('s3','loja'),'pop')}" data-anim="slide" data-rot="-1"><div class="ico"><svg viewBox="0 0 24 24"><path d="M4 9h16l-1 11H5L4 9z"/><path d="M9 9V6a3 3 0 0 1 6 0v3"/></svg></div><div>LOJA<i>“ainda tem no tamanho M?”</i></div></div>
 <div class="big h" style="top:250px;font-size:110px;line-height:.95" data-in="{W('s3','Pra')}">SÁBADO:<br><span class="grad">O DIA QUE MAIS<br>CHEGA MENSAGEM</span></div>
 <div class="big" style="top:690px" data-in="{W('s3','Pra')}"><span class="chip" style="font-size:90px;border-color:var(--red)" data-count="{W('s3','sábado')},{W('s3','mensagem')+0.6},0,37" data-pre="+" data-pos=" CONVERSAS">+0</span></div>
 <div class="big" style="top:840px;font-size:24px;color:var(--mut)" data-in="{W('s3','Pra')}">simulação</div>
 <div style="position:absolute;inset:0" data-in="{fx(W('s3','difícil'),'stamp')}"><div class="stamp" style="left:110px;top:1010px;font-size:96px" data-in="{W('s3','difícil')}" data-anim="stamp" data-shake="1" data-rot="-6">DIFÍCIL DE COBRIR</div></div>
</div>

<div class="scene" {sc('s4')}>
 <div class="big h" style="top:190px;font-size:96px">AS SAÍDAS <span class="grad">DE SEMPRE</span></div>
 <div class="opt" style="top:350px" data-in="{W('s4','contratar')}" data-anim="slide"><div class="h">CONTRATAR MAIS</div><p>mais folha de pagamento</p><div class="x" data-in="{fx(W('s4','gente')+0.4,'x')}" data-anim="stamp" data-shake="1">✕</div></div>
 <div class="opt" style="top:640px" data-in="{W('s4','rodízio')}" data-anim="slide"><div class="h">RODÍZIO</div><p>a semana fica desfalcada</p><div class="x" data-in="{fx(W('s4','desfalcada')+0.5,'x')}" data-anim="stamp" data-shake="1">✕</div></div>
 <div class="opt" style="top:930px" data-in="{W('s4','fechar')}" data-anim="slide"><div class="h">FECHAR E TORCER</div><p>o cliente vai pro concorrente</p><div class="x" data-in="{fx(W('s4','segunda')+0.3,'x')}" data-anim="stamp" data-shake="1">✕</div></div>
</div>

<div class="scene" {sc('s5')}>
 <div class="big h" style="top:200px;font-size:140px" data-in="{fx(W('s5','quarto'),'pop')}" data-anim="pop">O <span class="grad">4º CAMINHO</span></div>
 <div class="porta" data-in="{W('s5','Tem')}" data-out="{W('s5','WhatsApp')}"><div class="loja"><div class="toldo"></div><div class="vao"><div class="grade" style="height:100%" data-in="{fx(W('s5','porta'),'shutter')}" data-anim="grow"></div></div></div>
  <div class="placa" data-in="{W('s5','fecha')+0.3}" data-anim="stamp" data-shake="1">FECHADO</div></div>
 <div data-in="{fx(W('s5','WhatsApp'),'ding')}"><div class="ring" style="top:595px" data-ring></div><div class="ring" style="top:595px" data-ring></div><div class="ring" style="top:595px" data-ring></div>
  <div class="zap" data-anim="pop" data-in="{W('s5','WhatsApp')}"><svg viewBox="0 0 24 24"><path d="M20 12a8 8 0 0 1-11.8 7L4 20l1.1-4A8 8 0 1 1 20 12z"/><path d="M9 10c0 3 2 5 5 5l1-1.4-1.6-.8-.8.8c-1-.4-1.8-1.2-2.2-2.2l.8-.8-.8-1.6L9 10z"/></svg></div>
  <div class="big h" style="top:860px;font-size:110px">A PORTA FECHA.<br><span class="grad">O WHATSAPP ATENDE.</span></div></div>
</div>

<div class="scene" {sc('s6')}>
 <div class="big h" style="top:170px;font-size:84px" data-in="{W('s6','Uma')}">IA COM O <span class="grad">NOME DA SUA EMPRESA</span></div>
 <div class="feat" style="top:300px" data-in="{fx(W('s6','responde'),'pop')}" data-anim="slide"><div class="k">RESPONDE EM<br>SEGUNDOS</div><div class="v"><span class="seglbl">BARBEARIA · SÁB 21:14</span><span class="b1">Tem horário amanhã cedo?</span><span class="b2">Tenho 9h e 10h30 com o Rafa!</span></div></div>
 <div class="feat" style="top:510px" data-in="{fx(W('s6','marca'),'pop')}" data-anim="slide"><div class="k">MARCA NA<br>AGENDA</div><div class="v"><span class="seglbl">CLÍNICA · SÁB 10:02</span><span class="b2">Agendado ✓ Seg, 8h, Dra. Paula</span></div></div>
 <div class="feat" style="top:720px" data-in="{fx(W('s6','cobra'),'pop')}" data-anim="slide"><div class="k">COBRA<br>NO PIX</div><div class="v"><span class="seglbl">PET SHOP · SÁB 15:40</span><span class="b2">Pix do banho do Thor enviado ✓</span></div></div>
 <div class="feat" style="top:930px" data-in="{fx(W('s6','lembra'),'pop')}" data-anim="slide"><div class="k">LEMBRA NA<br>VÉSPERA</div><div class="v"><span class="seglbl">SALÃO · DOM 18:00</span><span class="b2">Lembrete: amanhã, 14h, corte e escova</span></div></div>
 <div class="feat" style="top:1140px;height:150px;border-color:var(--t2)" data-in="{fx(W('s6','pessoa'),'pop')}" data-anim="up"><div class="k" style="width:auto">PRA EQUIPE NA SEGUNDA:</div><div class="v"><span class="b1" style="align-self:auto">3 conversas separadas</span></div></div>
</div>

<div class="scene" {sc('s7')}>
 <div class="big h" style="top:200px;font-size:110px" data-in="{W('s7','equipe')}">A EQUIPE <span class="grad">DESCANSA.</span></div>
 <div class="big h" style="top:330px;font-size:110px" data-in="{fx(W('s7','cliente'),'pop')}">O CLIENTE É <span class="grad">ATENDIDO.</span></div>
 <div class="big h" style="top:460px;font-size:110px" data-in="{fx(W('s7','segunda'),'pop')}">A SEGUNDA <span class="grad">COMEÇA CHEIA.</span></div>
 <div data-in="{W('s7','descansa')}">{semana({'SEG':'on','TER':'on','QUA':'on','QUI':'on','SEX':'on','SÁB':'rest','DOM':'rest'}, top=680)}</div>
 <div style="position:absolute;left:50px;right:50px;top:680px;display:grid;grid-template-columns:repeat(7,1fr);gap:12px">
  <div><div class="dia full" data-in="{W('s7','segunda')}" data-anim="pop" data-shake="1">SEG<small>CHEIA</small></div></div><div></div><div></div><div></div><div></div>
  <div><div class="dia ia" data-in="{W('s7','cliente')}" data-anim="pop">SÁB<small>IA ON</small></div></div><div><div class="dia ia" data-in="{W('s7','cliente')+0.15}" data-anim="pop">DOM<small>IA ON</small></div></div></div>
</div>

<div class="scene" {sc('s8', True)}>
 <div class="big h" style="top:250px;font-size:120px;line-height:.95" data-in="{W('s8','Manda')}">MANDA PRA QUEM<br><span class="grad">VAI MONTAR A<br>ESCALA NOVA</span></div>
 <div class="big" style="top:740px" data-in="{fx(W('s8','Malvora'),'ding')}" data-anim="pop"><div id="sym8" style="width:230px;height:230px;margin:0 auto"></div></div>
 <div class="big h" style="top:1010px;font-size:76px" data-in="{W('s8','nova')}">MALVORA · <span class="grad">A NOVA ALQUIMIA DIGITAL</span></div>
</div>

<div id="cap"></div>
</div>
<script>window.CAP={json.dumps(caps, ensure_ascii=False)};
document.getElementById('sym8').innerHTML=symImg(230);</script>
</body></html>'''
open('alquimias-02.html', 'w').write(html)
json.dump({'tempos': T, 'total': round(END, 2)}, open('../tempos.json', 'w'), indent=1)
json.dump(sorted(EF), open('../efeitos.json', 'w'))
print('total', round(END, 2), 'efeitos', len(EF), 'legendas', len(caps))
