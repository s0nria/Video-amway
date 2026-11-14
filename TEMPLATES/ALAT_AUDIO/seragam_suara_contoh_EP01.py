"""EP01 v7: suara seragam + lebih jelas. Padan nada kedua-dua rakaman ke satu lengkung sasaran,
seimbangkan setiap ayat, tambah kecerahan (exciter), kemudian ganti audio v6 (video disalin terus)."""
import os, subprocess, wave, json, numpy as np
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, "rec")
SR, SPD = 48000, 1.15
def run(c): subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y"] + c, check=True)
def load(p):
    w = wave.open(p); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    return a[::2] if w.getnchannels() == 2 else a
def save(p, x, ch=1):
    w = wave.open(p, "wb"); w.setnchannels(ch); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()

N, HOP = 2048, 512
win = np.hanning(N).astype(np.float32)
f = np.fft.rfftfreq(N, 1 / SR)
def stft(x):
    x = np.pad(x, (N, N)); n = 1 + (len(x) - N) // HOP
    return np.stack([np.fft.rfft(x[i*HOP:i*HOP+N] * win) for i in range(n)])
def istft(X, L):
    y = np.zeros(HOP * (len(X) - 1) + N); wsum = np.zeros_like(y)
    for i, F in enumerate(X):
        y[i*HOP:i*HOP+N] += np.fft.irfft(F) * win; wsum[i*HOP:i*HOP+N] += win ** 2
    return (y / np.maximum(wsum, 1e-6))[N:N+L]

# lengkung sasaran (dB relatif kepada purata 300-3000 Hz): kurang berat, lebih jelas
TP = np.array([[80, -14], [150, -3], [250, 4], [300, 6], [600, 5], [1000, 1], [2000, -2], [3000, -3], [3900, -5]])
target = np.interp(np.log10(np.maximum(f, 1)), np.log10(TP[:, 0]), TP[:, 1])
def match(x):
    X = stft(x); P = np.abs(X) ** 2; e = P.sum(1); sp = e > e.max() * 1e-3
    lt = 10 * np.log10(P[sp].mean(0) + 1e-12)
    # licinkan 1/3 oktaf
    sm = np.array([lt[(f >= fc / 1.26) & (f <= fc * 1.26)].mean() if fc > 40 else lt[i] for i, fc in enumerate(f)])
    rel = sm - sm[(f > 300) & (f < 3000)].mean()
    g = np.clip(target - rel, -12, 8); g[f > 3900] = 0; g[f < 60] = -12
    print("   EQ dipakai (dB) @200/500/1k/2k/3k/3.8k:", [round(float(np.interp(v, f, g)), 1) for v in (200, 500, 1000, 2000, 3000, 3800)])
    return istft(X * (10 ** (g / 20))[None, :], len(x))

def deplosive(x, det=120, fc=170, target=0.015):
    """Anti-pop: kesan bingkai dengan tenaga bawah 120 Hz berlebihan (letupan p/b, nafas dekat mikrofon;
    suara biasa hampir tiada tenaga di situ), kemudian perlahankan hanya jalur bawah ~200 Hz pada bingkai itu."""
    X = stft(x); P = np.abs(X) ** 2
    lo = P[:, (f > 20) & (f < det)].sum(1); tot = P[:, (f > 20) & (f < 4000)].sum(1) + 1e-12; r = lo / tot
    act = tot > tot.max() * 1e-4
    g = np.where(act & (r > target), np.sqrt(target / np.maximum(r, 1e-12)), 1.0)
    g = np.clip(g, 10 ** (-30 / 20), 1.0)
    for i in range(1, len(g)): g[i] = min(g[i], 1 - (1 - g[i-1]) * 0.5)      # lepas ~3 bingkai
    for i in range(len(g) - 2, -1, -1): g[i] = min(g[i], 1 - (1 - g[i+1]) * 0.5)
    ramp = np.clip((fc + 50 - f) / 50, 0, 1)                                     # penuh <170 Hz, lembut ke 220 Hz
    G = 1 - ramp[None, :] * (1 - g[:, None])
    print(f"   anti-pop: {int((g < 0.7).sum())} bingkai letupan diperlahankan daripada {int(act.sum())} bingkai bersuara")
    return istft(X * G, len(x))

print("rakaman 1:"); r1 = match(load(os.path.join(R, "rec_clean2.wav"))); r1 = deplosive(r1); save(os.path.join(R, "rec1_eq.wav"), r1)
print("rakaman 2:"); r2 = match(load(os.path.join(R, "rec2_clean.wav"))); r2 = deplosive(r2); save(os.path.join(R, "rec2_eq.wav"), r2)

# potongan (rakaman, mula, tamat, letak) - sama dengan build_v6
C1 = [(0.94, 3.92, 0.3), (5.12, 8.02, 3.54), (8.52, 9.86, 6.8), (11.40, 15.42, 8.45), (16.26, 18.00, 12.25),
      (24.73, 27.87, 13.97), (28.35, 30.71, 16.9), (31.29, 33.29, 19.2), (40.27, 45.21, 21.55), (45.49, 58.31, 26.05),
      (60.57, 67.05, 37.45), (71.73, 76.83, 43.65), (77.25, 80.65, 48.3), (81.39, 85.59, 51.5), (86.25, 90.17, 55.8),
      (91.65, 93.79, 59.45), (94.11, 96.59, 61.55), (98.62, 102.80, 64.25), (104.74, 108.58, 68.0)]
CUTS = [(1, a, b, st, max(a - 0.08, 0)) for a, b, st in C1] + [(2, 0.0, 1.80, 71.55, 0.0)]
def act_db(x):
    n = int(.03 * SR); fr = x[:len(x)//n*n].reshape(-1, n); e = (fr ** 2).mean(1)
    return 10 * np.log10(e[e > e.max() * 10 ** -3.5].mean())
TARGET = -18.0
gains = []
for src, a, b, st, a0 in CUTS:
    x = (r1 if src == 1 else r2)[int(a * SR):int(b * SR)]; gains.append(TARGET - act_db(x))
print("gain setiap ayat (dB):", [round(g, 1) for g in gains])

DUR = 73.967
fc = ["[0:a]asplit=%d" % sum(1 for c in CUTS if c[0] == 1) + "".join(f"[s{j}]" for j, c in enumerate(CUTS) if c[0] == 1),
      f"[1:a]anull[s{len(CUTS)-1}]"]
for j, ((src, a, b, st, a0), g) in enumerate(zip(CUTS, gains)):
    b0 = b + 0.15; L = (b0 - a0) / SPD; lead = (a - a0) / SPD; d = int((st - lead) * 1000)
    fc.append(f"[s{j}]atrim={a0}:{b0},asetpts=PTS-STARTPTS,atempo={SPD},volume={g:.2f}dB,afade=t=in:d=0.03,"
              f"afade=t=out:st={L-0.05:.3f}:d=0.05,adelay={d}|{d}[c{j}]")
fc.append("".join(f"[c{j}]" for j in range(len(CUTS))) + f"amix=inputs={len(CUTS)}:normalize=0,atrim=0:{DUR}[v]")
vraw = os.path.join(R, "voice_raw_v7.wav")
run(["-i", os.path.join(R, "rec1_eq.wav"), "-i", os.path.join(R, "rec2_eq.wav"), "-filter_complex", ";".join(fc),
     "-map", "[v]", "-ar", str(SR), "-ac", "1", vraw])

post = ",".join(["highpass=f=100:poles=2", "aexciter=amount=2.5:drive=7:blend=0:freq=3200:ceil=10000",   # harmonik atas 4 kHz
                 "equalizer=f=5500:t=q:w=1.0:g=2", "deesser=i=0.35",
                 "acompressor=threshold=-22dB:ratio=2.5:attack=8:release=120:makeup=1.5",
                 "loudnorm=I=-14:TP=-1.5:LRA=5", "alimiter=limit=0.84"])
vfin = os.path.join(R, "voice_v7.wav")
run(["-i", vraw, "-af", post, "-ar", str(SR), "-ac", "2", vfin])

v6 = os.path.join(H, "EP01_Mikroplastik_v7b_watermark.mp4"); base = os.path.join(H, "base_v6.mp4")
out = os.path.join(H, "EP01_Mikroplastik_v8c_tanpa_pop.mp4")
run(["-i", v6, "-i", base, "-i", vfin, "-filter_complex",
     "[1:a]volume=0:enable='between(t,3.2,8.3)',volume=0.1:enable='between(t,8.3,13.85)',volume=0.8[bg];[bg][2:a]amix=inputs=2:normalize=0:duration=first,volume=-1.3dB,alimiter=limit=0.89[a]",
     "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-ar", "48000", "-b:a", "320k", "-movflags", "+faststart", out])
print(out)
