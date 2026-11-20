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
- **Cover hook 1 saat WAJIB** di depan setiap video: bina dalam `covers/cover-hariNN.html`, jana PNG dengan `node VIDEO_3D/covers/shot.js cover-hariNN.html`, kemudian sambung ke depan MP4 (lihat bahagian "Cover hook" di bawah).
- **Tanda nama `@empayarbiz_momyizz` WAJIB** sepanjang video (elemen `#wm`, penjuru kanan atas). Jangan buang bila salin templat.
- Semua teks, sticker, CTA dalam safe zone (x 60–940, y 160–1440).
- Tiada muzik dalam fail: tambah lagu dalam TikTok / Reels atau voiceover dalam CapCut.

## Templat untuk hari lain
Salin `hari07-span.html`. Masa setiap elemen ditetapkan dalam `window.renderAt(t)` (t dalam saat): `show(id, t, mula, tamat)` untuk teks DOM, dan kedudukan objek 3D dikira terus dari `t`, jadi render sentiasa sama setiap kali.

## Cover hook 1 saat (wajib)
1. Salin `covers/cover-hari08.html` → `covers/cover-hariNN.html`, tukar kicker, tajuk, visual dan tag.
   Visual 3D yang bersih boleh diambil dari templat video (sembunyikan `#fg`, contoh `window.NOZ` dalam `hari08-tidur.html`).
2. `node VIDEO_3D/covers/shot.js cover-hariNN.html` → `covers/cover-hariNN.png`
3. Sambung ke depan video (tiada render 3D semula):
```bash
ffmpeg -loop 1 -t 1 -framerate 30 -i VIDEO_3D/covers/cover-hariNN.png -i video.mp4 \
  -filter_complex "[0:v]fps=30,setsar=1,format=yuv420p[c];[1:v]fps=30,setsar=1,format=yuv420p[m];[c][m]concat=n=2:v=1:a=0[v]" \
  -map "[v]" -c:v libx264 -b:v 13M -pix_fmt yuv420p -movflags +faststart video-dengan-cover.mp4
```
4. Lagu (jika ada) mesti sepanjang video baharu (+1 s). Pilih bingkai pertama sebagai thumbnail semasa upload.

| Cover | Video |
|---|---|
| `covers/cover-hari07.html` | Hari 7, span dapur: "Bila kali terakhir korang tukar span?" |
| `covers/cover-hari08.html` | Hari 8, tidur & otak: "Otak ada 'syif cuci' masa kita tidur" |
