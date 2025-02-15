# [리눅스] Bash free 사용법

## Overview
`free` komutu, Linux sistemlerde bellek (RAM) kullanımını görüntülemek için kullanılan bir araçtır. Bu komut, sistemdeki toplam bellek, kullanılan bellek, boş bellek ve tampon/bellek önbelleği gibi bilgileri sağlar. Geliştiriciler ve sistem yöneticileri, bellek kullanımını izlemek ve sistem performansını değerlendirmek için bu komutu sıklıkla kullanır.

## Usage
`free` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
free [seçenekler]
```

### Yaygın Seçenekler
- `-h`: Bellek değerlerini insan tarafından okunabilir formatta (KB, MB, GB) gösterir.
- `-m`: Bellek değerlerini megabayt cinsinden gösterir.
- `-g`: Bellek değerlerini gigabayt cinsinden gösterir.
- `-s [saniye]`: Belirtilen saniye aralıklarıyla sürekli olarak bellek bilgilerini günceller.
- `-t`: Toplam bellek kullanımını gösterir.

## Examples
### Örnek 1: Temel Kullanım
Aşağıdaki komut, sistemdeki bellek kullanımını varsayılan formatta gösterir:

```bash
free
```

### Örnek 2: İnsan Tarafından Okunabilir Format
Aşağıdaki komut, bellek kullanımını insan tarafından okunabilir formatta görüntüler:

```bash
free -h
```

## Tips
- `free` komutunu sık sık kullanarak bellek kullanımını izlemek, sistem performansını optimize etmek için faydalıdır.
- `free -s 5` komutunu kullanarak her 5 saniyede bir bellek kullanımını güncelleyebilirsiniz. Bu, bellek kullanımındaki değişiklikleri anlık olarak takip etmenize yardımcı olur.
- `free` komutunu `watch` komutuyla birleştirerek sürekli güncellenen bir bellek durumu görüntüleyebilirsiniz:

```bash
watch free -h
```

Bu, bellek kullanımını gerçek zamanlı olarak izlemenizi sağlar.