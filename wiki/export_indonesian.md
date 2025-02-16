# [Linux] Bash export Penggunaan: Mengatur Variabel Lingkungan

## Overview
Perintah `export` dalam Bash digunakan untuk mengatur variabel lingkungan yang dapat diakses oleh proses anak. Dengan menggunakan `export`, Anda dapat membuat variabel yang didefinisikan dalam shell saat ini tersedia untuk program atau skrip yang dijalankan dari shell tersebut.

## Usage
Berikut adalah sintaks dasar dari perintah `export`:

```bash
export [options] [arguments]
```

## Common Options
- `-p`: Menampilkan semua variabel lingkungan yang diekspor saat ini.
- `-n`: Menghapus ekspor variabel, sehingga variabel tersebut tidak lagi tersedia untuk proses anak.
- `-f`: Mengekspor fungsi shell, bukan hanya variabel.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `export`:

1. **Menetapkan dan Mengekspor Variabel Lingkungan:**
   ```bash
   MY_VAR="Hello, World!"
   export MY_VAR
   ```

2. **Menampilkan Variabel Lingkungan yang Diekspor:**
   ```bash
   export -p
   ```

3. **Menghapus Ekspor Variabel:**
   ```bash
   export -n MY_VAR
   ```

4. **Mengekspor Fungsi Shell:**
   ```bash
   my_function() {
       echo "This is a function"
   }
   export -f my_function
   ```

5. **Menetapkan dan Mengekspor Variabel dalam Satu Baris:**
   ```bash
   export MY_VAR="Hello, World!"
   ```

## Tips
- Selalu gunakan `export` setelah mendefinisikan variabel jika Anda ingin variabel tersebut tersedia untuk proses anak.
- Gunakan `export -p` untuk memeriksa variabel lingkungan yang telah diekspor sebelum menjalankan skrip atau program.
- Hati-hati saat menggunakan `export -n`, karena ini akan menghapus variabel dari lingkungan anak dan dapat menyebabkan kesalahan jika variabel tersebut dibutuhkan.