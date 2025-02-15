# [리눅스] Bash diff 사용법

## Overview
`diff` komutu, iki dosya arasındaki farklılıkları karşılaştırmak için kullanılan bir araçtır. Genellikle metin dosyaları için kullanılır ve bu dosyalar arasındaki satır düzeyindeki değişiklikleri, eklemeleri ve silmeleri gösterir. Yazılım geliştirme süreçlerinde, kod değişikliklerini izlemek ve sürüm kontrol sistemleri ile entegrasyon sağlamak için yaygın olarak kullanılır.

## Usage
`diff` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
diff [seçenekler] dosya1 dosya2
```

### Yaygın Seçenekler
- `-u`: Unified format (birleştirilmiş format) ile çıktı verir, bu da değişikliklerin daha okunabilir bir şekilde gösterilmesini sağlar.
- `-c`: Context format (bağlam formatı) ile çıktı verir, bu da değişikliklerin etrafındaki satırları gösterir.
- `-i`: Büyük/küçük harf duyarsız karşılaştırma yapar.
- `-w`: Boşlukları göz ardı eder, yani sadece anlamlı değişiklikleri gösterir.

## Examples
### Örnek 1: Temel Kullanım
İki metin dosyasını karşılaştırmak için aşağıdaki komutu kullanabilirsiniz:

```bash
diff dosya1.txt dosya2.txt
```

Bu komut, `dosya1.txt` ve `dosya2.txt` dosyaları arasındaki farklılıkları satır bazında gösterecektir.

### Örnek 2: Unified Format Kullanımı
Daha okunabilir bir çıktı almak için `-u` seçeneğini kullanabilirsiniz:

```bash
diff -u dosya1.txt dosya2.txt
```

Bu komut, değişiklikleri daha net bir şekilde gösterir ve hangi satırların eklendiğini veya silindiğini anlamayı kolaylaştırır.

## Tips
- `diff` çıktısını bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz. Örneğin:

```bash
diff -u dosya1.txt dosya2.txt > farklar.patch
```

Bu komut, farklılıkları `farklar.patch` adlı bir dosyaya kaydeder.

- `diff` komutunu sık sık kullanıyorsanız, `vimdiff` gibi araçlarla entegrasyon yaparak, farklılıkları daha görsel bir arayüzde inceleyebilirsiniz.

- Dosyalar arasında sadece belirli bir dizin veya dosya türünü karşılaştırmak istiyorsanız, `find` komutu ile birlikte kullanarak daha hedefli karşılaştırmalar yapabilirsiniz.