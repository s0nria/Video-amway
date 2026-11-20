# -*- coding: utf-8 -*-
"""Versi pendek teks untuk post Facebook berlatar warna.

Facebook hanya membenarkan latar warna untuk teks pendek (lebih kurang 130 aksara atau kurang).
Setiap entri: tema hari -> (10:00 info ringkas, 16:00 pertanyaan, 21:00 info penting / alert).
Tips 18:30 tidak perlu: di Facebook ia dipost sebagai carousel tips.
Hari 1-8 tiada versi pendek kerana sudah dipost. Jalankan bina.py selepas edit (had 130 aksara disemak).
"""

HAD_FB = 130

FB_PENDEK = {
 "Papan pemotong & kain lap": (
  "Papan pemotong kayu atau plastik? Dua-dua ok 🔪 Yang penting: basuh dengan air panas & sabun lepas setiap guna.",
  "Apa paling susah nak jaga dapur bersih bila balik kerja dah penat? 🧽 Komen jujur 👇",
  "Ada alahan makanan dalam keluarga? Guna papan & pisau berasingan untuk kacang, makanan laut & telur ⚠️"),
 "Berapa jam tidur ibu & anak": (
  "Tidur kini antara 8 perkara utama kesihatan jantung (AHA 2022) ❤️🌙 Sama penting dengan makan & bergerak.",
  "Ibu-ibu, bila anak tidur lewat malam sekolah, apa yang paling korang risau? 🌙",
  "Mata berat masa memandu? Berhenti di tempat selamat & rehat ⚠️ Tingkap terbuka atau radio kuat tak membantu."),
 "Kesilapan dapur yang biasa": (
  "Jangan basuh ayam mentah di sinki 🍗 Percikan air bawa bakteria ke sekeliling. Masak sampai masak sempurna. (USDA)",
  "Jujur: korang masih basuh ayam mentah dalam sinki? 🙈 Ya / Kadang-kadang / Dah berhenti",
  "Cirit-birit berdarah, demam tinggi atau muntah sampai tak boleh minum? Terus ke klinik ⚠️ (CDC)"),
 "Panaskan bekal dalam bekas plastik": (
  "'Microwave safe' bermaksud bekas direka untuk microwave 🍱 Tiada label? Pindah dulu ke pinggan kaca.",
  "Apa yang buat korang masih panaskan bekal dalam bekas plastik? 🍱 Komen 👇",
  "Bekas plastik retak, melengkung, berubah warna atau berbau? Masa untuk tukar ⚠️"),
 "Skrin & cahaya malam": (
  "Cahaya skrin waktu malam boleh tekan melatonin, hormon yang buat kita mengantuk 📱🌙 (Harvard Health)",
  "Apa paling susah bila nak letak telefon di luar bilik waktu tidur? 📱",
  "Anak 6–12 tahun perlukan 9–12 jam tidur sehari (AASM) ⚠️ Cuba 'stesen cas keluarga' di ruang tamu."),
 "Bekal sihat ke pejabat": (
  "Nasi perang lebih tinggi serat daripada nasi putih 🍚 Tak biasa? Mula dengan campur separuh-separuh.",
  "Kalau ada bekal sihat siap dalam 1 minit, korang nak guna waktu bila? 🍱",
  "Bekal berkuah jangan dibiar lebih 2 jam di suhu bilik ⚠️ Ragu-ragu? Buang. (USDA)"),
 "Bilik tidur & posisi tidur yang bantu lena": (
  "Bilik tidur ideal: senyap, gelap, tenang & suhu selesa 🛏️ (CDC) Bilik korang dah cukup berapa?",
  "Korang tidur posisi apa? 😴 Telentang / mengiring kiri / mengiring kanan / meniarap",
  "Plaster mulut waktu tidur tengah viral ⚠️ Bukti masih sedikit & berisiko jika hidung tersumbat."),
 "Cara baca berita kesihatan (bahagian 2)": (
  "FDA: belum ada bukti tahap mikroplastik dalam makanan berisiko kepada manusia 🔬 Kajian diteruskan. Tak perlu panik.",
  "Dapat berita kesihatan menakutkan dalam group keluarga, apa perasaan pertama korang? 📱",
  "Berat turun tanpa sebab? Jangan anggap rezeki ⚠️ Jumpa doktor untuk pemeriksaan. (NHS)"),
 "Minum air cukup": (
  "Makin berumur, rasa dahaga makin kurang 👵🏻 Ingatkan mak ayah minum sedikit-sedikit sepanjang hari. (NHS)",
  "Kalau minum air cukup setiap hari, perubahan apa yang korang paling harap rasa? 💧",
  "Cuaca panas: pening, loya atau keliru boleh jadi tanda strok haba ⚠️ Dapatkan rawatan segera."),
 "Tidur sekejap (nap) 20–30 minit": (
  "Kajian NASA: nap kira-kira 26 minit, kewaspadaan juruterbang naik sehingga 54% 😴✈️",
  "Apa yang halang korang nak nap 20 minit masa rehat kerja? 😪",
  "Mengantuk teruk setiap hari walaupun tidur cukup? Jumpa doktor, jangan terus tambah kopi ⚠️"),
 "Cabaran Air 7 hari": (
  "Purata 66 hari untuk tabiat baharu jadi automatik (Lally 2010) 🗓️ Tak sempurna tak apa, sambung esok.",
  "Siapa nak join #CabaranAirMomyizz 7 hari? 💧 Komen JOIN 🙋‍♀️",
  "Gangguan bekalan air? Simpan dalam bekas bersih bertutup & didihkan sebelum minum jika ragu ⚠️"),
 "Kafein & tidur": (
  "Kafein 6 jam sebelum tidur masih boleh kurangkan tidur, dan kita tak sedar ☕🌙 (kajian 2013)",
  "Bila tidur selalu terganggu, apa paling cepat terjejas: fokus, sabar atau selera? 😴",
  "Minuman tenaga tinggi kafein & gula ⚠️ Hamil, menyusu atau ada masalah jantung? Rujuk doktor dulu."),
 "Usus & otak saling berhubung": (
  "WHO saran 25g serat sehari dari makanan, dan 400g sayur & buah 🌾🥦",
  "Apa paling susah nak cukupkan sayur & buah setiap hari? 🥦",
  "Sembelit berpanjangan atau darah dalam najis? Jumpa doktor, jangan bergantung pada teh 'detoks' ⚠️"),
 "Sarapan untuk otak: telur, oat & bijirin": (
  "Kuning telur kaya kolin, yang badan guna untuk hasilkan asetilkolin, penting untuk ingatan 🥚 (NIH)",
  "Kalau masa tak jadi masalah, sarapan ideal korang apa? 🍳",
  "'Pil minda' banyak dijual ⚠️ Semak nombor MAL. Tiada pil ganti tidur, makanan seimbang & bergerak."),
 "Makanan untuk otak: omega-3 & ikan tempatan": (
  "DHA (omega-3) antara lemak utama dalam otak & mata 🐟 Sumber terbaik: ikan kembung, sardin. (NIH)",
  "Ibu-ibu, bila anak tolak makan ikan, apa yang korang rasa? 🐟",
  "Makan ubat cair darah? Tanya doktor sebelum ambil minyak ikan / omega-3 ⚠️ (NIH)"),
 "Jantung, otak & tidur: rumusan siri": (
  "8 perkara jantung & otak (AHA): makan, gerak, tanpa rokok, tidur, berat, tekanan darah, gula, kolesterol ❤️🧠",
  "Daripada siri Tidur, Otak & Usus, tabiat mana yang korang dah mula? 🙋‍♀️",
  "1 dalam 2 yang ada kolesterol tinggi tak tahu (NHMS 2023) ⚠️ Satu ujian darah boleh beri jawapan."),
}
