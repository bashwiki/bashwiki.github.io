# [Linux] Bash ip Kullanımı: Ağ yapılandırmalarını yönetme

## Genel Bakış
`ip` komutu, Linux tabanlı işletim sistemlerinde ağ yapılandırmalarını yönetmek için kullanılan bir araçtır. Ağ arayüzlerini, yönlendirme tablolarını ve diğer ağ parametrelerini görüntülemek ve değiştirmek için kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
ip [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `link`: Ağ arayüzlerini yönetmek için kullanılır.
- `addr`: IP adreslerini görüntülemek veya ayarlamak için kullanılır.
- `route`: Yönlendirme tablolarını görüntülemek veya değiştirmek için kullanılır.
- `neigh`: Yakınlık tablosunu yönetmek için kullanılır.

## Yaygın Örnekler
Aşağıda `ip` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### 1. Ağ Arayüzlerini Listeleme
Ağ arayüzlerinin durumunu görüntülemek için:
```bash
ip link show
```

### 2. IP Adresi Ekleme
Bir ağ arayüzüne IP adresi eklemek için:
```bash
ip addr add 192.168.1.10/24 dev eth0
```

### 3. IP Adresi Silme
Bir ağ arayüzünden IP adresini silmek için:
```bash
ip addr del 192.168.1.10/24 dev eth0
```

### 4. Yönlendirme Tablosunu Görüntüleme
Yönlendirme tablosunu görüntülemek için:
```bash
ip route show
```

### 5. Yeni Bir Yönlendirme Eklemek
Yeni bir yönlendirme eklemek için:
```bash
ip route add 10.0.0.0/8 via 192.168.1.1
```

## İpuçları
- `ip` komutunu kullanmadan önce, ağ arayüzlerinizin ve IP adreslerinizin doğru olduğundan emin olun.
- Değişiklik yapmadan önce mevcut ayarları yedeklemek iyi bir uygulamadır.
- `ip` komutunu kullanırken, genellikle `sudo` ile çalıştırmak gerekebilir, çünkü ağ ayarlarını değiştirmek için yönetici yetkileri gereklidir.