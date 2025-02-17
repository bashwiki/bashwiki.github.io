# [Linux] Bash xargs Kullanımı: Komutları argümanlarla çalıştırır

## Genel Bakış
`xargs` komutu, standart girişten aldığı verileri alarak bu verileri bir komutun argümanları olarak kullanır. Bu, özellikle uzun argüman listeleri oluşturmak için yararlıdır ve birçok komutun çıktısını başka komutlara yönlendirmek için kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
xargs [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n N`: Her seferinde N argüman kullanarak komutu çalıştırır.
- `-d DELIMITER`: Girdiyi belirtilen ayırıcı ile ayırır.
- `-p`: Her komut çalıştırılmadan önce onay ister.
- `-0`: Null karakter ile ayrılmış girdileri işler (genellikle `find` komutuyla birlikte kullanılır).

## Yaygın Örnekler

### Örnek 1: `find` ile birlikte kullanma
Belirli bir dizindeki tüm `.txt` dosyalarını silmek için:

```bash
find . -name "*.txt" | xargs rm
```

### Örnek 2: Belirli bir kelimeyi dosyalarda arama
Bir dizindeki tüm dosyalarda "örnek" kelimesini aramak için:

```bash
ls | xargs grep "örnek"
```

### Örnek 3: Her dosya için ayrı bir komut çalıştırma
Bir dizindeki tüm dosyaları listeleyip her birini `cat` ile görüntülemek için:

```bash
ls | xargs -n 1 cat
```

### Örnek 4: Null karakter ile ayrılmış dosyaları işleme
`find` komutuyla birlikte kullanarak, boşluk içeren dosya adlarını doğru bir şekilde işlemek için:

```bash
find . -name "*.txt" -print0 | xargs -0 rm
```

## İpuçları
- `xargs` kullanırken, çok uzun argüman listeleri oluşturabileceğinizi unutmayın; bu, bazı sistemlerde komut satırı uzunluğu sınırlarına takılmanıza neden olabilir.
- `-p` seçeneğini kullanarak, komutları çalıştırmadan önce onay alabilirsiniz; bu, yanlışlıkla önemli dosyaları silmenizi önler.
- `-0` seçeneğini kullanarak, dosya adlarında boşluk veya özel karakterler olan dosyaları güvenli bir şekilde işleyebilirsiniz.