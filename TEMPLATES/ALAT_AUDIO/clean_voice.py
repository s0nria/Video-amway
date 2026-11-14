"""Pembersihan suara standard Momyizz: noise gating spektrum (profil dari ruang senyap) + rantai ffmpeg.
Guna: python3 -I clean_voice.py input.wav output.wav [noise_start noise_end]"""
import sys, subprocess, wave, numpy as np, noisereduce as nr

src, dst = sys.argv[1], sys.argv[2]
tmp_in = dst + ".in.wav"; tmp_nr = dst + ".nr.wav"
SR = 48000
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", src, "-ac", "1", "-ar", str(SR), "-sample_fmt", "s16", tmp_in], check=True)
w = wave.open(tmp_in); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768

def rms_db(a): return 20 * np.log10(np.sqrt((a ** 2).mean()) + 1e-9)
if len(sys.argv) >= 5:
    ns, ne = float(sys.argv[3]), float(sys.argv[4]); noise = x[int(ns * SR):int(ne * SR)]
else:  # cari 15% bingkai paling senyap (bukan senyap digital) sebagai profil bising
    f = int(0.05 * SR); fr = x[:len(x) // f * f].reshape(-1, f); e = (fr ** 2).mean(1)
    live = e > 1e-7                                   # abaikan senyap digital (< -70 dBFS)
    noise = fr[live & (e <= np.quantile(e[live], 0.15))].ravel()
print(f"bising asal: {rms_db(noise):.1f} dBFS")
y = nr.reduce_noise(y=x, sr=SR, y_noise=noise, stationary=True, prop_decrease=0.9, n_fft=2048)
w2 = wave.open(tmp_nr, "wb"); w2.setnchannels(1); w2.setsampwidth(2); w2.setframerate(SR)
w2.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes()); w2.close()

chain = ",".join([
    "highpass=f=90", "lowpass=f=3900",
    "afftdn=nf=-45:nr=8:tn=1",                       # sisa bising
    "agate=threshold=0.012:ratio=3:attack=3:release=120:range=0.06",  # senyapkan celah antara perkataan
    "equalizer=f=250:t=q:w=1.2:g=-3",                # kurangkan bunyi 'berdengung'
    "equalizer=f=2600:t=q:w=1.0:g=3",                # kejelasan sebutan
    "deesser=i=0.4",
    "acompressor=threshold=-20dB:ratio=3:attack=5:release=90:makeup=2",
    "loudnorm=I=-14:TP=-1.5:LRA=7",
])
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", tmp_nr, "-af", chain, "-ar", str(SR), "-ac", "2", dst], check=True)
for p in (tmp_in, tmp_nr):
    import os; os.remove(p)
print("siap:", dst)
