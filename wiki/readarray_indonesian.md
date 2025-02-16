# [Linux] Bash readarray Penggunaan: Membaca baris ke dalam array

## Overview
Perintah `readarray` dalam Bash digunakan untuk membaca baris dari input standar (seperti file atau output perintah) dan menyimpannya ke dalam array. Ini sangat berguna ketika Anda ingin memproses data baris demi baris dalam skrip Bash.

## Usage
Sintaks dasar dari perintah `readarray` adalah sebagai berikut:

```bash
readarray [options] [array_name]
```

Di mana `array_name` adalah nama array di mana baris-baris akan disimpan.

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `readarray`:

- `-n N`: Hanya membaca N baris dari input.
- `-s N`: Melewati N baris pertama dari input.
- `-t`: Menghapus karakter newline dari akhir setiap baris yang dibaca.

## Common Examples
Berikut adalah beberapa contoh penggunaan `readarray`:

1. **Membaca dari file ke dalam array:**
   ```bash
   readarray my_array < myfile.txt
   ```

2. **Membaca hanya 3 baris pertama dari file:**
   ```bash
   readarray -n 3 my_array < myfile.txt
   ```

3. **Melewati 2 baris pertama dan membaca sisanya:**
   ```bash
   readarray -s 2 my_array < myfile.txt
   ```

4. **Menghapus karakter newline dari setiap baris:**
   ```bash
   readarray -t my_array < myfile.txt
   ```

5. **Membaca output dari perintah dan menyimpannya dalam array:**
   ```bash
   readarray my_array < <(ls -1)
   ```

## Tips
- Pastikan untuk menggunakan opsi `-t` jika Anda tidak ingin karakter newline mengganggu pemrosesan data.
- Gunakan `declare -p my_array` untuk memeriksa isi dari array setelah Anda mengisinya dengan `readarray`.
- Jika Anda bekerja dengan file besar, pertimbangkan untuk menggunakan opsi `-n` dan `-s` untuk mengelola memori dengan lebih baik.