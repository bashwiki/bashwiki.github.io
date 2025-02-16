# [Linux] Bash sort penggunaan: Mengurutkan baris dalam file atau input

## Overview
Perintah `sort` digunakan untuk mengurutkan baris dalam file teks atau input yang diberikan. Perintah ini sangat berguna untuk mengorganisir data dalam urutan tertentu, baik secara alfabetis maupun numerik.

## Usage
Berikut adalah sintaks dasar dari perintah `sort`:

```
sort [options] [arguments]
```

## Common Options
- `-r`: Mengurutkan dalam urutan terbalik (descending).
- `-n`: Mengurutkan berdasarkan nilai numerik.
- `-k`: Mengurutkan berdasarkan kolom tertentu.
- `-u`: Menghapus baris duplikat setelah pengurutan.
- `-o`: Menyimpan hasil pengurutan ke dalam file.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `sort`:

1. **Mengurutkan file secara alfabetis:**
   ```bash
   sort namafile.txt
   ```

2. **Mengurutkan file secara terbalik:**
   ```bash
   sort -r namafile.txt
   ```

3. **Mengurutkan file berdasarkan nilai numerik:**
   ```bash
   sort -n angka.txt
   ```

4. **Mengurutkan berdasarkan kolom tertentu (misalnya kolom kedua):**
   ```bash
   sort -k2 namafile.txt
   ```

5. **Menghapus baris duplikat dan menyimpan hasil ke file baru:**
   ```bash
   sort -u namafile.txt -o hasil.txt
   ```

## Tips
- Selalu gunakan opsi `-o` jika Anda ingin menyimpan hasil pengurutan ke dalam file untuk menghindari kehilangan data asli.
- Kombinasikan opsi untuk hasil yang lebih spesifik, seperti `sort -n -k2` untuk mengurutkan berdasarkan kolom kedua dengan nilai numerik.
- Gunakan `cat` dan pipe (`|`) untuk mengurutkan output dari perintah lain, misalnya:
  ```bash
  cat namafile.txt | sort
  ```