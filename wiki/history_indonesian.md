# [Linux] Bash history Penggunaan: Menampilkan riwayat perintah

## Overview
Perintah `history` dalam Bash digunakan untuk menampilkan daftar perintah yang telah dieksekusi sebelumnya di terminal. Ini sangat berguna untuk mengingat perintah yang telah digunakan dan untuk mengulang perintah tanpa harus mengetiknya lagi.

## Usage
Sintaks dasar untuk perintah `history` adalah sebagai berikut:

```bash
history [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `history`:

- `-c`: Menghapus seluruh riwayat perintah.
- `-d offset`: Menghapus entri riwayat pada posisi tertentu.
- `n`: Menampilkan `n` entri terakhir dari riwayat.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `history`:

1. Menampilkan seluruh riwayat perintah:
   ```bash
   history
   ```

2. Menampilkan 10 perintah terakhir:
   ```bash
   history 10
   ```

3. Menghapus seluruh riwayat perintah:
   ```bash
   history -c
   ```

4. Menghapus entri riwayat tertentu, misalnya entri ke-5:
   ```bash
   history -d 5
   ```

## Tips
- Gunakan `!n` untuk menjalankan perintah ke-n dari riwayat. Misalnya, `!3` akan menjalankan perintah ketiga dalam daftar riwayat.
- Untuk mencari perintah sebelumnya, tekan `Ctrl + R` dan mulai ketikkan perintah yang ingin dicari.
- Pertimbangkan untuk mengatur ukuran riwayat dengan mengubah variabel `HISTSIZE` di file konfigurasi shell Anda agar tidak terlalu penuh.