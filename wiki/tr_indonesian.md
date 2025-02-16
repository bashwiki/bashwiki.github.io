# [Linux] Bash tr <Penggunaan setara>: Mengubah karakter dalam teks

## Overview
Perintah `tr` dalam Bash digunakan untuk mengubah atau menghapus karakter dalam input teks. Perintah ini sangat berguna untuk manipulasi string, seperti mengganti huruf atau menghapus karakter tertentu.

## Usage
Sintaks dasar dari perintah `tr` adalah sebagai berikut:

```bash
tr [options] [arguments]
```

## Common Options
- `-d`: Menghapus karakter yang ditentukan dari input.
- `-s`: Mengganti beberapa kemunculan karakter yang sama berurutan menjadi satu karakter.
- `-c`: Menggunakan karakter yang tidak ada dalam set yang ditentukan.
- `-t`: Mengganti karakter dalam set pertama dengan karakter dalam set kedua.

## Common Examples

1. **Mengganti huruf kecil dengan huruf besar:**
   ```bash
   echo "hello world" | tr 'a-z' 'A-Z'
   ```
   Output: `HELLO WORLD`

2. **Menghapus angka dari teks:**
   ```bash
   echo "abc123def456" | tr -d '0-9'
   ```
   Output: `abcdef`

3. **Mengganti spasi berlebih dengan satu spasi:**
   ```bash
   echo "This   is   a   test." | tr -s ' '
   ```
   Output: `This is a test.`

4. **Mengganti karakter tertentu:**
   ```bash
   echo "apple" | tr 'a' 'o'
   ```
   Output: `opple`

## Tips
- Selalu gunakan tanda kutip untuk menghindari masalah dengan karakter khusus.
- Kombinasikan `tr` dengan perintah lain menggunakan pipe (`|`) untuk manipulasi data yang lebih kompleks.
- Uji perintah `tr` dengan input yang berbeda untuk memahami cara kerjanya sebelum menggunakannya dalam skrip.