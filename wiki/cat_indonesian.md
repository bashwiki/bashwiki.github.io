# [Linux] Bash cat Penggunaan: Menampilkan isi file

## Overview
Perintah `cat` dalam Bash digunakan untuk menampilkan isi dari satu atau lebih file ke layar. Perintah ini sangat berguna untuk melihat konten file teks dengan cepat tanpa perlu membuka editor.

## Usage
Berikut adalah sintaks dasar dari perintah `cat`:

```bash
cat [options] [arguments]
```

## Common Options
- `-n`: Menampilkan nomor baris sebelum setiap baris output.
- `-b`: Menampilkan nomor baris, tetapi hanya untuk baris yang tidak kosong.
- `-E`: Menampilkan tanda `$` di akhir setiap baris.
- `-s`: Menghilangkan baris kosong ganda.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `cat`:

1. Menampilkan isi file:
   ```bash
   cat file.txt
   ```

2. Menampilkan beberapa file sekaligus:
   ```bash
   cat file1.txt file2.txt
   ```

3. Menampilkan isi file dengan nomor baris:
   ```bash
   cat -n file.txt
   ```

4. Menggabungkan beberapa file menjadi satu file baru:
   ```bash
   cat file1.txt file2.txt > gabungan.txt
   ```

5. Menampilkan isi file dan menambahkan tanda `$` di akhir setiap baris:
   ```bash
   cat -E file.txt
   ```

## Tips
- Gunakan `cat` dengan opsi `-n` untuk membantu dalam debugging, sehingga Anda dapat melihat di mana kesalahan mungkin terjadi dalam file.
- Untuk file yang sangat besar, pertimbangkan menggunakan `less` atau `more` agar lebih mudah untuk menggulir dan membaca.
- Jika Anda ingin menggabungkan file, pastikan untuk memeriksa hasilnya dengan `cat` sebelum menyimpan ke file baru untuk memastikan tidak ada kesalahan.