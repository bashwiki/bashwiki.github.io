# [Linux] Bash return penggunaan: Mengembalikan status keluar dari skrip

## Overview
Perintah `return` dalam Bash digunakan untuk mengembalikan status keluar dari fungsi atau skrip. Ini memungkinkan pengguna untuk memberikan informasi tentang keberhasilan atau kegagalan eksekusi suatu fungsi.

## Usage
Berikut adalah sintaks dasar dari perintah `return`:

```bash
return [status]
```

Di mana `[status]` adalah kode status yang ingin Anda kembalikan. Jika tidak ada status yang diberikan, `return` akan mengembalikan status keluar dari perintah terakhir yang dijalankan.

## Common Options
- `status`: Kode status yang ingin dikembalikan. Ini biasanya berupa angka antara 0 hingga 255, di mana 0 menunjukkan keberhasilan dan angka lainnya menunjukkan berbagai jenis kesalahan.

## Common Examples

### Contoh 1: Mengembalikan status sukses
```bash
my_function() {
    echo "Fungsi berhasil dijalankan."
    return 0
}
my_function
```

### Contoh 2: Mengembalikan status gagal
```bash
my_function() {
    echo "Fungsi gagal dijalankan."
    return 1
}
my_function
```

### Contoh 3: Menggunakan return dalam kondisi
```bash
check_number() {
    if [ $1 -gt 10 ]; then
        return 0
    else
        return 1
    fi
}
check_number 5
echo "Status keluar: $?"  # Menampilkan 1
check_number 15
echo "Status keluar: $?"  # Menampilkan 0
```

## Tips
- Selalu gunakan kode status yang konsisten untuk memudahkan debugging.
- Gunakan `return` dalam fungsi untuk mengontrol alur eksekusi skrip dengan lebih baik.
- Periksa status keluar dari fungsi dengan menggunakan `$?` setelah pemanggilan fungsi untuk mengetahui apakah fungsi berhasil atau tidak.