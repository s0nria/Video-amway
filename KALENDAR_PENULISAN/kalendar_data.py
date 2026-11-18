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
{"d": 30, "ep": 10, "tema": "Refleksi sebulan",
 "plan": ("Terima kasih sebulan bersama korang", "10 perkara Momyizz kongsi bulan ni",
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


# ================================================================ SIRI TRENDING: TIDUR, OTAK & USUS
# Diilhamkan oleh podcast tidur & otak yang tengah viral (YouTube, Ar Rasyidin Academy Ep 64).
# Isi podcast TIDAK dapat disemak (tiada transkrip); fakta di bawah daripada sumber rasmi sahaja.
# Jangan petik / atribusikan dakwaan kepada penceramah podcast. Siri ini dimasukkan sebagai Hari 7-13;
# kandungan asal Hari 7-30 dianjak menjadi Hari 14-37 (lihat bahagian bawah fail).
TREND_NOTA = "Siri trending: guna podcast tidur & otak yang viral sebagai hook sahaja. Jangan petik nama penceramah atau dakwaan podcast yang belum disemak."

TRENDING = [
{"d": "T1", "ep": None, "tema": "Tidur: masa otak 'membersihkan diri'",
 "video": {"tajuk": "Ramai share podcast tidur & otak, ini yang Momyizz semak", "nota": CERITA + " " + TREND_NOTA + " Sticker: 09-kartun-terkejut-pipi.",
  "babak": [
   ("0–3s", "Telefon tunjuk podcast tidur & otak di FYP, Momyizz tengok sambil baring", "Podcast pasal tidur & otak ni tengah viral. Momyizz pun terus semak kajiannya 🧠"),
   ("3–15s", "Momyizz bercakap ke kamera, bilik suram", "Kajian 2013 dalam jurnal Science: semasa tidur, ruang antara sel otak tikus membesar kira-kira 60%."),
   ("15–28s", "Animasi air mengalir antara sel (Flow)", "Cecair otak mengalir lebih laju dan sisa seperti beta-amiloid dibersihkan lebih cepat."),
   ("28–38s", "Momyizz letak telefon, tutup lampu", "Ini kajian haiwan. Pada manusia masih dikaji. Tapi satu benda dah jelas: tidur bukan sekadar rehat."),
   ("38–45s", "Momyizz senyum, selimut", "Malam ni, jom tidur awal sikit 🌙 | " + DISC),
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
  "Tips mula tidur awal 15 minit 💡\n\n✅ Minggu ni, masuk tidur 15 minit lebih awal daripada biasa\n✅ Minggu depan, tambah 15 minit lagi\n✅ Set peringatan 'masa tidur' di telefon\n\nPerlahan-lahan lebih mudah daripada terus paksa tidur 2 jam awal. 🌙",
  "Info penting: kalau korang selalu berdengkur kuat, tercungap waktu tidur, atau sangat mengantuk siang hari walaupun tidur cukup, jumpa doktor. ⚠️\n\nIni boleh jadi tanda masalah tidur seperti apnea tidur yang perlukan pemeriksaan.",
 ]},

{"d": "T2", "ep": None, "tema": "Berapa jam tidur ibu & anak",
 "video": {"tajuk": "Revenge bedtime: masa untuk diri sendiri yang dicuri dari tidur", "nota": CERITA + " " + TREND_NOTA + " Sticker: 04-satin-tutup-mulut.",
  "babak": [
   ("0–3s", "Jam 12:30 malam, Momyizz scroll telefon atas katil", "Anak dah tidur. Akhirnya masa untuk Momyizz… pukul 12:30 malam 😅"),
   ("3–15s", "Momyizz bercakap ke kamera", "Ada nama untuk ni: 'revenge bedtime'. Kita curi masa tidur untuk rasa ada masa sendiri."),
   ("15–28s", "Pagi: Momyizz menguap, kopi kedua", "Esoknya? Penat, cepat marah, kopi dua cawan."),
   ("28–40s", "Momyizz baca buku 15 minit pukul 10 malam", "Sekarang Momyizz cuba: 'masa sendiri' 20 minit lepas anak tidur, kemudian terus tidur."),
   ("40–45s", "Momyizz ke kamera", "Masa sendiri penting. Tidur pun penting 💛"),
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
  "Tips rutin tidur anak (dan ibu sekali) 💡\n\n✅ Waktu tidur sama setiap malam, termasuk hujung minggu (lebih kurang)\n✅ Lampu dimalapkan 30 minit sebelum tidur\n✅ Tiada skrin di atas katil\n✅ Bacaan atau sembang ringan sebagai 'tanda' masa tidur",
  "Info penting: mengantuk ketika memandu sangat berbahaya. ⚠️\n\nKalau mata berat semasa memandu, berhenti di tempat selamat dan rehat. Tingkap terbuka atau radio kuat bukan penyelesaian.",
 ]},

{"d": "T3", "ep": None, "tema": "Skrin & cahaya malam",
 "video": {"tajuk": "Telefon tidur di luar bilik", "nota": CERITA + " " + TREND_NOTA + " Sticker: 18-blazer-semangat.",
  "babak": [
   ("0–3s", "Muka diterangi cahaya telefon dalam gelap", "Scroll 'sekejap je'… tiba-tiba dah pukul 1 pagi 📱"),
   ("3–15s", "Momyizz bercakap ke kamera", "Cahaya terang pada waktu malam boleh tekan hormon melatonin, hormon yang bantu kita rasa mengantuk."),
   ("15–28s", "Momyizz cas telefon di dapur, bukan di bilik", "Eksperimen Momyizz minggu ni: telefon dicas di luar bilik."),
   ("28–40s", "Momyizz baca buku, lampu kuning malap", "Ganti dengan buku atau zikir. Malam ketiga, Momyizz tidur lebih cepat."),
   ("40–45s", "Momyizz ke kamera", "Siapa berani cuba 7 hari? 🙋‍♀️"),
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
  "Tips kalau telefon perlu ada di bilik (contoh: anak kecil, kerja) 💡\n\n✅ Aktifkan mod 'Jangan ganggu'\n✅ Letak telefon jauh dari katil, skrin ke bawah\n✅ Guna jam loceng biasa supaya tak perlu buka telefon pagi-pagi",
  "Info penting untuk ibu bapa: kanak-kanak 6–12 tahun perlukan 9–12 jam tidur sehari (AASM). ⚠️\n\nSkrin di bilik tidur boleh melambatkan waktu tidur anak. Pertimbangkan 'stesen cas keluarga' di ruang tamu.",
 ]},

{"d": "T4", "ep": None, "tema": "Kafein & tidur",
 "video": {"tajuk": "Kopi petang yang curi tidur malam", "nota": CERITA + " " + TREND_NOTA + " Sticker: 14-blazer-tutup-mulut.",
  "babak": [
   ("0–3s", "Kopi ais di meja kerja, jam 4 petang", "Kopi pukul 4 petang… dan tertanya kenapa susah tidur malam 🤔"),
   ("3–15s", "Momyizz bercakap ke kamera", "Satu kajian kecil (2013): kafein yang diambil 6 jam sebelum tidur masih kurangkan tidur hampir sejam."),
   ("15–28s", "Teks atas skrin, Momyizz terkejut", "Yang mengejutkan: peserta tak sedar pun tidur mereka terganggu. 😳"),
   ("28–40s", "Momyizz minum air kosong / teh herba waktu petang", "Sekarang kopi terakhir Momyizz sebelum pukul 2 petang."),
   ("40–45s", "Momyizz ke kamera", "Kopi tak salah. Masa yang penting ☕"),
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
  "Tips kurangkan kafein petang tanpa sakit kepala 💡\n\n✅ Kurangkan perlahan-lahan, contohnya setengah cawan dulu\n✅ Ganti cawan petang dengan air kosong atau teh herba tanpa kafein\n✅ Minum air kosong cukup sepanjang hari\n\nTerus berhenti mengejut boleh buat sesetengah orang sakit kepala.",
  "Info penting: minuman tenaga mengandungi kafein dan sering tinggi gula. ⚠️\n\nPeriksa label sebelum minum, dan berhati-hati jika hamil, menyusu atau ada masalah jantung. Rujuk doktor jika tidak pasti.",
 ]},

{"d": "T5", "ep": None, "tema": "Usus & otak saling berhubung",
 "video": {"tajuk": "Perut tak selesa, mood pun ikut", "nota": CERITA + " " + TREND_NOTA + " Sticker: 13-blazer-tunjuk-atas-kanan.",
  "babak": [
   ("0–3s", "Momyizz pegang perut, muka muram", "Pernah perasan? Perut tak selesa, mood pun ikut jatuh 😣"),
   ("3–15s", "Animasi garisan antara otak dan usus (Flow)", "Saintis panggil ni 'paksi usus–otak': usus dan otak berhubung melalui saraf, hormon dan bakteria usus."),
   ("15–28s", "Momyizz bercakap ke kamera", "Ada kajian awal kaitkan bakteria usus dengan mood. Tapi pada manusia, masih banyak dikaji."),
   ("28–40s", "Pinggan: sayur, buah, kekacang, bijirin penuh", "Yang dah jelas: WHO saran serat 25 g sehari dari makanan. Ramai tak cukup."),
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
  "Tips tambah serat tanpa perut kembung 💡\n\n✅ Tambah sedikit demi sedikit, satu hidangan seminggu\n✅ Minum air kosong yang cukup\n✅ Pilih pelbagai sumber: sayur, buah, kekacang, bijirin penuh\n✅ Kunyah perlahan",
  "Info penting: sembelit berpanjangan, perubahan tabiat buang air yang mendadak, atau darah dalam najis perlu diperiksa doktor. ⚠️\n\nJangan bergantung pada julap atau teh 'detoks' berulang kali tanpa nasihat.",
 ],
 "wa": {"tajuk": "Produk serat / kesihatan usus Nutrilite (PERLU SEMAK nama)", "nota": "Ruang tertutup sahaja. Nama produk serat/usus Nutrilite (kategori 'Healthy Gut' di amway.my) PERLU SEMAK sebelum hantar. Makanan tetap sumber utama serat. Tiada dakwaan kesihatan.",
  "t": "Hai [nama] 😊\n\nMinggu ni Momyizz kongsi siri Tidur, Otak & Usus. Ramai tanya macam mana nak cukupkan serat bila sibuk.\n\nMomyizz utamakan sayur, buah dan kekacang dulu. Untuk hari yang betul-betul tak cukup, ada pilihan dari Nutrilite:\n• Produk: [NAMA PRODUK — semak amway.my]\n• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n• Cara guna: [salin dari label]\n\nIni pelengkap, bukan pengganti makanan. 🙏 Nak tahu lebih? Reply \"SERAT\" 💛\n\n" + DISC}},

{"d": "T6", "ep": None, "tema": "Makanan untuk otak: omega-3 & ikan tempatan",
 "video": {"tajuk": "Ikan kembung: makanan otak yang murah", "nota": CERITA + " " + TREND_NOTA + " Sticker: 19-blazer-thumbs-up.",
  "babak": [
   ("0–3s", "Ikan kembung di pasar / dapur", "Makanan otak tak semestinya mahal 🐟"),
   ("3–15s", "Momyizz bercakap ke kamera", "DHA, sejenis omega-3, ialah antara lemak utama dalam struktur otak dan mata (NIH)."),
   ("15–28s", "Momyizz masak ikan kembung / sardin", "Sumbernya: ikan berlemak seperti ikan kembung, sardin dan salmon. Badan hanya hasilkan sedikit sendiri."),
   ("28–40s", "Pinggan keluarga dengan ikan", "Matlamat Momyizz: ikan 2 kali seminggu untuk satu keluarga."),
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
  "Tips anak mahu makan ikan 💡\n\n✅ Buang tulang & jadikan isi ikan dalam bubur, nasi goreng atau roti\n✅ Sardin dalam tin: jadikan inti sandwich\n✅ Goreng tepung ringan / bakar dengan sedikit kunyit\n✅ Makan bersama, anak ikut contoh",
  "Info penting: sedang makan ubat cair darah atau ada masalah pendarahan? ⚠️\n\nTanya doktor atau ahli farmasi sebelum mengambil suplemen minyak ikan / omega-3, kerana ia boleh berinteraksi dengan ubat tertentu. (NIH)",
 ],
 "wa": {"tajuk": "Nutrilite Omega-3 Fish Oil Plus", "nota": "Ruang tertutup sahaja. Sahkan nama & kandungan semasa di amway.my. TIADA dakwaan otak / daya ingatan.",
  "t": "Hai [nama] 😊\n\nMinggu ni Momyizz kongsi pasal makanan untuk otak. Ada yang tanya, macam mana kalau keluarga jarang makan ikan?\n\nMomyizz utamakan ikan 2 kali seminggu. Untuk yang jarang makan ikan, ada pilihan pelengkap:\n*Nutrilite Omega-3 Fish Oil Plus* (sahkan nama semasa)\n• Kandungan EPA/DHA: [salin dari label]\n• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n\nKalau sedang makan ubat (terutama ubat cair darah), tanya doktor dulu ya. 🙏 Reply \"OMEGA\" kalau nak tahu lebih 💛\n\n" + DISC}},

{"d": "T7", "ep": None, "tema": "Jantung, otak & tidur: rumusan siri",
 "video": {"tajuk": "Apa yang baik untuk jantung, baik untuk otak", "nota": CERITA + " " + TREND_NOTA + " Sticker: 06-satin-lambai-dua-tangan.",
  "babak": [
   ("0–3s", "Momyizz tunjuk 7 nota kecil di peti ais", "7 hari siri Tidur, Otak & Usus. Ini yang Momyizz belajar 🧠❤️"),
   ("3–15s", "Nota: tidur, skrin, kafein", "Tidur 7 jam+, skrin keluar bilik, kopi terakhir sebelum petang."),
   ("15–28s", "Nota: serat, ikan, bergerak", "Serat dari sayur & buah, ikan 2 kali seminggu, bergerak setiap hari."),
   ("28–40s", "Momyizz ukur tekanan darah di klinik / rumah", "Dan buat saringan: tekanan darah, gula, kolesterol. Banyak yang tak tahu mereka ada."),
   ("40–45s", "Momyizz melambai", "Terima kasih ikut siri ni 💛 Topik apa seterusnya?"),
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
  "Daripada 7 hari siri ni, mana satu korang dah cuba? 🙋‍♀️\n\n😴 Tidur awal\n📱 Telefon luar bilik\n☕ Kopi sebelum petang\n🥦 Tambah serat\n🐟 Ikan 2x seminggu\n\nKomen nombor emoji korang!",
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

# ---------------------------------------------------------------- SUSUNAN AKHIR
# Hari 1-6 asal, kemudian siri trending (Hari 7-13), kemudian Hari 7-30 asal dianjak +7 (Hari 14-37).
def _susun():
    global DAYS, MG_FULL, MG_PLAN
    asal, mgf, mgp = DAYS, dict(MG_FULL), dict(MG_PLAN)
    baru, mgf2, mgp2 = [], {}, {}
    for day in asal[:6]:
        baru.append(day)
        if day["d"] in mgf:
            mgf2[day["d"]] = mgf[day["d"]]
    for i, t in enumerate(TRENDING):
        n = 7 + i
        mgf2[n] = MG_TREND[t["d"]]
        baru.append(dict(t, d=n))
    for day in asal[6:]:
        old, n = day["d"], day["d"] + len(TRENDING)
        if old in mgf:
            mgf2[n] = mgf[old]
        if old in mgp:
            mgp2[n] = mgp[old]
        baru.append(dict(day, d=n))
    DAYS, MG_FULL, MG_PLAN = baru, mgf2, mgp2



# ================================================================ TAMBAHAN SIRI TRENDING (selepas transkrip podcast disemak)
# Topik di bawah dipilih daripada isi sebenar podcast (lihat PODCAST_SEMAKAN.md). Fakta dari sumber rasmi sahaja.
TRENDING_BARU = [
{"d": "N1", "ep": None, "tema": "Bilik tidur & posisi tidur yang bantu lena",
 "video": {"tajuk": "5 benda yang Momyizz ubah dalam bilik tidur", "nota": CERITA + " " + TREND_NOTA + " Sticker: 19-blazer-thumbs-up.",
  "babak": [
   ("0–3s", "Bilik tidur malam, Momyizz pegang telefon & remote aircond", "Tidur 8 jam tapi bangun macam tak tidur? Semak bilik korang 🛏️"),
   ("3–15s", "Momyizz cas telefon di luar bilik, padam lampu tidur", "Satu: telefon keluar bilik. Dua: bilik gelap, tiada lampu tidur."),
   ("15–27s", "Momyizz laras suhu bilik, kipas perlahan", "Tiga: bilik sejuk dan selesa. Empat: mandi suam atau ambil wuduk sebelum tidur."),
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
  "Tips bilik lebih gelap tanpa belanja besar 💡\n\n✅ Tutup lampu tidur, guna lampu kecil di koridor jika perlu\n✅ Langsir tebal atau tampal kertas gelap di tingkap\n✅ Tutup cahaya LED dari charger & TV\n✅ Penutup mata pun boleh",
  "Info penting: plaster mulut waktu tidur tengah viral. ⚠️\n\nKajian ulasan 2025 dapati buktinya sedikit, dan ia boleh berbahaya jika hidung tersumbat. Kalau selalu bernafas ikut mulut atau berdengkur kuat, jumpa doktor dulu.",
 ]},

{"d": "N2", "ep": None, "tema": "Tidur sekejap (nap) 20–30 minit",
 "video": {"tajuk": "Ganti 'lunch berat' dengan nap 20 minit", "nota": CERITA + " " + TREND_NOTA + " Sticker: 08-satin-thumbs-up.",
  "babak": [
   ("0–3s", "Momyizz menguap depan laptop pukul 2 petang", "Pukul 2 petang, mata dah berat… 😪"),
   ("3–15s", "Teks atas skrin + animasi kapal terbang (Flow)", "Kajian NASA (1995): juruterbang yang tidur sekejap ~26 minit, kewaspadaan naik sehingga 54%."),
   ("15–28s", "Momyizz set penggera 20 minit, baring di bilik rehat", "Rahsianya: pendek. Lebih 30 minit, bangun boleh jadi lebih mamai."),
   ("28–40s", "Momyizz bangun segar, sambung kerja", "Dan buat awal petang, bukan lewat petang, supaya tak ganggu tidur malam."),
   ("40–45s", "Momyizz ke kamera", "Nap pendek, bukan nap panjang 😉"),
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
  "Tips nap di pejabat 💡\n\n✅ Set penggera 20 minit\n✅ Guna penutup mata atau kain gelap\n✅ Kalau minum kopi, minum sebelum nap (kopi ambil masa untuk berkesan)\n✅ Bangun, terus basuh muka & gerak sikit",
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
   ("28–40s", "Pinggan sarapan lengkap", "Telur + bijirin penuh + buah. Simple, murah, kenyang lama."),
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
  "Tips telur dadar penuh sayur dalam 5 minit 💡\n\n✅ 2 biji telur + bawang + sawi / bayam cincang\n✅ Tambah sedikit lada hitam\n✅ Masak dengan minyak sedikit\n✅ Makan dengan roti gandum\n\nProtein + sayur dalam satu pinggan!",
  "Info penting: produk 'pil minda' atau 'booster otak' banyak dijual. ⚠️\n\nSemak nombor pendaftaran MAL dan dakwaannya. Tiada pil yang menggantikan tidur cukup, makanan seimbang dan bergerak.",
 ],
 "wa": {"tajuk": "Nutrilite Soy Protein Drink (pilihan protein sarapan)", "nota": "Ruang tertutup sahaja. Tiada dakwaan otak / ingatan. Fakta & harga dari amway.my hari ini.",
  "t": "Hai [nama] 😊\n\nMinggu ni Momyizz kongsi pasal sarapan untuk otak: telur, oat dan buah. Ada yang tanya, macam mana kalau pagi betul-betul tak sempat?\n\nPilihan protein tambahan yang Momyizz guna: *Nutrilite Soy Protein Drink*\n• Perisa: [semak amway.my]\n• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.\n• Cara guna: [salin dari label]\n\nIni pelengkap, bukan pengganti sarapan sebenar. 🙏 Reply \"NAK\" kalau berminat 💛\n\n" + DISC}},

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

# Susunan siri trending akhir (Hari 7 dan seterusnya)
TREND_ORDER = ["T1", "T2", "T3", "N1", "N2", "T4", "T5", "N3", "N4", "T6", "N5", "N6", "T7"]
_semua = {t["d"]: t for t in TRENDING + TRENDING_BARU}
TRENDING = [_semua[k] for k in TREND_ORDER]


_susun()
