# [Linux] Bash fdisk Penggunaan: Mengelola partisi disk

## Overview
Perintah `fdisk` digunakan untuk mengelola tabel partisi pada disk. Dengan `fdisk`, pengguna dapat membuat, menghapus, dan mengubah ukuran partisi pada perangkat penyimpanan seperti hard drive atau SSD.

## Usage
Berikut adalah sintaks dasar dari perintah `fdisk`:

```bash
fdisk [options] [device]
```

Di mana `[device]` adalah perangkat yang ingin Anda kelola, seperti `/dev/sda`.

## Common Options
- `-l`: Menampilkan semua partisi yang ada pada disk.
- `-u`: Menggunakan unit sektor untuk ukuran partisi.
- `-n`: Membuat partisi baru.
- `-d`: Menghapus partisi yang ada.
- `-t`: Mengubah tipe partisi.

## Common Examples
Berikut adalah beberapa contoh penggunaan `fdisk`:

1. **Menampilkan daftar partisi pada disk:**
   ```bash
   fdisk -l /dev/sda
   ```

2. **Membuat partisi baru:**
   ```bash
   fdisk /dev/sda
   ```
   Setelah menjalankan perintah di atas, Anda akan masuk ke mode interaktif. Gunakan perintah `n` untuk membuat partisi baru.

3. **Menghapus partisi:**
   ```bash
   fdisk /dev/sda
   ```
   Masuk ke mode interaktif dan gunakan perintah `d` untuk menghapus partisi yang diinginkan.

4. **Mengubah tipe partisi:**
   ```bash
   fdisk /dev/sda
   ```
   Masuk ke mode interaktif dan gunakan perintah `t` untuk mengubah tipe partisi.

## Tips
- Selalu cadangkan data penting sebelum melakukan perubahan pada partisi.
- Gunakan `fdisk` dengan hati-hati, karena kesalahan dapat mengakibatkan kehilangan data.
- Untuk pengguna yang tidak nyaman dengan antarmuka berbasis teks, pertimbangkan untuk menggunakan alat grafis seperti `gparted`.