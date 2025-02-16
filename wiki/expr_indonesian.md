# [Linux] Bash expr Penggunaan: Menghitung dan membandingkan ekspresi

## Overview
Perintah `expr` dalam Bash digunakan untuk mengevaluasi ekspresi dan melakukan operasi aritmatika, perbandingan, dan logika. Ini adalah alat yang berguna untuk melakukan perhitungan sederhana dalam skrip shell.

## Usage
Berikut adalah sintaks dasar dari perintah `expr`:

```bash
expr [options] [arguments]
```

## Common Options
- `+` : Menjumlahkan dua angka.
- `-` : Mengurangi angka kedua dari angka pertama.
- `*` : Mengalikan dua angka (perlu di-escape dengan `\` atau menggunakan tanda kutip).
- `/` : Membagi angka pertama dengan angka kedua.
- `%` : Menghitung sisa dari pembagian dua angka.
- `=` : Membandingkan dua nilai untuk kesetaraan.
- `>` : Memeriksa apakah nilai pertama lebih besar dari nilai kedua.
- `<` : Memeriksa apakah nilai pertama lebih kecil dari nilai kedua.

## Common Examples
Berikut adalah beberapa contoh penggunaan `expr`:

1. **Menjumlahkan dua angka:**
   ```bash
   expr 5 + 3
   ```
   Output: `8`

2. **Mengurangi angka:**
   ```bash
   expr 10 - 4
   ```
   Output: `6`

3. **Mengalikan dua angka:**
   ```bash
   expr 4 \* 3
   ```
   Output: `12`

4. **Membagi angka:**
   ```bash
   expr 20 / 4
   ```
   Output: `5`

5. **Mendapatkan sisa dari pembagian:**
   ```bash
   expr 10 % 3
   ```
   Output: `1`

6. **Membandingkan dua nilai:**
   ```bash
   expr 5 = 5
   ```
   Output: `1` (true)

7. **Memeriksa apakah satu angka lebih besar dari yang lain:**
   ```bash
   expr 7 \> 5
   ```
   Output: `1` (true)

## Tips
- Selalu gunakan tanda kutip atau escape (`\`) untuk operator perkalian (`*`) agar tidak bingung dengan wildcard di shell.
- Untuk operasi yang lebih kompleks, pertimbangkan menggunakan `bc` atau `awk` yang menawarkan lebih banyak fitur.
- Gunakan `$(...)` untuk menyimpan hasil dari `expr` ke dalam variabel, misalnya:
  ```bash
  hasil=$(expr 5 + 3)
  echo $hasil
  ```
- Pastikan untuk memeriksa kesalahan dalam ekspresi, karena `expr` akan mengembalikan nilai 0 jika terjadi kesalahan dalam evaluasi.