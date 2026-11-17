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

Peraturan: Momyizz & korang sahaja. Produk TIDAK muncul dalam video, carousel atau teks awam
(peraturan Amway Malaysia: tiada tawaran produk di ruang awam; video yang menyebut produk perlu semakan Amway).
Produk + harga hanya dalam slot wa (ruang tertutup).
"""

DISC = "Perkongsian ilmu umum. Bukan nasihat perubatan."
CERITA = "Cerita peribadi mesti benar. Ubah butiran ikut kehidupan sebenar Momyizz sebelum rakam."

JENIS_TEKS = [("10:00", "Info ringkas"), ("16:00", "Pertanyaan"), ("18:30", "Tips praktikal"), ("21:00", "Info penting / alert")]

DAYS = [
# ================================================================ HARI 1
{"d": 1, "ep": 1, "tema": "Mikroplastik: fakta, bukan panik",
 "video": {"tajuk": "Pagi-pagi isi botol air", "nota": CERITA + " Sticker: 14-blazer-tutup-mulut (babak hook).",
  "babak": [
   ("0–3s", "Close-up tangan isi air ke botol plastik lama yang calar", "Pernah fikir apa yang bersentuhan dengan air minuman kita? 🤔"),
   ("3–12s", "Momyizz bercakap ke kamera di dapur", "Semalam lalu FYP: 'Mikroplastik dalam air minuman!' Momyizz terus nak buang semua botol."),
   ("12–25s", "Momyizz duduk depan laptop, teh panas, malam", "Tapi Momyizz baca dulu laporan WHO. Rupanya ceritanya lebih tenang daripada yang viral."),
   ("25–38s", "Tangan susun botol kaca dan keluli di atas meja", "Mulai hari ni Momyizz kongsi fakta, bukan panik. Ikut siri ni ya."),
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
  "Tips pilih botol air guna semula 💡\n\n✅ Keluli tahan karat gred makanan atau kaca (dengan sarung silikon supaya tak mudah pecah)\n✅ Mulut botol lebar, senang dicuci\n✅ Basuh setiap hari dengan berus botol, keringkan terbuka\n\nBotol yang mudah dicuci = botol yang betul-betul dipakai hari-hari. 😉",
  "Info penting: botol air plastik sekali guna direka untuk SEKALI guna. ⚠️\n\nJangan isi air panas ke dalamnya, dan jangan guna berulang kali sampai calar. Kajian tentang kesan haba pada pelepasan zarah masih awal, tapi langkah ni mudah dan tak rugi apa-apa. 🌿",
 ]},

# ================================================================ HARI 2
{"d": 2, "ep": 1, "tema": "3 langkah kecil kurangkan pendedahan plastik",
 "video": {"tajuk": "3 benda kecil yang Momyizz ubah", "nota": CERITA + " Sticker: 18-blazer-semangat (babak akhir).",
  "babak": [
   ("0–3s", "Momyizz pegang beg sampah, berhenti, geleng kepala", "Tak perlu buang semua plastik esok pagi. 🙅‍♀️"),
   ("3–15s", "Tukar botol plastik calar ke botol keluli", "Satu: botol plastik dah calar? Tukar ke kaca atau keluli."),
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
  "Info ringkas: perubahan yang bertahan biasanya yang kecil. 🌱\n\nMomyizz mula dengan satu je minggu ni: botol air keluli dari rumah. Bila dah jadi tabiat, baru tambah langkah kedua.",
  "Soalan: dalam rumah korang, barang plastik apa yang paling banyak?\n\n🍱 Bekas makanan\n🧴 Botol\n🛍️ Beg plastik\n🥤 Cawan / straw\n\nMomyizz? Bekas makanan. Bertimbun dalam kabinet! 😅",
  "Tips jaga bekas plastik yang masih elok 💡\n\n✅ Basuh dengan span lembut, elak sabut kasar yang mencalarkan\n✅ Ikut label pengeluar untuk air panas, microwave dan mesin basuh pinggan\n✅ Simpan untuk barang kering bila dah tak sesuai untuk makanan panas\n✅ Retak, melengkung atau berbau? Masa untuk tukar",
  "Info penting musim tengkujuh: selepas banjir atau bila air paip keruh, didihkan air sebelum minum. 💧\n\nIni panduan asas kesihatan awam semasa banjir. Kongsi dengan keluarga di kawasan yang terjejas. 🙏",
 ]},

# ================================================================ HARI 3
{"d": 3, "ep": 1, "tema": "Cara baca berita kesihatan viral",
 "video": {"tajuk": "Kenapa Momyizz tak terus kongsi berita viral", "nota": CERITA + " Sticker: 04-satin-tutup-mulut atau 14-blazer-tutup-mulut.",
  "babak": [
   ("0–3s", "Skrin telefon: notifikasi group keluarga banyak", "Group keluarga dah kongsi lagi berita kesihatan viral… 📱"),
   ("3–15s", "Momyizz bercakap ke kamera", "Dulu Momyizz pernah forward satu tips viral. Rupanya salah. Malu sangat. 🙈"),
   ("15–30s", "Tangan tulis 3 soalan atas kertas", "Sekarang Momyizz tanya 3 soalan dulu: Siapa sumbernya? Ada kajian? Badan rasmi kata apa?"),
   ("30–40s", "Momyizz tunjuk label warna di skrin", "Sebab tu setiap post Momyizz ada label bukti: 🟢 🟠 🔵 🔴"),
   ("40–45s", "Momyizz senyum", "Fakta dulu, baru kongsi 💛"),
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
  "Tips semak berita kesihatan dalam 30 saat 💡\n\n1️⃣ Cari nama kajian atau badan yang disebut. Tiada nama? Tanda merah.\n2️⃣ Taip tajuk berita + \"sebenarnya.my\" di Google.\n3️⃣ Tengok tarikh. Berita lama selalu diulang viral.\n\nSave untuk group keluarga! 📲",
  "Info penting: sebelum forward berita kesihatan, semak dulu di portal semakan fakta rasmi Malaysia, sebenarnya.my. ✅\n\nSatu forward yang salah boleh buat orang tersayang panik atau ambil keputusan kesihatan yang silap.",
 ]},

# ================================================================ HARI 4
{"d": 4, "ep": 2, "tema": "Sarapan ibu yang selalu tertinggal",
 "video": {"tajuk": "Semua dah makan, kecuali ibu", "nota": CERITA + " Sticker: 10-satin-terkejut-pipi (babak hook). Boleh juga guna video Episod 2 (tab Episod).",
  "babak": [
   ("0–3s", "Meja makan: pinggan anak dan suami dah licin, pinggan ibu kosong", "Anak dah makan. Suami dah makan. Ibu? \"Nanti la.\" 🙃"),
   ("3–15s", "Momyizz kalut cari kunci, capai roti sambil keluar", "Hampir setiap pagi Momyizz jadi orang terakhir. Kadang langsung tak makan."),
   ("15–28s", "Momyizz di meja kerja pukul 11, lapar, capai snek manis", "Pukul 11 dah lapar sangat. Capai apa yang ada."),
   ("28–40s", "Momyizz masukkan bekas ke dalam beg sekali dengan bekal anak", "Minggu ni Momyizz cuba: siapkan bekal ibu sekali dengan bekal anak. 🍱"),
   ("40–45s", "Momyizz ke kamera", "Ibu pun perlu diisi dulu 💛 Siapa sama?"),
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
  "Tips pastikan ibu tak tertinggal sarapan 💡\n\n✅ Malam: letak bekas ibu SEBELAH bekas anak, terus nampak pagi esok\n✅ Simpan \"kotak snek sihat\" di pejabat: kacang, roti gandum, buah\n✅ Set peringatan telefon 10 pagi: \"Dah makan?\"\n\nKecil, tapi berkesan untuk Momyizz. 💛",
  "Info penting: 15.6% dewasa Malaysia ada diabetes, dan ramai tak tahu mereka menghidapnya (NHMS 2023). ⚠️\n\nKalau selalu skip makan dan banyak minum manis, buat saringan gula di klinik kesihatan. Tahu awal lebih baik. 🩸",
 ]},

# ================================================================ HARI 5
{"d": 5, "ep": 2, "tema": "Persediaan malam & pelan B pagi kelam-kabut",
 "video": {"tajuk": "10 minit malam untuk pagi yang tenang", "nota": CERITA + " Sticker: 19-blazer-thumbs-up (babak akhir). Tiada produk dalam video.",
  "babak": [
   ("0–3s", "Jam dinding 10 malam, dapur", "10 minit malam ni = pagi esok lebih tenang 🌙"),
   ("3–15s", "Rebus telur, masuk peti", "Rebus 4 biji telur, simpan dalam peti."),
   ("15–27s", "Oat dalam balang, tuang susu, letak buah", "Oat rendam semalaman. Esok tinggal ambil."),
   ("27–38s", "Bekas bekal tersusun atas meja", "Bekas bekal anak DAN ibu dah sedia."),
   ("38–45s", "Pagi: Momyizz sarapan sambil duduk", "Hasilnya? Sarapan sambil duduk. 5 minit pun rasa menang 🏆"),
  ],
  "caption": "Self-care tak semestinya spa. Kadang dia cuma sarapan sambil duduk 💛\n\n#Momyizz #RutinMalam #SarapanIbu #SelfCare"},
 "carousel": {"tajuk": "Pelan B bila pagi tak ikut rancangan",
  "slaid": [
   "PELAN B 🆘\nBila pagi tak ikut rancangan",
   "REALITI\nAnak demam, mesyuarat awal, lupa rebus telur. Ia berlaku. 😅",
   "PELAN B 1\nPisang + segenggam kacang dalam beg",
   "PELAN B 2\nSusu kotak kecil + roti gandum",
   "PELAN B 3\nMinuman protein untuk hari yang betul-betul tak sempat",
   "INGAT\nPelan B bukan pengganti sarapan sebenar.\nMakanan sebenar tetap nombor satu. 🙏\n\n" + DISC,
  ],
  "caption": "Pelan B korang apa? Kongsi kat komen 👇\n\n" + DISC + "\n\n#Momyizz #SarapanIbu #IbuBekerja #RealitiIbu"},
 "teks": [
  "Info ringkas: protein bukan dari daging sahaja. 🌱\n\nTelur, ikan, tauhu, tempe, kekacang dan susu semuanya sumber protein. Tauhu dan tempe antara pilihan protein yang mudah didapati dan berpatutan di Malaysia.",
  "Soalan: semalam pukul berapa korang makan makanan pertama? ⏰\n\n🕖 Sebelum 8 pagi\n🕘 8–10 pagi\n🕛 Lepas 10 pagi\n🙈 Tengah hari baru teringat\n\nMomyizz: 7:30 pagi, sambil duduk! 🎉",
  "Tips telur rebus untuk seminggu 💡\n\n✅ Rebus sekali gus 6–8 biji, sejukkan cepat dalam air sejuk\n✅ Simpan dalam peti BERSAMA kulit, dalam bekas bertutup\n✅ Elok dimakan dalam tempoh seminggu (USDA)\n✅ Tulis tarikh rebus pada bekas\n\nSarapan, bekal dan snek petang siap! 🥚",
  "Info penting: sebelum beli apa-apa supplemen atau minuman kesihatan, semak nombor pendaftaran \"MAL\" pada label. ⚠️\n\nProduk berdaftar dengan KKM boleh disemak melalui laman NPRA. Elak produk yang janji kurus cepat atau tiada maklumat pendaftaran.",
 ],
 "wa": {"tajuk": "Nutrilite Soy Protein Drink", "nota": "Ruang tertutup sahaja (pelanggan sedia ada / group tertutup / orang yang bertanya). Isi harga dan fakta dari amway.my hari ini. Jangan tambah dakwaan kesihatan.",
  "t": "Hai [nama] 😊\n\nMinggu ni Momyizz kongsi pasal sarapan ibu yang selalu tertinggal. Ramai tanya apa \"pelan B\" Momyizz untuk hari yang tak sempat makan.\n\nYang Momyizz guna: *Nutrilite Soy Protein Drink*\n• Perisa: [semak amway.my: Mixed Berries 500g / Green Tea 450g]\n• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n• Cara guna: [salin dari label / amway.my]\n\nMomyizz guna untuk hari kelam-kabut sahaja, bukan pengganti sarapan sebenar. 🙏\n\nKalau nak, reply \"NAK\" dan perisa pilihan, Momyizz uruskan. 💛\n\n" + DISC}},

# ================================================================ HARI 6
{"d": 6, "ep": 2, "tema": "Gula tersembunyi dalam minuman",
 "video": {"tajuk": "Gula paling banyak bukan dalam pinggan", "nota": CERITA + " Sticker: 09-kartun-terkejut-pipi (babak pendedahan).",
  "babak": [
   ("0–3s", "Tiga cawan atas meja: teh tarik, kopi ais, air kotak", "Gula paling banyak dalam rutin Momyizz… bukan dalam pinggan. 😳"),
   ("3–15s", "Momyizz tunjuk cawan satu per satu", "Teh tarik pagi. Kopi ais tengah hari. Air kotak petang."),
   ("15–28s", "Momyizz minum air kosong dulu, baru kopi", "Sekarang: air kosong dulu, baru kopi."),
   ("28–40s", "Momyizz di kaunter kedai, isyarat 'kurang manis'", "Bila beli: \"kurang manis ya!\""),
   ("40–45s", "Momyizz ke kamera", "Bukan haramkan teh tarik 😄 Sedar dan kurangkan."),
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
  "Jujur: minuman manis mana paling susah korang tinggal? 🧋\n\n☕ Teh tarik\n🧊 Kopi ais\n🧃 Air kotak\n🥤 Air bergas\n\nMomyizz: teh tarik pagi. Tengah cuba \"kurang manis\". 😅",
  "Tips kurangkan manis tanpa rasa terseksa 💡\n\nMinggu 1: minta \"kurang manis\"\nMinggu 2: \"separuh gula\"\nMinggu 3: cuba teh / kopi O kosong sekali sehari\n\nYang Momyizz perasan: lama-lama tekak dah biasa, dan air manis sangat terasa terlalu manis. 😄",
  "Info penting: ada sejarah diabetes dalam keluarga? ⚠️\n\nNHMS 2023: 15.6% dewasa Malaysia ada diabetes, dan ramai tak tahu. Saringan gula darah boleh dibuat di klinik kesihatan. Jangan tunggu ada simptom. 🩸",
 ],
 "wa": {"tajuk": "Minta testimoni (pelanggan sedia ada)", "nota": "Untuk dapatkan testimoni SEBENAR. Guna hanya dengan kebenaran, tanpa dakwaan perubatan.",
  "t": "Hai [nama] 😊 Terima kasih sebab percaya Momyizz.\n\nDah lebih kurang [tempoh] guna [produk]. Boleh kongsi sikit pengalaman [nama]? Contohnya macam mana [nama] guna dalam rutin harian, dan apa yang [nama] suka.\n\nKalau [nama] izinkan, Momyizz nak kongsi dalam group tertutup Momyizz (nama boleh disembunyikan). Kalau tak selesa pun takpe langsung. 💛"}},

# ================================================================ HARI 7
{"d": 7, "ep": 3, "tema": "Span dapur & kebersihan dapur",
 "video": {"tajuk": "Span yang Momyizz pegang setiap malam", "nota": CERITA + " Sticker: 14-blazer-tutup-mulut (babak span). Boleh juga guna video Episod 3 (tab Episod).",
  "babak": [
   ("0–3s", "Close-up span lama diperah, kekuningan", "Bila kali terakhir korang tukar ni? 🧽"),
   ("3–15s", "Momyizz basuh pinggan malam, pandang span", "Momyizz fikir: 'Tak apa, dia kan sentiasa bersabun.'"),
   ("15–28s", "Teks atas skrin + Momyizz terkejut", "Kajian 2017 jumpa bakteria sangat tinggi dalam span dapur terpakai. 😳"),
   ("28–40s", "Tulis tarikh pada span baru dengan marker", "Sekarang: tulis tarikh pada span baru, perah dan keringkan lepas guna."),
   ("40–45s", "Dapur bersih, Momyizz senyum", "Dapur bersih bermula dengan benda kecil ✨"),
  ],
  "caption": "Bila kali terakhir korang tukar span? Jujur je kat komen 😂\n\nSumber: Cardinale et al. (2017).\n\n#Momyizz #DapurBersih #TipsRumah"},
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
  "Lepas tengok video pagi tadi… berapa ramai yang terus pergi tukar span? 😂\n\nKomen:\n✅ DAH\n😅 ESOK\n\nMomyizz dah. Tarikh pun dah tulis!",
  "Tips span tahan lebih bersih 💡\n\n✅ Perah kuat lepas guna\n✅ Letak di rak berlubang / tempat berangin, bukan dalam sinki basah\n✅ Asingkan span pinggan dan kain lap meja\n✅ Tulis tarikh, tukar secara berkala\n\nSpan kering = kurang tempat untuk bakteria membiak. 🧽",
  "Info penting musim banjir: leptospirosis merebak melalui air atau tanah yang tercemar air kencing tikus. ⚠️\n\nElak meredah air banjir tanpa kasut, tutup makanan di dapur, dan dapatkan rawatan jika demam selepas terdedah kepada air banjir. 🙏",
 ],
 "wa": {"tajuk": "Amway Home Dish Drops", "nota": "Ruang tertutup sahaja. Fakta dan harga dari amway.my hari ini. Jangan dakwa sabun membunuh kuman atau menggantikan tukar span.",
  "t": "Hai [nama] 😊\n\nHari ni Momyizz kongsi pasal span dapur. Ada yang tanya sabun basuh pinggan apa Momyizz guna.\n\nMomyizz guna *DISH DROPS Concentrated Dishwashing Liquid (1L)* dari Amway Home.\n• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n• Cara guna / sukatan: [salin dari label / amway.my]\n• Kenapa Momyizz pilih: [pengalaman sebenar Momyizz]\n\nTapi ingat ya, sabun yang bagus tak menggantikan tabiat tukar span dan keringkan span. 🧽\n\nKalau berminat, reply \"NAK\", Momyizz uruskan. 💛"}},

# ================================================================ HARI 8-30 (rancangan; teks penuh dijana dengan Claude)
# Format: (video, carousel, [teks info, teks pertanyaan, teks tips, teks alert], wa atau None)
{"d": 8, "ep": 3, "tema": "Papan pemotong & kain lap",
 "plan": ("Momyizz tunjuk 2 papan pemotong: mentah vs masak", "Kain lap: bila patut basuh & tukar (5 slaid)",
          ["Kain lap lembap = tempat bakteria suka", "Korang ada berapa papan pemotong?", "Basuh papan pemotong dengan air panas & sabun, keringkan berdiri", "tikus di dapur musim hujan, tutup makanan"],
          "Soalan lazim Dish Drops (dari soalan pelanggan sebenar)")},
{"d": 9, "ep": 3, "tema": "Kesilapan dapur yang biasa",
 "plan": ("3 kesilapan dapur Momyizz dulu", "Mitos vs fakta kebersihan dapur",
          ["Basuh ayam mentah boleh percik bakteria ke sinki", "Korang basuh ayam mentah dalam sinki?", "Cara simpan lauk lebihan: sejukkan cepat, bekas bertutup, peti", "lauk lebih jangan biar semalaman di suhu bilik"], None)},
{"d": 10, "ep": 4, "tema": "Panaskan bekal dalam bekas plastik",
 "plan": ("Beratur depan microwave pantri pejabat", "Apa kajian makmal 2023 jumpa (label Kajian awal)",
          ["Label 'microwave safe' maksudnya apa", "Bekal korang panaskan dalam bekas apa?", "Pindah lauk ke pinggan kaca sebelum panaskan", "bekas retak / melengkung patut ditukar"], None)},
{"d": 11, "ep": 4, "tema": "Bekal sihat ke pejabat",
 "plan": ("Susun bekal seminggu dalam 20 minit", "Bekal ikut Pinggan Sihat (5 slaid)",
          ["Biar lauk sejuk sikit sebelum masuk bekas", "Korang bawa bekal berapa kali seminggu?", "Bekal seminggu: masak asas hari Ahad, susun ikut hari", "bekal berkuah jangan biar lebih 2 jam di suhu bilik"], None)},
{"d": 12, "ep": 4, "tema": "Cara baca berita kesihatan (bahagian 2)",
 "plan": ("Tajuk viral vs isi kajian sebenar", "Kajian makmal vs manusia: bezanya",
          ["FDA: belum ada bukti risiko mikroplastik dalam makanan, pemantauan diteruskan", "Berita kesihatan apa paling selalu masuk group keluarga?", "Tanya 3 soalan sebelum percaya tajuk viral", "semak sebenarnya.my sebelum forward"], None)},
{"d": 13, "ep": 5, "tema": "Minum air cukup",
 "plan": ("Botol air masih penuh sampai petang", "Berapa banyak air kita perlu (EFSA ~2.0 L wanita, termasuk makanan)",
          ["Air dari buah & sup pun dikira", "Hari ni korang dah minum berapa gelas?", "Tanda masa pada botol air (10 pg, 12 tgh, 3 ptg)", "cuaca panas / demam = perlu lebih air"], None)},
{"d": 14, "ep": 5, "tema": "Cabaran Air 7 hari",
 "plan": ("Lancar #CabaranAirMomyizz", "Trick 5 waktu solat = 5 gelas",
          ["Air kosong dulu, baru kopi", "Siapa nak join cabaran? Komen JOIN", "Letak botol air di tempat yang selalu nampak", "air kotak / sirap bukan pengganti air kosong"],
          "eSpring Water Purifier (hanya spesifikasi rasmi; JANGAN dakwa singkir mikroplastik)")},
{"d": 15, "ep": 5, "tema": "Dehidrasi & letih",
 "plan": ("Petang blur: kurang minum ke?", "Tanda badan perlukan air",
          ["Dehidrasi ringan dikaitkan dengan fokus menurun (kajian awal)", "Korang selalu letih pukul berapa?", "Tambah hirisan limau / timun dalam air kosong", "letih berpanjangan ada banyak punca, jumpa doktor"], None)},
{"d": 16, "ep": 6, "tema": "Rutin kulit 5 minit",
 "plan": ("Pukul 10 malam, 'cuci muka esok je la…'", "Cara cuci muka betul (AAD)",
          ["Air suam, bukan panas", "Rutin malam korang berapa langkah?", "Kit cuci muka 5 minit dalam satu dulang", "jangan tidur dengan mekap"], None)},
{"d": 17, "ep": 6, "tema": "SPF setiap hari",
 "plan": ("Dulang skincare sebelah sinki", "SPF 30 spektrum luas: kenapa setiap hari (AAD)",
          ["SPF tetap perlu walaupun dalam bangunan dekat tingkap", "Jenis kulit korang apa?", "Sapu SPF sebanyak dua jari untuk muka & leher", "produk 'cerah 7 hari' tanpa pendaftaran, hati-hati"],
          "ARTISTRY Gel Cleanser + ARTISTRY Skin Analysis Experience (tiada janji hasil)")},
{"d": 18, "ep": 6, "tema": "Skincare: konsisten lebih penting",
 "plan": ("Dulu 7 langkah, sekarang 3", "Rutin 3 langkah yang cukup",
          ["Rutin konsisten > banyak produk", "Produk skincare apa korang beli ikut trend?", "Habiskan satu produk dulu sebelum beli yang baharu", "uji produk baharu pada kulit kecil dulu (patch test)"], None)},
{"d": 19, "ep": 7, "tema": "Air botol plastik: kajian 2024",
 "plan": ("Dua kotak air botol dalam bonet", "Kajian 2024 dalam 6 slaid (Kajian awal + WHO)",
          ["Sampel terhad, mampu kesan ≠ terbukti bahaya", "Korang simpan air botol di mana?", "Simpan air botol di tempat sejuk dan teduh", "jangan simpan air botol dalam kereta panas lama-lama"], None)},
{"d": 20, "ep": 7, "tema": "Air minuman keluarga",
 "plan": ("2 benda yang Momyizz ubah", "Pilihan air minuman di rumah: kebaikan & perkara perlu jaga",
          ["Tukar kartrij penapis air ikut jadual pengeluar", "Air minuman di rumah korang dari mana?", "Jadual tukar kartrij penapis: tulis dalam kalendar telefon", "air paip keruh selepas banjir, didihkan"], None)},
{"d": 21, "ep": 7, "tema": "Rumusan siri mikroplastik",
 "plan": ("Refleksi 3 minggu berkongsi", "Siri mikroplastik dalam 1 carousel (save)",
          ["Ringkasan: 4 langkah paling mudah", "Topik apa korang nak seterusnya?", "Satu tabiat seminggu: pilih yang paling mudah", "ringkasan 3 tanda berita kesihatan palsu"], None)},
{"d": 22, "ep": 8, "tema": "Vitamin C setiap hari",
 "plan": ("Anak bersin, terus potong oren", "Gunakan carousel Episod 8 (tab Episod)",
          ["Badan tak boleh hasilkan vitamin C sendiri (NIH)", "Buah apa selalu ada di rumah korang?", "Potong buah awal-awal, simpan di aras mata dalam peti", "musim tengkujuh, basuh tangan & tidur cukup kekal asas"], None)},
{"d": 23, "ep": 8, "tema": "Mitos vitamin C",
 "plan": ("Trick anak makan buah tanpa disuruh", "Vitamin C cegah selesema? Apa kata Cochrane",
          ["Jambu batu antara buah tempatan tinggi vitamin C", "Teka: buah tempatan mana paling tinggi vitamin C?", "Buah tinggi vitamin C yang murah ikut musim", "dos tinggi tak semestinya lebih baik, ikut label"],
          "Nutrilite Bio C Plus sebagai pelengkap (makanan tetap utama; tiada dakwaan cegah / rawat)")},
{"d": 24, "ep": 8, "tema": "Vitamin C & zat besi",
 "plan": ("Menu buah seminggu bajet biasa", "Cara bantu penyerapan zat besi",
          ["Vitamin C bantu serap zat besi dari sumber tumbuhan", "Korang minum teh lepas makan?", "Jarakkan teh / kopi dari waktu makan", "pucat & pening berpanjangan, buat ujian darah"], None)},
{"d": 25, "ep": 9, "tema": "Duduk terlalu lama",
 "plan": ("Momyizz kira jam duduk semalam", "WHO 2020: berapa minit bergerak seminggu",
          ["Sedikit aktiviti lebih baik daripada tiada", "Berapa jam korang duduk hari ni?", "Set peringatan 'bangun & gerak' setiap jam", "29.9% dewasa Malaysia tidak aktif (NHMS 2023)"], None)},
{"d": 26, "ep": 9, "tema": "Gerak bersama keluarga",
 "plan": ("Jalan 10 minit lepas makan malam bawa anak", "10 cara gerak tanpa gym",
          ["Berdiri masa jawab telefon pun dikira", "Gerak apa korang buat hari ni?", "Jalan kaki keluarga: tetapkan masa yang sama setiap hari", "sakit dada / sesak nafas masa bersenam, berhenti & dapatkan rawatan"], None)},
{"d": 27, "ep": 9, "tema": "Kuatkan otot",
 "plan": ("Latihan 5 minit di rumah", "Latihan otot 2 hari seminggu (WHO 2020)",
          ["Otot kuat bantu aktiviti harian", "Korang pernah buat latihan otot?", "3 latihan otot tanpa alat: squat dinding, angkat botol air, tekan tubi lutut", "hamil / ada penyakit, tanya doktor sebelum mula"], None)},
{"d": 28, "ep": 10, "tema": "Kulit dari dalam",
 "plan": ("Rak skincare penuh, kulit tetap kusam", "Pinggan Glowing (5 slaid)",
          ["Vitamin C perlu untuk kolagen (NIH)", "Pinggan makan tengah hari korang hari ni?", "Isi separuh pinggan dengan sayur dulu", "1 dalam 2 yang ada kolesterol tinggi tak tahu (NHMS 2023)"], None)},
{"d": 29, "ep": 10, "tema": "Omega-3 & ikan tempatan",
 "plan": ("Ikan kembung & sardin minggu ni", "Sumber omega-3 tempatan + kajian kulit masih terhad",
          ["EPA & DHA ada dalam ikan berlemak (NIH)", "Korang makan ikan berapa kali seminggu?", "Cara masak ikan kembung / sardin yang mudah untuk anak", "makan ubat cair darah? Tanya doktor sebelum ambil omega-3"],
          "Nutrilite Omega-3 Fish Oil Plus (sahkan nama semasa) + ARTISTRY; tiada dakwaan mencerahkan")},
{"d": 30, "ep": 10, "tema": "Refleksi 30 hari",
 "plan": ("Terima kasih 30 hari bersama korang", "10 perkara Momyizz kongsi bulan ni",
          ["1 tabiat paling mudah untuk mula", "Bulan depan nak Momyizz kupas apa?", "Senarai semak 10 tabiat untuk bulan depan", "cara betul ambil supplemen (6 perkara)"],
          "Ikuti pelanggan: tanya pengalaman & keperluan ulang beli")},
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
 8: ("Cara basuh papan pemotong ikut jenis (kayu vs plastik)", "Ayam mentah & sayur guna papan sama? Penyelesaian: kod warna"),
 9: ("4 kesilapan simpan makanan dalam peti", "Lauk lebih semalaman di atas meja? Sejukkan & simpan dalam 2 jam"),
 10: ("Cara baca simbol pada bekas plastik", "Bekal berkuah tumpah dalam beg? Pilih bekas & cara susun"),
 11: ("Bekal seimbang dalam 1 bekas (formula ½ ¼ ¼)", "Bosan bekal sama setiap hari? Putaran 5 menu"),
 12: ("Beza kajian makmal, haiwan dan manusia", "Tajuk viral buat panik? 3 langkah bertenang"),
 13: ("Tanda badan kurang air", "Lupa minum bila sibuk? Ikat minum dengan rutin sedia ada"),
 14: ("Kira gelas air sehari dengan trick solat", "Tak suka air kosong? Tambah buah / herba segar"),
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
