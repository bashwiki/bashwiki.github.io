# [Linux] Bash rar Penggunaan: Mengompres dan mengekstrak file

## Overview
Perintah `rar` digunakan untuk mengompres dan mengekstrak file dalam format RAR. Format RAR dikenal karena kemampuannya untuk menghasilkan file kompresi yang lebih kecil dan mendukung pengarsipan multi-volume.

## Usage
Berikut adalah sintaks dasar dari perintah `rar`:

```bash
rar [options] [arguments]
```

## Common Options
- `a`: Menambahkan file ke arsip.
- `e`: Mengekstrak file dari arsip tanpa mempertahankan struktur direktori.
- `x`: Mengekstrak file dari arsip dengan mempertahankan struktur direktori.
- `t`: Menguji integritas arsip.
- `v`: Menampilkan informasi rinci tentang arsip.

## Common Examples
1. **Membuat arsip RAR baru:**
   ```bash
   rar a arsip.rar file1.txt file2.txt
   ```
   Perintah ini akan membuat arsip bernama `arsip.rar` yang berisi `file1.txt` dan `file2.txt`.

2. **Mengekstrak file dari arsip:**
   ```bash
   rar x arsip.rar
   ```
   Perintah ini akan mengekstrak semua file dari `arsip.rar` ke direktori saat ini.

3. **Menguji integritas arsip:**
   ```bash
   rar t arsip.rar
   ```
   Perintah ini akan memeriksa apakah `arsip.rar` tidak korup.

4. **Menambahkan file ke arsip yang sudah ada:**
   ```bash
   rar a arsip.rar file3.txt
   ```
   Perintah ini akan menambahkan `file3.txt` ke `arsip.rar` yang sudah ada.

## Tips
- Selalu gunakan opsi `t` setelah membuat arsip untuk memastikan tidak ada kesalahan dalam proses kompresi.
- Gunakan opsi `v` untuk mendapatkan informasi lebih lanjut tentang arsip, seperti ukuran dan jumlah file.
- Pertimbangkan untuk menggunakan kompresi tingkat tinggi dengan opsi `-m5` untuk mengurangi ukuran file lebih lanjut, meskipun ini akan memakan waktu lebih lama.