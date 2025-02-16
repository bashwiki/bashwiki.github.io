# [Linux] Bash basename Penggunaan: Mengambil nama file dari path

## Overview
Perintah `basename` digunakan untuk mengambil nama file dari sebuah path lengkap. Ini berguna ketika Anda hanya ingin mendapatkan nama file tanpa direktori yang menyertainya.

## Usage
Berikut adalah sintaks dasar dari perintah `basename`:

```bash
basename [options] [arguments]
```

## Common Options
- `-a`: Mengambil semua nama file dari daftar yang diberikan.
- `-s`: Menghapus suffix tertentu dari nama file.
- `--help`: Menampilkan bantuan penggunaan perintah.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `basename`:

1. Mengambil nama file dari path lengkap:
   ```bash
   basename /home/user/document.txt
   ```
   Output: `document.txt`

2. Menghapus suffix dari nama file:
   ```bash
   basename /home/user/document.txt .txt
   ```
   Output: `document`

3. Mengambil nama file dari beberapa path:
   ```bash
   basename -a /home/user/file1.txt /home/user/file2.txt
   ```
   Output:
   ```
   file1.txt
   file2.txt
   ```

## Tips
- Gunakan `basename` dalam skrip untuk memproses nama file secara otomatis.
- Kombinasikan dengan perintah lain seperti `find` untuk mengelola file dalam jumlah besar.
- Pastikan untuk menggunakan opsi `-s` jika Anda ingin menghapus ekstensi file tertentu dari output.