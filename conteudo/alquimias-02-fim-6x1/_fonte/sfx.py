"""Sintetiza efeitos sonoros simples (sem direitos autorais) e mistura na linha do tempo."""
import json, wave, numpy as np
SR = 44100
def env(n, a=0.005, r=0.5):
    t = np.arange(n) / SR; e = np.minimum(1, t / a) * np.exp(-t / (r * n / SR)); return e
def whoosh():
    n = int(0.38 * SR); x = np.random.randn(n)
    f = np.linspace(0.02, 0.35, n); y = np.zeros(n); acc = 0
    for i in range(n): acc += f[i] * (x[i] - acc); y[i] = acc
    w = np.sin(np.linspace(0, np.pi, n)) ** 2; return 0.5 * y * w / (abs(y).max() + 1e-9)
def pop():
    n = int(0.12 * SR); t = np.arange(n) / SR; fr = 900 * np.exp(-t * 18) + 300
    return 0.45 * np.sin(2 * np.pi * np.cumsum(fr) / SR) * env(n, 0.002, 0.25)
def stamp():
    n = int(0.25 * SR); t = np.arange(n) / SR
    return 0.7 * (np.sin(2 * np.pi * 70 * t) + 0.4 * np.random.randn(n) * np.exp(-t * 40)) * env(n, 0.001, 0.3)
def x():
    n = int(0.18 * SR); t = np.arange(n) / SR
    return 0.35 * np.sign(np.sin(2 * np.pi * 180 * t)) * env(n, 0.001, 0.2)
def ding():
    n = int(0.9 * SR); t = np.arange(n) / SR
    return 0.3 * (np.sin(2 * np.pi * 1318 * t) + 0.5 * np.sin(2 * np.pi * 1976 * t)) * env(n, 0.003, 0.35)
def shutter():
    n = int(0.6 * SR); t = np.arange(n) / SR
    return 0.25 * np.sign(np.sin(2 * np.pi * 34 * t)) * np.random.rand(n) * env(n, 0.01, 0.6)
FX = dict(whoosh=whoosh, pop=pop, stamp=stamp, x=x, ding=ding, shutter=shutter)
total = json.load(open('../tempos.json'))['total']
mix = np.zeros(int((total + 1) * SR))
for t, k in json.load(open('../efeitos.json')):
    s = FX[k](); i = int(t * SR); mix[i:i + len(s)] += s[:len(mix) - i]
mix = np.clip(mix * 0.6, -1, 1)
with wave.open('../efeitos.wav', 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
print('ok')
