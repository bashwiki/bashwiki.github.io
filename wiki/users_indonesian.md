# [Linux] Pengguna Bash: Mengelola pengguna sistem

## Overview
Perintah `users` digunakan untuk menampilkan daftar nama pengguna yang sedang aktif di sistem. Ini berguna untuk mengetahui siapa saja yang sedang masuk ke sistem pada waktu tertentu.

## Usage
Sintaks dasar dari perintah `users` adalah sebagai berikut:

```
users [options] [arguments]
```

## Common Options
- `-a`: Menampilkan semua pengguna yang sedang aktif, termasuk pengguna yang mungkin memiliki sesi yang tidak terlihat.
- `-H`: Menampilkan nama pengguna dalam format yang lebih mudah dibaca.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `users`:

1. Menampilkan daftar pengguna yang sedang aktif:
   ```bash
   users
   ```

2. Menampilkan semua pengguna aktif dengan opsi `-a`:
   ```bash
   users -a
   ```

3. Menampilkan pengguna dalam format yang lebih mudah dibaca:
   ```bash
   users -H
   ```

## Tips
- Gunakan perintah `who` untuk mendapatkan informasi lebih detail tentang sesi pengguna, termasuk waktu masuk dan terminal yang digunakan.
- Perintah `users` hanya menampilkan nama pengguna tanpa informasi tambahan. Jika Anda memerlukan informasi lebih lanjut, pertimbangkan untuk menggunakan perintah `w` atau `who`.