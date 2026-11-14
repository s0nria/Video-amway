# STANDARD PRODUKSI — Video Amway (Momyizz)

Status: **DISAHKAN** · **MENUNGGU** (tanya pengguna) · **CADANGAN** (draf, boleh diubah).

## Format — DISAHKAN (tempoh, platform, alat) · CADANGAN (teknikal)
| Perkara | Nilai |
|---|---|
| Nisbah | 9:16 menegak |
| Resolusi | 1080 × 1920 |
| Kadar bingkai | 30 fps |
| Tempoh | **Sasaran utama 60–75 s** (DISAHKAN 14 Nov 2026). Pilihan lain 45 s atau 90 s jika topik memerlukan (lihat `MASTER_WORKFLOW.md`) |
| Platform | **TikTok dan Instagram Reels** |
| Alat | **CapCut** (edit, sari kata, grafik) · **Flow** (jana klip B-roll AI) |
| Kekerapan | Sasaran **3 video sehari** (peringatan dalam worksheet, lihat `MASTER_WORKFLOW.md` Fasa 7) |

## Safe zone (kanvas 1080 × 1920) — CADANGAN
Kawasan yang selalu ditutup UI platform. Jangan letak teks penting, sticker, CTA atau penafian di sini.

| Sisi | Jarak dari tepi | Sebab |
|---|---|---|
| Atas | 160 px | Bar status, tab "Following/For You" |
| Bawah | 480 px | Caption, nama akaun, bar muzik |
| Kanan | 140 px | Butang like, komen, share |
| Kiri | 60 px | Margin keselamatan |

Kawasan selamat: x 60–940, y 160–1440. Lihat garis bantu dalam `TEMPLATES/MOTION_GRAPHICS_KIT/preview.html`.

## Teks & sari kata — DISAHKAN (font), CADANGAN (saiz)
- Sari kata: Nunito ExtraBold 800, warna Dakwat `#35362F` atas kotak Kertas `#FBF9F4`. Saiz 52–60 px, maksimum 2 baris, ~6 patah perkataan sebaris.
- Hook / big words: Fredoka Bold 700. Hook 88–110 px. Big word 130–160 px dalam warna Kayu `#A3876A` atau Sage gelap `#556A4C`.
- Nota tangan: Caveat Bold 700, maksimum satu pada satu masa.
- Bahasa: Bahasa Melayu santai. Ejaan konsisten. Istilah saintifik diterangkan dengan mudah.

## Audio — CADANGAN

### Kelajuan suara latar — DISAHKAN (14 Nov 2026)
- Rakaman suara Momyizz **dipercepat 1.2x** dalam setiap video (tanpa ubah pic suara; CapCut: Speed 1.2x, pilih "Pitch" kekal).
- Klip, grafik dan sari kata disusun ikut masa suara selepas dipercepat, supaya video jatuh dalam **60–75 s**.
- Potong ulangan, salah sebut dan frasa luar skrip sebelum mempercepat.

- Suara: puncak sekitar −6 dB, purata ~−14 LUFS.
- Muzik latar: 18–24 dB lebih rendah daripada suara.
- Sumber muzik — DISAHKAN: pustaka muzik **TikTok / CapCut**.
  - Untuk akaun perniagaan TikTok, hanya lagu dari **Commercial Music Library** boleh digunakan. Lagu trending biasa mungkin disekat atau dibisukan.
  - Claude tidak boleh menghasilkan fail muzik sebenar. Claude boleh cadangkan mood, tempo dan kata kunci carian untuk setiap video (contoh: "calm acoustic morning", "upbeat ukulele", 90–110 BPM).
  - Muzik yang didengar dalam video orang lain belum tentu boleh dipakai untuk video promosi produk.
- SFX (pop, whoosh, ding): sedikit sahaja, untuk big word atau pendedahan.

## Gerakan (motion) — CADANGAN
- Masuk: pop / skala 90%→100% + fade, 8–10 bingkai (0.3 s).
- Keluar: fade 6 bingkai (0.2 s).
- Easing: ease-out. Elakkan bounce berlebihan, glitch dan kesan neon (tak sesuai dengan gaya wellness lembut).
- Satu elemen grafik utama pada satu masa, selain sari kata.

## Eksport — CADANGAN
MP4 (H.264), 1080 × 1920, 30 fps, bitrate 12–16 Mbps, audio AAC 48 kHz 320 kbps.

## Senarai semak QC (Pintu 3)
- [ ] Fakta sepadan dengan skrip yang diluluskan. Tiada fakta "PERLU SEMAK"
- [ ] Tiada dakwaan perubatan, janji hasil atau tajuk menakutkan
- [ ] Label bukti pada setiap fakta kesihatan/mikroplastik
- [ ] Penafian "Perkongsian ilmu umum. Bukan nasihat perubatan." di skrin ≥ 3 s
- [ ] CTA tepat: "Nak dapatkan produk? Klik LINK di Bio"
- [ ] Tiada URL, nombor telefon atau WhatsApp dalam video
- [ ] Semua teks, sticker, CTA dan penafian dalam safe zone
- [ ] Sticker: satu set pakaian, satu di skrin pada satu masa, arah tunjuk betul, tidak tutup wajah/sari kata
- [ ] Hanya warna palet dan font Fredoka / Nunito / Caveat
- [ ] Sari kata sepadan dengan suara, tiada salah ejaan
- [ ] Audio seimbang, tiada bunyi pecah
- [ ] Klip AI (Flow) tidak menunjukkan produk Amway palsu, label rekaan atau hasil yang mengelirukan
- [ ] Muzik dari pustaka TikTok/CapCut yang dibenarkan untuk akaun anda
- [ ] Tiada unsur jenama lain (warna, template, CTA atau sticker bisnes lain)
