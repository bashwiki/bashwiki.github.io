# [리눅스] Bash systemctl 사용법

## Overview
`systemctl`, Linux sistemlerinde sistem ve hizmet yöneticisi olan `systemd` ile etkileşim kurmak için kullanılan bir komuttur. Bu komut, sistem servislerini başlatmak, durdurmak, yeniden başlatmak, durumlarını kontrol etmek ve sistemin genel durumunu yönetmek için kullanılır. `systemctl`, sistem yöneticilerine ve geliştiricilere, sistem bileşenlerini etkili bir şekilde yönetme yeteneği sağlar.

## Usage
Temel `systemctl` komutunun sözdizimi şu şekildedir:

```bash
systemctl [OPTIONS] COMMAND [NAME]
```

### Yaygın Seçenekler
- `start`: Belirtilen hizmeti başlatır.
- `stop`: Belirtilen hizmeti durdurur.
- `restart`: Belirtilen hizmeti yeniden başlatır.
- `status`: Belirtilen hizmetin durumunu gösterir.
- `enable`: Hizmeti sistem başlangıcında otomatik olarak başlatılacak şekilde ayarlar.
- `disable`: Hizmetin otomatik olarak başlatılmasını engeller.
- `list-units`: Yüklenmiş birimlerin listesini gösterir.

## Examples
### Örnek 1: Hizmeti Başlatma
Aşağıdaki komut, `nginx` hizmetini başlatır:

```bash
sudo systemctl start nginx
```

### Örnek 2: Hizmetin Durumunu Kontrol Etme
Aşağıdaki komut, `nginx` hizmetinin durumunu kontrol eder:

```bash
sudo systemctl status nginx
```

## Tips
- `systemctl` komutunu çalıştırırken genellikle `sudo` kullanmanız gerekebilir, çünkü sistem hizmetlerini yönetmek için yönetici izinlerine ihtiyaç vardır.
- Hizmetlerin otomatik olarak başlatılmasını sağlamak için `enable` komutunu kullanmayı unutmayın.
- Hizmetlerin durumunu düzenli olarak kontrol etmek, sistemin sağlıklı çalışmasını sağlamak için iyi bir uygulamadır.
- `systemctl` komutunun yardım sayfasını görüntülemek için `man systemctl` komutunu kullanabilirsiniz. Bu, mevcut tüm seçenekler ve komutlar hakkında daha fazla bilgi edinmenizi sağlar.