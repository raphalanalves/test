"""Trilha e efeitos do Alquimias #3 (sintetizados aqui, sem direitos autorais)."""
"""Trilha e efeitos do V14, sintetizados aqui (sem direitos autorais). Tempos iguais aos de v14.js."""
import sys, wave, numpy as np
SR = 44100
TOTAL = 51.97
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

stamp(0.5); boom(0.5,.6); whoosh(2.0,.5,.4); x=tt(1.5); add(lp(rng.standard_normal(len(x)),.05)*np.sin(np.pi*x/1.5),2.0,0.5)
stamp(3.65); whoosh(6.6,.4,.4); boom(7.12,.7); plim(8.88); plim(10.11,False)
for t in (13.15,14.77,16.51): plim(t)
stamp(15.46); whoosh(19.8,.4,.3); whoosh(22.1,.4,.4)
for k in range(16): tick(23.4+k*0.1,0.15)
boom(25.0,.6); x=tt(1.6); add(sum(np.sin(2*np.pi*f*x) for f in (1319,1568,1976,2637))*np.exp(-x*2.2)/4,25.0,0.16)
whoosh(28.1,.4,.4); stamp(28.79); whoosh(33.9,.4,.4); stamp(34.2); boom(34.2,.6)
for t in (42.23,43.3,43.9): plim(t)
boom(46.95,.6)
chord(0.3,(220,277.2,329.6),13,0.04); chord(13,(196,246.9,293.7),15,0.04); chord(28,(174.6,220,261.6),13,0.04); chord(41,(261.6,329.6,392,523.3),10.5,0.06)
m = max(abs(L).max(), abs(R).max()); L, R = L / m * 0.89, R / m * 0.89
st = np.empty(len(L) * 2); st[0::2] = L; st[1::2] = R
out = sys.argv[1] if len(sys.argv) > 1 else '../audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())
print('ok', out)
