# [Linux] Bash yum Penggunaan: Manajemen paket di sistem Linux

## Overview
Perintah `yum` (Yellowdog Updater Modified) adalah alat manajemen paket yang digunakan pada distribusi Linux berbasis RPM. Dengan `yum`, pengguna dapat menginstal, memperbarui, menghapus, dan mengelola paket perangkat lunak dengan mudah.

## Usage
Berikut adalah sintaks dasar dari perintah `yum`:

```bash
yum [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang sering digunakan dengan `yum`:

- `install`: Menginstal paket baru.
- `remove`: Menghapus paket yang sudah terinstal.
- `update`: Memperbarui semua paket yang terinstal ke versi terbaru.
- `search`: Mencari paket berdasarkan nama atau deskripsi.
- `info`: Menampilkan informasi tentang paket tertentu.

## Common Examples
Berikut adalah beberapa contoh penggunaan `yum`:

1. **Menginstal paket**:
   ```bash
   yum install nama_paket
   ```

2. **Menghapus paket**:
   ```bash
   yum remove nama_paket
   ```

3. **Memperbarui semua paket**:
   ```bash
   yum update
   ```

4. **Mencari paket**:
   ```bash
   yum search kata_kunci
   ```

5. **Menampilkan informasi tentang paket**:
   ```bash
   yum info nama_paket
   ```

## Tips
- Selalu jalankan `yum update` secara berkala untuk memastikan sistem Anda memiliki paket terbaru dan keamanan yang diperbarui.
- Gunakan opsi `-y` untuk mengotomatiskan persetujuan saat menginstal atau memperbarui paket, contohnya: `yum -y install nama_paket`.
- Periksa dependensi paket sebelum menginstal untuk menghindari masalah di kemudian hari.