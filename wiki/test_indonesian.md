# [Linux] Bash test penggunaan: Memeriksa kondisi ekspresi

## Overview
Perintah `test` dalam Bash digunakan untuk mengevaluasi ekspresi dan memeriksa kondisi tertentu. Ini sering digunakan dalam skrip untuk membuat keputusan berdasarkan hasil evaluasi, seperti memeriksa keberadaan file, membandingkan angka, atau memeriksa string.

## Usage
Sintaks dasar dari perintah `test` adalah sebagai berikut:

```bash
test [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang digunakan dengan perintah `test`:

- `-e [file]`: Memeriksa apakah file ada.
- `-f [file]`: Memeriksa apakah file adalah file biasa.
- `-d [directory]`: Memeriksa apakah direktori ada.
- `-z [string]`: Memeriksa apakah panjang string adalah nol.
- `-n [string]`: Memeriksa apakah panjang string lebih dari nol.
- `[string1] = [string2]`: Memeriksa apakah dua string sama.
- `[integer1] -eq [integer2]`: Memeriksa apakah dua angka sama.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan perintah `test`:

1. Memeriksa apakah sebuah file ada:
   ```bash
   test -e myfile.txt && echo "File ada"
   ```

2. Memeriksa apakah sebuah direktori ada:
   ```bash
   test -d mydirectory && echo "Direktori ada"
   ```

3. Memeriksa apakah sebuah string kosong:
   ```bash
   mystring=""
   test -z "$mystring" && echo "String kosong"
   ```

4. Membandingkan dua angka:
   ```bash
   a=5
   b=10
   test $a -lt $b && echo "$a lebih kecil dari $b"
   ```

5. Memeriksa kesamaan dua string:
   ```bash
   str1="hello"
   str2="hello"
   test "$str1" = "$str2" && echo "String sama"
   ```

## Tips
- Gunakan `[` sebagai alternatif untuk `test`, misalnya: `[ -e myfile.txt ]`.
- Selalu gunakan tanda kutip pada variabel untuk menghindari kesalahan saat variabel kosong.
- Kombinasikan beberapa kondisi dengan operator logika `&&` (dan) atau `||` (atau) untuk membuat keputusan yang lebih kompleks.