# [Linux] Bash tee Penggunaan: Menyalin dan Menampilkan Output

## Overview
Perintah `tee` dalam Bash digunakan untuk membaca dari input standar dan menulis ke output standar serta satu atau lebih file. Ini memungkinkan pengguna untuk melihat output dari suatu perintah sambil juga menyimpannya ke dalam file.

## Usage
Berikut adalah sintaks dasar dari perintah `tee`:

```bash
tee [options] [arguments]
```

## Common Options
- `-a`, `--append`: Menambahkan output ke file yang sudah ada, bukan menimpa file tersebut.
- `-i`, `--ignore-interrupts`: Mengabaikan sinyal interupsi.
- `--help`: Menampilkan informasi bantuan tentang penggunaan `tee`.
- `--version`: Menampilkan versi dari perintah `tee`.

## Common Examples
Berikut adalah beberapa contoh penggunaan `tee`:

1. Menyimpan output ke dalam file:
   ```bash
   echo "Hello, World!" | tee output.txt
   ```

2. Menyimpan output dan menampilkan di terminal sekaligus:
   ```bash
   ls -l | tee file_list.txt
   ```

3. Menambahkan output ke file yang sudah ada:
   ```bash
   echo "New entry" | tee -a output.txt
   ```

4. Menggunakan `tee` dengan beberapa file:
   ```bash
   echo "Logging data" | tee file1.txt file2.txt
   ```

## Tips
- Gunakan opsi `-a` jika Anda ingin menambahkan data ke file yang sudah ada tanpa menghapus isinya.
- Kombinasikan `tee` dengan perintah lain menggunakan pipe (`|`) untuk memproses output lebih lanjut.
- Pastikan Anda memiliki izin yang diperlukan untuk menulis ke file yang dituju agar tidak mengalami kesalahan saat menggunakan `tee`.