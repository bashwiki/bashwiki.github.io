# [Linux] Bash declare Penggunaan: Mendeklarasikan variabel dan atribut

## Overview
Perintah `declare` dalam Bash digunakan untuk mendeklarasikan variabel dan menetapkan atribut tertentu pada variabel tersebut. Ini memungkinkan pengguna untuk mengontrol jenis data dan perilaku variabel dalam skrip Bash.

## Usage
Berikut adalah sintaks dasar dari perintah `declare`:

```bash
declare [options] [arguments]
```

## Common Options
- `-a`: Mendeklarasikan variabel sebagai array.
- `-i`: Mendeklarasikan variabel sebagai integer, yang memungkinkan operasi aritmatika.
- `-r`: Menetapkan variabel sebagai read-only, sehingga nilainya tidak dapat diubah.
- `-x`: Menetapkan variabel sebagai variabel lingkungan yang dapat diakses oleh proses anak.

## Common Examples

### Mendeklarasikan Variabel Biasa
```bash
declare myVar="Hello, World!"
echo $myVar
```

### Mendeklarasikan Array
```bash
declare -a myArray=("Apple" "Banana" "Cherry")
echo ${myArray[1]}  # Output: Banana
```

### Mendeklarasikan Integer
```bash
declare -i myInt=5
myInt+=10
echo $myInt  # Output: 15
```

### Menetapkan Variabel Read-Only
```bash
declare -r myConst="This is a constant"
echo $myConst
# myConst="New Value"  # Ini akan menghasilkan error
```

### Mendeklarasikan Variabel Lingkungan
```bash
declare -x myEnvVar="Environment Variable"
echo $myEnvVar
```

## Tips
- Gunakan `declare -p` untuk menampilkan informasi tentang variabel yang telah dideklarasikan.
- Selalu gunakan opsi `-r` untuk variabel yang tidak boleh diubah setelah ditetapkan, untuk menghindari kesalahan.
- Saat menggunakan array, pastikan untuk menggunakan tanda kurung untuk mendeklarasikan elemen dengan benar.