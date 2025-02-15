# [리눅스] Bash gzip 사용법

## Overview
`gzip`, GNU Zip'in kısaltmasıdır ve dosyaları sıkıştırmak için kullanılan bir komut satırı aracıdır. Genellikle dosyaların boyutunu küçültmek ve depolama alanından tasarruf sağlamak amacıyla kullanılır. `gzip`, özellikle metin dosyaları için etkili bir sıkıştırma sağlar ve genellikle `.gz` uzantılı dosyalar oluşturur.

## Usage
`gzip` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
gzip [seçenekler] [dosya_adı]
```

### Yaygın Seçenekler:
- `-d` veya `--decompress`: Sıkıştırılmış bir dosyayı açar.
- `-k` veya `--keep`: Sıkıştırma işlemi sırasında orijinal dosyayı korur.
- `-v` veya `--verbose`: Sıkıştırma işlemi hakkında daha fazla bilgi verir.
- `-r` veya `--recursive`: Belirtilen dizindeki tüm dosyaları ve alt dizinleri sıkıştırır.

## Examples
### Örnek 1: Basit Sıkıştırma
Bir dosyayı sıkıştırmak için `gzip` komutunu aşağıdaki gibi kullanabilirsiniz:

```bash
gzip dosya.txt
```
Bu komut, `dosya.txt` dosyasını sıkıştırır ve `dosya.txt.gz` adında yeni bir dosya oluşturur.

### Örnek 2: Sıkıştırılmış Dosyayı Açma
Sıkıştırılmış bir dosyayı açmak için `-d` seçeneğini kullanabilirsiniz:

```bash
gzip -d dosya.txt.gz
```
Bu komut, `dosya.txt.gz` dosyasını açar ve orijinal `dosya.txt` dosyasını geri getirir.

## Tips
- Sıkıştırma işlemi sırasında dosyaların kaybolmaması için `-k` seçeneğini kullanarak orijinal dosyaları koruyabilirsiniz.
- Büyük dosyalarla çalışırken, sıkıştırma işleminin zaman alabileceğini unutmayın. Bu nedenle, sıkıştırma işlemini arka planda çalıştırmak için `&` operatörünü kullanabilirsiniz.
- Sıkıştırılmış dosyaların boyutunu kontrol etmek için `-v` seçeneğini kullanarak sıkıştırma işlemi hakkında bilgi alabilirsiniz.