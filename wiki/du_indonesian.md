# [Linux] Bash du Penggunaan: Mengukur penggunaan disk

## Overview
Perintah `du` (disk usage) digunakan untuk menampilkan jumlah ruang disk yang digunakan oleh file dan direktori. Ini sangat berguna untuk menganalisis penggunaan ruang disk pada sistem Anda.

## Usage
Berikut adalah sintaks dasar dari perintah `du`:

```bash
du [options] [arguments]
```

## Common Options
- `-h`: Menampilkan ukuran dalam format yang lebih mudah dibaca (misalnya, KB, MB, GB).
- `-s`: Menampilkan total penggunaan disk untuk setiap argumen, bukan untuk setiap subdirektori.
- `-a`: Menampilkan penggunaan disk untuk semua file, bukan hanya direktori.
- `-c`: Menampilkan total keseluruhan penggunaan disk di akhir output.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `du`:

1. Menampilkan penggunaan disk untuk direktori saat ini dalam format yang mudah dibaca:
   ```bash
   du -h
   ```

2. Menampilkan total penggunaan disk untuk direktori tertentu:
   ```bash
   du -sh /path/to/directory
   ```

3. Menampilkan penggunaan disk untuk semua file dan direktori dalam direktori saat ini:
   ```bash
   du -ah
   ```

4. Menampilkan penggunaan disk dan total keseluruhan untuk direktori tertentu:
   ```bash
   du -ch /path/to/directory
   ```

## Tips
- Gunakan opsi `-h` untuk memudahkan pemahaman ukuran file, terutama jika Anda bekerja dengan file besar.
- Kombinasikan `du` dengan perintah `sort` untuk mengurutkan hasil berdasarkan ukuran:
  ```bash
  du -h | sort -hr
  ```
- Untuk menemukan direktori yang menggunakan ruang disk terbesar, Anda bisa menggunakan:
  ```bash
  du -sh * | sort -hr | head -n 10
  ```