# [Linux] Bash true: [mengembalikan nilai benar]

## Overview
Perintah `true` dalam Bash adalah sebuah perintah sederhana yang selalu mengembalikan nilai keluar (exit status) 0, yang menunjukkan bahwa perintah tersebut berhasil dijalankan. Ini sering digunakan dalam skrip untuk menandakan keberhasilan atau untuk mengisi tempat yang memerlukan perintah yang valid.

## Usage
Berikut adalah sintaks dasar dari perintah `true`:

```bash
true [options] [arguments]
```

## Common Options
Perintah `true` tidak memiliki opsi atau argumen yang signifikan. Namun, Anda dapat menggunakan beberapa opsi umum yang berlaku untuk banyak perintah di Bash, seperti:

- `--help`: Menampilkan bantuan tentang penggunaan perintah.
- `--version`: Menampilkan versi dari perintah `true`.

## Common Examples

### Contoh 1: Menggunakan true dalam skrip
Anda dapat menggunakan `true` dalam skrip untuk menandakan bahwa bagian tertentu dari skrip telah berhasil dijalankan.

```bash
#!/bin/bash

if true; then
    echo "Ini selalu benar!"
fi
```

### Contoh 2: Menggunakan true dalam loop
`true` sering digunakan dalam loop untuk membuat loop yang berjalan terus-menerus.

```bash
while true; do
    echo "Loop ini akan terus berjalan..."
    sleep 1
done
```

### Contoh 3: Menggunakan true untuk mengisi tempat
`true` dapat digunakan untuk mengisi tempat dalam perintah yang memerlukan perintah yang valid.

```bash
command || true
```

## Tips
- Gunakan `true` untuk menghindari kesalahan dalam skrip ketika Anda membutuhkan perintah yang selalu berhasil.
- Kombinasikan `true` dengan perintah lain menggunakan operator logika untuk mengontrol alur eksekusi skrip.
- Meskipun `true` tidak memiliki opsi, Anda dapat menggunakan `--help` atau `--version` untuk mendapatkan informasi lebih lanjut tentang perintah ini.