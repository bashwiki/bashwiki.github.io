# [Linux] Bash systemctl Kullanımı: Sistem hizmetlerini yönetme

## Overview
`systemctl`, Linux sistemlerinde hizmetleri (servisleri) ve sistem durumunu yönetmek için kullanılan bir komuttur. Bu komut, sistemd tabanlı sistemlerde hizmetlerin başlatılması, durdurulması, yeniden başlatılması ve durumlarının kontrol edilmesi gibi işlemleri kolaylaştırır.

## Usage
Temel sözdizimi şu şekildedir:
```bash
systemctl [options] [arguments]
```

## Common Options
- `start`: Bir hizmeti başlatır.
- `stop`: Bir hizmeti durdurur.
- `restart`: Bir hizmeti yeniden başlatır.
- `status`: Bir hizmetin durumunu gösterir.
- `enable`: Bir hizmeti sistem başlangıcında otomatik olarak başlatılacak şekilde ayarlar.
- `disable`: Bir hizmetin otomatik olarak başlatılmasını engeller.

## Common Examples
Aşağıda `systemctl` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

- Bir hizmeti başlatmak için:
  ```bash
  systemctl start httpd
  ```

- Bir hizmeti durdurmak için:
  ```bash
  systemctl stop httpd
  ```

- Bir hizmetin durumunu kontrol etmek için:
  ```bash
  systemctl status httpd
  ```

- Bir hizmeti yeniden başlatmak için:
  ```bash
  systemctl restart httpd
  ```

- Bir hizmeti sistem başlangıcında otomatik olarak başlatmak için:
  ```bash
  systemctl enable httpd
  ```

- Bir hizmetin otomatik olarak başlatılmasını engellemek için:
  ```bash
  systemctl disable httpd
  ```

## Tips
- Hizmetlerin durumunu kontrol etmek için `status` seçeneğini kullanarak sorunları hızlıca tespit edebilirsiniz.
- Hizmetleri otomatik olarak başlatmak için `enable` seçeneğini kullanmak, sisteminizin her zaman gerekli hizmetlerle başlamasını sağlar.
- `systemctl` komutunu kullanırken, root yetkilerine sahip olmanız gerektiğini unutmayın; bu nedenle `sudo` ile birlikte kullanmanız gerekebilir.