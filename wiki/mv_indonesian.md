# [Linux] Bash mv Penggunaan: Memindahkan atau Mengganti Nama Berkas

## Overview
Perintah `mv` dalam Bash digunakan untuk memindahkan atau mengganti nama berkas dan direktori. Ini adalah alat yang sangat berguna dalam manajemen berkas di sistem operasi berbasis Unix.

## Usage
Berikut adalah sintaks dasar dari perintah `mv`:

```bash
mv [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `mv`:

- `-i`: Menampilkan prompt konfirmasi sebelum menimpa berkas yang ada.
- `-u`: Hanya memindahkan berkas jika berkas sumber lebih baru daripada berkas tujuan atau jika berkas tujuan tidak ada.
- `-v`: Menampilkan informasi tentang berkas yang sedang dipindahkan atau diganti namanya.
- `-n`: Tidak menimpa berkas yang sudah ada di tujuan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `mv`:

1. **Memindahkan berkas ke direktori lain:**
   ```bash
   mv file.txt /path/to/directory/
   ```

2. **Mengganti nama berkas:**
   ```bash
   mv oldname.txt newname.txt
   ```

3. **Memindahkan berkas dan menampilkan proses:**
   ```bash
   mv -v file.txt /path/to/directory/
   ```

4. **Mengganti nama berkas dengan konfirmasi:**
   ```bash
   mv -i file.txt /path/to/directory/
   ```

5. **Hanya memindahkan berkas yang lebih baru:**
   ```bash
   mv -u file.txt /path/to/directory/
   ```

## Tips
- Selalu gunakan opsi `-i` jika Anda tidak ingin secara tidak sengaja menimpa berkas yang ada.
- Gunakan opsi `-v` untuk mendapatkan umpan balik visual saat memindahkan berkas, terutama saat memindahkan banyak berkas sekaligus.
- Pastikan untuk memeriksa jalur direktori tujuan sebelum memindahkan berkas untuk menghindari kesalahan.