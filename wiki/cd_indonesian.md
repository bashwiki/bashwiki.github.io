# [Linux] Bash cd Penggunaan: Navigasi direktori

## Overview
Perintah `cd` (change directory) digunakan untuk berpindah antara direktori di dalam sistem file. Dengan menggunakan perintah ini, pengguna dapat mengakses folder yang berbeda untuk menjalankan perintah lain atau mengelola file.

## Usage
Sintaks dasar dari perintah `cd` adalah sebagai berikut:

```
cd [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `cd`:

- `..` : Pindah ke direktori induk dari direktori saat ini.
- `-` : Pindah kembali ke direktori sebelumnya.
- `~` : Pindah ke direktori home pengguna saat ini.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `cd`:

1. **Pindah ke direktori induk:**
   ```bash
   cd ..
   ```

2. **Pindah ke direktori home:**
   ```bash
   cd ~
   ```

3. **Pindah ke direktori tertentu:**
   ```bash
   cd /path/to/directory
   ```

4. **Pindah ke direktori sebelumnya:**
   ```bash
   cd -
   ```

## Tips
- Gunakan `cd` dengan jalur relatif untuk berpindah ke subdirektori tanpa perlu menulis jalur lengkap.
- Anda dapat menggunakan tab untuk menyelesaikan nama direktori secara otomatis, sehingga mempercepat navigasi.
- Untuk melihat direktori saat ini, gunakan perintah `pwd` setelah berpindah direktori.