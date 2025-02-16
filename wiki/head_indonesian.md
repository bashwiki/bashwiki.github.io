# [Linux] Bash head Penggunaan: Menampilkan Baris Awal dari File

## Overview
Perintah `head` digunakan untuk menampilkan beberapa baris pertama dari sebuah file. Secara default, `head` akan menampilkan 10 baris pertama, tetapi pengguna dapat menentukan jumlah baris yang ingin ditampilkan.

## Usage
Berikut adalah sintaks dasar dari perintah `head`:

```bash
head [options] [arguments]
```

## Common Options
- `-n [jumlah]`: Menentukan jumlah baris yang ingin ditampilkan. Misalnya, `-n 5` akan menampilkan 5 baris pertama.
- `-q`: Tidak menampilkan nama file saat menampilkan beberapa file.
- `-v`: Selalu menampilkan nama file sebelum konten file.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `head`:

1. Menampilkan 10 baris pertama dari file `data.txt`:
   ```bash
   head data.txt
   ```

2. Menampilkan 5 baris pertama dari file `data.txt`:
   ```bash
   head -n 5 data.txt
   ```

3. Menampilkan 3 baris pertama dari beberapa file:
   ```bash
   head -n 3 file1.txt file2.txt
   ```

4. Menampilkan isi file dengan nama file:
   ```bash
   head -v data.txt
   ```

## Tips
- Gunakan `head` bersama dengan perintah lain menggunakan pipe (`|`) untuk melihat bagian awal dari output perintah tersebut. Contoh:
  ```bash
  ls -l | head
  ```
- Jika Anda ingin melihat lebih dari 10 baris, ingat untuk selalu menggunakan opsi `-n` untuk menentukan jumlah baris yang diinginkan.
- `head` sangat berguna untuk memeriksa file log atau file teks besar tanpa harus membuka seluruh file.