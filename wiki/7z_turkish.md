# [Linux] Bash 7z Kullanımı: Dosyaları sıkıştırma ve açma aracı

## Genel Bakış
7z, dosyaları sıkıştırmak ve açmak için kullanılan güçlü bir komut satırı aracıdır. 7z formatı, yüksek sıkıştırma oranları sunarak dosyaların boyutunu önemli ölçüde azaltabilir. Bu araç, hem sıkıştırma hem de açma işlemleri için geniş bir dosya formatı desteği sunar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```
7z [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `a`: Yeni bir arşiv oluşturur ve dosyaları ekler.
- `x`: Arşivden dosyaları çıkarır.
- `l`: Arşiv içeriğini listeler.
- `d`: Arşivden dosyaları siler.
- `t`: Arşivin bütünlüğünü kontrol eder.
- `e`: Arşivden dosyaları çıkarır, ancak dizin yapısını korumaz.

## Yaygın Örnekler
1. **Yeni bir arşiv oluşturma:**
   ```bash
   7z a arşiv.7z dosya1.txt dosya2.txt
   ```

2. **Arşivden dosyaları çıkarma:**
   ```bash
   7z x arşiv.7z
   ```

3. **Arşiv içeriğini listeleme:**
   ```bash
   7z l arşiv.7z
   ```

4. **Arşivden belirli bir dosyayı silme:**
   ```bash
   7z d arşiv.7z dosya1.txt
   ```

5. **Arşivin bütünlüğünü kontrol etme:**
   ```bash
   7z t arşiv.7z
   ```

## İpuçları
- Sıkıştırma oranını artırmak için `-mx=9` seçeneğini kullanabilirsiniz. Örneğin:
  ```bash
  7z a -mx=9 arşiv.7z dosya.txt
  ```
- Büyük dosyalarla çalışırken, işlemlerinizi daha hızlı hale getirmek için çoklu iş parçacığı desteğini kullanabilirsiniz.
- Arşivlerinizi düzenli olarak kontrol edin ve gereksiz dosyaları silerek alan tasarrufu yapın.