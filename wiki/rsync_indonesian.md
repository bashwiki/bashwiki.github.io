# [Linux] Bash rsync Penggunaan: Menyalin dan menyinkronkan file

## Overview
Perintah `rsync` adalah alat yang sangat berguna untuk menyalin dan menyinkronkan file dan direktori antara lokasi yang berbeda, baik di dalam sistem lokal maupun melalui jaringan. Dengan `rsync`, Anda dapat mentransfer data dengan efisien, hanya menyalin bagian yang berubah dari file, sehingga menghemat waktu dan bandwidth.

## Usage
Berikut adalah sintaks dasar dari perintah `rsync`:

```
rsync [options] [source] [destination]
```

## Common Options
Berikut adalah beberapa opsi umum yang sering digunakan dengan `rsync`:

- `-a` : Mode arsip; menyalin file dan direktori secara rekursif dan mempertahankan atribut file.
- `-v` : Menampilkan output yang lebih rinci (verbose).
- `-z` : Mengompresi data selama transfer untuk menghemat bandwidth.
- `-r` : Menyalin direktori secara rekursif.
- `--delete` : Menghapus file di tujuan yang tidak ada di sumber.
- `-e` : Menentukan shell yang digunakan untuk koneksi (misalnya, SSH).

## Common Examples
Berikut adalah beberapa contoh penggunaan `rsync`:

1. Menyalin file dari direktori lokal ke direktori lokal:
   ```bash
   rsync -av /path/to/source/ /path/to/destination/
   ```

2. Menyalin file dari server jarak jauh ke lokal menggunakan SSH:
   ```bash
   rsync -avz user@remote:/path/to/source/ /path/to/destination/
   ```

3. Menyinkronkan direktori dan menghapus file yang tidak ada di sumber:
   ```bash
   rsync -av --delete /path/to/source/ /path/to/destination/
   ```

4. Menyalin file dengan kompresi untuk menghemat bandwidth:
   ```bash
   rsync -avz /path/to/source/ user@remote:/path/to/destination/
   ```

## Tips
- Selalu gunakan opsi `-n` (dry run) untuk melihat apa yang akan dilakukan `rsync` tanpa benar-benar melakukan transfer. Ini membantu menghindari kesalahan.
- Pastikan untuk menambahkan trailing slash (`/`) pada direktori sumber jika Anda ingin menyalin isi direktori, bukan direktori itu sendiri.
- Gunakan opsi `-e ssh` untuk meningkatkan keamanan saat mentransfer file melalui jaringan yang tidak aman.