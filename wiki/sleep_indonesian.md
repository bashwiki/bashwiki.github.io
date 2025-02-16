# [Linux] Bash sleep Penggunaan: Menunda eksekusi perintah

## Overview
Perintah `sleep` digunakan untuk menunda eksekusi perintah berikutnya dalam skrip atau terminal selama periode waktu tertentu. Ini berguna untuk memberikan jeda antara perintah atau untuk menunggu kondisi tertentu sebelum melanjutkan.

## Usage
Sintaks dasar dari perintah `sleep` adalah sebagai berikut:

```bash
sleep [options] [arguments]
```

## Common Options
- `-h`, `--help`: Menampilkan bantuan penggunaan perintah.
- `-V`, `--version`: Menampilkan versi dari perintah `sleep`.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `sleep`:

1. Menunda eksekusi selama 5 detik:
   ```bash
   sleep 5
   ```

2. Menunda eksekusi selama 2 menit:
   ```bash
   sleep 2m
   ```

3. Menunda eksekusi selama 1 jam:
   ```bash
   sleep 1h
   ```

4. Menggunakan `sleep` dalam skrip untuk menunggu sebelum menjalankan perintah lain:
   ```bash
   echo "Menunggu selama 10 detik..."
   sleep 10
   echo "Eksekusi dilanjutkan."
   ```

## Tips
- Gunakan `sleep` untuk memberikan jeda antara perintah dalam skrip otomatisasi agar tidak membebani sistem.
- Kombinasikan `sleep` dengan perintah lain dalam skrip untuk mengatur urutan eksekusi.
- Pastikan untuk tidak menggunakan waktu tidur yang terlalu lama dalam skrip yang berjalan secara otomatis, karena dapat menyebabkan keterlambatan yang tidak diinginkan.