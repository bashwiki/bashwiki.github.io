# [Linux] Bash arp Kullanımı: Ağdaki IP adreslerini ve MAC adreslerini görüntüleme

## Genel Bakış
`arp` komutu, bir ağdaki IP adresleri ile MAC adresleri arasındaki ilişkiyi görüntülemek ve yönetmek için kullanılır. Bu komut, özellikle yerel ağda cihazların iletişim kurmasını sağlamak için önemlidir.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
arp [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-a`: Tüm ARP girişlerini görüntüler.
- `-d`: Belirtilen IP adresine ait ARP girişini siler.
- `-s`: Belirtilen IP adresi için yeni bir ARP girişi ekler.
- `-n`: IP adreslerini çözümlemeden gösterir.

## Yaygın Örnekler
Aşağıda `arp` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### Tüm ARP Girişlerini Görüntüleme
```bash
arp -a
```

### Belirli Bir IP Adresinin ARP Girişini Silme
```bash
arp -d 192.168.1.10
```

### Yeni Bir ARP Girişi Ekleme
```bash
arp -s 192.168.1.20 00:11:22:33:44:55
```

### IP Adreslerini Çözümlemeden Görüntüleme
```bash
arp -n
```

## İpuçları
- ARP tablosunu düzenli olarak kontrol etmek, ağdaki cihazların durumunu anlamanıza yardımcı olabilir.
- Ağda sorun giderirken, ARP girişlerini silmek bazen bağlantı problemlerini çözebilir.
- Güvenlik nedeniyle, yalnızca güvenilir cihazların ARP girişlerini eklemeye dikkat edin.