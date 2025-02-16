# [Linux] Bash realpath Penggunaan: Menyelesaikan jalur file absolut

## Overview
Perintah `realpath` digunakan untuk mengubah jalur relatif atau simbolik menjadi jalur absolut. Ini sangat berguna untuk memastikan bahwa Anda bekerja dengan jalur yang tepat, terutama ketika berurusan dengan file dan direktori yang mungkin memiliki tautan simbolik.

## Usage
Sintaks dasar dari perintah `realpath` adalah sebagai berikut:

```
realpath [options] [arguments]
```

## Common Options
- `-m`, `--canonicalize-missing`: Mengembalikan jalur absolut meskipun file tidak ada.
- `-q`, `--quiet`: Tidak menampilkan pesan kesalahan jika jalur tidak valid.
- `-s`, `--strip`: Menghapus komponen yang tidak perlu dari jalur.

## Common Examples
Berikut adalah beberapa contoh penggunaan `realpath`:

1. Mengubah jalur relatif menjadi jalur absolut:
   ```bash
   realpath ./folder/file.txt
   ```

2. Menggunakan opsi untuk mengabaikan kesalahan jika file tidak ada:
   ```bash
   realpath -m ./nonexistentfile.txt
   ```

3. Menghapus komponen yang tidak perlu dari jalur:
   ```bash
   realpath -s /home/user/../user/folder/./file.txt
   ```

4. Menggunakan `realpath` pada tautan simbolik:
   ```bash
   realpath /path/to/symlink
   ```

## Tips
- Selalu gunakan `realpath` saat bekerja dengan jalur file untuk menghindari kebingungan antara jalur relatif dan absolut.
- Manfaatkan opsi `-m` untuk menghindari kesalahan ketika bekerja dengan file yang mungkin tidak ada.
- Gunakan `realpath` dalam skrip untuk memastikan bahwa jalur file yang digunakan selalu valid dan terstandarisasi.