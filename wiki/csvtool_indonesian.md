# [Linux] Bash csvtool Penggunaan: Mengelola file CSV

## Overview
Perintah `csvtool` digunakan untuk memanipulasi dan mengelola file CSV (Comma-Separated Values). Dengan `csvtool`, pengguna dapat melakukan berbagai operasi seperti mengekstrak kolom, mengurutkan data, dan mengubah format file CSV dengan mudah.

## Usage
Berikut adalah sintaks dasar dari perintah `csvtool`:

```bash
csvtool [options] [arguments]
```

## Common Options
- `-c`: Menentukan kolom yang ingin diekstrak.
- `-s`: Menentukan pemisah yang digunakan dalam file CSV (default adalah koma).
- `-r`: Mengurutkan data berdasarkan kolom tertentu.
- `-h`: Menampilkan bantuan dan informasi tentang penggunaan perintah.

## Common Examples
Berikut adalah beberapa contoh penggunaan `csvtool`:

1. **Menampilkan kolom tertentu dari file CSV**:
   Untuk menampilkan kolom pertama dan ketiga dari file `data.csv`:
   ```bash
   csvtool -c 1,3 read data.csv
   ```

2. **Mengubah pemisah dalam file CSV**:
   Untuk mengubah pemisah dari koma menjadi titik koma:
   ```bash
   csvtool -s ';' read data.csv
   ```

3. **Mengurutkan data berdasarkan kolom kedua**:
   Untuk mengurutkan data dalam `data.csv` berdasarkan kolom kedua:
   ```bash
   csvtool -r 2 sort data.csv
   ```

4. **Menggabungkan dua file CSV**:
   Untuk menggabungkan `file1.csv` dan `file2.csv`:
   ```bash
   csvtool cat file1.csv file2.csv
   ```

## Tips
- Selalu periksa format file CSV Anda sebelum menggunakan `csvtool` untuk memastikan pemisah yang benar.
- Gunakan opsi `-h` untuk mendapatkan informasi lebih lanjut tentang opsi yang tersedia.
- Simpan salinan file CSV asli sebelum melakukan operasi yang dapat mengubah data, untuk menghindari kehilangan informasi.