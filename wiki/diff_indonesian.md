# [Linux] Bash diff Penggunaan: Membandingkan file dan direktori

## Overview
Perintah `diff` digunakan untuk membandingkan dua file atau direktori dan menampilkan perbedaan di antara keduanya. Ini sangat berguna untuk melihat perubahan yang dilakukan pada file, terutama dalam pengembangan perangkat lunak dan pengelolaan versi.

## Usage
Berikut adalah sintaks dasar dari perintah `diff`:

```
diff [options] [file1] [file2]
```

## Common Options
- `-u`: Menampilkan output dalam format unified, yang lebih mudah dibaca.
- `-c`: Menampilkan output dalam format context, yang menunjukkan beberapa baris konteks di sekitar perbedaan.
- `-i`: Mengabaikan perbedaan dalam huruf besar/kecil.
- `-w`: Mengabaikan semua spasi putih saat membandingkan.
- `-r`: Membandingkan direktori secara rekursif.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `diff`:

1. **Membandingkan dua file teks:**
   ```bash
   diff file1.txt file2.txt
   ```

2. **Menggunakan opsi unified untuk output yang lebih jelas:**
   ```bash
   diff -u file1.txt file2.txt
   ```

3. **Membandingkan dua direktori:**
   ```bash
   diff -r dir1/ dir2/
   ```

4. **Mengabaikan perbedaan huruf besar/kecil:**
   ```bash
   diff -i file1.txt file2.txt
   ```

5. **Membandingkan dua file dan menyimpan hasil ke dalam file:**
   ```bash
   diff file1.txt file2.txt > hasil_diff.txt
   ```

## Tips
- Gunakan opsi `-u` untuk mendapatkan output yang lebih mudah dibaca, terutama saat bekerja dengan file besar.
- Jika Anda bekerja dengan banyak file, pertimbangkan untuk menggunakan `diff` dalam kombinasi dengan `find` untuk membandingkan file secara otomatis.
- Selalu periksa hasil `diff` sebelum melakukan penggabungan atau perubahan pada file untuk menghindari kehilangan data.