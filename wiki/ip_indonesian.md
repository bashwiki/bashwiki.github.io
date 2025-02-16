# [Linux] Bash ip Penggunaan: Mengelola jaringan dan alamat IP

## Overview
Perintah `ip` digunakan untuk mengelola dan mengkonfigurasi jaringan serta alamat IP pada sistem Linux. Ini adalah alat yang kuat untuk mengatur dan memantau pengaturan jaringan.

## Usage
Sintaks dasar dari perintah `ip` adalah sebagai berikut:
```
ip [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `ip`:

- `addr`: Menampilkan atau mengelola alamat IP.
- `link`: Menampilkan atau mengelola antarmuka jaringan.
- `route`: Menampilkan atau mengelola tabel routing.
- `neigh`: Mengelola tabel neighbor (tetangga) untuk protokol ARP.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `ip`:

1. **Menampilkan alamat IP dari semua antarmuka jaringan:**
   ```bash
   ip addr show
   ```

2. **Menambahkan alamat IP baru ke antarmuka tertentu:**
   ```bash
   ip addr add 192.168.1.10/24 dev eth0
   ```

3. **Menghapus alamat IP dari antarmuka:**
   ```bash
   ip addr del 192.168.1.10/24 dev eth0
   ```

4. **Menampilkan tabel routing:**
   ```bash
   ip route show
   ```

5. **Menambahkan rute baru:**
   ```bash
   ip route add 10.0.0.0/8 via 192.168.1.1
   ```

## Tips
- Selalu gunakan opsi `show` untuk memverifikasi pengaturan setelah melakukan perubahan.
- Gunakan `ip link set <interface> up` untuk mengaktifkan antarmuka yang dinonaktifkan.
- Untuk mendapatkan informasi lebih lanjut tentang opsi dan argumen, Anda dapat menggunakan `man ip` untuk membuka manual perintah.