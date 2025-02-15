# [리눅스] Bash break 사용법

## Overview
`break` komutu, bir döngüden çıkmak için kullanılan bir Bash komutudur. Genellikle `for`, `while` veya `until` döngülerinin içinde kullanılır ve döngünün hemen sonlanmasını sağlar. Bu, belirli bir koşul gerçekleştiğinde döngüyü sonlandırmak için oldukça yararlıdır.

## Usage
`break` komutunun temel kullanımı oldukça basittir. Aşağıda temel sözdizimi verilmiştir:

```bash
break [n]
```

- `n`: (isteğe bağlı) Çıkmak istediğiniz döngü seviyesini belirtir. Eğer belirtilmezse, en içteki döngüden çıkılır. Eğer birden fazla döngü iç içe geçmişse, `n` değeri kullanılarak hangi döngüden çıkılacağı belirlenebilir.

## Examples

### Örnek 1: Basit bir döngüden çıkma
Aşağıdaki örnekte, bir `for` döngüsü 5'e kadar sayar ve 3'e ulaştığında döngüyü sonlandırır:

```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        break
    fi
    echo $i
done
```
Bu komut çalıştırıldığında, çıktı olarak `1` ve `2` yazdırılır, ardından döngü `3` değerine ulaştığında sonlanır.

### Örnek 2: İç içe döngülerde çıkma
Aşağıdaki örnekte, iç içe geçmiş iki döngüde `break` komutunun nasıl kullanılacağını gösterir:

```bash
for i in {1..3}; do
    for j in {1..3}; do
        if [ $j -eq 2 ]; then
            break 2
        fi
        echo "i: $i, j: $j"
    done
done
```
Bu komut çalıştırıldığında, `j` değeri `2` olduğunda dıştaki döngü de dahil olmak üzere tüm döngüler sonlanır.

## Tips
- `break` komutunu kullanırken, döngülerin iç içe olup olmadığını dikkate almak önemlidir. `n` parametresi ile hangi döngüden çıkacağınızı belirleyebilirsiniz.
- Döngülerinizi daha okunabilir hale getirmek için, `break` komutunu kullanmadan önce koşul ifadelerinizi net bir şekilde tanımlayın.
- `break` komutunu kullanırken, döngülerin sonlanma koşullarını dikkatlice düşünün; gereksiz yere döngüleri sonlandırmak, programınızın beklenmedik şekilde çalışmasına neden olabilir.