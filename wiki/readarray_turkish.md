# [Linux] Bash readarray Kullanımı: Dizi olarak satırları okuma

## Overview
`readarray` komutu, bir dosyadan veya standart girdiden satırları okuyarak bir diziye atamak için kullanılır. Bu komut, özellikle çok sayıda satır içeren verileri işlemek için oldukça kullanışlıdır.

## Usage
Temel sözdizimi şu şekildedir:

```bash
readarray [seçenekler] [argümanlar]
```

## Common Options
- `-n N`: İlk N satırı okumayı atlar.
- `-s N`: İlk N satırı atlayarak okumaya başlar.
- `-t`: Satır sonu karakterlerini kaldırır.
- `-d DELIMITER`: Satır sonu karakterini özelleştirir.

## Common Examples
Aşağıda `readarray` komutunun bazı pratik örnekleri bulunmaktadır:

### Örnek 1: Bir dosyadan satırları diziye okuma
```bash
readarray my_array < dosya.txt
```
Bu komut, `dosya.txt` dosyasındaki tüm satırları `my_array` adlı diziye okur.

### Örnek 2: Satır sonu karakterlerini kaldırma
```bash
readarray -t my_array < dosya.txt
```
Bu komut, `dosya.txt` dosyasındaki satırları `my_array` dizisine okurken satır sonu karakterlerini kaldırır.

### Örnek 3: İlk 3 satırı atlayarak okuma
```bash
readarray -s 3 my_array < dosya.txt
```
Bu komut, `dosya.txt` dosyasındaki ilk 3 satırı atlayarak geri kalan satırları `my_array` dizisine okur.

## Tips
- Dizi elemanlarına erişmek için `echo "${my_array[index]}"` şeklinde kullanabilirsiniz.
- `readarray` komutunu bir dosya yerine bir komutun çıktısını okumak için de kullanabilirsiniz. Örneğin: `readarray my_array < <(ls)`.
- Büyük dosyalarla çalışırken, bellek kullanımını göz önünde bulundurun; gerekirse satırları parça parça okuyun.