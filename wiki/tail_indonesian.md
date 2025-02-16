# [Linux] Bash tail Penggunaan: Menampilkan bagian akhir dari file

## Overview
Perintah `tail` digunakan untuk menampilkan bagian akhir dari sebuah file. Secara default, `tail` akan menampilkan 10 baris terakhir dari file yang ditentukan. Ini sangat berguna untuk memantau log atau file teks yang terus diperbarui.

## Usage
Berikut adalah sintaks dasar dari perintah `tail`:

```bash
tail [options] [arguments]
```

## Common Options
- `-n [jumlah]`: Menentukan jumlah baris yang ingin ditampilkan dari akhir file. Misalnya, `-n 20` akan menampilkan 20 baris terakhir.
- `-f`: Mengikuti file yang sedang diperbarui. Ini berguna untuk memantau log secara real-time.
- `-c [jumlah]`: Menampilkan jumlah byte terakhir dari file. Misalnya, `-c 100` akan menampilkan 100 byte terakhir.
- `--help`: Menampilkan bantuan dan daftar opsi yang tersedia.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `tail`:

1. Menampilkan 10 baris terakhir dari sebuah file:
   ```bash
   tail namafile.txt
   ```

2. Menampilkan 20 baris terakhir dari sebuah file:
   ```bash
   tail -n 20 namafile.txt
   ```

3. Mengikuti file log secara real-time:
   ```bash
   tail -f logfile.log
   ```

4. Menampilkan 100 byte terakhir dari sebuah file:
   ```bash
   tail -c 100 namafile.txt
   ```

## Tips
- Gunakan opsi `-f` saat memantau file log untuk melihat pembaruan secara langsung.
- Kombinasikan `tail` dengan perintah lain menggunakan pipe (`|`) untuk analisis lebih lanjut. Misalnya, `tail -n 50 logfile.log | grep "ERROR"` untuk mencari baris yang mengandung "ERROR".
- Jika Anda ingin menghentikan pemantauan file dengan `-f`, tekan `Ctrl + C`.