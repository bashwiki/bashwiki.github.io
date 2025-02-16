# [Linux] Bash uname Penggunaan: Menampilkan informasi sistem

## Overview
Perintah `uname` digunakan untuk menampilkan informasi tentang sistem operasi yang sedang digunakan. Ini termasuk nama kernel, versi, dan informasi lainnya yang relevan mengenai sistem.

## Usage
Sintaks dasar dari perintah `uname` adalah sebagai berikut:

```
uname [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `uname`:

- `-a`: Menampilkan semua informasi sistem.
- `-s`: Menampilkan nama kernel.
- `-n`: Menampilkan nama jaringan (hostname).
- `-r`: Menampilkan versi kernel.
- `-v`: Menampilkan informasi versi tambahan.
- `-m`: Menampilkan arsitektur mesin.
- `-p`: Menampilkan tipe prosesor (jika tersedia).
- `-i`: Menampilkan informasi platform (jika tersedia).
- `-o`: Menampilkan nama sistem operasi.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `uname`:

1. Menampilkan semua informasi sistem:
   ```bash
   uname -a
   ```

2. Menampilkan hanya nama kernel:
   ```bash
   uname -s
   ```

3. Menampilkan versi kernel:
   ```bash
   uname -r
   ```

4. Menampilkan arsitektur mesin:
   ```bash
   uname -m
   ```

5. Menampilkan nama sistem operasi:
   ```bash
   uname -o
   ```

## Tips
- Gunakan `uname -a` untuk mendapatkan gambaran lengkap tentang sistem Anda dalam satu perintah.
- Perintah ini sangat berguna untuk skrip yang memerlukan informasi tentang lingkungan sistem.
- Kombinasikan `uname` dengan perintah lain untuk memfilter atau memformat output sesuai kebutuhan Anda.