# [리눅스] Bash pwd 사용법

## Genel Bakış
`pwd` (print working directory), mevcut çalışma dizinini gösteren bir Bash komutudur. Terminalde çalışırken hangi dizinde bulunduğunuzu hızlı bir şekilde öğrenmek için kullanılır. Bu komut, özellikle birden fazla dizin arasında geçiş yaparken ve dosya yollarını belirlerken faydalıdır.

## Kullanım
Temel `pwd` komutunun sözdizimi oldukça basittir:

```bash
pwd [seçenekler]
```

### Yaygın Seçenekler
- `-L`: Bu seçenek, sembolik bağlantıları takip eder ve mevcut dizinin gerçek yolunu gösterir.
- `-P`: Bu seçenek, sembolik bağlantıları takip etmeden mevcut dizinin fiziksel yolunu gösterir.

## Örnekler
### Örnek 1: Basit Kullanım
Mevcut çalışma dizininizi öğrenmek için sadece `pwd` komutunu yazabilirsiniz:

```bash
pwd
```
Çıktı:
```
/home/kullanici
```

### Örnek 2: Fiziksel Yol Gösterimi
Eğer sembolik bağlantıları takip etmeden mevcut dizinin fiziksel yolunu görmek isterseniz, `-P` seçeneğini kullanabilirsiniz:

```bash
pwd -P
```
Çıktı:
```
/home/kullanici/gercek_dizin
```

## İpuçları
- `pwd` komutunu sık sık kullanıyorsanız, terminalinizin başlangıç dizinini ayarlamak için `.bashrc` veya `.bash_profile` dosyalarınızı düzenleyebilirsiniz.
- `pwd` komutunu diğer dosya yönetimi komutlarıyla birleştirerek, dosya yollarını daha etkili bir şekilde kullanabilirsiniz. Örneğin, `cd $(pwd)/belgeler` komutu ile mevcut dizininizdeki "belgeler" dizinine hızlıca geçiş yapabilirsiniz.