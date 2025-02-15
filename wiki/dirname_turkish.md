# [리눅스] Bash dirname 사용법

## Overview
`dirname` komutu, bir dosya yolunun dizin kısmını ayıklamak için kullanılır. Temel amacı, verilen bir dosya yolunun dizin adını döndürmektir. Bu, özellikle dosya yolları ile çalışırken, dosyanın bulunduğu dizini belirlemek için faydalıdır.

## Usage
`dirname` komutunun temel sözdizimi şu şekildedir:

```bash
dirname [yol]
```

### Ortak Seçenekler
`dirname` komutunun kendine özgü bir seçeneği yoktur; yalnızca bir dosya yolu alır ve bu yolun dizin kısmını döndürür.

## Examples
Aşağıda `dirname` komutunun nasıl kullanılacağına dair iki pratik örnek bulunmaktadır:

### Örnek 1: Basit Kullanım
Bir dosya yolunun dizinini almak için:

```bash
$ dirname /home/kullanici/dosya.txt
/home/kullanici
```

Bu komut, `/home/kullanici/dosya.txt` dosyasının bulunduğu dizini döndürür.

### Örnek 2: Göreli Yol Kullanımı
Göreli bir yol verildiğinde de `dirname` kullanılabilir:

```bash
$ dirname ./belgeler/rapor.pdf
./belgeler
```

Bu komut, `./belgeler/rapor.pdf` dosyasının bulunduğu dizini döndürür.

## Tips
- `dirname` komutunu, dosya yollarını işlerken diğer komutlarla birleştirerek kullanabilirsiniz. Örneğin, bir dosyanın dizinini almak ve ardından o dizinde başka bir işlem yapmak için:
  
  ```bash
  cd $(dirname /home/kullanici/dosya.txt)
  ```

- Dosya yolunu kontrol etmek ve geçerli bir yol olup olmadığını doğrulamak için `test` veya `if` yapıları ile birlikte kullanabilirsiniz.

Bu bilgilerle `dirname` komutunu etkili bir şekilde kullanabilir ve dosya yolları ile çalışırken daha verimli olabilirsiniz.