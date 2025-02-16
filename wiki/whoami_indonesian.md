# [Linux] Bash whoami Penggunaan: Menampilkan nama pengguna saat ini

## Overview
Perintah `whoami` digunakan untuk menampilkan nama pengguna yang sedang aktif di terminal. Ini sangat berguna untuk memastikan identitas pengguna saat bekerja di sistem yang mungkin memiliki beberapa akun.

## Usage
Berikut adalah sintaks dasar dari perintah `whoami`:

```bash
whoami [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `whoami`:

- `--help`: Menampilkan informasi bantuan tentang penggunaan perintah.
- `--version`: Menampilkan versi dari perintah `whoami`.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `whoami`:

1. Menampilkan nama pengguna saat ini:
   ```bash
   whoami
   ```

2. Menampilkan informasi bantuan:
   ```bash
   whoami --help
   ```

3. Menampilkan versi dari perintah `whoami`:
   ```bash
   whoami --version
   ```

## Tips
- Gunakan `whoami` untuk memverifikasi bahwa Anda sedang menggunakan akun yang benar, terutama saat melakukan tugas administratif.
- Perintah ini sangat berguna dalam skrip untuk memastikan bahwa skrip dijalankan dengan hak akses yang sesuai.