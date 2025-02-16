# [Linux] Bash fc Penggunaan: Mengedit dan menjalankan perintah sebelumnya

## Overview
Perintah `fc` dalam Bash digunakan untuk mengedit dan menjalankan perintah yang telah dieksekusi sebelumnya. Dengan `fc`, pengguna dapat dengan mudah mengakses riwayat perintah mereka, melakukan perubahan, dan menjalankannya kembali tanpa harus mengetik ulang perintah tersebut.

## Usage
Berikut adalah sintaks dasar dari perintah `fc`:

```bash
fc [options] [arguments]
```

## Common Options
- `-l` : Menampilkan daftar perintah yang telah dieksekusi sebelumnya.
- `-r` : Mengurutkan daftar perintah secara terbalik.
- `-s` : Menjalankan perintah terakhir tanpa membuka editor.
- `-n` : Menampilkan nomor perintah dalam daftar.

## Common Examples
Berikut adalah beberapa contoh penggunaan `fc`:

1. **Menampilkan daftar perintah sebelumnya:**
   ```bash
   fc -l
   ```

2. **Menampilkan daftar perintah sebelumnya dengan nomor:**
   ```bash
   fc -ln 1 10
   ```

3. **Mengedit perintah terakhir di editor:**
   ```bash
   fc
   ```

4. **Menjalankan perintah terakhir tanpa mengedit:**
   ```bash
   fc -s
   ```

5. **Menampilkan perintah sebelumnya dalam urutan terbalik:**
   ```bash
   fc -r -l
   ```

## Tips
- Gunakan `fc` untuk memperbaiki kesalahan ketik pada perintah sebelumnya tanpa harus mengetik ulang.
- Anda dapat mengatur editor teks default untuk `fc` dengan mengatur variabel lingkungan `EDITOR`.
- Manfaatkan opsi `-n` untuk melihat nomor perintah dan lebih mudah memilih perintah yang ingin diedit.