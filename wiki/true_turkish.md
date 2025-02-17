# [Linux] Bash true Kullanımı: Her zaman doğru döner

## Overview
`true` komutu, her zaman başarılı bir çıkış durumu döndüren bir Bash komutudur. Genellikle bir komutun başarılı bir şekilde çalıştığını belirtmek veya bir koşulun her zaman doğru olduğu durumlarda kullanılır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
true [options] [arguments]
```

## Common Options
`true` komutunun kendisi için özel bir seçenek yoktur, çünkü her zaman başarılı bir çıkış durumu (0) döndürür. Ancak, `true` komutunu diğer komutlarla birlikte kullanarak çeşitli senaryolar oluşturabilirsiniz.

## Common Examples

### 1. Basit Kullanım
`true` komutunu doğrudan terminalde çalıştırarak her zaman başarılı bir çıkış alabilirsiniz:
```bash
true
```

### 2. Koşullu İfadelerde Kullanım
`true` komutunu bir koşul ifadesinde kullanarak her zaman doğru bir durumu kontrol edebilirsiniz:
```bash
if true; then
    echo "Bu her zaman doğru."
fi
```

### 3. Döngülerde Kullanım
Bir döngü içinde `true` komutunu kullanarak sonsuz bir döngü oluşturabilirsiniz:
```bash
while true; do
    echo "Bu sonsuz döngüdür."
    sleep 1
done
```

### 4. Komut Zincirlerinde Kullanım
`true` komutunu diğer komutlarla birleştirerek, önceki komutun başarılı olup olmadığını kontrol edebilirsiniz:
```bash
mkdir yeni_klasor && true
```

## Tips
- `true` komutunu, betiklerde veya otomasyon görevlerinde, belirli bir koşulun her zaman geçerli olduğu durumlarda kullanmak faydalıdır.
- `true` komutunu, hata kontrolü yapmadan devam etmek istediğiniz durumlarda kullanabilirsiniz.
- `true` komutunu `&&` operatörü ile diğer komutlarla birleştirerek, daha karmaşık komut zincirleri oluşturabilirsiniz.