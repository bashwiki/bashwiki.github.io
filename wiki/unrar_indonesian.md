# [Linux] Bash unrar Penggunaan: Ekstrak file RAR

## Overview
Perintah `unrar` digunakan untuk mengekstrak file dari arsip RAR. Ini adalah alat yang berguna untuk mengakses konten file yang terkompresi dalam format RAR, yang sering digunakan untuk menghemat ruang penyimpanan atau mengirim file besar.

## Usage
Sintaks dasar dari perintah `unrar` adalah sebagai berikut:

```
unrar [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `unrar`:

- `e`: Ekstrak file dari arsip ke direktori saat ini.
- `x`: Ekstrak file dengan mempertahankan struktur direktori.
- `l`: Tampilkan daftar file dalam arsip tanpa mengekstraknya.
- `v`: Tampilkan informasi rinci tentang file dalam arsip.
- `p`: Masukkan kata sandi untuk arsip yang dilindungi.

## Common Examples

1. **Ekstrak file ke direktori saat ini:**
   ```bash
   unrar e file.rar
   ```

2. **Ekstrak file dan mempertahankan struktur direktori:**
   ```bash
   unrar x file.rar
   ```

3. **Tampilkan daftar file dalam arsip:**
   ```bash
   unrar l file.rar
   ```

4. **Ekstrak file dengan kata sandi:**
   ```bash
   unrar x -pPASSWORD file.rar
   ```

5. **Tampilkan informasi rinci tentang file dalam arsip:**
   ```bash
   unrar v file.rar
   ```

## Tips
- Pastikan Anda memiliki izin yang tepat untuk mengekstrak file di direktori tujuan.
- Gunakan opsi `-p` dengan hati-hati, terutama jika kata sandi mengandung karakter khusus.
- Selalu periksa daftar file sebelum mengekstrak untuk menghindari mengekstrak file yang tidak diinginkan.