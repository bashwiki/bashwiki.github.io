# [Linux] Bash printf Kullanımı: Formatlı çıktı üretme aracı

## Genel Bakış
`printf` komutu, formatlı metin çıktısı üretmek için kullanılan bir Bash komutudur. C dilindeki `printf` fonksiyonuna benzer şekilde çalışır ve kullanıcıların belirli bir formatta verileri yazdırmasına olanak tanır.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
printf [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-v`: Değişkeni formatlı çıktı ile atar.
- `-f`: Format belirleme.
- `-n`: Yeni satır karakteri eklemez.

## Yaygın Örnekler
Aşağıda `printf` komutunun bazı pratik örnekleri verilmiştir:

### Örnek 1: Basit metin yazdırma
```bash
printf "Merhaba, Dünya!\n"
```

### Örnek 2: Değişken ile yazdırma
```bash
isim="Ali"
printf "Merhaba, %s!\n" "$isim"
```

### Örnek 3: Sayı formatlama
```bash
printf "Sayı: %.2f\n" 3.14159
```

### Örnek 4: Birden fazla argüman yazdırma
```bash
printf "Ad: %s, Yaş: %d\n" "Ayşe" 30
```

## İpuçları
- Format belirlerken `%s` (string) ve `%d` (integer) gibi format belirteçlerini kullanmayı unutmayın.
- Çıktıyı daha okunabilir hale getirmek için boşluk ve yeni satır karakterlerini kullanın.
- Uzun çıktılar için `-v` seçeneği ile çıktıyı bir değişkene atayarak daha sonra kullanabilirsiniz.