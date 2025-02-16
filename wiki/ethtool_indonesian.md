# [Linux] Bash ethtool Penggunaan: Mengelola dan memeriksa perangkat jaringan

## Overview
Perintah `ethtool` digunakan untuk mengelola dan memeriksa pengaturan perangkat jaringan Ethernet di sistem Linux. Dengan `ethtool`, pengguna dapat melihat informasi tentang koneksi jaringan, mengkonfigurasi parameter, dan melakukan diagnostik.

## Usage
Sintaks dasar dari perintah `ethtool` adalah sebagai berikut:

```bash
ethtool [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `ethtool`:

- `-s` : Mengatur parameter perangkat jaringan.
- `-i` : Menampilkan informasi driver perangkat.
- `-p` : Mengaktifkan lampu indikator pada perangkat untuk memudahkan identifikasi.
- `-t` : Menjalankan tes diagnostik pada perangkat.
- `-a` : Menampilkan pengaturan autonegotiation.

## Common Examples
Berikut adalah beberapa contoh penggunaan `ethtool`:

1. **Menampilkan informasi dasar tentang perangkat jaringan:**
   ```bash
   ethtool eth0
   ```

2. **Menampilkan informasi driver untuk perangkat jaringan:**
   ```bash
   ethtool -i eth0
   ```

3. **Mengatur kecepatan dan mode duplex perangkat:**
   ```bash
   ethtool -s eth0 speed 100 duplex full
   ```

4. **Mengaktifkan lampu indikator pada perangkat:**
   ```bash
   ethtool -p eth0
   ```

5. **Menjalankan tes diagnostik pada perangkat:**
   ```bash
   ethtool -t eth0
   ```

## Tips
- Pastikan Anda memiliki hak akses yang cukup (biasanya sebagai root) untuk menjalankan perintah `ethtool`.
- Gunakan opsi `-h` untuk mendapatkan bantuan dan daftar opsi yang tersedia.
- Selalu periksa dokumentasi perangkat keras Anda untuk memastikan pengaturan yang tepat saat menggunakan `ethtool`.