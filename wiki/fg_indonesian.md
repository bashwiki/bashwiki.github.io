# [Linux] Bash fg Penggunaan: Mengembalikan proses ke latar depan

## Overview
Perintah `fg` dalam Bash digunakan untuk mengembalikan proses yang berjalan di latar belakang ke latar depan. Ini berguna ketika Anda ingin berinteraksi kembali dengan proses yang sebelumnya Anda jalankan tetapi tidak terlihat di terminal.

## Usage
Berikut adalah sintaks dasar dari perintah `fg`:

```
fg [options] [job_spec]
```

## Common Options
- `job_spec`: Menentukan proses tertentu yang ingin Anda kembalikan ke latar depan. Anda dapat menggunakan nomor pekerjaan (job number) atau nama proses.
- `-n`: Mengembalikan proses terbaru yang berjalan di latar belakang ke latar depan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `fg`:

1. **Mengembalikan proses terakhir yang berjalan di latar belakang:**
   ```bash
   fg
   ```

2. **Mengembalikan proses tertentu dengan nomor pekerjaan:**
   ```bash
   fg %1
   ```

3. **Mengembalikan proses terbaru yang berjalan di latar belakang:**
   ```bash
   fg -n
   ```

4. **Mengembalikan proses berdasarkan nama:**
   ```bash
   fg %nama_proses
   ```

## Tips
- Pastikan Anda mengetahui nomor pekerjaan dari proses yang ingin Anda kembalikan. Anda dapat menggunakan perintah `jobs` untuk melihat daftar proses latar belakang.
- Jika Anda ingin menghentikan proses yang sedang berjalan di latar depan, Anda dapat menggunakan `Ctrl + C`.
- Gunakan `bg` untuk melanjutkan proses ke latar belakang jika Anda tidak ingin mengembalikannya ke latar depan.