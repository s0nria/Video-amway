# -*- coding: utf-8 -*-
"""Sumber kalendar konten harian Momyizz (Amway).

Edit fail ini, kemudian jalankan:  python3 KALENDAR_PENULISAN/bina.py

Format setiap hari (DISAHKAN pengguna, pilihan A): SATU topik, isi berbeza untuk setiap konten.
  video     08:30  🎥 Video STORYTELLING (TikTok / Reels, Flow AI) -> skrip babak + teks atas skrin + caption
  MG_FULL   13:30 / 19:30  🎞️ 2 video MOTION GRAFIK (tips; masalah -> penyelesaian) -> lihat bawah fail
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
  "Info penting: WHO anggarkan hampir 1 dalam 3 wanita berumur 15–49 tahun di dunia mengalami anemia. ⚠️\n\nSelalu letih, pucat, pening atau sesak nafas bila naik tangga? Buat ujian darah di klinik kesihatan. Jangan anggap penat ibu tu biasa. 🩸",
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

# ================================================================ HARI 8
{"d": 8, "ep": 3, "tema": "Papan pemotong & kain lap", "produk": ("dish", "Papan pemotong & kain lap berminyak susah bersih"),
 "video": {"tajuk": "Dua papan pemotong di dapur Momyizz", "nota": CERITA + " Sticker: 19-blazer-thumbs-up (babak akhir). Babak basuh: botol Dish Drops kelihatan; jangan sebut nama dalam sari kata / suara.",
  "babak": [
   ("0–3s", "Close-up dua papan pemotong: satu merah, satu hijau", "Kenapa Momyizz ada DUA papan pemotong? 🔪"),
   ("3–14s", "Momyizz potong ayam mentah atas papan merah", "Dulu satu papan untuk semua: potong ayam mentah, lepas tu terus potong timun. 🙈"),
   ("14–26s", "Teks atas skrin + Momyizz angguk", "WHO: asingkan bahan mentah dan bahan masak, termasuk pisau dan papan pemotong."),
   ("26–38s", "Picit sedikit sabun pekat ke span, buih banyak, gosok papan dengan air panas (botol Dish Drops kelihatan), keringkan papan berdiri", "Lepas guna: air panas + sabun. Sabun pekat, setitik je dah tanggal minyak. Keringkan berdiri. 🫧"),
   ("38–45s", "Momyizz tunjuk dua papan, thumbs up", "Merah untuk mentah, hijau untuk masak. Senang ingat! 💚 | " + DISC),
  ],
  "caption": "Korang guna satu papan pemotong untuk semua? Jujur je 😅\n\nSumber: WHO, Five Keys to Safer Food.\n" + DISC + "\n\n#Momyizz #DapurBersih #KeselamatanMakanan"},
 "carousel": {"tajuk": "Kain lap dapur: bila patut basuh & tukar?",
  "slaid": [
   "KAIN LAP DAPUR 🧻\nBila patut basuh & tukar?",
   "KENAPA PENTING?\nKain lap yang lembap dan ada sisa makanan jadi tempat bakteria membiak.\n🟢 Terbukti (USDA FSIS)",
   "1. ASINGKAN\nSatu kain untuk tangan, satu untuk meja, satu untuk pinggan.\nWarna berbeza = tak tertukar.",
   "2. BASUH KERAP\nBasuh dengan air panas.\nKain yang lap tumpahan daging mentah? Terus basuh, jangan guna semula.",
   "3. KERINGKAN & TUKAR\nSidai sampai kering, jangan biar bergumpal dalam sinki.\nMasih berbau lepas dibasuh? Masa untuk tukar.",
   "INGAT\nKain lap bersih = dapur lebih bersih.\nSave & kongsi 🌿\n\n" + DISC,
  ],
  "caption": "Kain lap dapur korang tukar bila? Kongsi kat komen 👇\n\nSumber: USDA FSIS, panduan keselamatan makanan di dapur.\n" + DISC + "\n\n#Momyizz #DapurBersih #TipsRumah"},
 "teks": [
  "Info ringkas: papan pemotong kayu atau plastik? Dua-dua boleh. 🔪\n\nUSDA kata permukaan tak berliang macam plastik lebih senang dibersihkan, tapi yang paling penting: basuh dengan air panas & sabun selepas setiap guna, dan buang papan yang dah calar dalam atau beralur.",
  "Soalan: kain lap dapur korang basuh atau tukar bila? 🧻\n\nA. Setiap hari\nB. 2–3 hari sekali\nC. Seminggu sekali\nD. Bila dah berbau 🙈\n\nMomyizz dulu D. Sekarang A, dan kain untuk tangan, meja & pinggan dah diasingkan ikut warna.",
  "Tips basuh papan pemotong 💡\n\n✅ Basuh sejurus lepas guna dengan air panas & sabun\n✅ Sabun pekat? Cairkan dulu, setitik pun dah tanggal minyak\n✅ Gosok alur & calar dengan berus\n✅ Keringkan BERDIRI, bukan tertiarap atas sinki\n✅ Calar dalam & susah dibersihkan? Masa untuk tukar\n\nPapan kering = kurang tempat bakteria bersembunyi. 🫧",
  "Info penting untuk keluarga yang ada alahan makanan: guna papan pemotong & pisau berasingan untuk kacang, makanan laut atau telur, supaya alergen tak berpindah ke makanan lain. ⚠️\n\nBibir atau muka bengkak, sesak nafas atau pening selepas makan ialah kecemasan. Terus ke hospital. 🚑",

 ],
 "wa": {"tajuk": "Soalan lazim Dish Drops", "nota": "Ruang tertutup sahaja (terutama untuk yang bertanya selepas konten span dapur). Jawapan dari AMWAY_BRAND/KEY_SELLING.md. Soalan mesin basuh pinggan: semak label dahulu. Tambah soalan pelanggan sebenar jika ada.",
  "t": "Hai [nama] 😊\n\nHari tu ramai tanya pasal sabun pekat Momyizz. Ni Momyizz kumpul soalan lazim *DISH DROPS Concentrated Dishwashing Liquid* dari Amway Home 👇\n\n❓ *Kenapa sikit je dah cukup?*\nSabun ni sangat pekat. Amway sebut setitik dah boleh tanggalkan minyak, dan buihnya tahan lama.\n\n❓ *Macam mana nak guna dengan span?*\nCairkan 1 bahagian sabun dengan 1–5 bahagian air dalam botol picit, kemudian picit sedikit ke span.\n\n❓ *Lembut tak kat tangan?*\nAda aloe vera dan formulanya dah diuji pakar dermatologi. Kulit setiap orang berbeza, jadi kalau kulit sangat sensitif, pakai sarung tangan.\n\n❓ *Mesra alam ke?*\nFormulanya biodegradable. 🌿\n\n❓ *Boleh guna dalam mesin basuh pinggan?*\n[PERLU SEMAK label / amway.my]\n\n❓ *Berapa harga?*\nRM[HARGA] untuk 1L (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n\nAda soalan lain? Reply je, Momyizz jawab. Nak order, reply \"NAK\". 💛"}},

# ================================================================ HARI 9
{"d": 9, "ep": 3, "tema": "Kesilapan dapur yang biasa", "produk": ("dish", "Sinki & alatan tercemar lepas sentuh ayam mentah"),
 "video": {"tajuk": "3 kesilapan dapur Momyizz dulu", "nota": CERITA + " Sticker: 14-blazer-tutup-mulut (babak kesilapan pertama). Babak sinki: botol Dish Drops kelihatan; jangan sebut nama dalam sari kata / suara.",
  "babak": [
   ("0–3s", "Momyizz pegang ayam beku, sengih bersalah", "3 benda dapur yang Momyizz buat dulu… rupanya salah. 😬"),
   ("3–14s", "Ayam beku dibiar atas kaunter, jam berdetik", "Satu: cairkan ayam beku atas kaunter dari pagi. Sekarang: cairkan dalam peti sejuk dari malam sebelumnya."),
   ("14–25s", "Momyizz nak basuh ayam mentah bawah paip, berhenti, geleng", "Dua: basuh ayam mentah bawah paip. Percikan air boleh bawa bakteria ke sinki & pinggan sekeliling."),
   ("25–37s", "Lap sinki & kaunter dengan span bersabun, buih banyak (botol Dish Drops kelihatan)", "Lepas pegang ayam mentah: basuh tangan, sinki & alatan dengan sabun. Sabun pekat, sikit je dah cukup. 🫧"),
   ("37–45s", "Momyizz tutup bekas lauk, masuk peti", "Tiga: lauk lebih jangan biar semalaman. Masuk peti dalam 2 jam. 💚 | " + DISC),
  ],
  "caption": "Kesilapan nombor berapa korang pernah buat? Momyizz buat ketiga-tiga 🙈\n\nSumber: USDA FSIS; WHO, Five Keys to Safer Food.\n" + DISC + "\n\n#Momyizz #DapurBersih #KeselamatanMakanan"},
 "carousel": {"tajuk": "Mitos vs fakta kebersihan dapur",
  "slaid": [
   "MITOS VS FAKTA 🍗\nKebersihan dapur",
   "MITOS: Basuh ayam mentah supaya bersih.\nFAKTA: Percikan air boleh sebarkan bakteria. Memasak sehingga masak sempurna yang membunuh bakteria.\n🟢 Terbukti (USDA)",
   "MITOS: Cairkan ayam beku atas kaunter, tak apa.\nFAKTA: Cairkan dalam peti sejuk, dalam air sejuk (tukar air setiap 30 minit) atau dalam microwave.\n🟢 Terbukti (USDA)",
   "MITOS: Lauk masih elok kalau tak berbau.\nFAKTA: Bakteria berbahaya tak semestinya ubah bau, rasa atau rupa makanan.\n🟢 Terbukti (USDA)",
   "MITOS: Lauk panas tak boleh terus masuk peti.\nFAKTA: Boleh. Bahagikan ke bekas kecil yang cetek supaya cepat sejuk.\n🟢 Terbukti (USDA)",
   "INGAT\nDapur selamat bermula dengan tabiat kecil yang konsisten.\nSave & kongsi 🌿\n\n" + DISC,
  ],
  "caption": "4 mitos dapur yang ramai masih percaya. Save & kongsi dengan keluarga 🍗\n\nSumber: USDA FSIS.\n" + DISC + "\n\n#Momyizz #DapurBersih #MitosFakta"},
 "teks": [
  "Info ringkas: USDA tak galakkan kita basuh ayam mentah di sinki. 🍗\n\nPercikan air boleh membawa bakteria ke sinki, pinggan dan permukaan sekeliling. Yang membunuh bakteria ialah memasak sehingga masak sempurna.",
  "Jujur sikit: korang basuh ayam mentah dalam sinki? 🙈\n\nA. Ya, setiap kali\nB. Kadang-kadang\nC. Dah berhenti\nD. Beli ayam siap bersih\n\nMomyizz dulu A. Sekarang C, dan lepas pegang ayam mentah terus basuh tangan & sinki dengan sabun pekat. Sikit je, dah berbuih. 🫧",
  "Tips simpan lauk lebihan 💡\n\n✅ Sejukkan cepat: bahagikan ke bekas kecil yang cetek\n✅ Guna bekas bertutup, tulis tarikh\n✅ Panaskan sampai benar-benar panas sebelum makan\n✅ Habiskan lauk lebihan dalam 3–4 hari (USDA)\n\nPeti kemas = kurang membazir. 🍱",
  "Info penting: tanda keracunan makanan yang perlukan rawatan segera. ⚠️\n\nCirit-birit berdarah, demam tinggi, muntah sampai tak boleh minum, cirit-birit lebih 3 hari, atau tanda dehidrasi (mulut kering, jarang kencing, pening bila berdiri). Jangan tunggu, pergi klinik. (CDC)",
 ]},

# ================================================================ HARI 10
{"d": 10, "ep": 4, "tema": "Panaskan bekal dalam bekas plastik", "produk": ("bodykey", "Beratur panaskan bekal; perlukan pilihan makan tengah hari yang tak perlu dipanaskan"),
 "video": {"tajuk": "Beratur depan microwave pantri", "nota": CERITA + " Sticker: 09-kartun-terkejut-pipi (babak kajian). Babak shake: kotak / paket BodyKey perisa pisang kelihatan; jangan sebut nama dalam sari kata / suara.",
  "babak": [
   ("0–3s", "Barisan orang depan microwave pantri pejabat, Momyizz di belakang sekali", "Pukul 1 petang. Barisan microwave dah panjang… 😮‍💨"),
   ("3–14s", "Bekas plastik bekal berputar dalam microwave", "Dulu Momyizz panaskan terus dalam bekas plastik. Tak pernah fikir pun."),
   ("14–26s", "Teks atas skrin + Momyizz terkejut", "Kajian makmal 2023: bekas plastik yang dipanaskan dalam microwave melepaskan zarah plastik. 🟠 Kajian awal"),
   ("26–38s", "Momyizz pindah lauk ke pinggan kaca. Hari lain: tuang paket shake pisang ke shaker, tambah air, goncang (kotak BodyKey perisa pisang kelihatan)", "Sekarang: pindah ke pinggan kaca. Hari microwave penuh? Shake pisang siap 1 minit, cuma perlu air. 🍌"),
   ("38–45s", "Momyizz minum di meja kerja, senyum", "Tak perlu panik, cuma ubah sikit tabiat. 💚 | " + DISC),
  ],
  "caption": "Korang panaskan bekal dalam bekas apa? 👇\n\nSumber: Hussain et al., Environmental Science & Technology (2023). Kajian makmal; kesan pada manusia masih dikaji.\n" + DISC + "\n\n#Momyizz #Mikroplastik #BekalPejabat #FaktaBukanPanik"},
 "carousel": {"tajuk": "Bekas plastik + microwave: apa kajian 2023 jumpa?",
  "slaid": [
   "BEKAS PLASTIK + MICROWAVE 🍱\nApa kajian 2023 jumpa?\n(Fakta, bukan panik)",
   "KAJIANNYA\nPenyelidik memanaskan bekas makanan plastik dalam microwave selama 3 minit di makmal.\n(Hussain et al., 2023)",
   "APA DIJUMPA\nSehingga 4.2 juta mikroplastik dan 2.1 bilion nanoplastik terlepas bagi setiap cm² bekas.\n🟠 Kajian awal",
   "TAPI INGAT\nIni kajian makmal pada bekas tertentu. Kesan pada kesihatan manusia masih dikaji.\n🔵 Masih dikaji",
   "LANGKAH MUDAH\n• Pindah lauk ke pinggan kaca / seramik sebelum panaskan\n• Ikut label \"microwave safe\"\n• Tutup dengan penutup kaca atau tisu dapur, bukan plastik",
   "FAKTA, BUKAN PANIK\nKurangkan pendedahan yang mudah dielak.\nSave & kongsi 🌿\n\n" + DISC,
  ],
  "caption": "Kajian microwave & bekas plastik dalam 6 slaid. Save untuk rujukan 🌿\n\nSumber: Hussain et al., Environmental Science & Technology (2023); WHO (2022).\n" + DISC + "\n\n#Momyizz #Mikroplastik #FaktaBukanPanik"},
 "teks": [
  "Info ringkas: label \"microwave safe\" bermaksud bekas itu direka untuk digunakan dalam microwave. 🍱\n\nTapi tetap ikut arahan pada label: tempoh, suhu, dan sama ada penutupnya boleh dimasukkan. Bekas tanpa label? Pindah dulu ke pinggan kaca.",
  "Soalan: bekal korang panaskan dalam bekas apa? 🍱\n\nA. Bekas plastik\nB. Pinggan kaca / seramik\nC. Tak panaskan, makan macam tu je\nD. Tak bawa bekal 😅\n\nMomyizz dulu A. Sekarang B. Hari yang kalut, shake pisang yang tak perlu dipanaskan langsung, siap 1 minit. 🍌",
  "Tips makan tengah hari tanpa beratur microwave 💡\n\n✅ Pindah lauk ke pinggan kaca dari rumah, terus sedia untuk dipanaskan\n✅ Bawa menu yang tak perlu dipanaskan: sandwich telur, salad, buah (makan dalam 2 jam)\n✅ Hari microwave penuh: paket shake dalam beg + 250ml air, siap 1 minit (17g protein, hanya 6g gula)\n\nMasa rehat untuk rehat, bukan beratur. 😄",
  "Info penting: bekas plastik yang retak, melengkung, berubah warna atau berbau patut ditukar. ⚠️\n\nJangan panaskan makanan dalam bekas tanpa label \"microwave safe\", dan elak memanaskan bekas plastik sekali guna dalam microwave.",
 ]},

# ================================================================ HARI 11
{"d": 11, "ep": 4, "tema": "Bekal sihat ke pejabat", "produk": ("bodykey", "Bekal tak seimbang; hari kalut tiada bekal langsung"),
 "video": {"tajuk": "Bekal 20 minit, siap sampai Rabu", "nota": CERITA + " Sticker: 05-satin-semangat (babak akhir). Babak beg kerja: paket BodyKey perisa pisang kelihatan; jangan sebut nama dalam sari kata / suara. Lauk masak hanya disimpan 3–4 hari (USDA), sebab itu bekal disediakan 2 kali seminggu.",
  "babak": [
   ("0–3s", "Timer 20 minit di telefon, dapur hari Ahad", "20 minit hari Ahad = bekal siap sampai Rabu. ⏱️"),
   ("3–14s", "Masak nasi perang, rebus telur, panggang ayam, potong sayur", "Masak asas sekali gus: nasi, protein, sayur."),
   ("14–27s", "Susun dalam bekas: separuh sayur, suku nasi, suku protein", "Susun ikut Pinggan Sihat: separuh sayur & buah, suku nasi, suku protein."),
   ("27–38s", "Label hari pada bekas, masuk peti. Paket shake pisang diselit dalam beg kerja (BodyKey kelihatan)", "Label hari, masuk peti. Rabu ulang sekali lagi. Hari paling kalut? Shake pisang: 17g protein, siap 1 minit. 🍌"),
   ("38–45s", "Momyizz buka peti, bekal tersusun, senyum", "Ahad & Rabu sibuk sikit, hari lain lebih tenang. 💚 | " + DISC),
  ],
  "caption": "Bekal ikut Pinggan Sihat, siap dalam 20 minit 🍱 Korang prep bekal hari apa?\n\nSumber: KKM, Pinggan Sihat Malaysia; USDA FSIS (simpanan lauk 3–4 hari).\n" + DISC + "\n\n#Momyizz #BekalSihat #PingganSihat #IbuBekerja"},
 "carousel": {"tajuk": "Bekal ikut Pinggan Sihat",
  "slaid": [
   "BEKAL IKUT PINGGAN SIHAT 🍱\nSuku-suku separuh (KKM)",
   "SEPARUH: SAYUR & BUAH 🥦\nBrokoli, kacang panjang, timun, buah potong.",
   "SUKU: BIJIRIN 🍚\nNasi (lebih baik nasi perang), mi, roti gandum penuh.",
   "SUKU: PROTEIN 🍗\nAyam, ikan, telur, tauhu, tempe, kekacang.",
   "TAMBAH 💧\nAir kosong, bukan air manis.\nSimpan bekal dalam peti, habiskan dalam 3–4 hari.",
   "SENANG INGAT\nSuku-suku separuh.\nSave & bawa ke dapur 💛\n\n" + DISC,
  ],
  "caption": "Panduan bekal ikut Pinggan Sihat. Save untuk prep minggu ni 🍱\n\nSumber: KKM, Pinggan Sihat Malaysia; USDA FSIS.\n" + DISC + "\n\n#Momyizz #PingganSihat #BekalSihat"},
 "teks": [
  "Info ringkas: nasi perang ada lebih banyak serat berbanding nasi putih. 🍚\n\nTak biasa? Mula dengan campur separuh nasi putih, separuh nasi perang. Lama-lama tekak dah biasa. (USDA FoodData Central)",
  "Soalan: seminggu korang bawa bekal berapa kali? 🍱\n\n0️⃣ Tak pernah\n1️⃣ 1–2 kali\n3️⃣ 3–4 kali\n5️⃣ Setiap hari bekerja\n\nMomyizz: 3 kali. Hari yang tak sempat langsung, paket shake pisang dalam beg jadi pelan B. 17g protein, siap 1 minit. 🍌",
  "Tips bekal tanpa pening 💡\n\n✅ Masak asas 2 kali seminggu: Ahad & Rabu\n✅ Biar lauk sejuk sedikit dalam bekas cetek, kemudian terus masuk peti\n✅ Label hari pada setiap bekas\n✅ Lauk masak dalam peti, habiskan dalam 3–4 hari (USDA)\n\nBekal tersusun = kurang beli makanan segera. 💛",
  "Info penting: bekal berkuah jangan dibiar lebih 2 jam di suhu bilik, atau 1 jam jika cuaca sangat panas (melebihi 32°C). ⚠️\n\nSimpan dalam peti pejabat atau beg bertebat dengan ice pack. Ragu-ragu? Buang. (USDA)",
 ],
 "wa": {"tajuk": "BodyKey shake pisang untuk bekal kalut", "nota": "Ruang tertutup sahaja. Key selling dari AMWAY_BRAND/KEY_SELLING.md (amway.my 128188M). Jangan tulis 'tanpa gula' / 'bebas laktosa'. Semak harga & promosi rasmi hari ini.",
  "t": "Hai [nama] 😊\n\nMinggu ni Momyizz kongsi cara susun bekal ikut Pinggan Sihat. Tapi jujur, ada hari yang memang tak sempat langsung. 😅\n\nHari macam tu, pelan B Momyizz: *BodyKey by Nutrilite Nutritious Meal Shake perisa pisang* 🍌\n• Paket individu, senang masuk beg kerja\n• Siap 1 minit: 1 paket + 250ml air, goncang. Tak perlu beratur microwave\n• 17g protein tumbuhan (soya & chia), 5g serat prebiotik\n• 20 vitamin & mineral\n• Hanya 6g gula, GI rendah\n\n• Harga: RM[HARGA] / kotak 14 paket (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n• Promosi: [promosi rasmi Amway, jika ada]\n\nNikmati sebagai sebahagian daripada diet sihat & gaya hidup aktif. Ada susu & soya, tak sesuai untuk yang tak tahan laktosa. Bawah 12 tahun, hamil / menyusu atau ada masalah kesihatan, rujuk doktor dulu ya. 🙏\n\nNak simpan sekotak untuk hari kalut? Reply \"PISANG\". 💛"}},

# ================================================================ HARI 12
{"d": 12, "ep": 4, "tema": "Cara baca berita kesihatan (bahagian 2)", "produk": ("bodykey", "Keliru iklan 'kurus cepat'; nak produk yang labelnya jelas tanpa janji kosong"),
 "video": {"tajuk": "3 tanda merah iklan kurus cepat", "nota": CERITA + " Sticker: 04-satin-tutup-mulut (babak hook). Babak label: kotak BodyKey perisa pisang kelihatan; jangan sebut nama. Sudut berat badan: ayat 'Keputusan berbeza mengikut individu' WAJIB.",
  "babak": [
   ("0–3s", "Skrin telefon: tajuk viral 'Minuman ni buat kurus 5 kg seminggu!'", "Tajuk macam ni pernah masuk group korang? 📱"),
   ("3–14s", "Momyizz baca telefon, kening berkerut", "Dulu Momyizz hampir beli. Janji kurus cepat, testimoni berlambak."),
   ("14–27s", "Tangan tulis 3 bendera merah atas kertas", "Sekarang Momyizz cari 3 tanda merah: janji kg dalam masa singkat, tiada label nutrisi yang jelas, tiada ayat 'keputusan berbeza'. 🚩"),
   ("27–38s", "Momyizz baca label kotak shake: GI rendah, 6g gula (BodyKey perisa pisang kelihatan)", "Yang Momyizz pilih: label jelas, GI rendah yang diperakui, tiada janji kg. Keputusan berbeza mengikut individu."),
   ("38–45s", "Momyizz senyum ke kamera", "Baca label dulu, baru percaya. 💚 | " + DISC),
  ],
  "caption": "3 tanda merah iklan kurus cepat. Save sebelum tertarik! 🚩\n\nKeputusan berbeza mengikut individu.\n" + DISC + "\n\n#Momyizz #FaktaBukanPanik #BacaLabel"},
 "carousel": {"tajuk": "Kajian makmal vs manusia: bezanya",
  "slaid": [
   "KAJIAN MAKMAL VS MANUSIA 🔬\nKenapa tajuk viral selalu terlebih?",
   "KAJIAN SEL / MAKMAL\nUji dalam tabung uji atau piring makmal. Langkah PALING awal.\n🟠 Kajian awal",
   "KAJIAN HAIWAN\nUji pada tikus dan haiwan lain. Hasil belum tentu sama pada manusia.\n🟠 Kajian awal",
   "KAJIAN MANUSIA\nUji pada orang sebenar. Lebih ramai peserta, lebih kukuh.\nBanyak kajian + badan rasmi setuju = 🟢 Terbukti",
   "CONTOH\nKajian bekas plastik + microwave (2023) dibuat di makmal. Sebab tu labelnya 🟠 Kajian awal, bukan 🟢 Terbukti.",
   "BILA BACA TAJUK\nTanya dulu: kajian jenis apa?\nSave & kongsi 🌿\n\n" + DISC,
  ],
  "caption": "Beza kajian makmal, haiwan & manusia dalam 6 slaid. Save supaya tak mudah termakan tajuk viral 🔬\n\nSumber: FDA, Microplastics and Nanoplastics in Foods.\n" + DISC + "\n\n#Momyizz #FaktaBukanPanik #LiterasiKesihatan"},
 "teks": [
  "Info ringkas: FDA (Amerika Syarikat) menyatakan bukti saintifik semasa belum menunjukkan tahap mikroplastik yang dikesan dalam makanan berisiko kepada kesihatan manusia. 🔬\n\nPenyelidikan dan pemantauan masih diteruskan. Jadi: ambil langkah mudah, tapi tak perlu panik.",
  "Soalan: berita kesihatan apa paling selalu masuk group keluarga korang? 📱\n\n🍋 Petua ubat semula jadi\n⚖️ Produk kurus cepat\n☠️ Makanan \"beracun\"\n🧪 Kajian baru \"mengejutkan\"\n\nMomyizz: produk kurus cepat! Sebab tu Momyizz baca label dulu. Yang Momyizz minum sekarang: GI rendah diperakui, 6g gula, tiada janji kg. 🍌",
  "Tips baca label nutrisi dalam 30 saat 💡\n\n1️⃣ Saiz hidangan dulu: satu bungkus mungkin 2 hidangan\n2️⃣ Gula: makin rendah makin baik\n3️⃣ Protein & serat: makin tinggi makin kenyang\n4️⃣ Senarai ramuan: ramuan pertama paling banyak\n\nContoh shake Momyizz: 6g gula, 17g protein, 5g serat sehidangan. 🍌",
  "Info penting: berat badan turun tanpa sebab, padahal tak cuba kurangkan? ⚠️\n\nJangan anggap rezeki. Penurunan berat yang tak dijangka boleh jadi tanda masalah kesihatan yang perlu diperiksa. Jumpa doktor, terutama jika disertai letih, demam atau hilang selera. (NHS)",
 ]},

# ================================================================ HARI 13
{"d": 13, "ep": 5, "tema": "Minum air cukup", "produk": ("espring", "Botol air tak berusik; nak air minuman yang sentiasa sedia di rumah"),
 "video": {"tajuk": "Botol air masih penuh sampai petang", "nota": CERITA + " Sticker: 13-blazer-tunjuk-atas-kanan (babak angka EFSA). Babak isi air: eSpring kelihatan; jangan sebut nama dalam sari kata / suara.",
  "babak": [
   ("0–3s", "Botol air penuh atas meja kerja, jam tunjuk 4 petang", "Pukul 4 petang. Botol air pagi tadi… masih penuh. 😅"),
   ("3–14s", "Momyizz sibuk depan laptop, lupa minum", "Sibuk sangat sampai lupa minum. Petang terus rasa blur."),
   ("14–26s", "Teks atas skrin: ~2.0 L sehari untuk wanita (termasuk dari makanan)", "EFSA: wanita dewasa perlukan lebih kurang 2.0 liter air sehari, termasuk dari makanan & minuman. 🟢 Terbukti"),
   ("26–38s", "Momyizz tulis tanda masa pada botol, isi dari penapis air di dapur (eSpring kelihatan)", "Trick Momyizz: tanda masa pada botol. Isi semula dari air yang ditapis di rumah, sentiasa sedia. 💧"),
   ("38–45s", "Botol kosong pukul 3 petang, Momyizz senyum", "Bukan paksa diri, cuma permudahkan. 💚 | " + DISC),
  ],
  "caption": "Hari ni korang dah minum berapa gelas? 💧\n\nSumber: EFSA (2010), Dietary Reference Values for water.\n" + DISC + "\n\n#Momyizz #MinumAir #GayaHidupSihat"},
 "carousel": {"tajuk": "Berapa banyak air kita perlu?",
  "slaid": [
   "BERAPA BANYAK AIR KITA PERLU? 💧",
   "WANITA DEWASA\nLebih kurang 2.0 liter sehari (jumlah dari minuman + makanan).\n🟢 Terbukti (EFSA)",
   "LELAKI DEWASA\nLebih kurang 2.5 liter sehari.\n🟢 Terbukti (EFSA)",
   "DARI MAKANAN PUN DIKIRA 🍉\nSup, buah dan sayur menyumbang lebih kurang 20% air harian. (EFSA)",
   "PERLU LEBIH BILA\n• Cuaca panas\n• Banyak berpeluh / bersenam\n• Demam atau cirit-birit\n• Mengandung atau menyusu",
   "SEMAK MUDAH\nAir kencing kuning cair = cukup. Kuning pekat = minum lagi. (NHS)\nSave 🌿\n\n" + DISC,
  ],
  "caption": "Keperluan air harian dalam 6 slaid. Save & kongsi 💧\n\nSumber: EFSA (2010); NHS.\n" + DISC + "\n\n#Momyizz #MinumAir #FaktaKesihatan"},
 "teks": [
  "Info ringkas: makin berumur, rasa dahaga makin kurang. 👵🏻\n\nSebab tu warga emas lebih mudah kurang minum tanpa sedar. Ingatkan mak ayah minum sedikit-sedikit sepanjang hari, jangan tunggu dahaga. (NHS)",
  "Soalan: sampai sekarang, korang dah minum berapa gelas air kosong? 💧\n\n🥛 0–2\n🥛🥛 3–4\n🥛🥛🥛 5–6\n🏆 7 ke atas\n\nMomyizz: 4 setakat ni. Senang sebab air di rumah dah ditapis dengan penapis yang diperakui 4 standard NSF/ANSI. Isi je botol keluli sebelum keluar. 😄",
  "Tips habiskan air tanpa sedar 💡\n\n✅ Tanda masa pada botol: 10 pg, 12 tgh, 3 ptg\n✅ Segelas air sebelum setiap kali makan\n✅ Letak botol dalam pandangan mata, bukan dalam beg\n\nBotol yang nampak = botol yang diminum. 😉",
  "Info penting cuaca panas: minum air dengan kerap walaupun tak dahaga, dan elak aktiviti berat di luar pada waktu paling panas. ⚠️\n\nPening, loya, keliru atau berhenti berpeluh semasa cuaca panas boleh jadi tanda strok haba. Dapatkan rawatan segera. 🙏",
 ]},

# ================================================================ HARI 14
{"d": 14, "ep": 5, "tema": "Cabaran Air 7 hari", "produk": ("espring", "Nak air minuman yang mudah diisi setiap hari untuk cabaran"),
 "video": {"tajuk": "Jom #CabaranAirMomyizz 7 hari", "nota": CERITA + " Sticker: 17-blazer-panggil (babak hook) atau 02-blazer-tunjuk-bawah (babak komen). Babak isi air: eSpring kelihatan; jangan sebut nama dalam sari kata / suara.",
  "babak": [
   ("0–3s", "Momyizz pegang botol keluli, panggil ke kamera", "Jom join #CabaranAirMomyizz 7 hari! 💧"),
   ("3–14s", "Teks atas skrin: 5 waktu solat = 5 gelas", "Trick paling senang: setiap kali lepas solat, segelas air. 5 waktu = 5 gelas."),
   ("14–26s", "Momyizz minum air kosong dulu, baru bancuh kopi", "Tambah segelas sebelum kopi pagi & segelas sebelum tidur. Dah 7!"),
   ("26–38s", "Isi botol dari penapis air di dapur, tick pada kalendar dinding (eSpring kelihatan)", "Momyizz isi dari air yang ditapis di rumah. Tick setiap hari kat kalendar. ✅"),
   ("38–45s", "Momyizz tunjuk ke bawah (ruang komen)", "Komen JOIN, kita buat sama-sama 7 hari! 💚 | " + DISC),
  ],
  "caption": "Komen JOIN kalau nak buat #CabaranAirMomyizz 7 hari dengan Momyizz! 💧\n\nIdea: 5 waktu solat = 5 gelas, + 1 sebelum kopi, + 1 sebelum tidur.\n" + DISC + "\n\n#Momyizz #CabaranAirMomyizz #MinumAir"},
 "carousel": {"tajuk": "Trick 5 waktu solat = 5 gelas",
  "slaid": [
   "#CABARANAIRMOMYIZZ 💧\n7 hari, 7 gelas sehari",
   "SUBUH 🌅\nSegelas air selepas solat. Badan baru bangun, perlukan air.",
   "ZOHOR & ASAR ☀️\nSegelas selepas setiap solat. Waktu tengah hari paling mudah lupa minum.",
   "MAGHRIB & ISYAK 🌙\nSegelas selepas setiap solat.",
   "BONUS +2 ☕\nSegelas sebelum kopi pagi, segelas sebelum tidur.\nJumlah: 7 gelas sehari.",
   "JOM MULA\nTick setiap hari, 7 hari berturut-turut.\nSave & tag kawan 🌿\n\n" + DISC,
  ],
  "caption": "Save carousel ni & tag kawan yang selalu lupa minum air 💧 #CabaranAirMomyizz\n\n" + DISC + "\n\n#Momyizz #CabaranAirMomyizz #MinumAir"},
 "teks": [
  "Info ringkas: tabiat baharu ambil masa. Kajian Lally et al. (2010) dapati purata 66 hari untuk tabiat jadi automatik, antara 18 hingga 254 hari. 🗓️\n\nJadi cabaran 7 hari ni cuma permulaan. Tak sempurna pun tak apa, yang penting sambung esok.",
  "Siapa nak join #CabaranAirMomyizz 7 hari? 💧\n\nKomen JOIN 🙋‍♀️\n\nPeraturan senang: 7 gelas air kosong sehari selama 7 hari. Setiap malam, kongsi tick korang kat komen. Momyizz pun buat sama, isi botol dari air ditapis di rumah. 💪",
  "Tips berjaya cabaran air 7 hari 💡\n\n✅ Letak botol di tempat yang selalu nampak: meja kerja, kereta, sebelah sejadah\n✅ Isi semula terus bila kosong, jangan tunggu dahaga\n✅ Penapis air di rumah = air sentiasa sedia, tak perlu beli air botol\n\nSenang = jadi tabiat. 😉",
  "Info penting: gangguan bekalan air di kawasan korang? ⚠️\n\nSimpan air dalam bekas bersih yang bertutup, guna dalam masa 1–2 hari, dan didihkan sebelum minum jika ragu-ragu. Bila bekalan pulih dan air keruh, biarkan paip mengalir sehingga jernih dulu.",
 ],
 "wa": {"tajuk": "eSpring untuk #CabaranAirMomyizz", "nota": "Ruang tertutup sahaja. Key selling dari AMWAY_BRAND/KEY_SELLING.md (amway.my 122940). Tulis MENGURANGKAN mikroplastik, jangan singkir / bebas. Semak harga & promosi rasmi hari ini.",
  "t": "Hai [nama] 😊\n\nMinggu ni Momyizz buat #CabaranAirMomyizz 7 hari. Ramai tanya: \"Air kat rumah Momyizz guna penapis apa?\"\n\nMomyizz guna *eSpring Water Purifier* (model baharu) dari Amway 💧\n• Diperakui 4 standard NSF/ANSI (42, 53, 55, 401)\n• Kurangkan lebih 170 bahan cemar, sekecil 0.2 mikron\n• Terbukti mengurangkan mikroplastik & 19 jenis sisa farmaseutikal\n• UV-C LED hapuskan 99.9% bakteria, virus & sista bawaan air\n• Aplikasi Amway Healthy Home ingatkan bila perlu tukar penapis\n• Halal, waranti 5 tahun\n\n• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n• Promosi: [promosi rasmi Amway, jika ada]\n• Kenapa Momyizz pilih: [pengalaman sebenar Momyizz]\n\nAir sentiasa sedia di rumah = lebih senang cukupkan minum setiap hari. Nak tahu lebih atau nak demo? Reply \"NAK\". 💛"}},

# ================================================================ HARI 15-30 (rancangan; teks penuh dijana dengan Claude)
# Format: (video, carousel, [teks info, teks pertanyaan, teks tips, teks alert], wa atau None)
{"d": 15, "ep": 5, "tema": "Dehidrasi & letih", "produk": ("bodykey", "Petang blur & lapar, terus capai snek manis"),
 "plan": ("Petang blur: kurang minum ke?", "Tanda badan perlukan air",
          ["Dehidrasi ringan dikaitkan dengan fokus menurun (kajian awal)", "Korang selalu letih pukul berapa?", "Petang: segelas air dulu, kemudian snek berprotein (contoh shake pisang 17g protein, hanya 6g gula) ganti kuih manis", "letih berpanjangan ada banyak punca, jumpa doktor"], None)},
{"d": 16, "ep": 6, "tema": "Rutin kulit 5 minit", "produk": ("cleanser", "Malas cuci muka malam; perlukan pencuci yang lembut & cepat"),
 "plan": ("Pukul 10 malam, 'cuci muka esok je la…'", "Cara cuci muka betul (AAD)",
          ["Air suam, bukan panas", "Rutin malam korang berapa langkah?", "Kit cuci muka 5 minit dalam satu dulang", "jangan tidur dengan mekap"], None)},
{"d": 17, "ep": 6, "tema": "SPF setiap hari", "produk": ("uv", "Skip SPF sebab rasa berminyak"),
 "plan": ("Dulang skincare sebelah sinki", "SPF 30 spektrum luas: kenapa setiap hari (AAD)",
          ["SPF tetap perlu walaupun dalam bangunan dekat tingkap", "Jenis kulit korang apa?", "Sapu SPF sebanyak dua jari untuk muka & leher", "kulit terbakar matahari sampai melepuh, demam atau pening: dapatkan rawatan; elak matahari terik 10 pagi–4 petang"],
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


# ================================================================ VIDEO MOTION GRAFIK (2 sehari)
# Dibina dalam CapCut guna komponen TEMPLATES/MOTION_GRAPHICS_KIT/KOMPONEN.md. Tiada rakaman diperlukan.
# Babak: (masa, komponen kit, teks atas skrin, animasi)
MG_INFO = [("13:30", "Tips"), ("19:30", "Masalah → penyelesaian")]
MG_END = ("22–25s", "PENAFIAN + STICKER", "Save & follow Momyizz 🌿\n" + DISC, "Fade masuk, sticker pop")

MG_FULL = {
1: [
 {"tajuk": "3 tanda botol plastik patut ditukar", "sticker": "13-blazer-tunjuk-atas-kanan", "babak": [
   ("0–3s", "HOOK", "Botol air korang dah patut tukar? 🤔", "Pop 0.3 s"),
   ("3–8s", "CHECKLIST baris 1", "✓ Calar atau kusam", "Baris muncul + SFX ding"),
   ("8–13s", "CHECKLIST baris 2", "✓ Berbau walaupun dah dibasuh", "Baris muncul"),
   ("13–18s", "CHECKLIST baris 3", "✓ Retak atau melengkung", "Baris muncul"),
   ("18–22s", "BIG_WORD", "TUKAR 🔄", "Pop besar"),
   MG_END],
  "caption": "3 tanda botol plastik patut ditukar. Botol korang lulus? 👇\n\n#Momyizz #Mikroplastik #TipsRumah"},
 {"tajuk": "Mitos vs fakta: air dalam botol plastik", "sticker": "04-satin-tutup-mulut", "babak": [
   ("0–3s", "HOOK", "\"Air dalam botol plastik semua beracun!\" Betul ke?", "Pop + goyang kecil"),
   ("3–8s", "BIG_WORD", "MITOS ❌", "Pop besar"),
   ("8–15s", "KAD_FAKTA + LABEL_BUKTI (Bukti belum cukup)", "WHO (2019): tahap mikroplastik semasa dalam air minuman belum tunjuk risiko kesihatan yang jelas. Data masih terhad.", "Kad naik dari bawah"),
   ("15–22s", "CHECKLIST", "Yang boleh buat:\n✓ Guna botol guna semula\n✓ Jangan isi air panas dalam botol sekali guna", "Baris satu per satu"),
   MG_END],
  "caption": "Fakta, bukan panik 🌿\n\nSumber: WHO (2019).\n" + DISC + "\n\n#Momyizz #MitosAtauFakta #Mikroplastik"}],
2: [
 {"tajuk": "3 tips supaya tak lupa bawa tumbler", "sticker": "18-blazer-semangat", "babak": [
   ("0–3s", "HOOK", "Beli tumbler cantik… tapi selalu tertinggal? 😅", "Pop"),
   ("3–9s", "CHECKLIST baris 1", "✓ Letak dekat kunci kereta", "Baris muncul"),
   ("9–15s", "CHECKLIST baris 2", "✓ Basuh malam, terus isi untuk esok", "Baris muncul"),
   ("15–22s", "CHECKLIST baris 3 + NOTA_TANGAN", "✓ Simpan satu lagi di pejabat\n(pelan B!)", "Baris muncul + anak panah lakaran"),
   MG_END],
  "caption": "Tumbler yang dibawa > tumbler yang cantik 😄 Tips korang?\n\n#Momyizz #KurangPlastik #TipsHarian"},
 {"tajuk": "Bekas plastik bertimbun? Susun 3 kotak", "sticker": "19-blazer-thumbs-up", "babak": [
   ("0–3s", "HOOK", "Kabinet penuh bekas plastik? 😩", "Pop"),
   ("3–9s", "KAD_FAKTA (warna Sage)", "KOTAK 1: GUNA\nMasih elok, tiada calar", "Kad masuk dari kiri"),
   ("9–15s", "KAD_FAKTA (warna Linen)", "KOTAK 2: BARANG KERING\nCalar sikit → simpan butang, alat tulis", "Kad masuk dari kanan"),
   ("15–22s", "KAD_FAKTA (warna Kayu)", "KOTAK 3: KITAR SEMULA\nRetak, melengkung, berbau", "Kad masuk dari bawah"),
   MG_END],
  "caption": "Susun bekas plastik dalam 3 kotak. Tak perlu membazir ♻️\n\n#Momyizz #RumahKemas #KurangPlastik"}],
3: [
 {"tajuk": "4 tanda berita kesihatan palsu", "sticker": "14-blazer-tutup-mulut", "babak": [
   ("0–3s", "HOOK", "Sebelum forward, tengok 4 tanda ni 🚩", "Pop"),
   ("3–8s", "CHECKLIST baris 1", "🚩 Tajuk HURUF BESAR & '!!!'", "Baris muncul + SFX"),
   ("8–13s", "CHECKLIST baris 2", "🚩 Tiada nama kajian atau badan rasmi", "Baris muncul"),
   ("13–18s", "CHECKLIST baris 3", "🚩 Janji 'sembuh 100%'", "Baris muncul"),
   ("18–22s", "CHECKLIST baris 4", "🚩 Desak 'SHARE SEGERA'", "Baris muncul"),
   MG_END],
  "caption": "4 tanda berita kesihatan palsu. Save & kongsi dengan group keluarga 📲\n\n#Momyizz #BeritaPalsu #FaktaBukanPanik"},
 {"tajuk": "Group keluarga kongsi berita palsu, macam mana nak tegur?", "sticker": "17-blazer-panggil", "babak": [
   ("0–3s", "HOOK", "Mak kongsi berita palsu dalam group… segan nak tegur? 😬", "Pop"),
   ("3–9s", "BIG_WORD", "JANGAN MALUKAN 🙅‍♀️", "Pop besar"),
   ("9–16s", "SARI_KATA (gaya mesej chat)", "\"Mak, Momyizz terjumpa semakan pasal berita ni. Rupanya tak betul. Ni pautannya 😊\"", "Muncul macam bubble chat"),
   ("16–22s", "NOTA_TANGAN", "Sopan + pautan semakan (sebenarnya.my) = lebih didengar", "Tulisan tangan muncul"),
   MG_END],
  "caption": "Tegur dengan kasih, bukan malukan 💛 Korang pernah buat?\n\n#Momyizz #BeritaPalsu #Keluarga"}],
4: [
 {"tajuk": "Sarapan di kedai? Formula 1+1+1", "sticker": "16-blazer-tunjuk-kanan", "babak": [
   ("0–3s", "HOOK", "Sarapan beli di kedai pun boleh seimbang 🍳", "Pop"),
   ("3–8s", "KAUNTER + teks", "1 protein\n(telur, ikan, kekacang)", "Angka 1 pop"),
   ("8–13s", "KAUNTER + teks", "1 bijirin\n(roti bakar gandum, nasi sederhana)", "Angka 1 pop"),
   ("13–18s", "KAUNTER + teks", "1 buah / sayur\n(pisang, timun, ulam)", "Angka 1 pop"),
   ("18–22s", "NOTA_TANGAN", "Nasi lemak? Tambah telur & timun, kurangkan sambal 😉", "Tulisan tangan"),
   MG_END],
  "caption": "Formula 1+1+1 untuk sarapan di kedai. Korang selalu order apa? 👇\n\n" + DISC + "\n\n#Momyizz #SarapanSihat #PingganSihat"},
 {"tajuk": "Lapar pukul 11, terus capai snek manis?", "sticker": "05-satin-semangat", "babak": [
   ("0–3s", "HOOK", "Pukul 11 dah lapar, terus capai kuih manis? 🍩", "Pop"),
   ("3–9s", "KAD_FAKTA", "Punca biasa: sarapan tanpa protein, atau tak sarapan langsung", "Kad naik"),
   ("9–15s", "CHECKLIST", "Penyelesaian:\n✓ Sarapan ada protein\n✓ Simpan snek berprotein di beg", "Baris satu per satu"),
   ("15–22s", "CHECKLIST", "Contoh snek:\n✓ Kacang\n✓ Telur rebus\n✓ Yogurt tanpa gula tambahan", "Baris satu per satu"),
   MG_END],
  "caption": "Lapar pukul 11? Cuba ni minggu ni 💪\n\n" + DISC + "\n\n#Momyizz #SnekSihat #IbuBekerja"}],
5: [
 {"tajuk": "Oat rendam semalaman: 3 bahan", "sticker": "08-satin-thumbs-up", "babak": [
   ("0–3s", "HOOK", "Sarapan siap sebelum korang bangun 😴", "Pop"),
   ("3–9s", "CHECKLIST baris 1", "1️⃣ ½ cawan oat", "Baris muncul"),
   ("9–15s", "CHECKLIST baris 2", "2️⃣ ½ cawan susu", "Baris muncul"),
   ("15–20s", "CHECKLIST baris 3", "3️⃣ Buah potong (pisang, betik, beri)", "Baris muncul"),
   ("20–22s", "NOTA_TANGAN", "Tutup, simpan dalam peti semalaman ❄️", "Tulisan tangan"),
   MG_END],
  "caption": "Oat rendam semalaman, 3 bahan je. Buah apa korang suka letak? 👇\n\n#Momyizz #SarapanSihat #OvernightOats"},
 {"tajuk": "Pagi selalu lewat? Undur 3 benda ke malam", "sticker": "12-blazer-tunjuk-kiri", "babak": [
   ("0–3s", "HOOK", "Pagi selalu kelam-kabut & lewat? ⏰", "Pop"),
   ("3–8s", "BIG_WORD", "UNDUR KE MALAM 🌙", "Pop besar"),
   ("8–13s", "CHECKLIST baris 1", "✓ Baju kerja & baju sekolah", "Baris muncul"),
   ("13–18s", "CHECKLIST baris 2", "✓ Beg & dokumen tepi pintu", "Baris muncul"),
   ("18–22s", "CHECKLIST baris 3", "✓ Bekal dalam peti, siap ambil", "Baris muncul"),
   MG_END],
  "caption": "3 benda yang Momyizz undur ke malam. Pagi jadi lebih tenang 🌿\n\n#Momyizz #RutinMalam #IbuBekerja"}],
6: [
 {"tajuk": "Tukar minuman manis kepada pilihan lebih baik", "sticker": "19-blazer-thumbs-up", "babak": [
   ("0–3s", "HOOK", "Tak perlu berhenti terus. Tukar sikit-sikit 🔄", "Pop"),
   ("3–9s", "KAD_FAKTA (2 lajur)", "Teh tarik → Teh O kurang manis", "Anak panah bergerak"),
   ("9–15s", "KAD_FAKTA (2 lajur)", "Air kotak → Air kosong + hirisan limau", "Anak panah bergerak"),
   ("15–22s", "KAD_FAKTA (2 lajur)", "Air bergas manis → Air berkarbonat tanpa gula", "Anak panah bergerak"),
   MG_END],
  "caption": "3 tukaran minuman yang mudah. Mana satu korang nak cuba? 👇\n\n" + DISC + "\n\n#Momyizz #KurangManis #GayaHidupSihat"},
 {"tajuk": "Anak minta air manis setiap hari?", "sticker": "03-satin-tunjuk-atas", "babak": [
   ("0–3s", "HOOK", "Anak minta air manis setiap hari? 🧃", "Pop"),
   ("3–9s", "CHECKLIST baris 1", "✓ Kurangkan stok di rumah (tiada = tak minta)", "Baris muncul"),
   ("9–15s", "CHECKLIST baris 2", "✓ Air kosong dalam botol kegemaran anak", "Baris muncul"),
   ("15–22s", "CHECKLIST baris 3 + NOTA_TANGAN", "✓ Air manis untuk 'hari istimewa'\nIbu ayah jadi contoh 💛", "Baris muncul + tulisan tangan"),
   MG_END],
  "caption": "Cara Momyizz kurangkan air manis anak tanpa bergaduh 😅\n\n" + DISC + "\n\n#Momyizz #AnakSihat #KurangManis"}],
7: [
 {"tajuk": "Jadual bersih dapur: harian, mingguan, bulanan", "sticker": "15-blazer-tunjuk-atas-kiri", "babak": [
   ("0–3s", "HOOK", "Dapur bersih tanpa penat sehari suntuk ✨", "Pop"),
   ("3–9s", "KAD_FAKTA (label HARIAN)", "Lap meja · keringkan span · buang sampah basah", "Kad masuk"),
   ("9–15s", "KAD_FAKTA (label MINGGUAN)", "Tukar span · basuh kain lap · lap pemegang peti", "Kad masuk"),
   ("15–22s", "KAD_FAKTA (label BULANAN)", "Bersih dalam peti · buang barang tamat tarikh", "Kad masuk"),
   MG_END],
  "caption": "Jadual bersih dapur ringkas. Save & tampal dekat peti 📌\n\n#Momyizz #DapurBersih #TipsRumah"},
 {"tajuk": "Dapur cepat berbau? Ini puncanya", "sticker": "20-blazer-terkejut-pipi", "babak": [
   ("0–3s", "HOOK", "Dapur cepat berbau walaupun dah kemas? 😷", "Pop"),
   ("3–9s", "KAD_FAKTA", "Punca biasa: sampah basah, sinki lembap, span lama, kain lap basah", "Kad naik"),
   ("9–16s", "CHECKLIST", "Penyelesaian:\n✓ Buang sampah basah setiap hari\n✓ Keringkan sinki selepas guna", "Baris satu per satu"),
   ("16–22s", "CHECKLIST", "✓ Tukar span berkala\n✓ Jemur kain lap sampai kering", "Baris satu per satu"),
   MG_END],
  "caption": "Dapur berbau selalunya bukan sebab tak kemas, tapi sebab lembap 💧\n\n#Momyizz #DapurBersih #TipsRumah"}],
}

# Idea motion grafik hari 8-30: (tips, masalah -> penyelesaian)
MG_PLAN = {
 8: ("4 tempat paling kotor di dapur & cara bersihkan", "Tangan berbau ayam lepas potong? Cara basuh tangan yang betul"),
 9: ("Susun peti sejuk ikut rak: mentah di bawah, siap makan di atas", "Nasi lebih semalam? Cara simpan & panaskan yang selamat"),
 10: ("Cara panaskan lauk dalam microwave sampai panas sekata", "Bekal berkuah tumpah dalam beg? Pilih bekas & cara susun"),
 11: ("Cara simpan sayur potong supaya segar 3 hari", "Bosan bekal sama setiap hari? Putaran 5 menu"),
 12: ("Testimoni vs kajian: bezanya", "Tajuk viral buat panik? 3 langkah bertenang"),
 13: ("Botol air ideal: saiz, bahan & cara basuh", "Kerap ke tandas bila mula minum cukup? Cara atur waktu minum"),
 14: ("Cara jejak cabaran 7 hari: tick kalendar, app atau gelang getah", "Tak suka air kosong? Tambah buah / herba segar"),
 15: ("Air dalam makanan: buah & sup yang membantu", "Letih petang? Semak 4 punca biasa"),
 16: ("Urutan cuci muka malam yang betul (AAD)", "Terlalu penat nak cuci muka? Versi 60 saat"),
 17: ("Berapa banyak SPF patut disapu", "Rasa SPF melekit? Cara pilih tekstur ikut jenis kulit"),
 18: ("Rutin 3 langkah pagi vs malam", "Kulit naik selepas cuba produk baru? Patch test"),
 19: ("Tempat simpan air botol yang betul", "Air botol tertinggal dalam kereta panas? Apa patut buat"),
 20: ("Bila tukar kartrij penapis air", "Air paip keruh selepas hujan lebat? Didih & tunggu jernih"),
 21: ("Rumusan 4 langkah kurangkan plastik", "Rasa terbeban nak ubah semua? Satu tabiat seminggu"),
 22: ("Buah tempatan tinggi vitamin C (jambu, betik, oren)", "Buah cepat rosak? Cara simpan supaya tahan"),
 23: ("Mitos vs fakta: vitamin C & selesema", "Anak tak suka buah? 3 cara hidang yang menarik"),
 24: ("Gandingan makanan bantu serap zat besi", "Minum teh sejurus lepas makan? Jarakkan 1 jam"),
 25: ("Kira minit bergerak seminggu (WHO 150 minit)", "Tiada masa bersenam? Pecahkan kepada 10 minit"),
 26: ("5 cara gerak sambil buat kerja rumah", "Anak asyik skrin? Aktiviti gerak satu keluarga"),
 27: ("3 latihan otot tanpa alat", "Lutut sakit bila squat? Versi lebih mudah & bila jumpa doktor"),
 28: ("Pinggan Glowing: susun ikut warna", "Skincare banyak tapi kusam? Semak 4 tabiat asas"),
 29: ("Sumber omega-3 tempatan & harganya berpatutan", "Anak tak suka ikan? Cara masak yang mudah"),
 30: ("10 tabiat bulan ni dalam 30 saat", "Hilang semangat selepas 30 hari? Pilih 1 untuk diteruskan"),
}


# ================================================================ SIRI TRENDING: TIDUR, OTAK & USUS
# Diilhamkan oleh podcast tidur & otak yang tengah viral (YouTube, Ar Rasyidin Academy Ep 64).
# Isi podcast TIDAK dapat disemak (tiada transkrip); fakta di bawah daripada sumber rasmi sahaja.
# Jangan petik / atribusikan dakwaan kepada penceramah podcast. Susunan dalam kalendar: lihat SUSUNAN di hujung fail
# (diselang setiap 3 hari; produk penyelesai masalah dalam PRODUK_TREND).
TREND_NOTA = "Siri trending: guna podcast tidur & otak yang viral sebagai hook sahaja. Jangan petik nama penceramah atau dakwaan podcast yang belum disemak."

TRENDING = [
{"d": "T1", "ep": None, "tema": "Tidur: masa otak 'membersihkan diri'",
 "video": {"tajuk": "Ramai share podcast tidur & otak, ini yang Momyizz semak", "nota": CERITA + " " + TREND_NOTA + " Sticker: 09-kartun-terkejut-pipi.",
  "babak": [
   ("0–3s", "Telefon tunjuk podcast tidur & otak di FYP, Momyizz tengok sambil baring", "Podcast pasal tidur & otak ni tengah viral. Momyizz pun terus semak kajiannya 🧠"),
   ("3–15s", "Momyizz bercakap ke kamera, bilik suram", "Kajian 2013 dalam jurnal Science: semasa tidur, ruang antara sel otak tikus membesar kira-kira 60%."),
   ("15–28s", "Animasi air mengalir antara sel (Flow)", "Cecair otak mengalir lebih laju dan sisa seperti beta-amiloid dibersihkan lebih cepat."),
   ("28–38s", "Momyizz letak telefon, tutup lampu", "Ini kajian haiwan. Pada manusia masih dikaji. Tapi satu benda dah jelas: tidur bukan sekadar rehat."),
   ("38–45s", "Momyizz habiskan shake pisang sebagai makan malam ringan (BodyKey perisa pisang kelihatan), kemudian tarik selimut", "Malam ni: makan malam ringan (shake GI rendah, 6g gula), tidur awal sikit 🌙 | " + DISC),
  ],
  "caption": "Tidur bukan sekadar rehat 🧠🌙 Siri Tidur, Otak & Usus Momyizz bermula hari ni.\n\nSumber: Xie et al. (2013), Science.\n" + DISC + "\n\n#Momyizz #Tidur #KesihatanOtak #FaktaBukanPanik"},
 "carousel": {"tajuk": "Apa jadi pada otak semasa kita tidur",
  "slaid": [
   "APA JADI PADA OTAK\nsemasa kita tidur? 🧠🌙",
   "OTAK 'MEMBERSIH'\nKajian tikus (Science, 2013): ruang antara sel otak membesar ~60% semasa tidur.\n🟠 Kajian awal (haiwan)",
   "SISA DIBUANG LEBIH CEPAT\nAliran cecair meningkat, sisa seperti beta-amiloid dibersihkan lebih laju.\n🟠 Kajian awal",
   "PADA MANUSIA?\nKajian pada manusia masih berjalan.\n🔵 Masih dikaji",
   "YANG DAH JELAS\nDewasa perlu tidur 7 jam atau lebih setiap malam secara konsisten.\n🟢 Terbukti (AASM)",
   "JADI?\nTidur cukup = sebahagian penjagaan kesihatan.\nSave & follow siri ni 🌿\n\n" + DISC,
  ],
  "caption": "Apa jadi pada otak semasa tidur, versi fakta 🧠\n\nSumber: Xie et al. (2013) Science; AASM/SRS (2015).\n" + DISC + "\n\n#Momyizz #Tidur #KesihatanOtak"},
 "teks": [
  "Info ringkas: pakar tidur (AASM) menyarankan orang dewasa tidur 7 jam atau lebih setiap malam secara konsisten. 🌙\n\nBukan sekali-sekala tidur panjang hujung minggu, tapi setiap malam.",
  "Jujur: semalam korang tidur berapa jam? 😴\n\n😵 Kurang 5 jam\n😐 5–6 jam\n🙂 7–8 jam\n😴 Lebih 8 jam\n\nMomyizz… 6 jam. Masih belajar!",
  "Tips mula tidur awal 15 minit 💡\n\n✅ Minggu ni, masuk tidur 15 minit lebih awal daripada biasa\n✅ Minggu depan, tambah 15 minit lagi\n✅ Set peringatan 'masa tidur' di telefon\n✅ Makan malam ringan, 2–3 jam sebelum tidur. Malam kalut: shake GI rendah, 205 kalori\n\nPerlahan-lahan lebih mudah daripada terus paksa tidur 2 jam awal. 🌙",
  "Info penting: kalau korang selalu berdengkur kuat, tercungap waktu tidur, atau sangat mengantuk siang hari walaupun tidur cukup, jumpa doktor. ⚠️\n\nIni boleh jadi tanda masalah tidur seperti apnea tidur yang perlukan pemeriksaan.",
 ]},

{"d": "T2", "ep": None, "tema": "Berapa jam tidur ibu & anak",
 "video": {"tajuk": "Revenge bedtime: masa untuk diri sendiri yang dicuri dari tidur", "nota": CERITA + " " + TREND_NOTA + " Sticker: 04-satin-tutup-mulut.",
  "babak": [
   ("0–3s", "Jam 12:30 malam, Momyizz scroll telefon atas katil", "Anak dah tidur. Akhirnya masa untuk Momyizz… pukul 12:30 malam 😅"),
   ("3–15s", "Momyizz bercakap ke kamera", "Ada nama untuk ni: 'revenge bedtime'. Kita curi masa tidur untuk rasa ada masa sendiri."),
   ("15–28s", "Pagi: Momyizz menguap, hampir capai kuih manis, tukar kepada shake pisang dalam shaker (BodyKey perisa pisang kelihatan)", "Esoknya? Penat, cepat marah, mengidam manis. Sekarang sarapan Momyizz: shake pisang 17g protein, hanya 6g gula."),
   ("28–40s", "Momyizz baca buku 15 minit pukul 10 malam", "Sekarang Momyizz cuba: 'masa sendiri' 20 minit lepas anak tidur, kemudian terus tidur."),
   ("40–45s", "Momyizz ke kamera", "Masa sendiri penting. Tidur pun penting 💛 | " + DISC),
  ],
  "caption": "Siapa selalu 'revenge bedtime'? 🙋‍♀️ Jom cari cara lebih seimbang.\n\n#Momyizz #IbuBekerja #Tidur #SelfCare"},
 "carousel": {"tajuk": "Berapa jam tidur ikut umur",
  "slaid": [
   "BERAPA JAM TIDUR?\nIkut umur, untuk satu keluarga 😴",
   "DEWASA\n7 jam atau lebih setiap malam\n🟢 Terbukti (AASM)",
   "KANAK-KANAK 6–12 TAHUN\n9–12 jam sehari\n🟢 (AASM, AHA)",
   "REMAJA 13–18 TAHUN\n8–10 jam sehari\n🟢 (AASM, AHA)",
   "TIDUR = KESIHATAN JANTUNG\nAHA (2022) memasukkan tidur dalam 8 perkara utama kesihatan jantung.",
   "MULA MALAM NI\nSatu waktu tidur yang sama untuk semua dalam rumah.\nSave untuk keluarga 🌙\n\n" + DISC,
  ],
  "caption": "Berapa jam tidur yang cukup untuk ibu, ayah dan anak? Save 🌙\n\nSumber: AASM; AHA Life's Essential 8 (2022).\n" + DISC + "\n\n#Momyizz #Tidur #KesihatanKeluarga"},
 "teks": [
  "Info ringkas: American Heart Association (2022) memasukkan tidur sebagai salah satu daripada 8 perkara utama untuk kesihatan jantung, sama penting dengan makan, bergerak dan tekanan darah. ❤️🌙",
  "Soalan: anak korang tidur pukul berapa malam sekolah? 🏫\n\n🕘 Sebelum 9\n🕙 9–10\n🕚 10–11\n🕛 Lepas 11\n\nKongsi kat komen, Momyizz nak tengok purata!",
  "Tips rutin tidur anak (dan ibu sekali) 💡\n\n✅ Waktu tidur sama setiap malam, termasuk hujung minggu (lebih kurang)\n✅ Lampu dimalapkan 30 minit sebelum tidur\n✅ Tiada skrin di atas katil\n✅ Bacaan atau sembang ringan sebagai 'tanda' masa tidur\n✅ Pagi lepas tidur tak cukup: sarapan berprotein, bukan kuih manis (Momyizz: shake 17g protein, 6g gula)",
  "Info penting: mengantuk ketika memandu sangat berbahaya. ⚠️\n\nKalau mata berat semasa memandu, berhenti di tempat selamat dan rehat. Tingkap terbuka atau radio kuat bukan penyelesaian.",
 ]},

{"d": "T3", "ep": None, "tema": "Skrin & cahaya malam",
 "video": {"tajuk": "Telefon tidur di luar bilik", "nota": CERITA + " " + TREND_NOTA + " Sticker: 18-blazer-semangat.",
  "babak": [
   ("0–3s", "Muka diterangi cahaya telefon dalam gelap", "Scroll 'sekejap je'… tiba-tiba dah pukul 1 pagi 📱"),
   ("3–15s", "Momyizz bercakap ke kamera", "Cahaya terang pada waktu malam boleh tekan hormon melatonin, hormon yang bantu kita rasa mengantuk."),
   ("15–28s", "Momyizz cas telefon di dapur, bukan di bilik", "Eksperimen Momyizz minggu ni: telefon dicas di luar bilik."),
   ("28–40s", "Momyizz baca buku, lampu kuning malap", "Ganti dengan buku atau zikir. Malam ketiga, Momyizz tidur lebih cepat."),
   ("40–45s", "Pagi: Momyizz sapu SPF sebelum kerja depan laptop (Artistry UV Protect kelihatan), kemudian ke kamera", "Siang depan skrin: SPF50+ yang juga lindungi daripada cahaya biru. Malam: telefon keluar bilik. Siapa berani cuba 7 hari? 🙋‍♀️ | " + DISC),
  ],
  "caption": "Cabaran 7 hari: telefon tidur di luar bilik. Join? 📱🌙\n\nSumber: Harvard Health Publishing.\n#Momyizz #Tidur #DigitalDetox"},
 "carousel": {"tajuk": "Bilik tidur yang bantu lena",
  "slaid": [
   "BILIK TIDUR YANG BANTU LENA 🛏️\n4 perkara mudah",
   "1. GELAP\nCahaya terang waktu malam boleh tekan melatonin (hormon mengantuk).\n🟢 (Harvard Health)",
   "2. SENYAP & SELESA\nCDC: bilik tidur yang senyap, gelap, tenang dan suhu selesa.",
   "3. TANPA SKRIN\nTutup skrin 30–60 minit sebelum tidur. Cas telefon di luar bilik.",
   "4. KATIL UNTUK TIDUR\nElak buat kerja atau scroll atas katil supaya otak kaitkan katil dengan tidur.",
   "MULA SATU DULU\nPilih satu perubahan malam ni.\nSave & cuba 🌙\n\n" + DISC,
  ],
  "caption": "4 perkara mudah untuk bilik tidur yang bantu lena. Mana satu korang nak cuba? 👇\n\nSumber: CDC; Harvard Health Publishing.\n" + DISC + "\n\n#Momyizz #Tidur #RumahSihat"},
 "teks": [
  "Info ringkas: cahaya terang pada waktu malam, termasuk dari skrin, boleh menekan hormon melatonin yang membantu kita rasa mengantuk. (Harvard Health Publishing) 📱🌙",
  "Jujur: telefon korang tidur di mana malam tadi? 📱\n\n🛏️ Atas katil\n🪑 Meja sebelah katil\n🚪 Luar bilik\n\nMomyizz baru pindah ke luar bilik minggu ni!",
  "Tips kalau telefon perlu ada di bilik (contoh: anak kecil, kerja) 💡\n\n✅ Aktifkan mod 'Jangan ganggu'\n✅ Letak telefon jauh dari katil, skrin ke bawah\n✅ Guna jam loceng biasa supaya tak perlu buka telefon pagi-pagi\n✅ Siang depan skrin: SPF50+ dengan perlindungan cahaya biru, sapu sebelum mula kerja",
  "Info penting untuk ibu bapa: kanak-kanak 6–12 tahun perlukan 9–12 jam tidur sehari (AASM). ⚠️\n\nSkrin di bilik tidur boleh melambatkan waktu tidur anak. Pertimbangkan 'stesen cas keluarga' di ruang tamu.",
 ]},

{"d": "T4", "ep": None, "tema": "Kafein & tidur",
 "video": {"tajuk": "Kopi petang yang curi tidur malam", "nota": CERITA + " " + TREND_NOTA + " Sticker: 14-blazer-tutup-mulut.",
  "babak": [
   ("0–3s", "Kopi ais di meja kerja, jam 4 petang", "Kopi pukul 4 petang… dan tertanya kenapa susah tidur malam 🤔"),
   ("3–15s", "Momyizz bercakap ke kamera", "Satu kajian kecil (2013): kafein yang diambil 6 jam sebelum tidur masih kurangkan tidur hampir sejam."),
   ("15–28s", "Teks atas skrin, Momyizz terkejut", "Yang mengejutkan: peserta tak sedar pun tidur mereka terganggu. 😳"),
   ("28–40s", "Petang: Momyizz goncang shake pisang dalam shaker (BodyKey perisa pisang kelihatan)", "Sekarang kopi terakhir Momyizz sebelum pukul 2 petang. Petang lapar? Shake pisang, 17g protein, hanya 6g gula."),
   ("40–45s", "Momyizz ke kamera", "Kopi tak salah. Masa yang penting ☕ | " + DISC),
  ],
  "caption": "Pukul berapa kopi terakhir korang hari ni? ☕👇\n\nSumber: Drake et al. (2013), J Clin Sleep Med.\n#Momyizz #Kafein #Tidur"},
 "carousel": {"tajuk": "Kafein tersembunyi dalam minuman harian",
  "slaid": [
   "KAFEIN BUKAN DALAM KOPI JE ☕\nTengok senarai ni",
   "KOPI\nSumber kafein paling biasa. Ais atau panas, sama sahaja.",
   "TEH\nTeh tarik, teh O, teh hijau pun ada kafein.",
   "MINUMAN LAIN\nMinuman tenaga, minuman berkola dan coklat juga ada kafein.",
   "KAJIAN 2013\nKafein 6 jam sebelum tidur masih kurangkan tidur hampir sejam (kajian kecil, 12 orang).\n🟠 Kajian awal",
   "PANDUAN MUDAH\nElak kafein sekurang-kurangnya 6 jam sebelum tidur.\nSave 🌙\n\n" + DISC,
  ],
  "caption": "Kafein tersembunyi dalam minuman harian. Save & semak cawan petang korang ☕\n\nSumber: Drake et al. (2013).\n" + DISC + "\n\n#Momyizz #Kafein #Tidur #GayaHidupSihat"},
 "teks": [
  "Info ringkas: kesan kafein boleh bertahan berjam-jam. Kajian 2013 mendapati kafein yang diambil 6 jam sebelum tidur masih mengurangkan tidur, dan peserta sendiri tak sedar. ☕🌙",
  "Soalan: kopi atau teh terakhir korang biasanya pukul berapa? ☕\n\n🌅 Pagi je\n🕑 Sebelum 2 petang\n🕓 Petang\n🌙 Malam pun minum\n\nMomyizz tengah cuba 'sebelum 2 petang'!",
  "Tips kurangkan kafein petang tanpa sakit kepala 💡\n\n✅ Kurangkan perlahan-lahan, contohnya setengah cawan dulu\n✅ Ganti cawan petang dengan air kosong, teh herba tanpa kafein, atau shake pisang (6g gula)\n✅ Minum air kosong cukup sepanjang hari\n\nTerus berhenti mengejut boleh buat sesetengah orang sakit kepala.",
  "Info penting: minuman tenaga mengandungi kafein dan sering tinggi gula. ⚠️\n\nPeriksa label sebelum minum, dan berhati-hati jika hamil, menyusu atau ada masalah jantung. Rujuk doktor jika tidak pasti.",
 ]},

{"d": "T5", "ep": None, "tema": "Usus & otak saling berhubung",
 "video": {"tajuk": "Perut tak selesa, mood pun ikut", "nota": CERITA + " " + TREND_NOTA + " Sticker: 13-blazer-tunjuk-atas-kanan.",
  "babak": [
   ("0–3s", "Momyizz pegang perut, muka muram", "Pernah perasan? Perut tak selesa, mood pun ikut jatuh 😣"),
   ("3–15s", "Animasi garisan antara otak dan usus (Flow)", "Saintis panggil ni 'paksi usus–otak': usus dan otak berhubung melalui saraf, hormon dan bakteria usus."),
   ("15–28s", "Momyizz bercakap ke kamera", "Ada kajian awal kaitkan bakteria usus dengan mood. Tapi pada manusia, masih banyak dikaji."),
   ("28–40s", "Pinggan: sayur, buah, kekacang, bijirin penuh; shaker shake pisang di tepi (BodyKey perisa pisang kelihatan)", "Yang dah jelas: WHO saran serat 25 g sehari dari makanan. Hari tak cukup sayur? Shake pisang Momyizz ada 5g serat prebiotik."),
   ("40–45s", "Momyizz ke kamera", "Jaga usus, mulakan dengan pinggan 🌿 | " + DISC),
  ],
  "caption": "Usus & otak saling berhubung 🧠🌿 Fakta, bukan hype.\n\nSumber: WHO (2023).\n" + DISC + "\n\n#Momyizz #KesihatanUsus #KesihatanOtak"},
 "carousel": {"tajuk": "Cara capai 25 g serat sehari",
  "slaid": [
   "SERAT 25 g SEHARI 🌾\nCara capai tanpa susah",
   "KENAPA?\nWHO (2023): dewasa sekurang-kurangnya 25 g serat semula jadi dari makanan sehari, dan 400 g sayur & buah.\n🟢 Terbukti",
   "PAGI\nOat atau roti gandum penuh + buah",
   "TENGAH HARI\nSeparuh pinggan sayur + kekacang (dal, kacang merah)",
   "SNEK\nBuah segar (jambu, betik, pisang) atau segenggam kacang",
   "INGAT\nTambah serat perlahan-lahan & minum air cukup supaya perut selesa.\nSave 🌿\n\n" + DISC,
  ],
  "caption": "Cara capai 25 g serat sehari ikut WHO. Save & cuba minggu ni 🌾\n\nSumber: WHO (2023).\n" + DISC + "\n\n#Momyizz #Serat #KesihatanUsus #PingganSihat"},
 "teks": [
  "Info ringkas: WHO (2023) menyarankan dewasa ambil sekurang-kurangnya 25 g serat semula jadi dari makanan sehari, bersama 400 g sayur dan buah. 🌾🥦",
  "Soalan: hari ni korang dah makan sayur atau buah berapa hidangan? 🥗\n\n0️⃣ Belum langsung\n1️⃣–2️⃣\n3️⃣–4️⃣\n5️⃣ ke atas\n\nMomyizz baru 2. Malam ni tambah!",
  "Tips tambah serat tanpa perut kembung 💡\n\n✅ Tambah sedikit demi sedikit, satu hidangan seminggu\n✅ Minum air kosong yang cukup\n✅ Pilih pelbagai sumber: sayur, buah, kekacang, bijirin penuh\n✅ Kunyah perlahan\n✅ Hari tak cukup sayur: shake pisang ada 5g serat prebiotik sehidangan",
  "Info penting: sembelit berpanjangan, perubahan tabiat buang air yang mendadak, atau darah dalam najis perlu diperiksa doktor. ⚠️\n\nJangan bergantung pada julap atau teh 'detoks' berulang kali tanpa nasihat.",
 ]},

{"d": "T6", "ep": None, "tema": "Makanan untuk otak: omega-3 & ikan tempatan",
 "video": {"tajuk": "Ikan kembung: makanan otak yang murah", "nota": CERITA + " " + TREND_NOTA + " Sticker: 19-blazer-thumbs-up.",
  "babak": [
   ("0–3s", "Ikan kembung di pasar / dapur", "Makanan otak tak semestinya mahal 🐟"),
   ("3–15s", "Momyizz bercakap ke kamera", "DHA, sejenis omega-3, ialah antara lemak utama dalam struktur otak dan mata (NIH)."),
   ("15–28s", "Momyizz masak ikan kembung / sardin", "Sumbernya: ikan berlemak seperti ikan kembung, sardin dan salmon. Badan hanya hasilkan sedikit sendiri."),
   ("28–40s", "Pinggan keluarga dengan ikan; botol Salmon Omega di kabinet dapur (Nutrilite Salmon Omega Complex kelihatan)", "Matlamat Momyizz: ikan 2 kali seminggu. Minggu yang jarang makan ikan, Momyizz ada pelengkap: 330mg omega-3 sebiji."),
   ("40–45s", "Momyizz ke kamera", "Ikan tempatan pun dah cukup bagus 💛 | " + DISC),
  ],
  "caption": "Makanan otak versi bajet: ikan kembung & sardin 🐟\n\nSumber: NIH Office of Dietary Supplements.\n" + DISC + "\n\n#Momyizz #Omega3 #KesihatanOtak #IkanTempatan"},
 "carousel": {"tajuk": "Omega-3: fakta vs hype",
  "slaid": [
   "OMEGA-3 & OTAK 🧠\nFakta vs hype",
   "FAKTA\nDHA ialah antara lemak utama dalam otak dan retina mata.\n🟢 Terbukti (NIH)",
   "SUMBER\nIkan berlemak: kembung, sardin, salmon, tenggiri.\n🟢 (NIH)",
   "BADAN HASILKAN SEDIKIT\nBadan hanya boleh hasilkan sedikit EPA & DHA sendiri, jadi makanan penting.\n🟢 (NIH)",
   "HYPE?\nSuplemen omega-3 untuk 'tingkatkan daya ingatan' orang sihat: bukti belum cukup.\n🔴 Bukti belum cukup (NIH)",
   "PILIHAN TERBAIK\nMakan ikan 2 kali seminggu.\nSave 🐟\n\n" + DISC,
  ],
  "caption": "Omega-3 & otak: mana fakta, mana hype? Save 🧠\n\nSumber: NIH Office of Dietary Supplements.\n" + DISC + "\n\n#Momyizz #Omega3 #FaktaBukanPanik"},
 "teks": [
  "Info ringkas: DHA, sejenis omega-3, ialah antara lemak utama dalam otak dan retina mata. Sumber terbaik: ikan berlemak seperti ikan kembung dan sardin. (NIH) 🐟🧠",
  "Soalan: keluarga korang makan ikan berapa kali seminggu? 🐟\n\n0️⃣ Jarang\n1️⃣ Sekali\n2️⃣ Dua kali\n3️⃣+ Selalu\n\nMomyizz tengah kejar 'dua kali'!",
  "Tips anak mahu makan ikan 💡\n\n✅ Buang tulang & jadikan isi ikan dalam bubur, nasi goreng atau roti\n✅ Sardin dalam tin: jadikan inti sandwich\n✅ Goreng tepung ringan / bakar dengan sedikit kunyit\n✅ Makan bersama, anak ikut contoh\n✅ Minggu jarang makan ikan: Momyizz ambil pelengkap omega-3 (330mg sebiji) untuk dewasa",
  "Info penting: sedang makan ubat cair darah atau ada masalah pendarahan? ⚠️\n\nTanya doktor atau ahli farmasi sebelum mengambil suplemen minyak ikan / omega-3, kerana ia boleh berinteraksi dengan ubat tertentu. (NIH)",
 ],
 "wa": {"tajuk": "Nutrilite Salmon Omega Complex", "nota": "Ruang tertutup sahaja. Key selling dari AMWAY_BRAND/KEY_SELLING.md (amway.my 103208, semak 18 Nov 2026). TIADA dakwaan otak / ingatan / jantung. Amaran rasmi wajib. Gambar: AMWAY_BRAND/PRODUK/salmon-omega-complex.png. Semak harga hari ini.",
  "t": "Hai [nama] 😊\n\nHari ni Momyizz kongsi pasal ikan tempatan & omega-3. Ada yang tanya, macam mana kalau keluarga jarang makan ikan?\n\nMomyizz utamakan ikan 2 kali seminggu. Untuk minggu yang jarang makan ikan, pelengkap yang Momyizz guna: *Nutrilite Salmon Omega Complex* 🐟\n• Sebiji: 193.51mg EPA + 137.42mg DHA = 330.93mg omega-3\n• Dari salmon perairan sejuk, dengan ikan bilis & sardin\n• Penyulingan molekul berulang untuk ketulenan\n• Dewasa: 1 biji sehari selepas makan · 120 biji sebotol\n• Tiada pewarna, perisa atau pengawet tiruan ditambah\n• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n\n⚠️ Tidak disyorkan untuk kanak-kanak atau yang sedang ambil ubat cair darah. Hamil / menyusu, rujuk doktor dulu. Softgel dari gelatin lembu.\n\nIni pelengkap, bukan pengganti makan ikan. 🙏 Reply \"OMEGA\" kalau nak tahu lebih 💛\n\n" + DISC}},

{"d": "T7", "ep": None, "tema": "Jantung, otak & tidur: rumusan siri",
 "video": {"tajuk": "Apa yang baik untuk jantung, baik untuk otak", "nota": CERITA + " " + TREND_NOTA + " Sticker: 06-satin-lambai-dua-tangan.",
  "babak": [
   ("0–3s", "Momyizz tunjuk nota-nota kecil di peti ais", "Sebulan siri Tidur, Otak & Usus. Ini yang Momyizz belajar 🧠❤️"),
   ("3–15s", "Nota: tidur, skrin, kafein", "Tidur 7 jam+, skrin keluar bilik, kopi terakhir sebelum petang."),
   ("15–28s", "Nota: serat, ikan, bergerak; shaker shake pisang di sebelah peti (BodyKey perisa pisang kelihatan)", "Serat dari sayur & buah, ikan 2 kali seminggu, bergerak setiap hari. Pagi kalut: sarapan GI rendah."),
   ("28–40s", "Momyizz ukur tekanan darah di klinik / rumah", "Dan buat saringan: tekanan darah, gula, kolesterol. Banyak yang tak tahu mereka ada."),
   ("40–45s", "Momyizz melambai", "Terima kasih ikut siri ni 💛 Topik apa seterusnya? | " + DISC),
  ],
  "caption": "Rumusan siri Tidur, Otak & Usus. Mana satu korang dah mula buat? 👇\n\nSumber: AHA Life's Essential 8 (2022); NHMS 2023.\n" + DISC + "\n\n#Momyizz #KesihatanJantung #KesihatanOtak"},
 "carousel": {"tajuk": "Life's Essential 8 (AHA) versi Momyizz",
  "slaid": [
   "8 PERKARA UNTUK JANTUNG & OTAK ❤️🧠\n(AHA Life's Essential 8)",
   "4 TABIAT\n🥗 Makan sihat\n🚶 Bergerak\n🚭 Tiada nikotin\n😴 Tidur cukup",
   "4 NOMBOR UNTUK DISEMAK\n⚖️ Berat badan\n🩸 Tekanan darah\n🍬 Gula darah\n🧈 Kolesterol",
   "MALAYSIA (NHMS 2023)\n29.2% dewasa ada darah tinggi, 33.3% kolesterol tinggi, 15.6% diabetes. Ramai tak tahu.",
   "TINDAKAN\nBuat saringan di klinik kesihatan, walaupun rasa sihat.",
   "MULA DENGAN SATU\nPilih satu tabiat minggu ni.\nSave & kongsi ❤️\n\n" + DISC,
  ],
  "caption": "8 perkara untuk jantung & otak, versi ringkas. Save ❤️🧠\n\nSumber: AHA Life's Essential 8 (2022); NHMS 2023 (KKM).\n" + DISC + "\n\n#Momyizz #KesihatanJantung #Saringan"},
 "teks": [
  "Info ringkas: AHA menyenaraikan 8 perkara utama untuk kesihatan jantung dan otak: makan sihat, bergerak, tiada nikotin, tidur cukup, berat badan, tekanan darah, gula darah dan kolesterol. ❤️🧠",
  "Daripada siri Tidur, Otak & Usus ni, mana satu korang dah cuba? 🙋‍♀️\n\n😴 Tidur awal\n📱 Telefon luar bilik\n☕ Kopi sebelum petang\n🥦 Tambah serat\n🐟 Ikan 2x seminggu\n🍌 Sarapan GI rendah\n\nKomen nombor emoji korang!",
  "Tips buat saringan kesihatan tanpa tangguh 💡\n\n✅ Tetapkan bulan lahir sebagai 'bulan saringan' setiap tahun\n✅ Bawa sekali ibu bapa atau pasangan\n✅ Simpan keputusan dalam satu folder di telefon\n✅ Tanya doktor apa nombor sasaran korang",
  "Info penting: 1 dalam 2 dewasa Malaysia yang ada kolesterol tinggi tidak tahu mereka menghidapnya (NHMS 2023). ⚠️\n\nKolesterol tinggi biasanya tiada simptom. Satu ujian darah boleh beri jawapan.",
 ]},
]

MG_TREND = {
"T1": [
 {"tajuk": "4 tanda korang kurang tidur", "sticker": "20-blazer-terkejut-pipi", "babak": [
   ("0–3s", "HOOK", "Tidur cukup ke sebenarnya? 4 tanda ni 😴", "Pop"),
   ("3–8s", "CHECKLIST baris 1", "✓ Perlu kopi untuk 'hidup' setiap pagi", "Baris muncul"),
   ("8–13s", "CHECKLIST baris 2", "✓ Mengantuk lepas makan tengah hari setiap hari", "Baris muncul"),
   ("13–18s", "CHECKLIST baris 3", "✓ Cepat marah & susah fokus", "Baris muncul"),
   ("18–22s", "CHECKLIST baris 4", "✓ Tidur 'ganti' panjang hujung minggu", "Baris muncul"),
   MG_END],
  "caption": "Berapa tanda korang ada? 👇 Dewasa perlu 7 jam+ (AASM).\n\n#Momyizz #Tidur #IbuBekerja"},
 {"tajuk": "Mitos vs fakta: 'Tidur 5 jam dah cukup, badan dah biasa'", "sticker": "04-satin-tutup-mulut", "babak": [
   ("0–3s", "HOOK", "\"Tidur 5 jam dah cukup, badan dah biasa.\" Betul ke?", "Pop + goyang"),
   ("3–8s", "BIG_WORD", "MITOS ❌", "Pop besar"),
   ("8–15s", "KAD_FAKTA + LABEL_BUKTI (Terbukti)", "Pakar tidur (AASM): dewasa perlu 7 jam atau lebih setiap malam secara konsisten.", "Kad naik"),
   ("15–22s", "CHECKLIST", "Mula dengan:\n✓ Tidur 15 minit lebih awal\n✓ Waktu bangun yang sama", "Baris satu per satu"),
   MG_END],
  "caption": "Badan 'biasa' tak sama dengan badan cukup rehat 😴\n\nSumber: AASM/SRS (2015).\n" + DISC + "\n\n#Momyizz #MitosAtauFakta #Tidur"}],
"T2": [
 {"tajuk": "Rutin 30 minit sebelum tidur", "sticker": "08-satin-thumbs-up", "babak": [
   ("0–3s", "HOOK", "30 minit sebelum tidur, buat ni 🌙", "Pop"),
   ("3–9s", "KAUNTER + teks", "30 min: malapkan lampu", "Angka kira turun"),
   ("9–15s", "KAUNTER + teks", "20 min: telefon dicas di luar bilik", "Angka kira turun"),
   ("15–22s", "KAUNTER + teks", "10 min: baca / zikir / sembang ringan", "Angka kira turun"),
   MG_END],
  "caption": "Rutin 30 minit sebelum tidur ala Momyizz 🌙 Save!\n\n#Momyizz #RutinMalam #Tidur"},
 {"tajuk": "Anak susah tidur malam? Semak 3 perkara", "sticker": "17-blazer-panggil", "babak": [
   ("0–3s", "HOOK", "Anak susah tidur malam? 😩", "Pop"),
   ("3–9s", "KAD_FAKTA", "Kanak-kanak 6–12 tahun perlukan 9–12 jam tidur (AASM)", "Kad naik"),
   ("9–15s", "CHECKLIST", "Semak:\n✓ Skrin dalam bilik?\n✓ Waktu tidur berubah-ubah?", "Baris satu per satu"),
   ("15–22s", "CHECKLIST", "✓ Minuman manis / berkafein petang?\nUbah satu dulu 💛", "Baris muncul"),
   MG_END],
  "caption": "3 perkara untuk disemak bila anak susah tidur 🌙\n\nSumber: AASM.\n" + DISC + "\n\n#Momyizz #AnakSihat #Tidur"}],
"T3": [
 {"tajuk": "Setting telefon untuk malam", "sticker": "16-blazer-tunjuk-kanan", "babak": [
   ("0–3s", "HOOK", "3 setting telefon yang bantu tidur 📱", "Pop"),
   ("3–9s", "CHECKLIST baris 1", "✓ Mod 'Jangan ganggu' automatik 10 malam", "Baris muncul"),
   ("9–15s", "CHECKLIST baris 2", "✓ Mod skrin malam / cahaya hangat", "Baris muncul"),
   ("15–22s", "CHECKLIST baris 3 + NOTA_TANGAN", "✓ Had masa apps media sosial\nTapi paling berkesan: telefon luar bilik 😉", "Baris + tulisan tangan"),
   MG_END],
  "caption": "3 setting telefon untuk malam. Dah cuba? 📱🌙\n\n#Momyizz #DigitalDetox #Tidur"},
 {"tajuk": "Dah baring tapi tak boleh lelap?", "sticker": "05-satin-semangat", "babak": [
   ("0–3s", "HOOK", "Dah baring sejam, mata masih segar? 😳", "Pop"),
   ("3–9s", "BIG_WORD", "JANGAN AMBIL TELEFON 📵", "Pop besar"),
   ("9–16s", "CHECKLIST", "Cuba:\n✓ Bangun, ke ruang lain yang malap\n✓ Buat aktiviti tenang (baca buku)", "Baris satu per satu"),
   ("16–22s", "CHECKLIST", "✓ Kembali ke katil bila mengantuk\nKerap jadi? Jumpa doktor", "Baris muncul"),
   MG_END],
  "caption": "Cara Momyizz bila susah lelap. Korang buat apa? 👇\n\n" + DISC + "\n\n#Momyizz #Tidur #Insomnia"}],
"T4": [
 {"tajuk": "Ganti kopi petang dengan ini", "sticker": "19-blazer-thumbs-up", "babak": [
   ("0–3s", "HOOK", "Mengantuk petang tapi tak nak kopi? ☕", "Pop"),
   ("3–9s", "CHECKLIST baris 1", "✓ Segelas air kosong sejuk", "Baris muncul"),
   ("9–15s", "CHECKLIST baris 2", "✓ Jalan 5 minit / naik tangga", "Baris muncul"),
   ("15–22s", "CHECKLIST baris 3", "✓ Cahaya matahari / tingkap 5 minit", "Baris muncul"),
   MG_END],
  "caption": "3 pengganti kopi petang. Mana satu korang pilih? 👇\n\n#Momyizz #Kafein #TipsHarian"},
 {"tajuk": "Mitos vs fakta: 'Minum kopi malam pun boleh tidur, tak ada kesan'", "sticker": "14-blazer-tutup-mulut", "babak": [
   ("0–3s", "HOOK", "\"Minum kopi malam pun boleh tidur, tak ada kesan.\" 🤔", "Pop"),
   ("3–8s", "BIG_WORD", "BELUM TENTU ⚠️", "Pop besar"),
   ("8–15s", "KAD_FAKTA + LABEL_BUKTI (Kajian awal)", "Kajian 2013: kafein 6 jam sebelum tidur kurangkan tidur hampir sejam, dan peserta tak sedar.", "Kad naik"),
   ("15–22s", "NOTA_TANGAN", "Boleh lelap ≠ tidur berkualiti", "Tulisan tangan"),
   MG_END],
  "caption": "Boleh lelap tak semestinya tidur berkualiti ☕\n\nSumber: Drake et al. (2013).\n" + DISC + "\n\n#Momyizz #MitosAtauFakta #Kafein"}],
"T5": [
 {"tajuk": "5 makanan tinggi serat yang mudah dapat", "sticker": "16-blazer-tunjuk-kanan", "babak": [
   ("0–3s", "HOOK", "5 makanan serat yang ada di dapur korang 🌾", "Pop"),
   ("3–8s", "CHECKLIST baris 1–2", "✓ Oat\n✓ Kacang dal / kacang merah", "Baris muncul"),
   ("8–14s", "CHECKLIST baris 3–4", "✓ Jambu batu / betik\n✓ Sayur hijau (kangkung, sawi)", "Baris muncul"),
   ("14–20s", "CHECKLIST baris 5", "✓ Roti / beras perang", "Baris muncul"),
   ("20–22s", "NOTA_TANGAN", "Sasaran WHO: 25 g sehari", "Tulisan tangan"),
   MG_END],
  "caption": "5 makanan tinggi serat yang mudah dapat 🌾\n\nSumber: WHO (2023).\n#Momyizz #Serat #KesihatanUsus"},
 {"tajuk": "Perut kembung bila mula makan sihat?", "sticker": "10-satin-terkejut-pipi", "babak": [
   ("0–3s", "HOOK", "Mula makan sayur banyak, perut terus kembung? 😣", "Pop"),
   ("3–9s", "KAD_FAKTA", "Punca biasa: tambah serat terlalu banyak, terlalu cepat", "Kad naik"),
   ("9–16s", "CHECKLIST", "Penyelesaian:\n✓ Tambah perlahan, satu hidangan seminggu\n✓ Minum air cukup", "Baris satu per satu"),
   ("16–22s", "CHECKLIST", "✓ Kunyah perlahan\nSakit berterusan? Jumpa doktor", "Baris muncul"),
   MG_END],
  "caption": "Perut kembung bila mula makan sihat? Ini sebabnya 🌿\n\n" + DISC + "\n\n#Momyizz #KesihatanUsus #Serat"}],
"T6": [
 {"tajuk": "3 cara masak ikan untuk keluarga sibuk", "sticker": "18-blazer-semangat", "babak": [
   ("0–3s", "HOOK", "Ikan 2 kali seminggu, cara orang sibuk 🐟", "Pop"),
   ("3–9s", "KAD_FAKTA (1)", "Ikan bakar air fryer + kunyit + garam: 15 minit", "Kad masuk"),
   ("9–15s", "KAD_FAKTA (2)", "Sardin tin + bawang + cili: inti roti / nasi", "Kad masuk"),
   ("15–22s", "KAD_FAKTA (3)", "Sup ikan + sayur: satu periuk untuk semua", "Kad masuk"),
   MG_END],
  "caption": "3 cara masak ikan untuk keluarga sibuk. Mana favourite korang? 🐟\n\n#Momyizz #IkanTempatan #Omega3"},
 {"tajuk": "Mitos vs fakta: 'Minyak ikan buat anak terus pandai'", "sticker": "04-satin-tutup-mulut", "babak": [
   ("0–3s", "HOOK", "\"Minyak ikan buat anak terus pandai.\" Betul ke? 🤔", "Pop"),
   ("3–8s", "BIG_WORD", "BELUM TERBUKTI ⚠️", "Pop besar"),
   ("8–15s", "KAD_FAKTA + LABEL_BUKTI (Bukti belum cukup)", "Bukti suplemen omega-3 untuk tingkatkan kecerdasan kanak-kanak sihat masih belum cukup (NIH).", "Kad naik"),
   ("15–22s", "CHECKLIST", "Yang terbukti bantu:\n✓ Makanan seimbang (termasuk ikan)\n✓ Tidur cukup\n✓ Aktiviti fizikal", "Baris satu per satu"),
   MG_END],
  "caption": "Tiada jalan pintas untuk 'pandai' 💛 Asas tetap paling penting.\n\nSumber: NIH ODS.\n" + DISC + "\n\n#Momyizz #MitosAtauFakta #AnakSihat"}],
"T7": [
 {"tajuk": "Checklist saringan kesihatan tahunan", "sticker": "15-blazer-tunjuk-atas-kiri", "babak": [
   ("0–3s", "HOOK", "Bila kali terakhir korang buat saringan? 🩺", "Pop"),
   ("3–9s", "CHECKLIST baris 1–2", "✓ Tekanan darah\n✓ Gula darah", "Baris muncul"),
   ("9–15s", "CHECKLIST baris 3–4", "✓ Kolesterol\n✓ Berat & ukur lilit pinggang", "Baris muncul"),
   ("15–22s", "NOTA_TANGAN", "Klinik kesihatan berdekatan boleh bantu 💛", "Tulisan tangan"),
   MG_END],
  "caption": "Checklist saringan tahunan. Save & tetapkan 'bulan saringan' korang 🩺\n\n#Momyizz #Saringan #KesihatanJantung"},
 {"tajuk": "Nak ubah semua tabiat sekali gus? Ini kenapa selalu gagal", "sticker": "05-satin-semangat", "babak": [
   ("0–3s", "HOOK", "Nak tidur awal, makan sihat, bersenam… semua serentak? 😵", "Pop"),
   ("3–9s", "KAD_FAKTA", "Terlalu banyak perubahan serentak = cepat penat & berhenti", "Kad naik"),
   ("9–16s", "BIG_WORD", "SATU TABIAT SEMINGGU", "Pop besar"),
   ("16–22s", "CHECKLIST", "Minggu 1: tidur 15 min awal\nMinggu 2: telefon luar bilik\nMinggu 3: ikan 2x", "Baris satu per satu"),
   MG_END],
  "caption": "Satu tabiat seminggu. Perlahan tapi kekal 🌿 Korang mula dengan apa?\n\n#Momyizz #TabiatSihat #IbuBekerja"}],
}


# ================================================================ TAMBAHAN SIRI TRENDING (selepas transkrip podcast disemak)
# Topik di bawah dipilih daripada isi sebenar podcast (lihat PODCAST_SEMAKAN.md). Fakta dari sumber rasmi sahaja.
TRENDING_BARU = [
{"d": "N1", "ep": None, "tema": "Bilik tidur & posisi tidur yang bantu lena",
 "video": {"tajuk": "5 benda yang Momyizz ubah dalam bilik tidur", "nota": CERITA + " " + TREND_NOTA + " Sticker: 19-blazer-thumbs-up.",
  "babak": [
   ("0–3s", "Bilik tidur malam, Momyizz pegang telefon & remote aircond", "Tidur 8 jam tapi bangun macam tak tidur? Semak bilik korang 🛏️"),
   ("3–15s", "Momyizz cas telefon di luar bilik, padam lampu tidur", "Satu: telefon keluar bilik. Dua: bilik gelap, tiada lampu tidur."),
   ("15–27s", "Momyizz laras suhu bilik, kemudian cuci muka di sinki (Artistry Balancing Jelly Cleanser kelihatan)", "Tiga: bilik sejuk dan selesa. Empat: mandi suam atau ambil wuduk, cuci muka dengan pencuci yang tak mengeringkan kulit."),
   ("27–38s", "Momyizz baring mengiring", "Lima: kalau selalu berdengkur, cuba tidur mengiring. Tidur telentang boleh buat dengkur lebih teruk."),
   ("38–45s", "Momyizz tarik selimut, senyum", "Ubah satu dulu malam ni 🌙 | " + DISC),
  ],
  "caption": "5 perubahan kecil dalam bilik tidur Momyizz. Mana satu korang nak cuba? 👇\n\nSumber: CDC; AASM.\n" + DISC + "\n\n#Momyizz #Tidur #BilikTidur"},
 "carousel": {"tajuk": "Bilik tidur ideal: fakta vs viral",
  "slaid": [
   "BILIK TIDUR IDEAL 🛏️\nFakta vs viral",
   "GELAP & SENYAP\nCDC: bilik tidur yang gelap, senyap dan selesa bantu tidur.\n🟢 Terbukti",
   "SEJUK\nBilik yang sejuk dan selesa bantu lena. Kajian kecil (2014): bilik 19°C sebulan tingkatkan 'lemak perang'.\n🟠 Kajian awal",
   "MANDI SUAM\nMandi suam 1–2 jam sebelum tidur boleh bantu lebih cepat lelap.\n🟠 Kajian (2019)",
   "MULUT DIPLASTER?\nViral, tapi kajian 2025: bukti sedikit dan ada risiko jika hidung tersumbat.\n🔴 Bukti belum cukup",
   "BERDENGKUR TERUK?\nCuba tidur mengiring & jumpa doktor untuk saringan apnea tidur.\nSave 🌙\n\n" + DISC,
  ],
  "caption": "Bilik tidur ideal ikut fakta. Save & semak bilik korang 🛏️\n\nSumber: CDC; Lee et al. (2014); Haghayegh et al. (2019); PLOS One (2025).\n" + DISC + "\n\n#Momyizz #Tidur #FaktaBukanPanik"},
 "teks": [
  "Info ringkas: CDC menyarankan bilik tidur yang senyap, gelap, tenang dan suhu yang selesa. Empat perkara ini nampak mudah, tapi ramai terlepas satu atau dua. 🛏️",
  "Soalan: korang tidur posisi apa? 😴\n\n⬆️ Telentang\n⬅️ Mengiring kiri\n➡️ Mengiring kanan\n⬇️ Meniarap\n\nMomyizz mengiring kanan, tapi selalu bangun dah telentang. 😂",
  "Tips bilik lebih gelap tanpa belanja besar 💡\n\n✅ Tutup lampu tidur, guna lampu kecil di koridor jika perlu\n✅ Langsir tebal atau tampal kertas gelap di tingkap\n✅ Tutup cahaya LED dari charger & TV\n✅ Penutup mata pun boleh\n✅ Rutin sebelum tidur: cuci muka dengan pencuci lembut yang tak mengeringkan kulit, terus tutup lampu",
  "Info penting: plaster mulut waktu tidur tengah viral. ⚠️\n\nKajian ulasan 2025 dapati buktinya sedikit, dan ia boleh berbahaya jika hidung tersumbat. Kalau selalu bernafas ikut mulut atau berdengkur kuat, jumpa doktor dulu.",
 ]},

{"d": "N2", "ep": None, "tema": "Tidur sekejap (nap) 20–30 minit",
 "video": {"tajuk": "Ganti 'lunch berat' dengan nap 20 minit", "nota": CERITA + " " + TREND_NOTA + " Sticker: 08-satin-thumbs-up.",
  "babak": [
   ("0–3s", "Momyizz menguap depan laptop pukul 2 petang", "Pukul 2 petang, mata dah berat… 😪"),
   ("3–15s", "Teks atas skrin + animasi kapal terbang (Flow)", "Kajian NASA (1995): juruterbang yang tidur sekejap ~26 minit, kewaspadaan naik sehingga 54%."),
   ("15–28s", "Momyizz set penggera 20 minit, baring di bilik rehat", "Rahsianya: pendek. Lebih 30 minit, bangun boleh jadi lebih mamai."),
   ("28–40s", "Hari WFH: Momyizz bangun, isi segelas air dari penapis di dapur (eSpring kelihatan), sambung kerja", "Bangun, segelas air, gerak sikit. Dan buat awal petang, bukan lewat petang, supaya tak ganggu tidur malam."),
   ("40–45s", "Momyizz ke kamera", "Nap pendek, bukan nap panjang 😉 | " + DISC),
  ],
  "caption": "Nap 20–30 minit: rahsia petang lebih segar. Korang team nap atau team kopi? 👇\n\nSumber: NASA (Rosekind et al.).\n#Momyizz #Nap #IbuBekerja"},
 "carousel": {"tajuk": "Cara nap yang betul",
  "slaid": [
   "NAP YANG BETUL 😴\nSupaya bangun segar, bukan mamai",
   "BERAPA LAMA?\n20–30 minit. Kajian NASA: ~26 minit tingkatkan kewaspadaan sehingga 54% (juruterbang).\n🟢 Kajian",
   "BILA?\nAwal petang. Nap lewat petang boleh ganggu tidur malam.",
   "KENAPA BUKAN LAMA?\nNap panjang boleh buat 'mamai' (sleep inertia) selepas bangun.",
   "TAK BOLEH LELAP?\nBaring rehat mata 10–20 minit pun membantu badan berehat.",
   "INGAT\nNap bukan pengganti tidur malam yang cukup.\nSave 😴\n\n" + DISC,
  ],
  "caption": "Cara nap yang betul supaya bangun segar. Save 😴\n\nSumber: NASA Ames (Rosekind et al.).\n" + DISC + "\n\n#Momyizz #Nap #Tidur"},
 "teks": [
  "Info ringkas: kajian NASA dapati juruterbang yang tidur sekejap kira-kira 26 minit menunjukkan kewaspadaan meningkat sehingga 54% berbanding yang tak tidur. 😴✈️",
  "Soalan: korang sempat nap tak waktu kerja? 😪\n\n✅ Selalu\n🙂 Kadang-kadang\n❌ Tak pernah\n🙈 Nap dalam kereta masa rehat\n\nMomyizz: kadang-kadang, dalam kereta! 😂",
  "Tips nap di pejabat 💡\n\n✅ Set penggera 20 minit\n✅ Guna penutup mata atau kain gelap\n✅ Kalau minum kopi, minum sebelum nap (kopi ambil masa untuk berkesan)\n✅ Bangun, segelas air & gerak sikit (Momyizz isi dari penapis yang diperakui 4 standard NSF/ANSI)",
  "Info penting: mengantuk teruk setiap hari walaupun tidur malam cukup boleh jadi tanda masalah tidur. ⚠️\n\nJangan terus tambah kopi. Jumpa doktor; klinik tidur di hospital boleh buat kajian tidur dengan surat rujukan doktor.",
 ]},

{"d": "N3", "ep": None, "tema": "Pewarna, pemanis & MSG: fakta vs viral",
 "video": {"tajuk": "Momyizz baca label snek anak", "nota": CERITA + " " + TREND_NOTA + " Sticker: 14-blazer-tutup-mulut.",
  "babak": [
   ("0–3s", "Momyizz terbalikkan paket snek warna-warni", "Snek warna-warni ni… apa sebenarnya dalam dia? 🤔"),
   ("3–15s", "Close-up label kod E (pewarna)", "Kajian Southampton (2007): campuran pewarna tiruan tertentu dikaitkan dengan hiperaktif pada sesetengah kanak-kanak."),
   ("15–28s", "Momyizz pegang minuman 'zero sugar'", "Pemanis tiruan? WHO (2023) tak syorkan ia untuk kawal berat badan."),
   ("28–40s", "Momyizz susun snek buah & kacang", "MSG pula diklasifikasikan selamat oleh FDA pada jumlah biasa. Yang penting: kurangkan makanan ultra-proses."),
   ("40–45s", "Momyizz ke kamera", "Baca label, bukan panik 🌿 | " + DISC),
  ],
  "caption": "Pewarna, pemanis, MSG: mana fakta, mana viral? 🌿\n\nSumber: McCann et al. (2007) Lancet; WHO (2023); FDA.\n" + DISC + "\n\n#Momyizz #BacaLabel #FaktaBukanPanik"},
 "carousel": {"tajuk": "3 bahan tambahan: apa kata kajian",
  "slaid": [
   "PEWARNA, PEMANIS & MSG 🧪\nApa kata kajian?",
   "PEWARNA TIRUAN\nKajian 2007 (Lancet): campuran pewarna tertentu + pengawet dikaitkan dengan hiperaktif pada sesetengah kanak-kanak.\n🟠 Kajian",
   "PEMANIS TIRUAN\nWHO (2023): tidak disyorkan untuk mengawal berat badan.\nKesan pada bakteria usus: 🟠 Kajian awal",
   "MSG\nFDA: diiktiraf selamat pada jumlah biasa. Dakwaan 'MSG rosakkan otak': 🔴 Bukti belum cukup",
   "GULA 'SIHAT'?\nGula kelapa, madu, gula perang tetap gula bebas. WHO: hadkan bawah 10% tenaga harian.",
   "PILIHAN TERBAIK\nLebih banyak makanan sebenar, kurang makanan ultra-proses.\nSave 🌿\n\n" + DISC,
  ],
  "caption": "Fakta ringkas tentang pewarna, pemanis & MSG. Save sebelum shopping 🛒\n\nSumber: McCann et al. (2007); WHO (2023); FDA.\n" + DISC + "\n\n#Momyizz #BacaLabel #MakananSihat"},
 "teks": [
  "Info ringkas: WHO (2023) tidak mengesyorkan pemanis tiruan untuk mengawal berat badan. Air kosong tetap pilihan terbaik untuk hilangkan dahaga. 💧",
  "Soalan jujur: korang baca label sebelum beli snek anak? 🛒\n\n✅ Selalu\n🙂 Kadang-kadang\n❌ Tak pernah\n\nMomyizz baru mula minggu ni, dan terkejut! 😳",
  "Tips baca label dalam 10 saat 💡\n\n✅ Senarai ramuan disusun dari paling banyak ke paling sedikit\n✅ Gula di 3 tempat pertama? Fikir dua kali\n✅ Senarai panjang dengan nama susah disebut = makanan sangat diproses\n✅ Pilih yang ramuannya pendek",
  "Info penting untuk ibu bapa: kalau anak nampak lebih hiperaktif selepas makan snek berwarna terang, cuba kurangkan dan perhatikan. ⚠️\n\nKesan berbeza pada setiap anak (Southampton, 2007). Rujuk doktor jika risau tentang tingkah laku anak.",
 ]},

{"d": "N4", "ep": None, "tema": "Sarapan untuk otak: telur, oat & bijirin",
 "video": {"tajuk": "Telur setiap pagi: kebiasaan lama yang ada sains", "nota": CERITA + " " + TREND_NOTA + " Sticker: 18-blazer-semangat.",
  "babak": [
   ("0–3s", "Telur separuh masak + roti gandum, kicap sikit", "Dulu mak suruh makan telur setiap pagi. Rupanya ada sains 🥚"),
   ("3–15s", "Momyizz bercakap ke kamera", "Kuning telur kaya kolin. Badan guna kolin untuk hasilkan asetilkolin, bahan kimia otak untuk ingatan dan otot (NIH)."),
   ("15–28s", "Momyizz masak oat dengan buah", "Oat dan barli pula ada beta-glukan, serat yang bantu kurangkan kolesterol LDL."),
   ("28–40s", "Pinggan sarapan lengkap; hari lain, paket shake pisang + shaker (BodyKey perisa pisang kelihatan)", "Telur + bijirin penuh + buah. Pagi kalut: shake pisang, 17g protein + 20 vitamin & mineral, siap 1 minit."),
   ("40–45s", "Momyizz ke kamera", "Sarapan otak tak perlu mahal 💛 | " + DISC),
  ],
  "caption": "Sarapan untuk otak versi bajet: telur, oat, buah 🥚🥣\n\nSumber: NIH Office of Dietary Supplements.\n" + DISC + "\n\n#Momyizz #SarapanSihat #KesihatanOtak"},
 "carousel": {"tajuk": "4 makanan sarapan & fungsinya",
  "slaid": [
   "SARAPAN UNTUK OTAK 🧠\n4 makanan & fungsinya",
   "TELUR\nKuning telur kaya kolin, diperlukan untuk menghasilkan asetilkolin (NIH).\n🟢 Terbukti",
   "OAT & BARLI\nBeta-glukan, serat yang bantu kurangkan kolesterol LDL.\n🟢 Terbukti",
   "PISANG, IKAN, KEKACANG\nSumber vitamin B6, diperlukan untuk menghasilkan bahan kimia otak (NIH).\n🟢 Terbukti",
   "COKLAT GELAP?\nFlavanol koko & ingatan: kajian kecil. Coklat tetap ada gula & kalori.\n🟠 Kajian awal",
   "FORMULA MUDAH\nProtein + bijirin penuh + buah.\nSave 🥚\n\n" + DISC,
  ],
  "caption": "4 makanan sarapan untuk otak, dengan label bukti. Save 🧠\n\nSumber: NIH ODS (kolin, vitamin B6); FDA (beta-glukan).\n" + DISC + "\n\n#Momyizz #SarapanSihat #FaktaBukanPanik"},
 "teks": [
  "Info ringkas: kuning telur antara sumber kolin terbaik. Badan guna kolin untuk menghasilkan asetilkolin, bahan kimia yang penting untuk ingatan dan pergerakan otot. (NIH) 🥚",
  "Soalan: telur pagi korang suka macam mana? 🥚\n\n🍳 Goreng\n🥚 Rebus\n🫕 Separuh masak\n🍳 Dadar dengan sayur\n\nMomyizz: separuh masak + kicap! 😋",
  "Tips telur dadar penuh sayur dalam 5 minit 💡\n\n✅ 2 biji telur + bawang + sawi / bayam cincang\n✅ Tambah sedikit lada hitam\n✅ Masak dengan minyak sedikit\n✅ Makan dengan roti gandum\n\nProtein + sayur dalam satu pinggan! Pagi tak sempat masak: shake pisang 17g protein. 🍌",
  "Info penting: produk 'pil minda' atau 'booster otak' banyak dijual. ⚠️\n\nSemak nombor pendaftaran MAL dan dakwaannya. Tiada pil yang menggantikan tidur cukup, makanan seimbang dan bergerak.",
 ]},

{"d": "N5", "ep": None, "tema": "Media sosial, notifikasi & anak",
 "video": {"tajuk": "Anak tiru apa kita buat, bukan apa kita cakap", "nota": CERITA + " " + TREND_NOTA + " Sticker: 04-satin-tutup-mulut.",
  "babak": [
   ("0–3s", "Momyizz scroll telefon, anak di sebelah juga pegang tablet", "\"Jangan main telefon lama-lama!\" kata Momyizz… sambil pegang telefon 😅"),
   ("3–15s", "Momyizz letak telefon, tengok anak", "Anak tak ikut apa kita cakap. Anak ikut apa kita buat."),
   ("15–28s", "Notifikasi berbunyi berkali-kali (Flow)", "Apps direka untuk tarik perhatian: setiap notifikasi buat kita nak tengok lagi."),
   ("28–40s", "Keluarga makan tanpa telefon, 'bakul telefon' di tepi", "Sekarang rumah Momyizz ada 'bakul telefon' waktu makan malam."),
   ("40–45s", "Momyizz & anak ketawa bersama", "Mula dari kita dulu 💛"),
  ],
  "caption": "Anak tiru apa kita buat. Siapa nak cuba 'bakul telefon' waktu makan? 🙋‍♀️\n\n#Momyizz #Parenting #DigitalDetox"},
 "carousel": {"tajuk": "Media sosial & kesihatan mental anak",
  "slaid": [
   "MEDIA SOSIAL & ANAK 📱\nApa yang ibu bapa perlu tahu",
   "AMARAN RASMI\nSurgeon General AS (2023): remaja yang guna media sosial lebih 3 jam sehari berdepan risiko 2 kali ganda simptom depresi & kebimbangan.",
   "DIREKA UNTUK TARIK PERHATIAN\nNotifikasi, scroll tanpa henti dan 'like' buat kita mahu kembali lagi.",
   "PERBANDINGAN\nMelihat 'hidup sempurna' orang lain boleh buat rasa tak cukup.",
   "LANGKAH KELUARGA\n• Tiada telefon waktu makan & di bilik tidur\n• Matikan notifikasi tak penting\n• Aktiviti luar bersama",
   "MULA DENGAN KITA\nAnak ikut apa kita buat.\nSave 💛\n\n" + DISC,
  ],
  "caption": "Media sosial & kesihatan mental anak, panduan ringkas untuk ibu bapa 📱\n\nSumber: US Surgeon General Advisory (2023).\n" + DISC + "\n\n#Momyizz #Parenting #KesihatanMental"},
 "teks": [
  "Info ringkas: Surgeon General Amerika (2023) memberi amaran, remaja yang menggunakan media sosial lebih 3 jam sehari berdepan risiko dua kali ganda simptom depresi dan kebimbangan. 📱",
  "Soalan: berapa jam korang guna telefon semalam? (semak 'Screen Time' 👀)\n\n📱 Bawah 2 jam\n📱📱 2–4 jam\n📱📱📱 4–6 jam\n🙈 Lebih 6 jam\n\nMomyizz semak… 5 jam. Malu! 😅",
  "Tips bercakap supaya anak betul-betul dengar 💡\n\n✅ Turun separas mata anak\n✅ Panggil nama, tunggu dia pandang\n✅ Cakap ringkas dengan contoh visual (\"macam semalam Amin kemas buku\")\n✅ Bercerita, bukan berleter",
  "Info penting: kalau anak sangat marah, murung atau tak boleh berfungsi tanpa gajet, dan ia berlarutan, dapatkan bantuan profesional. ⚠️\n\nKlinik kesihatan dan kaunselor sekolah boleh jadi langkah pertama.",
 ]},

{"d": "N6", "ep": None, "tema": "Jaga otak dari sekarang: 14 faktor demensia",
 "video": {"tajuk": "Demensia bukan hanya masalah orang tua", "nota": CERITA + " " + TREND_NOTA + " Sticker: 09-kartun-terkejut-pipi.",
  "babak": [
   ("0–3s", "Momyizz cari kunci, buka peti, lupa nak ambil apa", "Masuk dapur… lupa nak ambil apa. Normal ke? 😅"),
   ("3–15s", "Momyizz bercakap ke kamera", "Lupa sekali-sekala biasa. Tapi perubahan dalam otak untuk Alzheimer boleh bermula bertahun-tahun sebelum simptom."),
   ("15–28s", "Senarai faktor muncul (Flow / teks)", "Laporan Lancet (2024): 14 faktor yang boleh diubah, dan hampir 45% kes demensia berpotensi dicegah atau dilewatkan."),
   ("28–40s", "Momyizz berjalan pagi, ukur tekanan darah", "Antaranya: bergerak, kawal tekanan darah, gula & kolesterol, jaga pendengaran, kekal bersosial."),
   ("40–45s", "Momyizz ke kamera", "Apa yang kita buat hari ni, itulah otak kita esok 💛 | " + DISC),
  ],
  "caption": "Jaga otak dari umur 30-an & 40-an 🧠\n\nSumber: Lancet Commission (2024); Alzheimer's Association.\n" + DISC + "\n\n#Momyizz #KesihatanOtak #Demensia"},
 "carousel": {"tajuk": "14 faktor demensia yang boleh diubah (Lancet 2024)",
  "slaid": [
   "14 FAKTOR DEMENSIA 🧠\nYang boleh diubah (Lancet 2024)",
   "HAMPIR 45%\nkes demensia berpotensi dicegah atau dilewatkan jika faktor-faktor ini ditangani.\n🟢 (anggaran model)",
   "BADAN\nTekanan darah tinggi · diabetes · kolesterol LDL tinggi · obesiti · kurang bergerak",
   "GAYA HIDUP\nMerokok · alkohol berlebihan · pencemaran udara · kecederaan kepala",
   "DERIA & MINDA\nHilang pendengaran · hilang penglihatan tidak dirawat · depresi · terpencil sosial · kurang pendidikan",
   "MULA DENGAN SATU\nBerjalan, saringan tekanan darah, periksa pendengaran & mata.\nSave 🧠\n\n" + DISC,
  ],
  "caption": "14 faktor demensia yang boleh diubah. Save & kongsi dengan ibu bapa 🧠\n\nSumber: Livingston et al., Lancet (2024).\n" + DISC + "\n\n#Momyizz #KesihatanOtak #Saringan"},
 "teks": [
  "Info ringkas: laporan Lancet (2024) menyenaraikan 14 faktor risiko demensia yang boleh diubah, termasuk tekanan darah tinggi, diabetes, kurang bergerak dan hilang pendengaran. Hampir 45% kes berpotensi dicegah atau dilewatkan. 🧠",
  "Soalan: bila kali terakhir ibu bapa korang periksa pendengaran atau mata? 👂👀\n\n✅ Tahun ni\n🙂 Beberapa tahun lepas\n❌ Tak pernah\n\nMomyizz baru sedar ayah tak pernah periksa pendengaran.",
  "Tips berjalan untuk otak & mood 💡\n\n✅ Mula 10 minit selepas makan\n✅ Ajak pasangan / anak / ibu bapa\n✅ Tambah 5 minit setiap minggu\n\nKajian BMJ (2024): berjalan atau berjoging antara senaman paling berkesan untuk simptom depresi.",
  "Info penting: lupa yang semakin kerap dan mengganggu kehidupan harian (contoh: sesat di tempat biasa, ulang soalan sama) bukan sekadar 'faktor umur'. ⚠️\n\nBawa ibu bapa berjumpa doktor untuk pemeriksaan awal.",
 ]},
]

MG_TREND.update({
"N1": [
 {"tajuk": "4 penganggu tidur dalam bilik", "sticker": "16-blazer-tunjuk-kanan", "babak": [
   ("0–3s", "HOOK", "4 benda dalam bilik yang curi tidur korang 🛏️", "Pop"),
   ("3–8s", "CHECKLIST baris 1", "📱 Telefon & notifikasi", "Baris muncul"),
   ("8–13s", "CHECKLIST baris 2", "💡 Lampu tidur / cahaya LED", "Baris muncul"),
   ("13–18s", "CHECKLIST baris 3", "🥵 Bilik panas", "Baris muncul"),
   ("18–22s", "CHECKLIST baris 4", "🔊 Bunyi bising", "Baris muncul"),
   MG_END],
  "caption": "Berapa banyak ada dalam bilik korang? 👇\n\nSumber: CDC.\n#Momyizz #Tidur #BilikTidur"},
 {"tajuk": "Mitos vs fakta: 'Plaster mulut buat tidur lebih nyenyak'", "sticker": "04-satin-tutup-mulut", "babak": [
   ("0–3s", "HOOK", "\"Plaster mulut buat tidur lebih nyenyak!\" Betul ke? 🤐", "Pop"),
   ("3–8s", "BIG_WORD", "BELUM TERBUKTI ⚠️", "Pop besar"),
   ("8–15s", "KAD_FAKTA + LABEL_BUKTI (Bukti belum cukup)", "Ulasan kajian 2025: bukti sedikit, dan ada risiko jika hidung tersumbat.", "Kad naik"),
   ("15–22s", "CHECKLIST", "Lebih selamat:\n✓ Rawat hidung tersumbat\n✓ Tidur mengiring\n✓ Jumpa doktor jika berdengkur kuat", "Baris satu per satu"),
   MG_END],
  "caption": "Viral tak semestinya selamat 🤐\n\nSumber: PLOS One (2025).\n" + DISC + "\n\n#Momyizz #MitosAtauFakta #Tidur"}],
"N2": [
 {"tajuk": "Formula nap 20 minit", "sticker": "19-blazer-thumbs-up", "babak": [
   ("0–3s", "HOOK", "Nap 20 minit yang betul ⏰", "Pop"),
   ("3–9s", "KAUNTER + teks", "20 minit: set penggera", "Angka pop"),
   ("9–15s", "KAUNTER + teks", "1–3 petang: masa terbaik", "Angka pop"),
   ("15–22s", "NOTA_TANGAN", "Lebih 30 minit = boleh jadi mamai 😵", "Tulisan tangan"),
   MG_END],
  "caption": "Formula nap 20 minit. Save untuk pejabat ⏰\n\n#Momyizz #Nap #TipsHarian"},
 {"tajuk": "Bangun nap rasa lagi penat? Ini sebabnya", "sticker": "20-blazer-terkejut-pipi", "babak": [
   ("0–3s", "HOOK", "Bangun nap rasa lagi penat & mamai? 😵", "Pop"),
   ("3–9s", "KAD_FAKTA", "Punca biasa: nap terlalu lama, masuk tidur dalam", "Kad naik"),
   ("9–16s", "CHECKLIST", "Penyelesaian:\n✓ Hadkan 20–30 minit\n✓ Nap awal petang", "Baris satu per satu"),
   ("16–22s", "CHECKLIST", "✓ Bangun terus, cahaya & air\n✓ Gerak 2 minit", "Baris satu per satu"),
   MG_END],
  "caption": "Nap pendek > nap panjang 😴\n\n#Momyizz #Nap #Tidur"}],
"N3": [
 {"tajuk": "3 tanda makanan sangat diproses pada label", "sticker": "13-blazer-tunjuk-atas-kanan", "babak": [
   ("0–3s", "HOOK", "Kenal makanan sangat diproses dalam 10 saat 🛒", "Pop"),
   ("3–9s", "CHECKLIST baris 1", "✓ Senarai ramuan sangat panjang", "Baris muncul"),
   ("9–15s", "CHECKLIST baris 2", "✓ Nama bahan susah disebut / kod E banyak", "Baris muncul"),
   ("15–22s", "CHECKLIST baris 3", "✓ Gula dalam 3 ramuan pertama", "Baris muncul"),
   MG_END],
  "caption": "3 tanda makanan sangat diproses. Save untuk shopping 🛒\n\n#Momyizz #BacaLabel"},
 {"tajuk": "Mitos vs fakta: 'Gula kelapa tak apa, sebab sihat'", "sticker": "14-blazer-tutup-mulut", "babak": [
   ("0–3s", "HOOK", "\"Gula kelapa / madu tak apa, sebab sihat.\" 🤔", "Pop"),
   ("3–8s", "BIG_WORD", "TETAP GULA 🍯", "Pop besar"),
   ("8–15s", "KAD_FAKTA", "WHO: gula bebas (termasuk madu & sirap) dihadkan bawah 10% tenaga harian.", "Kad naik"),
   ("15–22s", "NOTA_TANGAN", "Tukar jenis gula tak sama dengan kurangkan gula 😉", "Tulisan tangan"),
   MG_END],
  "caption": "Gula 'sihat' tetap gula 🍯\n\nSumber: WHO.\n" + DISC + "\n\n#Momyizz #MitosAtauFakta #KurangManis"}],
"N4": [
 {"tajuk": "5 sarapan otak bawah 10 minit", "sticker": "08-satin-thumbs-up", "babak": [
   ("0–3s", "HOOK", "5 sarapan otak bawah 10 minit 🧠", "Pop"),
   ("3–8s", "CHECKLIST baris 1–2", "✓ Telur rebus + roti gandum\n✓ Oat + pisang", "Baris muncul"),
   ("8–14s", "CHECKLIST baris 3–4", "✓ Telur dadar sayur\n✓ Roti + sardin", "Baris muncul"),
   ("14–22s", "CHECKLIST baris 5", "✓ Bubur nasi + telur + ikan bilis", "Baris muncul"),
   MG_END],
  "caption": "5 sarapan otak bawah 10 minit. Mana favourite korang? 👇\n\n#Momyizz #SarapanSihat"},
 {"tajuk": "Mitos vs fakta: 'Telur naikkan kolesterol, jangan makan hari-hari'", "sticker": "03-satin-tunjuk-atas", "babak": [
   ("0–3s", "HOOK", "\"Telur tinggi kolesterol, jangan makan hari-hari!\" 🥚", "Pop"),
   ("3–8s", "BIG_WORD", "TAK SEMUDAH ITU", "Pop besar"),
   ("8–15s", "KAD_FAKTA", "Bagi kebanyakan orang sihat, telur boleh jadi sebahagian diet seimbang. Yang ada kolesterol tinggi / diabetes: ikut nasihat doktor.", "Kad naik"),
   ("15–22s", "NOTA_TANGAN", "Lebih penting: cara masak & apa yang dimakan bersama 🍳", "Tulisan tangan"),
   MG_END],
  "caption": "Telur: kawan atau lawan? Ikut keadaan korang 🥚\n\n" + DISC + "\n\n#Momyizz #MitosAtauFakta #Telur"}],
"N5": [
 {"tajuk": "4 setting telefon untuk keluarga", "sticker": "17-blazer-panggil", "babak": [
   ("0–3s", "HOOK", "4 setting telefon untuk rumah lebih tenang 📱", "Pop"),
   ("3–8s", "CHECKLIST baris 1", "✓ Matikan notifikasi apps media sosial", "Baris muncul"),
   ("8–13s", "CHECKLIST baris 2", "✓ Had masa harian (Screen Time / Digital Wellbeing)", "Baris muncul"),
   ("13–18s", "CHECKLIST baris 3", "✓ Mod 'Jangan ganggu' waktu makan malam", "Baris muncul"),
   ("18–22s", "CHECKLIST baris 4", "✓ Kawalan ibu bapa pada gajet anak", "Baris muncul"),
   MG_END],
  "caption": "4 setting telefon untuk keluarga. Dah cuba? 📱\n\n#Momyizz #Parenting #DigitalDetox"},
 {"tajuk": "Anak mengamuk bila gajet diambil?", "sticker": "05-satin-semangat", "babak": [
   ("0–3s", "HOOK", "Anak mengamuk bila tablet diambil? 😩", "Pop"),
   ("3–9s", "KAD_FAKTA", "Punca biasa: berhenti mengejut tanpa amaran", "Kad naik"),
   ("9–16s", "CHECKLIST", "Penyelesaian:\n✓ Beri amaran '5 minit lagi'\n✓ Tetapkan masa tamat bersama", "Baris satu per satu"),
   ("16–22s", "CHECKLIST", "✓ Ganti dengan aktiviti seronok (luar rumah)\n✓ Konsisten setiap hari", "Baris satu per satu"),
   MG_END],
  "caption": "Cara Momyizz kurangkan drama gajet 😅 Korang buat apa?\n\n#Momyizz #Parenting #AnakSihat"}],
"N6": [
 {"tajuk": "5 langkah jaga otak mulai minggu ni", "sticker": "18-blazer-semangat", "babak": [
   ("0–3s", "HOOK", "5 langkah jaga otak mulai minggu ni 🧠", "Pop"),
   ("3–8s", "CHECKLIST baris 1–2", "✓ Berjalan 30 minit\n✓ Tidur 7 jam+", "Baris muncul"),
   ("8–14s", "CHECKLIST baris 3–4", "✓ Semak tekanan darah\n✓ Periksa pendengaran & mata", "Baris muncul"),
   ("14–22s", "CHECKLIST baris 5", "✓ Jumpa kawan / keluarga", "Baris muncul"),
   MG_END],
  "caption": "5 langkah jaga otak, ikut laporan Lancet 2024 🧠\n\n#Momyizz #KesihatanOtak"},
 {"tajuk": "Mitos vs fakta: 'Nyanyuk tu biasa, nanti tua mesti kena'", "sticker": "10-satin-terkejut-pipi", "babak": [
   ("0–3s", "HOOK", "\"Nyanyuk tu biasa, nanti tua mesti kena.\" 🤔", "Pop"),
   ("3–8s", "BIG_WORD", "TIDAK SEMESTINYA", "Pop besar"),
   ("8–15s", "KAD_FAKTA + LABEL_BUKTI", "Lancet (2024): hampir 45% kes demensia berpotensi dicegah atau dilewatkan dengan menangani 14 faktor risiko.", "Kad naik"),
   ("15–22s", "NOTA_TANGAN", "Bermula dengan tabiat hari ini 💛", "Tulisan tangan"),
   MG_END],
  "caption": "Demensia bukan takdir yang pasti 🧠\n\nSumber: Lancet Commission (2024).\n" + DISC + "\n\n#Momyizz #MitosAtauFakta #Demensia"}],
})

# Senarai lengkap siri trending (susunan sebenar dalam SUSUNAN di bawah)
TREND_ORDER = ["T1", "T2", "T3", "N1", "N2", "T4", "T5", "N3", "N4", "T6", "N5", "N6", "T7"]
_semua = {t["d"]: t for t in TRENDING + TRENDING_BARU}
TRENDING = [_semua[k] for k in TREND_ORDER]


# ================================================================ SUSUNAN 30 HARI (DISAHKAN pengguna, 18 Nov 2026)
# Bulan ini fokus BodyKey Nutritious Meal Shake (formula baharu, perisa pisang). Kalendar dipadatkan kepada 30 hari.
# Siri trending diselang sehari atau dua hari, bermula Hari 8 (Hari 8, 10, 13, 15, 18, 20, 22, 24, 27, 29). Nombor dalam SUSUNAN = nombor hari asal dalam DAYS.
# Hari asal yang tidak digunakan bulan ini (boleh dipakai bulan depan): 15, 18, 19, 20, 21, 23, 24, 26, 28, 29;
# trending N3 (pewarna & MSG), N5 (media sosial & anak), N6 (14 faktor demensia).
PRODUK_TREND = {
 "T1": ("bodykey", "Makan malam lewat & berat; nak makan malam ringan sebelum tidur"),
 "T2": ("bodykey", "Kurang tidur, esoknya mengidam manis"),
 "T3": ("uv", "Depan skrin sepanjang hari; perlukan perlindungan kulit termasuk cahaya biru"),
 "N1": ("cleanser", "Rutin sebelum tidur; cuci muka tanpa kulit rasa ketat"),
 "N2": ("espring", "Lepas nap mamai; segelas air yang sentiasa sedia di rumah"),
 "T4": ("bodykey", "Kopi petang ganggu tidur; perlukan snek petang tanpa kopi"),
 "T5": ("bodykey", "Serat tak cukup; hari tak sempat makan sayur"),
 "N4": ("bodykey", "Sarapan otak tapi pagi tak sempat masak"),
 "T6": ("omega", "Keluarga jarang makan ikan berlemak"),
 "T7": ("bodykey", "Nak teruskan tabiat sihat; sarapan GI rendah bila kalut"),
}
# Hari 1-7 kekal ikut susunan asal kerana sudah / sedang dipost (Hari 1 = 12 Nov 2026, Hari 7 = span dapur, 18 Nov).
SUSUNAN = [1, 2, 3, 4, 5, 6, 7,
           "T1", 8, "T2", 9, 10, "T3", 11, "N1", 12, 13, "N2", 14, "T4", 16, "T5", 17, "N4", 22, 25, "T6", 27, "T7", 30]


def _susun30():
    global DAYS, MG_FULL, MG_PLAN
    asal = {d["d"]: d for d in DAYS}
    trend = {t["d"]: t for t in TRENDING + TRENDING_BARU}
    mgf, mgp = dict(MG_FULL), dict(MG_PLAN)
    baru, mgf2, mgp2 = [], {}, {}
    for n, k in enumerate(SUSUNAN, 1):
        if isinstance(k, str):
            baru.append(dict(trend[k], d=n, produk=PRODUK_TREND[k]))
            mgf2[n] = MG_TREND[k]
        else:
            baru.append(dict(asal[k], d=n))
            if k in mgf:
                mgf2[n] = mgf[k]
            if k in mgp:
                mgp2[n] = mgp[k]
    assert len(baru) == 30
    DAYS, MG_FULL, MG_PLAN = baru, mgf2, mgp2


_susun30()
