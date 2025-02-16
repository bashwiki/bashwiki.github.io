# [Linux] Bash groupmod Penggunaan: Mengubah Grup Pengguna

## Overview
Perintah `groupmod` digunakan untuk mengubah atribut dari grup yang sudah ada di sistem Linux. Dengan perintah ini, Anda dapat mengubah nama grup atau GID (Group ID) grup yang ada.

## Usage
Berikut adalah sintaks dasar dari perintah `groupmod`:

```bash
groupmod [options] [arguments]
```

## Common Options
- `-n, --new-name NEW_GROUP`: Mengubah nama grup menjadi `NEW_GROUP`.
- `-g, --gid GID`: Mengubah GID grup menjadi nilai yang ditentukan.
- `-h, --help`: Menampilkan bantuan penggunaan perintah ini.

## Common Examples
Berikut adalah beberapa contoh penggunaan `groupmod`:

1. **Mengubah nama grup:**
   Untuk mengubah nama grup dari `oldgroup` menjadi `newgroup`, gunakan perintah berikut:
   ```bash
   groupmod -n newgroup oldgroup
   ```

2. **Mengubah GID grup:**
   Jika Anda ingin mengubah GID grup `mygroup` menjadi `1001`, gunakan perintah ini:
   ```bash
   groupmod -g 1001 mygroup
   ```

3. **Mengubah nama dan GID grup:**
   Untuk mengubah nama grup `example` menjadi `sample` dan GID menjadi `2000`, Anda dapat menggunakan:
   ```bash
   groupmod -n sample -g 2000 example
   ```

## Tips
- Pastikan Anda memiliki hak akses yang diperlukan (biasanya sebagai pengguna root) untuk menjalankan perintah `groupmod`.
- Selalu periksa apakah grup yang ingin Anda ubah ada di sistem dengan menggunakan perintah `getent group`.
- Setelah mengubah grup, pastikan untuk memeriksa apakah perubahan telah diterapkan dengan benar menggunakan `getent group` atau `cat /etc/group`.