# -*- coding: utf-8 -*-
"""Sumber kalendar penulisan Momyizz (Amway).

Edit fail ini, kemudian jalankan:  python3 KALENDAR_PENULISAN/bina.py
Skrip itu menjana fail Markdown mingguan dan memasukkan data ke dalam worksheet.

Slot:
  pagi  = Personal branding (08:30, awam)
  tgh   = Edukasi / soft-sell (12:30, awam)
  mlm   = Interaksi (20:30, awam)
  tutup = Hard-sell, RUANG TERTUTUP sahaja (WhatsApp / group tertutup / DM)

Hari dengan teks penuh: fb, ig, th (senarai post Threads, setiap satu <= 500 aksara), wa (slot tutup).
Hari lain: idea + hook sahaja; worksheet sediakan butang "Salin arahan untuk Claude".
"""

DISC = "Perkongsian ilmu umum. Bukan nasihat perubatan."
CERITA = "Cerita peribadi mesti benar. Ubah butiran (anak, kerja, rutin) ikut kehidupan sebenar Momyizz sebelum post."

SLOT_INFO = {
    "pagi": ("08:30", "Personal branding"),
    "tgh": ("12:30", "Edukasi / soft-sell"),
    "mlm": ("20:30", "Interaksi"),
    "tutup": ("Bila sesuai", "Hard-sell (ruang tertutup)"),
}

DAYS = [
# ---------------------------------------------------------------- MINGGU 1
{"d": 1, "ep": 1, "tema": "Perkenalan + Mikroplastik: apa sebenarnya", "slots": [
 {"k": "pagi", "tajuk": "Perkenalan Momyizz", "nota": CERITA,
  "fb": """Hai korang, ini Momyizz. 👋

Ibu bekerja. Pagi kejar masa, petang kejar anak, malam baru ada masa untuk diri sendiri.

Satu tabiat Momyizz yang suami selalu gelak: setiap kali ada berita kesihatan viral, Momyizz tak terus kongsi. Momyizz cari dulu, apa WHO cakap, apa KKM cakap, kajian mana yang betul-betul wujud. 🔍

Sebab banyak sangat yang viral buat kita panik, padahal ceritanya tak semudah itu.

Jadi mulai hari ni, Momyizz nak kongsi apa yang Momyizz belajar. Tentang kesihatan keluarga, dapur, kulit dan gaya hidup. Ringkas, ada sumber, tanpa menakut-nakutkan.

Hari ni kita mula dengan satu perkataan yang selalu lalu di FYP: mikroplastik. Tengah hari nanti Momyizz kongsi apa yang Momyizz jumpa.

Korang pula, topik kesihatan apa yang paling selalu buat korang keliru? Komen, Momyizz senaraikan. 👇""",
  "ig": """Hai, ini Momyizz 👋 Ibu bekerja yang tak terus percaya benda viral.

Setiap kali ada berita kesihatan tular, Momyizz cari dulu: apa kata WHO, KKM dan kajian sebenar. 🔍

Mulai hari ni, Momyizz kongsi apa yang Momyizz belajar. Ringkas, ada sumber, tanpa panik.

Topik apa paling buat korang keliru? Komen 👇

#Momyizz #IbuBekerja #GayaHidupSihat #KesihatanKeluarga""",
  "th": ["Hai, ini Momyizz. Ibu bekerja yang ada satu tabiat pelik: setiap kali ada berita kesihatan viral, Momyizz tak kongsi dulu. Momyizz cari sumber dulu. 🔍",
         "Mulai hari ni Momyizz nak kongsi apa yang Momyizz jumpa. Kesihatan keluarga, dapur, kulit, gaya hidup. Ringkas, ada sumber, tanpa menakut-nakutkan.\n\nKorang, topik kesihatan apa yang paling selalu buat korang keliru?"]},
 {"k": "tgh", "tajuk": "Mikroplastik: apa sebenarnya", "nota": "Fakta dari Episod 1 (WHO 2019, 2022; UNEP).",
  "fb": """Mikroplastik. Semua orang cakap pasal ni. Tapi apa sebenarnya? 🤔

Ini yang Momyizz jumpa bila baca laporan WHO dan UNEP:

🔹 Mikroplastik ialah zarah plastik bersaiz kurang daripada 5 mm. Nanoplastik lebih kecil lagi. (WHO)
🔹 Datangnya dari plastik besar yang terurai, serat baju sintetik dan geseran tayar. (UNEP)
🔹 Memang terbukti ada di sekeliling kita: dalam air, makanan dan persekitaran. (WHO 2022)

Tapi ini bahagian yang jarang viral:
🔸 WHO (2019) kata, berdasarkan data yang ada, mikroplastik dalam air minuman pada tahap semasa belum menunjukkan risiko kesihatan yang jelas. Data masih terhad dan kajian diteruskan.
🔸 Kesan jangka panjang pada manusia masih dikaji.

Jadi tak perlu panik. Yang kita boleh buat ialah kurangkan pendedahan yang tak perlu, dengan cara yang mudah dan realistik. Esok Momyizz kongsi 3 langkah kecil yang Momyizz mula buat. 🌿

Sumber: WHO (2019, 2022), UNEP.
""" + DISC,
  "ig": """Mikroplastik: fakta, bukan panik 🌿

✅ Zarah plastik bawah 5 mm (WHO)
✅ Ada dalam air, makanan dan persekitaran (WHO 2022)
⏳ Kesan pada kesihatan manusia masih dikaji
ℹ️ WHO 2019: tahap semasa dalam air minuman belum tunjuk risiko jelas, data masih terhad

Save post ni. Esok Momyizz kongsi 3 langkah kecil yang realistik.

""" + DISC + """

#Momyizz #Mikroplastik #FaktaBukanPanik #KesihatanKeluarga""",
  "th": ["Mikroplastik ni sebenarnya apa? Momyizz baca laporan WHO dan UNEP semalam. Ringkasnya macam ni 🧵",
         "Mikroplastik = zarah plastik bawah 5 mm. Datang dari plastik yang terurai, serat baju sintetik, geseran tayar. Memang terbukti ada dalam air, makanan dan persekitaran. (WHO, UNEP)",
         "Yang jarang viral: WHO (2019) kata tahap semasa dalam air minuman belum tunjuk risiko kesihatan yang jelas. Data masih terhad, kajian diteruskan.\n\nJadi bukan panik. Kurangkan pendedahan yang tak perlu je. Esok Momyizz kongsi caranya."]},
 {"k": "mlm", "tajuk": "Poll botol air",
  "fb": """Soalan santai malam ni. 🌙

Botol air yang korang bawa ke tempat kerja atau sekolah anak, jenis apa?

A. Plastik
B. Kaca
C. Keluli tahan karat
D. Beli air botol je

Momyizz jawab dulu: dulu A, sekarang tengah tukar ke C. Cerita kenapa, esok pagi. 😄

Komen huruf korang 👇""",
  "ig": """Botol air korang jenis apa? 🤔

A. Plastik
B. Kaca
C. Keluli
D. Beli air botol je

Momyizz: dulu A, sekarang C. Komen huruf korang 👇

#Momyizz #BotolAir #GayaHidupSihat""",
  "th": ["Soalan malam: botol air yang korang bawa hari-hari, plastik, kaca, keluli, atau beli air botol je?\n\nMomyizz dulu plastik, sekarang tengah tukar ke keluli. Korang?"]},
]},

{"d": 2, "ep": 1, "tema": "3 langkah kecil kurangkan pendedahan", "slots": [
 {"k": "pagi", "tajuk": "Malam Momyizz baca laporan WHO", "nota": CERITA,
  "fb": """Semalam lepas anak-anak tidur, Momyizz duduk depan laptop dengan secawan teh. ☕

Bukan tengok drama. Baca laporan WHO pasal mikroplastik. 😅

Jujur, mula-mula rasa nak buang semua bekas plastik dalam rumah. Tapi makin baca, makin tenang. Sebab rupanya cara terbaik bukan buang semua, tapi ubah sikit-sikit yang mudah.

Itu satu benda yang Momyizz belajar jadi ibu: perubahan yang bertahan ialah perubahan yang kecil.

Tengah hari nanti Momyizz kongsi 3 langkah kecil yang Momyizz dah mula buat. 🌿

Korang pula, bila ada masa untuk diri sendiri, korang buat apa?""",
  "ig": """Malam semalam: anak tidur, teh panas, laporan WHO. ☕😅

Mula-mula rasa nak buang semua plastik. Makin baca, makin tenang.

Perubahan yang bertahan ialah perubahan yang kecil. 🌿

Masa untuk diri sendiri, korang buat apa? 👇

#Momyizz #IbuBekerja #MeTime #GayaHidupSihat""",
  "th": ["Malam tadi lepas anak tidur: teh panas + laporan WHO pasal mikroplastik. Bukan drama. 😅\n\nMula-mula nak buang semua plastik. Makin baca, makin tenang. Perubahan yang bertahan biasanya yang kecil je."]},
 {"k": "tgh", "tajuk": "3 langkah kecil", "nota": "Penyelesaian dari Episod 1.",
  "fb": """Tak perlu buang semua plastik esok pagi. 🙅‍♀️

Ini 3 langkah kecil yang Momyizz mula buat untuk kurangkan pendedahan mikroplastik yang tak perlu:

1️⃣ Botol plastik lama yang dah calar atau kusam, tukar ke botol kaca atau keluli tahan karat.
2️⃣ Jangan biar botol berisi air terlalu lama dalam kereta yang panas.
3️⃣ Kurangkan plastik sekali guna bila mudah. Contoh: bawa tumbler sendiri bila beli air.

Kenapa kecil? Sebab kecil senang diulang. Dan yang diulang itulah yang jadi tabiat. 💪

Ingat, ini tentang kurangkan pendedahan yang tak perlu, bukan takut. Kesan mikroplastik pada kesihatan manusia masih dikaji (WHO 2022).

Langkah mana korang nak cuba dulu? 1, 2 atau 3?

""" + DISC,
  "ig": """3 langkah kecil kurangkan mikroplastik 🌿

1️⃣ Tukar botol plastik yang dah calar
2️⃣ Jangan biar air botol dalam kereta panas
3️⃣ Bawa tumbler sendiri

Kecil, tapi senang diulang. Itulah yang jadi tabiat. 💪

Save untuk ingat. Korang nak mula langkah yang mana?

""" + DISC + """

#Momyizz #Mikroplastik #TipsRumah #GayaHidupSihat""",
  "th": ["Tak perlu buang semua plastik esok. Momyizz mula dengan 3 benda kecil je 🧵",
         "1. Botol plastik dah calar → tukar kaca atau keluli\n2. Jangan biar air dalam kereta panas lama-lama\n3. Bawa tumbler sendiri bila beli air",
         "Kecil sebab senang diulang. Yang diulang jadi tabiat.\n\nKorang nak cuba yang mana dulu?"]},
 {"k": "mlm", "tajuk": "Mitos atau fakta",
  "fb": """MITOS atau FAKTA? 🤔

"Mikroplastik dah terbukti menyebabkan penyakit pada manusia."

Komen jawapan korang. Esok tengah hari Momyizz dedahkan jawapan, dengan sumber sekali. 😉""",
  "ig": """MITOS atau FAKTA? 🤔

"Mikroplastik dah terbukti menyebabkan penyakit pada manusia."

Komen jawapan korang. Jawapan esok! 😉

#Momyizz #MitosAtauFakta #Mikroplastik""",
  "th": ["Mitos atau fakta: \"Mikroplastik dah terbukti menyebabkan penyakit pada manusia.\"\n\nJawab dulu. Esok Momyizz kongsi jawapan dengan sumber. 😉"]},
]},

{"d": 3, "ep": 1, "tema": "Cara baca label bukti", "slots": [
 {"k": "pagi", "tajuk": "Pagi kelam-kabut", "nota": CERITA,
  "fb": """6:45 pagi. 🕡

Seorang cari stokin, seorang tak jumpa botol air, bekal belum masuk beg, dan Momyizz masih belum sikat rambut. 😂

Pernah rasa pagi tu macam lari pecut, padahal hari baru mula?

Satu benda yang Momyizz perasan minggu ni: semua orang dalam rumah dah makan… kecuali Momyizz. Selalu "nanti la, sampai pejabat baru makan."

Esok Momyizz nak cerita pasal ni. Sebab rasanya ramai ibu macam ni juga.

Pagi korang pukul berapa paling kelam-kabut? ⏰""",
  "ig": """6:45 pagi: stokin hilang, botol air hilang, bekal belum masuk beg 😂

Dan Momyizz? Belum makan apa-apa. "Nanti la."

Ramai ibu macam ni juga kan? Esok Momyizz cerita.

Pagi korang paling kelam-kabut pukul berapa? ⏰

#Momyizz #IbuBekerja #RutinPagi #MomLife""",
  "th": ["6:45 pagi: stokin hilang, botol air hilang, bekal belum masuk beg. Dan Momyizz belum makan apa-apa. \"Nanti la.\" 😂\n\nIbu-ibu, korang pun selalu jadi orang terakhir makan?"]},
 {"k": "tgh", "tajuk": "Jawapan mitos + label bukti", "nota": "Jawapan kuiz semalam. Perkenal label bukti Momyizz.",
  "fb": """Jawapan semalam: MITOS. ❌

"Mikroplastik dah terbukti menyebabkan penyakit pada manusia" belum disokong bukti. WHO (2022) kata kesan jangka panjang pada manusia masih dikaji, dan belum ada bukti yang mengesahkan mikroplastik menyebabkan penyakit tertentu.

Tapi bukan bermaksud "tak ada apa-apa". Maksudnya sains masih mencari jawapan. 🔬

Sebab itu dalam setiap perkongsian, Momyizz letak label bukti:

🟢 Terbukti: disokong banyak kajian dan badan rasmi
🟠 Kajian awal: ada kajian, tapi masih sedikit atau dalam makmal
🔵 Masih dikaji: saintis belum ada jawapan
🔴 Bukti belum cukup: belum boleh buat kesimpulan

Supaya korang tahu mana yang pasti, mana yang belum. Tak perlu percaya bulat-bulat, tak perlu panik juga. 🌿

Berapa ramai yang jawab betul semalam? 🙋‍♀️

Sumber: WHO (2022).
""" + DISC,
  "ig": """Jawapan: MITOS ❌

Belum ada bukti mikroplastik menyebabkan penyakit tertentu pada manusia. Kesan jangka panjang masih dikaji (WHO 2022).

Label bukti dalam post Momyizz:
🟢 Terbukti
🟠 Kajian awal
🔵 Masih dikaji
🔴 Bukti belum cukup

Save supaya senang faham post akan datang 🌿

""" + DISC + """

#Momyizz #MitosAtauFakta #FaktaBukanPanik""",
  "th": ["Jawapan kuiz semalam: MITOS. Belum ada bukti mikroplastik menyebabkan penyakit tertentu pada manusia. Kesan jangka panjang masih dikaji. (WHO 2022)",
         "Sebab itu Momyizz letak label bukti dalam setiap post:\n🟢 Terbukti\n🟠 Kajian awal\n🔵 Masih dikaji\n🔴 Bukti belum cukup\n\nSupaya korang tahu mana yang pasti, mana yang belum."]},
 {"k": "mlm", "tajuk": "Teaser sarapan ibu",
  "fb": """Ibu-ibu, jujur sikit malam ni. 🙈

Pagi tadi korang sarapan apa?

☕ Kopi je
🍞 Roti sekeping sambil drive
🥣 Sarapan betul-betul
🤐 Tak sempat makan langsung

Momyizz… pilih yang kedua. Esok Momyizz kongsi kenapa ibu selalu jadi orang terakhir makan, dan cara mudah nak ubah. 💛""",
  "ig": """Pagi tadi korang sarapan apa? 🙈

☕ Kopi je
🍞 Roti sambil drive
🥣 Sarapan betul
🤐 Tak sempat langsung

Momyizz: yang kedua 😅 Esok kita sembang!

#Momyizz #SarapanIbu #IbuBekerja""",
  "th": ["Ibu-ibu, pagi tadi sarapan apa? Kopi je, roti sambil drive, sarapan betul, atau tak sempat langsung?\n\nMomyizz: roti sambil drive. 🙈"]},
]},

{"d": 4, "ep": 2, "tema": "Sarapan ibu yang selalu tertinggal", "slots": [
 {"k": "pagi", "tajuk": "Ibu makan paling akhir", "nota": CERITA,
  "fb": """Anak dah makan. Suami dah makan. Ibu? "Nanti la." 🙃

Momyizz baru perasan, hampir setiap pagi Momyizz jadi orang terakhir, kadang langsung tak sempat makan.

Lepas tu pukul 11 dah lapar sangat, capai apa yang ada. Petang balik, makan banyak sekali gus.

Bukan sebab kita tak tahu sarapan tu penting. Kita cuma selalu letak diri sendiri paling akhir.

Minggu ni Momyizz nak ubah satu benda kecil: siapkan "bekal ibu" sekali dengan bekal anak. 🍱

Siapa yang rasa tersentap sama? 🙋‍♀️""",
  "ig": """Anak dah makan. Suami dah makan. Ibu? "Nanti la." 🙃

Bukan sebab tak tahu. Kita cuma selalu letak diri sendiri paling akhir.

Minggu ni Momyizz cuba: siapkan bekal ibu sekali dengan bekal anak 🍱

Siapa sama? 🙋‍♀️

#Momyizz #SarapanIbu #IbuBekerja #SelfCare""",
  "th": ["Anak dah makan. Suami dah makan. Ibu? \"Nanti la.\" 🙃",
         "Bukan sebab kita tak tahu. Kita cuma selalu letak diri sendiri paling akhir.\n\nMinggu ni Momyizz cuba siapkan bekal ibu sekali dengan bekal anak. Siapa nak join?"]},
 {"k": "tgh", "tajuk": "Pinggan Sihat + Sarapan 5 Minit", "nota": "Fakta Episod 2 (KKM, Garis Panduan Diet Malaysia 2020).",
  "fb": """Sarapan ibu tak perlu mewah. Yang penting ada isi. 🍳

Panduan Pinggan Sihat Malaysia (KKM): separuh pinggan sayur dan buah, suku bijirin (utamakan bijirin penuh), suku protein seperti ikan, ayam, telur atau kekacang.

Untuk pagi, gabungan protein + karbohidrat kompleks + serat biasanya buat kita kenyang lebih lama berbanding minuman manis sahaja.

"Sarapan 5 Minit Ibu" versi Momyizz:
✅ Telur rebus (rebus malam sebelumnya) + roti gandum penuh + pisang
✅ Oat rendam semalaman dengan susu dan buah
✅ Siapkan bekal ibu sekali dengan bekal anak
✅ Segelas air kosong sebelum kopi

Garis Panduan Diet Malaysia juga galakkan kita hadkan gula tambahan, termasuk dalam minuman. ☕

Mana satu yang paling senang untuk korang?

Sumber: KKM, Garis Panduan Diet Malaysia 2020.
""" + DISC,
  "ig": """Sarapan 5 Minit Ibu 🍳

✅ Telur rebus + roti gandum + pisang
✅ Oat rendam semalaman + buah
✅ Bekal ibu sekali dengan bekal anak
✅ Air kosong dulu, baru kopi

Ikut Pinggan Sihat Malaysia (KKM): ada protein, bijirin penuh, buah atau sayur.

Save untuk minggu ni! 💛

""" + DISC + """

#Momyizz #SarapanSihat #PingganSihat #IbuBekerja""",
  "th": ["Sarapan ibu tak perlu mewah. Yang penting ada protein, bijirin penuh dan buah. (Pinggan Sihat Malaysia, KKM) 🧵",
         "Versi 5 minit Momyizz:\n• Telur rebus malam sebelumnya + roti gandum + pisang\n• Oat rendam semalaman + buah\n• Air kosong dulu, baru kopi",
         "Paling penting: siapkan bekal ibu sekali dengan bekal anak. Kalau dah siap, mesti makan.\n\nKorang pilih yang mana?"]},
 {"k": "mlm", "tajuk": "Kongsi menu sarapan",
  "fb": """Jom kumpul idea! 🙌

Apa menu sarapan paling laju korang, yang boleh siap bawah 5 minit?

Kongsi kat komen. Momyizz kumpulkan jadi satu senarai untuk semua ibu yang selalu terlupa makan pagi. 💛""",
  "ig": """Menu sarapan bawah 5 minit korang? ⏱️

Kongsi kat komen. Momyizz kumpul jadi satu senarai untuk semua ibu 💛

#Momyizz #SarapanSihat #IdeaSarapan""",
  "th": ["Apa menu sarapan paling laju korang? Bawah 5 minit. Kongsi, Momyizz nak curi idea. 👇"]},
]},

{"d": 5, "ep": 2, "tema": "Persediaan malam + hari kelam-kabut", "slots": [
 {"k": "pagi", "tajuk": "Persediaan malam 10 minit", "nota": CERITA,
  "fb": """Rahsia pagi Momyizz yang lebih tenang? Malam sebelumnya. 🌙

10 minit sebelum tidur:
🥚 Rebus 4 biji telur, simpan dalam peti
🥣 Oat masuk balang, tuang susu, letak buah
🎒 Bekal anak dan bekal ibu, bekas dah sedia atas meja

Pagi tadi, buat pertama kali minggu ni, Momyizz makan sarapan duduk. Lima minit je. Tapi rasa macam menang besar. 😂🏆

Kadang self-care tu bukan spa. Kadang dia cuma sarapan sambil duduk.

Korang ada rutin malam yang buat pagi lebih senang?""",
  "ig": """Pagi tenang bermula malam sebelumnya 🌙

🥚 Rebus telur
🥣 Oat rendam + buah
🎒 Bekas bekal dah sedia

Hasilnya: Momyizz sarapan sambil duduk. 5 minit pun rasa menang 😂🏆

Self-care tak semestinya spa 💛

#Momyizz #RutinMalam #SarapanIbu #SelfCare""",
  "th": ["Pagi tadi Momyizz sarapan sambil duduk. Lima minit je, tapi rasa macam menang. 😂\n\nRahsianya 10 minit malam sebelumnya: rebus telur, oat rendam, bekas bekal dah sedia.\n\nSelf-care tak semestinya spa."]},
 {"k": "tgh", "tajuk": "Hari yang betul-betul kelam-kabut (soft-sell)", "nota": "Soft-sell: pengalaman peribadi sahaja. Tiada harga, tiada ajakan beli (peraturan Amway: ruang awam). Nama produk sahaja; jangan tambah dakwaan.",
  "fb": """Realitinya, bukan setiap pagi berjalan ikut rancangan. 😅

Ada hari anak demam, ada hari mesyuarat awal, ada hari terlupa rebus telur.

Untuk hari macam tu, Momyizz ada "pelan B" yang tak sempurna, tapi lebih baik daripada perut kosong sampai tengah hari:
🍌 Pisang dan segenggam kacang dalam beg
🥛 Susu kotak kecil
🥤 Minuman protein yang Momyizz simpan untuk hari betul-betul tak sempat (Momyizz guna Nutrilite Soy Protein Drink)

Tapi Momyizz nak jujur: pelan B bukan pengganti sarapan sebenar. Makanan sebenar tetap nombor satu. Pelan B cuma untuk hari yang betul-betul kelam-kabut. 🙏

Pelan B korang apa?

""" + DISC,
  "ig": """Pelan B untuk pagi yang kelam-kabut 😅

🍌 Pisang + kacang
🥛 Susu kotak kecil
🥤 Minuman protein untuk hari betul-betul tak sempat

Jujur: pelan B bukan pengganti sarapan sebenar. Makanan sebenar tetap nombor satu 🙏

Pelan B korang apa?

""" + DISC + """

#Momyizz #SarapanIbu #IbuBekerja #RealitiIbu""",
  "th": ["Bukan setiap pagi ikut rancangan. Anak demam, mesyuarat awal, lupa rebus telur. 😅",
         "Pelan B Momyizz: pisang + kacang dalam beg, susu kotak kecil, atau minuman protein untuk hari yang betul-betul tak sempat.\n\nTapi pelan B bukan pengganti sarapan sebenar. Makanan sebenar tetap nombor satu.\n\nPelan B korang?"]},
 {"k": "mlm", "tajuk": "Pukul berapa makan pertama",
  "fb": """Soalan ringkas: semalam, pukul berapa korang makan makanan pertama? ⏰

🕖 Sebelum 8 pagi
🕘 8–10 pagi
🕛 Lepas 10 pagi
🙈 Tengah hari baru teringat

Momyizz semalam: 7:30 pagi, sambil duduk! 🎉""",
  "ig": """Semalam makan pertama pukul berapa? ⏰

🕖 Sebelum 8
🕘 8–10
🕛 Lepas 10
🙈 Tengah hari baru ingat

Momyizz: 7:30, sambil duduk 🎉

#Momyizz #SarapanIbu""",
  "th": ["Semalam korang makan pertama pukul berapa? Momyizz 7:30 pagi, sambil duduk. Satu pencapaian. 🎉"]},
 {"k": "tutup", "tajuk": "WhatsApp: Nutrilite Soy Protein Drink", "nota": "Ruang tertutup sahaja (pelanggan sedia ada / group tertutup / orang yang bertanya). Isi harga dan fakta dari amway.my hari ini. Jangan tambah dakwaan kesihatan.",
  "wa": """Hai [nama] 😊

Minggu ni Momyizz kongsi pasal sarapan ibu yang selalu tertinggal. Ramai tanya apa "pelan B" Momyizz untuk hari yang tak sempat makan.

Yang Momyizz guna: *Nutrilite Soy Protein Drink*
• Perisa: [semak amway.my: Mixed Berries 500g / Green Tea 450g]
• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.
• Cara guna: [salin dari label / amway.my]

Momyizz guna untuk hari kelam-kabut sahaja, bukan pengganti sarapan sebenar. 🙏

Kalau nak, reply "NAK" dan perisa pilihan, Momyizz uruskan. 💛

""" + DISC},
]},

{"d": 6, "ep": 2, "tema": "Kenapa Momyizz letak sumber + gula dalam minuman", "slots": [
 {"k": "pagi", "tajuk": "Kenapa Momyizz letak sumber", "nota": CERITA,
  "fb": """Ada yang tanya: "Momyizz, kenapa setiap post ada sumber? Penat tak?" 😄

Penat sikit. Tapi ada sebabnya.

Dulu Momyizz pernah kongsi satu tips kesihatan yang viral dalam group keluarga. Rupanya tak betul langsung. Malu? Sangat. 🙈

Sejak tu Momyizz janji dengan diri sendiri: kalau nak kongsi, mesti tahu datangnya dari mana. WHO, KKM, kajian yang betul-betul wujud.

Sebab bila korang baca post Momyizz, korang patut boleh percaya. Itu lebih penting daripada laju viral. 💛

Korang pernah termakan berita kesihatan palsu? Cerita sikit 👇""",
  "ig": """"Kenapa setiap post ada sumber?" 😄

Sebab dulu Momyizz pernah kongsi tips viral dalam group keluarga… rupanya salah. Malu sangat 🙈

Sejak tu: kalau nak kongsi, mesti tahu datangnya dari mana.

Percaya lebih penting daripada laju viral 💛

#Momyizz #FaktaBukanPanik #KesihatanKeluarga""",
  "th": ["Ada yang tanya kenapa setiap post Momyizz ada sumber.\n\nSebab dulu Momyizz pernah kongsi tips kesihatan viral dalam group keluarga. Rupanya salah. Malu sangat. 🙈\n\nSejak tu: tak tahu sumber, tak kongsi."]},
 {"k": "tgh", "tajuk": "Gula tambahan dalam minuman", "nota": "Fakta Episod 2 (Garis Panduan Diet Malaysia 2020). Jangan tambah angka gram tanpa sumber.",
  "fb": """Sarapan dah ok. Tapi minuman pagi kita macam mana? ☕🧋

Garis Panduan Diet Malaysia (KKM) galakkan kita hadkan gula tambahan, termasuk dalam minuman.

Yang Momyizz perasan dalam rutin sendiri: gula bukan banyak dalam makanan, tapi dalam air. Teh tarik pagi, kopi ais tengah hari, air kotak petang. Sikit-sikit, tapi berulang. 😅

Apa yang Momyizz cuba ubah (perlahan-lahan):
✅ Air kosong dulu, baru kopi atau teh
✅ Minta "kurang manis" bila beli
✅ Bawa botol air sendiri supaya kurang beli air manis

Bukan haramkan teh tarik. Cuma sedar dan kurangkan. 🌿

Minuman manis mana yang paling susah korang nak kurangkan?

Sumber: KKM, Garis Panduan Diet Malaysia 2020.
""" + DISC,
  "ig": """Gula paling banyak bukan dalam pinggan… tapi dalam cawan ☕🧋

KKM galakkan hadkan gula tambahan, termasuk dalam minuman.

Momyizz cuba:
✅ Air kosong dulu
✅ Minta kurang manis
✅ Bawa botol sendiri

Bukan haramkan teh tarik 😄 Sedar dan kurangkan.

""" + DISC + """

#Momyizz #KurangManis #GayaHidupSihat""",
  "th": ["Momyizz baru perasan: gula paling banyak dalam rutin Momyizz bukan dalam makanan. Dalam air. Teh tarik pagi, kopi ais tengah hari, air kotak petang. 😅",
         "KKM galakkan hadkan gula tambahan, termasuk dalam minuman. Bukan haramkan teh tarik. Air kosong dulu, minta kurang manis, bawa botol sendiri.\n\nMinuman manis mana paling susah korang tinggal?"]},
 {"k": "mlm", "tajuk": "Teaser span dapur",
  "fb": """Soalan jujur sebelum tidur. 🧽

Bila kali terakhir korang tukar span basuh pinggan?

A. Minggu ni
B. Bulan ni
C. Tak ingat…
D. Tunggu dia hancur 😂

Esok Momyizz kongsi satu kajian yang buat Momyizz terus pergi tukar span malam tu juga.""",
  "ig": """Bila kali terakhir tukar span basuh pinggan? 🧽

A. Minggu ni
B. Bulan ni
C. Tak ingat
D. Tunggu dia hancur 😂

Esok Momyizz kongsi kajian yang buat Momyizz terus tukar!

#Momyizz #DapurBersih #TipsRumah""",
  "th": ["Soalan jujur: bila kali terakhir korang tukar span basuh pinggan? 🧽\n\nEsok Momyizz kongsi kajian yang buat Momyizz terus tukar malam tu juga."]},
 {"k": "tutup", "tajuk": "WhatsApp: minta testimoni (pelanggan sedia ada)", "nota": "Untuk dapatkan testimoni SEBENAR. Guna testimoni hanya dengan kebenaran, tanpa dakwaan perubatan.",
  "wa": """Hai [nama] 😊 Terima kasih sebab percaya Momyizz.

Dah lebih kurang [tempoh] guna [produk]. Boleh kongsi sikit pengalaman [nama]? Contohnya macam mana [nama] guna dalam rutin harian, dan apa yang [nama] suka.

Kalau [nama] izinkan, Momyizz nak kongsi dalam group tertutup Momyizz (nama boleh disembunyikan). Kalau tak selesa pun takpe langsung. 💛"""},
]},

{"d": 7, "ep": 3, "tema": "Span dapur: penjaga kebersihan atau sarang kuman", "slots": [
 {"k": "pagi", "tajuk": "Rutin kemas dapur 10 minit", "nota": CERITA,
  "fb": """Rutin Momyizz lepas anak-anak tidur: 10 minit kemas dapur. 🌙

Bukan sebab rajin sangat. Tapi sebab pagi Momyizz jadi lebih tenang bila dapur dah bersih. 😌

Malam tadi, masa basuh pinggan, Momyizz pandang span dalam tangan. Nipis, dah kekuningan, bau masam sikit. Dah berapa minggu pun tak ingat. 🫣

"Tak apa, dia kan sentiasa bersabun." Itu yang Momyizz fikir selama ni.

Rupanya ada satu kajian yang cerita lain. Tengah hari nanti Momyizz kongsi.

Korang ada rutin malam kemas dapur juga?""",
  "ig": """10 minit kemas dapur setiap malam 🌙

Malam tadi pandang span dalam tangan: nipis, kekuningan, bau masam 🫣

"Tak apa, dia kan sentiasa bersabun."

Rupanya ada kajian yang cerita lain. Tengah hari nanti!

#Momyizz #DapurBersih #RutinMalam""",
  "th": ["Malam tadi pandang span basuh pinggan: nipis, kekuningan, bau masam. Dah berapa minggu pun tak ingat. 🫣\n\n\"Tak apa, dia sentiasa bersabun.\" Itu fikir Momyizz. Rupanya ada kajian yang cerita lain."]},
 {"k": "tgh", "tajuk": "Kajian span dapur", "nota": "Fakta Episod 3 (Cardinale et al. 2017; WHO 5 Kunci Makanan Lebih Selamat).",
  "fb": """Span basuh pinggan: penjaga kebersihan atau sarang kuman? 🧽

Kajian Cardinale et al. (2017, Scientific Reports) menemui kepadatan bakteria yang sangat tinggi dalam span dapur terpakai yang dikutip dari rumah. 🟢

Yang buat Momyizz terkejut: dalam kajian sama, span yang selalu "dibersihkan" dengan cara rumah tak semestinya kurang bakteria. Penulis kajian cadangkan span ditukar secara berkala, contohnya setiap minggu. 🟠

Kenapa? Span lembap, berliang dan ada sisa makanan. Tempat yang selesa untuk bakteria.

Rutin dapur yang Momyizz amalkan sekarang:
✅ Tulis tarikh pada span baru dengan marker
✅ Perah dan biar kering lepas guna, jangan rendam dalam sinki
✅ Kain lap meja dan kain lap pinggan diasingkan

Sabun yang bagus pun tak menggantikan tabiat tukar span tu ya. 😉

Bila kali terakhir korang tukar span? Jujur je kat komen. 😂

Sumber: Cardinale et al. (2017), WHO Five Keys to Safer Food.
""" + DISC,
  "ig": """Span dapur: bersih atau sarang kuman? 🧽

🟢 Kajian 2017 jumpa bakteria sangat tinggi dalam span dapur terpakai
🟠 Span yang "dibersihkan" cara rumah tak semestinya kurang bakteria. Penulis cadang tukar berkala, contoh setiap minggu

Tip Momyizz:
✅ Tulis tarikh pada span baru
✅ Perah & keringkan lepas guna
✅ Asingkan kain lap

Save & tag kawan! 😄

Sumber: Cardinale et al. (2017)

#Momyizz #DapurBersih #TipsRumah #Span""",
  "th": ["Bila kali terakhir korang tukar span basuh pinggan? Kajian ni buat Momyizz terus tukar malam tu juga 🧵",
         "Cardinale et al. (2017) jumpa kepadatan bakteria sangat tinggi dalam span dapur terpakai dari rumah. Span yang dibersihkan cara rumah pun tak semestinya kurang bakteria.",
         "Penulis cadang tukar span berkala, contohnya setiap minggu.\n\nTip Momyizz: tulis tarikh pada span baru, perah dan keringkan lepas guna. Korang tukar setiap berapa lama?"]},
 {"k": "mlm", "tajuk": "Poll span",
  "fb": """Lepas baca post tengah hari tadi… 😂

Berapa ramai yang terus pergi tukar span? 🙋‍♀️

Kalau dah tukar, komen "DAH ✅". Kalau belum, komen "ESOK 😅". Momyizz nak tengok siapa paling ramai!""",
  "ig": """Dah tukar span? 😂

Komen "DAH ✅" atau "ESOK 😅"

#Momyizz #DapurBersih""",
  "th": ["Lepas post span tengah hari tadi, berapa ramai yang terus pergi tukar? 🙋‍♀️ Momyizz dah. Tarikh pun dah tulis. 😂"]},
 {"k": "tutup", "tajuk": "WhatsApp: Amway Home Dish Drops", "nota": "Ruang tertutup sahaja. Fakta dan harga dari amway.my hari ini. Jangan dakwa sabun membunuh kuman atau menggantikan tukar span.",
  "wa": """Hai [nama] 😊

Hari ni Momyizz kongsi pasal span dapur. Ada yang tanya sabun basuh pinggan apa Momyizz guna.

Momyizz guna *DISH DROPS Concentrated Dishwashing Liquid (1L)* dari Amway Home.
• Harga: RM[HARGA] (semak amway.my, [tarikh]). Harga tertakluk kepada perubahan.
• Cara guna / sukatan: [salin dari label / amway.my]
• Kenapa Momyizz pilih: [pengalaman sebenar Momyizz]

Tapi ingat ya, sabun yang bagus tak menggantikan tabiat tukar span dan keringkan span. 🧽

Kalau berminat, reply "NAK", Momyizz uruskan. 💛"""},
]},

# ---------------------------------------------------------------- HARI 8-30 (rancangan; teks dijana dengan Claude)
{"d": 8, "ep": 3, "tema": "Kebersihan dapur: 5 kunci WHO", "plan": [
 ("pagi", "Barang dapur yang Momyizz tak kompromi", "Satu benda dalam dapur yang Momyizz tak kompromi langsung…"),
 ("tgh", "WHO 5 Kunci Makanan Lebih Selamat, versi dapur rumah", "WHO ada 5 kunci makanan selamat. Nombor 2 paling ramai terlepas."),
 ("mlm", "Tag kawan paling pembersih", "Tag kawan yang dapur dia paling bersih. 😄"),
 ("tutup", "Soalan lazim Dish Drops (dari soalan pelanggan sebenar)", "Ramai tanya pasal sabun pinggan Momyizz…")]},
{"d": 9, "ep": 3, "tema": "Kain lap & kesilapan dapur", "plan": [
 ("pagi", "Kesilapan dapur Momyizz dulu", "Dulu Momyizz guna satu kain lap untuk semua benda. 🙈"),
 ("tgh", "Kain lap meja vs kain lap pinggan: asingkan dan basuh", "Kain lap meja dan kain lap pinggan: korang asingkan tak?"),
 ("mlm", "Teaser: bekal dalam microwave", "Bekal dalam bekas plastik terus masuk microwave. Biasa buat?")]},
{"d": 10, "ep": 4, "tema": "Panaskan lauk dalam bekas plastik", "plan": [
 ("pagi", "Bekal ke pejabat setiap hari", "Pukul 12:30, beratur depan microwave pantri…"),
 ("tgh", "Kajian makmal Hussain et al. 2023 (label Kajian awal)", "Satu kajian makmal 2023 uji apa jadi bila bekas plastik masuk microwave."),
 ("mlm", "Korang panaskan bekal guna apa?", "Bekal korang panaskan dalam bekas apa?")]},
{"d": 11, "ep": 4, "tema": "Langkah mudah tanpa buang semua bekas", "plan": [
 ("pagi", "Pantri pejabat & kawan sepejabat", "Rakan sepejabat Momyizz tanya kenapa Momyizz bawa pinggan kaca…"),
 ("tgh", "3 langkah: pindah ke kaca, tukar bekas rosak, biar lauk sejuk", "Tak perlu buang semua bekas plastik. Buat 3 benda ni je."),
 ("mlm", "Mitos/fakta: label microwave safe", "Mitos atau fakta: 'microwave safe' bermaksud langsung tiada zarah plastik?")]},
{"d": 12, "ep": 4, "tema": "Cara baca berita kesihatan viral", "plan": [
 ("pagi", "Kenapa Momyizz tak panik bila baca tajuk viral", "Tajuk viral selalu lebih menakutkan daripada kajian sebenar."),
 ("tgh", "Kajian makmal vs badan manusia; FDA: belum ada bukti risiko", "Kajian makmal ≠ apa yang berlaku dalam badan kita. Ini bezanya."),
 ("mlm", "Teaser: botol air penuh sampai petang", "Balik kerja, botol air masih penuh. Angkat tangan siapa sama. 🙋‍♀️")]},
{"d": 13, "ep": 5, "tema": "Botol air masih penuh sampai petang", "plan": [
 ("pagi", "Botol air Momyizz yang tak terusik", "Pagi isi penuh, petang masih penuh. Kenapa jadi macam ni?"),
 ("tgh", "EFSA: ~2.0 L sehari wanita, termasuk dari makanan", "Berapa banyak air sebenarnya kita perlukan? Bukan semestinya 8 gelas."),
 ("mlm", "Lancar #CabaranAirMomyizz 7 hari", "Jom join #CabaranAirMomyizz 7 hari! Komen JOIN.")]},
{"d": 14, "ep": 5, "tema": "Trick minum air setiap hari", "plan": [
 ("pagi", "Cabaran hari 1: gambar botol Momyizz", "Hari 1 cabaran air. Ini botol Momyizz. Korang?"),
 ("tgh", "Trick segelas air lepas setiap waktu solat", "5 waktu solat = 5 gelas air. Trick paling senang Momyizz."),
 ("mlm", "Check-in cabaran", "Hari 1 cabaran: berapa gelas korang hari ni?"),
 ("tutup", "eSpring Water Purifier (hanya fakta spesifikasi rasmi; JANGAN dakwa singkir mikroplastik)", "Ramai tanya air apa Momyizz isi dalam botol…")]},
{"d": 15, "ep": 5, "tema": "Air kosong dulu, baru kopi", "plan": [
 ("pagi", "Rutin pagi: segelas air sebelum kopi", "Sebelum kopi pertama, Momyizz buat satu benda dulu."),
 ("tgh", "Dehidrasi ringan & fokus (label Kajian awal); letih berpanjangan jumpa doktor", "Petang selalu rasa blur? Mungkin kurang minum, mungkin juga sebab lain."),
 ("mlm", "Teaser: tertidur muka belum cuci", "Penat sangat sampai tertidur dengan muka belum cuci? 🙋‍♀️")]},
{"d": 16, "ep": 6, "tema": "Rutin kulit 5 minit selepas kerja", "plan": [
 ("pagi", "Pukul 10 malam, anak baru lena, Momyizz rebah", "Pukul 10 malam. 'Cuci muka esok je la…' 😴"),
 ("tgh", "AAD: cuci lembut, air suam, buang mekap sebelum tidur", "Cara cuci muka yang betul ikut pakar dermatologi (AAD)."),
 ("mlm", "Rutin malam korang berapa langkah?", "Rutin skincare malam korang berapa langkah?")]},
{"d": 17, "ep": 6, "tema": "SPF setiap hari + kenal jenis kulit", "plan": [
 ("pagi", "Dulang skincare sebelah sinki", "Tip paling berkesan Momyizz untuk rajin skincare: letak semua dalam satu dulang."),
 ("tgh", "AAD: pelembap + SPF 30 spektrum luas setiap hari", "Kalau boleh pilih satu langkah je, pakar pilih yang ni."),
 ("mlm", "Jenis kulit korang?", "Kering, berminyak, kombinasi atau sensitif? Komen jenis kulit korang."),
 ("tutup", "ARTISTRY Gel Cleanser + ARTISTRY Skin Analysis Experience (tiada janji hasil)", "Nak tahu jenis kulit sebenar sebelum beli apa-apa?")]},
{"d": 18, "ep": 6, "tema": "Konsisten lebih penting daripada banyak produk", "plan": [
 ("pagi", "Rak skincare Momyizz dulu vs sekarang", "Dulu 7 langkah. Sekarang 3. Kulit lebih ok."),
 ("tgh", "Rutin konsisten > bilangan produk; jangan beli ikut trend", "Rutin 3 langkah yang buat setiap hari menang rutin 10 langkah yang buat sekali-sekala."),
 ("mlm", "Teaser: air botol dalam bonet kereta", "Korang simpan air botol dalam kereta?")]},
{"d": 19, "ep": 7, "tema": "Air botol plastik: kajian 2024", "plan": [
 ("pagi", "Dua kotak air botol dalam bonet", "Hujung minggu Momyizz beli dua kotak air botol…"),
 ("tgh", "Qian et al. 2024 PNAS (Kajian awal) + WHO 2019 (Bukti belum cukup)", "Kajian 2024 kesan ratusan ribu zarah plastik dalam seliter air botol. Apa maksudnya?"),
 ("mlm", "Simpan air botol di mana?", "Air botol korang simpan di mana: rumah, kereta, pejabat?")]},
{"d": 20, "ep": 7, "tema": "Cara baca kajian dengan tenang", "plan": [
 ("pagi", "Apa yang Momyizz ubah lepas baca kajian ni", "Lepas baca kajian ni, Momyizz ubah dua benda je."),
 ("tgh", "Sampel terhad, mampu mengesan ≠ terbukti bahaya", "Kajian ni tak kata air botol bahaya. Ini sebabnya."),
 ("mlm", "Mitos/fakta: air botol dalam kereta panas", "Mitos atau fakta: kesan suhu tinggi pada botol plastik dah dikaji habis?")]},
{"d": 21, "ep": 7, "tema": "Rumusan 3 minggu", "plan": [
 ("pagi", "Refleksi 3 minggu Momyizz berkongsi", "3 minggu lepas Momyizz mula berkongsi. Ini yang Momyizz belajar daripada korang."),
 ("tgh", "Rumusan siri mikroplastik: 4 episod dalam 1 post", "Siri mikroplastik Momyizz dalam satu post. Save!"),
 ("mlm", "Undi topik seterusnya", "Topik apa korang nak Momyizz kupas lepas ni?")]},
{"d": 22, "ep": 8, "tema": "Vitamin C bukan hanya bila selesema", "plan": [
 ("pagi", "Anak bersin, Momyizz terus potong oren", "Setiap kali anak bersin, Momyizz terus potong oren. 🍊"),
 ("tgh", "NIH: badan tak hasilkan vitamin C; 75 mg wanita, 90 mg lelaki", "Badan kita langsung tak boleh hasilkan vitamin C sendiri."),
 ("mlm", "Buah apa selalu ada di rumah?", "Buah apa paling selalu ada di rumah korang?")]},
{"d": 23, "ep": 8, "tema": "Mitos vitamin C cegah selesema", "plan": [
 ("pagi", "Potong jambu, simpan dalam peti, anak senang capai", "Trick Momyizz supaya anak makan buah tanpa disuruh."),
 ("tgh", "Cochrane: tak terbukti cegah selesema bagi kebanyakan orang (Bukti belum cukup)", "Vitamin C cegah selesema? Ini kata kajian."),
 ("mlm", "Kuiz sumber vitamin C tempatan", "Teka: buah tempatan mana paling tinggi vitamin C?"),
 ("tutup", "Nutrilite Bio C Plus sebagai pelengkap (makanan tetap utama; tiada dakwaan cegah/rawat)", "Untuk hari yang susah dapat buah secukupnya…")]},
{"d": 24, "ep": 8, "tema": "Vitamin C & zat besi", "plan": [
 ("pagi", "Menu buah seminggu Momyizz", "Menu buah Momyizz minggu ni, bajet biasa je."),
 ("tgh", "Vitamin C bantu serap zat besi dari sumber tumbuhan (NIH)", "Makan sayur hijau? Tambah buah ni sekali."),
 ("mlm", "Teaser: duduk 9 jam sehari", "Kalau dikira, berapa jam korang duduk hari ni?")]},
{"d": 25, "ep": 9, "tema": "Duduk 9 jam sehari", "plan": [
 ("pagi", "Momyizz kira jam duduk semalam", "Semalam Momyizz kira: 9 jam duduk. Kereta, laptop, sofa."),
 ("tgh", "WHO 2020: 150–300 minit seminggu, sedikit lebih baik daripada tiada", "Tak sempat gym? WHO kata setiap pergerakan dikira."),
 ("mlm", "Lancar cabaran 10 Minit Gerak", "Jom cabaran 10 Minit Gerak 7 hari. Komen GERAK.")]},
{"d": 26, "ep": 9, "tema": "Gerak bersama anak", "plan": [
 ("pagi", "Jalan 10 minit lepas makan malam bawa anak", "Rutin baru keluarga Momyizz: jalan 10 minit lepas makan malam."),
 ("tgh", "Kurangkan masa duduk, intensiti apa pun dikira (WHO 2020)", "Berdiri masa jawab telefon pun dikira. Serius."),
 ("mlm", "Check-in cabaran gerak", "Hari ke berapa cabaran korang? Gerak apa hari ni?")]},
{"d": 27, "ep": 9, "tema": "Gerak dalam rutin kerja", "plan": [
 ("pagi", "Parkir jauh sikit, naik tangga", "Dua trick kecil Momyizz di tempat kerja."),
 ("tgh", "Latihan menguatkan otot 2 hari seminggu (WHO 2020)", "Bukan cardio je. WHO juga cadang latihan otot 2 kali seminggu."),
 ("mlm", "Teaser: skincare 7 langkah tapi sarapan skip", "Skincare 7 langkah, tapi sarapan skip? 🙋‍♀️")]},
{"d": 28, "ep": 10, "tema": "Glowing bermula dari pinggan", "plan": [
 ("pagi", "Rak skincare penuh, kulit tetap kusam", "Rak skincare Momyizz pernah penuh. Kulit? Tetap kusam."),
 ("tgh", "Vitamin C & kolagen; EPA/DHA dalam ikan kembung, sardin (NIH)", "Kulit bukan sekadar apa yang kita sapu."),
 ("mlm", "Pinggan glowing korang", "Kongsi pinggan makan tengah hari korang hari ni!")]},
{"d": 29, "ep": 10, "tema": "Pinggan Glowing Momyizz", "plan": [
 ("pagi", "Pinggan Glowing Momyizz seminggu", "Pinggan Glowing Momyizz: ikan 2 kali seminggu, ulam, buah, air."),
 ("tgh", "Kajian omega-3 untuk kulit masih terhad (Kajian awal); SPF tetap penting (AAD)", "Suplemen buat kulit glowing? Ini jawapan jujur."),
 ("mlm", "Luar + dalam: setuju?", "Glowing = luar + dalam. Setuju?"),
 ("tutup", "Nutrilite Omega-3 Fish Oil Plus (sahkan nama semasa) + ARTISTRY; tiada dakwaan mencerahkan", "Untuk yang jarang makan ikan…")]},
{"d": 30, "ep": 10, "tema": "Refleksi 30 hari", "plan": [
 ("pagi", "Terima kasih 30 hari bersama korang", "30 hari lepas Momyizz mula. Terima kasih korang. 💛"),
 ("tgh", "Rumusan 10 topik dalam satu post (save)", "10 perkara Momyizz kongsi bulan ni. Save satu post ni je."),
 ("mlm", "Undi topik kitaran seterusnya", "Bulan depan nak Momyizz kupas apa? Undi!"),
 ("tutup", "Ikuti pelanggan: tanya pengalaman & keperluan ulang beli", "Hai [nama], dah sebulan… macam mana setakat ni?")]},
]
