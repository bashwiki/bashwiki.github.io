# [Linux] Bash 7z Penggunaan: Mengompres dan mengekstrak file

## Overview
Perintah `7z` adalah alat baris perintah yang digunakan untuk mengompres dan mengekstrak file dalam berbagai format. Ini adalah bagian dari program 7-Zip, yang terkenal karena kemampuannya untuk menghasilkan file arsip dengan rasio kompresi yang tinggi.

## Usage
Sintaks dasar dari perintah `7z` adalah sebagai berikut:

```
7z [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `7z`:

- `a`: Menambahkan file ke dalam arsip.
- `x`: Mengekstrak file dari arsip.
- `l`: Menampilkan daftar file dalam arsip.
- `d`: Menghapus file dari arsip.
- `t`: Menguji integritas arsip.

## Common Examples

1. **Mengompres file menjadi arsip**:
   ```bash
   7z a arsip.7z file1.txt file2.txt
   ```

2. **Mengekstrak file dari arsip**:
   ```bash
   7z x arsip.7z
   ```

3. **Menampilkan daftar file dalam arsip**:
   ```bash
   7z l arsip.7z
   ```

4. **Menghapus file dari arsip**:
   ```bash
   7z d arsip.7z file1.txt
   ```

5. **Menguji integritas arsip**:
   ```bash
   7z t arsip.7z
   ```

## Tips
- Selalu periksa ukuran file setelah kompresi untuk memastikan bahwa kompresi berhasil.
- Gunakan opsi `-p` untuk menambahkan kata sandi pada arsip untuk keamanan tambahan.
- Pertimbangkan untuk menggunakan format `.7z` untuk kompresi yang lebih baik dibandingkan dengan format lain seperti `.zip`.