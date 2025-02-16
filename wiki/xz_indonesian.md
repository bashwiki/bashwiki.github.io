# [Linux] Bash xz Penggunaan: Kompresi dan dekompresi file

## Overview
Perintah `xz` digunakan untuk mengompresi dan mendekompresi file menggunakan algoritma kompresi LZMA. `xz` sangat efisien dalam mengurangi ukuran file, sehingga sering digunakan untuk menghemat ruang penyimpanan dan mempercepat transfer file.

## Usage
Sintaks dasar dari perintah `xz` adalah sebagai berikut:

```bash
xz [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `xz`:

- `-d`, `--decompress`: Mendekompresi file.
- `-k`, `--keep`: Menyimpan file asli setelah kompresi.
- `-v`, `--verbose`: Menampilkan informasi lebih detail selama proses kompresi atau dekompresi.
- `-9`: Mengatur tingkat kompresi maksimum (0-9), di mana 9 adalah tingkat kompresi tertinggi.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `xz`:

1. **Mengompresi file**:
   ```bash
   xz file.txt
   ```
   Ini akan menghasilkan file `file.txt.xz` dan menghapus `file.txt` asli.

2. **Menyimpan file asli saat mengompresi**:
   ```bash
   xz -k file.txt
   ```
   Ini akan menghasilkan `file.txt.xz` dan tetap menyimpan `file.txt`.

3. **Mendekompresi file**:
   ```bash
   xz -d file.txt.xz
   ```
   Ini akan mengembalikan file `file.txt` dari file terkompresi `file.txt.xz`.

4. **Menampilkan informasi selama proses kompresi**:
   ```bash
   xz -v file.txt
   ```
   Ini akan memberikan informasi lebih lanjut tentang proses kompresi yang sedang berlangsung.

## Tips
- Selalu gunakan opsi `-k` jika Anda ingin menjaga file asli saat mengompresi.
- Untuk kompresi yang lebih cepat, gunakan tingkat kompresi yang lebih rendah (misalnya, `-1`).
- Periksa ukuran file setelah kompresi untuk memastikan efektivitas kompresi yang diinginkan.