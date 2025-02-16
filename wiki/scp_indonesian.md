# [Linux] Bash scp Penggunaan: Menyalin file antar sistem secara aman

## Overview
Perintah `scp` (Secure Copy Protocol) digunakan untuk menyalin file dan direktori antara sistem secara aman melalui protokol SSH. Dengan `scp`, pengguna dapat mentransfer file dengan enkripsi, sehingga menjaga keamanan data selama proses transfer.

## Usage
Berikut adalah sintaks dasar dari perintah `scp`:

```bash
scp [options] [source] [destination]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `scp`:

- `-r`: Menyalin direktori secara rekursif.
- `-P port`: Menentukan port SSH yang digunakan (perhatikan huruf besar 'P').
- `-i identity_file`: Menggunakan file identitas tertentu untuk autentikasi.
- `-v`: Menampilkan informasi lebih detail tentang proses transfer (verbose).
- `-q`: Menonaktifkan output yang tidak perlu.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `scp`:

1. Menyalin file dari lokal ke server:
   ```bash
   scp /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
   ```

2. Menyalin file dari server ke lokal:
   ```bash
   scp user@remote_host:/path/to/remote/file.txt /path/to/local/directory/
   ```

3. Menyalin direktori secara rekursif:
   ```bash
   scp -r /path/to/local/directory user@remote_host:/path/to/remote/directory/
   ```

4. Menyalin file menggunakan port SSH yang berbeda:
   ```bash
   scp -P 2222 /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
   ```

## Tips
- Selalu pastikan bahwa Anda memiliki izin yang tepat untuk mengakses file dan direktori yang ingin Anda salin.
- Gunakan opsi `-v` untuk membantu dalam pemecahan masalah jika transfer tidak berhasil.
- Pertimbangkan untuk menggunakan kunci SSH untuk autentikasi yang lebih aman daripada menggunakan kata sandi.