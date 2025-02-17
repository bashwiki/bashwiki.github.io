# [Linux] Bash find Kullanımı: Dosya isimlerini bulma

## Genel Bakış
`find` komutu, belirli bir dizin içinde dosya ve dizinleri aramak için kullanılır. Kullanıcıların dosya isimlerini, türlerini, boyutlarını ve diğer özelliklerini belirleyerek arama yapmalarına olanak tanır.

## Kullanım
Temel sözdizimi şu şekildedir:
```
find [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-name`: Belirtilen isimle eşleşen dosyaları bulur.
- `-type`: Belirtilen türdeki dosyaları arar (örneğin, `f` dosya, `d` dizin).
- `-size`: Belirli bir boyutta dosyaları bulur.
- `-mtime`: Belirtilen gün sayısı içinde değiştirilmiş dosyaları bulur.
- `-exec`: Bulunan dosyalar üzerinde belirtilen komutu çalıştırır.

## Yaygın Örnekler
Aşağıda `find` komutunun bazı pratik örnekleri bulunmaktadır:

1. Belirli bir dizinde belirli bir isimle dosyaları bulma:
   ```bash
   find /path/to/directory -name "dosya.txt"
   ```

2. Sadece dizinleri bulma:
   ```bash
   find /path/to/directory -type d
   ```

3. 1 MB'den büyük dosyaları bulma:
   ```bash
   find /path/to/directory -size +1M
   ```

4. Son 7 gün içinde değiştirilmiş dosyaları bulma:
   ```bash
   find /path/to/directory -mtime -7
   ```

5. Bulunan dosyalar üzerinde bir komut çalıştırma (örneğin, silme):
   ```bash
   find /path/to/directory -name "*.tmp" -exec rm {} \;
   ```

## İpuçları
- `find` komutunu kullanırken, arama yapacağınız dizini doğru belirlediğinizden emin olun.
- Arama sonuçlarını daha iyi yönetmek için `-print` seçeneğini kullanabilirsiniz.
- `find` komutunu `-exec` ile kullanırken, `{}` ifadesinin bulunduğunuz dosya adını temsil ettiğini unutmayın.
- Uzun arama işlemlerinde, sonuçları bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz.