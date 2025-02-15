# [리눅스] Bash uniq 사용법

## Overview
`uniq` komutu, bir dosya veya standart girdi içindeki ardışık tekrar eden satırları kaldırmak için kullanılır. Temel amacı, belirli bir veri kümesindeki benzersiz satırları elde etmektir. `uniq`, genellikle sıralı verilerle birlikte kullanılır; çünkü yalnızca ardışık tekrarları kaldırır. Bu nedenle, genellikle `sort` komutuyla birlikte kullanılması önerilir.

## Usage
`uniq` komutunun temel sözdizimi şu şekildedir:

```bash
uniq [seçenekler] [girdi_dosyası] [çıktı_dosyası]
```

### Yaygın Seçenekler
- `-c`: Her benzersiz satırın önüne, o satırın kaç kez tekrar ettiğini gösteren bir sayı ekler.
- `-d`: Sadece tekrar eden satırları gösterir.
- `-u`: Sadece benzersiz olan satırları gösterir.
- `-i`: Büyük/küçük harf duyarsız olarak karşılaştırma yapar.

## Examples
### Örnek 1: Temel Kullanım
Aşağıdaki komut, `input.txt` dosyasındaki benzersiz satırları çıkartır ve sonucu `output.txt` dosyasına yazar:

```bash
uniq input.txt output.txt
```

### Örnek 2: Tekrar Sayısını Gösterme
Aşağıdaki komut, `input.txt` dosyasındaki her benzersiz satırın tekrar sayısını gösterir:

```bash
uniq -c input.txt
```

## Tips
- `uniq` komutunu kullanmadan önce verilerinizi sıralamak için `sort` komutunu kullanmayı unutmayın. Örneğin:

```bash
sort input.txt | uniq > output.txt
```

- Büyük/küçük harf duyarsız karşılaştırma yapmak istiyorsanız `-i` seçeneğini eklemeyi düşünün.
- Tekrar eden satırları görmek istiyorsanız `-d` seçeneğini kullanarak yalnızca tekrar eden satırları listeleyebilirsiniz.