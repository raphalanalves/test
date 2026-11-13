# Vinheta padrão da série "Entrevistas VIP · Clientes Malvora" (modelo reutilizável)
# uso: python3 vinheta.py <episodio> "<nome do cliente>" <logo_cliente.png> <saida.mp4> [largura]
import sys,subprocess,os
REPO=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))
ep,cli,logo,out=sys.argv[1:5]; W=int(sys.argv[5]) if len(sys.argv)>5 else 540; H=W*16//9; k=W/540
D=3.2; SYM=os.path.join(REPO,'conteudo','marca','simbolo-principal.png')
MARCA=os.path.join(REPO,'conteudo','marca')
ass=f"""[Script Info]
ScriptType: v4.00+
PlayResX: 540
PlayResY: 960
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: T,Inter ExtraBold,50,&H00F7F3F2,&H00F7F3F2,&H00000000,&H00000000,-1,0,0,0,100,100,2,0,1,0,0,5,0,0,0,1
Style: S,Inter ExtraBold,19,&H00AAD400,&H00AAD400,&H00000000,&H00000000,-1,0,0,0,100,100,6,0,1,0,0,5,0,0,0,1
Style: E,Inter,23,&H00FFFFFF,&H00FFFFFF,&H00EE687B,&H00EE687B,-1,0,0,0,100,100,1,0,3,9,0,5,0,0,0,1
Style: L,Inter,10,&H00AAD400,&H00AAD400,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 1,0:00:00.10,0:00:03.00,L,,0,0,0,,{{\\pos(0,0)\\p1\\alpha&H00&\\clip(0,0,0,960)\\t(0,500,\\clip(0,0,540,960))}}m 70 530 l 470 530 470 532 70 532
Dialogue: 2,0:00:00.55,0:00:03.00,S,,0,0,0,,{{\\pos(270,500)\\fad(250,0)\\fsp16\\t(0,700,\\fsp6)}}CLIENTES MALVORA
Dialogue: 2,0:00:00.75,0:00:03.00,T,,0,0,0,,{{\\pos(270,580)\\fad(200,0)\\fscx88\\fscy88\\fsp14\\t(0,450,\\fscx100\\fscy100\\fsp2)}}ENTREVISTAS VIP
Dialogue: 2,0:00:01.30,0:00:03.00,E,,0,0,0,,{{\\pos(270,660)\\fad(200,0)\\move(270,690,270,660,0,300)}}Ep. {ep} · {cli}
"""
open(out+'.ass','w').write(ass)
fc=(f"[1]scale={int(170*k)}:-1,format=rgba,fade=t=in:st=0.15:d=0.5:alpha=1[s0];"
    f"[s0]scale=w='trunc({170*k}*(0.7+0.3*min(t/0.6,1))/2)*2':h=-2:eval=frame[s1];"
    f"[2]scale={int(150*k)}:-1,format=rgba,colorkey=0x000000:0.12:0.08,fade=t=in:st=1.55:d=0.4:alpha=1[c];"
    f"[0][s1]overlay=x='(W-w)/2':y='{int(330*k)}-h/2':shortest=1[b];[b][c]overlay=x='(W-w)/2':y={int(760*k)}[d];"
    f"[d]ass={out}.ass,fade=t=out:st={D-0.25}:d=0.25,format=yuv420p[v];"
    f"[3:a]volume=1.6,adelay=0|0[a1];[4:a]volume=0.07,adelay=750|750[a2];[5:a]volume=0.0,adelay=1300|1300[a3];"
    f"[a1][a2][a3]amix=inputs=3:normalize=0:duration=longest,apad,atrim=0:{D},aresample=48000,aformat=channel_layouts=stereo:sample_fmts=s16[a]")
subprocess.run(['ffmpeg','-nostdin','-y','-loglevel','error','-f','lavfi','-i',f'color=0x0B0B13:s={W}x{H}:r=30:d={D}','-loop','1','-i',SYM,'-loop','1','-i',logo,
  '-i',os.path.join(MARCA,'sfx-swell-transicao.wav'),'-i',os.path.join(MARCA,'sfx-chime.mp3'),'-i',os.path.join(MARCA,'sfx-chime.mp3'),'-filter_complex',fc,'-map','[v]','-map','[a]','-t',str(D),'-c:v','libx264','-crf','16','-r','30','-c:a','pcm_s16le',out.replace('.mp4','.mov') if False else out],check=True)
print('ok',out)
