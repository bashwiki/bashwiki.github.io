# [리눅스] Bash cp 사용법

## Overview
`cp` komutu, Unix ve Linux işletim sistemlerinde dosyaları ve dizinleri kopyalamak için kullanılan bir komuttur. Bu komut, kaynak dosyaların veya dizinlerin bir kopyasını belirtilen hedef konumda oluşturur. `cp` komutu, dosya yönetimi ve yedekleme işlemleri için oldukça yaygın bir şekilde kullanılır.

## Usage
`cp` komutunun temel sözdizimi aşağıdaki gibidir:

```
cp [seçenekler] kaynak hedef
```

### Yaygın Seçenekler
- `-r` veya `--recursive`: Dizinleri ve içindeki tüm dosyaları kopyalamak için kullanılır.
- `-i` veya `--interactive`: Hedef dosya zaten varsa, üzerine yazmadan önce kullanıcıdan onay alır.
- `-u` veya `--update`: Sadece kaynak dosya hedef dosyadan daha yeni ise kopyalama işlemi gerçekleştirir.
- `-v` veya `--verbose`: Kopyalama işlemi sırasında hangi dosyaların kopyalandığını gösterir.

## Examples
### Örnek 1: Basit Dosya Kopyalama
Aşağıdaki komut, `dosya.txt` adlı dosyayı `yeni_dosya.txt` olarak kopyalar:

```bash
cp dosya.txt yeni_dosya.txt
```

### Örnek 2: Dizin Kopyalama
Aşağıdaki komut, `dizin` adlı dizini ve içindeki tüm dosyaları `yeni_dizin` adlı yeni bir dizine kopyalar:

```bash
cp -r dizin yeni_dizin
```

## Tips
- Kopyalama işlemi sırasında dosya adlarının çakışmasını önlemek için `-i` seçeneğini kullanarak, mevcut dosyaların üzerine yazmadan önce onay alabilirsiniz.
- `-v` seçeneği ile kopyalama işlemi sırasında hangi dosyaların kopyalandığını görebilir, bu da hata ayıklama sürecinde faydalı olabilir.
- Büyük dosya veya dizinleri kopyalarken, işlemin tamamlanmasını beklemek için sabırlı olun; büyük veriler zaman alabilir.