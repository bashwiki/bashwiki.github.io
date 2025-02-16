# [Linux] Bash mpstat Penggunaan: Memantau Statistik CPU

## Overview
Perintah `mpstat` digunakan untuk menampilkan statistik penggunaan CPU secara real-time. Ini membantu pengguna untuk menganalisis kinerja CPU dan mengidentifikasi potensi masalah.

## Usage
Berikut adalah sintaks dasar dari perintah `mpstat`:

```bash
mpstat [options] [arguments]
```

## Common Options
- `-P ALL`: Menampilkan statistik untuk semua CPU.
- `-u`: Menampilkan penggunaan CPU dalam persentase.
- `-r`: Menampilkan statistik tentang penggunaan memori.
- `-h`: Menampilkan informasi bantuan tentang penggunaan perintah.

## Common Examples
Berikut adalah beberapa contoh penggunaan `mpstat`:

1. Menampilkan statistik penggunaan CPU untuk semua CPU:
   ```bash
   mpstat -P ALL
   ```

2. Menampilkan penggunaan CPU dalam persentase:
   ```bash
   mpstat -u
   ```

3. Menampilkan statistik penggunaan memori:
   ```bash
   mpstat -r
   ```

4. Menampilkan statistik CPU setiap 5 detik:
   ```bash
   mpstat 5
   ```

## Tips
- Gunakan opsi `-P ALL` untuk mendapatkan gambaran menyeluruh tentang kinerja semua inti CPU.
- Jalankan `mpstat` dalam interval waktu tertentu untuk memantau perubahan penggunaan CPU secara real-time.
- Perhatikan nilai `idle` untuk memahami seberapa banyak CPU yang tidak digunakan, yang dapat membantu dalam pengambilan keputusan terkait sumber daya.