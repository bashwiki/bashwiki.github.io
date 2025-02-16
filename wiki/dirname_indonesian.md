# [Linux] Bash dirname Penggunaan: Mengambil nama direktori dari jalur file

## Overview
Perintah `dirname` digunakan untuk mengambil nama direktori dari jalur file yang diberikan. Ini berguna ketika Anda ingin memisahkan nama file dari jalurnya dan hanya mendapatkan bagian direktori.

## Usage
Sintaks dasar dari perintah `dirname` adalah sebagai berikut:

```bash
dirname [options] [arguments]
```

## Common Options
- `-z`: Menggunakan pemisah null untuk input dan output, berguna untuk menangani nama file dengan spasi atau karakter khusus.
- `--help`: Menampilkan bantuan tentang penggunaan perintah `dirname`.
- `--version`: Menampilkan versi dari perintah `dirname`.

## Common Examples
Berikut adalah beberapa contoh penggunaan `dirname`:

1. Mengambil nama direktori dari jalur file:
   ```bash
   dirname /home/user/documents/file.txt
   ```
   Output: `/home/user/documents`

2. Menggunakan `dirname` dengan jalur relatif:
   ```bash
   dirname ./folder/file.txt
   ```
   Output: `./folder`

3. Mengambil nama direktori dari jalur yang tidak memiliki file:
   ```bash
   dirname /home/user/documents/
   ```
   Output: `/home/user/documents`

4. Menggunakan `dirname` dalam skrip untuk mendapatkan direktori dari variabel:
   ```bash
   FILE_PATH="/home/user/documents/file.txt"
   DIR_NAME=$(dirname "$FILE_PATH")
   echo $DIR_NAME
   ```
   Output: `/home/user/documents`

## Tips
- Selalu gunakan tanda kutip pada jalur file yang mengandung spasi untuk menghindari kesalahan.
- Anda dapat menggabungkan `dirname` dengan perintah lain seperti `find` untuk mendapatkan direktori dari banyak file sekaligus.
- Gunakan opsi `-z` jika Anda bekerja dengan nama file yang mungkin mengandung karakter khusus atau spasi untuk memastikan hasil yang akurat.