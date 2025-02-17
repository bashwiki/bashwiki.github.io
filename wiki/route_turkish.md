# [Linux] Bash route kullanımı: Ağ yönlendirme tablolarını görüntüleme ve yönetme

## Overview
`route` komutu, Linux sistemlerinde ağ yönlendirme tablolarını görüntülemek ve yönetmek için kullanılır. Bu komut, sistemin hangi ağlara nasıl ulaşacağını belirleyen yönlendirme bilgilerini gösterir ve gerektiğinde bu bilgileri değiştirmeye olanak tanır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```
route [options] [arguments]
```

## Common Options
- `-n`: IP adreslerini ve ağları sayısal olarak gösterir, isim çözümlemesi yapmaz.
- `add`: Yeni bir yönlendirme ekler.
- `del`: Mevcut bir yönlendirmeyi siler.
- `-e`: Yönlendirme tablosunu detaylı bir şekilde gösterir.

## Common Examples
Aşağıda `route` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. **Yönlendirme tablosunu görüntüleme:**
   ```bash
   route -n
   ```

2. **Yeni bir yönlendirme ekleme:**
   ```bash
   route add -net 192.168.1.0/24 gw 192.168.1.1
   ```

3. **Bir yönlendirmeyi silme:**
   ```bash
   route del -net 192.168.1.0/24
   ```

4. **Detaylı yönlendirme tablosunu görüntüleme:**
   ```bash
   route -e
   ```

## Tips
- Yönlendirme tablolarını değiştirmeden önce mevcut ayarları yedeklemek iyi bir uygulamadır.
- `route` komutunu kullanmadan önce, sisteminizdeki ağ yapılandırmasını anlamak için `ifconfig` veya `ip a` komutlarını kullanabilirsiniz.
- Ağ ayarlarını değiştirmek için genellikle yönetici (root) yetkilerine ihtiyaç duyarsınız; bu nedenle komutları `sudo` ile çalıştırmayı unutmayın.