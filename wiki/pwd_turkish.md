# [Linux] Bash pwd Kullanımı: Geçerli dizini gösterir

## Genel Bakış
`pwd` (print working directory) komutu, terminalde bulunduğunuz mevcut dizinin tam yolunu gösterir. Bu komut, dosya sisteminde hangi dizinde çalıştığınızı anlamanızı sağlar.

## Kullanım
Temel sözdizimi şu şekildedir:
```
pwd [options] [arguments]
```

## Yaygın Seçenekler
- `-L`: Mantıksal yolu gösterir. (Varsayılan)
- `-P`: Fiziksel yolu gösterir. Yani, sembolik bağlantılara bakmadan gerçek dizin yolunu verir.

## Yaygın Örnekler
Aşağıda `pwd` komutunun bazı pratik örnekleri bulunmaktadır:

### Örnek 1: Basit Kullanım
Mevcut dizini görmek için:
```bash
pwd
```

### Örnek 2: Mantıksal Yol Gösterimi
Mantıksal yolu görüntülemek için:
```bash
pwd -L
```

### Örnek 3: Fiziksel Yol Gösterimi
Fiziksel yolu görüntülemek için:
```bash
pwd -P
```

## İpuçları
- `pwd` komutunu sıkça kullanarak, terminalde hangi dizinde olduğunuzu kolayca kontrol edebilirsiniz.
- Eğer sembolik bağlantılarla çalışıyorsanız, `-P` seçeneği ile gerçek dizin yolunu görmek faydalı olabilir.
- Çalıştığınız dizinle ilgili daha fazla bilgi almak için `ls` komutunu `pwd` ile birleştirebilirsiniz. Örneğin:
```bash
ls $(pwd)
```