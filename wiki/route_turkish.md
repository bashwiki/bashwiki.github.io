# [리눅스] Bash route 사용법

## Overview
`route` komutu, Linux ve Unix tabanlı işletim sistemlerinde ağ yönlendirme tablolarını görüntülemek ve yönetmek için kullanılır. Bu komut, sistemin hangi ağlara nasıl erişeceğini belirleyen yönlendirme kurallarını ayarlamak ve incelemek için önemli bir araçtır. Ağ yönlendirmesi, veri paketlerinin hedeflerine ulaşabilmesi için en uygun yolları belirler.

## Usage
`route` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
route [OPTION] [ARGUMENTS]
```

### Yaygın Seçenekler
- `-n`: IP adreslerini sayısal formatta gösterir, isim çözümlemesi yapmaz.
- `add`: Yeni bir yönlendirme kuralı ekler.
- `del`: Mevcut bir yönlendirme kuralını siler.
- `-e`: Yönlendirme tablosunu detaylı bir şekilde gösterir.

## Examples
### Örnek 1: Yönlendirme Tablosunu Görüntüleme
Ağ yönlendirme tablonuzu görüntülemek için aşağıdaki komutu kullanabilirsiniz:

```bash
route -n
```

Bu komut, yönlendirme tablonuzdaki tüm girişleri sayısal IP adresleriyle birlikte listeleyecektir.

### Örnek 2: Yeni Bir Yönlendirme Kuralı Ekleme
Ağınıza yeni bir yönlendirme kuralı eklemek için şu komutu kullanabilirsiniz:

```bash
route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1
```

Bu komut, 192.168.1.0/24 ağı için 192.168.1.1 geçiş noktasını belirler.

## Tips
- `route` komutunu kullanmadan önce, ağ yapılandırmanızı ve mevcut yönlendirme kurallarınızı iyice anlamak önemlidir.
- Yönlendirme değişiklikleri yapmadan önce mevcut yönlendirme tablonuzun bir yedeğini almak iyi bir uygulamadır.
- `route` komutunun bazı sistemlerde `ip route` komutuyla değiştirilmiş olabileceğini unutmayın; bu nedenle, sisteminizde hangi komutun kullanılacağını kontrol edin.