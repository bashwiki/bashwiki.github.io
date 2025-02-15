# [리눅스] Bash iptables 사용법

## Overview
`iptables`, Linux tabanlı işletim sistemlerinde ağ trafiğini kontrol etmek için kullanılan bir komut satırı aracıdır. Temel amacı, gelen ve giden ağ paketlerini filtrelemek, yönlendirmek ve yönetmektir. `iptables`, ağ güvenliği sağlamak için yaygın olarak kullanılır ve sistem yöneticilerine, belirli kurallara göre trafiği kontrol etme yeteneği sunar.

## Usage
`iptables` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
iptables [OPTION] [CHAIN] [RULE]
```

### Yaygın Seçenekler:
- `-A` veya `--append`: Belirtilen zincire yeni bir kural ekler.
- `-D` veya `--delete`: Belirtilen zincirden bir kuralı siler.
- `-L` veya `--list`: Mevcut kuralları listeler.
- `-F` veya `--flush`: Belirtilen zinciri temizler.
- `-P` veya `--policy`: Belirtilen zincir için varsayılan politikayı ayarlar.
- `-I` veya `--insert`: Belirtilen zincire yeni bir kuralı en başa ekler.

## Examples
### Örnek 1: Gelen Trafiği Engelleme
Aşağıdaki komut, 80 numaralı port üzerinden gelen tüm trafiği engeller:

```bash
iptables -A INPUT -p tcp --dport 80 -j DROP
```

### Örnek 2: Mevcut Kuralları Listeleme
Aşağıdaki komut, mevcut `INPUT` zincirindeki tüm kuralları listeler:

```bash
iptables -L INPUT
```

## Tips
- Kurallarınızı uygulamadan önce dikkatlice planlayın ve test edin. Yanlış yapılandırmalar, ağ bağlantınızı kesebilir.
- `iptables` kurallarını kaydetmek ve geri yüklemek için `iptables-save` ve `iptables-restore` komutlarını kullanın.
- Değişikliklerinizi kalıcı hale getirmek için sisteminizin başlangıçta `iptables` kurallarını yüklemesini sağlayın.
- Ağ trafiğini izlemek için `-v` seçeneğini kullanarak daha ayrıntılı bilgi alabilirsiniz.

Bu bilgilerle, `iptables` komutunu etkili bir şekilde kullanarak ağ güvenliğinizi artırabilirsiniz.