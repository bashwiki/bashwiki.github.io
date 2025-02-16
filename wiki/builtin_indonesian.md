# [Linux] Bash builtin `builtin`: Menjalankan perintah shell builtin

## Overview
Perintah `builtin` dalam Bash digunakan untuk menjalankan perintah yang merupakan bagian dari shell itu sendiri, bukan perintah eksternal. Ini berguna ketika Anda ingin memastikan bahwa Anda menjalankan versi builtin dari suatu perintah, terutama jika ada perintah eksternal dengan nama yang sama.

## Usage
Berikut adalah sintaks dasar untuk menggunakan perintah `builtin`:

```bash
builtin [options] [arguments]
```

## Common Options
- `-p`: Menggunakan versi builtin yang terdaftar dalam PATH.
- `-f`: Mengabaikan fungsi yang didefinisikan oleh pengguna dan menjalankan versi builtin.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `builtin`:

1. Menjalankan perintah `echo` sebagai builtin:
   ```bash
   builtin echo "Ini adalah perintah builtin echo"
   ```

2. Menggunakan opsi `-p` untuk menjalankan `type` sebagai builtin:
   ```bash
   builtin -p type echo
   ```

3. Menggunakan opsi `-f` untuk menjalankan `set` sebagai builtin meskipun ada fungsi dengan nama yang sama:
   ```bash
   builtin -f set
   ```

## Tips
- Gunakan `builtin` ketika Anda ingin memastikan bahwa Anda menggunakan versi builtin dari perintah, terutama jika ada kemungkinan konflik dengan perintah eksternal.
- Perintah `builtin` sangat berguna dalam skrip untuk menghindari kebingungan antara fungsi dan perintah builtin.
- Selalu periksa dokumentasi untuk memahami perintah builtin yang tersedia dan cara penggunaannya.