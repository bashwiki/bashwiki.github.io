# [Linux] Bash git penggunaan: Mengelola versi kode sumber

## Overview
Git adalah sistem kontrol versi yang digunakan untuk melacak perubahan dalam file dan kolaborasi dalam pengembangan perangkat lunak. Dengan git, pengguna dapat menyimpan riwayat perubahan, berkolaborasi dengan tim, dan mengelola berbagai versi proyek dengan efisien.

## Usage
Sintaks dasar untuk menggunakan git adalah sebagai berikut:
```
git [options] [arguments]
```

## Common Options
- `clone`: Mengunduh repositori dari server.
- `commit`: Menyimpan perubahan yang telah dilakukan ke dalam repositori.
- `push`: Mengunggah perubahan lokal ke repositori jarak jauh.
- `pull`: Mengunduh dan menggabungkan perubahan dari repositori jarak jauh.
- `status`: Menampilkan status file dalam repositori.

## Common Examples
Berikut adalah beberapa contoh penggunaan git yang umum:

1. **Mengkloning repositori**
   ```bash
   git clone https://github.com/username/repo.git
   ```

2. **Menambahkan perubahan ke staging area**
   ```bash
   git add file.txt
   ```

3. **Membuat commit dengan pesan**
   ```bash
   git commit -m "Pesan commit"
   ```

4. **Mengunggah perubahan ke repositori jarak jauh**
   ```bash
   git push origin main
   ```

5. **Mengunduh dan menggabungkan perubahan dari repositori jarak jauh**
   ```bash
   git pull origin main
   ```

6. **Menampilkan status file**
   ```bash
   git status
   ```

## Tips
- Selalu gunakan pesan commit yang jelas dan deskriptif agar mudah dipahami oleh anggota tim lainnya.
- Lakukan commit secara teratur untuk menyimpan kemajuan dan memudahkan pelacakan perubahan.
- Gunakan branch untuk mengembangkan fitur baru atau melakukan perbaikan tanpa mengganggu kode utama.
- Selalu periksa status repositori sebelum melakukan push atau pull untuk menghindari konflik.