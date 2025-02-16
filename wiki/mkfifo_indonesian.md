# [Linux] Bash mkfifo Penggunaan: Membuat FIFO (named pipe)

## Overview
Perintah `mkfifo` digunakan untuk membuat FIFO (First In First Out) atau named pipe di sistem operasi berbasis Unix. FIFO memungkinkan proses untuk berkomunikasi satu sama lain dengan cara mengirim dan menerima data secara berurutan.

## Usage
Berikut adalah sintaks dasar dari perintah `mkfifo`:

```bash
mkfifo [options] [arguments]
```

## Common Options
- `-m, --mode=MODE` : Menentukan mode akses untuk FIFO yang dibuat, menggunakan notasi oktal atau simbolik.
- `--help` : Menampilkan bantuan tentang penggunaan perintah `mkfifo`.
- `--version` : Menampilkan versi dari perintah `mkfifo`.

## Common Examples
Berikut adalah beberapa contoh penggunaan `mkfifo`:

1. **Membuat FIFO sederhana:**
   ```bash
   mkfifo mypipe
   ```

2. **Membuat FIFO dengan mode akses tertentu:**
   ```bash
   mkfifo -m 666 mypipe
   ```

3. **Membuat beberapa FIFO sekaligus:**
   ```bash
   mkfifo pipe1 pipe2 pipe3
   ```

4. **Menggunakan FIFO dalam proses komunikasi:**
   - Di terminal pertama, jalankan:
     ```bash
     cat < mypipe
     ```
   - Di terminal kedua, jalankan:
     ```bash
     echo "Hello, World!" > mypipe
     ```

## Tips
- Pastikan untuk menghapus FIFO setelah selesai digunakan dengan perintah `rm`, untuk menghindari kebingungan di direktori.
- Gunakan mode akses yang tepat saat membuat FIFO untuk memastikan bahwa proses lain dapat mengaksesnya sesuai kebutuhan.
- FIFO sangat berguna dalam skrip shell untuk mengalirkan data antara proses yang berjalan secara bersamaan.