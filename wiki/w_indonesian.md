# [Linux] Bash w: Menampilkan informasi pengguna yang sedang aktif

## Overview
Perintah `w` digunakan untuk menampilkan informasi tentang pengguna yang sedang aktif di sistem Linux. Informasi yang ditampilkan mencakup nama pengguna, waktu login, dan aktivitas yang sedang dilakukan oleh pengguna.

## Usage
Berikut adalah sintaks dasar dari perintah `w`:

```bash
w [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `w`:

- `-h`: Menghilangkan header dari output.
- `-s`: Menampilkan output dalam format ringkas.
- `-f`: Menampilkan informasi tentang pengguna yang terhubung melalui SSH.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `w`:

1. Menampilkan informasi pengguna yang sedang aktif:
   ```bash
   w
   ```

2. Menampilkan informasi tanpa header:
   ```bash
   w -h
   ```

3. Menampilkan informasi dalam format ringkas:
   ```bash
   w -s
   ```

4. Menampilkan informasi pengguna yang terhubung melalui SSH:
   ```bash
   w -f
   ```

## Tips
- Gunakan perintah `w` secara berkala untuk memantau aktivitas pengguna di sistem Anda.
- Kombinasikan dengan perintah lain seperti `grep` untuk mencari pengguna tertentu dalam output.
- Perhatikan kolom "idle" untuk mengetahui berapa lama pengguna tidak aktif.