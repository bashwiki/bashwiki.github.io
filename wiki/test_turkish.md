# [Linux] Bash test Kullanımı: Koşul testleri yapma aracı

## Overview
`test` komutu, belirli koşulları kontrol etmek için kullanılan bir Bash komutudur. Dosyaların varlığı, karşılaştırmalar ve diğer mantıksal işlemler gibi çeşitli testler yaparak, bir koşulun doğru veya yanlış olduğunu belirlemeye yardımcı olur.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
test [options] [arguments]
```

## Common Options
- `-e`: Belirtilen dosyanın var olup olmadığını kontrol eder.
- `-f`: Belirtilen yolun bir dosya olup olmadığını kontrol eder.
- `-d`: Belirtilen yolun bir dizin olup olmadığını kontrol eder.
- `-z`: Belirtilen stringin boş olup olmadığını kontrol eder.
- `-n`: Belirtilen stringin boş olmadığını kontrol eder.
- `=`: İki stringin eşit olup olmadığını kontrol eder.
- `-eq`: İki sayının eşit olup olmadığını kontrol eder.

## Common Examples
Aşağıda `test` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. Dosyanın varlığını kontrol etme
```bash
test -e dosya.txt && echo "Dosya mevcut."
```

### 2. Bir dizinin varlığını kontrol etme
```bash
test -d /home/kullanici && echo "Dizin mevcut."
```

### 3. Bir stringin boş olup olmadığını kontrol etme
```bash
string=""
test -z "$string" && echo "String boş."
```

### 4. İki sayının eşitliğini kontrol etme
```bash
sayi1=5
sayi2=5
test $sayi1 -eq $sayi2 && echo "Sayilar eşit."
```

### 5. İki stringin eşitliğini kontrol etme
```bash
string1="merhaba"
string2="merhaba"
test "$string1" = "$string2" && echo "Stringler eşit."
```

## Tips
- `test` komutunun yerine `[` ve `]` kullanarak daha okunabilir bir sözdizimi elde edebilirsiniz. Örneğin: `[ -e dosya.txt ]`.
- Koşul testlerini `if` yapıları içinde kullanarak daha karmaşık mantıklar oluşturabilirsiniz.
- `test` komutunu kullanırken, argümanlarınızı tırnak içine almayı unutmayın; bu, boşluk veya özel karakter içeren stringler için önemlidir.