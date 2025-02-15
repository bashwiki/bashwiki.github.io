# [리눅스] Bash hash 사용법

## Genel Bakış
`hash` komutu, Bash kabuğunda kullanılan bir komuttur ve komutların yolunu önbelleğe alarak, daha hızlı erişim sağlar. Komutlar çalıştırıldığında, Bash bu komutların tam yollarını kaydeder. Böylece, aynı komut tekrar çalıştırıldığında, Bash önbellekten bu yolu alarak daha hızlı bir şekilde çalıştırabilir. Bu, özellikle sık kullanılan komutlar için performansı artırır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
hash [seçenekler] [komutlar]
```

### Yaygın Seçenekler
- `-r`: Tüm önbelleği temizler. Bu seçenek kullanıldığında, önbellekteki tüm komut yolları silinir ve bir sonraki komut çalıştırıldığında, yollar yeniden kaydedilir.
- `-l`: Mevcut önbellekteki tüm komutların listesini gösterir.

## Örnekler

### Örnek 1: Mevcut önbelleği görüntüleme
Aşağıdaki komut, mevcut önbellekteki tüm komutların yollarını listeleyecektir:

```bash
hash -l
```

### Örnek 2: Önbelleği temizleme
Eğer önbelleği temizlemek isterseniz, şu komutu kullanabilirsiniz:

```bash
hash -r
```

Bu komut, tüm önbelleği sıfırlayarak, bir sonraki komut çalıştırıldığında yolların yeniden kaydedilmesini sağlar.

## İpuçları
- `hash` komutunu sık kullandığınız komutların performansını artırmak için kullanabilirsiniz. Özellikle, uzun ve karmaşık yolları olan komutlar için bu önbellekleme işlemi faydalı olacaktır.
- Eğer bir komutun yolunu değiştirdiyseniz veya yeni bir komut eklediyseniz, `hash -r` komutunu kullanarak önbelleği güncelleyebilirsiniz. Bu, eski yol bilgilerini temizler ve yeni bilgilerin kaydedilmesini sağlar.