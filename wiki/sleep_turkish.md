# [Linux] Bash sleep Kullanımı: Komutları belirli bir süre bekletir

## Overview
`sleep` komutu, bir Bash betiğinde veya terminalde belirli bir süre boyunca beklemek için kullanılır. Bu komut, genellikle diğer komutların çalıştırılmasından önce bir gecikme eklemek amacıyla kullanılır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```
sleep [options] [arguments]
```

## Common Options
- `-s`, `--seconds`: Bekleme süresini saniye cinsinden belirtir. Bu seçenek varsayılan olarak kullanılır.
- `-m`, `--minutes`: Bekleme süresini dakika cinsinden belirtir.
- `-h`, `--hours`: Bekleme süresini saat cinsinden belirtir.
- `-d`, `--days`: Bekleme süresini gün cinsinden belirtir.

## Common Examples
Aşağıda `sleep` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. 5 saniye beklemek için:
   ```bash
   sleep 5
   ```

2. 2 dakika beklemek için:
   ```bash
   sleep 2m
   ```

3. 1 saat beklemek için:
   ```bash
   sleep 1h
   ```

4. 3 gün beklemek için:
   ```bash
   sleep 3d
   ```

5. Bir komutun çalıştırılmasından önce 10 saniye beklemek için:
   ```bash
   sleep 10 && echo "10 saniye geçti!"
   ```

## Tips
- `sleep` komutunu bir betikte kullanırken, bekleme sürelerini dikkatlice ayarlamak, betiğin performansını artırabilir.
- Uzun bekleme süreleri kullanırken, betiğin akışını kaybetmemek için ara vermek faydalı olabilir.
- `sleep` komutunu, zamanlama gerektiren görevlerde veya otomatikleştirilmiş işlemlerde kullanarak, belirli bir sırayı koruyabilirsiniz.