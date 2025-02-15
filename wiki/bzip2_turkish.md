# [리눅스] Bash bzip2 사용법

## Overview
`bzip2`, dosya sıkıştırma için kullanılan bir komut satırı aracıdır. Genellikle büyük dosyaları daha küçük boyutlara sıkıştırmak için kullanılır ve bu sayede depolama alanından tasarruf sağlanır. `bzip2`, yüksek sıkıştırma oranları sunarak, verilerin daha az yer kaplamasını sağlar. Sıkıştırılmış dosyalar genellikle `.bz2` uzantısına sahiptir.

## Usage
`bzip2` komutunun temel sözdizimi şu şekildedir:

```bash
bzip2 [seçenekler] [dosya_adı]
```

### Yaygın Seçenekler
- `-d`, `--decompress`: Sıkıştırılmış bir dosyayı açar.
- `-k`, `--keep`: Orijinal dosyayı saklayarak sıkıştırma işlemi yapar.
- `-f`, `--force`: Zaten var olan dosyaların üzerine yazmak için zorlar.
- `-v`, `--verbose`: Sıkıştırma işlemi sırasında detaylı bilgi verir.

## Examples
### Örnek 1: Dosya Sıkıştırma
Bir dosyayı sıkıştırmak için `bzip2` komutunu şu şekilde kullanabilirsiniz:

```bash
bzip2 dosya.txt
```
Bu komut, `dosya.txt` dosyasını sıkıştırarak `dosya.txt.bz2` adında yeni bir dosya oluşturur.

### Örnek 2: Sıkıştırılmış Dosyayı Açma
Sıkıştırılmış bir dosyayı açmak için `-d` seçeneğini kullanabilirsiniz:

```bash
bzip2 -d dosya.txt.bz2
```
Bu komut, `dosya.txt.bz2` dosyasını açarak orijinal `dosya.txt` dosyasını geri getirir.

## Tips
- Sıkıştırma işlemi sırasında dosyaların boyutunu kontrol etmek için `-v` seçeneğini kullanarak işlem hakkında daha fazla bilgi alabilirsiniz.
- Büyük dosyalarla çalışırken, sıkıştırma işlemi zaman alabilir. Bu nedenle, sıkıştırma işlemini arka planda çalıştırmak için `&` operatörünü kullanabilirsiniz.
- `-k` seçeneği ile orijinal dosyayı koruyarak hem sıkıştırılmış hem de orijinal dosyaya sahip olabilirsiniz. Bu, verilerinizi kaybetmemek için iyi bir uygulamadır.