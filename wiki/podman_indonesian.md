# [Linux] Bash podman penggunaan: Mengelola kontainer tanpa daemon

## Overview
Podman adalah alat baris perintah yang digunakan untuk mengelola kontainer dan gambar kontainer. Berbeda dengan Docker, Podman tidak memerlukan daemon yang berjalan di latar belakang, sehingga memberikan fleksibilitas dan keamanan yang lebih baik dalam pengelolaan kontainer.

## Usage
Berikut adalah sintaks dasar untuk menggunakan podman:

```
podman [options] [arguments]
```

## Common Options
- `run`: Menjalankan kontainer baru.
- `ps`: Menampilkan daftar kontainer yang sedang berjalan.
- `images`: Menampilkan daftar gambar kontainer yang tersedia.
- `rm`: Menghapus kontainer yang tidak lagi diperlukan.
- `rmi`: Menghapus gambar kontainer.

## Common Examples
Berikut adalah beberapa contoh penggunaan podman:

### Menjalankan Kontainer
Untuk menjalankan kontainer baru dengan gambar tertentu:
```bash
podman run -d nginx
```

### Menampilkan Kontainer yang Sedang Berjalan
Untuk melihat daftar kontainer yang sedang berjalan:
```bash
podman ps
```

### Menampilkan Gambar Kontainer
Untuk melihat daftar gambar kontainer yang tersedia:
```bash
podman images
```

### Menghapus Kontainer
Untuk menghapus kontainer yang tidak lagi diperlukan:
```bash
podman rm <container_id>
```

### Menghapus Gambar Kontainer
Untuk menghapus gambar kontainer:
```bash
podman rmi <image_id>
```

## Tips
- Selalu gunakan opsi `-d` saat menjalankan kontainer jika Anda ingin menjalankannya di latar belakang.
- Gunakan `podman ps -a` untuk menampilkan semua kontainer, termasuk yang sudah berhenti.
- Manfaatkan tag pada gambar untuk mengelola versi yang berbeda dengan lebih mudah.