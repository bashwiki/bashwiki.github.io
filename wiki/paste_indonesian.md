# [Linux] Bash paste Penggunaan: Menggabungkan Baris dari Beberapa File

## Overview
Perintah `paste` digunakan untuk menggabungkan baris dari beberapa file menjadi satu baris. Setiap baris dari file yang berbeda akan digabungkan menjadi satu baris output, dengan pemisah yang dapat ditentukan.

## Usage
Berikut adalah sintaks dasar dari perintah `paste`:

```bash
paste [options] [arguments]
```

## Common Options
- `-d` : Menentukan pemisah yang digunakan antara kolom. Secara default, pemisahnya adalah tab.
- `-s` : Menggabungkan baris secara seri, bukan secara paralel.
- `-z` : Menggunakan karakter null sebagai pemisah.

## Common Examples
1. **Menggabungkan dua file dengan pemisah tab (default)**:
   ```bash
   paste file1.txt file2.txt
   ```

2. **Menggunakan pemisah koma**:
   ```bash
   paste -d ',' file1.txt file2.txt
   ```

3. **Menggabungkan baris secara seri**:
   ```bash
   paste -s file1.txt file2.txt
   ```

4. **Menggunakan karakter null sebagai pemisah**:
   ```bash
   paste -z file1.txt file2.txt
   ```

## Tips
- Pastikan file yang ingin digabungkan memiliki jumlah baris yang sama untuk hasil yang lebih teratur.
- Gunakan opsi `-d` untuk menyesuaikan pemisah sesuai kebutuhan, misalnya untuk menghasilkan file CSV.
- Cobalah menggabungkan lebih dari dua file untuk efisiensi saat menangani banyak data.