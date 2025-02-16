# [Linux] Bash inotifywait Penggunaan: Memantau perubahan file dan direktori

## Overview
Perintah `inotifywait` digunakan untuk memantau perubahan pada file dan direktori di sistem Linux. Dengan menggunakan inotifywait, pengguna dapat mendeteksi berbagai jenis perubahan seperti penambahan, penghapusan, atau modifikasi file secara real-time.

## Usage
Sintaks dasar dari perintah `inotifywait` adalah sebagai berikut:

```bash
inotifywait [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `inotifywait`:

- `-m`: Memantau perubahan secara terus-menerus (monitor mode).
- `-r`: Memantau direktori secara rekursif.
- `-e`: Menentukan jenis peristiwa yang ingin dipantau, seperti `modify`, `create`, `delete`, dll.
- `-q`: Menjalankan dalam mode tenang, hanya menampilkan peristiwa tanpa informasi tambahan.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `inotifywait`:

1. **Memantau perubahan pada direktori tertentu:**
   ```bash
   inotifywait -m /path/to/directory
   ```

2. **Memantau perubahan file dengan jenis peristiwa tertentu:**
   ```bash
   inotifywait -m -e modify,create,delete /path/to/directory
   ```

3. **Memantau direktori secara rekursif:**
   ```bash
   inotifywait -mr /path/to/directory
   ```

4. **Menggunakan mode tenang untuk memantau perubahan:**
   ```bash
   inotifywait -mq -e modify /path/to/file
   ```

## Tips
- Gunakan opsi `-m` untuk memantau perubahan secara terus-menerus jika Anda ingin mendapatkan pembaruan real-time.
- Kombinasikan opsi `-e` dengan beberapa jenis peristiwa untuk mendapatkan informasi yang lebih spesifik.
- Pertimbangkan untuk menggunakan `inotifywait` dalam skrip untuk otomatisasi tugas berdasarkan perubahan file.