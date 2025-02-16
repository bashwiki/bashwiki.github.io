# [Linux] Bash route penggunaan: Mengelola tabel rute jaringan

## Overview
Perintah `route` digunakan untuk menampilkan dan mengelola tabel rute jaringan di sistem operasi berbasis Unix/Linux. Dengan menggunakan perintah ini, pengguna dapat menambah, menghapus, atau mengubah rute yang digunakan oleh sistem untuk mengarahkan lalu lintas jaringan.

## Usage
Berikut adalah sintaks dasar dari perintah `route`:

```bash
route [options] [arguments]
```

## Common Options
- `-n`: Menampilkan alamat IP numerik tanpa mencoba untuk menyelesaikan nama host.
- `add`: Menambahkan rute baru ke tabel rute.
- `del`: Menghapus rute dari tabel rute.
- `-net`: Menunjukkan bahwa argumen berikutnya adalah alamat jaringan.
- `-host`: Menunjukkan bahwa argumen berikutnya adalah alamat host.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `route`:

1. **Menampilkan tabel rute saat ini:**
   ```bash
   route -n
   ```

2. **Menambahkan rute baru:**
   ```bash
   route add -net 192.168.1.0/24 gw 192.168.1.1
   ```

3. **Menghapus rute yang ada:**
   ```bash
   route del -net 192.168.1.0/24
   ```

4. **Menambahkan rute untuk host tertentu:**
   ```bash
   route add -host 10.0.0.5 gw 10.0.0.1
   ```

## Tips
- Selalu gunakan opsi `-n` saat menampilkan tabel rute untuk mempercepat proses dan menghindari resolusi nama yang tidak perlu.
- Pastikan untuk memeriksa tabel rute setelah menambahkan atau menghapus rute untuk memastikan perubahan telah diterapkan dengan benar.
- Gunakan perintah `ip route` sebagai alternatif modern untuk mengelola tabel rute, karena `route` dianggap lebih tua dan mungkin tidak tersedia di semua distribusi Linux.