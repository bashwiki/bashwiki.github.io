# [Linux] Bash local: Mendefinisikan variabel lokal dalam fungsi

## Overview
Perintah `local` digunakan dalam Bash untuk mendefinisikan variabel lokal di dalam fungsi. Variabel yang didefinisikan dengan `local` hanya dapat diakses dalam fungsi tempat mereka dideklarasikan, sehingga membantu menghindari konflik dengan variabel global.

## Usage
Berikut adalah sintaks dasar dari perintah `local`:

```bash
local [options] variable_name=value
```

## Common Options
Perintah `local` tidak memiliki banyak opsi, tetapi berikut adalah beberapa hal yang perlu diperhatikan:
- Tidak ada opsi khusus yang perlu ditambahkan saat menggunakan `local`, karena fungsinya hanya untuk mendeklarasikan variabel lokal.

## Common Examples
Berikut adalah beberapa contoh praktis penggunaan `local`:

### Contoh 1: Mendefinisikan variabel lokal
```bash
function contoh_fungsi {
    local variabel_lokal="Ini lokal"
    echo $variabel_lokal
}

contoh_fungsi  # Output: Ini lokal
echo $variabel_lokal  # Tidak ada output, karena variabel_lokal tidak dapat diakses di luar fungsi
```

### Contoh 2: Menggunakan variabel lokal dalam perhitungan
```bash
function hitung {
    local angka1=10
    local angka2=5
    local hasil=$((angka1 + angka2))
    echo "Hasil: $hasil"
}

hitung  # Output: Hasil: 15
```

### Contoh 3: Menghindari konflik variabel
```bash
variabel_global="Ini global"

function contoh_konflik {
    local variabel_global="Ini lokal"
    echo $variabel_global
}

contoh_konflik  # Output: Ini lokal
echo $variabel_global  # Output: Ini global
```

## Tips
- Selalu gunakan `local` saat mendeklarasikan variabel di dalam fungsi untuk menjaga ruang lingkup variabel.
- Ini membantu mencegah kesalahan yang disebabkan oleh variabel global yang tidak sengaja terubah.
- Gunakan nama variabel yang jelas dan deskriptif untuk meningkatkan keterbacaan kode Anda.