# -*- coding: utf-8 -*-
"""Blok Threads harian: 1 video 10 saat + 1 gambar dalam satu post.

Untuk setiap hari (9-30; Hari 1-8 sudah dipost):
  hook   : teks pendek atas skrin video 3D (tanpa nama produk)
  rakam  : idea video 10 saat jika rakam sendiri (produk sedang digunakan, close-up, bunyi asli)
  gambar : idea 1 gambar untuk dipasangkan
  teks   : teks harian yang dijadikan kapsyen Threads (0 = 10:00, 1 = 16:00, 2 = 18:30, 3 = 21:00)

Video 3D: VIDEO_3D/threads10.html (gambar produk asli + 3 key selling + CTA + penafian), render:
  node VIDEO_3D/render.js "threads10.html?h=10" 10 VIDEO_3D/threads/hari10.mp4
Peraturan: botol & jenama boleh kelihatan; nama produk TIDAK ditulis / disebut. Key selling dari KEY_SELLING.md.
"""

# 3 key selling ringkas setiap produk (disalin daripada PRODUK / AMWAY_BRAND/KEY_SELLING.md, tanpa nama produk)
CHIPS = {
 "bodykey": ["17g protein tumbuhan", "Hanya 6g gula, GI rendah", "Siap dalam 1 minit"],
 "dish": ["Sangat pekat", "Sikit je, buih banyak", "Ada aloe vera"],
 "espring": ["4 standard NSF/ANSI", "Kurangkan 170+ bahan cemar", "UV-C LED"],
 "soy": ["8g protein tumbuhan", "Bebas laktosa", "Tanpa pemanis tiruan"],
 "bioc": ["500mg vitamin C", "Dari ceri acerola", "1 tablet sehari"],
 "cleanser": ["Buang kekotoran & PM2.5", "Tak keringkan kulit", "pH seimbang"],
 "uv": ["SPF50+ / PA++++", "Spektrum luas", "Ringan, tak berminyak"],
 "omega": ["330mg omega-3 sebiji", "Salmon, bilis & sardin", "1 biji sehari"],
 "probiotik": ["6.3 bilion bakteria baik", "5 strain probiotik", "1 paket sehari"],
 "fos": ["2 serat larut prebiotik", "+ grape ferment", "Rasa sedap"],
}

GAMBAR_PRODUK = {
 "bodykey": "AMWAY_BRAND/PRODUK/bodykey-nutritious-meal-shake-banana.png",
 "dish": "AMWAY_BRAND/PRODUK/dish-drops-1l.png",
 "espring": "AMWAY_BRAND/PRODUK/espring-baharu.png",
 "soy": "AMWAY_BRAND/PRODUK/soy-protein-drink-450g.png",
 "bioc": "AMWAY_BRAND/PRODUK/bio-c-plus-60tab.png",
 "cleanser": "AMWAY_BRAND/PRODUK/artistry-balancing-jelly-cleanser.png",
 "uv": "AMWAY_BRAND/PRODUK/artistry-uv-protect-spf50.png",
 "omega": "AMWAY_BRAND/PRODUK/salmon-omega-complex.png",
}

THREADS = {
 9: ("Papan pemotong berminyak? 🔪", "Picit setitik sabun pekat atas span → gosok papan pemotong → buih banyak. Bunyi gosokan & air paip.", "Papan pemotong berdiri kering di rak, sinki bersih", 2),
 10: ("Malam lapar, nak yang ringan? 🌙", "Tuang 1 paket shake + air ke dalam botol → goncang → tuang ke gelas. Bunyi goncang.", "Meja malam: segelas shake + buku, lampu malap", 1),
 11: ("Lepas pegang ayam mentah… 🍗", "Basuh tangan & sinki: setitik sabun pekat, buih naik. Close-up tangan.", "Sinki & papan pemotong bersih, span bertarikh", 2),
 12: ("Tak nak beratur microwave? 🍱", "Pagi kalut: masukkan paket shake & botol dalam beg kerja, zip.", "Meja kerja: pinggan kaca + botol shake", 1),
 13: ("Depan skrin seharian? 💻", "Sapu pelindung matahari di belakang tangan, close-up tekstur ringan.", "Botol pelindung matahari sebelah laptop, cahaya tingkap", 0),
 14: ("Hari kalut tiada bekal? 🎒", "Isi beg bertebat: bekas bekal + paket shake + botol air.", "Bekal seminggu tersusun dalam peti", 1),
 15: ("Rutin 1 minit sebelum tidur ✨", "Cuci muka: close-up jelly di tapak tangan → berbuih lembut.", "Dulang skincare kemas sebelah sinki", 2),
 16: ("Label jelas, tanpa janji kosong 🔍", "Pusing kotak shake, zoom ke label nutrisi (6g gula, 17g protein).", "Kotak shake + nota 'baca label' tulisan tangan", 2),
 17: ("Botol air tak berusik lagi? 💧", "Isi gelas dari penapis air di dapur, slow-motion air jernih.", "Botol bertanda masa (10 pg, 12 tgh, 3 ptg)", 1),
 18: ("Bangun nap, terus segelas air 💧", "Tuang air dari penapis ke gelas, minum. Bunyi air.", "Gelas air + penggera 20 minit di telefon", 2),
 19: ("Cabaran air hari ke-? ✅", "Isi botol pagi dari penapis + tanda ✓ pada kertas cabaran.", "Kertas cabaran 7 hari ditampal di peti", 1),
 20: ("Pukul 4 petang, bukan kopi ☕➜🍌", "Tolak cawan kopi ke tepi, goncang shake dalam botol.", "Cawan kopi pagi vs botol shake petang", 2),
 21: ("Makan sihat tapi tak bermaya? 🍽️", "Tuang 1 paket shake + air dalam botol, goncang, tuang ke gelas sebelah pinggan sayur.", "Pinggan sayur, kekacang & gelas shake, pandangan atas", 2),
 22: ("Tak sempat makan sayur hari ni? 🥦", "Goncang shake, tuang ke gelas sebelah pinggan sayur.", "Pinggan sayur + gelas shake, pandangan atas", 1),
 23: ("Probiotik vs prebiotik? 🦠", "Tuang 1 paket probiotik terus atas lidah / dalam yogurt sejuk, close-up.", "Tempe, yogurt, pisang & paket probiotik di meja", 1),
 24: ("Sarapan otak, versi 1 minit 🧠", "Telur rebus atas meja + goncang shake, tuang ke gelas.", "Sarapan: telur, roti gandum, gelas shake", 1),
 25: ("30 jenis tumbuhan seminggu? 🌿", "Susun sayur, kekacang, rempah di meja, kira dengan jari; tabur serbuk serat dalam air.", "Senarai 30 tumbuhan di peti + bekas kekacang", 1),
 26: ("'Leaky gut' viral? 🧱", "Close-up pinggan serat + segelas air + paket probiotik, tangan tanda ✓ senarai amalan.", "Nota tulisan tangan: 5 amalan usus", 2),
 27: ("Keluarga jarang makan ikan? 🐟", "Ikan kembung di kuali + botol omega di meja makan.", "Hidangan ikan keluarga + botol omega", 1),
 28: ("Protein mesra usus 🫘", "Tempe garing di kuali, kemudian goncang minuman protein soya.", "Pinggan tempe, dal & sayur + botol minuman soya", 2),
 29: ("Tabiat sihat yang kekal 💛", "Susun 3 tabiat: botol air, kasut sukan, shake pagi.", "Senarai 3 tabiat tulisan tangan + shake", 1),
 30: ("Sebulan bersama korang 💛", "Buka kotak shake bulan depan, susun paket dalam bekas.", "Kalendar bulan baharu + kotak shake", 1),
}
