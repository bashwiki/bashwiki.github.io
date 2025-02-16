# [Linux] Bash readonly Penggunaan: Menetapkan Variabel Hanya Baca

## Overview
Perintah `readonly` dalam Bash digunakan untuk menetapkan variabel sebagai hanya baca. Setelah sebuah variabel ditetapkan sebagai readonly, nilainya tidak dapat diubah atau dihapus selama sesi shell tersebut. Ini berguna untuk menjaga integritas data yang tidak boleh diubah.

## Usage
Berikut adalah sintaks dasar dari perintah `readonly`:

```bash
readonly [options] [arguments]
```

## Common Options
- `-p`: Menampilkan semua variabel readonly yang ada beserta nilainya.

## Common Examples

### Menetapkan Variabel Sebagai Readonly
Untuk menetapkan variabel sebagai readonly, gunakan perintah berikut:

```bash
readonly NAMA="John Doe"
```

Setelah perintah ini, Anda tidak dapat mengubah nilai `NAMA`.

### Menampilkan Variabel Readonly
Untuk melihat semua variabel yang telah ditetapkan sebagai readonly, gunakan opsi `-p`:

```bash
readonly -p
```

### Mencoba Mengubah Variabel Readonly
Jika Anda mencoba mengubah nilai dari variabel readonly, Anda akan mendapatkan pesan kesalahan:

```bash
NAMA="Jane Doe"  # Ini akan menghasilkan kesalahan
```

## Tips
- Gunakan `readonly` untuk variabel yang berisi konfigurasi penting yang tidak boleh diubah selama eksekusi skrip.
- Selalu periksa variabel readonly dengan `readonly -p` sebelum melakukan perubahan untuk menghindari kesalahan.
- Pertimbangkan untuk menggunakan variabel readonly dalam skrip yang dibagikan untuk menjaga konsistensi dan mencegah perubahan yang tidak disengaja.