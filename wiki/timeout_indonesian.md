# [Linux] Bash timeout Penggunaan: Menghentikan proses setelah waktu tertentu

## Overview
Perintah `timeout` digunakan untuk menjalankan sebuah perintah dengan batasan waktu tertentu. Jika perintah tersebut tidak selesai dalam waktu yang ditentukan, `timeout` akan menghentikan proses tersebut secara otomatis. Ini sangat berguna untuk mencegah proses yang berjalan terlalu lama.

## Usage
Berikut adalah sintaks dasar dari perintah `timeout`:

```
timeout [options] [durasi] [perintah] [argumen...]
```

## Common Options
- `-k, --kill-after=DURASI`: Menghentikan proses dengan sinyal tertentu setelah durasi yang ditentukan, jika proses masih berjalan.
- `-s, --signal=SIGNAL`: Menentukan sinyal yang akan dikirim ke proses. Secara default, sinyal yang digunakan adalah `TERM`.
- `--preserve-status`: Mengembalikan status keluar dari perintah yang dijalankan, bukan status keluar dari `timeout`.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `timeout`:

1. Menjalankan perintah `sleep` selama 5 detik dan menghentikannya jika melebihi waktu:
   ```bash
   timeout 5s sleep 10
   ```

2. Menghentikan proses `ping` setelah 3 detik:
   ```bash
   timeout 3s ping google.com
   ```

3. Menggunakan sinyal `SIGKILL` untuk menghentikan proses setelah 10 detik:
   ```bash
   timeout -s KILL 10s sleep 30
   ```

4. Menjalankan skrip dengan batas waktu 1 menit dan mengembalikan status keluar dari skrip:
   ```bash
   timeout --preserve-status 1m ./myscript.sh
   ```

## Tips
- Selalu tentukan durasi yang cukup untuk proses yang Anda jalankan agar tidak terhenti secara prematur.
- Gunakan opsi `--preserve-status` jika Anda ingin mendapatkan status keluar dari perintah yang dijalankan, bukan dari `timeout`.
- Cobalah menggunakan sinyal yang berbeda dengan opsi `-s` untuk mengontrol bagaimana proses dihentikan, tergantung pada kebutuhan Anda.