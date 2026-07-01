#!/usr/bin/env python3
import sys
from banner import print_banner
from checker import check_username

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <username_or_email>")
        print("Example: python main.py johndoe123")
        sys.exit(1)
        
    target = sys.argv[1]
    
    print_banner()
    
    if '@' in target:
        print("\033[93m[!] Note: Mengekstrak username dari email...\033[0m")
        username = target.split('@')[0]
    else:
        username = target
        
    check_username(username)
    
    print("\n\033[96m[+] Audit Recommendations for Preventing Identity Theft:\033[0m")
    print(" 1. Jika ada akun yang tercantum tetapi BUKAN milik Anda, berhati-hatilah terhadap potensi penyamaran (Impersonation).")
    print(" 2. Hapus akun di platform lama yang sudah tidak Anda gunakan untuk mengurangi permukaan serangan (Attack Surface).")
    print(" 3. Selalu aktifkan Autentikasi Dua Faktor (2FA) di setiap akun penting Anda.")

if __name__ == "__main__":
    main()
