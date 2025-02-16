# [Linux] Bash dmesg Penggunaan: Menampilkan pesan kernel

## Overview
Perintah `dmesg` digunakan untuk menampilkan pesan dari buffer ring kernel. Ini berguna untuk melihat informasi tentang perangkat keras, driver, dan berbagai peristiwa yang terjadi selama booting sistem atau saat perangkat keras terhubung dan terputus.

## Usage
Berikut adalah sintaks dasar dari perintah `dmesg`:

```bash
dmesg [options] [arguments]
```

## Common Options
- `-C` : Menghapus buffer pesan kernel.
- `-c` : Menampilkan pesan dan kemudian menghapus buffer.
- `-n level` : Mengatur level pesan yang akan ditampilkan.
- `-T` : Menampilkan waktu dalam format yang dapat dibaca manusia.
- `-H` : Menampilkan pesan dalam format yang lebih mudah dibaca.

## Common Examples
Berikut adalah beberapa contoh penggunaan `dmesg`:

1. Menampilkan semua pesan kernel:
   ```bash
   dmesg
   ```

2. Menampilkan pesan kernel terbaru:
   ```bash
   dmesg | tail
   ```

3. Menghapus buffer pesan kernel setelah menampilkannya:
   ```bash
   dmesg -c
   ```

4. Menampilkan pesan dengan waktu yang dapat dibaca manusia:
   ```bash
   dmesg -T
   ```

5. Menampilkan pesan dengan level tertentu:
   ```bash
   dmesg -n 3
   ```

## Tips
- Gunakan `dmesg | less` untuk menggulir pesan dengan lebih nyaman.
- Periksa `dmesg` setelah menghubungkan perangkat baru untuk mendapatkan informasi tentang perangkat tersebut.
- Jika Anda mengalami masalah dengan perangkat keras, `dmesg` adalah tempat yang baik untuk memulai pemecahan masalah.