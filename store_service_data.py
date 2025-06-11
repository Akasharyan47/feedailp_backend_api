from dotenv import load_dotenv
import os, base64, json, firebase_admin
from firebase_admin import credentials, firestore

# — Load and decode Firebase credentials —
load_dotenv()
enc = os.getenv("FIREBASE_CREDENTIALS")
if not enc:
    raise ValueError("FIREBASE_CREDENTIALS missing in .env")
decoded = base64.b64decode(enc)
cred = credentials.Certificate(json.loads(decoded))
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

# — 1. Add 10 Service Types —
service_types = [
    {"service_type_id": "experience_review", "service_type_nm": "Experience Review"},
    {"service_type_id": "support_review", "service_type_nm": "Customer Support Review"},
    {"service_type_id": "delivery_review", "service_type_nm": "Delivery Review"}, 
    {"service_type_id": "installation_review", "service_type_nm": "Installation Service Review"},
    {"service_type_id": "quality_review", "service_type_nm": "Product Quality Review"}, 
    {"service_type_id": "customer_service_review", "service_type_nm": "Customer Service Review"},
    {"service_type_id": "feature_review", "service_type_nm": "Product Feature Review"},
]

for st in service_types:
    db.collection("service_types").document(st["service_type_id"]).set(st)
print("✅ Added 10 service_types")

# — 2. Add 10 Brands linked to service_type → experience_review —
brands = [
    {"brand_id": "apple", "brand_name": "Apple", "service_type_id": "experience_review"},
    {"brand_id": "samsung", "brand_name": "Samsung", "service_type_id": "experience_review"},
    {"brand_id": "sony", "brand_name": "Sony", "service_type_id": "experience_review"},
    {"brand_id": "lg", "brand_name": "LG", "service_type_id": "experience_review"},
    {"brand_id": "panasonic", "brand_name": "Panasonic", "service_type_id": "experience_review"},
    {"brand_id": "philips", "brand_name": "Philips", "service_type_id": "experience_review"},
    {"brand_id": "bose", "brand_name": "Bose", "service_type_id": "experience_review"},
    {"brand_id": "dell", "brand_name": "Dell", "service_type_id": "experience_review"},
    {"brand_id": "hp", "brand_name": "HP", "service_type_id": "experience_review"},
    {"brand_id": "lenovo", "brand_name": "Lenovo", "service_type_id": "experience_review"},
    {"brand_id": "asus", "brand_name": "Asus", "service_type_id": "experience_review"},
    {"brand_id": "acer", "brand_name": "Acer", "service_type_id": "experience_review"},
    {"brand_id": "microsoft", "brand_name": "Microsoft", "service_type_id": "experience_review"},
    {"brand_id": "google", "brand_name": "Google", "service_type_id": "experience_review"},
    {"brand_id": "amazon", "brand_name": "Amazon", "service_type_id": "experience_review"},
    {"brand_id": "oneplus", "brand_name": "OnePlus", "service_type_id": "experience_review"},
    {"brand_id": "xiaomi", "brand_name": "Xiaomi", "service_type_id": "experience_review"},
    {"brand_id": "oppo", "brand_name": "Oppo", "service_type_id": "experience_review"},
    {"brand_id": "vivo", "brand_name": "Vivo", "service_type_id": "experience_review"},
    {"brand_id": "realme", "brand_name": "Realme", "service_type_id": "experience_review"},
    {"brand_id": "motorola", "brand_name": "Motorola", "service_type_id": "experience_review"},
    {"brand_id": "nokia", "brand_name": "Nokia", "service_type_id": "experience_review"},
    {"brand_id": "htc", "brand_name": "HTC", "service_type_id": "experience_review"},
    {"brand_id": "huawei", "brand_name": "Huawei", "service_type_id": "experience_review"},
    {"brand_id": "zte", "brand_name": "ZTE", "service_type_id": "experience_review"},
    {"brand_id": "tcl", "brand_name": "TCL", "service_type_id": "experience_review"},
    {"brand_id": "sharp", "brand_name": "Sharp", "service_type_id": "experience_review"},
    {"brand_id": "roku", "brand_name": "Roku", "service_type_id": "experience_review"},
    {"brand_id": "blackberry", "brand_name": "BlackBerry", "service_type_id": "experience_review"},
    {"brand_id": "garmin", "brand_name": "Garmin", "service_type_id": "experience_review"},
    {"brand_id": "fitbit", "brand_name": "Fitbit", "service_type_id": "experience_review"},
    {"brand_id": "gopro", "brand_name": "GoPro", "service_type_id": "experience_review"},
    {"brand_id": "dji", "brand_name": "DJI", "service_type_id": "experience_review"},
    {"brand_id": "canon", "brand_name": "Canon", "service_type_id": "experience_review"},
    {"brand_id": "nikon", "brand_name": "Nikon", "service_type_id": "experience_review"},
    {"brand_id": "epson", "brand_name": "Epson", "service_type_id": "experience_review"},
    {"brand_id": "brother", "brand_name": "Brother", "service_type_id": "experience_review"},
    {"brand_id": "seagate", "brand_name": "Seagate", "service_type_id": "experience_review"},
    {"brand_id": "westerndigital", "brand_name": "Western Digital", "service_type_id": "experience_review"},
    {"brand_id": "sandisk", "brand_name": "SanDisk", "service_type_id": "experience_review"},
    {"brand_id": "kingston", "brand_name": "Kingston", "service_type_id": "experience_review"},
    {"brand_id": "logitech", "brand_name": "Logitech", "service_type_id": "experience_review"},
    {"brand_id": "razer", "brand_name": "Razer", "service_type_id": "experience_review"},
    {"brand_id": "alienware", "brand_name": "Alienware", "service_type_id": "experience_review"},
    {"brand_id": "msi", "brand_name": "MSI", "service_type_id": "experience_review"},
    {"brand_id": "jbl", "brand_name": "JBL", "service_type_id": "experience_review"},
    {"brand_id": "sennheiser", "brand_name": "Sennheiser", "service_type_id": "experience_review"},
    {"brand_id": "electrolux", "brand_name": "Electrolux", "service_type_id": "experience_review"},
    {"brand_id": "haier", "brand_name": "Haier", "service_type_id": "experience_review"}
]


for b in brands:
    db.collection("brands").document(b["brand_id"]).set(b)
print("✅ Added 10 brands")

# — 3. Add 10 Products linked to above brands →
products = [
    {"product_id": "apple_iphone14", "product_nm": "iPhone 14", "brand_id": "apple"},
    {"product_id": "apple_macbook_air", "product_nm": "MacBook Air", "brand_id": "apple"},
    {"product_id": "apple_airpods_pro", "product_nm": "AirPods Pro", "brand_id": "apple"},
    {"product_id": "apple_ipad_pro", "product_nm": "iPad Pro", "brand_id": "apple"},
    {"product_id": "apple_watch_series8", "product_nm": "Apple Watch Series 8", "brand_id": "apple"},

    {"product_id": "samsung_galaxy_s23", "product_nm": "Galaxy S23", "brand_id": "samsung"},
    {"product_id": "samsung_galaxy_tab_s8", "product_nm": "Galaxy Tab S8", "brand_id": "samsung"},
    {"product_id": "samsung_qled_tv", "product_nm": "QLED TV", "brand_id": "samsung"},
    {"product_id": "samsung_galaxy_watch5", "product_nm": "Galaxy Watch 5", "brand_id": "samsung"},
    {"product_id": "samsung_buds2", "product_nm": "Galaxy Buds 2", "brand_id": "samsung"},

    {"product_id": "dell_xps13", "product_nm": "XPS 13 Laptop", "brand_id": "dell"},
    {"product_id": "dell_inspiron15", "product_nm": "Inspiron 15", "brand_id": "dell"},
    {"product_id": "dell_alienware_m15", "product_nm": "Alienware m15", "brand_id": "dell"},
    {"product_id": "dell_ultrasharp_monitor", "product_nm": "UltraSharp Monitor", "brand_id": "dell"},
    {"product_id": "dell_poweredge_t40", "product_nm": "PowerEdge T40 Server", "brand_id": "dell"},

    {"product_id": "hp_spectre_x360", "product_nm": "Spectre x360", "brand_id": "hp"},
    {"product_id": "hp_envy_13", "product_nm": "Envy 13", "brand_id": "hp"},
    {"product_id": "hp_omen_15", "product_nm": "OMEN 15 Gaming Laptop", "brand_id": "hp"},
    {"product_id": "hp_laserjet_pro", "product_nm": "LaserJet Pro Printer", "brand_id": "hp"},
    {"product_id": "hp_rise_station", "product_nm": "HP Rise Docking Station", "brand_id": "hp"},

    {"product_id": "lenovo_thinkpad_x1", "product_nm": "ThinkPad X1 Carbon", "brand_id": "lenovo"},
    {"product_id": "lenovo_legion_5", "product_nm": "Legion 5 Gaming Laptop", "brand_id": "lenovo"},
    {"product_id": "lenovo_yoga_9i", "product_nm": "Yoga 9i", "brand_id": "lenovo"},
    {"product_id": "lenovo_tab_p11", "product_nm": "Tab P11 Pro", "brand_id": "lenovo"},
    {"product_id": "lenovo_ideapad_3", "product_nm": "IdeaPad 3", "brand_id": "lenovo"},

    {"product_id": "asus_zenbook_14", "product_nm": "ZenBook 14", "brand_id": "asus"},
    {"product_id": "asus_rog_strix", "product_nm": "ROG Strix G15", "brand_id": "asus"},
    {"product_id": "asus_vivobook_15", "product_nm": "VivoBook 15", "brand_id": "asus"},
    {"product_id": "asus_tuf_gaming_f15", "product_nm": "TUF Gaming F15", "brand_id": "asus"},
    {"product_id": "asus_proart_display", "product_nm": "ProArt Display", "brand_id": "asus"},

    {"product_id": "acer_swift_3", "product_nm": "Swift 3", "brand_id": "acer"},
    {"product_id": "acer_predator_helios_300", "product_nm": "Predator Helios 300", "brand_id": "acer"},
    {"product_id": "acer_spin_5", "product_nm": "Spin 5", "brand_id": "acer"},
    {"product_id": "acer_chromebook_spin", "product_nm": "Chromebook Spin 713", "brand_id": "acer"},
    {"product_id": "acer_nitro_5", "product_nm": "Nitro 5 Gaming Laptop", "brand_id": "acer"},

    {"product_id": "xiaomi_redmi_note_13", "product_nm": "Redmi Note 13", "brand_id": "xiaomi"},
    {"product_id": "xiaomi_mi_12", "product_nm": "Mi 12", "brand_id": "xiaomi"},
    {"product_id": "xiaomi_poco_x5", "product_nm": "Poco X5", "brand_id": "xiaomi"},
    {"product_id": "xiaomi_mi_band_7", "product_nm": "Mi Band 7", "brand_id": "xiaomi"},
    {"product_id": "xiaomi_smart_tv", "product_nm": "Mi Smart TV", "brand_id": "xiaomi"},

    {"product_id": "oneplus_nord_2", "product_nm": "OnePlus Nord 2", "brand_id": "oneplus"},
    {"product_id": "oneplus_10_pro", "product_nm": "OnePlus 10 Pro", "brand_id": "oneplus"},
    {"product_id": "oneplus_bullets_wireless", "product_nm": "Bullets Wireless 2", "brand_id": "oneplus"},
    {"product_id": "oneplus_watch", "product_nm": "OnePlus Watch", "brand_id": "oneplus"},
    {"product_id": "oneplus_nord_ce", "product_nm": "Nord CE", "brand_id": "oneplus"},

    {"product_id": "realme_gt_2", "product_nm": "Realme GT 2", "brand_id": "realme"},
    {"product_id": "realme_buds_q2", "product_nm": "Buds Q2", "brand_id": "realme"},
    {"product_id": "realme_narzo_50", "product_nm": "Narzo 50", "brand_id": "realme"},
    {"product_id": "realme_watch_2", "product_nm": "Watch 2", "brand_id": "realme"},
    {"product_id": "realme_c35", "product_nm": "Realme C35", "brand_id": "realme"},

    {"product_id": "google_pixel_7", "product_nm": "Pixel 7", "brand_id": "google"},
    {"product_id": "google_pixelbook_go", "product_nm": "Pixelbook Go", "brand_id": "google"},
    {"product_id": "google_nest_hub", "product_nm": "Nest Hub", "brand_id": "google"},
    {"product_id": "google_wifi_router", "product_nm": "Nest Wifi Router", "brand_id": "google"},
    {"product_id": "google_pixel_watch", "product_nm": "Pixel Watch", "brand_id": "google"},

    {"product_id": "motorola_edge_30", "product_nm": "Edge 30", "brand_id": "motorola"},
    {"product_id": "motorola_moto_g_power", "product_nm": "Moto G Power", "brand_id": "motorola"},
    {"product_id": "motorola_razr_5g", "product_nm": "Razr 5G", "brand_id": "motorola"},
    {"product_id": "motorola_moto_watch_100", "product_nm": "Moto Watch 100", "brand_id": "motorola"},
    {"product_id": "motorola_one_5g", "product_nm": "One 5G", "brand_id": "motorola"},
]


for p in products:
    db.collection("products").document(p["product_id"]).set(p)
print("✅ Added 10 products")

print("🎉 Data population complete.")
