# [Linux] Bash bc Penggunaan: Alat kalkulasi aritmatika

## Overview
Perintah `bc` adalah kalkulator aritmatika yang digunakan di lingkungan Bash. Ia memungkinkan pengguna untuk melakukan perhitungan matematika yang kompleks dengan dukungan untuk bilangan pecahan dan operasi aritmatika dasar.

## Usage
Berikut adalah sintaks dasar dari perintah `bc`:

```bash
bc [options] [arguments]
```

## Common Options
- `-l`: Menggunakan pustaka matematika standar, yang menyediakan fungsi trigonometri dan logaritma.
- `-q`: Menjalankan `bc` dalam mode diam, yang tidak menampilkan pesan sambutan.
- `-w`: Mengaktifkan mode peringatan untuk memperingatkan pengguna tentang kesalahan dalam ekspresi.

## Common Examples
Berikut adalah beberapa contoh penggunaan `bc`:

1. **Perhitungan sederhana:**
   ```bash
   echo "5 + 3" | bc
   ```
   Output: `8`

2. **Perhitungan dengan desimal:**
   ```bash
   echo "scale=2; 10 / 3" | bc
   ```
   Output: `3.33`

3. **Menggunakan pustaka matematika:**
   ```bash
   echo "scale=4; s(1)" | bc -l
   ```
   Output: `0.8415`

4. **Menghitung pangkat:**
   ```bash
   echo "2^3" | bc
   ```
   Output: `8`

5. **Menghitung akar kuadrat:**
   ```bash
   echo "scale=4; sqrt(16)" | bc
   ```
   Output: `4.0000`

## Tips
- Selalu tentukan `scale` jika Anda ingin hasil dengan presisi desimal.
- Gunakan `-l` untuk akses fungsi matematika yang lebih kompleks.
- Simpan perhitungan dalam file dan jalankan `bc` dengan file tersebut untuk perhitungan yang lebih rumit. Contoh:
  ```bash
  bc < file_perhitungan.txt
  ```