# [Linux] Bash nohup Penggunaan: Menjalankan proses di latar belakang

## Overview
Perintah `nohup` (no hang up) digunakan untuk menjalankan proses di latar belakang tanpa terpengaruh oleh sesi terminal yang sedang berjalan. Ini sangat berguna ketika Anda ingin menjalankan skrip atau aplikasi yang memerlukan waktu lama dan tidak ingin proses tersebut terhenti jika Anda keluar dari sesi terminal.

## Usage
Sintaks dasar dari perintah `nohup` adalah sebagai berikut:

```bash
nohup [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `nohup`:

- `&` : Menjalankan proses di latar belakang.
- `-h` : Menampilkan bantuan dan informasi tentang penggunaan `nohup`.
- `-v` : Menampilkan versi dari `nohup`.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `nohup`:

1. Menjalankan skrip shell di latar belakang:
   ```bash
   nohup ./myscript.sh &
   ```

2. Menjalankan perintah `ping` tanpa terputus:
   ```bash
   nohup ping google.com &
   ```

3. Menyimpan output ke file tertentu:
   ```bash
   nohup ./long_running_task > output.log &
   ```

4. Menjalankan aplikasi Python di latar belakang:
   ```bash
   nohup python my_script.py &
   ```

## Tips
- Selalu gunakan `&` di akhir perintah untuk memastikan proses berjalan di latar belakang.
- Periksa file `nohup.out` untuk melihat output dari proses yang dijalankan jika tidak menentukan file output lain.
- Gunakan perintah `jobs` untuk melihat daftar proses yang berjalan di latar belakang.