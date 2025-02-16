# [Linux] Bash blkid Penggunaan: Menampilkan informasi perangkat penyimpanan

## Overview
Perintah `blkid` digunakan untuk menampilkan informasi tentang perangkat penyimpanan yang terhubung ke sistem, seperti partisi dan sistem file. Ini berguna untuk mengetahui UUID (Universally Unique Identifier), tipe sistem file, dan label dari perangkat penyimpanan.

## Usage
Berikut adalah sintaks dasar dari perintah `blkid`:

```
blkid [options] [arguments]
```

## Common Options
- `-o`: Menentukan format output. Misalnya, `-o value` hanya menampilkan nilai dari atribut tertentu.
- `-s`: Menentukan atribut yang ingin ditampilkan, seperti `UUID`, `TYPE`, atau `LABEL`.
- `-p`: Mengabaikan cache dan membaca informasi langsung dari perangkat.
- `-c`: Menentukan file cache untuk menyimpan hasil.

## Common Examples
Berikut adalah beberapa contoh penggunaan `blkid`:

1. **Menampilkan semua perangkat penyimpanan:**
   ```bash
   blkid
   ```

2. **Menampilkan informasi dengan format output tertentu:**
   ```bash
   blkid -o list
   ```

3. **Menampilkan hanya UUID dari perangkat tertentu:**
   ```bash
   blkid -s UUID /dev/sda1
   ```

4. **Mengabaikan cache dan membaca informasi langsung:**
   ```bash
   blkid -p
   ```

## Tips
- Gunakan `blkid` dengan opsi `-o` untuk mendapatkan output yang lebih terstruktur dan mudah dibaca.
- Pastikan untuk menjalankan perintah ini dengan hak akses yang sesuai, terutama jika Anda ingin mengakses informasi dari perangkat yang dilindungi.
- Anda dapat menggabungkan `blkid` dengan perintah lain seperti `grep` untuk mencari informasi spesifik. Contoh:
  ```bash
  blkid | grep sda
  ```