# [Linux] Bash break Penggunaan: Menghentikan loop

## Overview
Perintah `break` dalam Bash digunakan untuk menghentikan eksekusi dari loop, baik itu loop `for`, `while`, atau `until`. Ketika `break` dipanggil, kontrol program akan keluar dari loop yang sedang berjalan dan melanjutkan eksekusi pada pernyataan setelah loop tersebut.

## Usage
Berikut adalah sintaks dasar dari perintah `break`:

```
break [n]
```

Di mana `n` adalah jumlah level loop yang ingin dihentikan. Jika `n` tidak ditentukan, maka `break` akan menghentikan loop terdekat.

## Common Options
- `n`: Menentukan jumlah level loop yang ingin dihentikan. Jika tidak ada nilai yang diberikan, `break` akan menghentikan loop terdekat.

## Common Examples

### Contoh 1: Menghentikan loop for
```bash
for i in {1..5}; do
  if [ $i -eq 3 ]; then
    break
  fi
  echo "Nomor: $i"
done
```
Output:
```
Nomor: 1
Nomor: 2
```

### Contoh 2: Menghentikan loop while
```bash
count=1
while [ $count -le 5 ]; do
  if [ $count -eq 4 ]; then
    break
  fi
  echo "Hitung: $count"
  ((count++))
done
```
Output:
```
Hitung: 1
Hitung: 2
Hitung: 3
```

### Contoh 3: Menghentikan loop nested
```bash
for i in {1..3}; do
  for j in {1..3}; do
    if [ $j -eq 2 ]; then
      break 2
    fi
    echo "i: $i, j: $j"
  done
done
```
Output:
```
i: 1, j: 1
```

## Tips
- Gunakan `break` dengan hati-hati dalam loop bersarang, karena dapat menghentikan lebih dari satu level loop jika tidak ditentukan.
- Pastikan untuk menggunakan `break` dalam konteks yang tepat agar tidak menghentikan loop yang tidak diinginkan.
- Pertimbangkan untuk menggunakan `continue` jika Anda hanya ingin melewati iterasi tertentu dalam loop tanpa menghentikannya.