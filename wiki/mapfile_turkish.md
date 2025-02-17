# [Linux] Bash mapfile Kullanımı: Diziye dosya içeriğini okuma

## Overview
`mapfile` komutu, bir dosyanın içeriğini bir diziye okumanıza olanak tanır. Bu komut, dosya satırlarını bir dizi elemanı olarak depolamak için kullanılır ve genellikle dosya içeriği üzerinde işlem yaparken oldukça faydalıdır.

## Usage
Temel sözdizimi şu şekildedir:

```bash
mapfile [options] [arguments]
```

## Common Options
- `-t`: Satır sonu karakterlerini kaldırır.
- `-n <number>`: Okunacak satır sayısını belirtir.
- `-O <number>`: Diziye eklemeye başlayacağınız indeksi belirtir.
- `-s <number>`: Atlanacak satır sayısını belirtir.

## Common Examples

### Örnek 1: Basit Kullanım
Bir dosyanın içeriğini bir diziye okumak için:

```bash
mapfile my_array < my_file.txt
```

### Örnek 2: Satır Sonu Karakterlerini Kaldırma
Satır sonu karakterlerini kaldırarak bir diziye okuma:

```bash
mapfile -t my_array < my_file.txt
```

### Örnek 3: Belirli Sayıda Satır Okuma
Sadece ilk 5 satırı okumak için:

```bash
mapfile -n 5 my_array < my_file.txt
```

### Örnek 4: Dizi İndeksini Belirleme
Dizinin 10. indeksinden başlamasını sağlamak:

```bash
mapfile -O 10 my_array < my_file.txt
```

### Örnek 5: Satır Atlama
İlk 3 satırı atlayarak okumak:

```bash
mapfile -s 3 my_array < my_file.txt
```

## Tips
- `mapfile` komutunu kullanmadan önce dosyanın var olduğundan emin olun.
- Dizi elemanlarına erişmek için dizinin indeks numarasını kullanabilirsiniz, örneğin: `${my_array[0]}`.
- Büyük dosyalarla çalışırken, bellek kullanımını göz önünde bulundurun; çok büyük dosyalar belleği doldurabilir.