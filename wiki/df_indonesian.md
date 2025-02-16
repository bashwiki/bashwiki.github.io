# [Linux] Bash df Penggunaan: Menampilkan informasi penggunaan disk

## Overview
Perintah `df` digunakan untuk menampilkan informasi tentang penggunaan ruang disk pada sistem file. Ini memberikan gambaran umum tentang berapa banyak ruang yang digunakan dan tersedia di setiap sistem file yang terpasang.

## Usage
Sintaks dasar dari perintah `df` adalah sebagai berikut:

```bash
df [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `df`:

- `-h`: Menampilkan ukuran dalam format yang lebih mudah dibaca (misalnya, KB, MB, GB).
- `-T`: Menampilkan tipe sistem file.
- `-a`: Menampilkan semua sistem file, termasuk yang tidak terpasang.
- `-i`: Menampilkan informasi tentang inode, bukan penggunaan ruang disk.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `df`:

1. Menampilkan informasi penggunaan disk dasar:
   ```bash
   df
   ```

2. Menampilkan informasi dalam format yang lebih mudah dibaca:
   ```bash
   df -h
   ```

3. Menampilkan tipe sistem file untuk setiap sistem file:
   ```bash
   df -T
   ```

4. Menampilkan semua sistem file, termasuk yang tidak terpasang:
   ```bash
   df -a
   ```

5. Menampilkan informasi tentang inode:
   ```bash
   df -i
   ```

## Tips
- Gunakan opsi `-h` untuk memudahkan pemahaman ukuran ruang disk, terutama jika Anda bekerja dengan sistem file besar.
- Periksa penggunaan inode dengan opsi `-i` jika Anda mengalami masalah dengan membuat file baru, karena bisa jadi Anda kehabisan inode meskipun ruang disk masih tersedia.
- Kombinasikan opsi untuk mendapatkan informasi yang lebih lengkap, misalnya `df -hT` untuk melihat ukuran dan tipe sistem file secara bersamaan.