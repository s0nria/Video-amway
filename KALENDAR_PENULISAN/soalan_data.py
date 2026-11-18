# -*- coding: utf-8 -*-
"""Soalan berimpak tinggi: skrip prospek (ruang tertutup) + gilir jenis soalan untuk post awam.

Prinsip (DISAHKAN pengguna, 18 Nov 2026): "Sales bukan tentang bercakap banyak. Sales ialah tentang bertanya
soalan yang betul." Tanya dulu, dengar, ringkaskan semula, baru cadang.

Peraturan Momyizz:
- Orang pertama "Momyizz"; orang kedua "korang" (kumpulan) atau [nama] (satu orang). Bukan awak / anda.
- Tiada janji hasil ("berapa cepat nampak perubahan") dan tiada soalan yang menakut-nakutkan.
- Topik kesihatan: jika ada tanda perubatan, cadangkan doktor dahulu.
- Post awam: utamakan jenis 1-4; jenis 5 versi lembut & komitmen kecil tanpa jualan dibenarkan. Tiada produk / harga / closing.
  Komitmen membeli + cadangan produk: WhatsApp / DM sahaja.
- Key selling produk dari AMWAY_BRAND/KEY_SELLING.md (dipaparkan automatik dari PRODUK dalam kalendar_data.py).
"""

JENIS_SOALAN = {
 "keadaan": ("1", "Keadaan sekarang", "Faham situasi sebenar prospek"),
 "impian": ("2", "Impian / hasil diingini", "Tahu apa yang prospek mahu capai (tanpa janji hasil)"),
 "halangan": ("3", "Halangan", "Keluarkan punca sebenar mereka susah bergerak"),
 "emosi": ("4", "Emosi", "Faham apa yang paling mengganggu perasaan mereka"),
 "kesan": ("5", "Kesan (lembut)", "Bantu prospek nampak kesan jika keadaan berterusan, tanpa menakutkan"),
 "komitmen": ("6", "Komitmen", "Bawa kepada langkah seterusnya dengan pilihan, bukan desakan"),
}

# Gilir jenis soalan untuk teks 16:00 hari rancangan (hari tanpa teks penuh)
GILIR_AWAM = ["keadaan", "impian", "halangan", "emosi"]

# Teks 16:00 hari siap salin: (jenis, teks baharu atau None = kekal). Dikunci ikut tema supaya selamat jika susunan hari berubah.
# Hari 1-7 tidak diubah kerana sudah dipost.
SOALAN_AWAM = {
 "Tidur: masa otak 'membersihkan diri'": ("keadaan", None),
 "Papan pemotong & kain lap": ("halangan",
  "Soalan jujur: apa yang paling susah nak jaga kebersihan dapur bila balik kerja dah penat? 🧽\n\nA. Tak ada tenaga lagi\nB. Anak-anak perlukan perhatian\nC. Tak tahu nak mula dari mana\nD. Tak ada orang tolong\n\nMomyizz: A, hampir setiap hari. 😅"),
 "Berapa jam tidur ibu & anak": ("emosi",
  "Ibu-ibu, bila anak tidur lewat malam sekolah, apa yang paling korang risau? 🌙\n\n😴 Esok dia mengantuk di kelas\n😤 Pagi jadi drama nak bangun\n😔 Rasa bersalah tak tegas\n🥱 Kita pun ikut tidur lewat\n\nMomyizz: yang last tu. Selalu! 😅"),
 "Kesilapan dapur yang biasa": ("keadaan", None),
 "Panaskan bekal dalam bekas plastik": ("halangan",
  "Soalan: apa yang buat korang masih guna bekas plastik untuk panaskan bekal? 🍱\n\n💸 Bekas kaca mahal\n🎒 Berat nak bawa\n🙈 Dah biasa\n🤷 Tak tahu pun ada beza\n\nTak ada jawapan salah. Momyizz pun dulu 'dah biasa'. 😄"),
 "Skrin & cahaya malam": ("halangan",
  "Jujur: apa yang paling susah bila nak letak telefon di luar bilik waktu tidur? 📱\n\n⏰ Guna sebagai jam loceng\n📲 Takut terlepas mesej penting\n😶 Scroll tu je masa untuk diri sendiri\n🙈 Dah jadi tabiat\n\nMomyizz: nombor 3. Korang?"),
 "Bekal sihat ke pejabat": ("impian",
  "Soalan: kalau ada bekal sihat yang boleh siap dalam 1 minit, korang paling nak guna waktu bila? 🍱\n\n🌅 Sarapan masa kalut\n🕛 Makan tengah hari di meja kerja\n🕓 Snek petang\n🚗 Dalam perjalanan\n\nKomen pilihan korang! 👇"),
 "Bilik tidur & posisi tidur yang bantu lena": ("keadaan", None),
 "Cara baca berita kesihatan (bahagian 2)": ("emosi",
  "Bila dapat berita kesihatan yang menakutkan dalam group keluarga, apa perasaan pertama korang? 📱\n\n😰 Terus risau\n🤔 Ragu-ragu\n😤 Geram sebab selalu palsu\n🔍 Terus nak semak\n\nMomyizz dulu nombor 1. Sekarang cuba jadi nombor 4. 😄"),
 "Minum air cukup": ("impian",
  "Soalan: kalau korang dapat minum air cukup setiap hari, perubahan apa yang korang paling harap rasa? 💧\n\n⚡ Petang tak terlalu letih\n🧠 Lebih fokus kerja\n😊 Mood lebih stabil\n🚽 Perut lebih selesa\n\nMomyizz: nombor 1! Korang?"),
 "Tidur sekejap (nap) 20–30 minit": ("halangan",
  "Jujur: apa yang halang korang nak nap 20 minit masa rehat kerja? 😪\n\n🏢 Tak ada tempat sesuai\n😳 Segan dengan rakan sekerja\n⏰ Takut terlajak tidur\n📋 Kerja tak habis\n\nMomyizz: takut terlajak, jadi set penggera 20 minit! ⏰"),
 "Cabaran Air 7 hari": ("komitmen", None),
 "Kafein & tidur": ("kesan",
  "Soalan: kalau tidur korang selalu terganggu, apa yang paling cepat terjejas? 😴\n\n💼 Fokus kerja\n😤 Sabar dengan anak & pasangan\n🍩 Selera makan manis\n🚗 Mengantuk masa memandu\n\nMomyizz: nombor 2. Tidur tak cukup = sumbu pendek! 😅"),
 "Usus & otak saling berhubung": ("halangan",
  "Jujur: apa yang paling susah nak cukupkan sayur & buah setiap hari? 🥦\n\n⏰ Tak sempat masak\n💸 Harga naik\n👧 Anak tak suka\n🙈 Lupa beli\n\nMomyizz: tak sempat masak hari bekerja. Korang?"),
 "Sarapan untuk otak: telur, oat & bijirin": ("impian",
  "Soalan: kalau masa tak jadi masalah, sarapan ideal korang macam mana? 🍳\n\n🥚 Telur + roti gandum\n🥣 Oat + buah\n🍚 Nasi lemak (jujur! 😂)\n🥤 Minuman berkhasiat yang cepat\n\nKomen sarapan impian korang 👇"),
 "Makanan untuk otak: omega-3 & ikan tempatan": ("emosi",
  "Ibu-ibu, bila anak tolak makan ikan, apa yang korang rasa? 🐟\n\n😩 Penat pujuk\n😔 Risau dia tak cukup khasiat\n😤 Geram sebab dah masak susah-susah\n🤷 Biar je, esok cuba lagi\n\nMomyizz: semua sekali dalam satu malam. 😂"),
 "Jantung, otak & tidur: rumusan siri": ("komitmen", None),
}

# Skrip prospek ikut topik. Langkah: (kod jenis atau tahap, tajuk, [mesej...]). Gunakan [nama] untuk prospek.
# "produk": kunci dalam PRODUK (kalendar_data.py) atau None. "amalan": cadangan tanpa produk (sentiasa didahulukan).
SKRIP = {
 "bodykey": {"tajuk": "Sarapan, bekal & urus berat (BodyKey Meal Shake)", "produk": "bodykey",
  "amalan": "Sarapan ada protein + serat; sediakan pelan B untuk hari kalut; makan ikut Pinggan Sihat.",
  "doktor": "Ada diabetes, buah pinggang, hamil atau makan ubat tertentu: tanya doktor sebelum guna pengganti makanan.",
  "langkah": [
   ("pembuka", "Sapa & minta izin", ["Hai [nama] 😊 Terima kasih komen di post sarapan Momyizz. Boleh Momyizz tanya sikit pasal rutin pagi [nama]? Supaya Momyizz tak bagi cadangan yang tak sesuai."]),
   ("keadaan", "Keadaan sekarang", ["Biasanya pagi [nama] sempat sarapan tak? Selalu makan apa?", "Waktu kerja pula, makan tengah hari macam mana: bawa bekal, beli atau kadang-kadang skip?"]),
   ("impian", "Impian", ["Kalau boleh ubah satu benda dalam cara [nama] makan, apa yang [nama] paling nak?", "Bagi [nama], sarapan yang 'cukup baik' tu macam mana?"]),
   ("halangan", "Halangan", ["Apa yang paling susah setakat ni? Masa, tak tahu nak makan apa, atau dah cuba tapi tak kekal?", "Ada apa-apa yang buat [nama] ragu-ragu nak cuba benda baharu untuk sarapan?"]),
   ("emosi", "Emosi", ["Bila skip makan dan lapar sangat tengah hari, apa yang [nama] rasa? Ada ganggu kerja atau mood?"]),
   ("kesan", "Kesan (lembut)", ["Kalau rutin sekarang berterusan beberapa bulan lagi, [nama] okay ke, atau ada benda yang [nama] harap boleh berubah?"]),
   ("ringkas", "Ringkaskan semula", ["Jadi kalau Momyizz faham betul: pagi [nama] selalu kalut, kadang skip sarapan, dan [nama] nak sesuatu yang cepat tapi berkhasiat. Betul tak?"]),
   ("cadang", "Cadangan (amalan dulu, produk kemudian)", ["Langkah pertama yang Momyizz cadang: [amalan]. Untuk hari yang betul-betul kalut, ada satu pilihan yang Momyizz sendiri guna: [produk]."]),
   ("komitmen", "Komitmen (pilihan, bukan desakan)", ["[nama] nak cuba untuk sarapan dulu, atau untuk bekal waktu kerja?", "Nak Momyizz sediakan 1 kotak perisa pisang dulu untuk cuba, atau nak tengok perisa lain dulu?"]),
   ("susulan", "Bila prospek kata 'nanti dulu'", ["Takpe [nama], tak perlu terburu-buru 😊 Boleh Momyizz tahu apa yang buat [nama] nak fikir dulu? Harga, rasa, atau nak tanya keluarga?", "Momyizz mesej semula minggu depan ya. Sementara tu, cuba dulu tips sarapan 5 minit yang Momyizz kongsi."]),
  ]},
 "espring": {"tajuk": "Air minuman di rumah (eSpring)", "produk": "espring",
  "amalan": "Minum air kosong cukup; didihkan air jika keruh selepas banjir; tukar kartrij ikut jadual.",
  "doktor": None,
  "langkah": [
   ("pembuka", "Sapa & minta izin", ["Hai [nama] 😊 Nampak [nama] berminat dengan topik air minuman. Boleh Momyizz tanya sikit pasal air di rumah?"]),
   ("keadaan", "Keadaan sekarang", ["Sekarang air minuman di rumah dari mana? Masak air paip, beli air botol, atau ada penapis?", "Berapa orang dalam rumah, dan siapa yang paling banyak minum?"]),
   ("impian", "Impian", ["Kalau boleh pilih, air minuman macam mana yang [nama] nak untuk keluarga?"]),
   ("halangan", "Halangan", ["Apa yang paling leceh dengan cara sekarang? Angkat botol, masak air, atau risau kebersihan?", "Pernah fikir nak guna penapis? Apa yang buat [nama] belum buat keputusan?"]),
   ("emosi", "Emosi", ["Bila dengar berita pasal air keruh atau gangguan bekalan, apa yang paling [nama] risau?"]),
   ("kesan", "Kesan (lembut)", ["Kalau terus beli air botol setiap minggu, [nama] rasa okay dari segi kos dan masa?"]),
   ("ringkas", "Ringkaskan semula", ["Jadi [nama] nak air minuman yang mudah, sentiasa sedia dan lebih yakin untuk keluarga. Betul?"]),
   ("cadang", "Cadangan", ["Asasnya: [amalan]. Untuk rumah Momyizz, Momyizz pilih [produk]."]),
   ("komitmen", "Komitmen", ["[nama] nak Momyizz terangkan cara pemasangan dulu, atau nak tahu kos penggantian kartrij dulu?"]),
   ("susulan", "Bila prospek kata 'nanti dulu'", ["Faham, ini keputusan besar untuk rumah 😊 Apa yang [nama] perlu tahu lagi supaya senang bincang dengan pasangan?"]),
  ]},
 "soy": {"tajuk": "Protein harian (Soy Protein Drink)", "produk": "soy",
  "amalan": "Protein dalam setiap hidangan: telur, ikan, tauhu, tempe, kekacang.",
  "doktor": "Ada masalah buah pinggang atau alahan soya: tanya doktor dahulu.",
  "langkah": [
   ("pembuka", "Sapa & minta izin", ["Hai [nama] 😊 Boleh Momyizz tanya sikit pasal pemakanan harian [nama]?"]),
   ("keadaan", "Keadaan sekarang", ["Dalam sehari, [nama] rasa protein cukup tak? Biasanya dari mana: ayam, ikan, telur, tauhu?"]),
   ("impian", "Impian", ["Apa yang [nama] harap dari pemakanan yang lebih baik? Lebih kenyang, lebih bertenaga, atau sokong senaman?"]),
   ("halangan", "Halangan", ["Apa yang buat susah nak cukupkan protein? Masa, bajet, atau tak suka makan banyak?"]),
   ("emosi", "Emosi", ["Ada tak waktu [nama] rasa cepat lapar atau letih, dan itu ganggu hari [nama]?"]),
   ("ringkas", "Ringkaskan semula", ["Jadi [nama] nak cara mudah untuk tambah protein bila tak sempat makan dengan lengkap. Betul?"]),
   ("cadang", "Cadangan", ["Mula dengan [amalan]. Bila tak sempat, Momyizz guna [produk]."]),
   ("komitmen", "Komitmen", ["[nama] nak guna untuk sarapan, atau selepas bersenam?"]),
   ("susulan", "Bila prospek kata 'nanti dulu'", ["Takpe 😊 Momyizz kongsi dulu senarai sumber protein murah, nanti kita sembang lagi."]),
  ]},
 "dish": {"tajuk": "Kebersihan dapur (Dish Drops)", "produk": "dish",
  "amalan": "Tukar span berkala, keringkan span, asingkan kain lap.",
  "doktor": None,
  "langkah": [
   ("pembuka", "Sapa & minta izin", ["Hai [nama] 😊 Seronok tengok [nama] komen pasal span dapur. Boleh Momyizz tanya pasal rutin dapur [nama]?"]),
   ("keadaan", "Keadaan sekarang", ["Sehari berapa kali basuh pinggan? Guna sabun macam mana: picit atas span atau bancuh dalam besen?"]),
   ("impian", "Impian", ["Apa yang [nama] nak dari sabun pinggan: jimat, kuat buang minyak, atau lembut di tangan?"]),
   ("halangan", "Halangan", ["Apa yang paling mengganggu dengan sabun sekarang? Cepat habis, minyak susah tanggal, atau tangan kering?"]),
   ("emosi", "Emosi", ["Bila pinggan masih berminyak walaupun dah basuh, apa yang [nama] rasa?"]),
   ("ringkas", "Ringkaskan semula", ["Jadi [nama] nak sabun yang jimat dan berkesan, dan tak keringkan tangan. Betul?"]),
   ("cadang", "Cadangan", ["Asasnya: [amalan]. Sabun yang Momyizz guna: [produk]."]),
   ("komitmen", "Komitmen", ["[nama] nak cuba 1 botol dulu, atau nak Momyizz tunjuk cara sukat supaya jimat?"]),
   ("susulan", "Bila prospek kata 'nanti dulu'", ["Takpe 😊 Bila sabun sekarang dah nak habis, mesej Momyizz ya."]),
  ]},
 "bioc": {"tajuk": "Vitamin C & buah harian (Bio C Plus)", "produk": "bioc",
  "amalan": "Satu hidangan buah tinggi vitamin C setiap hari (jambu batu, betik, oren).",
  "doktor": "Ada batu karang, masalah buah pinggang atau makan ubat tertentu: tanya doktor dahulu. Tiada dakwaan cegah selesema.",
  "langkah": [
   ("pembuka", "Sapa & minta izin", ["Hai [nama] 😊 Boleh Momyizz tanya sikit pasal makan buah dalam keluarga [nama]?"]),
   ("keadaan", "Keadaan sekarang", ["Seminggu, berapa hari keluarga [nama] makan buah?"]),
   ("impian", "Impian", ["Apa yang [nama] harap bila keluarga makan lebih seimbang?"]),
   ("halangan", "Halangan", ["Apa yang buat susah nak makan buah setiap hari: harga, cepat rosak, atau anak tak suka?"]),
   ("emosi", "Emosi", ["Bila anak tak nak makan buah, apa yang paling [nama] risau?"]),
   ("ringkas", "Ringkaskan semula", ["Jadi [nama] nak pastikan keluarga dapat vitamin C walaupun hari sibuk. Betul?"]),
   ("cadang", "Cadangan", ["Makanan tetap utama: [amalan]. Sebagai pelengkap untuk dewasa, ada [produk]."]),
   ("komitmen", "Komitmen", ["[nama] nak cuba untuk diri sendiri dulu, atau untuk pasangan juga?"]),
   ("susulan", "Bila prospek kata 'nanti dulu'", ["Takpe 😊 Cuba dulu trick potong buah simpan dalam peti yang Momyizz kongsi."]),
  ]},
 "cleanser": {"tajuk": "Rutin cuci muka (ARTISTRY Balancing Jelly Cleanser)", "produk": "cleanser",
  "amalan": "Cuci muka lembut 2 kali sehari, air suam, buang mekap sebelum tidur, pelembap.",
  "doktor": "Jerawat teruk, gatal, ruam atau kulit pedih berterusan: jumpa doktor / pakar kulit.",
  "langkah": [
   ("pembuka", "Sapa & minta izin", ["Hai [nama] 😊 Boleh Momyizz tanya sikit pasal rutin kulit [nama]? Supaya cadangan sesuai dengan jenis kulit."]),
   ("keadaan", "Keadaan sekarang", ["Kulit [nama] macam mana sekarang: berminyak, kering, kombinasi atau sensitif?", "Rutin malam sekarang ada berapa langkah?"]),
   ("impian", "Impian", ["Apa yang [nama] paling nak rasa lepas cuci muka? Bersih, tak ketat, atau segar?"]),
   ("halangan", "Halangan", ["Apa yang buat rutin susah kekal: penat, terlalu banyak produk, atau belum jumpa yang sesuai?", "Ada pengalaman tak best dengan produk sebelum ni?"]),
   ("emosi", "Emosi", ["Bila kulit tak selesa, ada ganggu keyakinan [nama] masa kerja atau keluar?"]),
   ("ringkas", "Ringkaskan semula", ["Jadi [nama] nak rutin ringkas yang bersihkan tanpa rasa ketat. Betul?"]),
   ("cadang", "Cadangan", ["Asas rutin: [amalan]. Pencuci yang Momyizz guna sekarang: [produk]. (Semak jenis kulit yang sesuai mengikut maklumat rasmi.)"]),
   ("komitmen", "Komitmen", ["[nama] nak cuba pencuci dulu, atau nak buat analisis kulit dulu?"]),
   ("susulan", "Bila prospek kata 'nanti dulu'", ["Takpe 😊 Cuba dulu rutin 5 minit yang Momyizz kongsi, nanti kita sembang lagi."]),
  ]},
 "uv": {"tajuk": "Pelindung matahari harian (ARTISTRY UV Protect)", "produk": "uv",
  "amalan": "SPF spektrum luas setiap pagi, sapu semula bila lama di luar.",
  "doktor": "Tompok kulit yang berubah bentuk / warna: jumpa doktor.",
  "langkah": [
   ("pembuka", "Sapa & minta izin", ["Hai [nama] 😊 Boleh Momyizz tanya pasal rutin pagi kulit [nama]?"]),
   ("keadaan", "Keadaan sekarang", ["[nama] pakai pelindung matahari setiap hari tak? Kalau tak, bila biasanya pakai?"]),
   ("impian", "Impian", ["Pelindung matahari macam mana yang [nama] selesa pakai setiap hari?"]),
   ("halangan", "Halangan", ["Apa yang buat malas pakai: melekit, berminyak, putih di muka, atau lupa?"]),
   ("emosi", "Emosi", ["Bila nampak tompok atau kulit kusam, apa yang [nama] rasa?"]),
   ("ringkas", "Ringkaskan semula", ["Jadi [nama] nak SPF yang ringan dan selesa supaya rajin pakai setiap hari. Betul?"]),
   ("cadang", "Cadangan", ["Asasnya: [amalan]. Yang Momyizz guna: [produk]."]),
   ("komitmen", "Komitmen", ["[nama] nak cuba untuk kerja harian dulu?"]),
   ("susulan", "Bila prospek kata 'nanti dulu'", ["Takpe 😊 Yang penting pakai SPF setiap hari, apa pun jenamanya."]),
  ]},
 "omega": {"tajuk": "Omega-3 & ikan (Salmon Omega Complex)", "produk": "omega",
  "amalan": "Ikan berlemak (kembung, sardin, salmon) 2 kali seminggu.",
  "doktor": "Makan ubat cair darah atau ada masalah pendarahan: tanya doktor sebelum ambil minyak ikan. Tiada dakwaan otak / ingatan.",
  "langkah": [
   ("pembuka", "Sapa & minta izin", ["Hai [nama] 😊 Boleh Momyizz tanya sikit pasal menu ikan dalam keluarga [nama]?"]),
   ("keadaan", "Keadaan sekarang", ["Seminggu, berapa kali keluarga [nama] makan ikan? Ikan jenis apa?"]),
   ("impian", "Impian", ["Apa yang [nama] harap dari menu keluarga yang lebih seimbang?"]),
   ("halangan", "Halangan", ["Apa yang buat susah: anak tak suka, tulang, bau, atau harga?"]),
   ("emosi", "Emosi", ["Bila anak tolak ikan, apa yang paling [nama] risau?"]),
   ("ringkas", "Ringkaskan semula", ["Jadi keluarga [nama] jarang makan ikan berlemak, dan [nama] cari cara mudah untuk lengkapkan. Betul?"]),
   ("cadang", "Cadangan", ["Utamakan [amalan]. Untuk yang jarang makan ikan, ada pelengkap [produk]."]),
   ("komitmen", "Komitmen", ["[nama] nak cuba untuk diri sendiri dulu, atau untuk pasangan juga?"]),
   ("susulan", "Bila prospek kata 'nanti dulu'", ["Takpe 😊 Cuba dulu resipi sardin & ikan kembung yang Momyizz kongsi."]),
  ]},
 "tidur": {"tajuk": "Tidur & rehat (tiada produk)", "produk": None,
  "amalan": "Waktu tidur konsisten, telefon di luar bilik, bilik gelap & sejuk, nap 20 minit sahaja.",
  "doktor": "Berdengkur kuat, tercungap waktu tidur, atau sangat mengantuk walaupun tidur cukup: jumpa doktor (kajian tidur).",
  "langkah": [
   ("pembuka", "Sapa & minta izin", ["Hai [nama] 😊 Terima kasih kongsi pasal tidur [nama]. Boleh Momyizz tanya sikit?"]),
   ("keadaan", "Keadaan sekarang", ["Biasanya [nama] tidur pukul berapa dan bangun pukul berapa?", "Bangun rasa segar, atau masih penat?"]),
   ("impian", "Impian", ["Kalau tidur [nama] lebih baik, apa yang [nama] paling harap berubah dalam hari [nama]?"]),
   ("halangan", "Halangan", ["Apa yang paling buat [nama] tidur lewat atau terjaga? Anak, telefon, kerja, atau fikiran?"]),
   ("emosi", "Emosi", ["Bila tak cukup tidur, apa yang paling terkesan: sabar, fokus atau mood?"]),
   ("ringkas", "Ringkaskan semula", ["Jadi [nama] tidur lewat sebab itu saja masa untuk diri sendiri, dan esoknya penat. Betul?"]),
   ("cadang", "Cadangan (amalan sahaja)", ["Cuba satu dulu minggu ni: [amalan]. Kalau ada tanda seperti berdengkur kuat, jumpa doktor ya."]),
   ("komitmen", "Komitmen", ["[nama] nak cuba telefon di luar bilik dulu, atau tidur 15 minit lebih awal dulu?"]),
   ("susulan", "Susulan", ["Momyizz tanya lagi minggu depan, macam mana tidur [nama] 😊"]),
  ]},
}

# Padankan mesej WhatsApp dengan skrip: kata kunci dalam tajuk WA -> kunci SKRIP
PADANAN_WA = [("bodykey", "bodykey"), ("espring", "espring"), ("soy", "soy"), ("dish", "dish"),
              ("bio c", "bioc"), ("cleanser", "cleanser"), ("uv protect", "uv"), ("spf", "uv"),
              ("omega", "omega"), ("salmon", "omega"), ("serat", "bodykey")]
