# [Linux] Bash wget Penggunaan: Mengunduh file dari internet

## Overview
Perintah `wget` adalah alat baris perintah yang digunakan untuk mengunduh file dari internet. Dengan `wget`, pengguna dapat mengunduh file dengan mudah melalui HTTP, HTTPS, dan FTP. Perintah ini sangat berguna untuk mengunduh file besar atau banyak file sekaligus.

## Usage
Berikut adalah sintaks dasar dari perintah `wget`:

```
wget [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `wget`:

- `-O [file]`: Menyimpan file yang diunduh dengan nama yang ditentukan.
- `-c`: Melanjutkan unduhan yang terputus.
- `-r`: Mengunduh secara rekursif, termasuk semua file yang terkait.
- `--limit-rate=[rate]`: Membatasi kecepatan unduhan.
- `-q`: Menjalankan dalam mode tenang (quiet mode), tanpa output ke layar.

## Common Examples
Berikut adalah beberapa contoh penggunaan `wget`:

1. **Mengunduh file tunggal:**
   ```bash
   wget https://example.com/file.zip
   ```

2. **Mengunduh file dengan nama yang berbeda:**
   ```bash
   wget -O myfile.zip https://example.com/file.zip
   ```

3. **Melanjutkan unduhan yang terputus:**
   ```bash
   wget -c https://example.com/largefile.zip
   ```

4. **Mengunduh seluruh situs web secara rekursif:**
   ```bash
   wget -r https://example.com
   ```

5. **Membatasi kecepatan unduhan:**
   ```bash
   wget --limit-rate=200k https://example.com/file.zip
   ```

## Tips
- Selalu periksa URL sebelum mengunduh untuk memastikan keamanannya.
- Gunakan opsi `-q` jika Anda ingin menjalankan unduhan di latar belakang tanpa output yang mengganggu.
- Untuk mengunduh beberapa file sekaligus, Anda bisa menggunakan file teks yang berisi daftar URL dan menjalankan `wget -i [file.txt]`.