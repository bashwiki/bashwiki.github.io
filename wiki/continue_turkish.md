# [리눅스] Bash continue 사용법

## Overview
`continue` komutu, bir döngü içinde kullanıldığında, döngünün mevcut yinelemesini atlayarak bir sonraki yinelemeye geçilmesini sağlar. Bu komut, özellikle belirli bir koşul sağlandığında döngüdeki bazı işlemleri atlamak istediğinizde yararlıdır. `continue`, genellikle `for`, `while` ve `until` döngüleri ile birlikte kullanılır.

## Usage
`continue` komutunun temel sözdizimi oldukça basittir:

```bash
continue [n]
```

Burada `n`, döngünün kaçıncı yinelemesine geçileceğini belirtir. Eğer `n` belirtilmezse, varsayılan olarak 1 alınır ve döngü bir sonraki yinelemeye geçer.

### Örnekler
Aşağıda `continue` komutunun nasıl kullanılacağını gösteren iki örnek bulunmaktadır:

**Örnek 1: Basit bir for döngüsü**
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo "Sayı: $i"
done
```
Bu örnekte, `i` değişkeni 3 olduğunda `continue` komutu çalışır ve 3 sayısı atlanır. Çıktı şöyle olacaktır:
```
Sayı: 1
Sayı: 2
Sayı: 4
Sayı: 5
```

**Örnek 2: While döngüsü ile kullanım**
```bash
count=1
while [ $count -le 5 ]; do
    if [ $count -eq 2 ]; then
        count=$((count + 1))
        continue
    fi
    echo "Sayım: $count"
    count=$((count + 1))
done
```
Bu örnekte, `count` değişkeni 2 olduğunda `continue` komutu çalışır ve 2 sayısı atlanır. Çıktı şöyle olacaktır:
```
Sayım: 1
Sayım: 3
Sayım: 4
Sayım: 5
```

## Tips
- `continue` komutunu kullanırken, döngüde atlanacak koşulları dikkatlice belirlemek önemlidir. Yanlış koşullar, beklenmeyen sonuçlara yol açabilir.
- `continue` komutunu kullanmadan önce, döngü değişkeninin güncellenmesini sağlamak için uygun bir mekanizma oluşturduğunuzdan emin olun. Aksi takdirde, sonsuz döngülerle karşılaşabilirsiniz.
- `continue` komutunu kullanarak kodunuzu daha okunabilir hale getirebilir ve belirli durumları daha kolay yönetebilirsiniz.