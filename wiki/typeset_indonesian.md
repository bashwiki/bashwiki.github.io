# [Linux] Bash typeset penggunaan: Mengatur variabel dan atribut

## Overview
Perintah `typeset` dalam Bash digunakan untuk mendeklarasikan variabel dan mengatur atributnya. Ini memungkinkan pengguna untuk mengontrol sifat variabel, seperti apakah variabel bersifat lokal, readonly, atau array.

## Usage
Sintaks dasar dari perintah `typeset` adalah sebagai berikut:

```bash
typeset [options] [arguments]
```

## Common Options
Berikut adalah beberapa opsi umum yang dapat digunakan dengan `typeset`:

- `-a`: Menetapkan variabel sebagai array.
- `-i`: Menetapkan variabel sebagai integer, yang memungkinkan perhitungan aritmatika.
- `-r`: Menetapkan variabel sebagai readonly, sehingga tidak dapat diubah setelah ditetapkan.
- `-x`: Menetapkan variabel sebagai variabel lingkungan yang dapat diakses oleh proses anak.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `typeset`:

### Menetapkan Variabel sebagai Array
```bash
typeset -a my_array
my_array=(apple banana cherry)
echo ${my_array[1]}  # Output: banana
```

### Menetapkan Variabel sebagai Integer
```bash
typeset -i my_number
my_number=5
my_number+=10
echo $my_number  # Output: 15
```

### Menetapkan Variabel sebagai Readonly
```bash
typeset -r my_constant=100
echo $my_constant  # Output: 100
# my_constant=200  # Ini akan menghasilkan error
```

### Menetapkan Variabel sebagai Variabel Lingkungan
```bash
typeset -x my_env_var="Hello World"
echo $my_env_var  # Output: Hello World
```

## Tips
- Gunakan `typeset` untuk mendeklarasikan variabel di dalam fungsi agar variabel tersebut bersifat lokal.
- Pertimbangkan untuk menggunakan opsi `-r` untuk variabel yang tidak seharusnya diubah setelah ditetapkan, membantu mencegah kesalahan.
- Untuk array, pastikan untuk menggunakan sintaks yang benar saat mengakses elemen, seperti `${my_array[index]}`.