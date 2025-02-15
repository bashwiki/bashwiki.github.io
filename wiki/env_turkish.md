# [리눅스] Bash env 사용법

## Overview
`env` komutu, mevcut ortam değişkenlerini görüntülemek veya yeni bir ortam değişkeni ile bir komut çalıştırmak için kullanılan bir Bash komutudur. Genellikle, bir programın hangi ortamda çalıştığını anlamak veya belirli bir ortam değişkeni ayarlayarak bir komutu çalıştırmak için kullanılır.

## Usage
Temel `env` komutunun sözdizimi aşağıdaki gibidir:

```bash
env [SEÇENEKLER] [ORTAM_DEĞİŞKENİ=DEĞER] [KOMUT]
```

### Yaygın Seçenekler
- `-i` veya `--ignore-environment`: Mevcut ortam değişkenlerini yoksayarak temiz bir ortamda komut çalıştırır.
- `-0` veya `--null`: Çıktıyı null karakter ile ayırır. Bu, özellikle dosya isimleri içeren çıktılar için kullanışlıdır.

## Examples
### Örnek 1: Mevcut Ortam Değişkenlerini Görüntüleme
Aşağıdaki komut, mevcut ortam değişkenlerini listeleyecektir:

```bash
env
```

### Örnek 2: Yeni Bir Ortam Değişkeni ile Komut Çalıştırma
Aşağıdaki komut, `MY_VAR` adında bir ortam değişkeni oluşturarak `printenv` komutunu çalıştırır:

```bash
env MY_VAR=HelloWorld printenv MY_VAR
```

Bu komutun çıktısı `HelloWorld` olacaktır.

## Tips
- `env` komutunu, bir komutun hangi ortamda çalıştığını test etmek için kullanabilirsiniz. Bu, özellikle farklı ortam değişkenleri ile uygulamaları denemek için faydalıdır.
- Ortam değişkenlerini ayarlarken, komutun yalnızca o komut için geçerli olacağını unutmayın. Komut tamamlandığında, ayarladığınız ortam değişkeni kaybolur.