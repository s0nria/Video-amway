import sys, json
from faster_whisper import WhisperModel
import wave, numpy as np
w = wave.open(sys.argv[1]); audio = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
m = WhisperModel(sys.argv[2], device="cpu", compute_type="int8")
segs, info = m.transcribe(audio, language="ms", word_timestamps=True, vad_filter=False, beam_size=5,
    initial_prompt="Kak Ana, sarapan ibu, Nutrilite Soy Protein Drink, Pinggan Sihat Malaysia, KKM.")
out = []
for s in segs:
    print(f"{s.start:6.2f}-{s.end:6.2f} {s.text}", flush=True)
    out.append({"start": s.start, "end": s.end, "text": s.text,
                "words": [{"w": w.word, "s": w.start, "e": w.end} for w in s.words]})
json.dump(out, open(sys.argv[3], "w"), ensure_ascii=False, indent=1)
