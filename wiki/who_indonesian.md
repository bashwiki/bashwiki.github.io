# [Linux] Bash who Penggunaan: Menampilkan pengguna yang sedang masuk

## Overview
Perintah `who` digunakan untuk menampilkan daftar pengguna yang sedang masuk ke sistem. Informasi yang ditampilkan mencakup nama pengguna, terminal yang digunakan, waktu masuk, dan alamat IP atau hostname jika tersedia.

## Usage
Sintaks dasar dari perintah `who` adalah sebagai berikut:

```
who [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `who`:

- `-a`: Menampilkan semua informasi yang tersedia, termasuk pengguna yang tidak aktif.
- `-b`: Menampilkan waktu terakhir sistem di-boot.
- `-q`: Menampilkan hanya nama pengguna dan jumlah pengguna yang sedang masuk.
- `--help`: Menampilkan bantuan tentang penggunaan perintah `who`.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `who`:

1. Menampilkan daftar pengguna yang sedang masuk:
   ```bash
   who
   ```

2. Menampilkan semua informasi pengguna, termasuk yang tidak aktif:
   ```bash
   who -a
   ```

3. Menampilkan waktu terakhir sistem di-boot:
   ```bash
   who -b
   ```

4. Menampilkan hanya nama pengguna dan jumlah pengguna yang sedang masuk:
   ```bash
   who -q
   ```

## Tips
- Gunakan opsi `-a` untuk mendapatkan informasi lebih lengkap tentang sesi pengguna.
- Perintah `who` dapat digabungkan dengan perintah lain seperti `grep` untuk mencari pengguna tertentu.
- Untuk informasi lebih lanjut tentang pengguna, pertimbangkan untuk menggunakan perintah `w`, yang memberikan informasi lebih detail tentang aktivitas pengguna.