# [Linux] Bash continue penggunaan: Melanjutkan eksekusi loop

## Overview
Perintah `continue` dalam Bash digunakan untuk melanjutkan eksekusi dari iterasi berikutnya dalam sebuah loop. Ketika `continue` dipanggil, perintah yang tersisa dalam iterasi saat ini akan dilewati, dan kontrol akan kembali ke awal loop untuk memulai iterasi berikutnya.

## Usage
Berikut adalah sintaks dasar dari perintah `continue`:

```bash
continue [n]
```

Di mana `n` adalah jumlah iterasi yang ingin dilewati. Jika tidak ditentukan, `continue` akan melewati iterasi saat ini dan melanjutkan ke iterasi berikutnya.

## Common Options
- `n`: Menentukan jumlah iterasi yang ingin dilewati. Misalnya, jika `n` diatur ke 2, maka dua iterasi berikutnya akan dilewati.

## Common Examples

### Contoh 1: Menggunakan continue dalam loop for
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo "Nomor: $i"
done
```
Output:
```
Nomor: 1
Nomor: 2
Nomor: 4
Nomor: 5
```
Pada contoh ini, ketika `i` sama dengan 3, perintah `continue` akan dilewati, sehingga angka 3 tidak akan ditampilkan.

### Contoh 2: Menggunakan continue dalam loop while
```bash
count=0
while [ $count -lt 5 ]; do
    count=$((count + 1))
    if [ $count -eq 2 ]; then
        continue
    fi
    echo "Hitungan: $count"
done
```
Output:
```
Hitungan: 1
Hitungan: 3
Hitungan: 4
Hitungan: 5
```
Di sini, ketika `count` mencapai 2, iterasi tersebut dilewati dan tidak mencetak angka 2.

### Contoh 3: Menggunakan continue dengan opsi n
```bash
for i in {1..10}; do
    if [ $i -lt 5 ]; then
        continue 2
    fi
    echo "Angka: $i"
done
```
Output:
```
Angka: 5
Angka: 6
Angka: 7
Angka: 8
Angka: 9
Angka: 10
```
Dalam contoh ini, ketika `i` kurang dari 5, dua iterasi berikutnya akan dilewati.

## Tips
- Gunakan `continue` untuk menghindari eksekusi kode yang tidak perlu dalam loop, sehingga membuat skrip lebih efisien.
- Pastikan untuk menggunakan `continue` dengan hati-hati, terutama dalam loop bersarang, agar tidak membingungkan alur kontrol.
- Selalu periksa kondisi yang memicu `continue` agar tidak terjadi pengulangan yang tidak diinginkan.