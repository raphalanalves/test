# monta tempos, legendas e o HTML a partir dos áudios da Amandoca
import json,subprocess
D=[float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'../audio/s{i}.mp3'])) for i in range(1,9)]
ST=[0.6]
for i,d in enumerate(D[:-1]): ST.append(round(ST[-1]+d+0.25,2))
TOTAL=round(ST[-1]+D[-1]+2.5,2)
WS=[[dict(w,t=round(w['t']+ST[i],3)) for w in json.load(open(f'../audio/s{i+1}.json'))] for i in range(8)]
CAP=[]
for W in WS:
    ch=[];cur=[]
    for w in W:
        cur.append(w)
        if len(cur)>=4 or w['w'] in ('Primeiro','Segundo','Terceiro','qualquer','irritado','cliente','opções','IA','empresa','pessoa','LGPD','assim','nome','embaixo'): ch.append(cur);cur=[]
    if cur:
        if len(cur)==1 and ch: ch[-1]+=cur
        else: ch.append(cur)
    for j,c in enumerate(ch):
        b=ch[j+1][0]['t'] if j+1<len(ch) else c[-1]['t']+c[-1]['d']+0.5
        CAP.append({"a":c[0]['t'],"b":round(b,3),"w":[[x['w'],x['t'],x['d']] for x in c]})
def wt(i,word):
    for w in WS[i]:
        if w['w'].lower().startswith(word.lower()): return w['t']
    return ST[i]
K={"st":ST,"total":TOTAL,"preco":wt(2,'pergunta'),"hor":wt(2,'pede'),"muda":wt(2,'muda'),"menu":wt(3,'menu'),"robo":wt(3,'robô'),
   "serv":wt(4,'saber'),"equipe":wt(4,'chamar'),"q1":wt(5,'desenvolveu'),"q2":wt(5,'onde'),"q3":wt(5,'LGPD'),"m1":wt(6,'tecnologia'),"m2":wt(6,'dados'),"m3":wt(6,'equipe'),"ia":wt(7,'Comenta')}
json.dump({"starts":ST,"total":TOTAL},open('../tempos.json','w'))
h=open('modelo.html').read().replace('/*DADOS*/','const K='+json.dumps(K)+',CAP='+json.dumps(CAP,ensure_ascii=False)+';')
open('video.html','w').write(h);print(ST,TOTAL)
