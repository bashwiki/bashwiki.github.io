# [Linux] Bash fgrep Penggunaan: Mencari string tetap dalam file

## Overview
Perintah `fgrep` adalah alat yang digunakan dalam sistem operasi berbasis Unix untuk mencari string tetap dalam file. Berbeda dengan `grep`, `fgrep` tidak melakukan ekspresi reguler, sehingga lebih cepat untuk pencarian string yang tidak berubah.

## Usage
Berikut adalah sintaks dasar dari perintah `fgrep`:

```
fgrep [options] [arguments]
```

## Common Options
- `-i`: Mengabaikan perbedaan antara huruf besar dan kecil saat mencari.
- `-v`: Menampilkan baris yang tidak cocok dengan pola yang diberikan.
- `-c`: Menghitung jumlah baris yang cocok dengan pola.
- `-n`: Menampilkan nomor baris dari hasil pencarian.
- `-r`: Mencari secara rekursif dalam direktori.

## Common Examples
Berikut adalah beberapa contoh penggunaan `fgrep`:

1. Mencari string tetap dalam file:
   ```bash
   fgrep "kata_kunci" file.txt
   ```

2. Mencari string tanpa memperhatikan huruf besar/kecil:
   ```bash
   fgrep -i "kata_kunci" file.txt
   ```

3. Menghitung jumlah baris yang cocok:
   ```bash
   fgrep -c "kata_kunci" file.txt
   ```

4. Menampilkan nomor baris dari hasil pencarian:
   ```bash
   fgrep -n "kata_kunci" file.txt
   ```

5. Mencari string dalam semua file di direktori secara rekursif:
   ```bash
   fgrep -r "kata_kunci" /path/to/directory
   ```

## Tips
- Gunakan opsi `-i` jika Anda tidak yakin tentang penggunaan huruf besar atau kecil dalam pencarian.
- Kombinasikan `fgrep` dengan perintah lain menggunakan pipe (`|`) untuk meningkatkan fungsionalitas.
- Pastikan untuk memeriksa file yang besar dengan hati-hati, karena hasil pencarian bisa sangat banyak.