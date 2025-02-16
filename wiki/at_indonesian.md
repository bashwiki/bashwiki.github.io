# [Linux] Bash di at: Menjadwalkan Eksekusi Perintah

## Overview
Perintah `at` digunakan untuk menjadwalkan eksekusi perintah atau skrip pada waktu tertentu di masa depan. Ini sangat berguna ketika Anda ingin menjalankan tugas secara otomatis tanpa harus berada di terminal pada saat itu.

## Usage
Berikut adalah sintaks dasar dari perintah `at`:

```
at [options] [arguments]
```

## Common Options
- `-f FILE`: Menentukan file yang berisi perintah yang akan dijalankan.
- `-m`: Mengirimkan email setelah perintah selesai dijalankan, meskipun tidak ada output.
- `-q QUEUE`: Menentukan antrian untuk perintah yang dijadwalkan.
- `-l`: Menampilkan daftar pekerjaan yang telah dijadwalkan.

## Common Examples

1. **Menjadwalkan perintah untuk dijalankan sekarang**:
   ```bash
   echo "echo Hello, World!" | at now
   ```

2. **Menjadwalkan perintah untuk dijalankan pada waktu tertentu**:
   ```bash
   echo "backup.sh" | at 14:00
   ```

3. **Menjadwalkan perintah untuk dijalankan pada hari tertentu**:
   ```bash
   echo "cleanup.sh" | at 09:00 tomorrow
   ```

4. **Menjadwalkan perintah dari file**:
   ```bash
   at -f /path/to/script.sh 15:00
   ```

5. **Melihat daftar pekerjaan yang dijadwalkan**:
   ```bash
   atq
   ```

## Tips
- Pastikan untuk memeriksa waktu sistem Anda agar perintah dijadwalkan pada waktu yang tepat.
- Gunakan opsi `-m` jika Anda ingin mendapatkan notifikasi setelah perintah selesai.
- Untuk menghapus pekerjaan yang dijadwalkan, gunakan perintah `atrm` diikuti dengan nomor pekerjaan yang ditampilkan oleh `atq`.