# Spesifikasi Komponen

Kanvas 1080 × 1920. Kawasan selamat: x 60–940, y 160–1440 (CADANGAN, lihat `PRODUCTION_STANDARD.md`).
Gerakan lalai: masuk pop 90%→100% + fade 0.3 s, keluar fade 0.2 s, ease-out.

---

## `HOOK` — tajuk pembuka (0–3 s)
- Kotak Kertas `#FBF9F4`, jejari 36 px, bayang lembut. Lebar maksimum 880 px.
- Teks: Fredoka Bold 700, 88–110 px, Dakwat `#35362F`. 1 perkataan kunci boleh diwarnakan Kayu `#A3876A`.
- Kedudukan: sepertiga atas (y ~220–600).
- Sticker sesuai: tunjuk atas (`01`/`03`), tutup mulut (`04`/`14`).
- Tiada tajuk sensasi atau menakutkan.

## `SARI_KATA` — sari kata ayat
- Kotak Kertas, padding 20 × 32 px, jejari 24 px.
- Nunito ExtraBold 800, 52–60 px, Dakwat. Maksimum 2 baris.
- Kedudukan: y ~1180–1400 (atas sempadan bawah safe zone).
- Muncul per ayat, tanpa animasi perkataan demi perkataan yang berlebihan.

## `BIG_WORD` — perkataan besar penekanan
- Fredoka Bold 700, 130–160 px (mesti muat dalam safe zone), Kayu `#A3876A` atau Sage gelap `#556A4C`, tanpa kotak.
- 1–2 perkataan sahaja. Tengah skrin. Pop masuk + SFX ringan.
- Maksimum 3 kali dalam satu video.

## `KAD_FAKTA` — kad fakta
- Kotak Kertas, lebar 880 px, jejari 36 px. Jalur atas 12 px dalam warna pilar.
- Tajuk kecil: Fredoka SemiBold 600, 44 px, warna pilar. Isi: Nunito 800, 48 px, Dakwat. Maksimum 25 patah perkataan.
- Sumber: Nunito 800, 28 px, Sage gelap, di bawah isi (contoh "Sumber: WHO, 2022").
- Sentiasa bersama `LABEL_BUKTI`.

## `LABEL_BUKTI` — label tahap bukti
- Pil, tinggi 64 px, jejari penuh. Teks Fredoka SemiBold 600, 32 px, putih Kertas.
- Warna: Terbukti `#4E7347` · Kajian awal `#B07C3A` · Masih dikaji: warna **MENUNGGU** (tiada dalam BRAND.md) · Bukti belum cukup `#A65B4B`.
- Kedudukan: penjuru kiri atas `KAD_FAKTA`.

## `LABEL_PILAR` — tag pilar
- Pil kecil, tinggi 52 px, latar warna pilar, teks Kertas, Fredoka 600, 28 px.
- Kedudukan: atas kiri skrin (dalam safe zone) pada 3 s pertama, atau atas `KAD_FAKTA`.

## `CHECKLIST` — senarai semak / tip
- Panel Sage lembut `#E2E8D9`, jejari 36 px, lebar 880 px.
- Setiap baris: bulatan Sage `#7F9373` dengan tanda ✓ Kertas, teks Nunito 800, 46 px.
- Maksimum 4 baris. Baris muncul satu demi satu (selang 0.4 s).
- Sticker sesuai: thumbs up (`08`/`19`).

## `KAUNTER` — angka beranimasi
- Angka Fredoka Bold 700, 160 px, Sage gelap. Unit/label Nunito 800, 44 px, Dakwat.
- Kira naik 0.8–1.2 s. Hanya angka yang ada sumber.

## `KAD_PRODUK` — pengenalan produk
- Panel Linen `#EAE1D0`, jejari 36 px. Gambar produk rasmi di tengah (latar dibuang).
- Nama produk: Fredoka 700, 56 px, Dakwat. 1–2 baris fakta Nunito 800, 40 px, **disalin tepat dari amway.my**.
- Tiada harga, tiada dakwaan perubatan, tiada janji hasil.

## `NOTA_TANGAN` — nota kecil
- Caveat Bold 700, 56–64 px, Kayu atau Sage gelap. Boleh ada anak panah lakaran.
- Maksimum satu di skrin pada satu masa.

## `PENAFIAN` — penafian wajib
- Teks tepat: **"Perkongsian ilmu umum. Bukan nasihat perubatan."**
- Nunito 800, 30–34 px, Dakwat pada kotak Kertas 85% legap, jejari 16 px.
- Kedudukan: dalam safe zone, di atas sari kata (y ~1100) atau atas kiri. Tempoh ≥ 3 s. Sebaiknya di babak fakta atau penutup.

## `CTA` — penutup
- Teks tepat: **"Nak dapatkan produk? Klik LINK di Bio"**
- Kotak Kertas, sempadan 6 px Sage gelap `#556A4C`, jejari 36 px, lebar 880 px.
- "Nak dapatkan produk?" Nunito 800, 48 px, Dakwat. "Klik LINK di Bio" Fredoka 700, 72 px, Sage gelap.
- Kedudukan: y ~900–1300. Sticker `02-blazer-tunjuk-bawah` di atas kotak, tunjuk ke CTA.
- Tempoh 3–5 s terakhir. Tiada URL, nombor telefon atau WhatsApp.

## `STICKER` — sticker Momyizz
- PNG lutsinar dari `AMWAY_BRAND/STICKERS/`. Lebar 35–45% skrin (380–490 px).
- Satu di skrin pada satu masa. Satu set pakaian setiap video. Arah tunjuk ke elemen yang dimaksudkan.
- Masuk: pop + goyang kecil 0.3 s. Tidak menutup wajah, sari kata atau CTA.

---

## Template alat edit
| Komponen | Alat | Nama / pautan template | Status |
|---|---|---|---|
| Semua | **MENUNGGU** | | Belum dibina |
