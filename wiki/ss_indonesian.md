# [Linux] Bash ss Penggunaan: Menampilkan informasi soket jaringan

## Overview
Perintah `ss` adalah alat yang digunakan untuk menampilkan informasi tentang soket jaringan di sistem Linux. Ini memberikan informasi yang lebih cepat dan lebih detail dibandingkan dengan perintah `netstat`, termasuk soket TCP, UDP, dan UNIX.

## Usage
Berikut adalah sintaks dasar dari perintah `ss`:

```bash
ss [options] [arguments]
```

## Common Options
- `-t`: Menampilkan soket TCP.
- `-u`: Menampilkan soket UDP.
- `-l`: Menampilkan soket yang sedang mendengarkan.
- `-p`: Menampilkan proses yang menggunakan soket.
- `-n`: Menampilkan alamat dan port dalam format numerik.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `ss`:

1. Menampilkan semua soket TCP:
   ```bash
   ss -t
   ```

2. Menampilkan semua soket UDP:
   ```bash
   ss -u
   ```

3. Menampilkan soket yang sedang mendengarkan:
   ```bash
   ss -l
   ```

4. Menampilkan soket beserta proses yang menggunakannya:
   ```bash
   ss -p
   ```

5. Menampilkan semua soket dengan alamat dan port dalam format numerik:
   ```bash
   ss -n
   ```

## Tips
- Gunakan opsi `-tuln` secara bersamaan untuk mendapatkan daftar lengkap soket yang mendengarkan baik TCP maupun UDP dalam format numerik.
- Untuk memantau perubahan dalam soket secara real-time, Anda dapat menggunakan perintah `watch` bersama dengan `ss`, seperti:
  ```bash
  watch ss -tuln
  ```
- Pastikan Anda menjalankan perintah ini dengan hak akses yang sesuai jika ingin melihat semua soket yang digunakan oleh proses sistem.