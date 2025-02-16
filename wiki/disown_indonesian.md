# [Linux] Bash disown: Menghapus proses dari daftar pekerjaan

## Overview
Perintah `disown` dalam Bash digunakan untuk menghapus proses dari daftar pekerjaan yang sedang berjalan di shell. Dengan menggunakan perintah ini, proses yang telah dijalankan di latar belakang tidak akan terpengaruh oleh penutupan terminal, sehingga tetap berjalan meskipun sesi shell berakhir.

## Usage
Berikut adalah sintaks dasar dari perintah `disown`:

```bash
disown [options] [arguments]
```

## Common Options
- `-h`: Menandai pekerjaan agar tidak menerima sinyal HUP (hangup) ketika shell ditutup.
- `-a`: Menghapus semua pekerjaan yang ada dari daftar pekerjaan.
- `-r`: Menghapus pekerjaan yang sedang berjalan saja dari daftar pekerjaan.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `disown`:

1. **Menghapus pekerjaan tertentu dari daftar:**
   ```bash
   disown %1
   ```
   Perintah ini akan menghapus pekerjaan dengan nomor 1 dari daftar pekerjaan.

2. **Menghapus semua pekerjaan dari daftar:**
   ```bash
   disown -a
   ```
   Dengan perintah ini, semua pekerjaan yang sedang berjalan akan dihapus dari daftar.

3. **Menandai pekerjaan agar tidak menerima sinyal HUP:**
   ```bash
   disown -h %2
   ```
   Perintah ini akan menandai pekerjaan dengan nomor 2 agar tetap berjalan meskipun shell ditutup.

## Tips
- Selalu periksa daftar pekerjaan Anda dengan perintah `jobs` sebelum menggunakan `disown` untuk memastikan Anda menghapus pekerjaan yang benar.
- Gunakan `disown` setelah menjalankan proses di latar belakang dengan `&` untuk menjaga agar proses tetap berjalan setelah terminal ditutup.
- Jika Anda ingin memantau proses yang telah di-disown, pertimbangkan untuk menggunakan perintah `ps` untuk melihat status proses tersebut.