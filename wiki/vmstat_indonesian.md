# [Linux] Bash vmstat Penggunaan: Memantau Statistik Sistem

## Overview
Perintah `vmstat` digunakan untuk memantau statistik sistem, termasuk penggunaan memori, proses, dan aktivitas I/O. Dengan menggunakan `vmstat`, pengguna dapat mendapatkan informasi penting tentang kinerja sistem secara real-time.

## Usage
Berikut adalah sintaks dasar dari perintah `vmstat`:

```bash
vmstat [options] [arguments]
```

## Common Options
- `-a`: Menampilkan informasi tentang memori aktif dan tidak aktif.
- `-m`: Menampilkan statistik penggunaan memori untuk cache dan buffer.
- `-s`: Menampilkan statistik sistem dalam format yang lebih ringkas.
- `-w`: Menampilkan output dalam format lebar, yang lebih mudah dibaca.
- `interval`: Menentukan interval waktu dalam detik untuk pembaruan statistik.

## Common Examples
Berikut adalah beberapa contoh penggunaan `vmstat`:

1. Menampilkan statistik sistem secara langsung:
   ```bash
   vmstat
   ```

2. Menampilkan statistik setiap 2 detik:
   ```bash
   vmstat 2
   ```

3. Menampilkan informasi memori aktif dan tidak aktif:
   ```bash
   vmstat -a
   ```

4. Menampilkan statistik sistem dalam format ringkas:
   ```bash
   vmstat -s
   ```

5. Menampilkan statistik dengan interval 5 detik selama 10 kali:
   ```bash
   vmstat 5 10
   ```

## Tips
- Gunakan `vmstat` bersama dengan perintah lain seperti `top` atau `htop` untuk analisis yang lebih mendalam tentang kinerja sistem.
- Perhatikan kolom `si` dan `so` untuk memantau swap in dan swap out, yang dapat menunjukkan masalah dengan memori.
- Cobalah menggunakan opsi `-m` untuk mendapatkan informasi lebih detail tentang penggunaan memori cache dan buffer.