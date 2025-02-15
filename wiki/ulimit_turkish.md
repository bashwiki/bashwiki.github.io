# [리눅스] Bash ulimit 사용법

## Overview
`ulimit` komutu, bir shell oturumu için sistem kaynaklarının sınırlarını belirlemeye yarar. Bu sınırlar, bir kullanıcı veya bir süreç tarafından kullanılabilecek kaynak miktarını kontrol eder. `ulimit`, özellikle sistem performansını optimize etmek ve kaynak tüketimini yönetmek için kullanılır. Bu komut, bellek kullanımı, dosya boyutları ve işlem sayısı gibi çeşitli kaynakları sınırlamak için kullanılabilir.

## Usage
`ulimit` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
ulimit [option] [limit]
```

### Yaygın Seçenekler
- `-a`: Tüm mevcut sınırları gösterir.
- `-c`: Çekirdek dosyası boyutunu ayarlar.
- `-d`: Veri segmenti boyutunu ayarlar.
- `-f`: Dosya boyutu sınırını ayarlar.
- `-l`: Kilitlenmiş bellek boyutunu ayarlar.
- `-m`: Fiziksel bellek boyutunu ayarlar.
- `-n`: Açık dosya sayısını ayarlar.
- `-s`: Yığın boyutunu ayarlar.
- `-t`: İşlem süresi sınırını ayarlar.
- `-u`: Kullanıcı başına maksimum işlem sayısını ayarlar.
- `-v`: Sanal bellek boyutunu ayarlar.

## Examples
### Örnek 1: Açık Dosya Sayısını Görüntüleme
Açık dosya sayısını görüntülemek için aşağıdaki komutu kullanabilirsiniz:

```bash
ulimit -n
```

Bu komut, mevcut shell oturumu için izin verilen maksimum açık dosya sayısını gösterir.

### Örnek 2: Maksimum Açık Dosya Sayısını Ayarlama
Maksimum açık dosya sayısını 1024 olarak ayarlamak için şu komutu kullanabilirsiniz:

```bash
ulimit -n 1024
```

Bu komut, mevcut shell oturumu için açık dosya sayısını 1024 ile sınırlar.

## Tips
- `ulimit` ayarları, yalnızca mevcut shell oturumu için geçerlidir. Shell kapatıldığında ayarlar kaybolur. Kalıcı değişiklikler yapmak için, genellikle `~/.bashrc` veya `~/.bash_profile` dosyasına eklemeler yapmanız gerekir.
- Sınırları artırmadan önce, sistem kaynaklarınızı göz önünde bulundurun. Aşırı kaynak kullanımı, sistemin dengesiz çalışmasına neden olabilir.
- `ulimit -a` komutunu kullanarak mevcut tüm sınırları kontrol etmek, hangi kaynakların sınırlandırıldığını anlamanıza yardımcı olabilir.