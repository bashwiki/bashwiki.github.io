# [리눅스] Bash ip 사용법

## Genel Bakış
`ip` komutu, Linux işletim sistemlerinde ağ yapılandırmasını yönetmek için kullanılan güçlü bir araçtır. Ağ arayüzlerini, yönlendirme tablolarını, tünelleri ve diğer ağ bileşenlerini görüntülemek ve yönetmek için kullanılır. `ip` komutu, `ifconfig` ve `route` gibi eski komutların yerini almış ve daha kapsamlı bir ağ yönetimi deneyimi sunmaktadır.

## Kullanım
Temel sözdizimi şu şekildedir:

```
ip [seçenekler] [nesne] [eylem] [parametreler]
```

Burada:
- **seçenekler**: Komutun davranışını değiştiren opsiyonlardır.
- **nesne**: Yönetmek istediğiniz ağ bileşenidir (örneğin, `link`, `addr`, `route`, vb.).
- **eylem**: Gerçekleştirmek istediğiniz işlemdir (örneğin, `show`, `add`, `del`, vb.).
- **parametreler**: Eylem için gerekli olan ek bilgilerdir.

### Yaygın Seçenekler
- `link`: Ağ arayüzlerini yönetmek için kullanılır.
- `addr`: IP adreslerini yönetmek için kullanılır.
- `route`: Yönlendirme tablolarını görüntülemek veya değiştirmek için kullanılır.

## Örnekler

### Örnek 1: Ağ Arayüzlerini Görüntüleme
Ağ arayüzlerinin durumunu görmek için aşağıdaki komutu kullanabilirsiniz:

```bash
ip link show
```

Bu komut, sistemdeki tüm ağ arayüzlerini ve durumlarını listeleyecektir.

### Örnek 2: IP Adresi Ekleme
Bir ağ arayüzüne yeni bir IP adresi eklemek için şu komutu kullanabilirsiniz:

```bash
ip addr add 192.168.1.100/24 dev eth0
```

Bu komut, `eth0` arayüzüne `192.168.1.100` IP adresini ekleyecektir.

## İpuçları
- `ip` komutunu kullanmadan önce, hangi ağ arayüzlerinin mevcut olduğunu görmek için `ip link show` komutunu çalıştırarak başlayabilirsiniz.
- `ip` komutunun sunduğu geniş seçenek yelpazesini keşfetmek için `man ip` komutunu kullanarak kılavuz sayfalarını inceleyebilirsiniz.
- Ağ yapılandırmalarınızı değiştirmeden önce mevcut yapılandırmanızı yedeklemek iyi bir uygulamadır. Bu, yanlış bir yapılandırma durumunda geri dönmenizi kolaylaştırır.

`ip` komutu, ağ yönetimi için vazgeçilmez bir araçtır ve doğru kullanıldığında sistem yöneticileri ve geliştiriciler için büyük kolaylık sağlar.