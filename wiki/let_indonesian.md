# [Linux] Bash let: Menghitung Ekspresi Aritmatika

## Overview
Perintah `let` dalam Bash digunakan untuk melakukan perhitungan aritmatika. Dengan `let`, Anda dapat melakukan operasi matematika sederhana seperti penjumlahan, pengurangan, perkalian, dan pembagian pada variabel.

## Usage
Berikut adalah sintaks dasar dari perintah `let`:

```bash
let [options] [arguments]
```

## Common Options
Beberapa opsi umum yang dapat digunakan dengan `let` antara lain:
- `-`: Menandakan pengurangan.
- `+`: Menandakan penjumlahan.
- `*`: Menandakan perkalian.
- `/`: Menandakan pembagian.
- `%`: Menandakan sisa bagi (modulus).

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `let`:

1. **Penjumlahan dua angka:**
   ```bash
   let "a = 5 + 3"
   echo $a  # Output: 8
   ```

2. **Pengurangan:**
   ```bash
   let "b = 10 - 4"
   echo $b  # Output: 6
   ```

3. **Perkalian:**
   ```bash
   let "c = 7 * 6"
   echo $c  # Output: 42
   ```

4. **Pembagian:**
   ```bash
   let "d = 20 / 4"
   echo $d  # Output: 5
   ```

5. **Modulus:**
   ```bash
   let "e = 10 % 3"
   echo $e  # Output: 1
   ```

## Tips
- Gunakan tanda kutip di sekitar ekspresi untuk menghindari kesalahan sintaks.
- Pastikan variabel yang digunakan telah dideklarasikan sebelumnya untuk menghindari hasil yang tidak terduga.
- Anda juga dapat menggunakan `let` dalam skrip Bash untuk melakukan perhitungan secara otomatis dalam loop atau fungsi.