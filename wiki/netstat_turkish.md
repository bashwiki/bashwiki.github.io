# [Linux] Bash netstat Kullanımı: Ağ bağlantılarını görüntüleme

## Genel Bakış
`netstat` komutu, ağ bağlantılarını, yönlendirme tablolarını, arayüz istatistiklerini ve diğer ağ ile ilgili bilgileri görüntülemek için kullanılır. Bu komut, sistem yöneticileri ve ağ uzmanları için ağ durumu hakkında bilgi edinmek amacıyla oldukça faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:

```
netstat [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-a`: Tüm bağlantıları ve dinleme soketlerini gösterir.
- `-t`: TCP bağlantılarını gösterir.
- `-u`: UDP bağlantılarını gösterir.
- `-n`: Adresleri ve port numaralarını sayısal olarak gösterir.
- `-l`: Sadece dinleme durumundaki soketleri gösterir.
- `-p`: Bağlantıların hangi süreç tarafından kullanıldığını gösterir.

## Yaygın Örnekler
Aşağıda `netstat` komutunun bazı pratik kullanımları verilmiştir:

### Tüm Ağ Bağlantılarını Gösterme
```
netstat -a
```

### Sadece TCP Bağlantılarını Görüntüleme
```
netstat -t
```

### UDP Bağlantılarını Listeleme
```
netstat -u
```

### Dinleme Durumundaki Soketleri Gösterme
```
netstat -l
```

### Bağlantıları Sayısal Olarak Gösterme
```
netstat -n
```

### Belirli Bir Süreçle İlişkili Bağlantıları Görüntüleme
```
netstat -p
```

## İpuçları
- `netstat` komutunu `grep` ile birleştirerek belirli bir port veya IP adresi için filtreleme yapabilirsiniz. Örneğin: 
  ```
  netstat -an | grep 80
  ```
- Ağ sorunlarını teşhis etmek için `netstat` çıktısını düzenli olarak kontrol edin.
- `netstat` komutunun çıktısını daha okunabilir hale getirmek için `column` komutunu kullanabilirsiniz:
  ```
  netstat -tuln | column -t
  ``` 

Bu bilgilerle `netstat` komutunu etkili bir şekilde kullanarak ağ bağlantılarınızı izleyebilir ve yönetebilirsiniz.