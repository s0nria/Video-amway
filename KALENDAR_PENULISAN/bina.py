#!/usr/bin/env python3
"""Bina kalendar penulisan: semak had aksara, jana Markdown, masukkan data ke worksheet.

Guna:  python3 KALENDAR_PENULISAN/bina.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from kalendar_data import DAYS, JENIS_TEKS, PRODUK, MG_FULL, MG_PLAN, MG_INFO  # noqa: E402
from masalah_data import MASALAH, CARA_BETUL, SUMBER  # noqa: E402
from soalan_data import JENIS_SOALAN, GILIR_AWAM, SOALAN_AWAM, SKRIP, PADANAN_WA  # noqa: E402


def skrip_untuk(teks):
    t = (teks or "").lower()
    for kata, kunci in PADANAN_WA:
        if kata in t:
            return kunci
    return None


def soalan_json():
    sk = {}
    for k, s in SKRIP.items():
        pr = PRODUK.get(s["produk"]) if s["produk"] else None
        sk[k] = {"tajuk": s["tajuk"], "amalan": s["amalan"], "doktor": s["doktor"],
                 "produk": {"nama": pr[0], "ks": pr[2]} if pr else None,
                 "langkah": [{"kod": kod, "tajuk": tj, "mesej": m} for kod, tj, m in s["langkah"]]}
    return {"jenis": {k: list(v) for k, v in JENIS_SOALAN.items()}, "skrip": sk}


def md_skrip():
    L = ["# Skrip Soalan Prospek (WhatsApp / DM / group tertutup)", "",
         "> \"Sales bukan tentang bercakap banyak. Sales ialah tentang bertanya soalan yang betul.\"", "",
         "Aliran: sapa → keadaan → impian → halangan → emosi → kesan (lembut) → ringkaskan semula → cadangan (amalan dulu, produk kemudian) → komitmen → susulan.",
         "Gantikan [nama] dengan nama prospek. Dalam worksheet: tab **Tulis** → **Skrip prospek** untuk butang salin.", "",
         "## 6 jenis soalan", "", "| # | Jenis | Tujuan |", "|---|---|---|"]
    L += [f"| {n} | {nm} | {tj} |" for n, nm, tj in JENIS_SOALAN.values()]
    L += ["", "Post awam: utamakan jenis 1–4; jenis 5 versi lembut & komitmen kecil tanpa jualan dibenarkan. Komitmen membeli & cadangan produk: ruang tertutup sahaja.", ""]
    for k, s in SKRIP.items():
        pr = PRODUK.get(s["produk"]) if s["produk"] else None
        L += [f"## {s['tajuk']}", ""]
        if s["doktor"]:
            L += [f"> ⚠️ {s['doktor']}", ""]
        for kod, tj, mesej in s["langkah"]:
            L += [f"**{tj}**", ""]
            for m in mesej:
                m = m.replace("[amalan]", s["amalan"].rstrip(".")).replace("[produk]", pr[0] if pr else "(tiada produk)")
                L += [f"- {m}"]
            L += [""]
        if pr:
            L += [f"Key selling (dari `AMWAY_BRAND/KEY_SELLING.md`): {pr[2]}", "", "Harga: semak amway.my pada hari itu.", ""]
    return "\n".join(L)

LIMIT_TH, LIMIT_IG, LIMIT_SLAID = 500, 2200, 260
BANNED = re.compile(r"(?<![A-Za-z])(aku|kau|saya|awak|anda)(?![A-Za-z])", re.I)


def _strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _strings(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield from _strings(v)


def check():
    errs = []
    for day in DAYS:
        if "video" in day and not carousel_tips(day["teks"][2])["cukup"]:
            errs.append(f"Hari {day['d']}: teks tips 18:30 perlu sekurang-kurangnya 2 baris ✅ / 1️⃣ untuk carousel tips")
    for tema, (jenis, teks) in SOALAN_AWAM.items():
        if jenis not in JENIS_SOALAN:
            errs.append(f"SOALAN_AWAM '{tema}': jenis '{jenis}' tidak sah")
        if jenis in ("kesan", "komitmen") and teks and ("RM" in teks or "order" in teks.lower()):
            errs.append(f"SOALAN_AWAM '{tema}': post awam tidak boleh ada harga / order")
        if teks and len(teks) > LIMIT_TH:
            errs.append(f"SOALAN_AWAM '{tema}': {len(teks)} aksara (> {LIMIT_TH})")
        if teks and BANNED.search(teks):
            errs.append(f"SOALAN_AWAM '{tema}': kata ganti nama dilarang")
        if not any(d["tema"] == tema for d in DAYS):
            errs.append(f"SOALAN_AWAM: tema '{tema}' tiada dalam kalendar")
    for k, s in SKRIP.items():
        if s["produk"] and s["produk"] not in PRODUK:
            errs.append(f"SKRIP {k}: produk '{s['produk']}' tiada dalam PRODUK")
        for _, _, mesej in s["langkah"]:
            for m in mesej:
                if BANNED.search(m):
                    errs.append(f"SKRIP {k}: kata ganti nama dilarang dalam '{m[:40]}'")
    for day in DAYS:
        tag = f"Hari {day['d']}"
        if day.get("produk", ("",))[0] not in PRODUK:
            errs.append(f"{tag}: perlu 'produk' (kunci dalam PRODUK)")
        if "video" in day:
            if len(day["teks"]) != len(JENIS_TEKS):
                errs.append(f"{tag}: perlu {len(JENIS_TEKS)} teks")
            for i, t in enumerate(day["teks"], 1):
                if len(t) > LIMIT_TH:
                    errs.append(f"{tag}: teks {i} = {len(t)} aksara (> {LIMIT_TH})")
            for i, t in enumerate(day["carousel"]["slaid"], 1):
                if len(t) > LIMIT_SLAID:
                    errs.append(f"{tag}: slaid {i} = {len(t)} aksara (> {LIMIT_SLAID})")
            for f in ("video", "carousel"):
                if len(day[f]["caption"]) > LIMIT_IG:
                    errs.append(f"{tag}: caption {f} terlalu panjang")
        if day["d"] in MG_FULL:
            mg = MG_FULL[day["d"]]
            if len(mg) != len(MG_INFO):
                errs.append(f"{tag}: perlu {len(MG_INFO)} video motion grafik dalam MG_FULL")
            for i, v in enumerate(mg, 1):
                if not 4 <= len(v["babak"]) <= 7:
                    errs.append(f"{tag}: motion grafik {i} perlu 4–7 babak")
                if len(v["caption"]) > LIMIT_IG:
                    errs.append(f"{tag}: caption motion grafik {i} terlalu panjang")
        elif day["d"] not in MG_PLAN:
            errs.append(f"{tag}: tiada motion grafik (MG_FULL) atau idea (MG_PLAN)")
        for t in list(_strings(day)) + list(_strings(MG_FULL.get(day["d"], []))) + list(_strings(MG_PLAN.get(day["d"], ()))):
            m = BANNED.search(t)
            if m:
                errs.append(f"{tag}: guna '{m.group(0)}' (guna Momyizz / korang)")
                break
    for m in MASALAH:
        for k, v in m.items():
            if isinstance(v, str):
                hit = BANNED.search(v)
                if hit:
                    errs.append(f"Masalah {m['n']} {k}: guna '{hit.group(0)}'")
            if k == "sumber":
                errs += [f"Masalah {m['n']}: sumber '{x}' tiada dalam SUMBER" for x in v if x not in SUMBER]
    return errs


def masalah_json():
    return {"items": MASALAH, "cara": CARA_BETUL, "sumber": SUMBER}


def md_masalah():
    L = ["# 20 Masalah Paling Mendesak — Audiens Momyizz", "",
         "Audiens: **ibu bekerja / wanita Malaysia 25–45 tahun yang menjaga keluarga**. Disusun ikut kesanggupan membayar (paling tinggi dahulu).",
         "Dalam worksheet: tab **Tulis** → **20 Masalah audiens** → butang **Salin arahan untuk Claude** pada setiap masalah.", "",
         "> Peraturan: supplemen ialah pelengkap, bukan pengganti makanan atau ubat. Tiada dakwaan mencegah / merawat. "
         "Cadangan produk dan harga hanya di ruang tertutup (peraturan Amway Malaysia). Nama produk yang belum disahkan di amway.my ditanda PERLU SEMAK.", "",
         "## Cara betul ambil supplemen (siri konten umum)", ""]
    L += [f"- **{t}:** {d}" for t, d in CARA_BETUL]
    L += ["", "## Ringkasan", "", "| # | Masalah | Kategori | Kesanggupan bayar | Hari kalendar berkaitan |", "|---|---|---|---|---|"]
    for m in MASALAH:
        L += [f"| {m['n']} | {m['tajuk']} | {m['kat']} | {m['bayar']} | {', '.join(map(str, m['hari'])) or '-'} |"]
    L += [""]
    for m in MASALAH:
        L += [f"## {m['n']}. {m['tajuk']}", "",
              f"- **Apa mereka rasa:** {m['rasa']}",
              f"- **Apa yang dah dicuba:** {m['cuba']}",
              f"- **Kenapa masih gagal:** {m['gagal']}",
              f"- **Kesanggupan bayar:** {m['bayar']}",
              f"- **Fakta untuk konten:** {m['fakta']}",
              f"- **Cara betul (supplemen / gaya hidup):** {m['supp']}",
              f"- **Cadangan Nutrilite / Amway (ruang tertutup sahaja):** {m['nutrilite']}"]
        if m["sumber"]:
            L += ["- **Sumber:** " + "; ".join(SUMBER[x] for x in m["sumber"])]
        L += [""]
    return "\n".join(L)


TIPS_BULLET = re.compile(r"^\s*(✅|✓|•|🔹|[1-9]\ufe0f?\u20e3|Minggu \d+:)\s*")


def carousel_tips(teks):
    """Jana carousel tips daripada teks 18:30: tajuk -> 1 tips 1 slaid -> penutup."""
    baris = [x.strip() for x in teks.split("\n") if x.strip()]
    tajuk = baris[0].replace("💡", "").strip()
    tips, penutup = [], []
    for x in baris[1:]:
        if TIPS_BULLET.match(x):
            tips.append(TIPS_BULLET.sub(lambda m: (m.group(1) + " ") if m.group(1).startswith("Minggu") else "", x).strip())
        elif tips:
            penutup.append(x)
    kepala = re.sub(r"^tips\s+", "", tajuk, flags=re.I)
    slaid = [f"💡 TIPS\n{kepala.upper()}\n(Save untuk rujukan)"]
    slaid += [f"TIPS {i}\n{t}" for i, t in enumerate(tips[:6], 1)]
    slaid.append(("\n".join(penutup) + "\n\n" if penutup else "") + "Save & kongsi 💛\nFollow Momyizz untuk tips setiap hari")
    return {"tajuk": tajuk, "slaid": slaid, "caption": teks, "cukup": len(tips) >= 2}


def to_json():
    out = []
    for day in DAYS:
        d = {"d": day["d"], "ep": day["ep"], "tema": day["tema"]}
        k, masalah = day["produk"]
        nama, gambar, ks = PRODUK[k]
        d["produk"] = {"nama": nama, "gambar": gambar, "ks": ks, "masalah": masalah}
        if day["ep"] is None:
            d["siri"] = "Siri trending: Tidur, Otak & Usus"
        if day["d"] in MG_FULL:
            mg = [{"masa": m, "jenis": j, "tajuk": v["tajuk"], "sticker": v["sticker"],
                   "babak": [list(b) for b in v["babak"]], "caption": v["caption"]}
                  for (m, j), v in zip(MG_INFO, MG_FULL[day["d"]])]
        else:
            mg = [{"masa": m, "jenis": j, "idea": x} for (m, j), x in zip(MG_INFO, MG_PLAN[day["d"]])]
        if "video" in day:
            v = day["video"]
            d["video"] = {"tajuk": v["tajuk"], "nota": v.get("nota", ""), "babak": [list(b) for b in v["babak"]], "caption": v["caption"]}
            d["carousel"] = day["carousel"]
            teks = list(day["teks"])
            jenis_s = None
            if day["d"] >= 8 and day["tema"] in SOALAN_AWAM:
                jenis_s, baru = SOALAN_AWAM[day["tema"]]
                if baru:
                    teks[1] = baru
            d["teks"] = [{"masa": m, "jenis": j, "t": t} for (m, j), t in zip(JENIS_TEKS, teks)]
            if jenis_s:
                d["teks"][1]["soalan"] = jenis_s
            d["ctips"] = carousel_tips(teks[2])
            if day.get("wa"):
                d["wa"] = dict(day["wa"], skrip=skrip_untuk(day["wa"].get("tajuk", "") + " " + day["wa"].get("t", "")))
            d["mg"] = mg
        else:
            vid, car, teks, wa = day["plan"]
            assert len(teks) == len(JENIS_TEKS), f"Hari {day['d']}: perlu {len(JENIS_TEKS)} idea teks"
            d["plan"] = {"mg": mg, "video": vid, "carousel": car, "teks": [{"masa": m, "jenis": j, "idea": t} for (m, j), t in zip(JENIS_TEKS, teks)], "wa": wa,
                         "wa_skrip": skrip_untuk(wa)}
            d["plan"]["teks"][1]["soalan"] = GILIR_AWAM[day["d"] % len(GILIR_AWAM)]
        out.append(d)
    return out


def video_text(v, onscreen=False):
    if onscreen:
        return "\n".join(b[2] for b in v["babak"])
    return "\n".join(f"{b[0]} | VISUAL: {b[1]} | TEKS/SUARA: {b[2]}" for b in v["babak"])


def carousel_text(c):
    return "\n\n".join(f"SLAID {i}\n{t}" for i, t in enumerate(c["slaid"], 1))


def judul(day):
    label = ("Episod " + str(day["ep"])) if day["ep"] else "🔥 " + day.get("siri", "Siri trending")
    return f"## Hari {day['d']} · {label} · {day['tema']}"


def mg_md(g):
    if "idea" in g:
        return [f"### 🎞️ {g['masa']} · VIDEO MOTION GRAFIK ({g['jenis']}): idea", "",
                f"> {g['idea']} (skrip dijana dengan Claude: tab **Tulis** → **Salin arahan untuk Claude**)", ""]
    L = [f"### 🎞️ {g['masa']} · UNTUK VIDEO MOTION GRAFIK ({g['jenis']}): {g['tajuk']}", "",
         "> Bina dalam CapCut guna komponen `TEMPLATES/MOTION_GRAPHICS_KIT/KOMPONEN.md`. Tiada rakaman. "
         f"Sticker: {g['sticker']}.", "",
         "| Masa | Komponen kit | Teks atas skrin | Animasi |", "|---|---|---|---|"]
    L += [f"| {b[0]} | {b[1]} | {b[2].replace(chr(10), '<br>')} | {b[3]} |" for b in g["babak"]]
    return L + ["", "**Caption**", "", "```", g["caption"], "```", ""]


def produk_md(day):
    pr = day["produk"]
    return [f"> 🧩 **Produk penyelesai masalah:** {pr['nama']} · **Masalah:** {pr['masalah']}",
            f"> **Key selling:** {pr['ks']} · **Gambar:** `{pr['gambar']}`", ""]


def md_week1(days, minggu=1):
    d0, d1 = (minggu - 1) * 7 + 1, minggu * 7
    days = [d for d in days if d0 <= d["d"] <= d1]
    L = [f"# Kalendar Konten — Minggu {minggu}: Hari {d0}–{d1} (siap salin)", "",
         "Setiap hari satu topik: **🎥 1 video storytelling · 🎞️ 2 video motion grafik · 🖼️ 1 carousel · ✍️ 4 teks** (+ 💬 WhatsApp bila sesuai). Isi setiap konten berbeza.",
         "Dalam worksheet: tab **Tulis** untuk butang salin dan checklist.",
         "Sumber: `kalendar_data.py` (jangan edit fail ini terus; jalankan `python3 KALENDAR_PENULISAN/bina.py`).", ""]
    for day in days:
        if "video" not in day:
            continue
        v, c = day["video"], day["carousel"]
        L += [judul(day), ""] + produk_md(day) + [
              f"### 🎥 08:30 · UNTUK VIDEO STORYTELLING (TikTok / Reels, Flow AI): {v['tajuk']}", "",
              "> Salin skrip ini ke CapCut / Flow untuk edit video.", ""]
        if v["nota"]:
            L += [f"> {v['nota']}", ""]
        L += ["| Masa | Visual | Teks atas skrin / suara |", "|---|---|---|"]
        L += [f"| {b[0]} | {b[1]} | {b[2]} |" for b in v["babak"]]
        L += ["", "**Caption video**", "", "```", v["caption"], "```", ""]
        for g in day["mg"]:
            L += mg_md(g)
        L += [
              f"### 🖼️ 12:30 · UNTUK CAROUSEL (Instagram / Facebook): {c['tajuk']}", "",
              "> Salin teks setiap slaid ke Canva / CapCut untuk edit carousel.", ""]
        for i, t in enumerate(c["slaid"], 1):
            L += [f"**Slaid {i}**", "", "```", t, "```", ""]
        L += ["**Caption carousel**", "", "```", c["caption"], "```", "",
              "### ✍️ TEKS SAHAJA (Threads / Facebook) — salin & post terus", ""]
        for t in day["teks"]:
            L += [f"**{t['masa']} · {t['jenis']}** ({len(t['t'])} / 500 aksara)", "", "```", t["t"], "```", ""]
        if day.get("ctips"):
            ct = day["ctips"]
            L += [f"### 🖼️ 18:30 · UNTUK CAROUSEL TIPS (Instagram / Facebook): {ct['tajuk']}", "",
                  "> Tips yang sama dalam bentuk gambar: satu tips satu slaid, letak gambar / ikon sebenar untuk setiap tips. Caption = teks tips 18:30 di atas.", ""]
            for i, t in enumerate(ct["slaid"], 1):
                L += [f"**Slaid {i}**", "", "```", t, "```", ""]
        if day.get("wa"):
            w = day["wa"]
            L += [f"### 💬 WhatsApp / group tertutup: {w['tajuk']}", "", f"> {w['nota']}", "", "```", w["t"], "```", ""]
        L += ["**Checklist hari ini**", "",
              "- [ ] 🎥 Video storytelling: TikTok · Reels"] + [f"- [ ] 🎞️ Motion grafik {g['jenis']}: TikTok · Reels" for g in day["mg"]] + (["- [ ] 🖼️ Carousel tips 18:30: Instagram · Facebook"] if day.get("ctips") else []) + [
              "- [ ] 🖼️ Carousel: Instagram · Facebook"]
        L += [f"- [ ] ✍️ {t['masa']} {t['jenis']}: Threads · Facebook" for t in day["teks"]]
        if day.get("wa"):
            L += ["- [ ] 💬 WhatsApp / group tertutup"]
        L += [""]
    return "\n".join(L)


def plan_range(days):
    ds = [d["d"] for d in days if "plan" in d]
    return (min(ds), max(ds)) if ds else None


def md_plan(days):
    a, b = plan_range(days)
    L = [f"# Kalendar Konten — Hari {a} hingga {b} (rancangan)", "",
         "Format sama seperti fail MINGGU_*: 🎥 video storytelling · 🎞️ 2 motion grafik · 🖼️ carousel · ✍️ 4 teks (+ 💬 WhatsApp).",
         "Teks penuh dijana dengan Claude: tab **Tulis** → pilih hari → **Salin arahan untuk Claude** → tampal dalam Claude Project.", ""]
    for day in days:
        if "plan" not in day:
            continue
        p = day["plan"]
        L += [judul(day), ""] + produk_md(day) + [
              f"- 🎥 **Video storytelling (08:30, Flow AI):** {p['video']}"]
        L += [f"- 🎞️ **Motion grafik {g['masa']} · {g['jenis']}:** {g['idea']}" for g in p["mg"]]
        L += [
              f"- 🖼️ **Carousel (12:30):** {p['carousel']}"]
        L += [f"- ✍️ **Teks {t['masa']} · {t['jenis']}:** {t['idea']}" for t in p["teks"]]
        if p["wa"]:
            L += [f"- 💬 **WhatsApp tertutup:** {p['wa']}"]
        L += [""]
    return "\n".join(L)


def weeks_full(days):
    return sorted({(d["d"] - 1) // 7 + 1 for d in days if "video" in d})


def md_index(days):
    L = ["# Kalendar Konten Momyizz (30 hari)", "",
         "**Fokus bulan ini: BodyKey Nutritious Meal Shake formula baharu (perisa pisang).** "
         "🔥 Siri trending Tidur, Otak & Usus diselang sehari atau dua hari (Hari 8, 10, 13, 15, 18, 20, 22, 24, 27, 29); semakan dakwaan podcast dalam `PODCAST_SEMAKAN.md`.", "",
         "| Fail | Isi |", "|---|---|",
         *[f"| `MINGGU_{w}.md` | Hari {(w-1)*7+1}–{w*7}: skrip video, teks carousel, 4 teks, WhatsApp + checklist |" for w in weeks_full(days)],
         *([f"| `HARI_{plan_range(days)[0]:02d}-{plan_range(days)[1]:02d}.md` | Hari {plan_range(days)[0]}–{plan_range(days)[1]}: rancangan setiap konten |"] if plan_range(days) else []),
         "| `PODCAST_SEMAKAN.md` | Semakan dakwaan podcast tidur & otak (sumber siri trending) |",
         "| `MASALAH_AUDIENS.md` | 20 masalah audiens: rasa, dah cuba, kenapa gagal, cara betul supplemen, cadangan Nutrilite |",
         "| `masalah_data.py` | Sumber data 20 masalah |",
         "| `kalendar_data.py` | Sumber data kalendar (edit di sini) |",
         "| `bina.py` | Semak had aksara dan gaya, jana Markdown, kemas kini worksheet |", "",
         "## Agihan sehari (satu topik, isi berbeza)", "",
         "| Masa | Konten | Untuk | Salin ke |", "|---|---|---|---|",
         "| 08:30 | 🎥 Video storytelling | TikTok · Reels | Flow (video AI) + CapCut |",
         "| 13:30 | 🎞️ Video motion grafik: tips | TikTok · Reels | CapCut + Motion Graphics Kit |",
         "| 19:30 | 🎞️ Video motion grafik: masalah → penyelesaian | TikTok · Reels | CapCut + Motion Graphics Kit |",
         "| 12:30 | 🖼️ Carousel | Instagram · Facebook | Canva / CapCut (edit carousel) |",
         "| 10:00 | ✍️ Teks: info ringkas | Threads · Facebook | Post terus |",
         "| 16:00 | ✍️ Teks: pertanyaan | Threads · Facebook | Post terus |",
         "| 18:30 | ✍️ Teks: tips praktikal | Threads · Facebook | Post terus |",
         "| 21:00 | ✍️ Teks: info penting / alert | Threads · Facebook | Post terus |",
         "| Bila sesuai | 💬 Hard-sell | WhatsApp / group tertutup | Hantar terus |", "",
         "Produk boleh kelihatan dalam video / gambar, tetapi nama produk tidak disebut dalam sari kata, voiceover, caption atau teks awam (`AMWAY_BRAND/BRAND.md`).", "",
         "Setiap hari ada **satu produk penyelesai masalah** (key selling: `AMWAY_BRAND/KEY_SELLING.md`).", "",
         "| Hari | Episod | Tema | Produk | WhatsApp | Status |", "|---|---|---|---|---|---|"]
    for day in days:
        wa = "✓" if (day.get("wa") or (day.get("plan") or {}).get("wa")) else ""
        L += [f"| {day['d']} | {day['ep'] or '🔥'} | {day['tema']} | {day['produk']['nama']} | {wa} | {'Siap salin' if 'video' in day else 'Rancangan'} |"]
    return "\n".join(L) + "\n"


def inject(data):
    blocks = {
        "WRITE_PLAN": "const WRITE_PLAN=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";",
        "MASALAH": "const MASALAH=" + json.dumps(masalah_json(), ensure_ascii=False, separators=(",", ":")) + ";",
        "SOALAN": "const SOALAN=" + json.dumps(soalan_json(), ensure_ascii=False, separators=(",", ":")) + ";",
    }
    for name in ("momyizz-planner.html", "index.html"):
        p = os.path.join(ROOT, name)
        s = open(p, encoding="utf-8").read()
        for key, js in blocks.items():
            a, b = f"/*{key}_START*/", f"/*{key}_END*/"
            if a not in s:
                raise SystemExit(f"Penanda {a} tiada dalam {name}")
            i, j = s.index(a) + len(a), s.index(b)
            s = s[:i] + js + s[j:]
        open(p, "w", encoding="utf-8").write(s)


if __name__ == "__main__":
    errs = check()
    if errs:
        print("RALAT:\n  " + "\n  ".join(errs))
        sys.exit(1)
    data = to_json()
    import glob
    for old in glob.glob(os.path.join(HERE, "MINGGU_*.md")) + glob.glob(os.path.join(HERE, "HARI_*.md")):
        os.remove(old)
    for w in weeks_full(data):
        open(os.path.join(HERE, f"MINGGU_{w}.md"), "w", encoding="utf-8").write(md_week1(data, w))
    pr = plan_range(data)
    if pr:
        open(os.path.join(HERE, f"HARI_{pr[0]:02d}-{pr[1]:02d}.md"), "w", encoding="utf-8").write(md_plan(data))
    open(os.path.join(HERE, "README.md"), "w", encoding="utf-8").write(md_index(data))
    open(os.path.join(HERE, "MASALAH_AUDIENS.md"), "w", encoding="utf-8").write(md_masalah())
    open(os.path.join(HERE, "SKRIP_PROSPEK.md"), "w", encoding="utf-8").write(md_skrip())
    inject(data)
    n = sum(1 for d in data if "video" in d)
    print(f"OK: {len(data)} hari, {n} hari siap salin. Markdown dan worksheet dikemas kini.")
