# [Linux] Bash watch Penggunaan: Memantau perintah secara berkala

## Overview
Perintah `watch` digunakan untuk menjalankan perintah tertentu secara berkala dan menampilkan hasilnya di terminal. Ini sangat berguna untuk memantau perubahan dalam output perintah, seperti status sistem atau file.

## Usage
Sintaks dasar dari perintah `watch` adalah sebagai berikut:

```bash
watch [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan perintah `watch`:

- `-n <seconds>`: Menentukan interval waktu (dalam detik) antara eksekusi perintah.
- `-d`: Menyoroti perbedaan antara output sebelumnya dan output saat ini.
- `-t`: Menghilangkan tampilan header dari output.
- `-x`: Menjalankan perintah dalam mode eksekusi penuh.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan perintah `watch`:

1. Memantau penggunaan CPU setiap 2 detik:
    ```bash
    watch -n 2 mpstat
    ```

2. Memantau perubahan pada direktori dengan `ls`:
    ```bash
    watch ls -l
    ```

3. Memantau penggunaan disk dengan `df`:
    ```bash
    watch -d df -h
    ```

4. Memantau proses tertentu, misalnya `top`, setiap 5 detik:
    ```bash
    watch -n 5 top
    ```

## Tips
- Gunakan opsi `-d` untuk lebih mudah melihat perubahan yang terjadi dalam output.
- Sesuaikan interval waktu dengan kebutuhan Anda agar tidak terlalu sering memanggil perintah yang berat.
- Jika Anda ingin menghentikan perintah `watch`, cukup tekan `Ctrl + C`.