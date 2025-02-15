# [리눅스] Bash test 사용법

## Genel Bakış
`test` komutu, bir koşulun doğruluğunu kontrol etmek için kullanılan bir Bash komutudur. Bu komut, belirli bir ifadenin doğru olup olmadığını belirlemek için kullanılır ve genellikle koşullu ifadelerde, özellikle `if` yapılarında kullanılır. `test` komutu, dosya varlığı, sayı karşılaştırmaları ve metin karşılaştırmaları gibi çeşitli koşulları değerlendirmek için kullanılabilir.

## Kullanım
`test` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
test [koşul]
```

Ya da alternatif olarak:

```bash
[ koşul ]
```

### Yaygın Seçenekler
- `-e dosya`: Dosyanın var olup olmadığını kontrol eder.
- `-f dosya`: Belirtilen dosyanın bir dosya olup olmadığını kontrol eder.
- `-d dizin`: Belirtilen dizinin bir dizin olup olmadığını kontrol eder.
- `-z dize`: Belirtilen dizenin boş olup olmadığını kontrol eder.
- `-n dize`: Belirtilen dizenin boş olmadığını kontrol eder.
- `a -eq b`: İki sayının eşit olup olmadığını kontrol eder.
- `a -ne b`: İki sayının eşit olmadığını kontrol eder.

## Örnekler

### Örnek 1: Dosya Varlığını Kontrol Etme
Aşağıdaki komut, `myfile.txt` dosyasının var olup olmadığını kontrol eder:

```bash
if test -e myfile.txt; then
    echo "Dosya mevcut."
else
    echo "Dosya mevcut değil."
fi
```

### Örnek 2: Sayı Karşılaştırması
Aşağıdaki komut, iki sayının eşit olup olmadığını kontrol eder:

```bash
a=5
b=10

if test $a -eq $b; then
    echo "Sayilar eşit."
else
    echo "Sayilar eşit değil."
fi
```

## İpuçları
- `test` komutunu kullanırken, koşul ifadelerini yazarken dikkatli olun. Parantezler (`[ ]`) kullanarak daha okunabilir hale getirebilirsiniz.
- `test` komutunun yerine `[` ve `]` kullanarak daha kısa bir yazım yapabilirsiniz. Örneğin, `test -e myfile.txt` yerine `[ -e myfile.txt ]` yazabilirsiniz.
- Koşul ifadelerinde boşluklara dikkat edin; boşluklar, komutun doğru çalışması için gereklidir.
- `test` komutunu kullanırken, koşul ifadelerini karmaşık hale getirmekten kaçının. Daha okunabilir ve anlaşılır kod yazmak için basit koşullar kullanmaya özen gösterin.