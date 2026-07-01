import json
import os

PLATFORMS = {}

db_path = os.path.join(os.path.dirname(__file__), 'data.json')
if os.path.exists(db_path):
    try:
        with open(db_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Mengekstrak semua URL dari master JSON (400-500+ web)
            for platform, info in data.items():
                if "url" in info:
                    url = info["url"]
                    # Mengganti placeholder format jika ada yang aneh, meski '{}' cukup lazim
                    if "{}" in url:
                        PLATFORMS[platform] = url
                    else:
                        PLATFORMS[platform] = url + "/{}"
    except Exception as e:
        print(f"[-] Error parsing master database: {e}")
else:
    print("[-] File database master (data.json) tidak ditemukan!")
