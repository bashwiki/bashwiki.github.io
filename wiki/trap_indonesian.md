# [Linux] Bash trap Penggunaan: Menangani sinyal dan kejadian

## Overview
Perintah `trap` dalam Bash digunakan untuk menangani sinyal dan kejadian tertentu yang terjadi selama eksekusi skrip. Dengan menggunakan `trap`, Anda dapat menentukan tindakan yang harus diambil ketika skrip menerima sinyal tertentu, seperti SIGINT (dari Ctrl+C) atau SIGTERM.

## Usage
Sintaks dasar dari perintah `trap` adalah sebagai berikut:

```bash
trap [options] [commands] [signals]
```

## Common Options
Beberapa opsi umum untuk `trap` meliputi:
- `-l`: Menampilkan daftar sinyal yang tersedia.
- `-p`: Menampilkan perintah yang terdaftar untuk sinyal tertentu.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `trap`:

### Contoh 1: Menangani SIGINT
Menangkap sinyal SIGINT dan menjalankan perintah tertentu sebelum keluar.

```bash
trap 'echo "Sinyal SIGINT diterima. Keluar dari skrip."' SIGINT
while true; do
    echo "Menjalankan skrip... Tekan Ctrl+C untuk menghentikan."
    sleep 2
done
```

### Contoh 2: Menangani SIGTERM
Menangkap sinyal SIGTERM dan melakukan pembersihan sebelum keluar.

```bash
trap 'echo "Menangani SIGTERM. Melakukan pembersihan..."; exit' SIGTERM
while true; do
    echo "Skrip berjalan. Kirim SIGTERM untuk menghentikan."
    sleep 2
done
```

### Contoh 3: Menampilkan daftar sinyal
Menggunakan opsi `-l` untuk menampilkan semua sinyal yang tersedia.

```bash
trap -l
```

## Tips
- Gunakan `trap` untuk memastikan bahwa skrip Anda dapat menangani sinyal dengan baik, terutama saat melakukan operasi yang memerlukan pembersihan.
- Selalu sertakan perintah pembersihan dalam `trap` untuk menghindari kehilangan data atau keadaan tidak konsisten.
- Uji skrip Anda dengan mengirimkan sinyal yang berbeda untuk memastikan bahwa `trap` berfungsi seperti yang diharapkan.