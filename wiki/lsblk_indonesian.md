# [Linux] Bash lsblk Penggunaan: Menampilkan informasi blok perangkat

## Overview
Perintah `lsblk` digunakan untuk menampilkan informasi tentang perangkat blok di sistem Linux. Ini termasuk hard disk, partisi, dan perangkat penyimpanan lainnya. Dengan `lsblk`, pengguna dapat dengan mudah melihat struktur perangkat penyimpanan dan bagaimana mereka terhubung.

## Usage
Sintaks dasar dari perintah `lsblk` adalah sebagai berikut:

```bash
lsblk [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `lsblk`:

- `-a`, `--all`: Menampilkan semua perangkat, termasuk yang tidak terpasang.
- `-f`, `--fs`: Menampilkan informasi sistem file pada perangkat.
- `-l`, `--list`: Menampilkan output dalam format daftar.
- `-o`, `--output`: Menentukan kolom mana yang akan ditampilkan.
- `-n`, `--noheadings`: Menyembunyikan judul kolom dalam output.

## Common Examples
Berikut adalah beberapa contoh penggunaan `lsblk`:

1. Menampilkan semua perangkat blok:
   ```bash
   lsblk
   ```

2. Menampilkan semua perangkat termasuk yang tidak terpasang:
   ```bash
   lsblk -a
   ```

3. Menampilkan informasi sistem file dari perangkat:
   ```bash
   lsblk -f
   ```

4. Menampilkan output dalam format daftar:
   ```bash
   lsblk -l
   ```

5. Menentukan kolom yang ditampilkan, misalnya hanya nama dan ukuran:
   ```bash
   lsblk -o NAME,SIZE
   ```

## Tips
- Gunakan opsi `-f` untuk mendapatkan informasi lebih detail tentang sistem file, seperti tipe dan label.
- Kombinasikan `lsblk` dengan perintah lain seperti `grep` untuk memfilter hasil yang diinginkan.
- Selalu gunakan opsi `-n` jika Anda ingin mengekspor output ke file untuk menghindari judul kolom yang tidak perlu.