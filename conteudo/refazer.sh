# uso: bash refazer.sh pasta saida.mp4 n_trechos — recalcula tempos, efeitos, mixagem e vídeo
set -e; cd "$1/_fonte"; python3 gerar.py >/dev/null
python3 - <<'P'
import json,re
K=json.load(open('../tempos.json'));s=open('sfx.py').read()
s=re.sub(r'TOTAL = [0-9.]+','TOTAL = %s'%K['total'],s);s=re.sub(r'\nS=\[[^\]]*\]; T=[0-9.]+','\nS=%s; T=%s'%(K['starts'],K['total']),s)
open('sfx.py','w').write(s)
P
python3 sfx.py ../efeitos.wav >/dev/null; cd ..
IN=""; F=""; L=""; i=1; for s in $(python3 -c "import json;print(' '.join(str(int(x*1000)) for x in json.load(open('tempos.json'))['starts']))"); do IN="$IN -i audio/s$i.mp3"; F="$F[$i:a]adelay=$s|$s[v$i];"; L="$L[v$i]"; i=$((i+1)); done
ffmpeg -loglevel error -y -i efeitos.wav $IN -filter_complex "[0:a]volume=0.4[fx];${F}[fx]${L}amix=inputs=$i:normalize=0,alimiter=limit=0.95[o]" -map "[o]" -ar 44100 audio-final.wav
T=$(python3 -c "import json;print(json.load(open('tempos.json'))['total'])")
cd _fonte; node render.js video.html $T ../tmp.mp4 ../audio-final.wav $(python3 -c "print($T-4)"); cd ..
ffmpeg -loglevel error -y -i tmp.mp4 -c:v libx264 -crf 24 -preset slow -pix_fmt yuv420p -c:a copy -movflags +faststart $2 && mv tmp-capa.jpg ${2%.mp4}-capa.jpg && rm tmp.mp4; echo "$2 $T"
