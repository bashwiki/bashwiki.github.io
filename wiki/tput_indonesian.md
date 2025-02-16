# [Linux] Bash tput Penggunaan: Mengatur tampilan terminal

## Overview
Perintah `tput` digunakan untuk mengatur tampilan terminal dengan mengontrol atribut seperti warna, posisi kursor, dan format teks. Ini memungkinkan pengguna untuk membuat antarmuka yang lebih menarik dan interaktif di dalam terminal.

## Usage
Sintaks dasar dari perintah `tput` adalah sebagai berikut:

```bash
tput [options] [arguments]
```

## Common Options
- `setaf [n]`: Mengatur warna teks depan ke warna yang ditentukan oleh nomor `n`.
- `setab [n]`: Mengatur warna latar belakang ke warna yang ditentukan oleh nomor `n`.
- `bold`: Mengaktifkan teks tebal.
- `clear`: Menghapus layar terminal.
- `cup [x] [y]`: Memindahkan kursor ke posisi yang ditentukan oleh koordinat `x` dan `y`.

## Common Examples
Berikut adalah beberapa contoh penggunaan `tput`:

1. **Mengatur warna teks depan menjadi merah:**
   ```bash
   tput setaf 1
   echo "Ini teks merah"
   ```

2. **Mengatur warna latar belakang menjadi hijau:**
   ```bash
   tput setab 2
   echo "Ini latar belakang hijau"
   ```

3. **Mengaktifkan teks tebal:**
   ```bash
   tput bold
   echo "Ini teks tebal"
   tput sgr0  # Mengembalikan ke pengaturan normal
   ```

4. **Menghapus layar terminal:**
   ```bash
   tput clear
   ```

5. **Memindahkan kursor ke baris ke-5 dan kolom ke-10:**
   ```bash
   tput cup 5 10
   echo "Kursor berada di sini"
   ```

## Tips
- Selalu gunakan `tput sgr0` setelah mengubah atribut teks untuk mengembalikan pengaturan ke keadaan normal.
- Cobalah untuk menggabungkan beberapa perintah `tput` dalam skrip untuk menciptakan tampilan yang dinamis.
- Periksa dukungan terminal Anda untuk warna dan atribut yang berbeda, karena tidak semua terminal mendukung semua opsi.