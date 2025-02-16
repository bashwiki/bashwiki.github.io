# [Linux] Bash useradd Penggunaan: Menambahkan pengguna baru ke sistem

## Overview
Perintah `useradd` digunakan untuk membuat akun pengguna baru di sistem Linux. Dengan menggunakan perintah ini, administrator dapat menambahkan pengguna baru dan mengatur beberapa opsi terkait akun tersebut.

## Usage
Berikut adalah sintaks dasar dari perintah `useradd`:

```
useradd [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `useradd`:

- `-m`: Membuat direktori home untuk pengguna baru.
- `-s`: Menentukan shell login yang akan digunakan oleh pengguna.
- `-g`: Menentukan grup utama untuk pengguna baru.
- `-G`: Menentukan grup tambahan yang akan diikutsertakan.
- `-c`: Menambahkan komentar atau deskripsi untuk pengguna.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `useradd`:

1. **Menambahkan pengguna baru dengan direktori home:**
   ```bash
   useradd -m john
   ```

2. **Menambahkan pengguna baru dengan shell tertentu:**
   ```bash
   useradd -m -s /bin/bash jane
   ```

3. **Menambahkan pengguna baru ke grup tertentu:**
   ```bash
   useradd -m -g developers -G admin mark
   ```

4. **Menambahkan komentar untuk pengguna baru:**
   ```bash
   useradd -m -c "Pengguna untuk proyek X" alice
   ```

## Tips
- Selalu gunakan opsi `-m` untuk memastikan direktori home dibuat untuk pengguna baru.
- Periksa grup yang ada sebelum menambahkan pengguna ke grup tambahan dengan opsi `-G`.
- Setelah menggunakan `useradd`, jangan lupa untuk mengatur kata sandi pengguna dengan perintah `passwd [username]`.