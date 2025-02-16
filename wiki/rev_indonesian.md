# [Linux] Bash rev: Membalikkan teks dalam setiap baris

## Overview
Perintah `rev` digunakan untuk membalikkan urutan karakter dalam setiap baris dari input yang diberikan. Ini sangat berguna ketika Anda perlu memanipulasi teks dengan cara yang tidak biasa atau hanya ingin melihat hasil yang terbalik.

## Usage
Berikut adalah sintaks dasar dari perintah `rev`:

```bash
rev [options] [arguments]
```

## Common Options
- `-o, --output=FILE` : Menentukan file output untuk menyimpan hasil.
- `-h, --help` : Menampilkan pesan bantuan dan keluar.
- `-V, --version` : Menampilkan versi dari perintah `rev`.

## Common Examples

1. **Membalikkan teks dari input standar:**
   ```bash
   echo "Hello World" | rev
   ```
   Output:
   ```
   dlroW olleH
   ```

2. **Membalikkan isi dari sebuah file:**
   ```bash
   rev file.txt
   ```
   Ini akan membalikkan setiap baris dalam `file.txt`.

3. **Menyimpan hasil ke file lain:**
   ```bash
   rev file.txt > reversed.txt
   ```
   Ini akan membalikkan isi `file.txt` dan menyimpannya ke dalam `reversed.txt`.

4. **Menggunakan opsi output:**
   ```bash
   rev --output=reversed.txt file.txt
   ```
   Ini juga membalikkan isi `file.txt` dan menyimpannya ke dalam `reversed.txt`.

## Tips
- Gunakan `rev` dalam kombinasi dengan perintah lain menggunakan pipe (`|`) untuk manipulasi teks yang lebih kompleks.
- Pastikan untuk memeriksa hasil output, terutama saat bekerja dengan file besar, untuk memastikan tidak ada kesalahan dalam pembalikan teks.
- Cobalah menggunakan `rev` dalam skrip untuk otomatisasi tugas yang melibatkan manipulasi teks.