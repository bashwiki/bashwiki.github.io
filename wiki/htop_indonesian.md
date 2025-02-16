# [Linux] Bash htop Penggunaan: Memantau penggunaan sumber daya sistem

## Overview
Perintah `htop` adalah alat interaktif untuk memantau penggunaan sumber daya sistem secara real-time. Ini memberikan tampilan yang lebih informatif dan mudah digunakan dibandingkan dengan perintah `top`, memungkinkan pengguna untuk melihat proses yang berjalan, penggunaan CPU, memori, dan swap dengan cara yang lebih visual.

## Usage
Sintaks dasar dari perintah `htop` adalah sebagai berikut:

```bash
htop [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `htop`:

- `-h`, `--help`: Menampilkan bantuan dan informasi tentang penggunaan `htop`.
- `-s`, `--sort`: Mengurutkan proses berdasarkan kolom tertentu (misalnya, CPU atau memori).
- `-p`, `--pid`: Menampilkan hanya proses dengan ID tertentu.
- `-u`, `--user`: Menampilkan proses yang berjalan oleh pengguna tertentu.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `htop`:

1. Menjalankan `htop` tanpa opsi:
   ```bash
   htop
   ```

2. Menampilkan proses yang diurutkan berdasarkan penggunaan CPU:
   ```bash
   htop -s PERCENT_CPU
   ```

3. Menampilkan hanya proses dari pengguna tertentu:
   ```bash
   htop -u username
   ```

4. Menampilkan proses dengan ID tertentu:
   ```bash
   htop -p 1234
   ```

## Tips
- Gunakan tombol panah untuk menavigasi antar proses dan `F9` untuk mengakhiri proses yang dipilih.
- Tekan `F2` untuk mengakses menu pengaturan, di mana Anda dapat menyesuaikan tampilan dan opsi yang ada.
- Anda dapat menggunakan `F3` untuk mencari proses tertentu dan `F4` untuk memfilter daftar proses.
- Pastikan Anda menjalankan `htop` dengan hak akses yang sesuai jika ingin melihat semua proses sistem.