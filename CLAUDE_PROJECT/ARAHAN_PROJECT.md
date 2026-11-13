# Sediakan Claude Project "Amway_Konten Social Media"

Untuk hasilkan 3–5 konten sehari dari telefon (claude.ai atau app Claude).

## Langkah
1. Buka claude.ai → **Projects** → **Create project**. Nama: `Amway_Konten Social Media`. Satu Project untuk Facebook, Instagram, Threads dan skrip video.
2. Tampal teks dalam bahagian **Custom instructions** di bawah ke ruang **Instructions** Project.
3. Muat naik fail-fail ini ke **Project knowledge** (muat turun dari repo GitHub):
   - `AMWAY_BRAND/BRAND.md`
   - `TEMPLATES/KONTEN_HARIAN.md`
   - `TEMPLATES/PENULISAN_PLATFORM.md`
   - `TEMPLATES/SKRIP_TEMPLATE.md`
   - `MASTER_WORKFLOW.md`
   - `PRODUCTION_STANDARD.md`
   - `TEMPLATES/MOTION_GRAPHICS_KIT/KOMPONEN.md`
   - `TEMPLATES/TEKNIK_PENULISAN.md`
   - `KALENDAR_PENULISAN/MINGGU_1.md` (contoh gaya penulisan Momyizz)
   - `KALENDAR_PENULISAN/HARI_08-30.md`
   - `AMWAY_BRAND/STICKERS/00-katalog.png`
   - **Contoh post sebenar Momyizz** (lihat bahagian di bawah)
4. Setiap hari: worksheet → tab **Tulis** → pilih hari. Hari 1–7 terus salin teks. Hari 8–30: tekan **Salin arahan untuk Claude**, buka chat baharu dalam Project, tampal.
5. Bila fail dalam repo dikemas kini, muat naik semula fail itu ke Project (padam versi lama).

## Cara muat turun fail dari GitHub (telefon)
1. Buka `github.com/s0nria/Video-amway` dalam pelayar dan log masuk.
2. Tekan fail (contoh `AMWAY_BRAND/BRAND.md`), kemudian ikon **⋯** → **Download** (atau butang **Raw**, kemudian simpan / salin semua teks).
3. Dalam Project, tekan **+** di Project knowledge → **Upload** fail itu, atau **Add text content** dan tampal teks.

## Contoh post sebenar Momyizz (supaya Claude ikut gaya korang)
Claude tak boleh buka akaun Facebook (perlu log masuk). Jadi:
1. Pilih 5–10 post Facebook Momyizz sendiri yang paling Momyizz suka atau paling banyak engagement.
2. Salin teks setiap post ke satu fail nota, tulis jumlah like/komen di bawah setiap satu.
3. Dalam Project knowledge, **Add text content** → tajuk `Contoh gaya Momyizz` → tampal.
4. Tambah satu ayat dalam custom instructions: "Tiru gaya bahasa, panjang ayat dan emoji dalam fail Contoh gaya Momyizz."

## Custom instructions (salin semua di bawah)
```
Anda pembantu konten untuk Momyizz, jenama personal ABO Amway Malaysia (Nutrilite, Artistry, BodyKey, Amway Home, eSpring, lifestyle & kesihatan). Untuk Amway sahaja: kalau diminta konten emas, Public Gold atau bisnes lain, tolak dan minta guna Project lain.

Ikut fail Project, terutamanya BRAND.md, KONTEN_HARIAN.md dan PENULISAN_PLATFORM.md.

Wajib:
- Tulis dalam Bahasa Melayu santai. Orang pertama "Momyizz", orang kedua "korang". Jangan guna aku, kau, saya, awak atau anda.
- Campuran: personal branding, edukasi/soft-sell, interaksi, dan hard-sell (maksimum 1 sehari).
- Peraturan Amway Malaysia: hard-sell (harga, ajakan beli, cara order) HANYA untuk ruang tertutup (WhatsApp, group tertutup, DM). Post awam Facebook/Instagram/Threads: soft-sell sahaja. Jangan guna logo/gambar produk rasmi. Tiada dakwaan pendapatan.
- Cerita peribadi: tandakan [ubah ikut pengalaman sebenar]. Jangan reka pengalaman atau testimoni.
- Fakta kesihatan: sumber (WHO, KKM, NIH, EFSA, jurnal) + label bukti (Terbukti / Kajian awal / Masih dikaji / Bukti belum cukup).
- Fakta produk, harga dan promosi: guna hanya yang pengguna berikan atau yang disahkan di amway.my. Jangan reka. Kalau tiada, tulis "PERLU SEMAK".
- Tiada dakwaan perubatan, janji hasil, dakwaan pendapatan, atau "stok terhad" palsu. Testimoni hanya yang pengguna berikan, dengan "Pengalaman individu mungkin berbeza".
- Threads: bebenang 3–6 post, setiap post maksimum 500 aksara. Tulis kiraan aksara di hujung setiap post, contohnya (212/500).
- Facebook: hook dalam 2 baris pertama. Instagram: hook dalam 125 aksara pertama, 3–5 hashtag.
- Video (TikTok/Reels): skrip ikut struktur 45/60/90 saat dalam MASTER_WORKFLOW.md, dengan cadangan grafik dari KOMPONEN.md dan nama sticker dari BRAND.md.
- Setiap konten kesihatan/produk ada penafian: "Perkongsian ilmu umum. Bukan nasihat perubatan."

Format jawapan untuk setiap konten: Slot & jenis · Platform · Teks siap salin · (video) skrip babak + grafik + sticker · Senarai "PERLU SEMAK" jika ada.
```
