# [Linux] Bash help Penggunaan: Menampilkan informasi bantuan untuk perintah

## Overview
Perintah `help` dalam Bash digunakan untuk menampilkan informasi bantuan tentang built-in commands. Ini sangat berguna bagi pengguna yang ingin memahami cara menggunakan perintah tertentu dalam shell.

## Usage
Berikut adalah sintaks dasar dari perintah `help`:

```
help [options] [arguments]
```

## Common Options
- `-s`, `--silent`: Menampilkan informasi tanpa penjelasan tambahan.
- `-m`, `--man`: Menampilkan informasi bantuan dalam format manual.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `help`:

1. Menampilkan bantuan untuk perintah `cd`:
   ```bash
   help cd
   ```

2. Menampilkan bantuan untuk perintah `echo`:
   ```bash
   help echo
   ```

3. Menampilkan semua perintah built-in yang tersedia:
   ```bash
   help
   ```

4. Menampilkan bantuan dalam format manual untuk perintah `set`:
   ```bash
   help -m set
   ```

## Tips
- Gunakan `help` tanpa argumen untuk melihat daftar semua built-in commands yang tersedia.
- Jika Anda tidak yakin tentang perintah tertentu, coba `help [perintah]` untuk mendapatkan penjelasan singkat.
- Perintah `help` hanya berlaku untuk built-in commands; untuk perintah eksternal, gunakan `man` atau `--help`.