# [리눅스] Bash rev 사용법

## Overview
`rev` komutu, bir dosyadaki veya standart girişteki her bir satırın karakterlerini tersine çevirerek çıktı verir. Bu, metin verilerini ters sırada görüntülemek için kullanışlıdır. Genellikle metin işleme ve veri analizi gibi durumlarda, belirli bir formatta verileri düzenlemek için tercih edilir.

## Usage
Temel kullanım şekli aşağıdaki gibidir:

```bash
rev [dosya_adı]
```

### Ortak Seçenekler
- `-` veya `--` ile başlayan seçenekler yoktur. `rev` komutu, yalnızca dosya adı veya standart giriş alır.

## Examples
### Örnek 1: Dosyadaki Satırları Ters Çevirme
Aşağıdaki komut, `metin.txt` dosyasındaki her bir satırın karakterlerini tersine çevirir:

```bash
rev metin.txt
```

### Örnek 2: Standart Girişten Veri Ters Çevirme
Aşağıdaki komut, kullanıcıdan alınan girişi tersine çevirir. Kullanıcı "merhaba" yazıp Enter tuşuna bastığında, çıktı "abahrem" olacaktır:

```bash
echo "merhaba" | rev
```

## Tips
- `rev` komutunu, diğer metin işleme komutlarıyla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz. Örneğin, `cat` komutuyla birlikte kullanarak bir dosyanın içeriğini tersine çevirebilirsiniz.
- Büyük dosyalarla çalışırken, `rev` komutunun çıktısını bir dosyaya yönlendirmek, sonuçları daha sonra incelemek için faydalı olabilir:

```bash
rev metin.txt > ters_metin.txt
```

Bu şekilde, `metin.txt` dosyasındaki her bir satırın ters çevrilmiş hali `ters_metin.txt` dosyasına kaydedilir.