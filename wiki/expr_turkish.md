# [Linux] Bash expr Kullanımı: Matematiksel ifadeleri değerlendirme

## Genel Bakış
`expr` komutu, Bash ortamında matematiksel ifadeleri değerlendirmek için kullanılan bir araçtır. Temel olarak, sayısal hesaplamalar yapmanıza, metin işlemleri gerçekleştirmenize ve mantıksal ifadeleri değerlendirmenize olanak tanır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
expr [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `+` : Toplama işlemi.
- `-` : Çıkarma işlemi.
- `*` : Çarpma işlemi. (Dikkat: Çarpma işlemi için kaçış karakteri `\` kullanmalısınız.)
- `/` : Bölme işlemi.
- `%` : Modül alma (kalan) işlemi.
- `=` : Değeri atama.
- `:` : Dize uzunluğunu bulma.

## Yaygın Örnekler
Aşağıda `expr` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### Toplama İşlemi
```bash
expr 5 + 3
```
Bu komut, 5 ile 3'ü toplar ve sonucu 8 olarak döndürür.

### Çıkarma İşlemi
```bash
expr 10 - 4
```
Bu komut, 10'dan 4'ü çıkarır ve sonucu 6 olarak verir.

### Çarpma İşlemi
```bash
expr 4 \* 7
```
Bu komut, 4 ile 7'yi çarpar ve sonucu 28 olarak döndürür. (Çarpma işlemi için `\` kullanmayı unutmayın.)

### Bölme İşlemi
```bash
expr 20 / 5
```
Bu komut, 20'yi 5'e böler ve sonucu 4 olarak verir.

### Modül Alma
```bash
expr 10 % 3
```
Bu komut, 10'un 3'e bölümünden kalan olan 1'i döndürür.

### Dize Uzunluğu
```bash
expr length "Merhaba"
```
Bu komut, "Merhaba" dizesinin uzunluğunu döndürür ve sonuç 7'dir.

## İpuçları
- `expr` komutunu kullanırken, çarpma işlemi için `\` karakterini kullanmayı unutmayın.
- Sayısal işlemler yaparken, boşlukların doğru yerleştirildiğinden emin olun; aksi takdirde hata alabilirsiniz.
- Daha karmaşık hesaplamalar için, `expr` yerine `bc` veya `awk` gibi daha gelişmiş araçları kullanmayı düşünebilirsiniz.