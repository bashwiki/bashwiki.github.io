# [Linux] Bash fgrep Kullanımı: Belirli bir metni içeren dosya satırlarını bulma

## Genel Bakış
`fgrep`, belirli bir metni içeren dosya satırlarını aramak için kullanılan bir komuttur. `grep` komutunun bir varyasyonu olan `fgrep`, yalnızca tam eşleşmeler arar ve düzenli ifadeleri desteklemez. Bu, metin aramalarını daha hızlı hale getirir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```
fgrep [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-i`: Büyük/küçük harf duyarsız arama yapar.
- `-v`: Eşleşmeyen satırları gösterir.
- `-c`: Eşleşen satırların sayısını gösterir.
- `-n`: Eşleşen satırların numaralarını gösterir.
- `-r`: Alt dizinlerdeki dosyaları da arar.

## Yaygın Örnekler
Aşağıda `fgrep` komutunun bazı pratik kullanımları bulunmaktadır:

1. Belirli bir kelimeyi içeren satırları bulma:
   ```bash
   fgrep "örnek" dosya.txt
   ```

2. Büyük/küçük harf duyarsız arama yapma:
   ```bash
   fgrep -i "örnek" dosya.txt
   ```

3. Eşleşmeyen satırları gösterme:
   ```bash
   fgrep -v "örnek" dosya.txt
   ```

4. Eşleşen satırların sayısını gösterme:
   ```bash
   fgrep -c "örnek" dosya.txt
   ```

5. Alt dizinlerdeki dosyaları arama:
   ```bash
   fgrep -r "örnek" /path/to/dizin
   ```

## İpuçları
- `fgrep` kullanırken, aradığınız metni tırnak içinde belirtmek, boşluk veya özel karakter içeren metinler için önemlidir.
- Performansı artırmak için, `fgrep` ile büyük dosyalarda arama yaparken, arama yapacağınız dosyaların sayısını sınırlamak iyi bir uygulamadır.
- `fgrep` komutunu sık sık kullananlar için, sık kullanılan arama terimlerini bir dosyada saklamak ve bu dosyayı komut satırında kullanmak pratik olabilir.