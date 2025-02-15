# [리눅스] Bash xargs 사용법

## Genel Bakış
`xargs`, Unix ve Linux sistemlerinde kullanılan bir komut satırı aracıdır. Temel amacı, standart girdi (stdin) üzerinden alınan verileri alıp, bunları bir komutun argümanları olarak kullanmaktır. Özellikle, uzun argüman listelerini işlemek için yararlıdır ve genellikle diğer komutlarla birlikte kullanılır. `xargs`, verileri birleştirerek komutları daha verimli bir şekilde çalıştırmanıza olanak tanır.

## Kullanım
`xargs` komutunun temel sözdizimi şu şekildedir:

```bash
xargs [seçenekler] [komut]
```

### Yaygın Seçenekler
- `-n N`: Her seferinde N argüman kullanarak komutu çalıştırır.
- `-d DELIMITER`: Girdiyi belirtilen ayırıcı ile böler.
- `-p`: Her komut çalıştırılmadan önce onay ister.
- `-0`: Null karakter (`\0`) ile ayrılmış girdileri işler, bu özellikle dosya adlarında boşluk veya özel karakterler olduğunda faydalıdır.

## Örnekler

### Örnek 1: Dosya Silme
Aşağıdaki komut, geçerli dizindeki tüm `.tmp` uzantılı dosyaları siler:

```bash
find . -name "*.tmp" | xargs rm
```

Bu komut, `find` komutunun çıktısını alır ve `rm` komutuna argüman olarak geçirir.

### Örnek 2: Belirli Bir Sayıda Argümanla Komut Çalıştırma
Aşağıdaki komut, her seferinde 3 dosya alarak `ls` komutunu çalıştırır:

```bash
ls | xargs -n 3 echo
```

Bu komut, `ls` çıktısını alır ve her seferinde 3 dosya ismi ile `echo` komutunu çalıştırır.

## İpuçları
- `xargs` kullanırken, girdi verilerinizde boşluk veya özel karakterler varsa `-0` seçeneğini kullanarak güvenli bir şekilde işlem yapabilirsiniz.
- `-p` seçeneği ile komut çalıştırılmadan önce onay alarak, yanlışlıkla istenmeyen işlemler yapmanızı önleyebilirsiniz.
- `xargs` ile birlikte `find`, `grep` gibi diğer komutları kullanarak güçlü ve esnek komut zincirleri oluşturabilirsiniz.

`xargs`, komut satırında verimli bir şekilde işlem yapmanıza olanak tanıyan güçlü bir araçtır. Doğru kullanıldığında, iş akışınızı önemli ölçüde hızlandırabilir.