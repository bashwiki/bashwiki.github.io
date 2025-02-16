# [Linux] Bash lsusb Penggunaan: Menampilkan informasi perangkat USB

## Overview
Perintah `lsusb` digunakan untuk menampilkan informasi tentang perangkat USB yang terhubung ke sistem. Ini memberikan daftar perangkat USB yang terdeteksi, termasuk ID vendor, ID produk, dan informasi lainnya yang relevan.

## Usage
Sintaks dasar dari perintah `lsusb` adalah sebagai berikut:

```bash
lsusb [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `lsusb`:

- `-v`: Menampilkan informasi yang lebih rinci tentang perangkat USB.
- `-t`: Menampilkan perangkat USB dalam format pohon, menunjukkan hierarki perangkat.
- `-s [bus]:[device]`: Menampilkan informasi hanya untuk perangkat tertentu berdasarkan bus dan nomor perangkat.
- `-d [vendor]:[product]`: Menampilkan informasi untuk perangkat dengan ID vendor dan produk tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan `lsusb`:

1. Menampilkan daftar semua perangkat USB yang terhubung:
   ```bash
   lsusb
   ```

2. Menampilkan informasi rinci tentang semua perangkat USB:
   ```bash
   lsusb -v
   ```

3. Menampilkan perangkat USB dalam format pohon:
   ```bash
   lsusb -t
   ```

4. Menampilkan informasi untuk perangkat tertentu berdasarkan bus dan nomor perangkat:
   ```bash
   lsusb -s 001:002
   ```

5. Menampilkan informasi untuk perangkat dengan ID vendor dan produk tertentu:
   ```bash
   lsusb -d 1234:5678
   ```

## Tips
- Gunakan opsi `-v` untuk mendapatkan informasi tambahan yang mungkin berguna untuk pemecahan masalah perangkat USB.
- Jika Anda hanya tertarik pada perangkat tertentu, gunakan opsi `-s` atau `-d` untuk mempersempit hasil.
- Perintah ini biasanya memerlukan hak akses root untuk menampilkan informasi lengkap, jadi pertimbangkan untuk menggunakan `sudo` jika diperlukan.