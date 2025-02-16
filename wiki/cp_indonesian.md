# [Linux] Bash cp Penggunaan: Menyalin file dan direktori

## Overview
Perintah `cp` digunakan untuk menyalin file dan direktori di sistem operasi berbasis Unix, termasuk Linux. Dengan perintah ini, Anda dapat membuat salinan dari file atau direktori yang ada ke lokasi yang diinginkan.

## Usage
Sintaks dasar dari perintah `cp` adalah sebagai berikut:

```
cp [options] [source] [destination]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `cp`:

- `-r` : Menyalin direktori secara rekursif.
- `-i` : Meminta konfirmasi sebelum menimpa file yang ada.
- `-u` : Menyalin hanya jika file sumber lebih baru daripada file tujuan atau jika file tujuan tidak ada.
- `-v` : Menampilkan informasi tentang file yang sedang disalin.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan perintah `cp`:

1. Menyalin file dari satu lokasi ke lokasi lain:
   ```bash
   cp file1.txt /path/to/destination/
   ```

2. Menyalin direktori secara rekursif:
   ```bash
   cp -r /path/to/source_directory /path/to/destination_directory
   ```

3. Menyalin file dengan konfirmasi jika file tujuan sudah ada:
   ```bash
   cp -i file1.txt /path/to/destination/
   ```

4. Menyalin file hanya jika file sumber lebih baru:
   ```bash
   cp -u file1.txt /path/to/destination/
   ```

5. Menyalin file sambil menampilkan proses:
   ```bash
   cp -v file1.txt /path/to/destination/
   ```

## Tips
- Selalu gunakan opsi `-i` jika Anda tidak ingin menimpa file yang ada tanpa konfirmasi.
- Gunakan opsi `-r` dengan hati-hati saat menyalin direktori, karena ini akan menyalin semua isi direktori tersebut.
- Pertimbangkan untuk menggunakan opsi `-v` saat melakukan penyalinan dalam jumlah besar untuk memantau prosesnya.