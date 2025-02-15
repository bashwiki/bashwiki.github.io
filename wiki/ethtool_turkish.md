# [리눅스] Bash ethtool 사용법

## Genel Bakış
`ethtool`, Linux tabanlı işletim sistemlerinde ağ arayüzlerinin özelliklerini görüntülemek ve yapılandırmak için kullanılan bir komuttur. Bu araç, ağ kartlarının durumunu kontrol etmek, hız ve duplex ayarlarını değiştirmek, hata istatistiklerini görüntülemek ve daha fazlasını yapmak için kullanılır. Genellikle ağ yöneticileri ve sistem yöneticileri tarafından ağ bağlantılarının performansını optimize etmek amacıyla tercih edilir.

## Kullanım
`ethtool` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
ethtool [seçenekler] [ağ arayüzü]
```

### Yaygın Seçenekler
- `-s`: Ağ arayüzünü yapılandırmak için kullanılır. Örneğin, hız ve duplex ayarlarını değiştirmek için.
- `-i`: Ağ arayüzü hakkında bilgi görüntüler (sürücü adı, sürüm, vb.).
- `-p`: Ağ arayüzünü geçici olarak yanıp söndürerek tanımlamak için kullanılır.
- `-d`: Ağ arayüzünün hata ayıklama bilgilerini görüntüler.
- `-a`: Ağ arayüzünün tüm özelliklerini ve ayarlarını listeler.

## Örnekler

### Örnek 1: Ağ Arayüzü Bilgilerini Görüntüleme
Ağ arayüzünüz hakkında bilgi almak için aşağıdaki komutu kullanabilirsiniz:

```bash
ethtool -i eth0
```

Bu komut, `eth0` arayüzü için sürücü adı, sürüm ve diğer ilgili bilgileri görüntüler.

### Örnek 2: Ağ Arayüzü Hızını ve Duplex Ayarını Değiştirme
Ağ arayüzünüzün hızını 1000 Mbps ve duplex modunu tam olarak ayarlamak için şu komutu kullanabilirsiniz:

```bash
ethtool -s eth0 speed 1000 duplex full
```

Bu komut, `eth0` arayüzünün hızını 1000 Mbps olarak ayarlayacak ve tam duplex modunu etkinleştirecektir.

## İpuçları
- `ethtool` komutunu kullanmadan önce, ağ arayüzünüzün adını doğru bir şekilde bildiğinizden emin olun. Ağ arayüzü adlarını görüntülemek için `ip link` veya `ifconfig` komutlarını kullanabilirsiniz.
- Ağ ayarlarını değiştirmeden önce mevcut ayarları yedeklemek iyi bir uygulamadır. Böylece, istenmeyen bir durumla karşılaşırsanız kolayca geri dönebilirsiniz.
- Ağ arayüzü üzerinde yapılan değişikliklerin kalıcı olması için, ilgili yapılandırma dosyalarını güncellemeyi unutmayın. Aksi takdirde, sistem yeniden başlatıldığında ayarlar kaybolabilir.