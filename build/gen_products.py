#!/usr/bin/env python3
"""Generate all product subpages for ERV.hk from a single template.
Specs sourced from DBA-HK 2025 catalogs and dba.hk Shopify product pages."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "products"
OUT.mkdir(parents=True, exist_ok=True)

PRODUCTS = [
    # ===== GEC V (Fresh Air Series) — 4 models, real catalog specs =====
    {
        "sku": "DBA-GEC30V",
        "image": "ceiling-dba-gec30v.jpg",
        "series_eyebrow_zh": "新風淨化天花式抽濕機 · GEC V 系列",
        "series_eyebrow_en": "Fresh-air ceiling dehumidifier · GEC V Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "新風 + 抽濕 + 過濾。為細小空間而設。",
        "headline_en": "Fresh air + dehumidify + filter. Sized for compact spaces.",
        "sub_zh": "200-400 平方呎住宅或一房戶之選。新風量達 170 CMH，五合一空氣探測器自動於四個模式 (抽濕 / 新風 / 混合 / 智能) 之間切換，38 dB(A) 低噪音運作。",
        "sub_en": "Built for 200-400 sq ft flats and single-bedroom units. Up to 170 CMH fresh-air, 5-in-1 air detector auto-switches across four modes (dehumidify / fresh-air / mixed / intelligent), 38 dB(A) low-noise operation.",
        "quick": [("適用面積", "Coverage", "200-400 sq ft"), ("新風量", "Fresh air", "0-170 CMH"), ("抽濕量", "Capacity", "30 L/day"), ("噪音", "Noise", "38/50 dB(A)")],
        "specs": [
            ("型號", "Model", "DBA-GEC30V"),
            ("類型", "Type", "新風淨化天花式抽濕機 / Fresh-air ceiling dehumidifier"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "30 L / day"),
            ("抽濕量 (26.7°C 60% RH)", "Capacity (26.7°C 60% RH)", "10.8 L / day"),
            ("新風量", "Fresh-air supply", "0-170 CMH"),
            ("室內循環風量", "Indoor airflow", "350 CMH"),
            ("適用面積", "Coverage", "200-400 sq ft"),
            ("運作噪音 (3m)", "Noise level (3m)", "38/50 dB(A)"),
            ("靜壓", "Static pressure", "100 Pa"),
            ("額定 / 最大功率", "Rated / Max power", "330 W / 440 W"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "992 × 526 × 245 mm"),
            ("重量", "Weight", "39 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("水泵揚程", "Drain pump head", "1.2 m"),
            ("出/入風口", "Air outlet/inlet", "⌀146 mm / ⌀146 mm × 2"),
            ("冷媒", "Refrigerant", "R134a / 260 g"),
            ("過濾", "Filtration", "HEPA + 不銹鋼網目 / HEPA + stainless mesh"),
            ("控制", "Control", "86×86mm LCD 觸控屏 / LCD touch panel"),
            ("通訊", "Connectivity", "RS485 Modbus + 乾接點 / Dry contact"),
        ],
        "related": ["DBA-GEC50V", "DBA-GEC70V", "DBA-UTC68"],
    },
    {
        "sku": "DBA-GEC50V",
        "image": "ceiling-dba-gec50v.jpg",
        "series_eyebrow_zh": "新風淨化天花式抽濕機 · GEC V 系列",
        "series_eyebrow_en": "Fresh-air ceiling dehumidifier · GEC V Series",
        "tag_zh": "暢銷", "tag_en": "BESTSELLER",
        "headline_zh": "中型住宅之選。香港最受歡迎機型。",
        "headline_en": "Mid-size flats. Our most popular model.",
        "sub_zh": "400-600 平方呎中型住宅、會所及辦公室之選。新風量 0-225 CMH 配合 50 公升 / 日抽濕，HEPA 過濾、五合一空氣探測、LCD 觸控屏全配。",
        "sub_en": "The right fit for 400-600 sq ft mid-size flats, clubhouses, and offices. 0-225 CMH fresh-air paired with 50 L/day dehumidification. HEPA, 5-in-1 sensor, and LCD touch panel standard.",
        "quick": [("適用面積", "Coverage", "400-600 sq ft"), ("新風量", "Fresh air", "0-225 CMH"), ("抽濕量", "Capacity", "50 L/day"), ("噪音", "Noise", "42/50 dB(A)")],
        "specs": [
            ("型號", "Model", "DBA-GEC50V"),
            ("類型", "Type", "新風淨化天花式抽濕機 / Fresh-air ceiling dehumidifier"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "50 L / day"),
            ("抽濕量 (26.7°C 60% RH)", "Capacity (26.7°C 60% RH)", "26.4 L / day"),
            ("新風量", "Fresh-air supply", "0-225 CMH"),
            ("室內循環風量", "Indoor airflow", "450 CMH"),
            ("適用面積", "Coverage", "400-600 sq ft"),
            ("運作噪音 (3m)", "Noise level (3m)", "42/50 dB(A)"),
            ("靜壓", "Static pressure", "100 Pa"),
            ("額定 / 最大功率", "Rated / Max power", "520 W / 780 W"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "1,004 × 560 × 255 mm"),
            ("重量", "Weight", "52 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("水泵揚程", "Drain pump head", "1.2 m"),
            ("出/入風口", "Air outlet/inlet", "⌀146 mm / ⌀146 mm × 2"),
            ("冷媒", "Refrigerant", "R410A / 400 g"),
            ("過濾", "Filtration", "HEPA + 不銹鋼網目 / HEPA + stainless mesh"),
            ("控制", "Control", "86×86mm LCD 觸控屏 / LCD touch panel"),
            ("通訊", "Connectivity", "RS485 Modbus + 乾接點 / Dry contact"),
        ],
        "related": ["DBA-GEC30V", "DBA-GEC70V", "DBA-GEC110V"],
    },
    {
        "sku": "DBA-GEC70V",
        "image": "ceiling-dba-gec70v.jpg",
        "series_eyebrow_zh": "新風淨化天花式抽濕機 · GEC V 系列",
        "series_eyebrow_en": "Fresh-air ceiling dehumidifier · GEC V Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "大型住宅 · 多房間管道分送。",
        "headline_en": "Large homes. Multi-room duct distribution.",
        "sub_zh": "600-800 平方呎住宅及會所之選。新風量 0-250 CMH，抽濕 70 公升 / 日，可外接管道分送多個房間。直流無刷變頻電機節能耐用。",
        "sub_en": "For 600-800 sq ft homes and clubhouses. 0-250 CMH fresh-air, 70 L/day dehumidification, ducted distribution to multiple rooms. DC brushless inverter motor for efficiency and longevity.",
        "quick": [("適用面積", "Coverage", "600-800 sq ft"), ("新風量", "Fresh air", "0-250 CMH"), ("抽濕量", "Capacity", "70 L/day"), ("噪音", "Noise", "45/50 dB(A)")],
        "specs": [
            ("型號", "Model", "DBA-GEC70V"),
            ("類型", "Type", "新風淨化天花式抽濕機 / Fresh-air ceiling dehumidifier"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "70 L / day"),
            ("抽濕量 (26.7°C 60% RH)", "Capacity (26.7°C 60% RH)", "33.6 L / day"),
            ("新風量", "Fresh-air supply", "0-250 CMH"),
            ("室內循環風量", "Indoor airflow", "500 CMH"),
            ("適用面積", "Coverage", "600-800 sq ft"),
            ("運作噪音 (3m)", "Noise level (3m)", "45/50 dB(A)"),
            ("靜壓", "Static pressure", "100 Pa"),
            ("額定 / 最大功率", "Rated / Max power", "850 W / 1,150 W"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "1,032 × 626 × 265 mm"),
            ("重量", "Weight", "60 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("水泵揚程", "Drain pump head", "1.2 m"),
            ("出/入風口", "Air outlet/inlet", "⌀146 mm / ⌀146 mm × 2"),
            ("冷媒", "Refrigerant", "R134a / 550 g"),
            ("過濾", "Filtration", "HEPA + 不銹鋼網目 / HEPA + stainless mesh"),
            ("通訊", "Connectivity", "RS485 Modbus + 乾接點 / Dry contact"),
        ],
        "related": ["DBA-GEC50V", "DBA-GEC110V", "DBA-THC35"],
    },
    {
        "sku": "DBA-GEC110V",
        "image": "ceiling-dba-gec110v.jpg",
        "series_eyebrow_zh": "新風淨化天花式抽濕機 · GEC V 系列",
        "series_eyebrow_en": "Fresh-air ceiling dehumidifier · GEC V Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "大宅、會所、辦公室。GEC V 系列旗艦。",
        "headline_en": "Large residences, clubhouses, offices. GEC V flagship.",
        "sub_zh": "800-1,200 平方呎大型住宅、酒店套房及辦公室之選。新風量達 450 CMH，抽濕 110 公升 / 日，⌀196mm 大型風口配大型管道分送多個房間。",
        "sub_en": "For 800-1,200 sq ft large homes, hotel suites, and offices. Up to 450 CMH fresh-air, 110 L/day dehumidification, ⌀196mm flanges support large ducts and multi-room distribution.",
        "quick": [("適用面積", "Coverage", "800-1,200 sq ft"), ("新風量", "Fresh air", "0-450 CMH"), ("抽濕量", "Capacity", "110 L/day"), ("風量", "Airflow", "900 CMH")],
        "specs": [
            ("型號", "Model", "DBA-GEC110V"),
            ("類型", "Type", "新風淨化天花式抽濕機 / Fresh-air ceiling dehumidifier"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "110 L / day"),
            ("抽濕量 (26.7°C 60% RH)", "Capacity (26.7°C 60% RH)", "52.8 L / day"),
            ("新風量", "Fresh-air supply", "0-450 CMH"),
            ("室內循環風量", "Indoor airflow", "900 CMH"),
            ("適用面積", "Coverage", "800-1,200 sq ft"),
            ("運作噪音 (3m)", "Noise level (3m)", "45/50 dB(A)"),
            ("靜壓", "Static pressure", "100 Pa"),
            ("額定 / 最大功率", "Rated / Max power", "1,020 W / 1,415 W"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "1,200 × 795 × 284 mm"),
            ("重量", "Weight", "71 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("水泵揚程", "Drain pump head", "1.2 m"),
            ("出/入風口", "Air outlet/inlet", "⌀196 mm / ⌀196 mm × 2"),
            ("冷媒", "Refrigerant", "R410A / 900 g"),
            ("過濾", "Filtration", "HEPA + 不銹鋼網目 / HEPA + stainless mesh"),
            ("通訊", "Connectivity", "RS485 Modbus + 乾接點 / Dry contact"),
        ],
        "related": ["DBA-GEC70V", "DBA-THC50", "DBA-UTC120"],
    },
    # ===== THC (Climate Control Unit) — 3 models, real specs from dba.hk =====
    {
        "sku": "DBA-THC35",
        "image": "ceiling-dba-thc35.jpg",
        "series_eyebrow_zh": "恆溫恆濕氣候控制機 · THC 系列",
        "series_eyebrow_en": "Climate control unit · THC Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "一機代替冷氣 + 抽濕機 + 加濕器。",
        "headline_en": "One machine replaces AC + dehumidifier + humidifier.",
        "sub_zh": "DBA THC 系列入門款。製冷 3.5 kW、PTC 加熱 3.8 kW、加濕 1.2 kg/小時，內置抽濕功能 — 同時自動調節溫度與濕度，WiFi 智能控制。",
        "sub_en": "The entry-level DBA THC unit. 3.5 kW cooling, 3.8 kW PTC heating, 1.2 kg/hr humidification, plus dehumidification — automatic temperature + humidity control with WiFi.",
        "quick": [("製冷", "Cooling", "3.5 kW"), ("製熱", "Heating", "3.8 kW (PTC)"), ("加濕", "Humidify", "1.2 kg/hr"), ("風量", "Airflow", "650 CMH")],
        "specs": [
            ("型號", "Model", "DBA-THC35"),
            ("類型", "Type", "恆溫恆濕氣候控制機 / Climate control unit"),
            ("製冷能力", "Cooling capacity", "3.5 kW (3,500 W)"),
            ("製熱能力 (PTC)", "Heating capacity (PTC)", "3.8 kW (3,800 W)"),
            ("加濕量", "Humidification", "1.2 kg / hr"),
            ("抽濕功能", "Dehumidification", "✓"),
            ("風量", "Airflow", "650 CMH"),
            ("運作噪音", "Noise level", "50 dB(A)"),
            ("室內機尺寸", "Indoor unit dimensions", "1,000 × 585 × 240 mm"),
            ("室內機重量", "Indoor unit weight", "35.5 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("冷媒", "Refrigerant", "R410A / 1,300 g"),
            ("控制", "Control", "WiFi 智能 + LCD / WiFi smart + LCD"),
            ("通訊", "Connectivity", "RS485 Modbus BMS"),
        ],
        "related": ["DBA-THC50", "DBA-THC66", "DBA-GEC50V"],
    },
    {
        "sku": "DBA-THC50",
        "image": "ceiling-dba-thc50.jpg",
        "series_eyebrow_zh": "恆溫恆濕氣候控制機 · THC 系列",
        "series_eyebrow_en": "Climate control unit · THC Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "中型恆溫恆濕。EER 高達 3.22。",
        "headline_en": "Mid-size climate control. EER up to 3.22.",
        "sub_zh": "5.0 kW 製冷 + 5.0 kW PTC 加熱 + 1.5 kg/小時加濕，分體式設計 (室內機 + 室外機)。EER 3.22、COP 3.2 — 比傳統「冷氣 + 抽濕 + 加濕」三件組合更省電。",
        "sub_en": "5.0 kW cooling + 5.0 kW PTC heating + 1.5 kg/hr humidification in a split-system design (indoor + outdoor). EER 3.22 and COP 3.2 — more efficient than the traditional AC + dehumidifier + humidifier stack.",
        "quick": [("製冷", "Cooling", "5.0 kW"), ("製熱", "Heating", "5.0 kW (PTC)"), ("加濕", "Humidify", "1.5 kg/hr"), ("EER / COP", "EER / COP", "3.22 / 3.2")],
        "specs": [
            ("型號", "Model", "DBA-THC50"),
            ("類型", "Type", "恆溫恆濕氣候控制機 (分體式) / Climate control unit (split-system)"),
            ("製冷能力", "Cooling capacity", "5.0 kW (5,000 W)"),
            ("製熱能力 (PTC)", "Heating capacity (PTC)", "5.0 kW (5,000 W)"),
            ("加濕量", "Humidification", "1.5 kg / hr"),
            ("抽濕功能", "Dehumidification", "✓"),
            ("風量", "Airflow", "650 CMH"),
            ("EER", "EER", "3.22"),
            ("COP", "COP", "3.2"),
            ("運作噪音", "Noise level", "50 dB(A)"),
            ("室內機尺寸", "Indoor unit dimensions", "1,000 × 585 × 240 mm"),
            ("室外機尺寸", "Outdoor unit dimensions", "802 × 564 × 323 mm"),
            ("室內機重量", "Indoor unit weight", "35.5 kg"),
            ("室外機重量", "Outdoor unit weight", "34 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("冷媒", "Refrigerant", "R410A / 1,300 g"),
            ("控制", "Control", "WiFi 智能 + LCD / WiFi smart + LCD"),
            ("通訊", "Connectivity", "RS485 Modbus BMS"),
        ],
        "related": ["DBA-THC35", "DBA-THC66", "DBA-GEC70V"],
    },
    {
        "sku": "DBA-THC66",
        "image": "ceiling-dba-thc66.jpg",
        "series_eyebrow_zh": "恆溫恆濕氣候控制機 · THC 系列",
        "series_eyebrow_en": "Climate control unit · THC Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "大型恆溫恆濕。為大宅與商業空間。",
        "headline_en": "Large climate control. For mansions and commercial spaces.",
        "sub_zh": "THC 系列旗艦。7.0 kW 製冷 + 7.4 kW PTC 加熱 + 2.0 kg/小時加濕，1,300 CMH 大風量、IPX4 防水等級、50 Pa 外靜壓 — 適合大宅、酒窖、畫廊、錄音室及小型商業空間。",
        "sub_en": "THC flagship. 7.0 kW cooling + 7.4 kW PTC heating + 2.0 kg/hr humidification, 1,300 CMH airflow, IPX4 rated, 50 Pa external static — for mansions, wine cellars, galleries, studios, and small commercial spaces.",
        "quick": [("製冷", "Cooling", "7.0 kW"), ("製熱", "Heating", "7.4 kW (PTC)"), ("加濕", "Humidify", "2.0 kg/hr"), ("風量", "Airflow", "1,300 CMH")],
        "specs": [
            ("型號", "Model", "DBA-THC66"),
            ("類型", "Type", "恆溫恆濕氣候控制機 (分體式) / Climate control unit (split-system)"),
            ("製冷能力", "Cooling capacity", "7.0 kW (7,000 W)"),
            ("製熱能力 (PTC)", "Heating capacity (PTC)", "7.4 kW (7,400 W)"),
            ("加濕量", "Humidification", "2.0 kg / hr"),
            ("抽濕功能", "Dehumidification", "✓"),
            ("風量", "Airflow", "1,300 CMH"),
            ("外靜壓", "External static pressure", "50 Pa"),
            ("EER", "EER", "3.02"),
            ("COP", "COP", "3.2"),
            ("最大功率", "Max power", "3,500 W + 2,000 W (PTC)"),
            ("運作噪音 (室內)", "Noise (indoor)", "55 dB(A)"),
            ("運作噪音 (室外)", "Noise (outdoor)", "60 dB(A)"),
            ("防水等級", "IP rating", "IPX4"),
            ("室內機尺寸", "Indoor unit dimensions", "1,000 × 585 × 240 mm"),
            ("室外機尺寸", "Outdoor unit dimensions", "900 × 700 × 337 mm"),
            ("室內機重量", "Indoor unit weight", "37 kg"),
            ("室外機重量", "Outdoor unit weight", "45 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("冷媒", "Refrigerant", "R410A / 1,600 g"),
            ("控制", "Control", "WiFi 智能 / WiFi smart"),
            ("通訊", "Connectivity", "RS485 Modbus BMS"),
        ],
        "related": ["DBA-THC50", "DBA-THC35", "DBA-GEC110V"],
    },
    # ===== UTC (Ultra Thin Series) — 3 models, real catalog specs =====
    {
        "sku": "DBA-UTC20",
        "image": "ceiling-dba-utc20-1.jpg",
        "series_eyebrow_zh": "超薄天花式抽濕機 · UTC 系列",
        "series_eyebrow_en": "Ultra-thin ceiling dehumidifier · UTC Series",
        "tag_zh": "一級能源", "tag_en": "GRADE 1",
        "headline_zh": "200mm 超薄。香港一級能源標籤。",
        "headline_en": "200 mm slim. Hong Kong Grade 1 Energy Label.",
        "sub_zh": "細小空間的精準抽濕。200mm 超薄機身，39 dB(A) 比安靜對話更輕，獲香港一級能源標籤認證。適合主人房、儲物室及衣帽間。",
        "sub_en": "Precision dehumidification for small spaces. 200 mm ultra-slim body, 39 dB(A) operation quieter than a hushed conversation, Hong Kong Grade 1 Energy Label certified. Ideal for master bedrooms, store rooms, and walk-in closets.",
        "quick": [("適用面積", "Coverage", "200-400 sq ft"), ("抽濕量", "Capacity", "20 L/day"), ("噪音", "Noise", "39 dB(A)"), ("厚度", "Thickness", "200 mm")],
        "specs": [
            ("型號", "Model", "DBA-UTC20"),
            ("類型", "Type", "超薄天花式抽濕機 / Ultra-thin ceiling dehumidifier"),
            ("能源標籤", "Energy label", "香港一級 / Hong Kong Grade 1"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "20 L / day"),
            ("抽濕量 (26.7°C 60% RH)", "Capacity (26.7°C 60% RH)", "9.9 L / day"),
            ("風量", "Airflow", "220 CMH"),
            ("適用面積", "Coverage", "200-400 sq ft"),
            ("運作噪音 (3m)", "Noise level (3m)", "39 dB(A)"),
            ("靜壓", "Static pressure", "80 Pa"),
            ("額定 / 最大功率", "Rated / Max power", "196 W / 300 W"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "865 × 376 × 200 mm"),
            ("重量", "Weight", "28 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("水泵揚程", "Drain pump head", "1.8 m"),
            ("出/入風口", "Air outlet/inlet", "⌀146 mm"),
            ("冷媒", "Refrigerant", "R134a / 230 g"),
            ("殺菌", "Sterilisation", "UV-C 紫外線 / UV-C lamp"),
            ("通訊", "Connectivity", "WiFi App + RS485 Modbus"),
        ],
        "related": ["DBA-UTC68", "DBA-UTC120", "DBA-GEC30V"],
    },
    {
        "sku": "DBA-UTC68",
        "image": "ceiling-dba-utc68-1.jpg",
        "series_eyebrow_zh": "超薄天花式抽濕機 · UTC 系列",
        "series_eyebrow_en": "Ultra-thin ceiling dehumidifier · UTC Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "中型住宅 · 一台搞掂全屋。",
        "headline_en": "Whole-home humidity from one ceiling unit.",
        "sub_zh": "一台 UTC68 即可分送乾爽空氣至 800-1,000 平方呎多個房間。240mm 安裝高度、48 dB(A) 低噪音、500 CMH 風量。WiFi App + RS485 BMS 標配。",
        "sub_en": "A single UTC68 distributes dry air to 800-1,000 sq ft across multiple rooms. 240 mm install height, 48 dB(A) noise, 500 CMH airflow. WiFi App + RS485 BMS standard.",
        "quick": [("適用面積", "Coverage", "800-1,000 sq ft"), ("抽濕量", "Capacity", "68 L/day"), ("風量", "Airflow", "500 CMH"), ("噪音", "Noise", "48 dB(A)")],
        "specs": [
            ("型號", "Model", "DBA-UTC68"),
            ("類型", "Type", "超薄天花式抽濕機 / Ultra-thin ceiling dehumidifier"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "68 L / day"),
            ("抽濕量 (26.7°C 60% RH)", "Capacity (26.7°C 60% RH)", "42 L / day"),
            ("風量", "Airflow", "500 CMH"),
            ("適用面積", "Coverage", "800-1,000 sq ft"),
            ("運作噪音 (3m)", "Noise level (3m)", "48 dB(A)"),
            ("靜壓", "Static pressure", "100 Pa"),
            ("額定 / 最大功率", "Rated / Max power", "880 W / 1,250 W"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "1,010 × 500 × 240 mm"),
            ("重量", "Weight", "42 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("水泵揚程", "Drain pump head", "1.8 m"),
            ("出/入風口", "Air outlet/inlet", "⌀146 mm"),
            ("冷媒", "Refrigerant", "R410A / 600 g"),
            ("殺菌", "Sterilisation", "UV-C 紫外線 / UV-C lamp"),
            ("通訊", "Connectivity", "WiFi App + RS485 Modbus"),
        ],
        "related": ["DBA-UTC20", "DBA-UTC120", "DBA-GEC50V"],
    },
    {
        "sku": "DBA-UTC120",
        "image": "ceiling-dba-utc120-1.jpg",
        "series_eyebrow_zh": "超薄天花式抽濕機 · UTC 系列",
        "series_eyebrow_en": "Ultra-thin ceiling dehumidifier · UTC Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "大宅及複式單位。一台覆蓋 1,500 呎。",
        "headline_en": "1,500 sq ft of comfort from one ceiling.",
        "sub_zh": "適用於大宅、複式單位、會所主廳。310mm 厚度、890 CMH 大風量、120 公升 / 日抽濕量 — UTC 系列旗艦。",
        "sub_en": "Sized for large residences, duplexes, and clubhouse main halls. 310 mm thick, 890 CMH airflow, 120 L/day capacity — the UTC flagship.",
        "quick": [("適用面積", "Coverage", "1,300-1,500 sq ft"), ("抽濕量", "Capacity", "120 L/day"), ("風量", "Airflow", "890 CMH"), ("噪音", "Noise", "50 dB(A)")],
        "specs": [
            ("型號", "Model", "DBA-UTC120"),
            ("類型", "Type", "超薄天花式抽濕機 / Ultra-thin ceiling dehumidifier"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "120 L / day"),
            ("抽濕量 (26.7°C 60% RH)", "Capacity (26.7°C 60% RH)", "53 L / day"),
            ("風量", "Airflow", "890 CMH"),
            ("適用面積", "Coverage", "1,300-1,500 sq ft"),
            ("運作噪音 (3m)", "Noise level (3m)", "50 dB(A)"),
            ("靜壓", "Static pressure", "100 Pa"),
            ("額定 / 最大功率", "Rated / Max power", "1,010 W / 1,600 W"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "1,075 × 746 × 310 mm"),
            ("重量", "Weight", "64 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("水泵揚程", "Drain pump head", "1.8 m"),
            ("出/入風口", "Air outlet/inlet", "⌀196 mm"),
            ("冷媒", "Refrigerant", "R410A / 900 g"),
            ("殺菌", "Sterilisation", "UV-C 紫外線 / UV-C lamp"),
            ("通訊", "Connectivity", "WiFi App + RS485 Modbus"),
        ],
        "related": ["DBA-UTC68", "DBA-GEC110V", "DBA-THC50"],
    },
    # ===== GEC (Commercial Ceiling) — kept from earlier =====
    {
        "sku": "DBA-GEC68LD-HP",
        "image": "ceiling-dba-gec68ld-1.jpg",
        "series_eyebrow_zh": "商用天花抽濕機 · GEC 系列",
        "series_eyebrow_en": "Commercial ceiling · GEC Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "商用入門款。WiFi App + BMS 標配。",
        "headline_en": "Commercial entry-level. WiFi App + BMS standard.",
        "sub_zh": "中型商業空間入門選擇。68 公升 / 日抽濕、500 CMH 風量、覆蓋 800-1,000 平方呎。WiFi App 與 RS485 BMS 標配。",
        "sub_en": "An entry-level commercial unit for mid-size spaces. 68 L/day, 500 CMH airflow, 800-1,000 sq ft coverage. WiFi App and RS485 BMS standard.",
        "quick": [("適用面積", "Coverage", "800-1,000 sq ft"), ("抽濕量", "Capacity", "68 L/day"), ("風量", "Airflow", "500 CMH"), ("噪音", "Noise", "49 dB(A)")],
        "specs": [
            ("型號", "Model", "DBA-GEC68LD-HP"),
            ("類型", "Type", "商用天花抽濕機 / Commercial ceiling dehumidifier"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "68 L / day"),
            ("風量", "Airflow", "500 CMH"),
            ("適用面積", "Coverage", "800-1,000 sq ft"),
            ("運作噪音", "Noise level", "49 dB(A)"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "970 × 525 × 345 mm"),
            ("重量", "Weight", "44 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("殺菌", "Sterilisation", "UV-C 紫外線 / UV-C lamp"),
            ("通訊", "Connectivity", "WiFi App + RS485 Modbus"),
        ],
        "related": ["DBA-GEC145LD-HP", "DBA-GEC50V", "DBA-UTC68"],
    },
    {
        "sku": "DBA-GEC145LD-HP",
        "image": "ceiling-dba-gec145ld-1.jpg",
        "series_eyebrow_zh": "商用天花抽濕機 · GEC 系列",
        "series_eyebrow_en": "Commercial ceiling · GEC Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "商廈與會所核心機型。",
        "headline_en": "The workhorse for offices and clubhouses.",
        "sub_zh": "高靜壓設計，適合多區管道分送。1,500-1,700 平方呎覆蓋、1,200 CMH 風量、145 公升 / 日抽濕。",
        "sub_en": "High static-pressure design for ducted multi-zone distribution. 1,500-1,700 sq ft coverage, 1,200 CMH airflow, 145 L/day capacity.",
        "quick": [("適用面積", "Coverage", "1,500-1,700 sq ft"), ("抽濕量", "Capacity", "145 L/day"), ("風量", "Airflow", "1,200 CMH"), ("噪音", "Noise", "50 dB(A)")],
        "specs": [
            ("型號", "Model", "DBA-GEC145LD-HP"),
            ("類型", "Type", "商用天花抽濕機 / Commercial ceiling dehumidifier"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "145 L / day"),
            ("風量", "Airflow", "1,200 CMH"),
            ("適用面積", "Coverage", "1,500-1,700 sq ft"),
            ("運作噪音", "Noise level", "50 dB(A)"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "1,005 × 695 × 440 mm"),
            ("重量", "Weight", "70 kg"),
            ("電源", "Power supply", "220-240V / 50Hz"),
            ("殺菌", "Sterilisation", "UV-C 紫外線 / UV-C lamp"),
            ("通訊", "Connectivity", "RS485 Modbus"),
        ],
        "related": ["DBA-GEC68LD-HP", "DBA-GEC280LD", "DBA-THC66"],
    },
    {
        "sku": "DBA-GEC280LD",
        "image": "ceiling-dba-gec280ld-1.jpg",
        "series_eyebrow_zh": "商用天花抽濕機 · GEC 系列",
        "series_eyebrow_en": "Commercial ceiling · GEC Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "大型商廈與宴會廳。",
        "headline_en": "For large commercial floors and ballrooms.",
        "sub_zh": "三相電源、1,700 CMH 大風量、280 公升 / 日抽濕，覆蓋 2,500-3,000 平方呎。商廈、酒店宴會廳、大型會所適用。",
        "sub_en": "Three-phase power, 1,700 CMH airflow, 280 L/day capacity for 2,500-3,000 sq ft. Built for commercial floors, hotel ballrooms, and large clubhouses.",
        "quick": [("適用面積", "Coverage", "2,500-3,000 sq ft"), ("抽濕量", "Capacity", "280 L/day"), ("風量", "Airflow", "1,700 CMH"), ("噪音", "Noise", "58 dB(A)")],
        "specs": [
            ("型號", "Model", "DBA-GEC280LD"),
            ("類型", "Type", "商用天花抽濕機 / Commercial ceiling dehumidifier"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "280 L / day"),
            ("風量", "Airflow", "1,700 CMH"),
            ("適用面積", "Coverage", "2,500-3,000 sq ft"),
            ("運作噪音", "Noise level", "58 dB(A)"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "1,137 × 900 × 540 mm"),
            ("重量", "Weight", "108 kg"),
            ("電源", "Power supply", "380V 3N / 50Hz"),
            ("通訊", "Connectivity", "RS485 Modbus"),
        ],
        "related": ["DBA-GEC145LD-HP", "DBA-GEC400LD", "DBA-THC66"],
    },
    {
        "sku": "DBA-GEC400LD",
        "image": "ceiling-dba-gec400ld-1.jpg",
        "series_eyebrow_zh": "商用天花抽濕機 · GEC 系列",
        "series_eyebrow_en": "Commercial ceiling · GEC Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "工業級大空間方案。",
        "headline_en": "Industrial-grade large-space solution.",
        "sub_zh": "3,250 CMH 大風量、400 公升 / 日抽濕量，覆蓋 3,000-4,000 平方呎工業及大型商業空間。",
        "sub_en": "3,250 CMH airflow, 400 L/day capacity for 3,000-4,000 sq ft industrial and large commercial spaces.",
        "quick": [("適用面積", "Coverage", "3,000-4,000 sq ft"), ("抽濕量", "Capacity", "400 L/day"), ("風量", "Airflow", "3,250 CMH"), ("噪音", "Noise", "65 dB(A)")],
        "specs": [
            ("型號", "Model", "DBA-GEC400LD"),
            ("類型", "Type", "商用天花抽濕機 / Commercial ceiling dehumidifier"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "400 L / day"),
            ("風量", "Airflow", "3,250 CMH"),
            ("適用面積", "Coverage", "3,000-4,000 sq ft"),
            ("運作噪音", "Noise level", "65 dB(A)"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "1,270 × 1,200 × 605 mm"),
            ("重量", "Weight", "210 kg"),
            ("電源", "Power supply", "380V 3N / 50Hz"),
            ("通訊", "Connectivity", "RS485 Modbus"),
        ],
        "related": ["DBA-GEC280LD", "DBA-GEC550LD", "DBA-THC66"],
    },
    {
        "sku": "DBA-GEC550LD",
        "image": "ceiling-dba-gec550ld-1.jpg",
        "series_eyebrow_zh": "商用天花抽濕機 · GEC 系列",
        "series_eyebrow_en": "Commercial ceiling · GEC Series",
        "tag_zh": None, "tag_en": None,
        "headline_zh": "GEC 系列最大型號。",
        "headline_en": "The largest GEC ceiling unit.",
        "sub_zh": "550 公升 / 日抽濕，覆蓋 4,000-5,000 平方呎超大型空間。會展、酒店宴會大廳、室內運動場館適用。",
        "sub_en": "550 L/day for 4,000-5,000 sq ft venues — exhibition halls, large ballrooms, indoor sports facilities.",
        "quick": [("適用面積", "Coverage", "4,000-5,000 sq ft"), ("抽濕量", "Capacity", "550 L/day"), ("風量", "Airflow", "3,250 CMH"), ("噪音", "Noise", "65 dB(A)")],
        "specs": [
            ("型號", "Model", "DBA-GEC550LD"),
            ("類型", "Type", "商用天花抽濕機 / Commercial ceiling dehumidifier"),
            ("抽濕量 (30°C 80% RH)", "Capacity (30°C 80% RH)", "550 L / day"),
            ("風量", "Airflow", "3,250 CMH"),
            ("適用面積", "Coverage", "4,000-5,000 sq ft"),
            ("運作噪音", "Noise level", "65 dB(A)"),
            ("尺寸 (L × W × H)", "Dimensions (L × W × H)", "1,270 × 1,200 × 605 mm"),
            ("重量", "Weight", "240 kg"),
            ("電源", "Power supply", "380V 3N / 50Hz"),
            ("通訊", "Connectivity", "RS485 Modbus"),
        ],
        "related": ["DBA-GEC400LD", "DBA-GEC280LD", "DBA-THC66"],
    },
]


def slug(sku: str) -> str:
    return sku.lower()


def render_quick(quick):
    parts = []
    for zh, en, val in quick:
        parts.append(f'''        <div class="ph-quick-item">
          <div class="pq-label"><span lang-zh>{zh}</span><span lang-en>{en}</span></div>
          <div class="pq-value">{val}</div>
        </div>''')
    return "\n".join(parts)


def render_specs(specs):
    parts = []
    for zh, en, val in specs:
        parts.append(f'              <tr><td><span lang-zh>{zh}</span><span lang-en>{en}</span></td><td>{val}</td></tr>')
    return "\n".join(parts)


def render_related(related, all_products):
    by_sku = {p["sku"]: p for p in all_products}
    parts = []
    for sku in related:
        p = by_sku.get(sku)
        if not p:
            continue
        parts.append(f'''        <a href="{slug(p["sku"])}.html" class="ph-rel-card">
          <img src="../images/{p["image"]}" alt="{p["sku"]}" />
          <h4>{p["sku"]}</h4>
          <p><span lang-zh>{p["series_eyebrow_zh"]}</span><span lang-en>{p["series_eyebrow_en"]}</span></p>
          <span class="ph-rel-link"><span lang-zh>查看詳情 →</span><span lang-en>View details →</span></span>
        </a>''')
    return "\n".join(parts)


def render_tag(zh, en):
    if not zh:
        return ""
    return f'      <span class="ph-tag"><span lang-zh>{zh}</span><span lang-en>{en}</span></span>'


PAGE = """<!DOCTYPE html>
<html lang="zh-Hant" data-lang="zh">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{sku} · {series_eyebrow_en} | ERV.hk</title>
  <meta name="description" content="{sku} — {sub_en}" />
  <link rel="canonical" href="https://www.erv.hk/products/{slug}.html" />
  <link rel="alternate" hreflang="zh-Hant" href="https://www.erv.hk/products/{slug}.html" />
  <link rel="alternate" hreflang="en" href="https://www.erv.hk/products/{slug}.html?lang=en" />

  <meta property="og:type" content="product" />
  <meta property="og:title" content="{sku} — ERV.hk" />
  <meta property="og:description" content="{sub_en}" />
  <meta property="og:url" content="https://www.erv.hk/products/{slug}.html" />
  <meta property="og:image" content="https://www.erv.hk/images/{image}" />

  <script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{sku}",
  "description": "{sub_en}",
  "brand": {{"@type": "Brand", "name": "DBA"}},
  "manufacturer": {{"@type": "Organization", "name": "Debiasia Green Technology (HK) Co. Ltd.", "url": "https://www.dba.hk"}},
  "category": "{series_eyebrow_en}",
  "image": "https://www.erv.hk/images/{image}",
  "sku": "{sku}"
  }}</script>
  <script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "ERV.hk", "item": "https://www.erv.hk/"}},
    {{"@type": "ListItem", "position": 2, "name": "Products", "item": "https://www.erv.hk/#products"}},
    {{"@type": "ListItem", "position": 3, "name": "{sku}", "item": "https://www.erv.hk/products/{slug}.html"}}
  ]
  }}</script>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+TC:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../style.css" />
  <link rel="stylesheet" href="../product.css" />
  <link rel="icon" type="image/svg+xml" href="../images/logo-erv.svg" />
</head>
<body class="product-page">

  <div class="top-bar">
    <div class="container">
      <div class="tb-left">
        <span class="tb-mute">
          <span lang-zh>香港 · 澳門 · 大灣區工程供應</span>
          <span lang-en>Hong Kong · Macau · Greater Bay Area</span>
        </span>
      </div>
      <div class="tb-right">
        <a href="https://wa.me/85284043880" target="_blank" rel="noopener">WhatsApp · +852 8404 3880</a>
        <div class="lang-switch" role="group" aria-label="Language">
          <button data-lang="zh" class="active">繁中</button>
          <button data-lang="en">EN</button>
        </div>
      </div>
    </div>
  </div>

  <nav id="nav">
    <div class="nav-inner">
      <a href="../index.html" class="logo"><img src="../images/logo-erv.svg" alt="ERV.hk" /></a>
      <ul class="nav-links">
        <li><a href="../index.html#system"><span lang-zh>系統</span><span lang-en>System</span></a></li>
        <li><a href="../index.html#technology"><span lang-zh>技術</span><span lang-en>Technology</span></a></li>
        <li><a href="../index.html#applications"><span lang-zh>應用</span><span lang-en>Applications</span></a></li>
        <li><a href="../index.html#products"><span lang-zh>產品</span><span lang-en>Products</span></a></li>
        <li><a href="../index.html#catalogs"><span lang-zh>型錄</span><span lang-en>Catalogs</span></a></li>
        <li><a href="../index.html#faq"><span lang-zh>常見問題</span><span lang-en>FAQ</span></a></li>
        <li><a href="../index.html#quote" class="nav-cta"><span lang-zh>免費諮詢</span><span lang-en>Get a quote</span></a></li>
      </ul>
      <button class="nav-mobile-btn" onclick="toggleNav()" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
    <ul class="mobile-nav" id="mobileNav">
      <li><a href="../index.html#products"><span lang-zh>產品</span><span lang-en>Products</span></a></li>
      <li><a href="../index.html#quote"><span lang-zh>免費諮詢</span><span lang-en>Get a quote</span></a></li>
    </ul>
  </nav>

  <div class="breadcrumb">
    <div class="container">
      <a href="../index.html">ERV.hk</a>
      <span class="sep">/</span>
      <a href="../index.html#products"><span lang-zh>產品</span><span lang-en>Products</span></a>
      <span class="sep">/</span>
      <span class="bc-current">{sku}</span>
    </div>
  </div>

  <section class="ph-hero">
    <div class="container">
      <div class="ph-grid">
        <div class="ph-copy">
          <p class="ph-eyebrow"><span lang-zh>{series_eyebrow_zh}</span><span lang-en>{series_eyebrow_en}</span></p>
{tag_html}
          <h1>{sku}</h1>
          <p class="ph-sub">
            <span lang-zh>{headline_zh}</span>
            <span lang-en>{headline_en}</span>
          </p>
          <p class="ph-sub">
            <span lang-zh>{sub_zh}</span>
            <span lang-en>{sub_en}</span>
          </p>
          <div class="ph-quick">
{quick_html}
          </div>
          <div class="ph-actions">
            <a href="../index.html#quote" class="btn-pill"><span lang-zh>免費諮詢</span><span lang-en>Get a quote</span></a>
            <a href="https://wa.me/85284043880" class="btn-pill outline" target="_blank" rel="noopener">WhatsApp →</a>
          </div>
        </div>
        <div class="ph-visual">
          <img src="../images/{image}" alt="{sku}" />
        </div>
      </div>
    </div>
  </section>

  <section class="ph-highlights">
    <div class="container">
      <div class="ph-h-grid">
        <div class="ph-h-card">
          <div class="ph-h-icon">01</div>
          <h4><span lang-zh>天花隱藏式安裝</span><span lang-en>Hidden in the ceiling</span></h4>
          <p><span lang-zh>機身完全隱藏於假天花，只見出風口與回風口格柵，不影響室內裝修美感。</span><span lang-en>The unit disappears into the false ceiling — only the supply and return grilles are visible, preserving interior aesthetics.</span></p>
        </div>
        <div class="ph-h-card">
          <div class="ph-h-icon">02</div>
          <h4><span lang-zh>BMS 整合控制</span><span lang-en>BMS-ready control</span></h4>
          <p><span lang-zh>RS485 Modbus 通訊接口可直接接入樓宇 BMS — 集中設定、溫濕度監測、故障警報。</span><span lang-en>RS485 Modbus integrates directly with building BMS for centralised setpoints, telemetry, and alarms.</span></p>
        </div>
        <div class="ph-h-card">
          <div class="ph-h-icon">03</div>
          <h4><span lang-zh>香港售後保障</span><span lang-en>Hong Kong support</span></h4>
          <p><span lang-zh>原廠 1 年保養 (壓縮機 3 年)，香港工程隊負責安裝、調試、保養及維修。CE / CB / ISO 9001 / RoHS 認證。</span><span lang-en>1-year warranty (3-year compressor). Hong Kong engineering team for install, commissioning, service, and repair. CE / CB / ISO 9001 / RoHS certified.</span></p>
        </div>
      </div>
    </div>
  </section>

  <section class="ph-specs">
    <div class="container">
      <div class="ph-spec-wrap">
        <h2><span lang-zh>完整技術規格</span><span lang-en>Full specifications</span></h2>
        <table class="ph-spec-table">
{specs_html}
        </table>
      </div>
    </div>
  </section>

  <section class="ph-related">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow"><span lang-zh>相關型號</span><span lang-en>Related models</span></p>
        <h2 style="font-size:clamp(1.6rem,2.6vw,2.2rem);"><span lang-zh>同系列其他型號</span><span lang-en>More from the range</span></h2>
      </div>
      <div class="ph-rel-grid">
{related_html}
      </div>
    </div>
  </section>

  <section class="ph-cta">
    <div class="container">
      <h2><span lang-zh>準備為您的場地度身配置？</span><span lang-en>Ready to size {sku} for your space?</span></h2>
      <p><span lang-zh>留下場地資料，香港工程顧問將於一個工作天內回覆建議型號、估價及上門勘察安排。</span><span lang-en>Submit your details and a Hong Kong engineer will reply within one business day with recommended models, pricing, and a site survey.</span></p>
      <a href="../index.html#quote" class="btn-pill"><span lang-zh>免費諮詢 →</span><span lang-en>Request a quote →</span></a>
    </div>
  </section>

  <footer>
    <div class="container">
      <div class="footer-bottom" style="padding-top:0;">
        <span>© 2026 ERV.hk · <span lang-zh>由 DBA 製造</span><span lang-en>Manufactured by DBA</span></span>
        <span><a href="../index.html" style="color:rgba(255,255,255,0.6);">← <span lang-zh>返回首頁</span><span lang-en>Back to home</span></a></span>
      </div>
    </div>
  </footer>

  <script src="../script.js"></script>
</body>
</html>
"""


def main():
    # Clean stale pages from earlier (GEC80V, THC80, THC150) so they don't linger
    for stale in ("dba-gec80v.html", "dba-thc80.html", "dba-thc150.html"):
        p = OUT / stale
        if p.exists():
            p.unlink()
            print(f"  ✗ removed {stale}")

    for p in PRODUCTS:
        slug_name = slug(p["sku"])
        html = PAGE.format(
            sku=p["sku"],
            slug=slug_name,
            image=p["image"],
            series_eyebrow_zh=p["series_eyebrow_zh"],
            series_eyebrow_en=p["series_eyebrow_en"],
            tag_html=render_tag(p["tag_zh"], p["tag_en"]),
            headline_zh=p["headline_zh"],
            headline_en=p["headline_en"],
            sub_zh=p["sub_zh"],
            sub_en=p["sub_en"],
            quick_html=render_quick(p["quick"]),
            specs_html=render_specs(p["specs"]),
            related_html=render_related(p["related"], PRODUCTS),
        )
        out_path = OUT / f"{slug_name}.html"
        out_path.write_text(html, encoding="utf-8")
        print(f"  ✓ {out_path.name}")
    print(f"Generated {len(PRODUCTS)} product pages → {OUT}")


if __name__ == "__main__":
    main()
