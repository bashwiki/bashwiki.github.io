# [Linux] Bash svn Penggunaan: Mengelola versi file

## Overview
Perintah `svn` (Subversion) digunakan untuk mengelola versi dari file dan direktori. Ini memungkinkan pengguna untuk melacak perubahan, mengelola revisi, dan berkolaborasi dalam proyek pengembangan perangkat lunak.

## Usage
Berikut adalah sintaks dasar dari perintah `svn`:

```bash
svn [options] [arguments]
```

## Common Options
- `checkout`: Mengunduh salinan kerja dari repositori.
- `commit`: Mengirimkan perubahan lokal ke repositori.
- `update`: Memperbarui salinan kerja dengan perubahan terbaru dari repositori.
- `add`: Menambahkan file baru ke dalam repositori.
- `delete`: Menghapus file dari repositori.
- `status`: Menampilkan status file dalam salinan kerja.

## Common Examples
Berikut adalah beberapa contoh penggunaan perintah `svn`:

1. **Mengunduh salinan kerja dari repositori:**
   ```bash
   svn checkout https://example.com/svn/repo
   ```

2. **Mengirimkan perubahan ke repositori:**
   ```bash
   svn commit -m "Menambahkan fitur baru"
   ```

3. **Memperbarui salinan kerja:**
   ```bash
   svn update
   ```

4. **Menambahkan file baru:**
   ```bash
   svn add file_baru.txt
   ```

5. **Menghapus file dari repositori:**
   ```bash
   svn delete file_hapus.txt
   ```

6. **Menampilkan status file:**
   ```bash
   svn status
   ```

## Tips
- Selalu lakukan `svn update` sebelum melakukan `commit` untuk menghindari konflik.
- Gunakan pesan yang jelas dan deskriptif saat melakukan `commit` untuk memudahkan pelacakan perubahan.
- Pertimbangkan untuk menggunakan `svn log` untuk melihat riwayat perubahan dan revisi sebelumnya.