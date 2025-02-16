# [Linux] Bash su Penggunaan: Mengganti pengguna dalam sesi terminal

## Overview
Perintah `su` (substitute user) digunakan untuk mengganti pengguna dalam sesi terminal. Dengan perintah ini, pengguna dapat menjalankan perintah sebagai pengguna lain, biasanya sebagai pengguna root, yang memberikan akses lebih tinggi untuk melakukan tugas administratif.

## Usage
Berikut adalah sintaks dasar dari perintah `su`:

```bash
su [options] [username]
```

Jika `username` tidak ditentukan, perintah ini akan mencoba mengganti ke pengguna root secara default.

## Common Options
- `-` atau `--login`: Menjalankan shell login untuk pengguna yang dituju, yang berarti lingkungan pengguna baru akan dimuat.
- `-c`: Menjalankan perintah tertentu sebagai pengguna yang dituju.
- `-s`: Menentukan shell yang akan digunakan untuk sesi.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `su`:

1. **Mengganti ke pengguna root:**
   ```bash
   su
   ```
   Setelah menjalankan perintah ini, Anda akan diminta untuk memasukkan kata sandi root.

2. **Mengganti ke pengguna tertentu:**
   ```bash
   su username
   ```
   Gantilah `username` dengan nama pengguna yang ingin Anda masuki.

3. **Menjalankan perintah sebagai pengguna lain:**
   ```bash
   su -c 'ls /root'
   ```
   Perintah ini akan menjalankan `ls /root` sebagai pengguna root.

4. **Mengganti ke pengguna dengan shell yang berbeda:**
   ```bash
   su -s /bin/bash username
   ```
   Ini akan mengganti ke pengguna `username` menggunakan shell Bash.

## Tips
- Selalu gunakan `su` dengan hati-hati, terutama saat mengganti ke pengguna root, untuk menghindari perubahan yang tidak diinginkan pada sistem.
- Pertimbangkan untuk menggunakan `sudo` sebagai alternatif yang lebih aman untuk menjalankan perintah tertentu dengan hak akses yang lebih tinggi tanpa harus mengganti pengguna sepenuhnya.
- Pastikan Anda memiliki kata sandi yang benar untuk pengguna yang ingin Anda ganti.