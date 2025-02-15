# [리눅스] Bash arp 사용법

## Genel Bakış
`arp` komutu, bir ağda bulunan cihazların IP adresleri ile MAC adresleri arasındaki ilişkiyi yönetmek için kullanılır. Bu komut, özellikle yerel ağlarda, cihazların fiziksel adreslerini (MAC) öğrenmek ve bu adresleri IP adresleri ile eşleştirmek için önemlidir. `arp`, ağdaki cihazların iletişim kurmasını sağlamak için gerekli olan adres çözümleme işlemlerini gerçekleştirir.

## Kullanım
`arp` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
arp [seçenekler] [IP_adresi]
```

### Yaygın Seçenekler
- `-a`: Tüm ARP girişlerini listele.
- `-d`: Belirtilen IP adresine ait ARP girişini sil.
- `-s`: Belirtilen IP adresine MAC adresi ekle.

## Örnekler

### Tüm ARP Girişlerini Listeleme
Ağınızdaki tüm ARP girişlerini görüntülemek için aşağıdaki komutu kullanabilirsiniz:

```bash
arp -a
```

Bu komut, ağınızdaki cihazların IP ve MAC adreslerini listeleyecektir.

### ARP Girişini Silme
Belirli bir IP adresine ait ARP girişini silmek için şu komutu kullanabilirsiniz:

```bash
arp -d 192.168.1.10
```

Bu komut, `192.168.1.10` IP adresine ait ARP girişini ağdan kaldıracaktır.

## İpuçları
- ARP önbelleğini düzenli olarak kontrol etmek, ağınızdaki cihazların doğru şekilde iletişim kurmasını sağlamak için önemlidir.
- Ağda değişiklikler olduğunda (örneğin, yeni cihazlar eklendiğinde), ARP önbelleğini güncellemek için `arp -a` komutunu kullanarak mevcut durumu kontrol edin.
- Eğer bir cihazın MAC adresini değiştirdiyseniz, eski ARP girişinin silinmesi gerekebilir. Bu durumda `arp -d` komutunu kullanarak eski girişi kaldırın ve yeni MAC adresini ekleyin.