# [리눅스] Bash dnf 사용법

## Overview
`dnf` (Dandified YUM), Red Hat tabanlı dağıtımlarda (Fedora, RHEL, CentOS gibi) kullanılan bir paket yönetim aracıdır. `dnf`, yazılım paketlerini yüklemek, güncellemek, kaldırmak ve yönetmek için kullanılır. `yum`'un daha yeni bir versiyonu olarak, daha iyi performans, daha az bellek kullanımı ve daha iyi bağımlılık çözümleme yetenekleri sunar.

## Usage
`dnf` komutunun temel sözdizimi şu şekildedir:

```bash
dnf [seçenekler] [komut] [paket_adı]
```

### Yaygın Seçenekler
- `install`: Belirtilen paketi yükler.
- `remove`: Belirtilen paketi kaldırır.
- `update`: Yüklü paketleri günceller.
- `search`: Belirtilen terimi içeren paketleri arar.
- `info`: Belirtilen paket hakkında bilgi gösterir.
- `list`: Yüklü veya mevcut paketlerin listesini gösterir.

## Examples
### Örnek 1: Paket Yükleme
Bir paketi yüklemek için `install` komutunu kullanabilirsiniz. Örneğin, `httpd` paketini yüklemek için:

```bash
sudo dnf install httpd
```

### Örnek 2: Paket Güncelleme
Tüm yüklü paketleri güncellemek için `update` komutunu kullanabilirsiniz:

```bash
sudo dnf update
```

## Tips
- `dnf` komutunu çalıştırmadan önce `sudo` kullanmayı unutmayın, çünkü çoğu paket yönetim işlemi için yönetici izinleri gereklidir.
- Paketlerin güncel olduğundan emin olmak için düzenli olarak `dnf update` komutunu çalıştırın.
- `dnf` ile birlikte `--assumeyes` seçeneğini kullanarak, onay istemeden işlemleri gerçekleştirebilirsiniz. Örneğin:

```bash
sudo dnf install --assumeyes httpd
```

Bu, yükleme işlemini onaylamadan otomatik olarak gerçekleştirecektir. Ancak dikkatli kullanmalısınız, çünkü bu seçenek bazı durumlarda istenmeyen sonuçlara yol açabilir.