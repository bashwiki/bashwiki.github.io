# [Linux] Bash iostat Penggunaan: Memantau Statistik I/O

## Overview
Perintah `iostat` digunakan untuk memantau statistik input/output (I/O) dari sistem, termasuk penggunaan CPU dan aktivitas disk. Ini membantu pengguna dalam menganalisis kinerja sistem dan mengidentifikasi potensi masalah.

## Usage
Berikut adalah sintaks dasar dari perintah `iostat`:

```
iostat [options] [arguments]
```

## Common Options
- `-c`: Menampilkan statistik CPU.
- `-d`: Menampilkan statistik disk.
- `-x`: Menampilkan statistik disk dengan informasi yang lebih mendetail.
- `-t`: Menampilkan waktu dan tanggal saat laporan dibuat.
- `-p`: Menampilkan statistik untuk partisi disk tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan `iostat`:

1. Menampilkan statistik CPU dan disk secara default:
   ```bash
   iostat
   ```

2. Menampilkan statistik CPU saja:
   ```bash
   iostat -c
   ```

3. Menampilkan statistik disk dengan informasi mendetail:
   ```bash
   iostat -dx
   ```

4. Menampilkan statistik untuk partisi tertentu:
   ```bash
   iostat -p sda
   ```

5. Menampilkan laporan dengan timestamp:
   ```bash
   iostat -t
   ```

## Tips
- Gunakan `iostat` secara berkala untuk memantau kinerja sistem dan mendeteksi masalah sebelum menjadi serius.
- Kombinasikan `iostat` dengan alat pemantauan lainnya seperti `vmstat` atau `top` untuk analisis yang lebih komprehensif.
- Simpan output `iostat` ke dalam file untuk analisis lebih lanjut dengan menggunakan redirection, seperti:
  ```bash
  iostat -dx > iostat_report.txt
  ```