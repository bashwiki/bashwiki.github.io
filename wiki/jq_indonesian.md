# [Linux] Bash jq Penggunaan: Memproses JSON dengan mudah

## Overview
`jq` adalah alat baris perintah yang digunakan untuk memproses dan menganalisis data dalam format JSON. Dengan `jq`, pengguna dapat mengekstrak, memfilter, dan mengubah data JSON dengan cara yang sederhana dan efisien.

## Usage
Sintaks dasar dari perintah `jq` adalah sebagai berikut:

```bash
jq [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang sering digunakan dengan `jq`:

- `-c`: Menghasilkan output dalam format kompak.
- `-r`: Menghasilkan output dalam format mentah (tanpa tanda kutip).
- `-f <file>`: Menggunakan file yang berisi skrip jq.
- `--arg <name> <value>`: Mengatur variabel jq dengan nama dan nilai yang diberikan.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `jq`:

1. **Menampilkan seluruh konten JSON**:
   ```bash
   cat data.json | jq .
   ```

2. **Mengambil nilai dari kunci tertentu**:
   ```bash
   cat data.json | jq '.nama'
   ```

3. **Memfilter data berdasarkan kondisi**:
   ```bash
   cat data.json | jq '.[] | select(.umur > 30)'
   ```

4. **Mengubah format output**:
   ```bash
   cat data.json | jq -r '.[] | "\(.nama) - \(.umur)"'
   ```

5. **Menggunakan variabel**:
   ```bash
   cat data.json | jq --arg nama "John" '.[] | select(.nama == $nama)'
   ```

## Tips
- Selalu gunakan opsi `-c` jika Anda ingin output yang lebih ringkas, terutama saat bekerja dengan data besar.
- Manfaatkan opsi `-r` untuk mendapatkan output yang lebih bersih saat Anda hanya membutuhkan nilai.
- Simpan skrip jq yang kompleks dalam file dan gunakan opsi `-f` untuk memudahkan penggunaan kembali.