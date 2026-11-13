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
from kalendar_data import DAYS, SLOT_INFO  # noqa: E402

LIMIT_TH, LIMIT_IG = 500, 2200
BANNED = re.compile(r"(?<![A-Za-z])(aku|kau|saya|awak|anda)(?![A-Za-z])", re.I)


def check():
    errs = []
    for day in DAYS:
        for s in day.get("slots", []):
            tag = f"Hari {day['d']} {s['k']}"
            for i, t in enumerate(s.get("th", []), 1):
                if len(t) > LIMIT_TH:
                    errs.append(f"{tag}: Threads {i} = {len(t)} aksara (> {LIMIT_TH})")
            if len(s.get("ig", "")) > LIMIT_IG:
                errs.append(f"{tag}: Instagram {len(s['ig'])} aksara (> {LIMIT_IG})")
            for f in ("fb", "ig", "wa"):
                m = BANNED.search(s.get(f, ""))
                if m:
                    errs.append(f"{tag}: {f} guna '{m.group(0)}' (guna Momyizz / korang)")
            for t in s.get("th", []):
                m = BANNED.search(t)
                if m:
                    errs.append(f"{tag}: Threads guna '{m.group(0)}'")
    return errs


def to_json():
    out = []
    for day in DAYS:
        d = {"d": day["d"], "ep": day["ep"], "tema": day["tema"]}
        if "slots" in day:
            d["slots"] = day["slots"]
        else:
            d["plan"] = [{"k": k, "idea": idea, "hook": hook} for k, idea, hook in day["plan"]]
        out.append(d)
    return out


def md_week1(days):
    L = ["# Kalendar Penulisan — Minggu 1 (teks penuh)", "",
         "Teks siap salin untuk Facebook, Instagram dan Threads. Dalam worksheet, buka tab **Tulis** untuk butang salin dan checklist.",
         "Sumber: `kalendar_data.py` (jangan edit fail ini terus; jalankan `python3 KALENDAR_PENULISAN/bina.py`).", ""]
    for day in days:
        if "slots" not in day:
            continue
        L += [f"## Hari {day['d']} · Episod {day['ep']} · {day['tema']}", ""]
        for s in day["slots"]:
            masa, jenis = SLOT_INFO[s["k"]]
            L += [f"### {masa} · {jenis}: {s['tajuk']}", ""]
            if s.get("nota"):
                L += [f"> {s['nota']}", ""]
            if "wa" in s:
                L += ["**WhatsApp / group tertutup**", "", "```", s["wa"], "```", ""]
                continue
            L += [f"**Facebook** ({len(s['fb'])} aksara)", "", "```", s["fb"], "```", "",
                  f"**Instagram** ({len(s['ig'])} / 2200 aksara)", "", "```", s["ig"], "```", "",
                  "**Threads**", ""]
            for i, t in enumerate(s["th"], 1):
                L += [f"{i}/{len(s['th'])} ({len(t)} / 500 aksara)", "", "```", t, "```", ""]
        L += ["**Checklist hari ini**", ""]
        for s in day["slots"]:
            masa, jenis = SLOT_INFO[s["k"]]
            plats = ["WhatsApp / group tertutup"] if "wa" in s else ["Facebook", "Instagram", "Threads"]
            L += [f"- [ ] {masa} {jenis}: " + " · ".join(f"[ ] {p}" for p in plats)]
        L += [""]
    return "\n".join(L)


def md_plan(days):
    L = ["# Kalendar Penulisan — Hari 8 hingga 30 (rancangan)", "",
         "Idea dan hook untuk setiap slot. Teks penuh dijana dengan Claude:",
         "dalam worksheet, tab **Tulis** → pilih hari → **Salin arahan untuk Claude**, kemudian tampal dalam Claude Project.", ""]
    for day in days:
        if "plan" not in day:
            continue
        L += [f"## Hari {day['d']} · Episod {day['ep']} · {day['tema']}", "", "| Slot | Idea | Hook |", "|---|---|---|"]
        for p in day["plan"]:
            masa, jenis = SLOT_INFO[p["k"]]
            L += [f"| {masa} {jenis} | {p['idea']} | {p['hook']} |"]
        L += [""]
    return "\n".join(L)


def md_index(days):
    L = ["# Kalendar Penulisan Momyizz (30 hari)", "",
         "| Fail | Isi |", "|---|---|",
         "| `MINGGU_1.md` | Hari 1–7: teks penuh Facebook, Instagram, Threads, WhatsApp + checklist |",
         "| `HARI_08-30.md` | Hari 8–30: idea dan hook setiap slot |",
         "| `kalendar_data.py` | Sumber data (edit di sini) |",
         "| `bina.py` | Semak had aksara, jana Markdown, kemas kini worksheet |", "",
         "Slot harian: **08:30** personal branding · **12:30** edukasi / soft-sell · **20:30** interaksi · "
         "**hard-sell** di ruang tertutup sahaja (WhatsApp / group tertutup), ikut peraturan Amway Malaysia dalam `AMWAY_BRAND/BRAND.md`.", "",
         "| Hari | Episod | Tema | Hard-sell (tertutup) | Teks |", "|---|---|---|---|---|"]
    for day in days:
        items = day.get("slots") or day.get("plan")
        hs = "✓" if any(x["k"] == "tutup" for x in items) else ""
        L += [f"| {day['d']} | {day['ep']} | {day['tema']} | {hs} | {'Penuh' if 'slots' in day else 'Rancangan'} |"]
    return "\n".join(L) + "\n"


def inject(data):
    js = "const WRITE_PLAN=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";"
    for name in ("momyizz-planner.html", "index.html"):
        p = os.path.join(ROOT, name)
        s = open(p, encoding="utf-8").read()
        a, b = "/*WRITE_PLAN_START*/", "/*WRITE_PLAN_END*/"
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
    open(os.path.join(HERE, "MINGGU_1.md"), "w", encoding="utf-8").write(md_week1(data))
    open(os.path.join(HERE, "HARI_08-30.md"), "w", encoding="utf-8").write(md_plan(data))
    open(os.path.join(HERE, "README.md"), "w", encoding="utf-8").write(md_index(data))
    inject(data)
    n = sum(len(d.get("slots", [])) for d in data)
    print(f"OK: {len(data)} hari, {n} slot teks penuh. Markdown dan worksheet dikemas kini.")
