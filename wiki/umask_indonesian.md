# [Linux] Bash umask Penggunaan: Mengatur izin file default

## Overview
Perintah `umask` digunakan untuk mengatur izin default yang diterapkan pada file dan direktori baru yang dibuat oleh pengguna. Nilai umask menentukan izin yang akan dibatalkan saat file atau direktori baru dibuat, sehingga membantu dalam mengontrol akses ke file tersebut.

## Usage
Sintaks dasar dari perintah umask adalah sebagai berikut:

```
umask [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum untuk umask beserta penjelasannya:

- `-S`: Menampilkan umask dalam format simbolik.
- `-p`: Menampilkan umask saat ini dengan format yang lebih mudah dibaca.
- `value`: Menetapkan nilai umask baru, biasanya dalam format oktal.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan umask:

1. **Menampilkan nilai umask saat ini:**
   ```bash
   umask
   ```

2. **Mengatur umask menjadi 027 (izin untuk pemilik dan grup, tidak ada untuk lainnya):**
   ```bash
   umask 027
   ```

3. **Menampilkan umask dalam format simbolik:**
   ```bash
   umask -S
   ```

4. **Mengatur umask menjadi 007 (hanya pemilik yang memiliki izin penuh, grup tidak memiliki izin, dan lainnya tidak memiliki izin):**
   ```bash
   umask 007
   ```

## Tips
- Selalu periksa nilai umask Anda sebelum membuat file baru untuk memastikan izin yang sesuai.
- Pertimbangkan untuk menetapkan umask yang lebih ketat di lingkungan multi-pengguna untuk meningkatkan keamanan.
- Anda dapat menambahkan perintah umask ke file konfigurasi shell (seperti `.bashrc` atau `.bash_profile`) untuk menetapkan nilai default setiap kali Anda membuka terminal.