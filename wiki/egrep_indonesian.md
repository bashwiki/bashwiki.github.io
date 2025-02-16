# [Linux] Bash egrep Penggunaan: Mencari pola dalam teks

## Overview
Perintah `egrep` adalah alat yang digunakan untuk mencari pola dalam teks menggunakan ekspresi reguler. `egrep` adalah versi dari `grep` yang mendukung ekspresi reguler yang lebih kuat, memungkinkan pencarian yang lebih kompleks dan fleksibel.

## Usage
Berikut adalah sintaks dasar dari perintah `egrep`:

```bash
egrep [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `egrep`:

- `-i`: Mengabaikan perbedaan antara huruf besar dan kecil saat mencari.
- `-v`: Menampilkan baris yang tidak cocok dengan pola yang diberikan.
- `-c`: Menghitung jumlah baris yang cocok dengan pola.
- `-n`: Menampilkan nomor baris dari hasil pencarian.
- `-r`: Mencari secara rekursif dalam direktori.

## Common Examples
Berikut adalah beberapa contoh penggunaan `egrep`:

1. Mencari kata "contoh" dalam file `teks.txt`:
   ```bash
   egrep "contoh" teks.txt
   ```

2. Mencari kata "contoh" tanpa memperhatikan huruf besar/kecil:
   ```bash
   egrep -i "contoh" teks.txt
   ```

3. Menampilkan baris yang tidak mengandung kata "contoh":
   ```bash
   egrep -v "contoh" teks.txt
   ```

4. Menghitung jumlah baris yang mengandung kata "contoh":
   ```bash
   egrep -c "contoh" teks.txt
   ```

5. Mencari secara rekursif dalam semua file di direktori saat ini:
   ```bash
   egrep -r "contoh" .
   ```

## Tips
- Gunakan opsi `-i` jika Anda tidak yakin tentang penggunaan huruf besar/kecil dalam pencarian.
- Kombinasikan `egrep` dengan perintah lain menggunakan pipe (`|`) untuk memfilter hasil lebih lanjut.
- Selalu gunakan tanda kutip untuk pola yang mengandung spasi atau karakter khusus agar tidak terjadi kesalahan dalam interpretasi perintah.