# [Linux] Bash bc Kullanımı: Hesaplama aracı

## Genel Bakış
`bc`, Bash ortamında matematiksel hesaplamalar yapmak için kullanılan bir komut satırı aracıdır. Temel aritmetik işlemlerden karmaşık matematiksel hesaplamalara kadar geniş bir yelpazede işlevsellik sunar. `bc`, kullanıcıların hesaplamalarını etkileşimli bir şekilde yapmalarına veya bir dosyadan komutlar alarak otomatik hesaplamalar gerçekleştirmelerine olanak tanır.

## Kullanım
`bc` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
bc [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-l`: Matematiksel fonksiyonlar ve daha yüksek hassasiyet için standart matematik kütüphanesini yükler.
- `-q`: Başlangıçta herhangi bir bilgi mesajı göstermez.
- `-e`: Komutları doğrudan komut satırından çalıştırmak için kullanılır.

## Yaygın Örnekler
Aşağıda `bc` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### Temel Aritmetik İşlemler
Toplama, çıkarma, çarpma ve bölme işlemleri yapmak için:

```bash
echo "5 + 3" | bc
```

### Kesirli Sayılarla Hesaplama
Kesirli sayılarla işlem yapmak için:

```bash
echo "scale=2; 10 / 3" | bc
```

### Matematiksel Fonksiyonlar
Karekök hesaplamak için `-l` seçeneği ile birlikte:

```bash
echo "sqrt(16)" | bc -l
```

### Değişken Kullanımı
Değişken tanımlayıp kullanmak:

```bash
echo "x=5; y=10; x * y" | bc
```

## İpuçları
- `scale` değişkenini kullanarak sonuçların hassasiyetini ayarlayabilirsiniz. Örneğin, `scale=3; 1/3` ifadesi 0.333 olarak sonuçlanır.
- `bc` komutunu bir dosyadan komut almak için kullanmak isterseniz, dosya adını doğrudan komutun argümanı olarak verebilirsiniz: `bc dosya.txt`.
- Hesaplamalarınızı daha okunabilir hale getirmek için, karmaşık ifadeleri parantez içinde yazmayı unutmayın.