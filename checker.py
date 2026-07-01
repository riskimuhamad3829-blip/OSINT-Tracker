import requests
import time
import concurrent.futures
from platforms import PLATFORMS
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Mematikan warning SSL demi kecepatan dan menghindari spam terminal
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def check_single_platform(platform, url, headers):
    try:
        # verify=False dan allow_redirects=True untuk mencegah nyangkut di cloudflare/ssl rusak
        response = requests.get(url, headers=headers, timeout=10, verify=False, allow_redirects=True)
        return platform, url, response.status_code
    except Exception:
        return platform, url, -1

def check_username(username):
    print(f"[*] Auditing digital footprint for username: \033[96m{username}\033[0m")
    print(f"[*] Version: \033[93m3.0 (ULTIMATE Edition)\033[0m\n")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    total_platforms = len(PLATFORMS)
    print(f"[+] Engine Started! Memeriksa \033[91m{total_platforms} situs web\033[0m dengan \033[93mHyper-Threading (50 Pekerja Paralel)\033[0m...\n")
    print(f"[!] Menyembunyikan tampilan 'TIDAK ADA' agar fokus hanya menampilkan temuan...\n")
    
    found_count = 0
    not_found_count = 0
    error_count = 0
    
    results_to_save = []
    
    # 50 threads untuk 500+ web agar super ekstrim kecepatannya!
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = {
            executor.submit(check_single_platform, p, u.format(username), headers): p 
            for p, u in PLATFORMS.items()
        }
        
        for future in concurrent.futures.as_completed(futures):
            platform, url, status = future.result()
            
            # Simple heuristic
            if status == 200:
                print(f"  \033[92m[+] ADA       : {platform:<25} -> {url}\033[0m")
                results_to_save.append(f"[+] ADA       : {platform:<25} -> {url}")
                found_count += 1
            elif status == 404:
                not_found_count += 1
            elif status == -1:
                error_count += 1
            else:
                error_count += 1

    report_filename = f"report_ultimate_{username}.txt"
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(f"=== Laporan OSINT Tracker (v3.0 ULTIMATE) ===\n")
        f.write(f"Target Username : {username}\n")
        f.write(f"Total Platform  : {total_platforms} Situs Web\n")
        f.write("==========================================\n\n")
        f.write(">>> DAFTAR AKUN DITEMUKAN <<<\n")
        if not results_to_save:
            f.write("Tidak ada jejak akun yang ditemukan di database kami.\n")
        else:
            for line in results_to_save:
                f.write(line + "\n")
        f.write(f"\n[Ringkasan]\nAda: {found_count} | Tidak Ada / 404: {not_found_count} | Error/Unclear: {error_count}\n")
        
    print(f"\n[+] Audit Selesai (v3.0 ULTIMATE)!")
    print(f"    - Ditemukan (ADA)    : \033[92m{found_count}\033[0m")
    print(f"    - Tidak Ditemukan    : \033[91m{not_found_count}\033[0m")
    print(f"    - Unclear / Error    : \033[93m{error_count}\033[0m")
    print(f"\n\033[92m[✓] LAPORAN TERSIMPAN: File \033[93m{report_filename}\033[92m berhasil dibuat!\033[0m")
