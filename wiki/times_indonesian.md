# [Linux] Bash times penggunaan: Mengukur waktu eksekusi proses

## Overview
Perintah `times` dalam Bash digunakan untuk menampilkan waktu CPU yang digunakan oleh shell dan semua proses yang diluncurkan dari shell tersebut. Ini memberikan informasi tentang berapa lama waktu yang dihabiskan dalam mode pengguna dan mode sistem.

## Usage
Berikut adalah sintaks dasar dari perintah `times`:

```bash
times [options] [arguments]
```

## Common Options
Perintah `times` tidak memiliki banyak opsi, tetapi berikut adalah beberapa yang umum digunakan:
- `-p`: Menampilkan waktu dalam format POSIX yang lebih ringkas.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `times`:

1. **Menampilkan waktu CPU untuk shell saat ini:**
   ```bash
   times
   ```

2. **Menggunakan opsi -p untuk format yang lebih ringkas:**
   ```bash
   times -p
   ```

3. **Menjalankan beberapa perintah dan kemudian menampilkan waktu CPU:**
   ```bash
   sleep 2
   ls
   times
   ```

## Tips
- Gunakan `times` setelah menjalankan beberapa perintah untuk mendapatkan gambaran tentang waktu yang dihabiskan untuk setiap proses.
- Perintah ini sangat berguna dalam skrip untuk menganalisis kinerja dan efisiensi eksekusi.