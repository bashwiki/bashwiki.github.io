# [리눅스] Bash mapfile 사용법

## Overview
`mapfile`, Bash kabuğunda bir komut olup, bir dosyadaki satırları bir diziye okuma işlemi için kullanılır. Bu komut, özellikle dosya içeriğini dizi elemanları olarak depolamak isteyen mühendisler ve geliştiriciler için oldukça kullanışlıdır. `mapfile`, her bir satırı dizinin bir elemanı olarak kaydeder ve bu sayede dosya içeriği üzerinde kolaylıkla işlem yapma imkanı sunar.

## Usage
`mapfile` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
mapfile [options] [array_name]
```

### Yaygın Seçenekler:
- `-t`: Satır sonu karakterlerini kaldırarak dizinin elemanlarını oluşturur. Bu, genellikle istenen bir davranıştır çünkü satır sonu karakterleri çoğu durumda gereksizdir.
- `-n count`: Okunacak satır sayısını belirtir. Bu seçenek ile sadece belirtilen sayıda satır okunur.
- `-s count`: Okunacak satırların başlangıç noktasını belirtir. Bu, dosyanın başından itibaren belirli bir sayıda satırı atlayarak okumaya başlamak için kullanılır.

## Examples

### Örnek 1: Basit Kullanım
Aşağıdaki örnekte, bir dosyadaki tüm satırlar `my_array` adlı bir diziye okunmaktadır.

```bash
mapfile my_array < my_file.txt
echo "${my_array[@]}"
```

Bu komut, `my_file.txt` dosyasındaki her satırı `my_array` dizisinin bir elemanı olarak depolar ve ardından dizinin içeriğini ekrana yazdırır.

### Örnek 2: Satır Sonu Karakterlerini Kaldırma
Aşağıdaki örnekte, satır sonu karakterleri kaldırılarak bir dosyadaki satırlar okunmaktadır.

```bash
mapfile -t my_array < my_file.txt
for line in "${my_array[@]}"; do
    echo "$line"
done
```

Burada `-t` seçeneği kullanılarak, dizinin elemanları oluşturulurken satır sonu karakterleri kaldırılmıştır.

## Tips
- `mapfile` komutunu kullanırken, dosyanın büyük boyutlarda olması durumunda bellek kullanımını göz önünde bulundurmalısınız. Büyük dosyalar okunduğunda, sistem kaynakları üzerinde olumsuz etkiler yaratabilir.
- Dizi elemanlarını döngü ile işlemek, dosya içeriği üzerinde işlem yapmanın etkili bir yoludur. Bu nedenle, `mapfile` ile okunan diziyi döngülerle kullanmak iyi bir uygulamadır.
- `mapfile` komutunu kullanmadan önce, dosyanın var olduğundan ve okunabilir olduğundan emin olun. Aksi takdirde, hata mesajları ile karşılaşabilirsiniz.