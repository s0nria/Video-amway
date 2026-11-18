# -*- coding: utf-8 -*-
"""Sumber kalendar konten harian Momyizz (Amway).

Edit fail ini, kemudian jalankan:  python3 KALENDAR_PENULISAN/bina.py

Format setiap hari (DISAHKAN pengguna, pilihan A): SATU topik, isi berbeza untuk setiap konten.
  video     08:30  🎥 Untuk VIDEO (TikTok / Reels)   -> skrip babak + teks atas skrin + caption
  carousel  12:30  🖼️ Untuk CAROUSEL (Instagram / Facebook) -> teks setiap slaid + caption
  teks      4 post ✍️ TEKS SAHAJA (Threads / Facebook) -> salin & post terus (<= 500 aksara)
            10:00 Info ringkas · 16:00 Pertanyaan · 18:30 Tips praktikal · 21:00 Info penting / alert
  wa        💬 WhatsApp / group tertutup (hard-sell, bila sesuai)

Peraturan: Momyizz & korang sahaja. Produk BOLEH kelihatan dalam video / gambar carousel (botol & jenama,
rakaman sendiri; DISAHKAN pengguna 18 Nov 2026), tetapi nama produk / jenama TIDAK disebut dalam sari kata,
teks atas skrin, voiceover, caption atau teks awam
(peraturan Amway Malaysia: tiada tawaran produk di ruang awam; closing awam melalui "Klik LINK di Bio" sahaja.
Video: kebenaran upline ada; Amway tapis selepas post dan maklumkan upline jika perlu dibuang).
Produk + harga hanya dalam slot wa (ruang tertutup).

Key selling (DISAHKAN pengguna): setiap konten yang berkaitan dengan produk ada sekurang-kurangnya satu key selling
dari AMWAY_BRAND/KEY_SELLING.md. Awam: ciri sahaja, tanpa nama produk. WhatsApp: nama + 3-5 key selling.
"""

DISC = "Perkongsian ilmu umum. Bukan nasihat perubatan."
CERITA = "Cerita peribadi mesti benar. Ubah butiran ikut kehidupan sebenar Momyizz sebelum rakam."

# Produk penyelesai masalah (DISAHKAN pengguna 18 Nov 2026): setiap hari SATU produk.
# Muncul dalam video (kelihatan + 1 key selling), 16:00 atau 18:30, dan WhatsApp bila hari hard-sell.
# 21:00 alert dan konten bencana / saringan penyakit kekal tanpa produk. Key selling: AMWAY_BRAND/KEY_SELLING.md
PRODUK = {
 "bodykey": ("BodyKey by Nutrilite Nutritious Meal Shake TERBARU (hero: perisa pisang baharu; juga Chocolate, Café Latte, Berry)", "AMWAY_BRAND/PRODUK/bodykey-nutritious-meal-shake-banana.png · bodykey-banana-gaya-studio.jpg · bodykey-banana-gaya-beg.jpg",
             "meal replacement terbaru untuk SEMUA gaya hidup (sarapan / bekal / on-the-go, sedar gula, urus berat) · 17g protein tumbuhan (soya & chia) · 5g serat prebiotik · 20 vitamin & mineral · hanya 6g gula, GI rendah · siap 1 minit · ada susu & soya"),
 "espring": ("eSpring Water Purifier (model baharu)", "AMWAY_BRAND/PRODUK/espring-baharu.png",
             "4 standard NSF/ANSI · kurangkan 170+ bahan cemar · UV-C LED 99.9% bakteria & virus · terbukti kurangkan mikroplastik"),
 "soy": ("NUTRILITE Soy Protein Drink (Original 450g)", "AMWAY_BRAND/PRODUK/soy-protein-drink-450g.png",
         "protein tumbuhan · 8g protein, 9 asid amino perlu · bebas laktosa · tanpa pemanis & tanpa perisa tiruan"),
 "dish": ("Amway Home DISH DROPS (1L)", "AMWAY_BRAND/PRODUK/dish-drops-1l.png",
          "sangat pekat · sikit je buih banyak & tahan lama · aloe vera · diuji pakar dermatologi · biodegradable"),
 "bioc": ("NUTRILITE Bio C Plus All Day Formula", "AMWAY_BRAND/PRODUK/bio-c-plus-60tab.png",
          "500mg vitamin C · dari ceri acerola · 1 tablet sehari · tanpa pewarna & perisa tiruan"),
 "cleanser": ("ARTISTRY SKIN NUTRITION Balancing Jelly Cleanser (yang Momyizz guna sekarang)", "AMWAY_BRAND/PRODUK/artistry-balancing-jelly-cleanser.png",
              "buang pencemaran & kekotoran termasuk PM2.5 (terbukti klinikal) · Shiso Perilla & aloe vera · tidak menanggalkan minyak semula jadi & tidak mengeringkan · pH seimbang · vegan · JANGAN tulis 'untuk kulit kering' (rasmi: berminyak / normal ke berminyak)"),
 "uv": ("ARTISTRY SKIN NUTRITION Multi-Defense UV Protect SPF50+/PA++++", "AMWAY_BRAND/PRODUK/artistry-uv-protect-spf50.png",
        "SPF50+/PA++++ · spektrum luas · ringan, tak berminyak · sesuai semua jenis kulit"),
 "omega": ("NUTRILITE Salmon Omega Complex", "AMWAY_BRAND/PRODUK/salmon-omega-complex.png",
           "330.93mg omega-3 (EPA + DHA) sebiji · salmon, ikan bilis & sardin · 1 biji sehari"),
}

JENIS_TEKS = [("10:00", "Info ringkas"), ("16:00", "Pertanyaan"), ("18:30", "Tips praktikal"), ("21:00", "Info penting / alert")]

DAYS = [
# ================================================================ HARI 1
{"d": 1, "ep": 1, "tema": "Mikroplastik: fakta, bukan panik", "produk": ("espring", "Risau air minuman di rumah bila baca berita mikroplastik"),
 "video": {"tajuk": "Pagi-pagi isi botol air", "nota": CERITA + " Sticker: 14-blazer-tutup-mulut (babak hook).",
  "babak": [
   ("0–3s", "Close-up tangan isi air ke botol plastik lama yang calar", "Pernah fikir apa yang bersentuhan dengan air minuman kita? 🤔"),
   ("3–12s", "Momyizz bercakap ke kamera di dapur", "Semalam lalu FYP: 'Mikroplastik dalam air minuman!' Momyizz terus nak buang semua botol."),
   ("12–25s", "Momyizz duduk depan laptop, teh panas, malam", "Tapi Momyizz baca dulu laporan WHO. Rupanya ceritanya lebih tenang daripada yang viral."),
   ("25–38s", "Tangan isi botol keluli dari penapis air di dapur (eSpring kelihatan)", "Langkah Momyizz: air minuman di rumah ditapis dengan penapis yang ada pensijilan bebas. Fakta, bukan panik."),
   ("38–45s", "Momyizz senyum, tunjuk ke atas", "Siri Mikroplastik Momyizz 🌿 | Perkongsian ilmu umum. Bukan nasihat perubatan."),
  ],
  "caption": "Mikroplastik: fakta, bukan panik 🌿 Siri baharu Momyizz bermula hari ni. Follow supaya tak terlepas.\n\n#Momyizz #Mikroplastik #FaktaBukanPanik #IbuBekerja"},
 "carousel": {"tajuk": "Mikroplastik dalam 5 slaid",
  "slaid": [
   "MIKROPLASTIK\nApa sebenarnya? 🤔\n(Fakta, bukan panik)",
   "APA ITU?\nZarah plastik bersaiz kurang daripada 5 mm.\nNanoplastik lebih kecil lagi.\n🟢 Terbukti (WHO)",
   "DARI MANA?\n• Plastik besar yang terurai\n• Serat baju sintetik\n• Geseran tayar\n🟢 Terbukti (UNEP)",
   "DI MANA?\nDalam air, makanan dan persekitaran.\n🟢 Terbukti (WHO 2022)",
   "BAHAYA KE?\nKesan pada kesihatan manusia masih dikaji.\nWHO (2019): tahap semasa dalam air minuman belum tunjuk risiko jelas.\n🔵 Masih dikaji",
   "JADI?\nTak perlu panik.\nKurangkan pendedahan yang tak perlu.\nSave & follow siri ni 🌿\n\n" + DISC,
  ],
  "caption": "Mikroplastik dalam 5 slaid. Save untuk rujukan 🌿\n\nSumber: WHO (2019, 2022), UNEP.\n" + DISC + "\n\n#Momyizz #Mikroplastik #FaktaBukanPanik #KesihatanKeluarga"},
 "teks": [
  "Info ringkas: mikroplastik ialah zarah plastik yang lebih kecil daripada 5 mm. Lebih kecil daripada sebutir beras. 🍚\n\nIa datang dari plastik yang terurai, serat baju sintetik dan geseran tayar. (UNEP)",
  "Soalan jujur: botol air yang korang bawa hari-hari, jenis apa?\n\nA. Plastik\nB. Kaca\nC. Keluli tahan karat\nD. Beli air botol je\n\nMomyizz dulu A, sekarang tengah tukar ke C. 😄",
  "Tips pilih botol air guna semula 💡\n\n✅ Keluli tahan karat gred makanan atau kaca (dengan sarung silikon supaya tak mudah pecah)\n✅ Mulut botol lebar, senang dicuci\n✅ Basuh setiap hari dengan berus botol, keringkan terbuka\n✅ Isi dari air di rumah. Momyizz guna penapis yang diperakui 4 standard NSF/ANSI\n\nBotol yang mudah dicuci = botol yang betul-betul dipakai hari-hari. 😉",
  "Info penting: botol air plastik sekali guna direka untuk SEKALI guna. ⚠️\n\nJangan isi air panas ke dalamnya, dan jangan guna berulang kali sampai calar. Kajian tentang kesan haba pada pelepasan zarah masih awal, tapi langkah ni mudah dan tak rugi apa-apa. 🌿",
 ]},

# ================================================================ HARI 2
{"d": 2, "ep": 1, "tema": "3 langkah kecil kurangkan pendedahan plastik", "produk": ("espring", "Asyik beli air botol plastik; nak isi botol keluli dari rumah"),
 "video": {"tajuk": "3 benda kecil yang Momyizz ubah", "nota": CERITA + " Sticker: 18-blazer-semangat (babak akhir).",
  "babak": [
   ("0–3s", "Momyizz pegang beg sampah, berhenti, geleng kepala", "Tak perlu buang semua plastik esok pagi. 🙅‍♀️"),
   ("3–15s", "Tukar botol plastik calar ke botol keluli, isi dari penapis air di dapur (eSpring kelihatan)", "Satu: botol plastik dah calar? Tukar ke kaca atau keluli. Isi dari air yang ditapis di rumah."),
   ("15–27s", "Keluarkan botol air dari kereta yang panas", "Dua: jangan biar air botol lama-lama dalam kereta panas."),
   ("27–38s", "Bawa tumbler sendiri ke kedai air", "Tiga: bawa tumbler sendiri bila beli air."),
   ("38–45s", "Momyizz ke kamera, genggam tangan", "Kecil, tapi senang diulang. Itu yang jadi tabiat 💪 | " + DISC),
  ],
  "caption": "3 langkah kecil kurangkan plastik. Mana satu korang nak cuba dulu? 👇\n\n#Momyizz #Mikroplastik #TipsRumah #GayaHidupSihat"},
 "carousel": {"tajuk": "Plastik di rumah: tukar yang mana dulu?",
  "slaid": [
   "PLASTIK DI RUMAH\nTukar yang mana dulu? 🏠\n(Tak perlu tukar semua sekali gus)",
   "1. BOTOL AIR\nDah calar atau kusam? Tukar dulu.\nPilihan: kaca / keluli tahan karat.",
   "2. BEKAS MAKANAN\nRetak, melengkung atau berbau? Masa untuk tukar.",
   "3. PLASTIK SEKALI GUNA\nStraw, cawan, beg.\nKurangkan bila mudah: bawa tumbler & beg sendiri.",
   "4. YANG BOLEH TUNGGU\nBekas yang masih elok boleh terus guna untuk simpan barang kering.\nTak perlu membazir. ♻️",
   "INGAT\nTujuan: kurangkan pendedahan yang tak perlu, bukan takut.\nSave untuk rujukan 🌿\n\n" + DISC,
  ],
  "caption": "Senarai tukar plastik ikut keutamaan. Save & kongsi dengan keluarga 🌿\n\n" + DISC + "\n\n#Momyizz #Mikroplastik #RumahSihat #TipsRumah"},
 "teks": [
  "Info ringkas: perubahan yang bertahan biasanya yang kecil. 🌱\n\nMomyizz mula dengan satu je minggu ni: botol air keluli, isi dari penapis air di rumah, tak beli air botol lagi. Bila dah jadi tabiat, baru tambah langkah kedua.",
  "Soalan: dalam rumah korang, barang plastik apa yang paling banyak?\n\n🍱 Bekas makanan\n🧴 Botol\n🛍️ Beg plastik\n🥤 Cawan / straw\n\nMomyizz? Bekas makanan. Bertimbun dalam kabinet! 😅",
  "Tips jaga bekas plastik yang masih elok 💡\n\n✅ Basuh dengan span lembut, elak sabut kasar yang mencalarkan\n✅ Ikut label pengeluar untuk air panas, microwave dan mesin basuh pinggan\n✅ Simpan untuk barang kering bila dah tak sesuai untuk makanan panas\n✅ Retak, melengkung atau berbau? Masa untuk tukar",
  "Info penting musim tengkujuh: selepas banjir atau bila air paip keruh, didihkan air sebelum minum. 💧\n\nIni panduan asas kesihatan awam semasa banjir. Kongsi dengan keluarga di kawasan yang terjejas. 🙏",
 ],
 "wa": {"tajuk": "eSpring Water Purifier (model baharu)", "nota": "Ruang tertutup sahaja. Key selling dari AMWAY_BRAND/KEY_SELLING.md (amway.my 122940, semak 18 Nov 2026). Tulis MENGURANGKAN mikroplastik, jangan singkir / bebas. Gambar: AMWAY_BRAND/PRODUK/espring-baharu.png. Semak harga & promosi hari ini.",
  "t": "Hai [nama] 😊\n\nMinggu ni Momyizz kongsi pasal kurangkan plastik. Langkah pertama Momyizz: berhenti beli air botol, isi botol keluli dari penapis air di rumah. Ada yang tanya penapis apa.\n\nMomyizz guna *eSpring Water Purifier* (model baharu) dari Amway.\n• Diperakui 4 standard NSF/ANSI (42, 53, 55, 401)\n• Kurangkan lebih 170 bahan cemar, sekecil 0.2 mikron\n• Terbukti mengurangkan mikroplastik & 19 jenis sisa farmaseutikal\n• UV-C LED hapuskan 99.9% bakteria, virus & sista bawaan air\n• Aplikasi Amway Healthy Home ingatkan bila perlu tukar penapis\n• Halal, waranti 5 tahun\n• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n• Kenapa Momyizz pilih: [pengalaman sebenar Momyizz]\n\nKalau nak tahu lebih atau nak demo, reply \"NAK\", Momyizz uruskan. 💛"}},

# ================================================================ HARI 3
{"d": 3, "ep": 1, "tema": "Cara baca berita kesihatan viral", "produk": ("espring", "Susah percaya dakwaan produk; nak bukti pensijilan bebas"),
 "video": {"tajuk": "Kenapa Momyizz tak terus kongsi berita viral", "nota": CERITA + " Sticker: 04-satin-tutup-mulut atau 14-blazer-tutup-mulut.",
  "babak": [
   ("0–3s", "Skrin telefon: notifikasi group keluarga banyak", "Group keluarga dah kongsi lagi berita kesihatan viral… 📱"),
   ("3–15s", "Momyizz bercakap ke kamera", "Dulu Momyizz pernah forward satu tips viral. Rupanya salah. Malu sangat. 🙈"),
   ("15–30s", "Tangan tulis 3 soalan atas kertas", "Sekarang Momyizz tanya 3 soalan dulu: Siapa sumbernya? Ada kajian? Badan rasmi kata apa?"),
   ("30–40s", "Momyizz tunjuk label warna di skrin", "Sebab tu setiap post Momyizz ada label bukti: 🟢 🟠 🔵 🔴"),
   ("40–45s", "Momyizz senyum sebelah penapis air di dapur (eSpring kelihatan)", "Produk pun sama: Momyizz semak sijil bebasnya dulu. Fakta dulu, baru kongsi 💛 | " + DISC),
  ],
  "caption": "3 soalan sebelum forward berita kesihatan. Korang pernah termakan berita palsu? 👇\n\n#Momyizz #FaktaBukanPanik #BeritaPalsu"},
 "carousel": {"tajuk": "Label bukti Momyizz",
  "slaid": [
   "LABEL BUKTI MOMYIZZ\nCara faham setiap post 🔍",
   "🟢 TERBUKTI\nDisokong banyak kajian dan badan rasmi (WHO, KKM).",
   "🟠 KAJIAN AWAL\nAda kajian, tapi masih sedikit atau dalam makmal.",
   "🔵 MASIH DIKAJI\nSaintis belum ada jawapan muktamad.",
   "🔴 BUKTI BELUM CUKUP\nBelum boleh buat kesimpulan.",
   "KENAPA PENTING?\nSupaya korang tahu mana yang pasti dan mana yang belum.\nTak perlu percaya bulat-bulat, tak perlu panik. 🌿",
  ],
  "caption": "Save supaya senang faham post Momyizz akan datang 🔍\n\n#Momyizz #FaktaBukanPanik #LiterasiKesihatan"},
 "teks": [
  "Info ringkas: \"kajian makmal\" tak sama dengan \"terbukti pada manusia\". 🔬\n\nKajian sel atau haiwan ialah langkah awal. Banyak hasil makmal tak sama bila diuji pada manusia. Jadi bila baca tajuk viral, tengok dulu kajian jenis apa.",
  "Mitos atau fakta? 🤔\n\n\"Mikroplastik dah terbukti menyebabkan penyakit tertentu pada manusia.\"\n\nJawapan: MITOS. Kesan jangka panjang masih dikaji, belum ada bukti yang mengesahkan penyakit tertentu. (WHO 2022)\n\nBerapa ramai yang teka betul?",
  "Tips semak berita kesihatan dalam 30 saat 💡\n\n1️⃣ Cari nama kajian atau badan yang disebut. Tiada nama? Tanda merah.\n2️⃣ Taip tajuk berita + \"sebenarnya.my\" di Google.\n3️⃣ Tengok tarikh. Berita lama selalu diulang viral.\n4️⃣ Produk pun sama: cari pensijilan bebas (contoh NSF untuk penapis air), bukan testimoni je.\n\nSave untuk group keluarga! 📲",
  "Info penting: sebelum forward berita kesihatan, semak dulu di portal semakan fakta rasmi Malaysia, sebenarnya.my. ✅\n\nSatu forward yang salah boleh buat orang tersayang panik atau ambil keputusan kesihatan yang silap.",
 ]},

# ================================================================ HARI 4
{"d": 4, "ep": 2, "tema": "Sarapan ibu yang selalu tertinggal", "produk": ("bodykey", "Ibu skip sarapan; perlukan hidangan lengkap yang cepat"),
 "video": {"tajuk": "Semua dah makan, kecuali ibu", "nota": CERITA + " Sticker: 10-satin-terkejut-pipi (babak hook). Boleh juga guna video Episod 2 (tab Episod).",
  "babak": [
   ("0–3s", "Meja makan: pinggan anak dan suami dah licin, pinggan ibu kosong", "Anak dah makan. Suami dah makan. Ibu? \"Nanti la.\" 🙃"),
   ("3–15s", "Momyizz kalut cari kunci, capai roti sambil keluar", "Hampir setiap pagi Momyizz jadi orang terakhir. Kadang langsung tak makan."),
   ("15–28s", "Momyizz di meja kerja pukul 11, lapar, capai snek manis", "Pukul 11 dah lapar sangat. Capai apa yang ada."),
   ("28–40s", "Momyizz masukkan bekas ke dalam beg sekali dengan bekal anak; paket shake pisang & shaker di sebelah (BodyKey perisa pisang kelihatan)", "Minggu ni Momyizz cuba: siapkan bekal ibu sekali dengan bekal anak. Hari tak sempat? Shake pisang siap 1 minit: 17g protein tumbuhan + 20 vitamin & mineral. 🍌"),
   ("40–45s", "Momyizz ke kamera", "Ibu pun perlu diisi dulu 💛 Siapa sama? | " + DISC),
  ],
  "caption": "Ibu-ibu, korang pun selalu jadi orang terakhir makan? 🙋‍♀️\n\n#Momyizz #SarapanIbu #IbuBekerja #MomLife"},
 "carousel": {"tajuk": "Sarapan 5 minit ibu",
  "slaid": [
   "SARAPAN 5 MINIT IBU 🍳\nTak perlu mewah. Yang penting ada isi.",
   "IKUT PINGGAN SIHAT (KKM)\n¼ protein · ¼ bijirin penuh · ½ sayur & buah",
   "IDEA 1\nTelur rebus (rebus malam sebelumnya) + roti gandum penuh + pisang",
   "IDEA 2\nOat rendam semalaman dengan susu + buah potong",
   "IDEA 3\nRoti gandum + sardin / kekacang + segelas air kosong",
   "TIP\nSiapkan bekal ibu sekali dengan bekal anak.\nSave untuk minggu ni 💛\n\n" + DISC,
  ],
  "caption": "3 idea sarapan 5 minit untuk ibu. Mana satu korang pilih? 👇\n\nSumber: KKM, Garis Panduan Diet Malaysia 2020.\n" + DISC + "\n\n#Momyizz #SarapanSihat #PingganSihat #IbuBekerja"},
 "teks": [
  "Info ringkas: gabungan protein + karbohidrat kompleks + serat pada waktu pagi biasanya buat kita kenyang lebih lama, berbanding minuman manis sahaja. 🍳\n\nContoh: telur + roti gandum + buah.",
  "Ibu-ibu, jujur sikit: pagi tadi korang sarapan apa? 🙈\n\n☕ Kopi je\n🍞 Roti sambil drive\n🥣 Sarapan betul-betul\n🤐 Tak sempat langsung\n\nMomyizz: roti sambil drive. Esok cuba lagi!",
  "Tips pastikan ibu tak tertinggal sarapan 💡\n\n✅ Malam: letak bekas ibu SEBELAH bekas anak, terus nampak pagi esok\n✅ Simpan \"kotak snek sihat\" di pejabat: kacang, roti gandum, buah\n✅ Set peringatan telefon 10 pagi: \"Dah makan?\"\n✅ Hari kalut: paket shake dalam beg, campur 250ml air, siap 1 minit (17g protein, 20 vitamin & mineral)\n\nKecil, tapi berkesan untuk Momyizz. 💛",
  "Info penting: 15.6% dewasa Malaysia ada diabetes, dan ramai tak tahu mereka menghidapnya (NHMS 2023). ⚠️\n\nKalau selalu skip makan dan banyak minum manis, buat saringan gula di klinik kesihatan. Tahu awal lebih baik. 🩸",
 ],
 "wa": {"tajuk": "BodyKey Nutritious Meal Shake PERISA PISANG (baharu)", "nota": "Ruang tertutup sahaja. Key selling dari AMWAY_BRAND/KEY_SELLING.md (amway.my 128188M, semak 18 Nov 2026). Jangan tulis 'tanpa gula' atau 'bebas laktosa'. Sebut sudut berat badan hanya dengan 'Keputusan berbeza mengikut individu'. Gambar: bodykey-banana-gaya-studio.jpg. Semak harga & promosi rasmi hari ini.",
  "t": "Hai [nama] 😊\n\nMinggu ni Momyizz kongsi pasal ibu yang selalu skip sarapan. Ada yang tanya shake apa Momyizz minum pagi tadi. 🍌\n\nItu *BodyKey by Nutrilite Nutritious Meal Shake*, *PERISA PISANG yang baru keluar!*\n\nBukan untuk diet je tau. Sesuai untuk sarapan, bekal, petang kalut, atau bila nak kurangkan gula:\n• 17g protein tumbuhan dari soya & biji chia\n• 5g serat prebiotik\n• 20 vitamin & mineral\n• Hanya 6g gula sehidangan, GI rendah (diperakui Glycemic Index Center)\n• Siap 1 minit: 1 paket + 250ml air, goncang\n• Paket individu, senang masuk beg\n• Ada juga perisa Chocolate, Café Latte & Berry\n\n• Harga: RM[HARGA] / kotak 14 paket (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n• Promosi: [promosi rasmi Amway, jika ada]\n• Rasa pisang pada Momyizz: [pengalaman sebenar Momyizz]\n\nNikmati sebagai sebahagian daripada diet sihat & gaya hidup aktif. Ada susu & soya, tak sesuai untuk yang tak tahan laktosa. Bawah 12 tahun, hamil / menyusu atau ada masalah kesihatan, rujuk doktor dulu ya. 🙏\n\nNak cuba? Reply \"PISANG\", Momyizz uruskan. 💛"}},

# ================================================================ HARI 5
{"d": 5, "ep": 2, "tema": "Persediaan malam & pelan B pagi kelam-kabut", "produk": ("soy", "Pagi kelam-kabut, perlukan pelan B yang ada protein"),
 "video": {"tajuk": "10 minit malam untuk pagi yang tenang", "nota": CERITA + " Sticker: 19-blazer-thumbs-up (babak akhir). Babak bekal: tin Soy Protein Drink kelihatan sebagai pelan B; jangan sebut nama dalam sari kata / suara.",
  "babak": [
   ("0–3s", "Jam dinding 10 malam, dapur", "10 minit malam ni = pagi esok lebih tenang 🌙"),
   ("3–15s", "Rebus telur, masuk peti", "Rebus 4 biji telur, simpan dalam peti."),
   ("15–27s", "Oat dalam balang, tuang susu, letak buah", "Oat rendam semalaman. Esok tinggal ambil."),
   ("27–38s", "Bekas bekal tersusun atas meja + tin minuman protein di sebelah (Soy Protein Drink kelihatan)", "Bekas bekal anak DAN ibu dah sedia. Pelan B pun ada: minuman protein tumbuhan."),
   ("38–45s", "Pagi: Momyizz sarapan sambil duduk", "Hasilnya? Sarapan sambil duduk. 5 minit pun rasa menang 🏆"),
  ],
  "caption": "Self-care tak semestinya spa. Kadang dia cuma sarapan sambil duduk 💛\n\n#Momyizz #RutinMalam #SarapanIbu #SelfCare"},
 "carousel": {"tajuk": "Pelan B bila pagi tak ikut rancangan",
  "slaid": [
   "PELAN B 🆘\nBila pagi tak ikut rancangan",
   "REALITI\nAnak demam, mesyuarat awal, lupa rebus telur. Ia berlaku. 😅",
   "PELAN B 1\nPisang + segenggam kacang dalam beg",
   "PELAN B 2\nSusu kotak kecil + roti gandum",
   "PELAN B 3\nMinuman protein untuk hari yang betul-betul tak sempat\n(Momyizz pilih protein tumbuhan, bebas laktosa, tanpa pewarna & perisa tiruan. Semak label ya!)",
   "INGAT\nPelan B bukan pengganti sarapan sebenar.\nMakanan sebenar tetap nombor satu. 🙏\n\n" + DISC,
  ],
  "caption": "Pelan B korang apa? Kongsi kat komen 👇\n\n" + DISC + "\n\n#Momyizz #SarapanIbu #IbuBekerja #RealitiIbu"},
 "teks": [
  "Info ringkas: protein bukan dari daging sahaja. 🌱\n\nTelur, ikan, tauhu, tempe, kekacang dan susu semuanya sumber protein. Tauhu dan tempe antara pilihan protein yang mudah didapati dan berpatutan di Malaysia.",
  "Soalan: semalam pukul berapa korang makan makanan pertama? ⏰\n\n🕖 Sebelum 8 pagi\n🕘 8–10 pagi\n🕛 Lepas 10 pagi\n🙈 Tengah hari baru teringat\n\nMomyizz: 7:30 pagi, sambil duduk! 🎉",
  "Tips telur rebus untuk seminggu 💡\n\n✅ Rebus sekali gus 6–8 biji, sejukkan cepat dalam air sejuk\n✅ Simpan dalam peti BERSAMA kulit, dalam bekas bertutup\n✅ Elok dimakan dalam tempoh seminggu (USDA)\n✅ Tulis tarikh rebus pada bekas\n\nSarapan, bekal dan snek petang siap! 🥚",
  "Info penting: sebelum beli apa-apa supplemen atau minuman kesihatan, semak nombor pendaftaran \"MAL\" pada label. ⚠️\n\nProduk berdaftar dengan KKM boleh disemak melalui laman NPRA. Elak produk yang janji kurus cepat atau tiada maklumat pendaftaran.",
 ],
 "wa": {"tajuk": "Nutrilite Soy Protein Drink", "nota": "Ruang tertutup sahaja (pelanggan sedia ada / group tertutup / orang yang bertanya). Key selling dari AMWAY_BRAND/KEY_SELLING.md (amway.my, semak 18 Nov 2026). Gambar: AMWAY_BRAND/PRODUK/soy-protein-drink-450g.png (Original Flavour 450g). Semak harga hari ini. Jangan tambah dakwaan kesihatan (imun, letih, kolesterol).",
  "t": "Hai [nama] 😊\n\nMinggu ni Momyizz kongsi pasal sarapan ibu yang selalu tertinggal. Ramai tanya apa \"pelan B\" Momyizz untuk hari yang tak sempat makan.\n\nYang Momyizz guna: *Nutrilite Soy Protein Drink*\n• Protein tumbuhan: gabungan gandum, soya & kacang pea\n• 8g protein setiap hidangan, ada kesemua 9 asid amino perlu\n• Bebas laktosa, rendah lemak\n• Tiada pewarna, perisa atau pengawet tiruan ditambah\n• Perisa: Original Flavour, 450g. Tanpa perisa & tanpa pemanis, jadi senang campur dalam apa-apa minuman\n• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n• Cara guna: campur 1–2 sudu dalam minuman, kacau / goncang. Boleh juga tabur atas bijirin\n• Tidak disyorkan untuk bayi bawah 1 tahun. Penghidap gout, hadkan pengambilan purin\n\nMomyizz guna untuk hari kelam-kabut sahaja, bukan pengganti sarapan sebenar. 🙏\n\nKalau nak, reply \"NAK\", Momyizz uruskan. 💛\n\n" + DISC}},

# ================================================================ HARI 6
{"d": 6, "ep": 2, "tema": "Gula tersembunyi dalam minuman", "produk": ("bodykey", "Nak ganti minuman manis pagi dengan pilihan GI rendah, kurang gula"),
 "video": {"tajuk": "Gula paling banyak bukan dalam pinggan", "nota": CERITA + " Sticker: 09-kartun-terkejut-pipi (babak pendedahan).",
  "babak": [
   ("0–3s", "Tiga cawan atas meja: teh tarik, kopi ais, air kotak", "Gula paling banyak dalam rutin Momyizz… bukan dalam pinggan. 😳"),
   ("3–15s", "Momyizz tunjuk cawan satu per satu", "Teh tarik pagi. Kopi ais tengah hari. Air kotak petang."),
   ("15–28s", "Momyizz minum air kosong dulu, baru kopi", "Sekarang: air kosong dulu, baru kopi."),
   ("28–40s", "Momyizz di kaunter kedai, isyarat 'kurang manis'", "Bila beli: \"kurang manis ya!\""),
   ("40–45s", "Momyizz goncang shake pisang dalam shaker, tuang ke gelas (kotak BodyKey perisa pisang kelihatan), senyum ke kamera", "Bukan haramkan teh tarik 😄 Pagi Momyizz sekarang: shake pisang GI rendah, hanya 6g gula. | " + DISC),
  ],
  "caption": "Minuman manis mana paling susah korang nak kurangkan? 👇\n\n#Momyizz #KurangManis #GayaHidupSihat"},
 "carousel": {"tajuk": "Cara baca label gula",
  "slaid": [
   "GULA TERSEMBUNYI 🧋\nCara kesan dalam 10 saat",
   "1. BACA LABEL\nTengok baris \"Gula\" atau \"Jumlah gula\" dalam jadual nutrisi.",
   "2. TENGOK SAIZ HIDANGAN\nSatu botol mungkin ada lebih daripada satu hidangan.",
   "3. NAMA LAIN GULA\nSirap, sukrosa, glukosa, fruktosa, madu, gula perang.",
   "4. CARI LOGO\n\"Pilihan Lebih Sihat\" (KKM) membantu pilih produk yang lebih baik.",
   "KKM GALAKKAN\nHadkan gula tambahan, termasuk dalam minuman.\nSave untuk masa membeli-belah 🛒\n\n" + DISC,
  ],
  "caption": "4 cara kesan gula tersembunyi. Save & bawa masa shopping 🛒\n\nSumber: KKM, Garis Panduan Diet Malaysia 2020.\n" + DISC + "\n\n#Momyizz #KurangManis #BacaLabel"},
 "teks": [
  "Info ringkas: Garis Panduan Diet Malaysia (KKM) galakkan kita hadkan gula tambahan, termasuk dalam minuman. ☕\n\nTrick paling mudah Momyizz: segelas air kosong dulu, baru kopi atau teh.",
  "Jujur: minuman manis mana paling susah korang tinggal? 🧋\n\n☕ Teh tarik\n🧊 Kopi ais\n🧃 Air kotak\n🥤 Air bergas\n\nMomyizz: teh tarik pagi. Sekarang selang-seli dengan shake pisang GI rendah, hanya 6g gula. Rasa macam milkshake pisang! 🍌",
  "Tips kurangkan manis tanpa rasa terseksa 💡\n\nMinggu 1: minta \"kurang manis\"\nMinggu 2: \"separuh gula\"\nMinggu 3: cuba teh / kopi O kosong sekali sehari\nMinggu 4: tukar satu minuman manis pagi kepada shake GI rendah (6g gula, 17g protein)\n\nYang Momyizz perasan: lama-lama tekak dah biasa, dan air manis sangat terasa terlalu manis. 😄",
  "Info penting: ada sejarah diabetes dalam keluarga? ⚠️\n\nNHMS 2023: 15.6% dewasa Malaysia ada diabetes, dan ramai tak tahu. Saringan gula darah boleh dibuat di klinik kesihatan. Jangan tunggu ada simptom. 🩸",
 ],
 "wa": {"tajuk": "Minta testimoni (pelanggan sedia ada)", "nota": "Untuk dapatkan testimoni SEBENAR. Guna hanya dengan kebenaran, tanpa dakwaan perubatan.",
  "t": "Hai [nama] 😊 Terima kasih sebab percaya Momyizz.\n\nDah lebih kurang [tempoh] guna [produk]. Boleh kongsi sikit pengalaman [nama]? Contohnya macam mana [nama] guna dalam rutin harian, dan apa yang [nama] suka.\n\nKalau [nama] izinkan, Momyizz nak kongsi dalam group tertutup Momyizz (nama boleh disembunyikan). Kalau tak selesa pun takpe langsung. 💛"}},

# ================================================================ HARI 7
{"d": 7, "ep": 3, "tema": "Span dapur & kebersihan dapur", "produk": ("dish", "Picit sabun banyak-banyak; nak sabun pekat yang jimat & lembut di tangan"),
 "video": {"tajuk": "Span yang Momyizz pegang setiap malam", "nota": CERITA + " Sticker: 14-blazer-tutup-mulut (babak span). Boleh juga guna video Episod 3 (tab Episod). Babak sabun: botol Dish Drops BOLEH kelihatan (rakaman sendiri), tetapi JANGAN sebut nama Dish Drops / Amway dalam sari kata, teks atas skrin, voiceover atau caption. Kalau ada yang tanya 'sabun apa?' di komen, balas 'Momyizz DM ya 😊' dan kongsi dalam DM / WhatsApp (slot wa).",
  "babak": [
   ("0–3s", "Close-up span lama diperah, kekuningan", "Bila kali terakhir korang tukar ni? 🧽"),
   ("3–12s", "Momyizz picit sabun banyak-banyak terus atas span", "Dulu Momyizz picit sabun banyak-banyak. Fikir: span sentiasa bersabun, mesti bersih."),
   ("12–22s", "Teks atas skrin + Momyizz terkejut", "Kajian 2017 jumpa bakteria sangat tinggi dalam span dapur terpakai. 😳"),
   ("22–32s", "Tulis tarikh pada span baru dengan marker", "Sekarang: tulis tarikh pada span baru, perah dan keringkan lepas guna."),
   ("32–41s", "Close-up botol Dish Drops, tuang sedikit + air ke botol picit, picit sikit ke span, close-up buih banyak", "Sabun pekat pun Momyizz cairkan dulu. Sikit je, buih banyak & tahan lama 🫧"),
   ("41–45s", "Dapur bersih, Momyizz senyum", "Dapur bersih bermula dengan benda kecil ✨ | " + DISC),
  ],
  "caption": "Bila kali terakhir korang tukar span? Jujur je kat komen 😂\n\nSabun pun Momyizz dah tak picit banyak-banyak. Sabun pekat, cairkan dulu, sikit je dah berbuih 🫧 Tangan basuh pinggan hari-hari, jadi Momyizz pilih yang ada aloe vera & dah diuji pakar dermatologi 🤲\n\nSumber: Cardinale et al. (2017).\n" + DISC + "\n\n#Momyizz #DapurBersih #TipsRumah"},
 "carousel": {"tajuk": "5 Kunci Makanan Lebih Selamat (WHO)",
  "slaid": [
   "5 KUNCI MAKANAN LEBIH SELAMAT\nVersi dapur rumah (WHO) 🍽️",
   "1. JAGA KEBERSIHAN\nBasuh tangan, permukaan dan alatan. Tukar span secara berkala.",
   "2. ASINGKAN\nMentah dan masak guna papan pemotong berbeza.",
   "3. MASAK SEMPURNA\nTerutama ayam, daging, telur dan makanan laut.",
   "4. SUHU SELAMAT\nJangan biar lauk lama di suhu bilik. Simpan dalam peti.",
   "5. AIR & BAHAN SELAMAT\nGuna air yang selamat dan bahan yang segar.\nSave & kongsi 🌿\n\n" + DISC,
  ],
  "caption": "5 kunci makanan lebih selamat dari WHO. Save untuk dapur korang 🍽️\n\nSumber: WHO Five Keys to Safer Food.\n" + DISC + "\n\n#Momyizz #DapurBersih #KeselamatanMakanan"},
 "teks": [
  "Info ringkas: span yang \"dibersihkan\" dengan cara rumah tak semestinya kurang bakteria. 🧽\n\nPenulis kajian Cardinale et al. (2017) cadangkan span ditukar secara berkala, contohnya setiap minggu.",
  "Soalan jujur: korang guna sabun basuh pinggan macam mana? 🧽\n\nA. Picit terus atas span, banyak-banyak\nB. Cairkan dulu dalam botol picit / mangkuk air\n\nMomyizz dulu A. Sekarang B. Sabun pekat, sikit je dah berbuih banyak, buih pun tahan lama. Jimat! 🫧",
  "Tips span tahan lebih bersih 💡\n\n✅ Perah kuat lepas guna\n✅ Letak di rak berlubang / tempat berangin, bukan dalam sinki basah\n✅ Asingkan span pinggan dan kain lap meja\n✅ Tulis tarikh, tukar secara berkala\n✅ Sabun pekat? Cairkan dulu, picit sikit je\n✅ Pilih sabun yang dah diuji pakar dermatologi, tangan kita basuh pinggan hari-hari\n\nSpan kering = kurang tempat untuk bakteria membiak. 🧽",
  "Info penting musim banjir: leptospirosis merebak melalui air atau tanah yang tercemar air kencing tikus. ⚠️\n\nElak meredah air banjir tanpa kasut, tutup makanan di dapur, dan dapatkan rawatan jika demam selepas terdedah kepada air banjir. 🙏",
 ],
 "wa": {"tajuk": "Amway Home Dish Drops", "nota": "Ruang tertutup sahaja. Key selling dari AMWAY_BRAND/KEY_SELLING.md (amway.my, semak 18 Nov 2026). JANGAN tulis 'sesuai untuk kulit sensitif' (tiada sumber rasmi). Semak harga hari ini. Jangan dakwa sabun membunuh kuman atau menggantikan tukar span.",
  "t": "Hai [nama] 😊\n\nPagi tadi Momyizz kongsi pasal span dapur, dan ada yang tanya: \"Sabun apa tu, sikit je tapi buih banyak?\" 🫧\n\nItu *DISH DROPS Concentrated Dishwashing Liquid (1L)* dari Amway Home.\n• Sangat pekat: setitik pun dah boleh tanggalkan minyak\n• Buihnya tahan lama, jadi tak perlu tambah sabun selalu\n• Cara guna untuk span: cairkan 1 bahagian sabun dengan 1–5 bahagian air dalam botol picit, picit sedikit ke span\n• Ada aloe vera yang melembutkan, dan dah diuji pakar dermatologi. Sesuai untuk yang basuh pinggan hari-hari 🤲\n• Formula biodegradable, lebih mesra alam 🌿\n• Boleh juga basuh sayur & buah (1 ml dalam 5 L air)\n• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n• Kenapa Momyizz pilih: [pengalaman sebenar Momyizz]\n\nTapi ingat ya, sabun yang bagus tak menggantikan tabiat tukar span dan keringkan span. 🧽\n\nKalau berminat, reply \"NAK\", Momyizz uruskan. 💛"}},

# ================================================================ HARI 8-30 (rancangan; teks penuh dijana dengan Claude)
# Format: (video, carousel, [teks info, teks pertanyaan, teks tips, teks alert], wa atau None)
{"d": 8, "ep": 3, "tema": "Papan pemotong & kain lap", "produk": ("dish", "Papan pemotong & kain lap berminyak susah bersih"),
 "plan": ("Momyizz tunjuk 2 papan pemotong: mentah vs masak", "Kain lap: bila patut basuh & tukar (5 slaid)",
          ["Kain lap lembap = tempat bakteria suka", "Korang ada berapa papan pemotong?", "Basuh papan pemotong dengan air panas & sabun, keringkan berdiri", "tikus di dapur musim hujan, tutup makanan"],
          "Soalan lazim Dish Drops (dari soalan pelanggan sebenar)")},
{"d": 9, "ep": 3, "tema": "Kesilapan dapur yang biasa", "produk": ("dish", "Tak tahu cara basuh sayur & buah dengan betul"),
 "plan": ("3 kesilapan dapur Momyizz dulu", "Mitos vs fakta kebersihan dapur",
          ["Basuh ayam mentah boleh percik bakteria ke sinki", "Korang basuh ayam mentah dalam sinki?", "Cara simpan lauk lebihan: sejukkan cepat, bekas bertutup, peti", "lauk lebih jangan biar semalaman di suhu bilik"], None)},
{"d": 10, "ep": 4, "tema": "Panaskan bekal dalam bekas plastik", "produk": ("bodykey", "Beratur panaskan bekal; perlukan pilihan makan tengah hari yang tak perlu dipanaskan"),
 "plan": ("Beratur depan microwave pantri pejabat", "Apa kajian makmal 2023 jumpa (label Kajian awal)",
          ["Label 'microwave safe' maksudnya apa", "Bekal korang panaskan dalam bekas apa?", "Pindah lauk ke pinggan kaca sebelum panaskan. Hari microwave penuh? Shake siap 1 minit, cuma perlu air", "bekas retak / melengkung patut ditukar"], None)},
{"d": 11, "ep": 4, "tema": "Bekal sihat ke pejabat", "produk": ("bodykey", "Bekal tak seimbang; tak tahu pinggan yang betul"),
 "plan": ("Susun bekal seminggu dalam 20 minit", "Bekal ikut Pinggan Sihat (5 slaid)",
          ["Biar lauk sejuk sikit sebelum masuk bekas", "Korang bawa bekal berapa kali seminggu?", "Bekal seminggu: masak asas hari Ahad, susun ikut hari, guna pinggan Suku-Suku Separuh sebagai panduan", "bekal berkuah jangan biar lebih 2 jam di suhu bilik"],
          "BodyKey Nutritious Meal Shake perisa pisang: bekal kalut siap 1 minit, 17g protein, 6g gula (key selling KEY_SELLING.md; ada susu & soya)")},
{"d": 12, "ep": 4, "tema": "Cara baca berita kesihatan (bahagian 2)", "produk": ("bodykey", "Keliru iklan 'kurus cepat'; nak program berstruktur tanpa janji kosong"),
 "plan": ("Tajuk viral vs isi kajian sebenar", "Kajian makmal vs manusia: bezanya",
          ["FDA: belum ada bukti risiko mikroplastik dalam makanan, pemantauan diteruskan", "Berita kesihatan apa paling selalu masuk group keluarga?", "Tanya 3 soalan sebelum percaya tajuk viral atau iklan 'kurus cepat': ada pendaftaran KKM? ada janji kg? ada 'keputusan berbeza'?", "semak sebenarnya.my sebelum forward"], None)},
{"d": 13, "ep": 5, "tema": "Minum air cukup", "produk": ("espring", "Malas minum air kosong sebab rasa / sumber air"),
 "plan": ("Botol air masih penuh sampai petang", "Berapa banyak air kita perlu (EFSA ~2.0 L wanita, termasuk makanan)",
          ["Air dari buah & sup pun dikira", "Hari ni korang dah minum berapa gelas?", "Tanda masa pada botol air (10 pg, 12 tgh, 3 ptg)", "cuaca panas / demam = perlu lebih air"], None)},
{"d": 14, "ep": 5, "tema": "Cabaran Air 7 hari", "produk": ("espring", "Nak air minuman yang mudah diisi setiap hari untuk cabaran"),
 "plan": ("Lancar #CabaranAirMomyizz", "Trick 5 waktu solat = 5 gelas",
          ["Air kosong dulu, baru kopi", "Siapa nak join cabaran? Komen JOIN", "Letak botol air di tempat yang selalu nampak", "air kotak / sirap bukan pengganti air kosong"],
          "eSpring Water Purifier model baharu (key selling dari KEY_SELLING.md; boleh tulis MENGURANGKAN mikroplastik ikut amway.my, JANGAN tulis singkir / bebas mikroplastik)")},
{"d": 15, "ep": 5, "tema": "Dehidrasi & letih", "produk": ("bodykey", "Petang blur & lapar, terus capai snek manis"),
 "plan": ("Petang blur: kurang minum ke?", "Tanda badan perlukan air",
          ["Dehidrasi ringan dikaitkan dengan fokus menurun (kajian awal)", "Korang selalu letih pukul berapa?", "Petang: segelas air dulu, kemudian snek berprotein (contoh shake pisang 17g protein, hanya 6g gula) ganti kuih manis", "letih berpanjangan ada banyak punca, jumpa doktor"], None)},
{"d": 16, "ep": 6, "tema": "Rutin kulit 5 minit", "produk": ("cleanser", "Malas cuci muka malam; perlukan pencuci yang lembut & cepat"),
 "plan": ("Pukul 10 malam, 'cuci muka esok je la…'", "Cara cuci muka betul (AAD)",
          ["Air suam, bukan panas", "Rutin malam korang berapa langkah?", "Kit cuci muka 5 minit dalam satu dulang", "jangan tidur dengan mekap"], None)},
{"d": 17, "ep": 6, "tema": "SPF setiap hari", "produk": ("uv", "Skip SPF sebab rasa berminyak"),
 "plan": ("Dulang skincare sebelah sinki", "SPF 30 spektrum luas: kenapa setiap hari (AAD)",
          ["SPF tetap perlu walaupun dalam bangunan dekat tingkap", "Jenis kulit korang apa?", "Sapu SPF sebanyak dua jari untuk muka & leher", "produk 'cerah 7 hari' tanpa pendaftaran, hati-hati"],
          "ARTISTRY SKIN NUTRITION Multi-Defense UV Protect SPF50+/PA++++ (key selling dari KEY_SELLING.md; tiada janji hasil, tiada dakwaan cegah penuaan)")},
{"d": 18, "ep": 6, "tema": "Skincare: konsisten lebih penting", "produk": ("cleanser", "Rutin skincare terlalu panjang; nak 2 langkah asas yang konsisten"),
 "plan": ("Dulu 7 langkah, sekarang 3", "Rutin 3 langkah yang cukup",
          ["Rutin konsisten > banyak produk", "Produk skincare apa korang beli ikut trend?", "Habiskan satu produk dulu sebelum beli yang baharu", "uji produk baharu pada kulit kecil dulu (patch test)"], None)},
{"d": 19, "ep": 7, "tema": "Air botol plastik: kajian 2024", "produk": ("espring", "Nak kurangkan air botol plastik"),
 "plan": ("Dua kotak air botol dalam bonet", "Kajian 2024 dalam 6 slaid (Kajian awal + WHO)",
          ["Sampel terhad, mampu kesan ≠ terbukti bahaya", "Korang simpan air botol di mana?", "Simpan air botol di tempat sejuk dan teduh", "jangan simpan air botol dalam kereta panas lama-lama"], None)},
{"d": 20, "ep": 7, "tema": "Air minuman keluarga", "produk": ("espring", "Air minuman seisi keluarga: nak pilihan di rumah"),
 "plan": ("2 benda yang Momyizz ubah", "Pilihan air minuman di rumah: kebaikan & perkara perlu jaga",
          ["Tukar kartrij penapis air ikut jadual pengeluar", "Air minuman di rumah korang dari mana?", "Jadual tukar kartrij penapis: tulis dalam kalendar telefon", "air paip keruh selepas banjir, didihkan"], None)},
{"d": 21, "ep": 7, "tema": "Rumusan siri mikroplastik", "produk": ("espring", "Rumusan: langkah praktikal kurangkan pendedahan mikroplastik di rumah"),
 "plan": ("Refleksi 3 minggu berkongsi", "Siri mikroplastik dalam 1 carousel (save)",
          ["Ringkasan: 4 langkah paling mudah", "Topik apa korang nak seterusnya?", "Satu tabiat seminggu: pilih yang paling mudah", "ringkasan 3 tanda berita kesihatan palsu"], None)},
{"d": 22, "ep": 8, "tema": "Vitamin C setiap hari", "produk": ("bioc", "Susah makan buah setiap hari"),
 "plan": ("Anak bersin, terus potong oren", "Gunakan carousel Episod 8 (tab Episod)",
          ["Badan tak boleh hasilkan vitamin C sendiri (NIH)", "Buah apa selalu ada di rumah korang?", "Potong buah awal-awal, simpan di aras mata dalam peti", "musim tengkujuh, basuh tangan & tidur cukup kekal asas"], None)},
{"d": 23, "ep": 8, "tema": "Mitos vitamin C", "produk": ("bioc", "Keliru mitos vitamin C; nak cara ambil yang betul (pelengkap)"),
 "plan": ("Trick anak makan buah tanpa disuruh", "Vitamin C cegah selesema? Apa kata Cochrane",
          ["Jambu batu antara buah tempatan tinggi vitamin C", "Teka: buah tempatan mana paling tinggi vitamin C?", "Buah tinggi vitamin C yang murah ikut musim", "dos tinggi tak semestinya lebih baik, ikut label"],
          "Nutrilite Bio C Plus sebagai pelengkap (makanan tetap utama; tiada dakwaan cegah / rawat)")},
{"d": 24, "ep": 8, "tema": "Vitamin C & zat besi", "produk": ("bodykey", "Menu tak seimbang sepanjang minggu; nak tambah zat besi & vitamin C yang mudah"),
 "plan": ("Menu buah seminggu bajet biasa", "Cara bantu penyerapan zat besi",
          ["Vitamin C bantu serap zat besi dari sumber tumbuhan", "Korang minum teh lepas makan?", "Jarakkan teh / kopi dari waktu makan. Shake pisang sehidangan ada 5.8mg zat besi & 34mg vitamin C (label)", "pucat & pening berpanjangan, buat ujian darah"], None)},
{"d": 25, "ep": 9, "tema": "Duduk terlalu lama", "produk": ("bodykey", "Duduk lama, susah jejak tabiat harian"),
 "plan": ("Momyizz kira jam duduk semalam", "WHO 2020: berapa minit bergerak seminggu",
          ["Sedikit aktiviti lebih baik daripada tiada", "Berapa jam korang duduk hari ni?", "Set peringatan 'bangun & gerak' setiap jam", "29.9% dewasa Malaysia tidak aktif (NHMS 2023)"], None)},
{"d": 26, "ep": 9, "tema": "Gerak bersama keluarga", "produk": ("bodykey", "Nak gaya hidup aktif seisi keluarga, bukan diet sorang-sorang"),
 "plan": ("Jalan 10 minit lepas makan malam bawa anak", "10 cara gerak tanpa gym",
          ["Berdiri masa jawab telefon pun dikira", "Gerak apa korang buat hari ni?", "Jalan kaki keluarga: tetapkan masa yang sama setiap hari", "sakit dada / sesak nafas masa bersenam, berhenti & dapatkan rawatan"], None)},
{"d": 27, "ep": 9, "tema": "Kuatkan otot", "produk": ("bodykey", "Latihan otot tapi hidangan kurang protein"),
 "plan": ("Latihan 5 minit di rumah", "Latihan otot 2 hari seminggu (WHO 2020)",
          ["Otot kuat bantu aktiviti harian", "Korang pernah buat latihan otot?", "3 latihan otot tanpa alat: squat dinding, angkat botol air, tekan tubi lutut", "hamil / ada penyakit, tanya doktor sebelum mula"],
          "BodyKey Nutritious Meal Shake perisa pisang selepas bersenam: 17g protein tumbuhan sehidangan (key selling KEY_SELLING.md; tiada janji otot / kurus)")},
{"d": 28, "ep": 10, "tema": "Kulit dari dalam", "produk": ("cleanser", "Kulit kusam walaupun banyak produk; asas: cuci muka betul"),
 "plan": ("Rak skincare penuh, kulit tetap kusam", "Pinggan Glowing (5 slaid)",
          ["Vitamin C perlu untuk kolagen (NIH)", "Pinggan makan tengah hari korang hari ni?", "Isi separuh pinggan dengan sayur dulu", "1 dalam 2 yang ada kolesterol tinggi tak tahu (NHMS 2023)"], None)},
{"d": 29, "ep": 10, "tema": "Omega-3 & ikan tempatan", "produk": ("omega", "Jarang makan ikan berlemak"),
 "plan": ("Ikan kembung & sardin minggu ni", "Sumber omega-3 tempatan + kajian kulit masih terhad",
          ["EPA & DHA ada dalam ikan berlemak (NIH)", "Korang makan ikan berapa kali seminggu?", "Cara masak ikan kembung / sardin yang mudah untuk anak", "makan ubat cair darah? Tanya doktor sebelum ambil omega-3"],
          "NUTRILITE Salmon Omega Complex (key selling dari KEY_SELLING.md; sertakan amaran rasmi: ubat cair darah, hamil / menyusu, kanak-kanak; tiada dakwaan kulit)")},
{"d": 30, "ep": 10, "tema": "Refleksi 30 hari", "produk": ("bodykey", "Bulan depan: mula perjalanan pengurusan berat badan 60 hari"),
 "plan": ("Terima kasih 30 hari bersama korang", "10 perkara Momyizz kongsi bulan ni",
          ["1 tabiat paling mudah untuk mula", "Bulan depan nak Momyizz kupas apa?", "Senarai semak 10 tabiat untuk bulan depan", "cara betul ambil supplemen (6 perkara)"],
          "BodyKey Nutritious Meal Shake perisa pisang untuk rutin bulan depan, atau Jump Start Kit (New Edition) bagi yang nak urus berat badan + ikuti pelanggan sedia ada (key selling KEY_SELLING.md; sudut berat: WAJIB 'Keputusan berbeza mengikut individu')")},
]
