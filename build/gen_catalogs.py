#!/usr/bin/env python3
"""Generate ERV.hk product catalogs (GEC V + UTC) as branded PDFs.

Output: clients/erv-hk/catalogs/erv-gec-v-fresh-air-ceiling.pdf
        clients/erv-hk/catalogs/erv-utc-ultra-thin-ceiling.pdf

Style: navy bg, orange accent, white text, English + Traditional Chinese.
No DBA contact info — ERV.hk channels only.
"""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, Color
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont

OUT_DIR = Path(__file__).resolve().parent.parent / "catalogs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

NAVY      = HexColor("#060a1a")
NAVY_2    = HexColor("#0d1530")
BLUE      = HexColor("#0023ff")
ACCENT    = HexColor("#ff8a14")
ACCENT_D  = HexColor("#d96900")
LINE      = Color(1, 1, 1, alpha=0.12)
MUTED     = Color(1, 1, 1, alpha=0.65)
SUBTLE    = Color(1, 1, 1, alpha=0.45)

# macOS STHeiti Light has full Traditional Chinese coverage. Falls back to
# STSong-Light (CIDFont) if the system font isn't available.
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

def fill_bg(c, color=NAVY):
    c.setFillColor(color)
    c.rect(0, 0, W, H, fill=1, stroke=0)

def draw_text(c, x, y, text, font=LATIN, size=10, color=white):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawString(x, y, text)

def draw_text_right(c, x, y, text, font=LATIN, size=10, color=white):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawRightString(x, y, text)

def draw_eyebrow(c, x, y, text, color=ACCENT):
    c.setFont(LATIN_B, 9)
    c.setFillColor(color)
    c.drawString(x, y, text.upper())

def hline(c, x1, y, x2, color=LINE, w=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(w)
    c.line(x1, y, x2, y)

def page_chrome(c, page_num, total, series_label):
    """Header strip + footer on every interior page."""
    # Header band
    c.setFillColor(NAVY_2)
    c.rect(0, H - 38, W, 38, fill=1, stroke=0)
    draw_text(c, MARGIN, H - 24, "ERV.HK", font=LATIN_B, size=11, color=ACCENT)
    draw_text(c, MARGIN + 70, H - 24, series_label, font=LATIN, size=9, color=MUTED)
    draw_text_right(c, W - MARGIN, H - 24,
                    f"{page_num} / {total}", font=LATIN, size=9, color=SUBTLE)

    # Footer with ERV.hk channels
    fy = 32
    hline(c, MARGIN, fy + 18, W - MARGIN)
    draw_text(c, MARGIN, fy, "www.erv.hk", font=LATIN_B, size=9, color=white)
    draw_text(c, MARGIN + 110, fy, "WhatsApp +852 8404 3880", font=LATIN, size=9, color=MUTED)
    draw_text(c, MARGIN + 270, fy, "Hotline +852 2121 0968", font=LATIN, size=9, color=MUTED)
    draw_text_right(c, W - MARGIN, fy, "erv@erv.hk", font=LATIN, size=9, color=MUTED)

def cover(c, series_code, title_en, title_zh, lead_en, lead_zh, model_list, capacity_label):
    fill_bg(c, NAVY)
    # Decorative blocks
    c.setFillColor(BLUE)
    c.rect(0, 0, 6, H, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, H - 90, 60, 4, fill=1, stroke=0)

    # Brand mark
    draw_text(c, MARGIN, H - 70, "ERV.HK", font=LATIN_B, size=22, color=white)
    draw_text(c, MARGIN + 90, H - 70, "Hong Kong fresh-air & humidity systems",
              font=LATIN, size=10, color=MUTED)

    # Series tag
    draw_eyebrow(c, MARGIN, H - 200, f"PRODUCT CATALOG / {series_code} SERIES", color=ACCENT)

    # Big title
    c.setFont(LATIN_B, 38)
    c.setFillColor(white)
    c.drawString(MARGIN, H - 250, title_en)
    c.setFont(CJK, 26)
    c.drawString(MARGIN, H - 290, title_zh)

    # Stat row — models list + capacity
    stat_y = H - 380
    hline(c, MARGIN, stat_y + 50, W - MARGIN, color=LINE, w=0.8)
    models_str = "  ·  ".join(model_list)
    cap_w = 200  # right column reserved for capacity
    models_x = MARGIN
    cap_x = W - MARGIN - cap_w

    draw_eyebrow(c, models_x, stat_y + 32, "MODELS", color=SUBTLE)
    # Auto-fit; wrap to two lines if still too wide at 14pt.
    avail = cap_x - models_x - 20
    size = 22
    c.setFont(LATIN_B, size)
    while c.stringWidth(models_str, LATIN_B, size) > avail and size > 14:
        size -= 1
        c.setFont(LATIN_B, size)
    c.setFillColor(white)
    if c.stringWidth(models_str, LATIN_B, size) > avail and len(model_list) > 3:
        # Split into two rows; auto-fit each line independently.
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
    c.setFillColor(white)
    c.drawString(cap_x, stat_y, capacity_label)
    hline(c, MARGIN, stat_y - 18, W - MARGIN, color=LINE, w=0.8)

    # Lead paragraph
    lead_y = H - 480
    c.setFont(LATIN, 11)
    c.setFillColor(MUTED)
    for i, line in enumerate(_wrap(lead_en, 78)):
        c.drawString(MARGIN, lead_y - i * 16, line)
    zh_y = lead_y - len(_wrap(lead_en, 78)) * 16 - 24
    c.setFont(CJK, 11)
    c.setFillColor(MUTED)
    for i, line in enumerate(_wrap_cjk(lead_zh, 36)):
        c.drawString(MARGIN, zh_y - i * 18, line)

    # Cover footer
    cf_y = 60
    c.setFillColor(NAVY_2)
    c.rect(0, 0, W, 90, fill=1, stroke=0)
    draw_text(c, MARGIN, cf_y + 12, "Manufactured for ERV.hk by HK Environmental Electrical Appliance Limited",
              font=LATIN, size=9, color=MUTED)
    draw_text(c, MARGIN, cf_y - 6, "www.erv.hk  ·  www.erv.com.hk  ·  www.ervhk.com",
              font=LATIN_B, size=10, color=white)
    draw_text_right(c, W - MARGIN, cf_y + 12, "erv@erv.hk",
                    font=LATIN, size=9, color=ACCENT)
    draw_text_right(c, W - MARGIN, cf_y - 6, "WhatsApp +852 8404 3880",
                    font=LATIN_B, size=10, color=white)
    c.showPage()

def overview_page(c, page_num, total, series_label, series_code,
                  description_en, description_zh, features, applications):
    fill_bg(c, NAVY)
    page_chrome(c, page_num, total, series_label)

    y = H - 90
    draw_eyebrow(c, MARGIN, y, f"01  ABOUT THE {series_code} SERIES")
    y -= 26
    c.setFont(LATIN_B, 22)
    c.setFillColor(white)
    c.drawString(MARGIN, y, "System overview")
    y -= 32

    # English description
    c.setFont(LATIN, 11)
    c.setFillColor(MUTED)
    for line in _wrap(description_en, 82):
        c.drawString(MARGIN, y, line)
        y -= 15
    y -= 16
    c.setFont(CJK, 10.5)
    for line in _wrap_cjk(description_zh, 38):
        c.drawString(MARGIN, y, line)
        y -= 17
    y -= 22

    # Two-column: Features | Applications
    col_w = (W - 2 * MARGIN - 24) / 2
    col1_x = MARGIN
    col2_x = MARGIN + col_w + 24

    box_top = y
    box_h = 240
    # Features card
    c.setFillColor(NAVY_2)
    c.roundRect(col1_x, box_top - box_h, col_w, box_h, 10, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(col1_x, box_top - box_h, col_w, box_h, 10, fill=0, stroke=1)
    # Applications card
    c.setFillColor(NAVY_2)
    c.roundRect(col2_x, box_top - box_h, col_w, box_h, 10, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(col2_x, box_top - box_h, col_w, box_h, 10, fill=0, stroke=1)

    # Feature heading + items
    fy = box_top - 26
    draw_eyebrow(c, col1_x + 18, fy, "KEY FEATURES")
    fy -= 22
    c.setFont(LATIN_B, 13)
    c.setFillColor(white)
    c.drawString(col1_x + 18, fy, "What's standard")
    fy -= 22
    for f in features:
        c.setFillColor(ACCENT)
        c.circle(col1_x + 24, fy + 4, 2, fill=1, stroke=0)
        c.setFont(LATIN, 10)
        c.setFillColor(white)
        c.drawString(col1_x + 34, fy, f)
        fy -= 17

    # Applications heading + items
    ay = box_top - 26
    draw_eyebrow(c, col2_x + 18, ay, "APPLICATIONS")
    ay -= 22
    c.setFont(LATIN_B, 13)
    c.setFillColor(white)
    c.drawString(col2_x + 18, ay, "Where it works")
    ay -= 22
    for a in applications:
        c.setFillColor(ACCENT)
        c.circle(col2_x + 24, ay + 4, 2, fill=1, stroke=0)
        c.setFont(LATIN, 10)
        c.setFillColor(white)
        c.drawString(col2_x + 34, ay, a)
        ay -= 17

    c.showPage()

def specs_page(c, page_num, total, series_label, series_code, models, columns):
    fill_bg(c, NAVY)
    page_chrome(c, page_num, total, series_label)

    y = H - 90
    draw_eyebrow(c, MARGIN, y, f"02  {series_code} SERIES MODEL SPECIFICATIONS")
    y -= 26
    c.setFont(LATIN_B, 22)
    c.setFillColor(white)
    c.drawString(MARGIN, y, "Specifications")
    y -= 12
    c.setFont(LATIN, 10)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, y, "All measurements at 27 °C / 60% RH unless otherwise stated.")
    y -= 28

    # Table
    table_x = MARGIN
    table_w = W - 2 * MARGIN
    label_w = 130
    col_w = (table_w - label_w) / len(models)

    # Header row
    row_h = 32
    c.setFillColor(NAVY_2)
    c.rect(table_x, y - row_h, table_w, row_h, fill=1, stroke=0)
    c.setFont(LATIN_B, 9)
    c.setFillColor(SUBTLE)
    c.drawString(table_x + 12, y - 18, "PARAMETER")
    for i, m in enumerate(models):
        cx = table_x + label_w + i * col_w
        c.setFont(LATIN_B, 11)
        c.setFillColor(white)
        c.drawCentredString(cx + col_w / 2, y - 18, m["name"])
        if m.get("tag"):
            c.setFont(LATIN_B, 7)
            c.setFillColor(ACCENT)
            c.drawCentredString(cx + col_w / 2, y - 28, m["tag"])
    y -= row_h
    hline(c, table_x, y, table_x + table_w, color=LINE, w=0.6)

    # Body rows
    for ridx, (key, label_en, label_zh) in enumerate(columns):
        body_h = 26
        if ridx % 2 == 0:
            c.setFillColor(Color(1, 1, 1, alpha=0.025))
            c.rect(table_x, y - body_h, table_w, body_h, fill=1, stroke=0)
        # Label
        c.setFont(LATIN_B, 9.5)
        c.setFillColor(white)
        c.drawString(table_x + 12, y - 16, label_en)
        c.setFont(CJK, 8.5)
        c.setFillColor(SUBTLE)
        c.drawString(table_x + 12, y - 24, label_zh)
        # Values
        for i, m in enumerate(models):
            cx = table_x + label_w + i * col_w
            val = m["specs"].get(key, "—")
            c.setFont(LATIN, 10.5)
            c.setFillColor(white)
            c.drawCentredString(cx + col_w / 2, y - 16, val)
        y -= body_h
        hline(c, table_x, y, table_x + table_w, color=LINE, w=0.4)
    c.showPage()

def picker_page(c, page_num, total, series_label, series_code, picker_rows):
    fill_bg(c, NAVY)
    page_chrome(c, page_num, total, series_label)

    y = H - 90
    draw_eyebrow(c, MARGIN, y, f"03  HOW TO PICK A {series_code} MODEL")
    y -= 26
    c.setFont(LATIN_B, 22)
    c.setFillColor(white)
    c.drawString(MARGIN, y, "Sizing guide")
    y -= 12
    c.setFont(LATIN, 10)
    c.setFillColor(MUTED)
    en_text = "Match the right unit to the room load.  /  "
    c.drawString(MARGIN, y, en_text)
    c.setFont(CJK, 10)
    c.drawString(MARGIN + c.stringWidth(en_text, LATIN, 10), y, "按面積選型")
    y -= 30

    # Header
    table_x = MARGIN
    table_w = W - 2 * MARGIN
    cols = [("ROOM TYPE", 0.30), ("FLOOR AREA", 0.22), ("RECOMMENDED", 0.28), ("NOTES", 0.20)]
    c.setFillColor(NAVY_2)
    c.rect(table_x, y - 28, table_w, 28, fill=1, stroke=0)
    cx = table_x
    for label, frac in cols:
        c.setFont(LATIN_B, 9)
        c.setFillColor(SUBTLE)
        c.drawString(cx + 12, y - 18, label)
        cx += table_w * frac
    y -= 28
    hline(c, table_x, y, table_x + table_w, color=LINE, w=0.6)

    # Rows
    for i, row in enumerate(picker_rows):
        body_h = 36
        if i % 2 == 0:
            c.setFillColor(Color(1, 1, 1, alpha=0.025))
            c.rect(table_x, y - body_h, table_w, body_h, fill=1, stroke=0)
        cx = table_x
        for (label, frac), val in zip(cols, row):
            tx = cx + 12
            if label == "RECOMMENDED":
                c.setFont(LATIN_B, 11)
                c.setFillColor(ACCENT)
            else:
                c.setFont(LATIN, 10.5)
                c.setFillColor(white)
            c.drawString(tx, y - 22, val)
            cx += table_w * frac
        y -= body_h
        hline(c, table_x, y, table_x + table_w, color=LINE, w=0.4)

    # CTA card
    y -= 36
    card_h = 130
    c.setFillColor(BLUE)
    c.roundRect(MARGIN, y - card_h, W - 2 * MARGIN, card_h, 12, fill=1, stroke=0)
    c.setFont(LATIN_B, 14)
    c.setFillColor(white)
    c.drawString(MARGIN + 24, y - 30, "Free site assessment, 24-hour response")
    c.setFont(CJK, 12)
    c.drawString(MARGIN + 24, y - 50, "免費場地評估 · 一個工作天回覆")
    c.setFont(LATIN, 10)
    c.setFillColor(Color(1, 1, 1, alpha=0.9))
    cta_lines = _wrap("Tell us your floor area, ceiling height, target RH and timeline. A Hong Kong engineer will reply with model recommendation, pricing, lead-time, and a site survey appointment.", 88)
    for i, line in enumerate(cta_lines):
        c.drawString(MARGIN + 24, y - 70 - i * 14, line)
    c.setFont(LATIN_B, 11)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN + 24, y - card_h + 16, "→ www.erv.hk/#quote   ·   WhatsApp +852 8404 3880   ·   erv@erv.hk")

    c.showPage()

def _wrap(text, width):
    """Naive word-wrap for Latin text."""
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
    """Wrap CJK by character count."""
    return [text[i:i + width] for i in range(0, len(text), width)]

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
          ["GEC30V", "GEC50V", "GEC70V", "GEC110V"], "30–110 L/day")

    overview_page(c, 2, total, series_label, "GEC V",
                  "The GEC V Series is the flagship fresh-air ceiling dehumidifier engineered for Hong Kong's sub-tropical climate. It maintains target humidity while continuously introducing HEPA-filtered outdoor air — solving CO2 build-up, PM2.5, cooking odours, and humidity in a single concealed unit. The 5-in-1 air detector reads PM2.5, CO2, VOC, temperature, and relative humidity, switching modes automatically.",
                  "GEC V 系列為 ERV.hk 旗艦新風天花式抽濕機，專為香港氣候研發。在維持空間濕度的同時，引入經 HEPA 過濾的潔淨新風 — 一機解決室內 CO2 累積、PM2.5、烹飪異味與潮濕問題。內置五合一空氣探測器自動偵測 PM2.5、CO2、VOC、溫度與濕度，並於四個模式之間智能切換。",
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
                  ])

    specs_page(c, 3, total, series_label, "GEC V",
               models=[
                   {"name": "GEC30V", "specs": {
                       "capacity": "30 L/day",
                       "fresh_air": "0–170 CMH",
                       "coverage": "200–400 sq ft",
                       "airflow": "350 CMH",
                       "noise": "38–50 dB(A)",
                       "dim": "992 × 526 × 245",
                       "weight": "39 kg",
                       "power": "230V / 50Hz",
                   }},
                   {"name": "GEC50V", "tag": "BESTSELLER", "specs": {
                       "capacity": "50 L/day",
                       "fresh_air": "0–225 CMH",
                       "coverage": "400–600 sq ft",
                       "airflow": "450 CMH",
                       "noise": "42–50 dB(A)",
                       "dim": "1004 × 560 × 255",
                       "weight": "52 kg",
                       "power": "230V / 50Hz",
                   }},
                   {"name": "GEC70V", "specs": {
                       "capacity": "70 L/day",
                       "fresh_air": "0–250 CMH",
                       "coverage": "600–800 sq ft",
                       "airflow": "500 CMH",
                       "noise": "45–50 dB(A)",
                       "dim": "1032 × 626 × 265",
                       "weight": "60 kg",
                       "power": "230V / 50Hz",
                   }},
                   {"name": "GEC110V", "specs": {
                       "capacity": "110 L/day",
                       "fresh_air": "0–450 CMH",
                       "coverage": "800–1200 sq ft",
                       "airflow": "900 CMH",
                       "noise": "45–50 dB(A)",
                       "dim": "1200 × 795 × 284",
                       "weight": "71 kg",
                       "power": "230V / 50Hz",
                   }},
               ],
               columns=[
                   ("capacity",   "Dehumidification",  "抽濕量"),
                   ("fresh_air",  "Fresh-air volume",  "新風量"),
                   ("coverage",   "Coverage",          "適用面積"),
                   ("airflow",    "Airflow",           "風量"),
                   ("noise",      "Noise",             "噪音"),
                   ("dim",        "Dimensions (mm)",   "尺寸"),
                   ("weight",     "Weight",            "重量"),
                   ("power",      "Power supply",      "電源"),
               ])

    picker_page(c, 4, total, series_label, "GEC V",
                picker_rows=[
                    ("Studio / 1-bed", "200–400 sq ft",    "GEC30V",  "Single zone"),
                    ("2-bed flat",     "400–600 sq ft",    "GEC50V",  "Whole-home"),
                    ("3-bed flat",     "600–800 sq ft",    "GEC70V",  "Whole-home"),
                    ("Duplex / large", "800–1,200 sq ft",  "GEC110V", "Multi-zone duct"),
                    ("Hotel suite",    "400–700 sq ft",    "GEC50V",  "Per-suite quiet"),
                    ("Clubhouse / gym","800+ sq ft",       "GEC110V", "High fresh-air"),
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
          ["UTC20", "UTC68", "UTC120"], "20–120 L/day")

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
                  ])

    specs_page(c, 3, total, series_label, "UTC",
               models=[
                   {"name": "UTC20", "tag": "ENERGY GRADE 1", "specs": {
                       "capacity": "20 L/day",
                       "coverage": "200–400 sq ft",
                       "airflow": "220 CMH",
                       "noise": "39 dB(A)",
                       "thickness": "200 mm",
                       "dim": "865 × 376 × 200",
                       "weight": "28 kg",
                       "power": "230V / 50Hz",
                   }},
                   {"name": "UTC68", "specs": {
                       "capacity": "68 L/day",
                       "coverage": "800–1000 sq ft",
                       "airflow": "500 CMH",
                       "noise": "48 dB(A)",
                       "thickness": "240 mm",
                       "dim": "1010 × 500 × 240",
                       "weight": "42 kg",
                       "power": "230V / 50Hz",
                   }},
                   {"name": "UTC120", "specs": {
                       "capacity": "120 L/day",
                       "coverage": "1300–1500 sq ft",
                       "airflow": "890 CMH",
                       "noise": "50 dB(A)",
                       "thickness": "310 mm",
                       "dim": "1075 × 746 × 310",
                       "weight": "64 kg",
                       "power": "230V / 50Hz",
                   }},
               ],
               columns=[
                   ("capacity",   "Dehumidification",  "抽濕量"),
                   ("coverage",   "Coverage",          "適用面積"),
                   ("airflow",    "Airflow",           "風量"),
                   ("noise",      "Noise",             "噪音"),
                   ("thickness",  "Profile thickness", "厚度"),
                   ("dim",        "Dimensions (mm)",   "尺寸"),
                   ("weight",     "Weight",            "重量"),
                   ("power",      "Power supply",      "電源"),
               ])

    picker_page(c, 4, total, series_label, "UTC",
                picker_rows=[
                    ("Bedroom",            "200–300 sq ft",   "UTC20",  "Quiet, slim"),
                    ("Studio / 1-bed",     "200–400 sq ft",   "UTC20",  "HK Grade 1"),
                    ("2–3 bed flat",       "600–1,000 sq ft", "UTC68",  "Pump drainage"),
                    ("Duplex / large",     "1,000+ sq ft",    "UTC120", "Multi-zone"),
                    ("Wine storage room",  "any",             "UTC20",  "Stable RH"),
                    ("Office / clubhouse", "1,000+ sq ft",    "UTC120", "BMS-ready"),
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
          ["GEC68LD-HP", "GEC145LD-HP", "GEC280LD", "GEC400LD", "GEC550LD"], "68–550 L/day")

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
                  ])

    specs_page(c, 3, total, series_label, "GEC",
               models=[
                   {"name": "GEC68LD-HP", "specs": {
                       "capacity": "68 L/day",
                       "coverage": "800–1,000 sq ft",
                       "airflow": "500 CMH",
                       "static": "30 Pa",
                       "dim": "970 × 525 × 345",
                       "phase": "1ph 230V",
                   }},
                   {"name": "GEC145LD-HP", "specs": {
                       "capacity": "145 L/day",
                       "coverage": "1,500–1,700 sq ft",
                       "airflow": "1,200 CMH",
                       "static": "50 Pa",
                       "dim": "1,005 × 695 × 440",
                       "phase": "1ph 230V",
                   }},
                   {"name": "GEC280LD", "specs": {
                       "capacity": "280 L/day",
                       "coverage": "2,500–3,000 sq ft",
                       "airflow": "1,700 CMH",
                       "static": "60 Pa",
                       "dim": "1,137 × 900 × 540",
                       "phase": "3ph 380V",
                   }},
                   {"name": "GEC400LD", "specs": {
                       "capacity": "400 L/day",
                       "coverage": "3,000–4,000 sq ft",
                       "airflow": "3,250 CMH",
                       "static": "80 Pa",
                       "dim": "1,270 × 1,200 × 605",
                       "phase": "3ph 380V",
                   }},
                   {"name": "GEC550LD", "specs": {
                       "capacity": "550 L/day",
                       "coverage": "4,000–5,000 sq ft",
                       "airflow": "3,250 CMH",
                       "static": "80 Pa",
                       "dim": "1,270 × 1,200 × 605",
                       "phase": "3ph 380V",
                   }},
               ],
               columns=[
                   ("capacity",  "Dehumidification",  "抽濕量"),
                   ("coverage",  "Coverage",          "適用面積"),
                   ("airflow",   "Airflow",           "風量"),
                   ("static",    "External static",   "外靜壓"),
                   ("dim",       "Dimensions (mm)",   "尺寸"),
                   ("phase",     "Power supply",      "電源"),
               ])

    picker_page(c, 4, total, series_label, "GEC",
                picker_rows=[
                    ("Small office / retail",  "800–1,000 sq ft",   "GEC68LD-HP",  "Single zone"),
                    ("Open-plan office",       "1,500–1,700 sq ft", "GEC145LD-HP", "BMS-ready"),
                    ("Showroom / hall",        "2,500–3,000 sq ft", "GEC280LD",    "3-phase"),
                    ("Banquet / clubhouse",    "3,000–4,000 sq ft", "GEC400LD",    "High static"),
                    ("Indoor pool / hangar",   "4,000–5,000 sq ft", "GEC550LD",    "Maximum"),
                    ("Multi-zone hotel floor", "Custom",            "GEC400LD x N","Per-zone duct"),
                ])

    c.save()
    print(f"Wrote {out}")


if __name__ == "__main__":
    gen_gec_v()
    gen_utc()
    gen_gec_commercial()
