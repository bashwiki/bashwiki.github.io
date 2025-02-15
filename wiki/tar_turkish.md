# [리눅스] Bash tar 사용법

## Genel Bakış
`tar`, Unix ve Linux sistemlerinde dosyaları arşivlemek ve sıkıştırmak için kullanılan bir komut satırı aracıdır. "Tape Archive" kelimelerinin kısaltması olan `tar`, birden fazla dosyayı tek bir dosya halinde birleştirerek depolama ve taşıma işlemlerini kolaylaştırır. Genellikle yedekleme işlemleri için kullanılır ve arşiv dosyaları oluşturmanın yanı sıra, mevcut arşivleri açma ve içeriğini görüntüleme gibi işlevleri de destekler.

## Kullanım
`tar` komutunun temel sözdizimi şu şekildedir:

```bash
tar [seçenekler] [arşiv dosyası] [dosya veya dizin]
```

### Yaygın Seçenekler
- `-c`: Yeni bir arşiv oluşturur.
- `-x`: Mevcut bir arşivi açar.
- `-f`: Arşiv dosyasının adını belirtir.
- `-v`: İşlem sırasında ayrıntılı çıktı verir (verbose).
- `-z`: Arşivi gzip ile sıkıştırır veya açar.
- `-j`: Arşivi bzip2 ile sıkıştırır veya açar.

## Örnekler

### Arşiv Oluşturma
Aşağıdaki komut, `belgeler` dizinini `yedek.tar.gz` adlı bir arşiv dosyası olarak sıkıştırır:

```bash
tar -czvf yedek.tar.gz belgeler/
```

### Arşiv Açma
Aşağıdaki komut, `yedek.tar.gz` adlı arşiv dosyasını açar:

```bash
tar -xzvf yedek.tar.gz
```

## İpuçları
- Arşiv dosyalarını oluştururken, dosya ve dizin isimlerini tam olarak belirtmek, karmaşayı önler ve işlemin doğru bir şekilde gerçekleştirilmesini sağlar.
- `-v` seçeneğini kullanarak, hangi dosyaların arşivlendiğini veya açıldığını takip edebilirsiniz.
- Sıkıştırma seçenekleri (`-z` veya `-j`) kullanarak, arşiv dosyalarının boyutunu önemli ölçüde azaltabilirsiniz, bu da depolama alanından tasarruf sağlar.
- Arşivlerinizi düzenli olarak yedeklemek, veri kaybını önlemek için iyi bir uygulamadır.