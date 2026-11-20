# VIDEO_3D — video grafik 3D Momyizz

Video motion grafik dengan elemen 3D (three.js), dirender terus ke MP4 tanpa rakaman.
Gaya ikut `TEMPLATES/MOTION_GRAPHICS_KIT/` (palet, font, safe zone) dan peraturan `AMWAY_BRAND/BRAND.md`.

| Fail | Isi |
|---|---|
| `hari07-span.html` | Hari 7, span dapur (57 s): span lama → kajian 2017 → span baharu bertarikh → cairkan Dish Drops dalam botol picit 1:5 → besen berbuih → produk + CTA |
| `hari08-tidur.html` | Hari 8, 🔥 siri Tidur & Otak (44 s, tema malam): telefon podcast trending → sel otak 3D (ruang +60%, Xie et al. 2013, kajian haiwan) → cecair otak membawa sisa → bulan "tidur bukan sekadar rehat" (masih dikaji) → shake pisang BodyKey sebagai makan malam ringan → produk + CTA |
| `render.js` | Render HTML ke MP4 (1080×1920, 30 fps, H.264, audio senyap) |
| `fonts/`, `fonts_local.css` | Fredoka, Nunito, Caveat (Google Fonts, lesen OFL) disimpan setempat |

## Threads 10 saat (`threads10.html`)
Templat video produk 10 saat untuk post Threads (video + 1 gambar): gambar produk asli atas podium 3D, hook ikut topik hari, 3 key selling, CTA "Klik LINK di Bio" + penafian, tanda nama `@empayarbiz_momyizz`.
Data dijana oleh `KALENDAR_PENULISAN/bina.py` ke `threads10_data.js` dari `KALENDAR_PENULISAN/threads_data.py` (hook, key selling `CHIPS`, gambar `GAMBAR_PRODUK`).
```bash
BITRATE=5M MAXRATE=6M node VIDEO_3D/render.js "threads10.html?h=17" 10 VIDEO_3D/threads/hari17.mp4   # MP4 diabaikan .gitignore: hantar kepada pengguna; simpan poster JPG sahaja
(cd VIDEO_3D && SNAP=5.8 node render.js "threads10.html?h=17")   # poster: snap_5.8.png -> threads/hari17.jpg
python3 KALENDAR_PENULISAN/bina.py   # pautan muat turun muncul dalam worksheet
```
Satu video 10 s ambil lebih kurang 1–2 minit; fail sekitar 5 MB.

## Cara render
```bash
cd VIDEO_3D && npm install && cd ..          # sekali sahaja (three.js)
node VIDEO_3D/render.js hari07-span.html 57 hari07-span.mp4
SNAP=15,37,55 node VIDEO_3D/render.js hari07-span.html   # semak beberapa bingkai sahaja (snap_*.png)
```
Perlu: Node, Playwright + Chromium, ffmpeg, python3. Render 57 s ambil lebih kurang 6 minit.

## Peraturan (wajib)
- Produk guna **gambar asli** dari `AMWAY_BRAND/PRODUK/` (boleh berpusing / bergerak, jangan dilukis semula). Alat seperti botol picit boleh dibina 3D.
- Nama produk / jenama **tidak** ditulis dalam teks atas skrin. Key selling dari `AMWAY_BRAND/KEY_SELLING.md` sahaja.
- Fakta ada sumber + label bukti. Penafian "Perkongsian ilmu umum. Bukan nasihat perubatan." sekurang-kurangnya 3 s. CTA "Nak dapatkan produk? Klik LINK di Bio".
- **Tanda nama `@empayarbiz_momyizz` WAJIB** sepanjang video (elemen `#wm`, penjuru kanan atas). Jangan buang bila salin templat.
- Semua teks, sticker, CTA dalam safe zone (x 60–940, y 160–1440).
- Tiada muzik dalam fail: tambah lagu dalam TikTok / Reels atau voiceover dalam CapCut.

## Templat untuk hari lain
Salin `hari07-span.html`. Masa setiap elemen ditetapkan dalam `window.renderAt(t)` (t dalam saat): `show(id, t, mula, tamat)` untuk teks DOM, dan kedudukan objek 3D dikira terus dari `t`, jadi render sentiasa sama setiap kali.
