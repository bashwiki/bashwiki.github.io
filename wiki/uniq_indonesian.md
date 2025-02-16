# [Linux] Bash uniq Penggunaan: Menghapus Duplikat Baris

## Overview
Perintah `uniq` dalam Bash digunakan untuk menghapus baris yang duplikat dalam sebuah file atau output dari perintah lain. Perintah ini hanya menghapus duplikat yang berurutan, sehingga penting untuk mengurutkan data terlebih dahulu jika ingin menghapus semua duplikat.

## Usage
Sintaks dasar dari perintah `uniq` adalah sebagai berikut:

```bash
uniq [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `uniq`:

- `-c`: Menghitung jumlah kemunculan setiap baris yang unik.
- `-d`: Menampilkan hanya baris yang muncul lebih dari sekali.
- `-u`: Menampilkan hanya baris yang unik (tidak muncul lebih dari sekali).
- `-i`: Mengabaikan perbedaan huruf besar dan kecil saat membandingkan baris.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `uniq`:

1. Menghapus duplikat dari file:
   ```bash
   uniq file.txt
   ```

2. Mengurutkan dan kemudian menghapus duplikat:
   ```bash
   sort file.txt | uniq
   ```

3. Menghitung jumlah kemunculan setiap baris:
   ```bash
   uniq -c file.txt
   ```

4. Menampilkan hanya baris yang muncul lebih dari sekali:
   ```bash
   uniq -d file.txt
   ```

5. Mengabaikan perbedaan huruf besar dan kecil:
   ```bash
   uniq -i file.txt
   ```

## Tips
- Selalu gunakan `sort` sebelum `uniq` jika Anda ingin menghapus semua duplikat dalam file, karena `uniq` hanya menghapus duplikat yang berurutan.
- Untuk analisis data yang lebih kompleks, pertimbangkan untuk menggabungkan `uniq` dengan perintah lain seperti `grep` atau `awk`.
- Simpan hasil `uniq` ke file baru dengan menggunakan redirection, misalnya:
  ```bash
  uniq file.txt > hasil.txt
  ```