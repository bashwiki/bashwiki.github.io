# [Linux] Bash command penggunaan: Menghitung jumlah baris dalam file

## Overview
Perintah `wc` (word count) digunakan untuk menghitung jumlah baris, kata, dan karakter dalam file. Ini adalah alat yang berguna untuk analisis teks dan pemrosesan data.

## Usage
Berikut adalah sintaks dasar dari perintah `wc`:

```bash
wc [options] [file...]
```

## Common Options
- `-l`: Menghitung jumlah baris.
- `-w`: Menghitung jumlah kata.
- `-c`: Menghitung jumlah karakter.
- `-m`: Menghitung jumlah karakter (dalam Unicode).
- `-L`: Menampilkan panjang baris terpanjang.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `wc`:

1. Menghitung jumlah baris dalam sebuah file:
   ```bash
   wc -l namafile.txt
   ```

2. Menghitung jumlah kata dalam sebuah file:
   ```bash
   wc -w namafile.txt
   ```

3. Menghitung jumlah karakter dalam sebuah file:
   ```bash
   wc -c namafile.txt
   ```

4. Menghitung jumlah baris, kata, dan karakter sekaligus:
   ```bash
   wc namafile.txt
   ```

5. Menghitung jumlah baris dalam beberapa file:
   ```bash
   wc -l file1.txt file2.txt
   ```

## Tips
- Gunakan opsi `-l` untuk cepat mengetahui jumlah baris dalam file log.
- Kombinasikan `wc` dengan perintah lain menggunakan pipe (`|`) untuk analisis yang lebih kompleks. Contoh:
  ```bash
  cat namafile.txt | wc -l
  ```
- Untuk menghitung panjang baris terpanjang, gunakan opsi `-L`:
  ```bash
  wc -L namafile.txt
  ```