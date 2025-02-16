# [Linux] Bash mkdir Penggunaan: Membuat direktori baru

## Overview
Perintah `mkdir` digunakan untuk membuat direktori baru di sistem file. Dengan menggunakan perintah ini, pengguna dapat mengorganisir file dan folder dengan lebih baik.

## Usage
Berikut adalah sintaks dasar dari perintah `mkdir`:

```
mkdir [options] [arguments]
```

## Common Options
- `-p`: Membuat direktori secara rekursif, termasuk semua direktori induk yang diperlukan.
- `-v`: Menampilkan pesan yang menunjukkan direktori yang telah dibuat.
- `-m`: Menentukan mode izin untuk direktori yang baru dibuat.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `mkdir`:

1. **Membuat direktori baru**:
   ```bash
   mkdir folder_baru
   ```

2. **Membuat beberapa direktori sekaligus**:
   ```bash
   mkdir folder1 folder2 folder3
   ```

3. **Membuat direktori secara rekursif**:
   ```bash
   mkdir -p /path/to/folder/baru
   ```

4. **Membuat direktori dengan izin tertentu**:
   ```bash
   mkdir -m 755 folder_izin
   ```

5. **Menampilkan pesan saat membuat direktori**:
   ```bash
   mkdir -v folder_ditampilkan
   ```

## Tips
- Selalu gunakan opsi `-p` jika Anda tidak yakin apakah direktori induk sudah ada, untuk menghindari kesalahan.
- Gunakan opsi `-v` untuk mendapatkan konfirmasi visual saat membuat direktori, terutama saat membuat banyak direktori.
- Pertimbangkan untuk menetapkan izin yang tepat saat membuat direktori baru untuk menjaga keamanan file Anda.