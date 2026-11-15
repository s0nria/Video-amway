"""Episod 2: Sarapan Ibu Yang Selalu Tertinggal — hook cover + sari kata.
Gaya ikut AMWAY_BRAND/BRAND.md & TEMPLATES/MOTION_GRAPHICS_KIT/KOMPONEN.md."""
import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = os.path.dirname(os.path.abspath(__file__))
UP = "/root/.claude/uploads/9184b19e-ba3a-5b15-aac5-53ecc321e714/"
STK = "/home/user/Video-amway/AMWAY_BRAND/STICKERS/"
OUT = sys.argv[1] if len(sys.argv) > 1 else S + "/out"
os.makedirs(OUT, exist_ok=True)
W, H, FPS = 1080, 1920, 30

# Susunan ikut storyboard: pagi -> pejabat -> pinggan -> idea sarapan -> produk -> penutup
CLIPS = ["ce86719c-670571347_1794749147202571.mp4", "8310fd8d-803477808_1794749217277974.mp4",
         "02f856dc-203194378_1794749212038589.mp4", "d13d12d0-354649346_1794749222703151.mp4",
         "97dd8780-692952755_1794751917365762.mp4", "fafd5c2b-558080079_1794752351341120.mp4"]
DUR = [7.93, 7.93, 10.0, 7.93, 7.93, 7.93]
TOTAL = sum(DUR)  # 49.65

KRIM, KERTAS, DAKWAT = "#F2EEE5", "#FBF9F4", "#35362F"
SAGE, SAGE_G, KAYU = "#7F9373", "#556A4C", "#A3876A"
TERBUKTI = "#4E7347"

def font(name, size, var):
    f = ImageFont.truetype(f"{S}/fonts/{name}.ttf", size)
    f.set_variation_by_name(var)
    return f

def tw(d, txt, f):
    b = d.textbbox((0, 0), txt, font=f)
    return b[2] - b[0]

def wrap(txt, f, maxw):
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    lines, cur = [], ""
    for w in txt.split():
        t = (cur + " " + w).strip()
        if tw(d, t, f) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    return lines

def shadow_box(size, radius, fill, border=None, bw=0, alpha=255, shadow=True):
    w, h = size
    pad = 40 if shadow else 0
    im = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    if shadow:
        sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle((pad, pad + 12, pad + w, pad + h + 12), radius, fill=(53, 54, 47, 40))
        im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(16)))
    box = Image.new("RGBA", im.size, (0, 0, 0, 0))
    col = Image.new("RGBA", (1, 1), fill).getpixel((0, 0))[:3] + (alpha,)
    ImageDraw.Draw(box).rounded_rectangle((pad, pad, pad + w, pad + h), radius, fill=col,
                                          outline=border, width=bw)
    return Image.alpha_composite(im, box), pad

# ---------- komponen (setiap satu pulangkan (RGBA, x, y) penuh-kanvas) ----------
def sari_kata(txt, ybot=1400):
    f = font("Nunito", 56, "ExtraBold")
    lines = [l for part in txt.split("\n") for l in wrap(part, f, 800)]
    assert len(lines) <= 2, txt
    lh = 72
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    bw = max(tw(d, l, f) for l in lines) + 64
    bh = lh * len(lines) + 36
    im, pad = shadow_box((bw, bh), 24, KERTAS)
    dr = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        dr.text((pad + bw / 2, pad + 18 + lh * i + lh / 2), l, font=f, fill=DAKWAT, anchor="mm")
    cx = 500  # tengah kawasan selamat x 60–940
    return im, int(cx - im.width / 2), int(ybot - bh - pad)

def penafian(y=1150, kiri=False):
    f = font("Nunito", 32, "ExtraBold")
    lines = ["Perkongsian ilmu umum.", "Bukan nasihat perubatan."] if kiri else \
            ["Perkongsian ilmu umum. Bukan nasihat perubatan."]
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    bw, bh = max(tw(d, l, f) for l in lines) + 40, 44 * len(lines) + 10
    im, pad = shadow_box((bw, bh), 16, KERTAS, alpha=217, shadow=False)
    for i, l in enumerate(lines):
        ImageDraw.Draw(im).text((bw / 2, 5 + 44 * i + 22), l, font=f, fill=DAKWAT, anchor="mm")
    return im, (60 if kiri else int(500 - bw / 2)), y

def label_bukti(label, color, sumber, y=300):
    fl = font("Fredoka", 32, "SemiBold")
    fs = font("Nunito", 30, "ExtraBold")
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    lw = tw(d, label, fl) + 48
    sw = tw(d, sumber, fs) + 44
    h = 64
    im = Image.new("RGBA", (lw + sw + 12, h), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, lw, h), h // 2, fill=color)
    dr.text((lw / 2, h / 2), label, font=fl, fill=KERTAS, anchor="mm")
    col = Image.new("RGBA", (1, 1), KERTAS).getpixel((0, 0))[:3] + (230,)
    dr.rounded_rectangle((lw + 12, 0, lw + 12 + sw, h), h // 2, fill=col)
    dr.text((lw + 12 + sw / 2, h / 2), sumber, font=fs, fill=SAGE_G, anchor="mm")
    return im, 60, y

def big_word(txt, color=SAGE_G, y=1180, size=100):
    f = font("Fredoka", size, "Bold")
    lines = [l for part in txt.split("\n") for l in wrap(part, f, 800)]
    lh = int(size * 1.12)
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    bw = max(tw(d, l, f) for l in lines) + 80
    bh = lh * len(lines) + 50
    im, pad = shadow_box((bw, bh), 36, KERTAS)
    dr = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        dr.text((pad + bw / 2, pad + 25 + lh * i + lh / 2), l, font=f, fill=color, anchor="mm")
    return im, int(500 - im.width / 2), y - pad

def hook_card():
    # di atas muka ibu (bawah jam "7:15 AM" dalam klip)
    f = font("Fredoka", 76, "Bold")
    l1, l2 = "Anak dah makan,", "suami dah makan…"
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    bw = max(tw(d, l1, f), tw(d, l2, f)) + 80
    bh = 2 * 90 + 40
    im, pad = shadow_box((bw, bh), 36, KERTAS)
    dr = ImageDraw.Draw(im)
    dr.text((pad + bw / 2, pad + 20 + 45), l1, font=f, fill=DAKWAT, anchor="mm")
    dr.text((pad + bw / 2, pad + 20 + 90 + 45), l2, font=f, fill=DAKWAT, anchor="mm")
    return im, int(500 - im.width / 2), 248 - pad

def hook_ibu():
    f = font("Fredoka", 160, "Bold")
    t = "IBU?"
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    w = tw(d, t, f)
    im = Image.new("RGBA", (w + 80, 220), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    dr.text((im.width / 2, 110), t, font=f, fill=KAYU, anchor="mm", stroke_width=10, stroke_fill=KERTAS)
    return im, int(250 - im.width / 2), 790   # bawah muka ibu, kiri

def hook_nanti():
    f = font("Caveat", 96, "Bold")
    t = "“Nanti la…”"
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    w = tw(d, t, f)
    im = Image.new("RGBA", (w + 60, 150), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((im.width / 2, 75), t, font=f, fill=SAGE_G, anchor="mm", stroke_width=8, stroke_fill=KERTAS)
    return im, int(645 - im.width / 2), 835   # sebaris dengan IBU?, kanan

def label_pilar():
    fl = font("Fredoka", 28, "SemiBold")
    t = "Health & Wellness · Episod 2"
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    w = tw(d, t, fl) + 44
    im = Image.new("RGBA", (w, 52), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w, 52), 26, fill="#5C7A58")
    dr.text((w / 2, 26), t, font=fl, fill=KERTAS, anchor="mm")
    return im, 60, 214

def cta():
    f1 = font("Nunito", 48, "ExtraBold")
    f2 = font("Fredoka", 72, "Bold")
    # kotak di bawah (y 1230–1440, tak tutup muka); sticker di kanan bawah tunjuk ke kotak
    f2 = font("Fredoka", 64, "Bold")
    bw, bh = 640, 210
    im, pad = shadow_box((bw, bh), 36, KERTAS, border=SAGE_G, bw=6)
    dr = ImageDraw.Draw(im)
    dr.text((pad + bw / 2, pad + 64), "Nak dapatkan produk?", font=f1, fill=DAKWAT, anchor="mm")
    dr.text((pad + bw / 2, pad + 144), "Klik LINK di Bio", font=f2, fill=SAGE_G, anchor="mm")
    return im, 60 - pad, 1438 - 210 - pad

def sticker(fname, width, x, ybot):
    im = Image.open(STK + fname).convert("RGBA")
    im = im.crop(im.split()[3].getbbox())
    h = int(im.height * width / im.width)
    im = im.resize((width, h), Image.LANCZOS)
    return im, x, ybot - h

# ---------- garis masa ----------
T = []  # (mula, tamat, komponen)
SAFE = (60, 160, 940, 1440)  # x0, y0, x1, y1 — kawasan selamat TikTok/Reels

def vis_box(comp):
    """Kotak nampak sebenar (abaikan bayang lembut, alfa <= 60)."""
    im, x, y = comp
    b = im.split()[3].point(lambda v: 255 if v > 60 else 0).getbbox()
    return (x + b[0], y + b[1], x + b[2], y + b[3])

def add(a, b, comp, boleh_keluar=False):
    """boleh_keluar=True: hanya untuk sticker penutup (dibenarkan pengguna keluar frame bawah)."""
    bx = vis_box(comp)
    if boleh_keluar:
        T.append((a, b, comp)); return
    assert SAFE[0] <= bx[0] and SAFE[1] <= bx[1] and bx[2] <= SAFE[2] and bx[3] <= SAFE[3], \
        f"KELUAR SAFE ZONE {a:.2f}-{b:.2f}: {bx}"
    T.append((a, b, comp))

def watermark():
    f = font("Nunito", 30, "ExtraBold")
    t = "@empayarbiz_momyizz"
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    bw, bh = tw(d, t, f) + 32, 48
    im, pad = shadow_box((bw, bh), 24, KERTAS, alpha=225, shadow=False)
    ImageDraw.Draw(im).text((bw / 2, bh / 2 - 2), t, font=f, fill=SAGE_G, anchor="mm")
    return im, 940 - bw, 172   # atas kanan, betul-betul bawah garis safe zone atas

# Babak produk sebenar (ganti tin AI dalam klip 5, 1.958–4.875 s)
PROD_A, PROD_B = None, None
PROD_IMG = Image.open("/home/user/Video-amway/AMWAY_BRAND/PRODUK/nutrilite-soy-protein-drink.jpg").convert("RGB")
def product_scene(t):
    k = (t - PROD_A) / (PROD_B - PROD_A)
    bg = PROD_IMG.resize((int(PROD_IMG.width * H / PROD_IMG.height), H), Image.BILINEAR)
    bg = bg.crop(((bg.width - W) // 2, 0, (bg.width - W) // 2 + W, H)).filter(ImageFilter.GaussianBlur(28))
    bg = Image.blend(bg, Image.new("RGB", (W, H), KRIM), 0.35).convert("RGBA")
    crop = PROD_IMG.crop((330, 150, 1150, 918))           # tin + gelas + kacang soya
    z = 1.0 + 0.06 * k                                       # zoom perlahan
    cw, ch = int(crop.width / z), int(crop.height / z)
    crop = crop.crop(((crop.width - cw) // 2, (crop.height - ch) // 2, (crop.width + cw) // 2, (crop.height + ch) // 2))
    cardw = 880; cardh = int(cardw * 768 / 820)
    crop = crop.resize((cardw, cardh), Image.LANCZOS)
    card, pad = shadow_box((cardw, cardh), 36, KERTAS)
    m = Image.new("L", (cardw, cardh), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, cardw, cardh), 36, fill=255)
    card.paste(crop, (pad, pad), m)
    bg.alpha_composite(card, (60 - pad, 350 - pad))
    return bg

# HOOK 3 s (cover)
add(0.00, TOTAL, watermark())
# COVER 1 s: hook penuh muncul terus dari bingkai pertama (jadi thumbnail), hilang pada 1.0 s.
# Sticker tutup mulut hanya pada cover; tiada sticker bila video berjalan.
add(0.00, 1.00, hook_card())
add(0.00, 1.00, hook_ibu())
add(0.00, 1.00, hook_nanti())
add(0.00, 1.00, sticker("14-blazer-tutup-mulut.png", 300, 940 - 300, 1440))
add(1.00, 2.00, sari_kata("Ibu? “Nanti la…”", ybot=1438))
add(2.00, 3.00, sari_kata("Siapa macam ni?", ybot=1438))

c = [0]
for d in DUR: c.append(c[-1] + d)
PROD_A, PROD_B = c[4] + 1.958, c[4] + 4.875
SUB = [
    # klip 1 — pagi (0–7.93)
    (3.00, 5.40, "7.15 pagi. Kak Ana siapkan anak dulu."),
    (5.40, c[1], "Untuk diri sendiri? Secawan kopi je."),
    # klip 2 — pejabat (7.93–15.86)
    (c[1], 10.60, "11 pagi, dalam mesyuarat… perut berbunyi."),
    (10.60, 13.20, "Kepala rasa berat. Capai biskut dalam laci."),
    (13.20, c[2], "Petang balik, lapar sangat. Makan banyak sekali gus."),
    # klip 3 — pinggan (15.86–25.86)
    (c[2], 18.20, "Bukan sebab tak tahu jaga makan."),
    (18.20, 20.30, "Tapi ibu selalu letak diri paling akhir."),
    (20.30, 22.30, "Pinggan Sihat KKM:\n½ sayur & buah"),
    (22.30, 24.10, "¼ bijirin penuh, ¼ protein"),
    (24.10, c[3], "Hadkan gula tambahan, termasuk minuman."),
    # klip 4 — idea sarapan 5 minit (25.86–33.79)
    (c[3], 28.20, "Idea 1: telur rebus, roti gandum, pisang"),
    (28.20, 30.40, "Idea 2: oat rendam semalaman + buah"),
    (30.40, 32.20, "Siapkan bekal ibu sekali dengan bekal anak"),
    (32.20, c[4], "Air kosong dulu, baru kopi."),
    # klip 5 — produk (33.79–41.72)
    (c[4], 36.40, "Protein + karbo kompleks + serat, kenyang lebih lama."),
    (36.40, 37.90, "Hari terlalu kelam-kabut?"),
    (37.90, 39.80, "Nutrilite Soy Protein Drink boleh jadi pilihan tambahan."),
    (39.80, c[5], "Tapi BUKAN pengganti sarapan sebenar."),
    # klip 6 — penutup (41.72–49.65)
    (c[5], 44.20, "Ibu pun manusia. Duduk 5 minit, makan dengan tenang."),
]
for a, b, t in SUB:
    # babak penutup: penafian duduk di bawah, jadi sari kata naik supaya tak bertindih
    # penutup: sari kata di paling bawah supaya tak tutup muka ibu/anak
    add(a, b, sari_kata(t, ybot=1438 if a >= c[5] else 1400))

add(20.30, c[3], label_bukti("Fakta terbukti", TERBUKTI, "Sumber: KKM MDG 2020"))
add(c[3] + 0.2, 30.40, label_bukti("Sarapan 5 Minit Ibu", SAGE_G, "Sedia malam sebelumnya", y=1130))
add(c[4], 36.40, label_bukti("Panduan", SAGE, "Panduan pemakanan umum"))
add(20.30, c[3], penafian())
add(44.20, 46.60, big_word("Perut ibu juga\nperlu diisi.", y=1228, size=72))
# penafian: dipapar di babak fakta (20.3–25.9 s, 5.6 s). Penutup dikosongkan supaya tak tutup muka.
add(46.60, TOTAL, cta())
add(46.80, TOTAL, sticker("15-blazer-tunjuk-atas-kiri.png", 360, 715, 1840), boleh_keluar=True)

def overlaps():
    bad = []
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            a1, b1, c1 = T[i]; a2, b2, c2 = T[j]
            if min(b1, b2) - max(a1, a2) <= 0.01: continue
            p, q = vis_box(c1), vis_box(c2)
            if p[0] < q[2] and q[0] < p[2] and p[1] < q[3] and q[1] < p[3]:
                bad.append((round(max(a1, a2), 2), p, q))
    # teks yang tertanam dalam klip AI (jam, "Breakfast Idea")
    for a1, b1, q in FACES:
        for a2, b2, c2 in T:
            if min(b1, b2) - max(a1, a2) <= 0.01: continue
            p = vis_box(c2)
            if p[0] < q[2] and q[0] < p[2] and p[1] < q[3] and q[1] < p[3]:
                bad.append(("MUKA", round(max(a1, a2), 2), p, q))
    for a1, b1, q in BAKED:
        for a2, b2, c2 in T:
            if min(b1, b2) - max(a1, a2) <= 0.01: continue
            p = vis_box(c2)
            if p[0] < q[2] and q[0] < p[2] and p[1] < q[3] and q[1] < p[3]:
                bad.append(("klip", round(max(a1, a2), 2), p, q))
    return bad
# Kotak muka subjek (ibu / anak) — tulisan & grafik tak boleh tutup
c6 = c[5]
FACES = [(0, 1.958, (370, 520, 670, 810)), (0, 1.958, (250, 1020, 420, 1290)),   # klip 1: ibu, anak
         (c6, c6 + 2.0, (500, 580, 670, 910)), (c6, c6 + 2.0, (250, 990, 460, 1255)),
         (c6 + 2.0, c6 + 4.0, (420, 370, 670, 780)), (c6 + 2.0, c6 + 4.0, (10, 835, 285, 1095)),
         (c6 + 4.0, c6 + 6.92, (250, 395, 815, 1180)),
         (c6 + 6.92, TOTAL, (420, 420, 685, 805)), (c6 + 6.92, TOTAL, (25, 850, 230, 1070))]
BAKED = [(0, c[1], (215, 155, 525, 235)), (c[1], c[2], (165, 155, 565, 235)),
         (c[3], c[3] + 2.0, (230, 265, 860, 365)), (c[3] + 1.9, c[3] + 4.0, (300, 320, 820, 430))]
for o in overlaps(): print("BERTINDIH:", o)

def ease(x): return 1 - (1 - x) ** 3

def frame_overlay(t):
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for a, b, (im, x, y) in T:
        if not (a <= t < b): continue
        k_in = 1 if a == 0 else min(1, (t - a) / 0.3)   # elemen saat 0 terus penuh (cover)
        k_out = min(1, (b - t) / 0.2) if b < TOTAL - 0.01 else 1
        alpha = ease(k_in) * k_out
        s = 0.9 + 0.1 * ease(k_in)
        if s < 0.999:
            nw, nh = max(1, int(im.width * s)), max(1, int(im.height * s))
            im2 = im.resize((nw, nh), Image.BILINEAR)
            x2, y2 = x + (im.width - nw) // 2, y + (im.height - nh) // 2
        else:
            im2, x2, y2 = im, x, y
        if alpha < 0.999:
            im2 = im2.copy(); im2.putalpha(im2.split()[3].point(lambda v: int(v * alpha)))
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        layer.paste(im2, (x2, y2), im2)
        canvas = Image.alpha_composite(canvas, layer)
    return canvas

def hook_vignette(t):
    """Gelapkan sedikit bahagian atas semasa hook supaya teks jelas."""
    if t >= 1.0: return None
    g = Image.new("L", (1, H))
    for yy in range(H):
        g.putpixel((0, yy), int(110 * max(0, 1 - yy / 1100)))
    g = g.resize((W, H))
    k = 1 if t < 0.8 else (1.0 - t) / 0.2
    blk = Image.new("RGBA", (W, H), (53, 54, 47, 0))
    blk.putalpha(g.point(lambda v: int(v * k)))
    return blk

if __name__ == "__main__":
    mode = sys.argv[2] if len(sys.argv) > 2 else "video"
    inputs = []
    for f in CLIPS: inputs += ["-i", UP + f]
    fc = "".join(f"[{i}:v]fps={FPS},scale={W}:{H},setsar=1[v{i}];[{i}:a]aresample=48000[a{i}];" for i in range(6))
    fc += "".join(f"[v{i}][a{i}]" for i in range(6)) + "concat=n=6:v=1:a=1[v][a]"
    base = S + "/base.mp4"
    if not os.path.exists(base):
        subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
                        "-c:v", "libx264", "-crf", "12", "-preset", "fast", "-c:a", "aac", "-b:a", "320k", base], check=True)
    if mode == "stills":
        for t in [float(x) for x in sys.argv[3].split(",")]:
            fr = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", base, "-frames:v", "1", "-f", "rawvideo",
                                 "-pix_fmt", "rgba", "-"], capture_output=True).stdout
            im = Image.frombytes("RGBA", (W, H), fr)
            if PROD_A <= t < PROD_B: im = product_scene(t)
            v = hook_vignette(t)
            if v: im = Image.alpha_composite(im, v)
            im = Image.alpha_composite(im, frame_overlay(t))
            im.convert("RGB").save(f"{OUT}/still_{t:05.2f}.png")
        sys.exit()
    if mode == "cover":
        fr = subprocess.run(["ffmpeg", "-v", "error", "-ss", "0.3", "-i", base, "-frames:v", "1", "-f", "rawvideo",
                             "-pix_fmt", "rgba", "-"], capture_output=True).stdout
        im = Image.alpha_composite(Image.frombytes("RGBA", (W, H), fr), hook_vignette(0.3))
        im = Image.alpha_composite(im, frame_overlay(0.3))
        im.convert("RGB").save(f"{OUT}/EP02_cover_hook.png"); sys.exit()
    LIMIT = float(sys.argv[3]) if mode == "clip" else TOTAL
    NAME = f"EP02_preview_0-{LIMIT:g}s.mp4" if mode == "clip" else "EP02_Sarapan_Ibu.mp4"
    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", base, "-f", "rawvideo", "-pix_fmt", "rgba", "-"], stdout=subprocess.PIPE)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS),
                            "-i", "-", "-i", base, "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "medium",
                            "-b:v", "14M", "-maxrate", "16M", "-bufsize", "28M", "-pix_fmt", "yuv420p",
                            "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-shortest", "-movflags", "+faststart",
                            f"{OUT}/{NAME}"], stdin=subprocess.PIPE)
    i = 0
    while True:
        fr = dec.stdout.read(W * H * 4)
        if len(fr) < W * H * 4 or i >= round(LIMIT * FPS): break
        t = i / FPS
        im = Image.frombytes("RGBA", (W, H), fr)
        if PROD_A <= t < PROD_B: im = product_scene(t)
        v = hook_vignette(t)
        if v: im = Image.alpha_composite(im, v)
        im = Image.alpha_composite(im, frame_overlay(t))
        enc.stdin.write(im.tobytes())
        if i == 0:  # cover / thumbnail = rupa penuh hook
            pass
        i += 1
    dec.kill(); enc.stdin.close(); enc.wait()
    # SRT untuk CapCut
    def ts(x):
        ms = int(round(x * 1000)); return f"{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}"
    srt = [(0.0, 1.0, "Anak dah makan, suami dah makan…"), (1.0, 2.0, "Ibu? “Nanti la…”"),
           (2.0, 3.0, "Siapa macam ni?")] + SUB + [(44.2, 46.6, "Perut ibu juga perlu diisi.")]
    with open(f"{OUT}/EP02_Sarapan_Ibu_sarikata.srt", "w") as fh:
        for n, (a, b, t) in enumerate(srt, 1):
            fh.write(f"{n}\n{ts(a)} --> {ts(b)}\n{t}\n\n")
    print("frames", i)
