# [Linux] Bash return kullanımı: Çıkış durumunu döndürme

## Overview
`return` komutu, bir fonksiyondan çıkış durumunu döndürmek için kullanılır. Bu komut, bir fonksiyonun sonucunu belirlemek ve çağrıldığı yere geri bildirim sağlamak amacıyla kullanılır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
return [options] [n]
```

Burada `n`, döndürmek istediğiniz çıkış durumunu belirtir. Eğer `n` belirtilmezse, fonksiyonun en son çalıştırılan komutunun çıkış durumu döndürülür.

## Common Options
- `n`: Döndürmek istediğiniz çıkış durumunu belirtir. Genellikle 0 (başarılı) veya 1 (başarısız) gibi değerler kullanılır.

## Common Examples
Aşağıda `return` komutunun bazı pratik örnekleri verilmiştir:

### Örnek 1: Basit bir fonksiyon
```bash
my_function() {
    echo "Fonksiyon çalışıyor."
    return 0
}

my_function
echo "Çıkış durumu: $?"
```
Bu örnekte, `my_function` çağrıldığında 0 çıkış durumu döndürülür.

### Örnek 2: Hata durumu döndürme
```bash
my_function() {
    echo "Bir hata oluştu."
    return 1
}

my_function
echo "Çıkış durumu: $?"
```
Bu örnekte, fonksiyon 1 çıkış durumu döndürerek bir hata olduğunu belirtir.

### Örnek 3: Çıkış durumunu kontrol etme
```bash
my_function() {
    return 0
}

my_function
if [ $? -eq 0 ]; then
    echo "Fonksiyon başarılı bir şekilde çalıştı."
else
    echo "Fonksiyon başarısız oldu."
fi
```
Bu örnekte, çıkış durumu kontrol edilerek fonksiyonun başarılı olup olmadığı belirlenir.

## Tips
- `return` komutunu yalnızca fonksiyonlar içinde kullanın; dışarıda kullanıldığında hata verebilir.
- Çıkış durumlarını standart hale getirmek için 0'ı başarı, 1'i hata olarak kullanın.
- Fonksiyonlarınızda anlamlı çıkış durumları döndürmek, hata ayıklamayı kolaylaştırır.