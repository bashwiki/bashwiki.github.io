# [Linux] Bash renice Penggunaan: Mengubah prioritas proses

## Overview
Perintah `renice` digunakan untuk mengubah prioritas eksekusi dari proses yang sedang berjalan di sistem operasi Linux. Dengan mengubah prioritas ini, Anda dapat mengatur seberapa banyak sumber daya CPU yang dialokasikan untuk proses tertentu, yang dapat membantu dalam mengelola kinerja sistem.

## Usage
Sintaks dasar dari perintah `renice` adalah sebagai berikut:

```bash
renice [options] [arguments]
```

## Common Options
- `-n`, `--priority`: Menentukan nilai prioritas baru. Nilai ini dapat berupa angka dari -20 (prioritas tertinggi) hingga 19 (prioritas terendah).
- `-p`, `--pid`: Mengubah prioritas untuk proses dengan ID proses tertentu.
- `-g`, `--pgroup`: Mengubah prioritas untuk grup proses tertentu.
- `-u`, `--user`: Mengubah prioritas untuk semua proses yang dimiliki oleh pengguna tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `renice`:

1. Mengubah prioritas proses dengan ID 1234 menjadi 10:
   ```bash
   renice 10 -p 1234
   ```

2. Mengubah prioritas semua proses yang dimiliki oleh pengguna "john" menjadi 5:
   ```bash
   renice 5 -u john
   ```

3. Mengubah prioritas grup proses dengan ID grup 5678 menjadi -5:
   ```bash
   renice -5 -g 5678
   ```

4. Menampilkan prioritas dari proses yang sedang berjalan:
   ```bash
   ps -o pid,ni,cmd
   ```

## Tips
- Pastikan Anda memiliki hak akses yang cukup untuk mengubah prioritas proses, terutama jika Anda mencoba mengubah proses yang dimiliki oleh pengguna lain.
- Gunakan nilai prioritas yang lebih rendah (misalnya, -10) untuk memberikan lebih banyak sumber daya CPU kepada proses yang penting.
- Periksa prioritas proses yang sedang berjalan secara berkala untuk memastikan sistem tetap responsif.