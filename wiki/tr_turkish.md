# [Linux] Bash tr Kullanımı: Karakterleri Dönüştürme

## Overview
`tr` komutu, bir dosyadaki veya standart girdi akışındaki karakterleri dönüştürmek veya silmek için kullanılır. Genellikle metin işleme görevlerinde, belirli karakterleri değiştirmek veya belirli karakterleri kaldırmak için tercih edilir.

## Usage
Temel sözdizimi şu şekildedir:
```bash
tr [options] [arguments]
```

## Common Options
- `-d`: Belirtilen karakterleri siler.
- `-s`: Ardışık aynı karakterleri birleştirir.
- `-c`: Belirtilen karakterler dışındaki tüm karakterleri işler.
- `-t`: Belirtilen karakterlerin yalnızca ilkini işler.

## Common Examples
Aşağıda `tr` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. **Karakter Dönüşümü**: Küçük harfleri büyük harflere dönüştürme.
   ```bash
   echo "merhaba dünya" | tr 'a-z' 'A-Z'
   ```

2. **Karakter Silme**: Belirli bir karakteri silme.
   ```bash
   echo "merhaba dünya" | tr -d 'a'
   ```

3. **Ardışık Karakterleri Birleştirme**: Birden fazla boşluğu tek bir boşlukla değiştirme.
   ```bash
   echo "merhaba    dünya" | tr -s ' '
   ```

4. **Karakter Değiştirme**: Belirli karakterleri başka karakterlerle değiştirme.
   ```bash
   echo "merhaba dünya" | tr 'a' 'e'
   ```

5. **Karakter Seti Tersi**: Belirtilen karakterler dışındaki tüm karakterleri dönüştürme.
   ```bash
   echo "merhaba dünya" | tr -c 'a-zA-Z' ' '
   ```

## Tips
- `tr` komutunu kullanırken, girdi akışını yönlendirmek için `echo` veya dosya isimleri kullanabilirsiniz.
- Komutları birleştirerek daha karmaşık metin işleme görevleri gerçekleştirebilirsiniz.
- `tr` komutunun büyük-küçük harf duyarlı olduğunu unutmayın; bu nedenle dönüşüm yaparken dikkatli olun.