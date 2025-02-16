# [Linux] Bash cmake Penggunaan: Alat untuk mengelola proses pembangunan perangkat lunak

## Overview
Perintah `cmake` adalah alat yang digunakan untuk mengelola proses pembangunan perangkat lunak. CMake membantu dalam mengkonfigurasi proyek dan menghasilkan file make yang diperlukan untuk membangun aplikasi di berbagai platform.

## Usage
Berikut adalah sintaks dasar dari perintah `cmake`:

```bash
cmake [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `cmake`:

- `-S <path>`: Menentukan direktori sumber dari proyek.
- `-B <path>`: Menentukan direktori build untuk output.
- `-D <var>=<value>`: Mengatur variabel CMake dengan nilai tertentu.
- `-G <generator>`: Menentukan generator yang akan digunakan untuk membangun proyek.
- `--build <path>`: Membangun proyek di direktori yang ditentukan.

## Common Examples
Berikut adalah beberapa contoh penggunaan `cmake`:

1. **Mengkonfigurasi proyek dari direktori sumber**:
   ```bash
   cmake -S . -B build
   ```

2. **Mengatur variabel saat konfigurasi**:
   ```bash
   cmake -S . -B build -D CMAKE_BUILD_TYPE=Release
   ```

3. **Menggunakan generator tertentu**:
   ```bash
   cmake -S . -B build -G "Unix Makefiles"
   ```

4. **Membangun proyek setelah konfigurasi**:
   ```bash
   cmake --build build
   ```

## Tips
- Selalu gunakan direktori terpisah untuk build (`-B`) agar file build tidak tercampur dengan file sumber.
- Periksa dokumentasi proyek untuk opsi konfigurasi spesifik yang mungkin diperlukan.
- Gunakan opsi `-D` untuk menyesuaikan pengaturan build sesuai kebutuhan proyek Anda.