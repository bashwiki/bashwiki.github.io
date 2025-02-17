# [Linux] Bash diff Kullanımı: İki dosya arasındaki farkları gösterir

## Genel Bakış
`diff` komutu, iki dosya arasındaki farklılıkları karşılaştırmak ve bu farklılıkları göstermek için kullanılır. Özellikle metin dosyalarında yapılan değişiklikleri tespit etmek için oldukça faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
diff [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-u`: Birleştirilmiş formatta çıktı verir.
- `-c`: Bağlam formatında çıktı verir.
- `-i`: Büyük/küçük harf duyarsız karşılaştırma yapar.
- `-w`: Boşlukları göz ardı eder.
- `-r`: Dizindeki alt dizinleri de karşılaştırır.

## Yaygın Örnekler
1. İki dosya arasındaki farkları görmek için:
   ```bash
   diff dosya1.txt dosya2.txt
   ```

2. Birleştirilmiş formatta çıktı almak için:
   ```bash
   diff -u dosya1.txt dosya2.txt
   ```

3. Boşlukları göz ardı ederek karşılaştırma yapmak için:
   ```bash
   diff -w dosya1.txt dosya2.txt
   ```

4. Bir dizindeki tüm dosyaları karşılaştırmak için:
   ```bash
   diff -r dizin1/ dizin2/
   ```

## İpuçları
- Değişiklikleri daha iyi anlamak için `-u` seçeneğini kullanarak birleştirilmiş formatta çıktı almayı tercih edin.
- Farklılıkları daha kolay görmek için `diff` çıktısını bir dosyaya yönlendirebilirsiniz:
  ```bash
  diff dosya1.txt dosya2.txt > farklar.txt
  ```
- `diff` çıktısını `patch` komutuyla birleştirerek dosyalar üzerinde değişiklik yapabilirsiniz.