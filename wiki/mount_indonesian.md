# [Linux] Bash mount Penggunaan: Menghubungkan sistem file

## Overview
Perintah `mount` digunakan untuk menghubungkan sistem file ke dalam struktur direktori yang ada di Linux. Dengan menggunakan `mount`, Anda dapat mengakses data dari perangkat penyimpanan eksternal seperti hard drive, USB flash drive, atau partisi lain yang tidak terhubung secara otomatis.

## Usage
Berikut adalah sintaks dasar dari perintah `mount`:

```bash
mount [options] [arguments]
```

## Common Options
- `-t` : Menentukan tipe sistem file (misalnya, ext4, ntfs).
- `-o` : Menentukan opsi tambahan saat melakukan mount (misalnya, read-only, noexec).
- `-a` : Mount semua sistem file yang terdaftar di `/etc/fstab`.
- `-r` : Mount sistem file dalam mode read-only.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `mount`:

1. **Mount partisi dengan tipe sistem file ext4:**
   ```bash
   mount -t ext4 /dev/sda1 /mnt/mydrive
   ```

2. **Mount USB flash drive dengan opsi read-only:**
   ```bash
   mount -o ro /dev/sdb1 /mnt/usb
   ```

3. **Mount semua sistem file yang terdaftar di `/etc/fstab`:**
   ```bash
   mount -a
   ```

4. **Mount partisi dengan opsi tambahan:**
   ```bash
   mount -o noexec,nosuid /dev/sdc1 /mnt/partisi
   ```

## Tips
- Pastikan Anda memiliki hak akses yang cukup (biasanya sebagai pengguna root) untuk menjalankan perintah `mount`.
- Selalu unmount sistem file setelah selesai digunakan dengan perintah `umount` untuk mencegah kerusakan data.
- Periksa file `/etc/fstab` untuk konfigurasi mount otomatis saat booting sistem.