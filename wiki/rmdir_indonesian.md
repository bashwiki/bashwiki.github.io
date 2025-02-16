# [Linux] Bash rmdir Penggunaan: Menghapus direktori kosong

## Overview
Perintah `rmdir` digunakan untuk menghapus direktori yang kosong. Jika direktori yang ingin dihapus berisi file atau subdirektori, perintah ini tidak akan berhasil dan akan menampilkan pesan kesalahan.

## Usage
Berikut adalah sintaks dasar dari perintah `rmdir`:

```
rmdir [options] [arguments]
```

## Common Options
- `-p`: Menghapus direktori beserta direktori induknya jika kosong.
- `--ignore-fail-on-non-empty`: Mengabaikan kesalahan jika direktori tidak kosong.

## Common Examples

### Menghapus direktori kosong
Untuk menghapus direktori bernama `folder_kosong`, gunakan perintah berikut:

```bash
rmdir folder_kosong
```

### Menghapus beberapa direktori kosong sekaligus
Anda dapat menghapus beberapa direktori kosong dengan satu perintah:

```bash
rmdir folder1 folder2 folder3
```

### Menghapus direktori dan direktori induknya
Jika Anda ingin menghapus direktori `folder_baru` dan direktori induknya jika juga kosong, gunakan opsi `-p`:

```bash
rmdir -p folder_baru/folder_induk
```

## Tips
- Pastikan direktori yang ingin dihapus benar-benar kosong, karena `rmdir` tidak akan menghapus direktori yang berisi file.
- Gunakan perintah `ls` untuk memeriksa isi direktori sebelum menghapusnya.
- Jika Anda perlu menghapus direktori yang tidak kosong, pertimbangkan menggunakan perintah `rm -r` dengan hati-hati, karena ini akan menghapus semua isi direktori secara rekursif.