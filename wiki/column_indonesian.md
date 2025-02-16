# [Linux] Bash column Penggunaan: Mengatur Teks dalam Kolom

## Overview
Perintah `column` digunakan untuk mengatur teks dalam format kolom yang rapi. Ini sangat berguna untuk menampilkan data dalam bentuk tabel, sehingga lebih mudah dibaca dan dianalisis.

## Usage
Sintaks dasar dari perintah `column` adalah sebagai berikut:

```bash
column [options] [arguments]
```

## Common Options
- `-t`: Mengatur teks dalam kolom berdasarkan pemisah default (spasi atau tab).
- `-s`: Menentukan pemisah yang digunakan untuk kolom, misalnya koma atau titik koma.
- `-n`: Mengabaikan baris kosong saat memformat kolom.
- `-c`: Menentukan lebar kolom maksimum.

## Common Examples

1. **Mengatur teks dengan pemisah default (spasi)**:
   ```bash
   echo -e "Nama Umur\nAlice 30\nBob 25" | column
   ```

2. **Menggunakan pemisah khusus (misalnya koma)**:
   ```bash
   echo -e "Nama,Umur\nAlice,30\nBob,25" | column -s, -t
   ```

3. **Mengabaikan baris kosong**:
   ```bash
   echo -e "Nama Umur\n\nAlice 30\n\nBob 25" | column -n
   ```

4. **Menentukan lebar kolom maksimum**:
   ```bash
   echo -e "Nama Umur\nAlice 30\nBob 25" | column -c 20
   ```

## Tips
- Selalu gunakan opsi `-t` untuk memformat data dengan rapi, terutama saat bekerja dengan data yang memiliki banyak kolom.
- Jika menggunakan pemisah khusus, pastikan untuk menyertakan opsi `-s` agar `column` dapat mengenali pemisah tersebut.
- Cobalah untuk menggabungkan `column` dengan perintah lain seperti `cat` atau `grep` untuk memformat output yang lebih kompleks.