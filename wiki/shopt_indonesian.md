# [Linux] Bash shopt Penggunaan: Mengelola opsi shell

## Overview
Perintah `shopt` dalam Bash digunakan untuk mengelola opsi shell yang dapat mengubah perilaku shell. Dengan `shopt`, pengguna dapat mengaktifkan atau menonaktifkan fitur tertentu yang mempengaruhi cara shell beroperasi.

## Usage
Sintaks dasar untuk menggunakan `shopt` adalah sebagai berikut:

```bash
shopt [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `shopt`:

- `-s` : Mengaktifkan opsi yang ditentukan.
- `-u` : Menonaktifkan opsi yang ditentukan.
- `-p` : Menampilkan semua opsi yang saat ini diatur beserta nilainya.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `shopt`:

1. **Mengaktifkan opsi `nullglob`**:
   Opsi ini membuat wildcard yang tidak cocok dengan file menjadi kosong.
   ```bash
   shopt -s nullglob
   ```

2. **Menonaktifkan opsi `dotglob`**:
   Opsi ini mengontrol apakah file yang dimulai dengan titik (.) akan termasuk dalam hasil glob.
   ```bash
   shopt -u dotglob
   ```

3. **Menampilkan semua opsi yang diatur**:
   Untuk melihat semua opsi yang saat ini diatur di shell.
   ```bash
   shopt -p
   ```

4. **Mengaktifkan opsi `histappend`**:
   Opsi ini memungkinkan riwayat perintah ditambahkan ke file riwayat alih-alih menimpa.
   ```bash
   shopt -s histappend
   ```

## Tips
- Selalu periksa opsi yang saat ini diatur dengan `shopt -p` sebelum mengubahnya untuk memahami dampaknya.
- Gunakan `shopt` dalam skrip untuk memastikan bahwa skrip Anda berjalan dengan perilaku yang diharapkan, terutama saat menggunakan fitur globbing.
- Ingat untuk menonaktifkan opsi yang tidak lagi diperlukan untuk menjaga lingkungan shell Anda tetap bersih dan teratur.