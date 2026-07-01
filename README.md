# OSINT Personal Data Tracker v3.0 ULTIMATE 🔥

Sebuah alat CLI berbasis Python skala masif (Ultimate Edition) untuk melacak jejak digital username di **RATUSAN** platform media sosial dan website publik. 
Dibuat khusus untuk keperluan edukasi dan analisis legal (OSINT - Open Source Intelligence) guna meminimalisir risiko *Identity Theft*.

## 🔥 Fitur Ultra-Powerful v3.0
- **Massive 500+ Website Database**: Basis data didukung oleh integrasi format JSON berskala master (Sherlock-style) yang menembus lebih dari 450-500+ situs web terkemuka di seluruh dunia!
- **Hyper-Threading Engine (50 Workers)**: Dengan target 500 web, kami menginjeksi 50 pekerja (thread) paralel agar proses pemindaian masif ini bisa selesai hanya dalam hitungan detik.
- **Smart CLI Output**: Layar terminal tidak akan dipenuhi warna merah karena kini skrip hanya memunculkan hasil **yang berhasil ditemukan (HIJAU)** agar tampilan tetap bersih, elegan, dan fokus.
- **Auto-Report Generator**: Laporan otomatis berformat `report_ultimate_{username}.txt` dengan semua *direct link*.
- **SSL Error Ignorance**: Sistem dirancang menembus masalah sertifikat dan redirect demi kecepatan maksimal pencarian data publik.

## Instalasi & Persiapan

Pastikan Python 3 sudah terinstall.

1. Masuk ke direktori:
   ```bash
   cd /root/OSINT_Tracker
   ```
2. Pastikan file `data.json` sudah berada di dalam folder yang sama.
3. Install modul pelengkap:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Penggunaan Lengkap

```bash
python main.py <username>
```

**Contoh:**
```bash
python main.py riskimuhamad
```

## Ketentuan & Etika Penggunaan (Legal Warning)
- Alat ini murni untuk pengecekan data OSINT **legal** (karena mengekstrak info yang dibagikan secara publik).
- Jangan gunakan alat ini untuk kegiatan *stalking* atau pelanggaran hukum privasi pihak ketiga.
- **Gunakan HANYA untuk audit digital milik Anda sendiri atau keperluan edukasi cyber security defensive.**
