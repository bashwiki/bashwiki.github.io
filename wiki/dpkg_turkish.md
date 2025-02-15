# [리눅스] Bash dpkg 사용법

## Overview
`dpkg`, Debian Paket Yönetim Sistemi'nin bir parçası olan bir komut satırı aracıdır. Debian tabanlı işletim sistemlerinde (örneğin, Ubuntu) yazılım paketlerini yönetmek için kullanılır. `dpkg`, paketlerin kurulumu, kaldırılması ve bilgilerin görüntülenmesi gibi işlemleri gerçekleştirmek için kullanılır. Bu komut, .deb uzantılı paket dosyalarını doğrudan işleyebilir.

## Usage
Temel `dpkg` komut sözdizimi aşağıdaki gibidir:

```bash
dpkg [seçenekler] [paket_adı]
```

### Yaygın Seçenekler
- `-i`, `--install`: Belirtilen .deb paketini kurar.
- `-r`, `--remove`: Belirtilen paketi kaldırır.
- `-l`, `--list`: Yüklenmiş paketlerin listesini gösterir.
- `-s`, `--status`: Belirtilen paketin durumunu gösterir.
- `-c`, `--contents`: Belirtilen paketin içeriğini listeler.

## Examples
### Örnek 1: Bir Paketi Kurma
Aşağıdaki komut, `example-package.deb` adlı bir paketi kurar:

```bash
sudo dpkg -i example-package.deb
```

### Örnek 2: Yüklenmiş Paketleri Listeleme
Yüklenmiş tüm paketleri listelemek için şu komutu kullanabilirsiniz:

```bash
dpkg -l
```

## Tips
- Paket kurulumunda bağımlılık sorunları ile karşılaşabilirsiniz. Bu durumda, `apt-get install -f` komutunu kullanarak eksik bağımlılıkları çözebilirsiniz.
- `dpkg` komutunu kullanmadan önce, sisteminizde yedekleme yapmanız önerilir. Özellikle önemli paketleri kaldırmadan önce dikkatli olun.
- Paket bilgilerini daha ayrıntılı görmek için `dpkg -s paket_adı` komutunu kullanabilirsiniz. Bu, paketin durumu, sürümü ve bağımlılıkları hakkında bilgi verir.