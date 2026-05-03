#!/usr/bin/env python3
"""Generate ERV.hk product catalogs (GEC, GEC V, UTC) as branded PDFs.

Output: clients/erv-hk/catalogs/erv-gec-commercial-ceiling.pdf
        clients/erv-hk/catalogs/erv-gec-v-fresh-air-ceiling.pdf
        clients/erv-hk/catalogs/erv-utc-ultra-thin-ceiling.pdf

Style: light/white background, ERV blue brand mark, warm orange accent,
bilingual EN + Traditional Chinese, with embedded product photos.
"""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "catalogs"
IMG_DIR = ROOT / "images"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---- Light palette ----
BG        = white
PANEL     = HexColor("#f5f7fb")     # subtle off-white panel
PANEL_2   = HexColor("#eceff8")     # slightly warmer panel
INK       = HexColor("#0a0e1f")     # near-black
INK_SOFT  = HexColor("#3a4159")
MUTED     = HexColor("#5d6378")
SUBTLE    = HexColor("#8a8fa0")
LINE      = HexColor("#e4e6ee")
LINE_SOFT = HexColor("#eef0f5")
BLUE      = HexColor("#0023ff")     # ERV brand blue (logo)
BLUE_DARK = HexColor("#001bb8")
ACCENT    = HexColor("#ff8a14")     # warm accent for eyebrow tags
ACCENT_D  = HexColor("#d96900")

# CJK fonts
try:
    pdfmetrics.registerFont(TTFont("STHeiti", "/System/Library/Fonts/STHeiti Light.ttc", subfontIndex=0))
    pdfmetrics.registerFont(TTFont("STHeiti-Bold", "/System/Library/Fonts/STHeiti Light.ttc", subfontIndex=1))
    CJK = "STHeiti"
    CJK_B = "STHeiti-Bold"
except Exception:
    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    CJK = "STSong-Light"
    CJK_B = "STSong-Light"

LATIN = "Helvetica"
LATIN_B = "Helvetica-Bold"

W, H = A4  # 595 x 842 pt
MARGIN = 40

# ---------- helpers ----------

def fill_bg(c, color=BG):
    c.setFillColor(color)
    c.rect(0, 0, W, H, fill=1, stroke=0)

def draw_text(c, x, y, text, font=LATIN, size=10, color=INK):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawString(x, y, text)

def draw_text_right(c, x, y, text, font=LATIN, size=10, color=INK):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawRightString(x, y, text)

def draw_eyebrow(c, x, y, text, color=ACCENT_D, size=9):
    c.setFont(LATIN_B, size)
    c.setFillColor(color)
    c.drawString(x, y, text.upper())

def hline(c, x1, y, x2, color=LINE, w=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(w)
    c.line(x1, y, x2, y)

def draw_image_fit(c, path, x, y, w, h, bg=white, border=None):
    """Draw an image fitted within (x,y,w,h); preserves aspect.

    Default is pure white background with no border, so product photos sit
    cleanly on the page.
    """
    if not Path(path).exists():
        c.setFillColor(bg)
        c.roundRect(x, y, w, h, 8, fill=1, stroke=0)
        return
    if bg is not None:
        c.setFillColor(bg)
        c.roundRect(x, y, w, h, 8, fill=1, stroke=0)
    if border is not None:
        c.setStrokeColor(border)
        c.setLineWidth(0.5)
        c.roundRect(x, y, w, h, 8, fill=0, stroke=1)
    img = ImageReader(path)
    iw, ih = img.getSize()
    pad = 8
    avail_w = w - 2 * pad
    avail_h = h - 2 * pad
    scale = min(avail_w / iw, avail_h / ih)
    dw, dh = iw * scale, ih * scale
    dx = x + (w - dw) / 2
    dy = y + (h - dh) / 2
    c.drawImage(img, dx, dy, dw, dh, mask='auto', preserveAspectRatio=True)

def page_chrome(c, page_num, total, series_label):
    """Top header band + footer on every interior page."""
    # Header (light)
    c.setFillColor(PANEL)
    c.rect(0, H - 38, W, 38, fill=1, stroke=0)
    hline(c, 0, H - 38, W, color=LINE, w=0.5)
    draw_text(c, MARGIN, H - 24, "ERV.HK", font=LATIN_B, size=11, color=BLUE)
    draw_text(c, MARGIN + 70, H - 24, series_label, font=LATIN, size=9, color=MUTED)
    draw_text_right(c, W - MARGIN, H - 24,
                    f"{page_num} / {total}", font=LATIN, size=9, color=SUBTLE)

    # Footer
    fy = 32
    hline(c, MARGIN, fy + 18, W - MARGIN)
    draw_text(c, MARGIN, fy, "www.erv.hk", font=LATIN_B, size=9, color=BLUE)
    draw_text(c, MARGIN + 110, fy, "WhatsApp +852 8404 3880", font=LATIN, size=9, color=MUTED)
    draw_text(c, MARGIN + 270, fy, "Hotline +852 2121 0968", font=LATIN, size=9, color=MUTED)
    draw_text_right(c, W - MARGIN, fy, "erv@erv.hk", font=LATIN, size=9, color=MUTED)

# ---------- pages ----------

def cover(c, series_code, title_en, title_zh, lead_en, lead_zh,
          model_list, capacity_label, hero_image=None):
    fill_bg(c, BG)
    # Side stripes (brand)
    c.setFillColor(BLUE)
    c.rect(0, 0, 6, H, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, H - 92, 60, 4, fill=1, stroke=0)

    # Brand mark
    draw_text(c, MARGIN, H - 70, "ERV.HK", font=LATIN_B, size=22, color=BLUE)
    draw_text(c, MARGIN + 90, H - 70, "Hong Kong fresh-air & humidity systems",
              font=LATIN, size=10, color=MUTED)

    # Hero product image — right column on cover, between brand and stat row
    hero_w = 220
    hero_h = 260
    hero_x = W - MARGIN - hero_w
    hero_y = H - 360  # bottom edge → image spans H-100 to H-360
    if hero_image:
        draw_image_fit(c, str(IMG_DIR / hero_image), hero_x, hero_y, hero_w, hero_h,
                       bg=white, border=None)

    # Series tag
    draw_eyebrow(c, MARGIN, H - 160, f"PRODUCT CATALOG / {series_code} SERIES", color=ACCENT_D)

    # Big title — auto-fit to available width (left column, image on right)
    title_max_w = hero_x - MARGIN - 24 if hero_image else (W - 2 * MARGIN)
    title_size = 38
    c.setFont(LATIN_B, title_size)
    while c.stringWidth(title_en, LATIN_B, title_size) > title_max_w and title_size > 22:
        title_size -= 1
        c.setFont(LATIN_B, title_size)
    c.setFillColor(INK)
    c.drawString(MARGIN, H - 215, title_en)
    c.setFont(CJK, 22)
    c.setFillColor(INK_SOFT)
    c.drawString(MARGIN, H - 255, title_zh)

    # Stat row — models list + capacity
    stat_y = H - 410
    hline(c, MARGIN, stat_y + 50, W - MARGIN, color=LINE, w=0.8)
    models_str = "  ·  ".join(model_list)
    cap_w = 200
    models_x = MARGIN
    cap_x = W - MARGIN - cap_w

    draw_eyebrow(c, models_x, stat_y + 32, "MODELS", color=SUBTLE)
    avail = cap_x - models_x - 20
    size = 22
    c.setFont(LATIN_B, size)
    while c.stringWidth(models_str, LATIN_B, size) > avail and size > 14:
        size -= 1
        c.setFont(LATIN_B, size)
    c.setFillColor(INK)
    if c.stringWidth(models_str, LATIN_B, size) > avail and len(model_list) > 3:
        half = (len(model_list) + 1) // 2
        line1 = "  ·  ".join(model_list[:half])
        line2 = "  ·  ".join(model_list[half:])
        size = 16
        while size > 10 and (
            c.stringWidth(line1, LATIN_B, size) > avail
            or c.stringWidth(line2, LATIN_B, size) > avail
        ):
            size -= 1
        c.setFont(LATIN_B, size)
        c.drawString(models_x, stat_y + 10, line1)
        c.drawString(models_x, stat_y - 12, line2)
    else:
        c.drawString(models_x, stat_y, models_str)

    draw_eyebrow(c, cap_x, stat_y + 32, "CAPACITY", color=SUBTLE)
    c.setFont(LATIN_B, 22)
    c.setFillColor(BLUE)
    c.drawString(cap_x, stat_y, capacity_label)
    hline(c, MARGIN, stat_y - 18, W - MARGIN, color=LINE, w=0.8)

    # Lead paragraph
    lead_y = H - 500
    c.setFont(LATIN, 11)
    c.setFillColor(MUTED)
    en_lines = _wrap(lead_en, 78)
    for i, line in enumerate(en_lines):
        c.drawString(MARGIN, lead_y - i * 16, line)
    zh_y = lead_y - len(en_lines) * 16 - 24
    c.setFont(CJK, 11)
    c.setFillColor(MUTED)
    lead_max_w = W - 2 * MARGIN
    for i, line in enumerate(wrap_smart(c, lead_zh, lead_max_w, CJK, 11)):
        c.drawString(MARGIN, zh_y - i * 18, line)

    # Cover footer (subtle)
    cf_y = 60
    c.setFillColor(PANEL)
    c.rect(0, 0, W, 90, fill=1, stroke=0)
    hline(c, 0, 90, W, color=LINE, w=0.5)
    draw_text(c, MARGIN, cf_y + 12, "ERV.HK 2026. Environmental Electrical Appliance Limited",
              font=LATIN, size=9, color=MUTED)
    draw_text(c, MARGIN, cf_y - 6, "www.erv.hk",
              font=LATIN_B, size=12, color=BLUE)
    draw_text_right(c, W - MARGIN, cf_y + 12, "erv@erv.hk",
                    font=LATIN, size=9, color=ACCENT_D)
    draw_text_right(c, W - MARGIN, cf_y - 6, "WhatsApp +852 8404 3880",
                    font=LATIN_B, size=10, color=INK)
    c.showPage()

def overview_page(c, page_num, total, series_label, series_code,
                  description_en, description_zh, features, applications,
                  hero_image=None, feature_image=None, feature_caption=None):
    fill_bg(c, BG)
    page_chrome(c, page_num, total, series_label)

    y = H - 90
    draw_eyebrow(c, MARGIN, y, f"01  ABOUT THE {series_code} SERIES")
    y -= 26
    c.setFont(LATIN_B, 22)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, "System overview")
    y -= 30

    # Two-column body: text on left, image on right
    text_w = (W - 2 * MARGIN) * 0.58
    img_w = (W - 2 * MARGIN) * 0.38
    img_x = W - MARGIN - img_w
    text_x = MARGIN

    # Description text (text column)
    c.setFont(LATIN, 10.5)
    c.setFillColor(MUTED)
    en_chars = int(text_w / 5.5)  # rough chars-per-line
    ty = y
    for line in _wrap(description_en, 56):
        c.drawString(text_x, ty, line)
        ty -= 14
    ty -= 10
    c.setFont(CJK, 10)
    for line in wrap_smart(c, description_zh, text_w, CJK, 10):
        c.drawString(text_x, ty, line)
        ty -= 16

    # Right column: hero product image (always) plus an optional feature
    # close-up below it (e.g. the LCD touch panel for GEC V).
    if hero_image and feature_image:
        hero_h = 150
        feat_h = 130
        draw_image_fit(c, str(IMG_DIR / hero_image),
                       img_x, y - hero_h + 10, img_w, hero_h,
                       bg=white, border=None)
        feat_y = y - hero_h + 10 - feat_h - 6
        draw_image_fit(c, str(IMG_DIR / feature_image),
                       img_x, feat_y, img_w, feat_h,
                       bg=white, border=None)
        if feature_caption:
            c.setFont(LATIN_B, 8.5)
            c.setFillColor(MUTED)
            c.drawCentredString(img_x + img_w / 2, feat_y - 10,
                                feature_caption.upper())
        bottom = feat_y - (16 if feature_caption else 6)
    elif hero_image:
        img_h = 240
        draw_image_fit(c, str(IMG_DIR / hero_image),
                       img_x, y - img_h + 10, img_w, img_h,
                       bg=white, border=None)
        bottom = y - img_h + 4
    else:
        bottom = y

    y = min(ty, bottom) - 24

    # Two-column cards (Features / Applications)
    col_w = (W - 2 * MARGIN - 24) / 2
    col1_x = MARGIN
    col2_x = MARGIN + col_w + 24

    box_top = y
    box_h = 220

    # Feature card
    c.setFillColor(PANEL)
    c.roundRect(col1_x, box_top - box_h, col_w, box_h, 10, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(col1_x, box_top - box_h, col_w, box_h, 10, fill=0, stroke=1)
    # Applications card
    c.setFillColor(PANEL)
    c.roundRect(col2_x, box_top - box_h, col_w, box_h, 10, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(col2_x, box_top - box_h, col_w, box_h, 10, fill=0, stroke=1)

    # Features
    fy = box_top - 24
    draw_eyebrow(c, col1_x + 18, fy, "KEY FEATURES")
    fy -= 22
    c.setFont(LATIN_B, 13)
    c.setFillColor(INK)
    c.drawString(col1_x + 18, fy, "What's standard")
    fy -= 22
    for f in features:
        c.setFillColor(ACCENT)
        c.circle(col1_x + 24, fy + 4, 2, fill=1, stroke=0)
        c.setFont(LATIN, 9.5)
        c.setFillColor(INK_SOFT)
        c.drawString(col1_x + 34, fy, f)
        fy -= 16

    # Applications
    ay = box_top - 24
    draw_eyebrow(c, col2_x + 18, ay, "APPLICATIONS")
    ay -= 22
    c.setFont(LATIN_B, 13)
    c.setFillColor(INK)
    c.drawString(col2_x + 18, ay, "Where it works")
    ay -= 22
    for a in applications:
        c.setFillColor(ACCENT)
        c.circle(col2_x + 24, ay + 4, 2, fill=1, stroke=0)
        c.setFont(LATIN, 9.5)
        c.setFillColor(INK_SOFT)
        c.drawString(col2_x + 34, ay, a)
        ay -= 16

    c.showPage()

def specs_page(c, page_num, total, series_label, series_code, models, columns):
    fill_bg(c, BG)
    page_chrome(c, page_num, total, series_label)

    y = H - 90
    draw_eyebrow(c, MARGIN, y, f"02  {series_code} SERIES MODEL SPECIFICATIONS")
    y -= 26
    c.setFont(LATIN_B, 22)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, "Specifications")
    y -= 12
    c.setFont(LATIN, 10)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, y, "All measurements at 27 °C / 60% RH unless otherwise stated.")
    y -= 22

    # Image strip — small thumbnail per model above the table
    table_x = MARGIN
    table_w = W - 2 * MARGIN
    label_w = 130
    col_w = (table_w - label_w) / len(models)

    img_h = 60
    img_pad = 6
    img_y = y - img_h
    for i, m in enumerate(models):
        cx = table_x + label_w + i * col_w
        if m.get("image"):
            draw_image_fit(c, str(IMG_DIR / m["image"]),
                           cx + img_pad, img_y,
                           col_w - 2 * img_pad, img_h,
                           bg=white, border=None)
    y = img_y - 12

    # Header row — model names
    row_h = 30
    c.setFillColor(BLUE)
    c.rect(table_x, y - row_h, table_w, row_h, fill=1, stroke=0)
    c.setFont(LATIN_B, 9)
    c.setFillColor(white)
    c.drawString(table_x + 12, y - 18, "PARAMETER")
    for i, m in enumerate(models):
        cx = table_x + label_w + i * col_w
        c.setFont(LATIN_B, 10.5)
        c.setFillColor(white)
        # Auto-fit model name to column width
        size = 10.5
        while c.stringWidth(m["name"], LATIN_B, size) > col_w - 6 and size > 7:
            size -= 0.5
            c.setFont(LATIN_B, size)
        c.drawCentredString(cx + col_w / 2, y - 16, m["name"])
        if m.get("tag"):
            c.setFont(LATIN_B, 7)
            c.setFillColor(ACCENT)
            c.drawCentredString(cx + col_w / 2, y - 26, m["tag"])
    y -= row_h
    hline(c, table_x, y, table_x + table_w, color=LINE, w=0.6)

    # Body rows — sized so the bilingual two-line label fits inside the row
    n_rows = len(columns)
    body_h = 26 if n_rows >= 12 else (28 if n_rows >= 10 else 30)
    label_size = 9 if n_rows >= 12 else 9.5
    zh_size = label_size - 1.5
    val_size = 9.5 if n_rows >= 12 else 10
    en_top_pad = 11           # baseline distance from row top for EN
    zh_gap = label_size       # distance from EN baseline down to ZH baseline
    for ridx, (key, label_en, label_zh) in enumerate(columns):
        if ridx % 2 == 0:
            c.setFillColor(PANEL)
            c.rect(table_x, y - body_h, table_w, body_h, fill=1, stroke=0)
        c.setFont(LATIN_B, label_size)
        c.setFillColor(INK)
        c.drawString(table_x + 12, y - en_top_pad, label_en)
        c.setFont(CJK, zh_size)
        c.setFillColor(SUBTLE)
        c.drawString(table_x + 12, y - en_top_pad - zh_gap, label_zh)
        for i, m in enumerate(models):
            cx = table_x + label_w + i * col_w
            val = m["specs"].get(key, "—")
            size = val_size
            c.setFont(LATIN, size)
            while c.stringWidth(val, LATIN, size) > col_w - 8 and size > 7:
                size -= 0.5
                c.setFont(LATIN, size)
            c.setFillColor(INK_SOFT)
            c.drawCentredString(cx + col_w / 2, y - body_h / 2 - 3, val)
        y -= body_h
        hline(c, table_x, y, table_x + table_w, color=LINE_SOFT, w=0.4)
    c.showPage()

def config_page(c, page_num, total, series_label, series_code,
                config_items, control_items):
    fill_bg(c, BG)
    page_chrome(c, page_num, total, series_label)

    y = H - 90
    draw_eyebrow(c, MARGIN, y, f"03  {series_code} CONFIGURATION & CONTROL")
    y -= 26
    c.setFont(LATIN_B, 22)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, "Configuration & control")
    y -= 12
    c.setFont(LATIN, 10)
    c.setFillColor(MUTED)
    en_text = "Standard configuration and control features.  /  "
    c.drawString(MARGIN, y, en_text)
    c.setFont(CJK, 10)
    c.drawString(MARGIN + c.stringWidth(en_text, LATIN, 10), y, "標配項目與控制功能")
    y -= 38

    col_w = (W - 2 * MARGIN - 24) / 2
    col1_x = MARGIN
    col2_x = MARGIN + col_w + 24
    box_h = 360

    text_x_offset = 38
    right_pad = 18
    for col_x, head_label, items in [
        (col1_x, "CONFIGURATION", config_items),
        (col2_x, "SMART CONTROL", control_items),
    ]:
        c.setFillColor(PANEL)
        c.roundRect(col_x, y - box_h, col_w, box_h, 12, fill=1, stroke=0)
        c.setStrokeColor(LINE)
        c.roundRect(col_x, y - box_h, col_w, box_h, 12, fill=0, stroke=1)
        cy = y - 24
        draw_eyebrow(c, col_x + 22, cy, head_label)
        cy -= 26
        c.setFont(LATIN_B, 14)
        c.setFillColor(INK)
        c.drawString(col_x + 22, cy,
                     "What's standard" if head_label == "CONFIGURATION" else "Built-in intelligence")
        cy -= 26
        text_max_w = col_w - text_x_offset - right_pad
        for it_en, it_zh in items:
            c.setFillColor(ACCENT)
            c.circle(col_x + 28, cy + 3, 2, fill=1, stroke=0)
            # Auto-fit EN bullet to card width
            en_size = 10
            c.setFont(LATIN_B, en_size)
            while c.stringWidth(it_en, LATIN_B, en_size) > text_max_w and en_size > 7.5:
                en_size -= 0.5
                c.setFont(LATIN_B, en_size)
            c.setFillColor(INK)
            c.drawString(col_x + text_x_offset, cy, it_en)
            cy -= 12
            # Auto-fit ZH bullet too (CJK can also overflow)
            zh_size = 9
            c.setFont(CJK, zh_size)
            while c.stringWidth(it_zh, CJK, zh_size) > text_max_w and zh_size > 7.5:
                zh_size -= 0.5
                c.setFont(CJK, zh_size)
            c.setFillColor(MUTED)
            c.drawString(col_x + text_x_offset, cy, it_zh)
            cy -= 16

    y -= box_h + 28

    # CTA strip — brand blue
    card_h = 80
    c.setFillColor(BLUE)
    c.roundRect(MARGIN, y - card_h, W - 2 * MARGIN, card_h, 12, fill=1, stroke=0)
    c.setFont(LATIN_B, 13)
    c.setFillColor(white)
    c.drawString(MARGIN + 22, y - 28, "Free site assessment · 24-hour response")
    c.setFont(CJK, 11)
    c.drawString(MARGIN + 22, y - 46, "免費場地評估 · 一個工作天回覆")
    c.setFont(LATIN_B, 10.5)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN + 22, y - 64, "→ www.erv.hk/#quote   ·   WhatsApp +852 8404 3880   ·   erv@erv.hk")

    c.showPage()

# ---------- text wrapping ----------

def _wrap(text, width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if len(test) <= width:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def _wrap_cjk(text, width):
    """Legacy char-count wrapper kept for callers that still use it."""
    return [text[i:i + width] for i in range(0, len(text), width)]


def _is_cjk(ch):
    """Return True for any Chinese / Japanese / Korean / fullwidth glyph."""
    if not ch:
        return False
    cp = ord(ch)
    return (
        0x3000 <= cp <= 0x303F   # CJK symbols & punctuation
        or 0x3400 <= cp <= 0x4DBF
        or 0x4E00 <= cp <= 0x9FFF
        or 0xF900 <= cp <= 0xFAFF
        or 0xFE30 <= cp <= 0xFE4F
        or 0xFF00 <= cp <= 0xFFEF  # halfwidth/fullwidth forms
    )


def _tokenize_mixed(text):
    """Yield (kind, str) tokens. CJK chars individually; Latin runs atomic."""
    out, i, n = [], 0, len(text)
    while i < n:
        ch = text[i]
        if ch.isspace():
            j = i
            while j < n and text[j].isspace():
                j += 1
            out.append(('space', text[i:j]))
            i = j
        elif _is_cjk(ch):
            out.append(('cjk', ch))
            i += 1
        else:
            j = i
            while j < n and not _is_cjk(text[j]) and not text[j].isspace():
                j += 1
            out.append(('latin', text[i:j]))
            i = j
    return out


def wrap_smart(c, text, max_w, font, size):
    """Width-aware wrapper. Latin tokens stay atomic; CJK breaks per char."""
    tokens = _tokenize_mixed(text)
    lines, cur = [], ""
    for kind, t in tokens:
        # Drop a leading space at the start of a fresh line
        candidate = cur + t if (cur or kind != 'space') else cur
        if c.stringWidth(candidate, font, size) <= max_w:
            cur = candidate
            continue
        # Doesn't fit — flush the current line, start a new one with this token
        if cur.strip():
            lines.append(cur.rstrip())
        cur = "" if kind == 'space' else t
    if cur.strip():
        lines.append(cur.rstrip())
    return lines

# ========== GEC V CATALOG ==========

def gen_gec_v():
    out = OUT_DIR / "erv-gec-v-fresh-air-ceiling.pdf"
    c = canvas.Canvas(str(out), pagesize=A4)
    c.setTitle("ERV.hk · GEC V Series Fresh-air Ceiling Dehumidifier Catalog")
    c.setAuthor("ERV.hk")

    series_label = "GEC V Series · Fresh-air Ceiling Dehumidifier"
    total = 4

    cover(c, "GEC V",
          "Fresh-air ceiling",
          "新風淨化天花式抽濕機",
          "Fresh air × dehumidification × HEPA filtration in one ceiling unit. Independent fresh-air valve, return-air valve, HEPA filter, and a 5-in-1 air detector — auto-switching across dehumidify, fresh-air, mixed, and intelligent modes.",
          "新風 × 抽濕 × HEPA 過濾，一台天花機完成。獨立新風閥、回風閥、HEPA 高效濾網與五合一空氣探測器，可於抽濕、新風、混合、智能四個模式之間自動切換。",
          ["DBA-GEC30V", "DBA-GEC50V", "DBA-GEC70V", "DBA-GEC110V"], "30–110 L/day",
          hero_image="ceiling-dba-gec50v.jpg")

    overview_page(c, 2, total, series_label, "GEC V",
                  "The GEC V Series is the flagship fresh-air ceiling dehumidifier engineered for Hong Kong's sub-tropical climate. It maintains target humidity while continuously introducing HEPA-filtered outdoor air — solving CO2 build-up, PM2.5, cooking odours, and humidity in a single concealed unit. The 5-in-1 air detector reads PM2.5, CO2, VOC, temperature, and relative humidity, switching modes automatically.",
                  "GEC V 系列為 DBA 旗艦新風天花式抽濕機，專為香港氣候研發。在維持空間濕度的同時，引入經 HEPA 過濾的潔淨新風 — 一機解決室內 CO2 累積、PM2.5、烹飪異味與潮濕問題。內置五合一空氣探測器自動偵測 PM2.5、CO2、VOC、溫度與濕度，並於四個模式之間智能切換。",
                  features=[
                      "Fresh-air valve · 0–450 CMH on demand",
                      "HEPA + stainless steel mesh filtration",
                      "5-in-1 air sensor (PM2.5/CO2/VOC/T/RH)",
                      "DC brushless inverter motor",
                      "1.2 m head drain pump",
                      "86×86 mm LCD touch panel",
                      "RS485 Modbus BMS interface",
                      "WiFi App + scheduled timer",
                      "Power-off memory + dry-contact input",
                  ],
                  applications=[
                      "Luxury residential & duplexes",
                      "Hotel suites & serviced apartments",
                      "Clubhouses & private dining",
                      "Offices & retail (zone-distributed)",
                      "Premium residences in Mid-Levels",
                      "Concealed false-ceiling installation",
                  ],
                  hero_image="ceiling-dba-gec110v.jpg",
                  feature_image="panel-dba-gecv.jpg",
                  feature_caption="86×86 mm LCD touch panel · 5-in-1 air detector")

    specs_page(c, 3, total, series_label, "GEC V",
               models=[
                   {"name": "DBA-GEC30V", "image": "ceiling-dba-gec30v.jpg", "specs": {
                       "cap_30": "30 L/day", "cap_27": "10.8 L/day",
                       "fresh_air": "0–170 CMH", "airflow": "350 CMH",
                       "coverage": "200–400 sq ft", "noise": "38/50 dB(A)",
                       "static": "100 Pa", "power": "330 / 440 W",
                       "dim": "992 × 526 × 245 mm", "weight": "39 kg",
                       "supply": "220-240V / 50Hz", "drain": "1.2 m",
                       "ports": "Ø146 mm × 3", "refrig": "R134a / 260 g",
                       "filter": "HEPA + SS mesh", "comm": "RS485 + Dry contact",
                   }},
                   {"name": "DBA-GEC50V", "tag": "BESTSELLER", "image": "ceiling-dba-gec50v.jpg", "specs": {
                       "cap_30": "50 L/day", "cap_27": "26.4 L/day",
                       "fresh_air": "0–225 CMH", "airflow": "450 CMH",
                       "coverage": "400–600 sq ft", "noise": "42/50 dB(A)",
                       "static": "100 Pa", "power": "520 / 780 W",
                       "dim": "1,004 × 560 × 255 mm", "weight": "52 kg",
                       "supply": "220-240V / 50Hz", "drain": "1.2 m",
                       "ports": "Ø146 mm × 3", "refrig": "R410A / 400 g",
                       "filter": "HEPA + SS mesh", "comm": "RS485 + Dry contact",
                   }},
                   {"name": "DBA-GEC70V", "image": "ceiling-dba-gec70v.jpg", "specs": {
                       "cap_30": "70 L/day", "cap_27": "—",
                       "fresh_air": "0–250 CMH", "airflow": "500 CMH",
                       "coverage": "600–800 sq ft", "noise": "45/50 dB(A)",
                       "static": "100 Pa", "power": "—",
                       "dim": "1,032 × 626 × 265 mm", "weight": "60 kg",
                       "supply": "220-240V / 50Hz", "drain": "1.2 m",
                       "ports": "Ø146 mm × 3", "refrig": "R410A",
                       "filter": "HEPA + SS mesh", "comm": "RS485 + Dry contact",
                   }},
                   {"name": "DBA-GEC110V", "image": "ceiling-dba-gec110v.jpg", "specs": {
                       "cap_30": "110 L/day", "cap_27": "52.8 L/day",
                       "fresh_air": "0–450 CMH", "airflow": "900 CMH",
                       "coverage": "800–1,200 sq ft", "noise": "45/50 dB(A)",
                       "static": "100 Pa", "power": "1,020 / 1,415 W",
                       "dim": "1,200 × 795 × 284 mm", "weight": "71 kg",
                       "supply": "220-240V / 50Hz", "drain": "1.2 m",
                       "ports": "Ø196 mm × 3", "refrig": "R410A / 900 g",
                       "filter": "HEPA + SS mesh", "comm": "RS485 + Dry contact",
                   }},
               ],
               columns=[
                   ("cap_30",    "Capacity (30°C 80%)",   "抽濕量 (30°C 80%)"),
                   ("cap_27",    "Capacity (26.7°C 60%)", "抽濕量 (26.7°C 60%)"),
                   ("fresh_air", "Fresh-air supply",      "新風量"),
                   ("airflow",   "Indoor airflow",        "室內風量"),
                   ("coverage",  "Coverage",              "適用面積"),
                   ("noise",     "Noise (3 m)",           "噪音 (3 米)"),
                   ("static",    "Static pressure",       "靜壓"),
                   ("power",     "Rated / Max power",     "額定 / 最大功率"),
                   ("dim",       "Dimensions (L×W×H)",    "尺寸"),
                   ("weight",    "Weight",                "重量"),
                   ("supply",    "Power supply",          "電源"),
                   ("drain",     "Drain pump head",       "水泵揚程"),
                   ("ports",     "Air outlet / inlet",    "出 / 入風口"),
                   ("refrig",    "Refrigerant",           "冷媒"),
                   ("filter",    "Filtration",            "過濾"),
                   ("comm",      "Connectivity",          "通訊"),
               ])

    config_page(c, 4, total, series_label, "GEC V",
                config_items=[
                    ("Drain pump (1.2 m head)",            "排水泵 1.2 m 揚程"),
                    ("HEPA high-efficiency filter",        "HEPA 高效空氣過濾網"),
                    ("Stainless steel mesh pre-filter",    "不銹鋼網目濾網"),
                    ("DC brushless inverter motor",        "直流無刷變頻電機"),
                    ("5-in-1 air detector",                "五合一空氣探測器"),
                    ("86×86 mm LCD touch panel",           "86×86mm LCD 彩色觸控屏"),
                    ("Independent fresh / return valves",  "獨立新風閥及回風閥"),
                    ("Concealed false-ceiling mount",      "天花式隱藏安裝"),
                ],
                control_items=[
                    ("RH setpoint range 20–95%",          "濕度設定範圍 20–95%"),
                    ("4 modes: dehumidify / fresh-air / mixed / smart", "四模式：抽濕 / 新風 / 混合 / 智能"),
                    ("Low / high fan speed",              "低 / 高風速"),
                    ("RS485 Modbus BMS interface",        "RS485 Modbus 樓宇管理接口"),
                    ("Schedule on/off + power-off memory","定時開關機 + 斷電記憶"),
                    ("Dry-contact input + fault detection","乾接點輸入 + 故障偵測"),
                    ("PM2.5 / CO2 / VOC / T / RH sensing","PM2.5 / CO2 / VOC / 溫濕度感應"),
                    ("Auto mode-switch by air quality",   "依空氣質素智能切換模式"),
                ])

    c.save()
    print(f"Wrote {out}")

# ========== UTC CATALOG ==========

def gen_utc():
    out = OUT_DIR / "erv-utc-ultra-thin-ceiling.pdf"
    c = canvas.Canvas(str(out), pagesize=A4)
    c.setTitle("ERV.hk · UTC Series Ultra-thin Ceiling Dehumidifier Catalog")
    c.setAuthor("ERV.hk")

    series_label = "UTC Series · Ultra-thin Ceiling Dehumidifier"
    total = 4

    cover(c, "UTC",
          "Ultra-thin ceiling",
          "超薄天花式抽濕機",
          "A 200 mm slim profile that disappears into any false ceiling. Pure precision dehumidification from 39 dB(A) — quieter than a hushed conversation. UV-C lamp, WiFi App, RS485 BMS, and Hong Kong Grade 1 Energy Label on the entry model.",
          "200 mm 超薄機身，無聲融入假天花。專注於高效抽濕，39 dB(A) 起 — 比安靜對話更輕。配備 UV-C 殺菌、WiFi App、RS485 BMS，UTC20 取得香港一級能源標籤。",
          ["DBA-UTC20", "DBA-UTC68", "DBA-UTC120"], "20–120 L/day",
          hero_image="ceiling-dba-utc20-1.jpg")

    overview_page(c, 2, total, series_label, "UTC",
                  "The UTC Series prioritises absolute precision dehumidification with a near-silent profile. At only 200 mm thick (UTC20), it disappears into any false ceiling and is ideal as a humidity supplement when fresh-air ventilation is already handled separately. UV-C sterilisation, scheduled timers, WiFi App, and RS485 Modbus BMS are standard.",
                  "UTC 系列專注於精準、靜音抽濕。最薄機型 200 mm (UTC20)，無聲融入假天花，適合已有獨立新風系統的住宅或會所作為濕度補強。標配 UV-C 殺菌燈、定時開關、WiFi App 與 RS485 Modbus 樓宇管理系統接口。",
                  features=[
                      "Slim 200–310 mm profile",
                      "39 dB(A) low-noise operation",
                      "UV-C sterilisation lamp",
                      "Stainless steel mesh filter",
                      "1.8 m head drain pump",
                      "5 m humidity sensor cable",
                      "WiFi App + IR remote",
                      "RS485 Modbus BMS",
                      "HK Grade 1 Energy Label (UTC20)",
                  ],
                  applications=[
                      "Existing AC + ventilation projects",
                      "Apartments needing pure RH control",
                      "Bedrooms (low-noise priority)",
                      "Wine storage rooms",
                      "Storage & wardrobes",
                      "Server / equipment closets",
                  ],
                  hero_image="ceiling-dba-utc68-1.jpg")

    specs_page(c, 3, total, series_label, "UTC",
               models=[
                   {"name": "DBA-UTC20", "tag": "HK GRADE 1", "image": "ceiling-dba-utc20-1.jpg", "specs": {
                       "cap_30": "20 L/day", "cap_27": "9.9 L/day",
                       "airflow": "220 CMH", "coverage": "200–400 sq ft",
                       "noise": "39 dB(A)", "static": "80 Pa",
                       "power": "196 / 300 W", "thickness": "200 mm",
                       "dim": "865 × 376 × 200 mm", "weight": "28 kg",
                       "supply": "220-240V / 50Hz", "drain": "1.8 m",
                       "ports": "Ø146 mm", "refrig": "R134a / 230 g",
                       "uvc": "UV-C lamp", "comm": "WiFi + RS485",
                   }},
                   {"name": "DBA-UTC68", "image": "ceiling-dba-utc68-1.jpg", "specs": {
                       "cap_30": "68 L/day", "cap_27": "42 L/day",
                       "airflow": "500 CMH", "coverage": "800–1,000 sq ft",
                       "noise": "48 dB(A)", "static": "100 Pa",
                       "power": "880 / 1,250 W", "thickness": "240 mm",
                       "dim": "1,010 × 500 × 240 mm", "weight": "42 kg",
                       "supply": "220-240V / 50Hz", "drain": "1.8 m",
                       "ports": "Ø146 mm", "refrig": "R410A / 600 g",
                       "uvc": "UV-C lamp", "comm": "WiFi + RS485",
                   }},
                   {"name": "DBA-UTC120", "image": "ceiling-dba-utc120-1.jpg", "specs": {
                       "cap_30": "120 L/day", "cap_27": "53 L/day",
                       "airflow": "890 CMH", "coverage": "1,300–1,500 sq ft",
                       "noise": "50 dB(A)", "static": "100 Pa",
                       "power": "1,010 / 1,600 W", "thickness": "310 mm",
                       "dim": "1,075 × 746 × 310 mm", "weight": "64 kg",
                       "supply": "220-240V / 50Hz", "drain": "1.8 m",
                       "ports": "Ø196 mm", "refrig": "R410A / 900 g",
                       "uvc": "UV-C lamp", "comm": "WiFi + RS485",
                   }},
               ],
               columns=[
                   ("cap_30",   "Capacity (30°C 80%)",   "抽濕量 (30°C 80%)"),
                   ("cap_27",   "Capacity (26.7°C 60%)", "抽濕量 (26.7°C 60%)"),
                   ("airflow",  "Airflow",               "風量"),
                   ("coverage", "Coverage",              "適用面積"),
                   ("noise",    "Noise (3 m)",           "噪音 (3 米)"),
                   ("static",   "Static pressure",       "靜壓"),
                   ("power",    "Rated / Max power",     "額定 / 最大功率"),
                   ("thickness","Profile thickness",     "厚度"),
                   ("dim",      "Dimensions (L×W×H)",    "尺寸"),
                   ("weight",   "Weight",                "重量"),
                   ("supply",   "Power supply",          "電源"),
                   ("drain",    "Drain pump head",       "水泵揚程"),
                   ("ports",    "Air outlet / inlet",    "出 / 入風口"),
                   ("refrig",   "Refrigerant",           "冷媒"),
                   ("uvc",      "Sterilisation",         "殺菌"),
                   ("comm",     "Connectivity",          "通訊"),
               ])

    config_page(c, 4, total, series_label, "UTC",
                config_items=[
                    ("Drain pump (1.8 m head)",         "排水泵 1.8 m 揚程"),
                    ("UV-C sterilisation lamp",         "UV-C 紫外線殺菌燈"),
                    ("Stainless steel mesh filter",     "不銹鋼網目濾網"),
                    ("Emergency stop button",           "緊急停機按鈕"),
                    ("5 m humidity sensor cable",       "5 m 濕度感應線"),
                    ("IR remote included",              "遙控器標配"),
                    ("Slim 200–310 mm profile",         "200–310 mm 超薄機身"),
                    ("Concealed false-ceiling mount",   "天花式隱藏安裝"),
                ],
                control_items=[
                    ("RH setpoint range 20–95%",        "濕度設定範圍 20–95%"),
                    ("Low / high fan speed",            "低 / 高風速"),
                    ("WiFi App control",                "WiFi App 智能控制"),
                    ("RS485 Modbus BMS",                "RS485 Modbus 樓宇管理接口"),
                    ("Scheduled on/off timer",          "定時開關機"),
                    ("Power-off memory",                "斷電記憶"),
                    ("HK Grade 1 Energy Label (UTC20)", "香港一級能源標籤 (UTC20)"),
                    ("Quiet from 39 dB(A)",             "39 dB(A) 起低噪音運作"),
                ])

    c.save()
    print(f"Wrote {out}")


# ========== GEC COMMERCIAL (LD) CATALOG ==========

def gen_gec_commercial():
    out = OUT_DIR / "erv-gec-commercial-ceiling.pdf"
    c = canvas.Canvas(str(out), pagesize=A4)
    c.setTitle("ERV.hk · GEC Commercial Ceiling Dehumidifier Catalog")
    c.setAuthor("ERV.hk")

    series_label = "GEC Series · Commercial Ceiling Dehumidifier"
    total = 4

    cover(c, "GEC",
          "Commercial ceiling",
          "商用天花式抽濕機",
          "High static pressure ducted ceiling dehumidifiers built for large floors and multi-room distribution. RS485 BMS standard, 68 to 550 L/day capacity. Engineered for offices, retail, hotel ballrooms, indoor pools, and large clubhouses.",
          "為大空間設計的高靜壓商用天花機 — 商廈辦公室、零售商舖、酒店宴會廳、室內泳池、大型會所。RS485 BMS 標配，68 至 550 公升 / 日抽濕量任選，多區管道分送。",
          ["DBA-GEC68LD-HP", "DBA-GEC145LD-HP", "DBA-GEC280LD", "DBA-GEC400LD", "DBA-GEC550LD"], "68–550 L/day",
          hero_image="ceiling-dba-gec145ld-1.jpg")

    overview_page(c, 2, total, series_label, "GEC",
                  "The GEC commercial ceiling series handles large floor plates and ducted multi-zone distribution that smaller residential units cannot serve. High static pressure (up to 80 Pa) drives air through long duct runs, while the stainless evaporator and pump drainage suit demanding industrial and commercial environments. Five capacity points cover everything from a 1,000 sq ft retail unit to a 5,000 sq ft hotel ballroom.",
                  "GEC 商用天花系列專為大面積、多區管道分送設計 — 高靜壓 (最高 80 Pa) 推動長距離管道送風，不銹鋼蒸發器與排水泵應對嚴苛的商業與工業環境。五款抽濕量由 68 至 550 公升 / 日，涵蓋 1,000 至 5,000 平方呎空間。",
                  features=[
                      "High static pressure for ducting",
                      "Stainless steel evaporator & tank",
                      "Pump drainage with 10 m head",
                      "RS485 Modbus BMS interface",
                      "Three-phase models (GEC400LD+)",
                      "DC inverter compressor (HP series)",
                      "Centralised setpoint and alarms",
                      "Concealed false-ceiling mount",
                      "Low-noise EC fan motor",
                  ],
                  applications=[
                      "Open-plan offices & coworking",
                      "Retail outlets & showrooms",
                      "Hotel ballrooms & lobbies",
                      "Indoor swimming pools",
                      "Clubhouses & banquet halls",
                      "Logistics & cold storage rooms",
                  ],
                  hero_image="ceiling-dba-gec280ld-1.jpg")

    specs_page(c, 3, total, series_label, "GEC",
               models=[
                   {"name": "DBA-GEC68LD-HP", "image": "ceiling-dba-gec68ld-1.jpg", "specs": {
                       "capacity": "68 L/day", "coverage": "800–1,000 sq ft",
                       "airflow": "500 CMH", "noise": "49 dB(A)",
                       "dim": "970 × 525 × 345 mm", "weight": "—",
                       "supply": "220-240V / 50Hz", "uvc": "UV-C lamp",
                       "comm": "RS485 Modbus",
                   }},
                   {"name": "DBA-GEC145LD-HP", "image": "ceiling-dba-gec145ld-1.jpg", "specs": {
                       "capacity": "145 L/day", "coverage": "1,500–1,700 sq ft",
                       "airflow": "1,200 CMH", "noise": "50 dB(A)",
                       "dim": "1,005 × 695 × 440 mm", "weight": "70 kg",
                       "supply": "220-240V / 50Hz", "uvc": "UV-C lamp",
                       "comm": "RS485 Modbus",
                   }},
                   {"name": "DBA-GEC280LD", "image": "ceiling-dba-gec280ld-1.jpg", "specs": {
                       "capacity": "280 L/day", "coverage": "2,500–3,000 sq ft",
                       "airflow": "1,700 CMH", "noise": "58 dB(A)",
                       "dim": "1,137 × 900 × 540 mm", "weight": "108 kg",
                       "supply": "380V 3N / 50Hz", "uvc": "—",
                       "comm": "RS485 Modbus",
                   }},
                   {"name": "DBA-GEC400LD", "image": "ceiling-dba-gec400ld-1.jpg", "specs": {
                       "capacity": "400 L/day", "coverage": "3,000–4,000 sq ft",
                       "airflow": "3,250 CMH", "noise": "65 dB(A)",
                       "dim": "1,270 × 1,200 × 605 mm", "weight": "210 kg",
                       "supply": "380V 3N / 50Hz", "uvc": "—",
                       "comm": "RS485 Modbus",
                   }},
                   {"name": "DBA-GEC550LD", "image": "ceiling-dba-gec550ld-1.jpg", "specs": {
                       "capacity": "550 L/day", "coverage": "4,000–5,000 sq ft",
                       "airflow": "3,250 CMH", "noise": "65 dB(A)",
                       "dim": "1,270 × 1,200 × 605 mm", "weight": "240 kg",
                       "supply": "380V 3N / 50Hz", "uvc": "—",
                       "comm": "RS485 Modbus",
                   }},
               ],
               columns=[
                   ("capacity", "Capacity (30°C 80%)", "抽濕量 (30°C 80%)"),
                   ("coverage", "Coverage",            "適用面積"),
                   ("airflow",  "Airflow",             "風量"),
                   ("noise",    "Noise level",         "噪音"),
                   ("dim",      "Dimensions (L×W×H)",  "尺寸"),
                   ("weight",   "Weight",              "重量"),
                   ("supply",   "Power supply",        "電源"),
                   ("uvc",      "Sterilisation",       "殺菌"),
                   ("comm",     "Connectivity",        "通訊"),
               ])

    config_page(c, 4, total, series_label, "GEC",
                config_items=[
                    ("High static pressure for ducting",     "高靜壓管道送風"),
                    ("Stainless steel evaporator & tank",    "不銹鋼蒸發器與水盤"),
                    ("Pump drainage (10 m head)",            "排水泵 10 m 揚程"),
                    ("DC inverter compressor (HP series)",   "直流變頻壓縮機 (HP 機型)"),
                    ("UV-C sterilisation (68LD/145LD)",      "UV-C 殺菌燈 (68LD/145LD)"),
                    ("EC fan motor — low noise",             "EC 低噪音風扇電機"),
                    ("Three-phase 380V (280LD/400LD/550LD)", "三相電源 (280LD 起)"),
                    ("Concealed false-ceiling mount",        "天花式隱藏安裝"),
                ],
                control_items=[
                    ("RH setpoint range 20–95%",          "濕度設定範圍 20–95%"),
                    ("Centralised setpoints via BMS",     "BMS 集中控制設定"),
                    ("RS485 Modbus interface",            "RS485 Modbus 樓宇管理接口"),
                    ("Fault relay + alarm output",        "故障繼電器 + 警報輸出"),
                    ("Schedule on/off + power-off memory","定時開關機 + 斷電記憶"),
                    ("Dry-contact remote enable",         "乾接點遠程啟動"),
                    ("Real-time runtime telemetry",       "實時運行狀態遙測"),
                    ("Multi-zone duct distribution",      "多區管道分送"),
                ])

    c.save()
    print(f"Wrote {out}")


if __name__ == "__main__":
    gen_gec_v()
    gen_utc()
    gen_gec_commercial()
