"""Trilha e efeitos do V14, sintetizados aqui (sem direitos autorais). Tempos iguais aos de v14.js."""
import sys, wave, numpy as np
SR = 44100
TOTAL = 18.4
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

# --- toque do celular: frase de marimba (autoral) + vibração
def ring(a, b):
    notes = [659, 784, 988, 1319, 988, 784]
    t = a
    while t < b - 0.1:
        for k, f in enumerate(notes):
            if t + k * 0.1 < b: add(tone(f, 0.35, 0.12, (1, .5, .2, .08)), t + k * 0.1, 0.16, pan=(-.3 if k % 2 else .3))
        t += 0.6
    d = b - a; x = tt(d)
    buzz = np.sign(np.sin(2 * np.pi * 155 * x)) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 2.5 * x)))
    add(lp(buzz, 0.08) * np.sin(np.pi * x / d), a, 0.22)
for a, b in [(0.15, 1.35), (1.65, 2.85), (9.45, 10.25)]: ring(a, b)

# --- tensão no começo (pad grave)
x = tt(4.3); pad = (np.sin(2 * np.pi * 55 * x) + .5 * np.sin(2 * np.pi * 82.4 * x)) * np.minimum(1, x / 1.5) * np.minimum(1, (4.3 - x) / .3)
add(pad, 0, 0.12)

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

# chamada perdida
glitch(3.0, 0.32); boom(3.0, 0.7); stamp(3.45)

# palavras no ritmo: bumbo em cada palavra, chimbal no contratempo, palmas nas pares
W0, B, NW = 4.3, 0.72, 7
glitch(W0 - 0.12, 0.2)
for i in range(NW):
    t = W0 + i * B
    kick(t, 0.9 if i < NW - 1 else 0.4)
    hat(t + B / 2); hat(t + B / 4, .06); hat(t + 3 * B / 4, .06)
    if i % 2: clap(t)
    x = tt(B); bass = np.sin(2 * np.pi * [55, 55, 65.4, 55, 73.4, 65.4, 55][i] * x) * np.exp(-x * 3)
    add(bass, t, 0.3)
    if i in (3, 4): glitch(t, 0.14)
riser(W0 + 5 * B, B)
boom(W0 + 6 * B, 1.0); whoosh(W0 + 6 * B - .2, .3, .3)

# volta o celular, IA responde, cliente desliga
whoosh(10.15, 0.4, 0.4)
for k in range(5): tick(10.5 + k * 0.09, 0.08)
plim(10.95)
busy(11.55)
plim(12.2, up=False)
for k in range(5): tick(12.7 + k * 0.1, 0.08)
plim(13.25)
x = tt(1.6)  # brilho de confirmação
add(sum(np.sin(2 * np.pi * f * x) for f in (1319, 1568, 1976, 2637)) * np.exp(-x * 2.2) * np.minimum(1, x / .02) / 4, 13.3, 0.18)

# trilha de fundo da parte boa (acordes suaves)
def chord(t, fs, d, g=0.07):
    x = tt(d); s = sum(np.sin(2 * np.pi * f * x) + .3 * np.sin(2 * np.pi * 2 * f * x) for f in fs)
    add(s * np.minimum(1, x / .4) * np.minimum(1, (d - x) / .6), t, g)
chord(9.45, (220, 277.2, 329.6), 2.2); chord(11.6, (196, 246.9, 293.7), 2.2); chord(13.7, (174.6, 220, 261.6), 2.4)
whoosh(14.25, 0.5, 0.4)

# fecho digitado e marca
for k in range(len("RESPONDE NA HORA.")): tick(14.55 + k / 22, 0.14)
for k in range(len("NINGUÉM PRECISA LIGAR.")): tick(15.55 + k / 22, 0.14)
boom(16.6, 0.5)
chord(16.55, (261.6, 329.6, 392, 523.3), 1.85, 0.09)
x = tt(1.6); add(sum(np.sin(2 * np.pi * f * x) for f in (2093, 2637, 3136)) * np.exp(-x * 2) / 3, 16.65, 0.12, pan=.3)

m = max(abs(L).max(), abs(R).max()); L, R = L / m * 0.89, R / m * 0.89
st = np.empty(len(L) * 2); st[0::2] = L; st[1::2] = R
out = sys.argv[1] if len(sys.argv) > 1 else '../audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())
print('ok', out)
