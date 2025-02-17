# [Linux] Bash docker kullanımı: Docker konteynerlerini yönetmek için bir araç

## Genel Bakış
Docker, uygulamaları ve hizmetleri konteynerler içinde çalıştırmak için kullanılan bir platformdur. Konteynerler, uygulamaların bağımlılıklarıyla birlikte izole bir ortamda çalışmasını sağlar, böylece taşınabilirlik ve ölçeklenebilirlik sunar.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
docker [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `run`: Yeni bir konteyner başlatır.
- `ps`: Çalışan konteynerleri listeler.
- `stop`: Çalışan bir konteyneri durdurur.
- `rm`: Bir konteyneri siler.
- `images`: Mevcut Docker imajlarını listeler.

## Yaygın Örnekler
Aşağıda, Docker komutlarının bazı pratik örnekleri bulunmaktadır:

### Yeni Bir Konteyner Başlatma
```bash
docker run -d --name my_container nginx
```
Bu komut, arka planda (`-d` seçeneği ile) yeni bir Nginx konteyneri başlatır.

### Çalışan Konteynerleri Listeleme
```bash
docker ps
```
Bu komut, o anda çalışan tüm konteynerleri listeler.

### Bir Konteyneri Durdurma
```bash
docker stop my_container
```
Bu komut, `my_container` adındaki konteyneri durdurur.

### Bir Konteyneri Silme
```bash
docker rm my_container
```
Bu komut, durdurulmuş olan `my_container` konteynerini siler.

### Mevcut İmajları Listeleme
```bash
docker images
```
Bu komut, sistemde mevcut olan Docker imajlarını listeler.

## İpuçları
- Konteynerlerinizi düzenli olarak temizleyin. Kullanmadığınız konteynerleri silmek, sistem kaynaklarınızı korumanıza yardımcı olur.
- Docker imajlarını güncel tutun. Güvenlik açıklarını önlemek için imajlarınızı düzenli olarak güncelleyin.
- `docker-compose` kullanarak birden fazla konteyneri kolayca yönetebilirsiniz. Bu, uygulama mimarinizin karmaşıklığını azaltır.