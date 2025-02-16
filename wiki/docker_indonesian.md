# [Linux] Bash docker penggunaan: Mengelola kontainer dan gambar

## Overview
Perintah `docker` digunakan untuk mengelola kontainer dan gambar dalam lingkungan Docker. Docker memungkinkan pengguna untuk menjalankan aplikasi dalam kontainer yang terisolasi, sehingga memudahkan pengembangan, pengujian, dan penyebaran aplikasi.

## Usage
Sintaks dasar dari perintah docker adalah sebagai berikut:

```bash
docker [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang sering digunakan dengan perintah docker:

- `run`: Menjalankan kontainer baru.
- `ps`: Menampilkan daftar kontainer yang sedang berjalan.
- `images`: Menampilkan daftar gambar yang tersedia.
- `rm`: Menghapus satu atau lebih kontainer.
- `rmi`: Menghapus satu atau lebih gambar.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah docker:

1. **Menjalankan kontainer baru dari gambar**:
   ```bash
   docker run hello-world
   ```

2. **Menampilkan daftar kontainer yang sedang berjalan**:
   ```bash
   docker ps
   ```

3. **Menampilkan semua kontainer, termasuk yang tidak berjalan**:
   ```bash
   docker ps -a
   ```

4. **Menghapus kontainer yang tidak lagi diperlukan**:
   ```bash
   docker rm <container_id>
   ```

5. **Menghapus gambar yang tidak lagi diperlukan**:
   ```bash
   docker rmi <image_id>
   ```

## Tips
- Selalu periksa gambar dan kontainer yang tidak terpakai untuk menghemat ruang disk.
- Gunakan tag pada gambar untuk mengelola versi dengan lebih baik.
- Manfaatkan Docker Compose untuk mengelola aplikasi multi-kontainer dengan lebih mudah.