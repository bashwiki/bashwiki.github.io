# [Linux] Bash nice Penggunaan: Mengatur Prioritas Proses

## Overview
Perintah `nice` digunakan untuk mengatur prioritas eksekusi proses di sistem operasi Linux. Dengan menggunakan `nice`, pengguna dapat menentukan seberapa besar sumber daya CPU yang akan dialokasikan untuk proses tertentu, yang dapat membantu dalam mengelola beban kerja sistem.

## Usage
Sintaks dasar dari perintah `nice` adalah sebagai berikut:

```bash
nice [options] [command]
```

## Common Options
- `-n, --adjustment=N`: Menentukan nilai penyesuaian prioritas. Nilai ini dapat berkisar dari -20 (prioritas tertinggi) hingga 19 (prioritas terendah).
- `-h, --help`: Menampilkan bantuan penggunaan perintah `nice`.
- `--version`: Menampilkan versi dari perintah `nice`.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `nice`:

1. Menjalankan perintah `sleep` dengan prioritas default:
   ```bash
   nice sleep 10
   ```

2. Menjalankan perintah `make` dengan prioritas yang lebih rendah:
   ```bash
   nice -n 10 make
   ```

3. Menjalankan skrip Python dengan prioritas yang lebih tinggi:
   ```bash
   nice -n -5 python script.py
   ```

4. Menjalankan perintah `gzip` dengan prioritas terendah:
   ```bash
   nice -n 19 gzip file.txt
   ```

## Tips
- Gunakan `nice` saat menjalankan proses yang tidak mendesak untuk menghindari mengganggu proses penting lainnya.
- Periksa prioritas proses yang sedang berjalan dengan menggunakan perintah `top` atau `htop`.
- Jika Anda perlu mengubah prioritas proses yang sudah berjalan, gunakan perintah `renice` untuk mengubah prioritasnya.