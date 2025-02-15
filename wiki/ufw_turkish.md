# [리눅스] Bash ufw 사용법

## Overview
`ufw` (Uncomplicated Firewall), Linux sistemlerinde güvenlik duvarı yapılandırmasını basit ve kullanıcı dostu bir şekilde yönetmek için kullanılan bir komut satırı aracıdır. `ufw`, özellikle yeni başlayanlar ve sistem yöneticileri için, karmaşık iptables komutlarına alternatif olarak tasarlanmıştır. Temel amacı, ağ trafiğini kontrol etmek ve sistemin güvenliğini artırmaktır.

## Usage
`ufw` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
ufw [OPTIONS] [COMMAND]
```

### Yaygın Seçenekler:
- `enable`: Güvenlik duvarını etkinleştirir.
- `disable`: Güvenlik duvarını devre dışı bırakır.
- `status`: Güvenlik duvarının mevcut durumunu gösterir.
- `allow`: Belirtilen port veya hizmet için trafiğe izin verir.
- `deny`: Belirtilen port veya hizmet için trafiği engeller.
- `delete`: Daha önce eklenmiş bir kuralı siler.

## Examples
### Örnek 1: Güvenlik Duvarını Etkinleştirme
Güvenlik duvarını etkinleştirmek için aşağıdaki komutu kullanabilirsiniz:

```bash
sudo ufw enable
```

Bu komut, `ufw`'yi etkinleştirir ve varsayılan kuralları uygular.

### Örnek 2: Belirli Bir Portu Açma
Örneğin, 80 numaralı portu (HTTP) açmak için şu komutu kullanabilirsiniz:

```bash
sudo ufw allow 80
```

Bu komut, HTTP trafiğine izin verir ve web sunucunuzun dışarıdan erişilebilir olmasını sağlar.

## Tips
- `ufw` kullanmadan önce, mevcut güvenlik duvarı kurallarınızı kontrol etmek için `ufw status verbose` komutunu kullanın.
- Değişikliklerinizi uygulamadan önce `ufw`'nin durumunu kontrol edin ve gerektiğinde yedekleme yapın.
- Güvenlik duvarı kurallarınızı düzenli olarak gözden geçirin ve gereksiz kuralları kaldırarak güvenliğinizi artırın.
- `ufw` ile birlikte `iptables`'ı kullanıyorsanız, `ufw`'nin iptables kurallarını etkileyebileceğini unutmayın.