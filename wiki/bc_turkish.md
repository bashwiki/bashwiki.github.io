# [리눅스] Bash bc 사용법

## Overview
`bc`, "basic calculator" (temel hesap makinesi) anlamına gelen bir komut satırı aracıdır. Matematiksel hesaplamalar yapmak için kullanılır ve özellikle ondalıklı sayılarla çalışmak için idealdir. `bc`, kullanıcıların karmaşık matematiksel ifadeleri değerlendirmesine ve hesaplamalar yapmasına olanak tanır. Ayrıca, kullanıcı tanımlı fonksiyonlar ve değişkenler ile programlama yetenekleri de sunar.

## Usage
`bc` komutunun temel sözdizimi şu şekildedir:

```bash
bc [options] [file]
```

### Yaygın Seçenekler
- `-l`: Matematiksel fonksiyonlar ve sabitler içeren bir kütüphane ile başlatır. Bu seçenek, daha karmaşık hesaplamalar için kullanışlıdır.
- `-q`: Çıktıdan "bc" sürüm numarasını gizler ve daha temiz bir çıktı sağlar.
- `-e`: Komut satırından doğrudan ifadeler girmeye olanak tanır.

## Examples
### Örnek 1: Basit Hesaplama
Aşağıdaki komut, `bc` kullanarak iki sayının toplamını hesaplar:

```bash
echo "5 + 3" | bc
```
Bu komutun çıktısı `8` olacaktır.

### Örnek 2: Ondalık Sayılarla Hesaplama
`-l` seçeneği ile daha karmaşık bir hesaplama yapabiliriz:

```bash
echo "scale=2; 10 / 3" | bc -l
```
Bu komut, `10` sayısını `3` sayısına böler ve sonucu iki ondalık basamakla gösterir. Çıktı `3.33` olacaktır.

## Tips
- `scale` değişkeni, ondalık basamak sayısını belirler. Hesaplamalarınızda istediğiniz hassasiyeti sağlamak için `scale` değerini ayarlayın.
- `bc` ile matematiksel ifadeleri doğrudan dosyadan okuyarak daha karmaşık hesaplamalar yapabilirsiniz. Örneğin, bir dosya oluşturup içerisine ifadeleri yazdıktan sonra şu şekilde çalıştırabilirsiniz:

```bash
bc < hesaplamalar.txt
```
- `bc` kullanırken, ifadelerinizi doğru bir şekilde yazdığınızdan emin olun; aksi takdirde hata mesajları alabilirsiniz.