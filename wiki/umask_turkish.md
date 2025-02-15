# [리눅스] Bash umask 사용법

## Genel Bakış
`umask`, Unix ve Linux sistemlerinde dosya ve dizinlerin varsayılan izinlerini belirlemek için kullanılan bir komuttur. Bu komut, yeni oluşturulan dosya ve dizinlerin sahiplik izinlerini kontrol eder. `umask` değeri, dosya izinlerini kısıtlamak için kullanılır ve bu sayede güvenlik sağlanır. Örneğin, bir dosya oluşturulduğunda, sistemin belirlediği varsayılan izinler `umask` değeri ile değiştirilir.

## Kullanım
Temel `umask` komutunun sözdizimi aşağıdaki gibidir:

```bash
umask [seçenekler] [değer]
```

- **değer**: `umask` değeri, genellikle üç veya dört basamaklı bir oktal sayı olarak belirtilir. Bu değer, yeni dosya ve dizinlerin varsayılan izinlerini belirler.
- **seçenekler**: `-S` seçeneği ile mevcut `umask` değerini sembolik olarak görüntüleyebilirsiniz.

## Örnekler
### Örnek 1: Mevcut umask değerini görüntüleme
Aşağıdaki komut, mevcut `umask` değerini gösterir:

```bash
umask
```

Bu komut, örneğin `0022` gibi bir çıktı verebilir. Bu, yeni dosyaların varsayılan olarak `rw-r--r--` (644) ve dizinlerin `rwxr-xr-x` (755) izinlerine sahip olacağı anlamına gelir.

### Örnek 2: Yeni umask değeri ayarlama
Aşağıdaki komut, yeni bir `umask` değeri ayarlamak için kullanılır:

```bash
umask 007
```

Bu komut, yeni oluşturulan dosyaların varsayılan izinlerini `rw-r-----` (640) ve dizinlerin `rwxr-x---` (750) olarak ayarlayacaktır.

## İpuçları
- `umask` değerini ayarlarken, izinlerin doğru bir şekilde ayarlandığından emin olun. Yanlış bir `umask` değeri, dosyalarınıza istenmeyen erişim kısıtlamaları getirebilir.
- `umask` ayarlarını kalıcı hale getirmek için, bu komutu kullanıcı profil dosyalarınıza (örneğin, `~/.bashrc` veya `~/.bash_profile`) ekleyebilirsiniz.
- `umask` değerini ayarlarken, her zaman izinlerin toplamının 777'yi geçmemesine dikkat edin. Örneğin, `umask 002` kullanıldığında, yeni dosyaların izinleri 664 olacaktır (666 - 002 = 664).

Bu bilgilerle, `umask` komutunu etkili bir şekilde kullanarak dosya ve dizin izinlerinizi yönetebilirsiniz.