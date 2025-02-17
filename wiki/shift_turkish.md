# [Linux] Bash shift Kullanımı: Komut satırındaki argümanları kaydırma

## Overview
`shift` komutu, Bash betiklerinde veya komut satırında, argümanların konumunu kaydırmak için kullanılır. Bu komut, `$1`, `$2`, `$3` gibi özel değişkenlerin değerlerini sola kaydırarak, ilk argümanı siler ve diğerlerini bir pozisyon sola kaydırır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
shift [n]
```

Burada `n`, kaydırılacak argüman sayısını belirtir. Eğer `n` belirtilmezse, varsayılan olarak 1 kabul edilir.

## Common Options
- `n`: Kaydırılacak argüman sayısını belirtir. Örneğin, `shift 2` komutu, ilk iki argümanı kaydırır.

## Common Examples

### Örnek 1: Basit Kaydırma
Aşağıdaki komut, ilk argümanı kaydırır ve ikinci argümanı birinci olarak alır.

```bash
#!/bin/bash
echo "İlk argüman: $1"
shift
echo "Yeni ilk argüman: $1"
```

### Örnek 2: Birden Fazla Argümanı Kaydırma
Bu örnekte, iki argümanı kaydırıyoruz.

```bash
#!/bin/bash
echo "Argümanlar: $1, $2, $3"
shift 2
echo "Yeni argümanlar: $1, $2"
```

### Örnek 3: Argümanları Döngü ile İşleme
Argümanları döngü ile işleyip kaydırarak tüm argümanları yazdırabiliriz.

```bash
#!/bin/bash
while [ "$#" -gt 0 ]; do
    echo "Argüman: $1"
    shift
done
```

## Tips
- `shift` komutunu kullanmadan önce, argüman sayısını kontrol etmek için `"$#"` değişkenini kullanabilirsiniz.
- `shift` komutunu kullanırken, kaydırdığınız argümanların değerlerini kaybettiğinizi unutmayın; bu nedenle, önemli argümanları kaydırmadan önce bir değişkene atamak iyi bir uygulamadır.
- `shift` komutunu, argümanları işlemek için döngülerle birlikte kullanmak, betiklerinizi daha esnek hale getirebilir.