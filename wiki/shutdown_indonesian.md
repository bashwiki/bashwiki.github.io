# [Linux] Bash shutdown Penggunaan: Mematikan atau merestart sistem

## Overview
Perintah `shutdown` digunakan untuk mematikan atau merestart sistem Linux secara aman. Dengan menggunakan perintah ini, Anda dapat menjadwalkan waktu untuk mematikan komputer atau memberikan pesan kepada pengguna lain sebelum sistem dimatikan.

## Usage
Sintaks dasar dari perintah `shutdown` adalah sebagai berikut:

```bash
shutdown [options] [time] [message]
```

## Common Options
Berikut adalah beberapa opsi umum untuk perintah `shutdown`:

- `-h` : Mematikan sistem.
- `-r` : Merestart sistem.
- `-c` : Membatalkan shutdown yang dijadwalkan.
- `+m` : Menjadwalkan shutdown dalam m menit.
- `hh:mm` : Menjadwalkan shutdown pada waktu tertentu (format 24 jam).

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `shutdown`:

1. Mematikan sistem segera:
   ```bash
   shutdown -h now
   ```

2. Merestart sistem segera:
   ```bash
   shutdown -r now
   ```

3. Menjadwalkan shutdown dalam 10 menit:
   ```bash
   shutdown -h +10
   ```

4. Menjadwalkan shutdown pada pukul 22:00:
   ```bash
   shutdown -h 22:00
   ```

5. Membatalkan shutdown yang dijadwalkan:
   ```bash
   shutdown -c
   ```

6. Mengirim pesan kepada pengguna sebelum mematikan:
   ```bash
   shutdown -h +5 "Sistem akan dimatikan dalam 5 menit. Silakan simpan pekerjaan Anda."
   ```

## Tips
- Selalu beri tahu pengguna lain sebelum mematikan sistem, terutama jika Anda bekerja di lingkungan multi-user.
- Gunakan opsi `-c` untuk membatalkan shutdown jika Anda berubah pikiran.
- Pertimbangkan untuk menggunakan `shutdown` dalam skrip otomatisasi untuk mematikan sistem pada waktu tertentu.