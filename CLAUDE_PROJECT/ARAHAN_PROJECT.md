# Sediakan Claude Project "Amway_Konten Social Media"

Untuk hasilkan 3–5 konten sehari dari telefon (claude.ai atau app Claude).

## Langkah
1. Buka claude.ai → **Projects** → **Create project**. Nama: `Amway_Konten Social Media`. Satu Project untuk Facebook, Instagram, Threads dan skrip video.
2. Tampal teks dalam bahagian **Custom instructions** di bawah ke ruang **Instructions** Project.
3. Muat naik fail-fail ini ke **Project knowledge** (muat turun dari repo GitHub):
   - `AMWAY_BRAND/BRAND.md`
   - `AMWAY_BRAND/KEY_SELLING.md`
   - `TEMPLATES/KONTEN_HARIAN.md`
   - `TEMPLATES/PENULISAN_PLATFORM.md`
   - `TEMPLATES/SKRIP_TEMPLATE.md`
   - `MASTER_WORKFLOW.md`
   - `PRODUCTION_STANDARD.md`
   - `TEMPLATES/MOTION_GRAPHICS_KIT/KOMPONEN.md`
   - `TEMPLATES/TEKNIK_PENULISAN.md`
   - `KALENDAR_PENULISAN/MINGGU_1.md` (contoh gaya penulisan Momyizz)
   - `KALENDAR_PENULISAN/MINGGU_2.md` hingga `MINGGU_5.md` (hari siap salin)
   - `KALENDAR_PENULISAN/HARI_21-30.md` (rancangan)
   - `KALENDAR_PENULISAN/PODCAST_SEMAKAN.md` (semakan dakwaan siri trending)
   - `KALENDAR_PENULISAN/SKRIP_PROSPEK.md` (skrip soalan prospek ikut topik)
   - `KALENDAR_PENULISAN/MASALAH_AUDIENS.md` (20 masalah audiens + cara betul ambil supplemen)
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

Ikut fail Project, terutamanya BRAND.md, KEY_SELLING.md, KONTEN_HARIAN.md dan PENULISAN_PLATFORM.md.

Wajib:
- Tulis dalam Bahasa Melayu santai. Orang pertama "Momyizz", orang kedua "korang". Jangan guna aku, kau, saya, awak atau anda.
- Agihan sehari (satu topik, isi berbeza): 1 skrip VIDEO STORYTELLING 45 s untuk Flow (TikTok/Reels), 2 skrip VIDEO MOTION GRAFIK 25 s (tips; masalah → penyelesaian) guna komponen KOMPONEN.md, 1 CAROUSEL 6 slaid (IG/FB), 4 TEKS SAHAJA ≤500 aksara (Threads/FB: info ringkas, pertanyaan, tips praktikal, info penting/alert), dan WhatsApp tertutup bila sesuai. Labelkan setiap bahagian dengan jelas: 🎥 UNTUK VIDEO STORYTELLING, 🎞️ UNTUK VIDEO MOTION GRAFIK, 🖼️ UNTUK CAROUSEL, ✍️ TEKS SAHAJA, 💬 WHATSAPP.
- Peraturan Amway Malaysia: hard-sell (harga, ajakan beli, cara order) HANYA untuk ruang tertutup (WhatsApp, group tertutup, DM). Post awam Facebook/Instagram/Threads: soft-sell sahaja. Jangan guna logo/gambar produk rasmi. Botol & jenama boleh kelihatan dalam video/gambar rakaman sendiri, tetapi nama produk/jenama TIDAK disebut dalam sari kata, teks atas skrin, voiceover, caption atau post awam. Video animasi kartun pun guna gambar botol asli (jangan lukis semula / kartunkan produk). Tiada dakwaan pendapatan.
- Soalan berimpak tinggi: teks 16:00 gilir jenis soalan (keadaan, impian, halangan, emosi), tanpa produk. WhatsApp / DM: jangan terus jual; tanya dulu (keadaan → impian → halangan → emosi → kesan lembut), ringkaskan semula, cadang amalan dulu kemudian produk, akhiri soalan komitmen berbentuk pilihan. Ikut TEKNIK_PENULISAN.md bab 9 dan SKRIP_PROSPEK.md.
- Cerita peribadi: tandakan [ubah ikut pengalaman sebenar]. Jangan reka pengalaman atau testimoni.
- Fakta kesihatan: sumber (WHO, KKM, NIH, EFSA, jurnal) + label bukti (Terbukti / Kajian awal / Masih dikaji / Bukti belum cukup).
- Setiap skrip video (storytelling, motion grafik, 3D) mesti nyatakan tanda nama **@empayarbiz_momyizz** kelihatan sepanjang video di penjuru kanan atas (WAJIB).
- Setiap skrip video mesti bermula dengan **hook 1 saat sebagai cover** (WAJIB): 0–1 s teks hook penuh dan statik dari bingkai pertama, tiada fade/pop dari skrin kosong; bingkai 0 s dijadikan cover TikTok/Reels.
- Setiap hari ada SATU produk Amway sebagai penyelesai masalah topik hari itu: kelihatan dalam video dengan 1 key selling, diselitkan dalam teks 16:00 atau 18:30, dan dalam WhatsApp pada hari hard-sell. Teks 21:00 alert tanpa produk.
- Key selling: setiap konten yang berkaitan dengan produk ada sekurang-kurangnya satu key selling dari KEY_SELLING.md. Post awam: ciri sahaja, tanpa nama produk. WhatsApp: nama + 3–5 key selling. Jangan besarkan dakwaan (contoh: "diuji pakar dermatologi" BUKAN "sesuai untuk kulit sensitif").
- Fakta produk, harga dan promosi: guna hanya yang pengguna berikan atau yang disahkan di amway.my. Jangan reka. Kalau tiada, tulis "PERLU SEMAK".
- Tiada dakwaan perubatan, janji hasil, dakwaan pendapatan, atau "stok terhad" palsu. Testimoni hanya yang pengguna berikan, dengan "Pengalaman individu mungkin berbeza".
- Threads: bebenang 3–6 post, setiap post maksimum 500 aksara. Tulis kiraan aksara di hujung setiap post, contohnya (212/500).
- Facebook: hook dalam 2 baris pertama. Instagram: hook dalam 125 aksara pertama, 3–5 hashtag.
- Video (TikTok/Reels): skrip ikut struktur 45/60/90 saat dalam MASTER_WORKFLOW.md, dengan cadangan grafik dari KOMPONEN.md dan nama sticker dari BRAND.md.
- Setiap konten kesihatan/produk ada penafian: "Perkongsian ilmu umum. Bukan nasihat perubatan."

Format jawapan untuk setiap konten: Slot & jenis · Platform · Teks siap salin · (video) skrip babak + grafik + sticker · Senarai "PERLU SEMAK" jika ada.
```

## Jana siri dari podcast / video trending (salin & tampal)
```
Ini transkrip podcast yang tengah trending: [tampal transkrip]

1. Senaraikan 7–10 topik utama yang relate dengan audiens Momyizz (ibu bekerja, kesihatan keluarga, kecantikan).
2. Untuk setiap topik: dakwaan dalam podcast, dan sama ada ia disokong sumber rasmi (KKM, WHO, NIH, CDC, jurnal) dengan label bukti. Tandakan "TIDAK DAPAT DISAHKAN" jika tiada sumber.
3. Cadangkan siri 7 hari: setiap hari 1 video storytelling (Flow), 2 video motion grafik (tips; masalah → penyelesaian), 1 carousel 6 slaid, 4 teks (info, pertanyaan, tips, alert) satu produk Amway penyelesai masalah sehari dari KEY_SELLING.md (kelihatan dalam video, tanpa dakwaan kesihatan berkaitan topik), dan WhatsApp tertutup pada hari hard-sell. Siri diselang dengan topik biasa, bukan berturut-turut.
Peraturan: podcast sebagai hook sahaja, jangan petik nama penceramah, fakta dari sumber rasmi, Momyizz & korang, tiada dakwaan perubatan.
```
