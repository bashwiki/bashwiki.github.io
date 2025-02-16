# [Linux] Bash sed Penggunaan: Mengedit teks dalam aliran data

## Overview
Perintah `sed` (stream editor) adalah alat yang digunakan untuk memanipulasi dan mengedit teks dalam aliran data. Dengan `sed`, Anda dapat melakukan berbagai operasi seperti pencarian, penggantian, penghapusan, dan penyisipan teks secara efisien.

## Usage
Berikut adalah sintaks dasar dari perintah `sed`:

```bash
sed [options] [arguments]
```

## Common Options
- `-e`: Menentukan ekspresi pengeditan.
- `-i`: Mengedit file secara langsung (in-place).
- `-n`: Menonaktifkan output default, hanya menampilkan hasil yang ditentukan.
- `s`: Menyediakan fungsi substitusi untuk mengganti teks.

## Common Examples
Berikut adalah beberapa contoh penggunaan `sed`:

1. **Mengganti teks dalam file**:
   Mengganti semua kemunculan "lama" dengan "baru" dalam file `file.txt`.
   ```bash
   sed -i 's/lama/baru/g' file.txt
   ```

2. **Menampilkan baris tertentu**:
   Menampilkan hanya baris ke-2 hingga ke-4 dari file `file.txt`.
   ```bash
   sed -n '2,4p' file.txt
   ```

3. **Menghapus baris yang mengandung teks tertentu**:
   Menghapus semua baris yang mengandung kata "hapus" dari file `file.txt`.
   ```bash
   sed -i '/hapus/d' file.txt
   ```

4. **Menambahkan teks di akhir setiap baris**:
   Menambahkan " - akhir" di akhir setiap baris dalam file `file.txt`.
   ```bash
   sed -i 's/$/ - akhir/' file.txt
   ```

## Tips
- Selalu buat salinan cadangan file sebelum menggunakan opsi `-i` untuk menghindari kehilangan data.
- Gunakan opsi `-n` bersama dengan perintah `p` untuk menampilkan hasil yang lebih terfokus.
- Cobalah untuk menggunakan ekspresi reguler untuk pencarian dan penggantian yang lebih kompleks.