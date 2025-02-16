# [Linux] Bash source Penggunaan: Menjalankan skrip dalam konteks saat ini

## Overview
Perintah `source` dalam Bash digunakan untuk mengeksekusi skrip shell dalam konteks shell saat ini. Ini memungkinkan variabel dan fungsi yang didefinisikan dalam skrip untuk tersedia setelah skrip selesai dijalankan, berbeda dengan menjalankan skrip secara langsung yang akan membuat subshell baru.

## Usage
Berikut adalah sintaks dasar dari perintah `source`:

```bash
source [options] [arguments]
```

## Common Options
- `-h`, `--help`: Menampilkan bantuan tentang penggunaan perintah `source`.
- `-V`, `--version`: Menampilkan versi dari shell yang digunakan.

## Common Examples

### Menjalankan Skrip
Untuk menjalankan skrip bernama `myscript.sh`, Anda dapat menggunakan perintah berikut:

```bash
source myscript.sh
```

### Menggunakan Sumber dari File Konfigurasi
Anda dapat menggunakan `source` untuk memuat file konfigurasi, seperti `.bashrc`, untuk memperbarui pengaturan shell Anda tanpa perlu membuka sesi baru:

```bash
source ~/.bashrc
```

### Menjalankan Skrip dengan Parameter
Jika skrip Anda menerima parameter, Anda dapat menggunakan `source` dengan variabel yang ditetapkan sebelumnya:

```bash
VAR="Hello"
source myscript.sh
```

### Menggunakan Sumber dengan Path Lengkap
Jika skrip berada di direktori lain, Anda dapat memberikan path lengkapnya:

```bash
source /path/to/myscript.sh
```

## Tips
- Selalu pastikan skrip yang akan dijalankan dengan `source` memiliki izin eksekusi yang tepat.
- Gunakan `source` untuk memuat ulang file konfigurasi setelah melakukan perubahan, agar perubahan tersebut langsung diterapkan.
- Jika Anda ingin menjalankan skrip tanpa mempengaruhi lingkungan saat ini, pertimbangkan untuk menggunakan `bash myscript.sh` sebagai alternatif.