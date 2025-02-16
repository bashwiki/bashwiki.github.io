# [Linux] Bash pwd Penggunaan: Menampilkan direktori kerja saat ini

## Overview
Perintah `pwd` (print working directory) digunakan untuk menampilkan jalur direktori kerja saat ini di terminal. Ini sangat berguna untuk mengetahui lokasi Anda dalam struktur sistem file.

## Usage
Sintaks dasar dari perintah `pwd` adalah sebagai berikut:

```
pwd [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `pwd`:

- `-L`: Menampilkan jalur direktori kerja saat ini dengan mengikuti simbolik link.
- `-P`: Menampilkan jalur direktori kerja saat ini dengan mengikuti jalur fisik, tanpa mengikuti simbolik link.

## Common Examples
Berikut adalah beberapa contoh penggunaan `pwd`:

1. Menampilkan direktori kerja saat ini:
   ```bash
   pwd
   ```

2. Menampilkan jalur direktori kerja saat ini dengan mengikuti simbolik link:
   ```bash
   pwd -L
   ```

3. Menampilkan jalur direktori kerja saat ini dengan mengikuti jalur fisik:
   ```bash
   pwd -P
   ```

## Tips
- Gunakan `pwd` sebelum menjalankan perintah lain untuk memastikan Anda berada di direktori yang benar.
- Kombinasikan `pwd` dengan perintah lain menggunakan `&&` untuk menjalankan perintah berikutnya hanya jika `pwd` berhasil.
- Jika Anda bekerja dengan banyak terminal, gunakan `pwd` untuk menghindari kebingungan tentang direktori kerja Anda saat ini.