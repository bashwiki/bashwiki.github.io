# [Linux] Bash top Penggunaan: Menampilkan proses yang berjalan

## Overview
Perintah `top` digunakan untuk menampilkan informasi tentang proses-proses yang sedang berjalan di sistem Linux. Ini memberikan tampilan real-time dari penggunaan CPU, memori, dan berbagai statistik lainnya, sehingga pengguna dapat memantau kinerja sistem dan mengidentifikasi proses yang memerlukan perhatian.

## Usage
Sintaks dasar dari perintah `top` adalah sebagai berikut:

```bash
top [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `top`:

- `-d <delay>`: Mengatur interval pembaruan tampilan dalam detik.
- `-n <number>`: Menentukan jumlah pembaruan yang akan ditampilkan sebelum keluar.
- `-u <user>`: Menampilkan hanya proses yang dimiliki oleh pengguna tertentu.
- `-p <pid>`: Menampilkan hanya proses dengan ID proses tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `top`:

1. Menjalankan `top` dengan pembaruan setiap 2 detik:
   ```bash
   top -d 2
   ```

2. Menampilkan hanya proses yang dimiliki oleh pengguna `john`:
   ```bash
   top -u john
   ```

3. Menjalankan `top` dan menampilkan hanya proses dengan ID 1234:
   ```bash
   top -p 1234
   ```

4. Menjalankan `top` dan menghentikan setelah 5 pembaruan:
   ```bash
   top -n 5
   ```

## Tips
- Gunakan tombol `h` saat dalam tampilan `top` untuk mendapatkan bantuan tentang kontrol dan opsi lainnya.
- Untuk mengurutkan proses berdasarkan penggunaan CPU, tekan tombol `P` saat dalam tampilan `top`.
- Anda dapat menghentikan proses langsung dari tampilan `top` dengan memilih proses dan menekan `k`, kemudian memasukkan ID proses yang ingin dihentikan.