# [Linux] Bash g++ Penggunaan: Kompilasi program C++

## Overview
Perintah `g++` adalah kompiler untuk bahasa pemrograman C++. Ia digunakan untuk mengubah kode sumber C++ menjadi file eksekusi yang dapat dijalankan di sistem operasi. `g++` merupakan bagian dari GNU Compiler Collection (GCC) dan mendukung berbagai fitur bahasa C++.

## Usage
Berikut adalah sintaks dasar dari perintah `g++`:

```bash
g++ [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `g++`:

- `-o <file>`: Menentukan nama file output yang dihasilkan.
- `-Wall`: Mengaktifkan semua peringatan untuk membantu menemukan potensi masalah dalam kode.
- `-g`: Menyertakan informasi debugging dalam file output.
- `-std=<standard>`: Menentukan standar C++ yang akan digunakan (misalnya, `-std=c++11`).
- `-I<directory>`: Menambahkan direktori untuk pencarian file header.

## Common Examples
Berikut adalah beberapa contoh penggunaan `g++`:

1. **Kompilasi file sumber sederhana:**
   ```bash
   g++ program.cpp
   ```

2. **Kompilasi dengan nama file output yang ditentukan:**
   ```bash
   g++ program.cpp -o program_executable
   ```

3. **Mengaktifkan semua peringatan saat kompilasi:**
   ```bash
   g++ -Wall program.cpp
   ```

4. **Menyertakan informasi debugging:**
   ```bash
   g++ -g program.cpp -o program_debug
   ```

5. **Menggunakan standar C++ tertentu:**
   ```bash
   g++ -std=c++11 program.cpp -o program_cpp11
   ```

## Tips
- Selalu gunakan opsi `-Wall` untuk menangkap peringatan yang dapat membantu memperbaiki kode.
- Jika Anda sedang dalam tahap pengembangan, gunakan opsi `-g` untuk memudahkan debugging.
- Pastikan untuk menyertakan file header yang diperlukan dengan opsi `-I` jika file header berada di direktori yang tidak standar.
- Pertimbangkan untuk menggunakan sistem build seperti Makefile untuk mengelola proyek yang lebih besar dengan banyak file sumber.