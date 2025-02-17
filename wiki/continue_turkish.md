# [Linux] Bash continue kullanımı: Döngüdeki bir sonraki yinelemeye geçer

## Genel Bakış
`continue` komutu, bir döngü içinde kullanıldığında, döngünün mevcut yinelemesini atlayarak bir sonraki yinelemeye geçilmesini sağlar. Bu, belirli bir koşul sağlandığında döngünün geri kalanını atlamak için yararlıdır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
continue [options]
```

## Yaygın Seçenekler
`continue` komutunun kendisi için özel bir seçenek yoktur, ancak döngü içinde belirli bir koşula bağlı olarak kullanılabilir.

## Yaygın Örnekler

### Örnek 1: Basit bir döngüde continue kullanımı
Aşağıdaki örnekte, 1'den 10'a kadar olan sayılardan yalnızca çift olanları yazdırıyoruz. Tek sayılar için `continue` komutunu kullanarak döngünün o kısmını atlıyoruz.

```bash
for i in {1..10}; do
    if (( i % 2 != 0 )); then
        continue
    fi
    echo $i
done
```

### Örnek 2: Belirli bir koşula göre continue kullanımı
Bu örnekte, bir dizideki sayılardan yalnızca 5'ten büyük olanları yazdırıyoruz.

```bash
numbers=(1 2 3 4 5 6 7 8 9 10)
for num in "${numbers[@]}"; do
    if (( num <= 5 )); then
        continue
    fi
    echo $num
done
```

### Örnek 3: while döngüsünde continue kullanımı
Aşağıdaki örnekte, 1'den 10'a kadar olan sayılardan yalnızca 3'e bölünebilenleri yazdırıyoruz.

```bash
count=1
while [ $count -le 10 ]; do
    if (( count % 3 != 0 )); then
        ((count++))
        continue
    fi
    echo $count
    ((count++))
done
```

## İpuçları
- `continue` komutunu kullanırken, döngü koşullarınızı dikkatlice belirleyin. Yanlış koşullar, beklenmeyen sonuçlara yol açabilir.
- `continue` komutunu, karmaşık döngülerde kodunuzu daha okunabilir hale getirmek için kullanabilirsiniz.
- Gelişmiş senaryolar için `continue` komutunu `if` koşullarıyla birleştirerek kullanmak, kodunuzu daha esnek hale getirebilir.