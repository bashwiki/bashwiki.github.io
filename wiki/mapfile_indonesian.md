# [Linux] Bash mapfile Penggunaan: Membaca file ke dalam array

## Overview
Perintah `mapfile` dalam Bash digunakan untuk membaca isi dari file dan menyimpannya ke dalam array. Ini sangat berguna ketika Anda ingin memproses data dari file baris demi baris.

## Usage
Berikut adalah sintaks dasar dari perintah `mapfile`:

```bash
mapfile [options] [array_name]
```

## Common Options
- `-n N`: Membaca hanya N baris dari file.
- `-s N`: Melewati N baris pertama dari file.
- `-t`: Menghilangkan karakter newline dari setiap baris yang dibaca.

## Common Examples

### Contoh 1: Membaca file ke dalam array
Membaca semua baris dari file `data.txt` ke dalam array `lines`:

```bash
mapfile lines < data.txt
```

### Contoh 2: Membaca dengan melewati beberapa baris
Melewati 2 baris pertama dari file `data.txt` dan membaca sisanya ke dalam array `lines`:

```bash
mapfile -s 2 lines < data.txt
```

### Contoh 3: Membaca hanya beberapa baris
Membaca hanya 3 baris pertama dari file `data.txt` ke dalam array `lines`:

```bash
mapfile -n 3 lines < data.txt
```

### Contoh 4: Menghilangkan newline
Membaca file `data.txt` dan menghilangkan karakter newline dari setiap baris:

```bash
mapfile -t lines < data.txt
```

## Tips
- Pastikan file yang ingin dibaca ada dan dapat diakses untuk menghindari kesalahan.
- Gunakan opsi `-t` jika Anda ingin memproses data tanpa karakter newline, terutama saat melakukan operasi string.
- Cobalah untuk menggabungkan beberapa opsi untuk memaksimalkan penggunaan `mapfile` sesuai kebutuhan Anda.