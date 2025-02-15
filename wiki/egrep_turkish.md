# [리눅스] Bash egrep 사용법

## Overview
`egrep`, "extended grep" anlamına gelir ve düzenli ifadelerle arama yapmak için kullanılan bir komuttur. `grep` komutunun bir uzantısıdır ve daha karmaşık desenleri tanımlamak için ek özellikler sunar. `egrep`, metin dosyalarında veya standart girişte belirli bir deseni aramak için kullanılır ve genellikle metin işleme ve analizinde faydalıdır.

## Usage
Temel sözdizimi şu şekildedir:

```bash
egrep [seçenekler] 'desen' [dosya_adı]
```

### Yaygın Seçenekler
- `-i`: Büyük/küçük harf duyarsız arama yapar.
- `-v`: Deseni içermeyen satırları gösterir.
- `-c`: Eşleşen satırların sayısını gösterir.
- `-n`: Eşleşen satırların satır numaralarını gösterir.
- `-r` veya `-R`: Alt dizinler dahil olmak üzere dizinlerde arama yapar.

## Examples
### Örnek 1: Basit Desen Arama
Aşağıdaki komut, `metin.txt` dosyasında "örnek" kelimesini arar:

```bash
egrep 'örnek' metin.txt
```

### Örnek 2: Büyük/Küçük Harf Duyarsız Arama
Aşağıdaki komut, "örnek" kelimesinin büyük/küçük harf farkı gözetmeksizin aramasını yapar:

```bash
egrep -i 'örnek' metin.txt
```

## Tips
- `egrep` kullanırken, karmaşık desenler oluşturmak için parantezler ve `|` (veya) operatörlerini kullanabilirsiniz. Örneğin, `egrep 'örnek|test' metin.txt` komutu, hem "örnek" hem de "test" kelimelerini arar.
- Performans açısından, büyük dosyalar üzerinde arama yaparken `-c` seçeneği ile sadece eşleşen satırların sayısını almak, gereksiz çıktıdan kaçınmanıza yardımcı olabilir.
- `egrep` komutunu diğer komutlarla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz. Örneğin, `cat dosya.txt | egrep 'desen'` ile dosyayı okumadan direkt olarak arama yapabilirsiniz.