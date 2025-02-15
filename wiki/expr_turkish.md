# [리눅스] Bash expr 사용법

## Genel Bakış
`expr` komutu, Bash ve diğer Unix benzeri işletim sistemlerinde matematiksel ifadeleri değerlendirmek için kullanılan bir komuttur. Temel olarak, sayısal hesaplamalar, string işlemleri ve mantıksal ifadeler üzerinde çalışmak için kullanılır. `expr`, genellikle basit hesaplamalar yapmak veya değişkenler arasında karşılaştırmalar gerçekleştirmek için tercih edilir.

## Kullanım
`expr` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
expr [seçenekler] ifade
```

### Yaygın Seçenekler
- `+` : Toplama işlemi.
- `-` : Çıkarma işlemi.
- `*` : Çarpma işlemi (çarpma işlemi için `\` ile kaçış yapılması gerekir: `\*`).
- `/` : Bölme işlemi.
- `%` : Modül (kalan) işlemi.
- `=` : Eşitlik kontrolü.
- `!=` : Eşitsizlik kontrolü.
- `>` : Büyüklük kontrolü.
- `<` : Küçüklük kontrolü.

## Örnekler
### Örnek 1: Basit Matematiksel Hesaplama
Aşağıdaki komut, iki sayının toplamını hesaplar:

```bash
result=$(expr 5 + 3)
echo "Sonuç: $result"
```
Bu komut, `5 + 3` işlemini gerçekleştirir ve sonucu `Sonuç: 8` olarak yazdırır.

### Örnek 2: String Uzunluğunu Hesaplama
`expr` komutu, bir string'in uzunluğunu hesaplamak için de kullanılabilir:

```bash
string="Merhaba Dünya"
length=$(expr length "$string")
echo "String uzunluğu: $length"
```
Bu komut, `Merhaba Dünya` string'inin uzunluğunu hesaplar ve sonucu `String uzunluğu: 13` olarak yazdırır.

## İpuçları
- `expr` komutunu kullanırken, işlemler arasında boşluk bırakmayı unutmayın. Aksi takdirde, komut doğru çalışmayabilir.
- Daha karmaşık işlemler için `expr` yerine `bc` veya `awk` gibi daha güçlü araçlar kullanmayı düşünebilirsiniz.
- `expr` komutunu kullanırken, değişkenleri çift tırnak içinde kullanmak, boşluk veya özel karakter içeren string'lerde sorun yaşamamanızı sağlar.

`expr` komutu, basit hesaplamalar ve string işlemleri için etkili bir araçtır. Ancak, daha karmaşık işlemler için diğer araçları değerlendirmek her zaman iyi bir fikirdir.