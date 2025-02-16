# [Linux] Bash grep Penggunaan: Mencari pola dalam teks

## Overview
Perintah `grep` digunakan untuk mencari pola tertentu dalam file atau output dari perintah lain. Ini sangat berguna untuk menemukan informasi spesifik dalam teks yang panjang atau dalam log file.

## Usage
Sintaks dasar dari perintah `grep` adalah sebagai berikut:

```bash
grep [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang digunakan dengan `grep`:

- `-i`: Mengabaikan perbedaan antara huruf besar dan kecil.
- `-r`: Mencari secara rekursif dalam direktori.
- `-v`: Menampilkan baris yang tidak cocok dengan pola.
- `-n`: Menampilkan nomor baris dari hasil pencarian.
- `-l`: Menampilkan nama file yang mengandung pola yang dicari.

## Common Examples
Berikut adalah beberapa contoh penggunaan `grep`:

1. Mencari kata "error" dalam file `log.txt`:
   ```bash
   grep "error" log.txt
   ```

2. Mencari kata "success" tanpa memperhatikan huruf besar/kecil:
   ```bash
   grep -i "success" log.txt
   ```

3. Mencari pola dalam semua file di direktori secara rekursif:
   ```bash
   grep -r "pattern" /path/to/directory
   ```

4. Menampilkan nomor baris dari hasil pencarian:
   ```bash
   grep -n "warning" log.txt
   ```

5. Menampilkan nama file yang mengandung kata "failed":
   ```bash
   grep -l "failed" *.txt
   ```

## Tips
- Gunakan opsi `-i` jika Anda tidak yakin tentang huruf besar/kecil dalam pencarian.
- Kombinasikan `grep` dengan perintah lain menggunakan pipe (`|`) untuk mempersempit hasil pencarian.
- Simpan hasil pencarian ke dalam file dengan menggunakan redirection (`>`):
  ```bash
  grep "pattern" log.txt > hasil.txt
  ```