# [Linux] Bash last: Menampilkan riwayat login pengguna

## Overview
Perintah `last` digunakan untuk menampilkan daftar login pengguna terakhir di sistem. Ini memberikan informasi tentang pengguna yang telah masuk, waktu login, serta durasi sesi mereka. Data ini diambil dari file log sistem.

## Usage
Berikut adalah sintaks dasar dari perintah `last`:

```bash
last [options] [arguments]
```

## Common Options
- `-a`: Menampilkan alamat IP atau hostname dari mana pengguna melakukan login.
- `-n [number]`: Menentukan jumlah entri yang ingin ditampilkan. Misalnya, `-n 5` akan menampilkan 5 entri terakhir.
- `-R`: Menghilangkan tampilan hostname atau alamat IP.
- `-x`: Menampilkan informasi tentang sesi yang tidak aktif, seperti reboot dan shutdown.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `last`:

1. Menampilkan semua login terakhir:
   ```bash
   last
   ```

2. Menampilkan 10 login terakhir:
   ```bash
   last -n 10
   ```

3. Menampilkan login terakhir dengan alamat IP:
   ```bash
   last -a
   ```

4. Menampilkan informasi login tanpa hostname:
   ```bash
   last -R
   ```

5. Menampilkan sesi reboot dan shutdown:
   ```bash
   last -x
   ```

## Tips
- Gunakan opsi `-n` untuk membatasi jumlah entri yang ditampilkan, sehingga lebih mudah untuk melihat informasi terbaru.
- Periksa file log `/var/log/wtmp` jika Anda ingin melihat lebih banyak detail tentang login yang lebih lama.
- Kombinasikan perintah `last` dengan `grep` untuk mencari login pengguna tertentu, misalnya:
  ```bash
  last | grep username
  ```