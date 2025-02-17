# [Linux] Bash declare Kullanımı: Değişkenleri Tanımlama ve Özelleştirme

## Genel Bakış
`declare` komutu, Bash kabuğunda değişkenleri tanımlamak ve bu değişkenlerin özelliklerini belirlemek için kullanılır. Bu komut, değişkenlerin türünü ve özelliklerini ayarlayarak daha kontrollü bir programlama deneyimi sağlar.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
declare [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-i`: Değişkeni tam sayı olarak tanımlar. Bu durumda, değişkenin değeri matematiksel işlemlere tabi tutulur.
- `-r`: Değişkeni salt okunur yapar. Bu değişkenin değeri daha sonra değiştirilemez.
- `-a`: Değişkeni dizin (array) olarak tanımlar.
- `-A`: Değişkeni ilişkilendirilmiş dizi (associative array) olarak tanımlar.
- `-x`: Değişkeni ortam değişkeni olarak tanımlar. Bu, değişkenin alt süreçlere aktarılmasını sağlar.

## Yaygın Örnekler
Aşağıda `declare` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### Tam Sayı Değişkeni Tanımlama
```bash
declare -i sayi=5
sayi+=10
echo $sayi  # Çıktı: 15
```

### Salt Okunur Değişken
```bash
declare -r sabit=100
echo $sabit  # Çıktı: 100
# sabit=200  # Bu satır hata verecektir.
```

### Dizi Tanımlama
```bash
declare -a dizi=(elma armut muz)
echo ${dizi[1]}  # Çıktı: armut
```

### İlişkilendirilmiş Dizi Tanımlama
```bash
declare -A renkler
renkler[elma]="kırmızı"
renkler[armut]="yeşil"
echo ${renkler[elma]}  # Çıktı: kırmızı
```

### Ortam Değişkeni Olarak Tanımlama
```bash
declare -x PATH="/usr/local/bin:$PATH"
```

## İpuçları
- Değişkenlerinizi tanımlarken, türlerini belirlemek için `declare` komutunu kullanarak kodunuzun daha okunabilir ve yönetilebilir olmasını sağlayabilirsiniz.
- Salt okunur değişkenler kullanarak, kritik değerlerin yanlışlıkla değiştirilmesini önleyebilirsiniz.
- Dizi ve ilişkilendirilmiş dizi kullanarak, birden fazla değeri yönetmek için daha etkili bir yol sunabilirsiniz.