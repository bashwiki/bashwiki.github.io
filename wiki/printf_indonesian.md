# [Linux] Bash printf Penggunaan: Menampilkan Format Teks

## Overview
Perintah `printf` dalam Bash digunakan untuk mencetak teks dengan format yang ditentukan. Ini memungkinkan pengguna untuk mengontrol bagaimana output ditampilkan, termasuk pengaturan lebar, presisi, dan jenis data yang ditampilkan.

## Usage
Berikut adalah sintaks dasar dari perintah `printf`:

```bash
printf [options] [arguments]
```

## Common Options
- `-v`: Menyimpan hasil format ke dalam variabel.
- `-f`: Menentukan format output.
- `-n`: Menghilangkan karakter newline di akhir output.

## Common Examples

1. **Mencetak Teks Sederhana**
   ```bash
   printf "Hello, World!\n"
   ```

2. **Menggunakan Format untuk Angka**
   ```bash
   printf "Nilai: %.2f\n" 3.14159
   ```

3. **Mencetak Beberapa Nilai**
   ```bash
   printf "Nama: %s, Umur: %d\n" "Alice" 30
   ```

4. **Mengatur Lebar Kolom**
   ```bash
   printf "|%-10s|%10s|\n" "Nama" "Umur"
   printf "|%-10s|%10d|\n" "Bob" 25
   ```

5. **Menyimpan Hasil ke Variabel**
   ```bash
   printf -v myVar "Hasil: %.1f" 9.876
   echo $myVar
   ```

## Tips
- Gunakan `\n` untuk menambahkan baris baru dalam output.
- Manfaatkan format spesifier seperti `%s` untuk string, `%d` untuk integer, dan `%f` untuk floating-point.
- Selalu periksa hasil output untuk memastikan format yang diinginkan tercapai, terutama saat bekerja dengan angka desimal.