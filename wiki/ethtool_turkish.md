# [Linux] Bash ethtool Kullanımı: Ağ arayüzü bilgilerini görüntüleme ve yönetme

## Genel Bakış
`ethtool`, Linux tabanlı sistemlerde ağ arayüzlerinin özelliklerini ve durumunu görüntülemek ve yönetmek için kullanılan bir komuttur. Bu komut, ağ kartlarının yapılandırmasını ve performansını analiz etmek için oldukça faydalıdır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
ethtool [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-h`, `--help`: Yardım bilgilerini gösterir.
- `-s`, `--set-priv-flags`: Ağ arayüzünün özel bayraklarını ayarlamak için kullanılır.
- `-i`, `--driver`: Ağ arayüzü için sürücü bilgilerini gösterir.
- `-p`, `--identify`: Ağ arayüzünü tanımlamak için LED'i yakar.
- `-S`, `--statistics`: Ağ arayüzü istatistiklerini görüntüler.

## Yaygın Örnekler
Aşağıda `ethtool` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. Ağ arayüzü bilgilerini görüntüleme:
   ```bash
   ethtool eth0
   ```

2. Ağ arayüzü sürücüsü bilgilerini gösterme:
   ```bash
   ethtool -i eth0
   ```

3. Ağ arayüzü istatistiklerini görüntüleme:
   ```bash
   ethtool -S eth0
   ```

4. Ağ arayüzünü tanımlamak için LED'i yakma:
   ```bash
   ethtool -p eth0
   ```

## İpuçları
- `ethtool` komutunu kullanmadan önce, hangi ağ arayüzlerinin mevcut olduğunu görmek için `ip link show` komutunu kullanabilirsiniz.
- Ağ kartı ayarlarını değiştirmeden önce mevcut ayarları yedeklemek iyi bir uygulamadır.
- Ağ bağlantı sorunlarını gidermek için `ethtool` ile istatistikleri kontrol etmek, sorunun kaynağını bulmanıza yardımcı olabilir.