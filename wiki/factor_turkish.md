# [Linux] Bash faktör kullanımı: Sayıları asal çarpanlarına ayırma

## Overview
`factor` komutu, verilen sayıların asal çarpanlarını bulmak için kullanılır. Bu komut, bir veya daha fazla sayıyı alır ve her bir sayının asal çarpanlarını gösterir.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
factor [options] [arguments]
```

## Common Options
- `-h`, `--help`: Yardım mesajını gösterir.
- `-V`, `--version`: Versiyon bilgilerini gösterir.

## Common Examples
Aşağıda `factor` komutunun bazı pratik örnekleri bulunmaktadır:

1. Tek bir sayının asal çarpanlarını bulma:
   ```bash
   factor 28
   ```
   Çıktı:
   ```
   28: 2 2 7
   ```

2. Birden fazla sayının asal çarpanlarını bulma:
   ```bash
   factor 15 21 42
   ```
   Çıktı:
   ```
   15: 3 5
   21: 3 7
   42: 2 3 7
   ```

3. Asal çarpanları bulma için bir dosyadan sayı okuma:
   ```bash
   echo -e "10\n15\n20" > sayilar.txt
   factor $(cat sayilar.txt)
   ```
   Çıktı:
   ```
   10: 2 5
   15: 3 5
   20: 2 2 5
   ```

## Tips
- `factor` komutunu kullanırken, sayıları boşlukla ayırarak birden fazla sayı girebilirsiniz.
- Büyük sayılarla çalışırken, `factor` komutunun performansını göz önünde bulundurun; çok büyük sayılar için işlem süresi uzayabilir.
- Asal çarpanları bulmak için `factor` komutunu sık sık kullanıyorsanız, bir betik yazarak işlemlerinizi otomatikleştirebilirsiniz.