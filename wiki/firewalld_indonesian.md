# [Linux] Bash firewalld Penggunaan: Mengelola firewall dengan mudah

## Overview
Perintah `firewalld` digunakan untuk mengelola firewall di sistem Linux. Dengan `firewalld`, pengguna dapat mengatur aturan firewall secara dinamis, memungkinkan atau memblokir lalu lintas jaringan berdasarkan zona dan layanan yang ditentukan.

## Usage
Berikut adalah sintaks dasar dari perintah `firewalld`:

```bash
firewalld [options] [arguments]
```

## Common Options
- `--zone`: Menentukan zona yang akan digunakan.
- `--add-service`: Menambahkan layanan ke zona tertentu.
- `--remove-service`: Menghapus layanan dari zona tertentu.
- `--list-all`: Menampilkan semua pengaturan untuk zona yang dipilih.
- `--permanent`: Menyimpan perubahan secara permanen.

## Common Examples
Berikut adalah beberapa contoh penggunaan `firewalld`:

1. **Menambahkan layanan HTTP ke zona publik:**
   ```bash
   firewall-cmd --zone=public --add-service=http
   ```

2. **Menghapus layanan FTP dari zona internal:**
   ```bash
   firewall-cmd --zone=internal --remove-service=ftp
   ```

3. **Menampilkan semua pengaturan untuk zona publik:**
   ```bash
   firewall-cmd --zone=public --list-all
   ```

4. **Menambahkan port 8080 ke zona yang ditentukan secara permanen:**
   ```bash
   firewall-cmd --zone=public --add-port=8080/tcp --permanent
   ```

5. **Menerapkan perubahan setelah menambahkan aturan:**
   ```bash
   firewall-cmd --reload
   ```

## Tips
- Selalu gunakan opsi `--permanent` jika Anda ingin perubahan tetap ada setelah reboot.
- Gunakan `firewall-cmd --state` untuk memeriksa status `firewalld`.
- Sebelum melakukan perubahan besar, pertimbangkan untuk mencadangkan konfigurasi firewall Anda.