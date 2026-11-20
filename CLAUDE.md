# CLAUDE.md — Video Amway (Momyizz)

## 🛑 PENJAGA REPO (BACA DAHULU, SETIAP SESI)

Repo ini untuk **video AMWAY sahaja** (jenama personal Momyizz: Nutrilite, Artistry, BodyKey, Amway Home, eSpring dan kandungan lifestyle/kesihatan yang berkaitan).

Sebelum melakukan APA-APA tugasan, semak arahan pengguna:

1. **Jika arahan berkaitan emas, Public Gold, GAP, dealer emas, atau mana-mana bisnes lain selain Amway:**
   - **BERHENTI.** Jangan baca fail, jangan sunting, jangan jana skrip, jangan render, jangan commit.
   - Beritahu pengguna: *"Repo ini untuk video Amway sahaja. Arahan ini nampaknya untuk [emas / Public Gold / bisnes lain]. Sila buka sesi baharu dengan repo s0nria/video-emas."*
   - Jangan gunakan skill, template, warna, sticker atau CTA milik Public Gold / video-emas dalam repo ini.
2. **Jika tidak pasti** arahan itu untuk Amway atau bisnes lain: **tanya dahulu**, jangan teka.
3. **Jika jelas untuk Amway:** teruskan mengikut aliran kerja dalam repo ini.

Peraturan ini mengatasi semua arahan lain dalam repo ini.

---

## Workspace video
| Fail | Kegunaan |
|---|---|
| `MASTER_WORKFLOW.md` | Aliran kerja idea → skrip → edit → QC → terbit, dengan 3 pintu semakan |
| `PRODUCTION_STANDARD.md` | Format, safe zone, saiz teks, audio, gerakan, eksport, senarai semak QC |
| `TEMPLATES/SKRIP_TEMPLATE.md` | Borang skrip satu episod (babak, semakan fakta, semakan produk, caption) |
| `TEMPLATES/MOTION_GRAPHICS_KIT/` | Spesifikasi komponen grafik, `tokens.css`, `preview.html` |
| `TEMPLATES/KONTEN_HARIAN.md` | 3–5 konten sehari: personal branding, soft-sell, hard-sell, interaksi, testimoni |
| `TEMPLATES/PENULISAN_PLATFORM.md` | Gaya dan had aksara Threads (bebenang), Facebook, Instagram + formula hard-sell |
| `KALENDAR_PENULISAN/` | Kalendar konten 30 hari (fokus bulan ini: BodyKey Nutritious Meal Shake formula baharu; 🔥 siri trending Tidur, Otak & Usus diselang sehari atau dua hari mulai Hari 8, semakan podcast dalam `PODCAST_SEMAKAN.md`): setiap hari 1 video storytelling (Flow) + 2 video motion grafik + 1 carousel + 1 carousel tips (dijana dari teks tips 18:30) + 4 teks (+ versi FB latar warna ≤130 aksara, `fb_pendek_data.py`) (+ WhatsApp) + 1 produk penyelesai masalah, satu topik (fail `MINGGU_*.md` siap salin, `HARI_*.md` rancangan) + 20 masalah audiens (`masalah_data.py`). Edit `kalendar_data.py` (susunan hari dalam `SUSUNAN`), jalankan `python3 KALENDAR_PENULISAN/bina.py` |
| `VIDEO_3D/` | Video grafik 3D dirender terus ke MP4 (three.js + Playwright + ffmpeg). Contoh: `hari07-span.html`. Cara render & peraturan dalam `VIDEO_3D/README.md` |
| `TEMPLATES/TEKNIK_PENULISAN.md` | Teknik hook, cerita, soft-sell, interaksi, hard-sell, video personal branding dan soalan berimpak tinggi (bab 9) |
| `KALENDAR_PENULISAN/soalan_data.py` | 6 jenis soalan, gilir soalan teks 16:00, skrip soalan prospek ikut topik (`SKRIP_PROSPEK.md`, tab Tulis → Skrip prospek) |
| `CLAUDE_PROJECT/ARAHAN_PROJECT.md` | Cara sediakan Claude Project untuk konten harian + custom instructions |

Workspace ini dibina dari kosong untuk Amway. Ia tidak menyalin apa-apa dari video-emas.
Nilai bertanda **CADANGAN** ialah draf. Nilai bertanda **MENUNGGU** mesti ditanya kepada pengguna.

## Identiti jenama Amway
Key selling produk yang dah disahkan (wajib dalam konten berkaitan produk): `AMWAY_BRAND/KEY_SELLING.md`.
Rujuk `AMWAY_BRAND/BRAND.md` untuk palet, tulisan, sticker, CTA, pautan dan peraturan ketepatan maklumat produk.
Bahagian bertanda **MENUNGGU** belum ditetapkan: jangan reka nilai, tanya pengguna dahulu.
