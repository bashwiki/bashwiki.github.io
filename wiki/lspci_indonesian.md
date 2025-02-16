# [Linux] Bash lspci Penggunaan: Menampilkan informasi perangkat PCI

## Overview
Perintah `lspci` digunakan untuk menampilkan informasi tentang perangkat yang terhubung melalui bus PCI (Peripheral Component Interconnect) di sistem Linux. Ini sangat berguna untuk mengidentifikasi perangkat keras yang terpasang, seperti kartu grafis, kartu jaringan, dan perangkat lainnya.

## Usage
Sintaks dasar dari perintah `lspci` adalah sebagai berikut:

```bash
lspci [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `lspci`:

- `-v`: Menampilkan informasi lebih rinci tentang perangkat.
- `-vv`: Menampilkan informasi yang lebih detail lagi.
- `-k`: Menampilkan driver yang digunakan oleh perangkat.
- `-n`: Menampilkan ID vendor dan ID perangkat dalam format numerik.
- `-s <slot>`: Menampilkan informasi hanya untuk perangkat yang berada di slot tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `lspci`:

1. Menampilkan daftar semua perangkat PCI:
   ```bash
   lspci
   ```

2. Menampilkan informasi rinci tentang semua perangkat:
   ```bash
   lspci -v
   ```

3. Menampilkan informasi tentang perangkat tertentu dengan slot yang ditentukan:
   ```bash
   lspci -s 00:1f.0
   ```

4. Menampilkan driver yang digunakan oleh perangkat:
   ```bash
   lspci -k
   ```

5. Menampilkan ID vendor dan ID perangkat dalam format numerik:
   ```bash
   lspci -n
   ```

## Tips
- Gunakan opsi `-v` atau `-vv` untuk mendapatkan informasi lebih lengkap tentang perangkat, terutama saat melakukan troubleshooting.
- Jika Anda mencari perangkat tertentu, Anda bisa menggabungkan `lspci` dengan `grep` untuk menyaring hasil, misalnya:
  ```bash
  lspci | grep -i network
  ```
- Pastikan Anda menjalankan perintah ini dengan hak akses yang sesuai jika diperlukan, terutama saat mengakses informasi perangkat keras yang lebih sensitif.