# [Linux] Bash groups penggunaan: Menampilkan grup pengguna

## Overview
Perintah `groups` digunakan untuk menampilkan grup-grup yang menjadi anggota bagi pengguna tertentu. Jika tidak ada nama pengguna yang diberikan, perintah ini akan menampilkan grup untuk pengguna yang sedang aktif saat ini.

## Usage
Berikut adalah sintaks dasar dari perintah `groups`:

```bash
groups [options] [arguments]
```

## Common Options
- `-h`, `--help`: Menampilkan bantuan penggunaan perintah.
- `-n`, `--no-name`: Menampilkan ID grup tanpa nama grup.
- `--version`: Menampilkan versi dari perintah `groups`.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `groups`:

1. Menampilkan grup untuk pengguna yang sedang aktif:
   ```bash
   groups
   ```

2. Menampilkan grup untuk pengguna tertentu:
   ```bash
   groups username
   ```

3. Menampilkan grup tanpa nama grup, hanya ID grup:
   ```bash
   groups -n username
   ```

4. Menampilkan bantuan penggunaan:
   ```bash
   groups --help
   ```

## Tips
- Gunakan perintah `groups` untuk dengan cepat memeriksa keanggotaan grup pengguna, terutama saat mengelola izin akses.
- Jika Anda tidak yakin tentang nama pengguna, Anda dapat menggunakan perintah `whoami` untuk mengetahui nama pengguna yang sedang aktif.
- Perintah ini sangat berguna dalam lingkungan multi-pengguna untuk memastikan bahwa pengguna memiliki akses yang tepat ke sumber daya.