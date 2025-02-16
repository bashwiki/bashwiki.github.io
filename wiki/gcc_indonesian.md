# [Linux] Bash gcc Penggunaan: Kompilasi kode sumber C dan C++

## Overview
Perintah `gcc` (GNU Compiler Collection) adalah kompiler yang digunakan untuk mengubah kode sumber yang ditulis dalam bahasa pemrograman C dan C++ menjadi file eksekusi. `gcc` adalah alat yang sangat penting dalam pengembangan perangkat lunak, memungkinkan pengembang untuk mengompilasi dan menjalankan program mereka.

## Usage
Sintaks dasar dari perintah `gcc` adalah sebagai berikut:

```bash
gcc [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `gcc`:

- `-o <file>`: Menentukan nama file output yang dihasilkan.
- `-Wall`: Mengaktifkan semua peringatan yang berguna.
- `-g`: Menyertakan informasi debugging dalam file output.
- `-I<directory>`: Menambahkan direktori untuk pencarian file header.
- `-L<directory>`: Menambahkan direktori untuk pencarian file library.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `gcc`:

1. Mengompilasi file C sederhana menjadi file eksekusi:

    ```bash
    gcc hello.c -o hello
    ```

2. Mengompilasi dengan mengaktifkan semua peringatan:

    ```bash
    gcc -Wall program.c -o program
    ```

3. Mengompilasi dengan informasi debugging:

    ```bash
    gcc -g debug.c -o debug
    ```

4. Mengompilasi beberapa file sumber sekaligus:

    ```bash
    gcc file1.c file2.c -o myprogram
    ```

5. Menambahkan direktori untuk pencarian file header:

    ```bash
    gcc -I/usr/local/include myprogram.c -o myprogram
    ```

## Tips
- Selalu gunakan opsi `-Wall` untuk menangkap potensi masalah dalam kode Anda.
- Jika Anda melakukan pengembangan aktif, pertimbangkan untuk menggunakan opsi `-g` untuk memudahkan debugging.
- Untuk proyek besar, gunakan Makefile untuk mengelola proses kompilasi dengan lebih efisien.
- Pastikan untuk memeriksa dokumentasi resmi `gcc` untuk opsi tambahan dan fitur yang lebih lanjut.