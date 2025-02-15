# [리눅스] Bash xz 사용법

## Overview
`xz`, dosya sıkıştırma ve açma işlemleri için kullanılan bir komut satırı aracıdır. Genellikle yüksek sıkıştırma oranları sunan LZMA (Lempel-Ziv-Markov chain algorithm) algoritmasını kullanarak dosyaları sıkıştırır. `xz`, özellikle büyük dosyaların depolanması ve aktarılması sırasında yer tasarrufu sağlamak amacıyla tercih edilir.

## Usage
`xz` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
xz [seçenekler] [dosya_adı]
```

### Yaygın Seçenekler
- `-d` veya `--decompress`: Sıkıştırılmış bir dosyayı açar.
- `-k` veya `--keep`: Sıkıştırma işlemi sırasında orijinal dosyayı korur.
- `-v` veya `--verbose`: İşlem sırasında daha fazla bilgi verir.
- `-9`: Maksimum sıkıştırma seviyesini kullanır (1-9 arasında bir değer alabilir, 9 en yüksek sıkıştırmadır).

## Examples
### Örnek 1: Dosya Sıkıştırma
Bir dosyayı sıkıştırmak için `xz` komutunu kullanabilirsiniz:

```bash
xz dosya.txt
```
Bu komut, `dosya.txt` dosyasını sıkıştırır ve `dosya.txt.xz` adında bir dosya oluşturur.

### Örnek 2: Dosya Açma
Sıkıştırılmış bir dosyayı açmak için `-d` seçeneğini kullanabilirsiniz:

```bash
xz -d dosya.txt.xz
```
Bu komut, `dosya.txt.xz` dosyasını açar ve orijinal `dosya.txt` dosyasını geri getirir.

## Tips
- Sıkıştırma işlemi sırasında orijinal dosyayı korumak istiyorsanız `-k` seçeneğini kullanmayı unutmayın.
- Büyük dosyalarla çalışırken, sıkıştırma süresinin uzayabileceğini göz önünde bulundurun. Gerekirse `-1` ile `-9` arasında bir sıkıştırma seviyesi seçerek işlem süresini optimize edebilirsiniz.
- `-v` seçeneği ile işlem sırasında ilerlemeyi takip edebilir, sıkıştırma işleminin ne kadar sürdüğünü görebilirsiniz.