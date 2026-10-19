"""Trilha e efeitos do V5 (sintetizados aqui, sem direitos autorais)."""
"""Trilha e efeitos do V14, sintetizados aqui (sem direitos autorais). Tempos iguais aos de v14.js."""
import sys, wave, numpy as np
SR = 44100
TOTAL = 25.2
rng = np.random.default_rng(7)
L = np.zeros(int(TOTAL * SR)); R = np.zeros_like(L)

def add(sig, t, g=1.0, pan=0.0):
    i = int(t * SR); n = min(len(sig), len(L) - i)
    if n <= 0: return
    L[i:i + n] += sig[:n] * g * (1 - max(pan, 0)); R[i:i + n] += sig[:n] * g * (1 + min(pan, 0))

def tt(d): return np.arange(int(d * SR)) / SR
def env(d, a=0.004, dec=0.3):
    t = tt(d); return np.minimum(1, t / a) * np.exp(-t / dec)
def tone(f, d, dec=0.25, harm=(1, .35, .12)):
    t = tt(d); return sum(h * np.sin(2 * np.pi * f * (k + 1) * t) for k, h in enumerate(harm)) * env(d, 0.003, dec)
def lp(x, a):  # filtro passa-baixa simples
    y = np.zeros_like(x); acc = 0.0
    for i, v in enumerate(x): acc += a * (v - acc); y[i] = acc
    return y

def glitch(t, d=0.3):
    x = tt(d); n = rng.standard_normal(len(x))
    crush = np.round(n * 3) / 3 * np.sign(np.sin(2 * np.pi * rng.uniform(40, 90) * x))
    add(crush * np.exp(-x / d * 1.5), t, 0.28, pan=rng.uniform(-.6, .6))
def boom(t, g=0.9):
    x = tt(1.2); f = 120 * np.exp(-x * 5) + 38
    add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x * 2.6), t, g)
def stamp(t):
    x = tt(0.3); add((np.sin(2 * np.pi * 70 * x) + .6 * rng.standard_normal(len(x)) * np.exp(-x * 45)) * np.exp(-x * 9), t, 0.55)
def kick(t, g=0.8):
    x = tt(0.35); f = 150 * np.exp(-x * 30) + 48
    add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x * 9), t, g)
def hat(t, g=0.12):
    x = tt(0.06); add(np.diff(rng.standard_normal(len(x) + 1)) * np.exp(-x * 70), t, g, pan=.4)
def clap(t):
    x = tt(0.2); n = rng.standard_normal(len(x))
    add(lp(n, 0.5) * (np.exp(-x * 30) + .5 * np.exp(-np.maximum(x - .012, 0) * 30) * (x > .012)), t, 0.35, pan=-.2)
def whoosh(t, d=0.45, g=0.45):
    x = tt(d); n = rng.standard_normal(len(x)); y = np.zeros_like(n); acc = 0
    a = np.linspace(.01, .4, len(x))
    for i in range(len(x)): acc += a[i] * (n[i] - acc); y[i] = acc
    add(y * np.sin(np.pi * x / d) ** 2 / (abs(y).max() + 1e-9), t, g)
def riser(t, d):
    x = tt(d); n = rng.standard_normal(len(x)); y = np.zeros_like(n); acc = 0
    a = np.linspace(.005, .5, len(x))
    for i in range(len(x)): acc += a[i] * (n[i] - acc); y[i] = acc
    add(y / (abs(y).max() + 1e-9) * (x / d) ** 2, t, 0.35)
    add(np.sin(2 * np.pi * np.cumsum(np.linspace(200, 900, len(x))) / SR) * (x / d) ** 2, t, 0.06)
def plim(t, up=True):
    a, b = (988, 1319) if up else (784, 988)
    add(tone(a, 0.25, 0.08), t, 0.22, pan=.2); add(tone(b, 0.45, 0.14), t + 0.08, 0.22, pan=-.2)
def tick(t, g=0.18):
    x = tt(0.03); add(rng.standard_normal(len(x)) * np.exp(-x * 220), t, g, pan=rng.uniform(-.3, .3))
def busy(t):
    for k in range(3): add(np.sin(2 * np.pi * 425 * tt(0.18)) * np.minimum(1, tt(0.18) / .005), t + k * 0.34, 0.16)

def chord(t, fs, d, g=0.07):
    x = tt(d); s = sum(np.sin(2 * np.pi * f * x) + .3 * np.sin(2 * np.pi * 2 * f * x) for f in fs)
    add(s * np.minimum(1, x / .4) * np.minimum(1, (d - x) / .6), t, g)

TA0,DA,NA,TB0,DB,NB,TRW,TRES=3.0,0.62,14,13.68,1.25,4,12.28,19.58
boom(0.05,0.6); whoosh(2.7,.4,.4)
for i in range(NA):
    t=TA0+i*DA; kick(t,0.55); hat(t+DA/2)
    add(tone(523*(1.06**i),0.2,0.08),t,0.12)   # tom sobe a cada mensagem (tensão)
    if i in (1,6): glitch(t-0.1,0.12)
x=tt(TRW-TA0); add(np.sin(2*np.pi*np.cumsum(np.linspace(110,190,len(x)))/SR)*np.minimum(1,x/1),TA0,0.08)
stamp(TA0+NA*DA)
# rebobinar
x=tt(TB0-0.4-TRW); add(np.sin(2*np.pi*np.cumsum(np.linspace(900,120,len(x)))/SR)*0.5+0.3*rng.standard_normal(len(x))*np.sin(2*np.pi*30*x),TRW,0.25)
for k in range(10): tick(TRW+k*0.12,0.2)
whoosh(TB0-0.5,.4,.4)
for i in range(NB): plim(TB0+i*DB, up=i%2==1)
chord(TB0,(261.6,329.6,392),5.8,0.07)
x=tt(1.6); add(sum(np.sin(2*np.pi*f*x) for f in (1319,1568,1976,2637))*np.exp(-x*2.2)/4,TB0+3*DB,0.18)
whoosh(TRES-0.3,.4,.4); kick(TRES+0.4,0.8); stamp(TRES+0.4); kick(TRES+1.0,0.8); plim(TRES+1.0)
boom(TRES+2.0,0.5); chord(TRES+2.0,(261.6,329.6,392,523.3),3.5,0.09)
m = max(abs(L).max(), abs(R).max()); L, R = L / m * 0.89, R / m * 0.89
st = np.empty(len(L) * 2); st[0::2] = L; st[1::2] = R
out = sys.argv[1] if len(sys.argv) > 1 else '../audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())
print('ok', out)
