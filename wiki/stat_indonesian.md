# [Linux] Bash stat Penggunaan: Menampilkan informasi status file

## Overview
Perintah `stat` digunakan untuk menampilkan informasi status dari file atau direktori di sistem Linux. Informasi yang ditampilkan mencakup ukuran file, waktu akses, waktu modifikasi, dan banyak lagi.

## Usage
Sintaks dasar dari perintah `stat` adalah sebagai berikut:

```
stat [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `stat`:

- `-c` : Menentukan format output yang diinginkan.
- `-f` : Menampilkan informasi sistem file dari file yang ditentukan.
- `--help` : Menampilkan bantuan tentang penggunaan perintah `stat`.
- `--version` : Menampilkan versi dari perintah `stat`.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `stat`:

1. Menampilkan informasi dasar tentang sebuah file:
   ```bash
   stat nama_file.txt
   ```

2. Menampilkan informasi sistem file dari sebuah direktori:
   ```bash
   stat -f /path/to/directory
   ```

3. Menggunakan opsi format khusus untuk menampilkan hanya ukuran file:
   ```bash
   stat -c %s nama_file.txt
   ```

4. Menampilkan informasi lengkap dari file dengan waktu akses dan modifikasi:
   ```bash
   stat -c "Akses: %x, Modifikasi: %y" nama_file.txt
   ```

## Tips
- Gunakan opsi `-c` untuk mengkustomisasi output sesuai kebutuhan Anda.
- Untuk memeriksa informasi beberapa file sekaligus, Anda dapat mencantumkan beberapa nama file dalam satu perintah.
- Jika Anda sering menggunakan format tertentu, pertimbangkan untuk membuat alias di `.bashrc` untuk mempercepat akses.