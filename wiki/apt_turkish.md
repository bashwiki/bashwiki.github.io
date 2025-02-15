# [리눅스] Bash apt 사용법

## Overview
`apt`, Debian tabanlı sistemlerde (örneğin Ubuntu) kullanılan bir paket yönetim aracıdır. `apt`, yazılım paketlerini yüklemek, güncellemek ve kaldırmak için kullanılır. Kullanıcıların sistemlerinde yazılım kurulumunu ve yönetimini kolaylaştırmak amacıyla tasarlanmıştır.

## Usage
Temel `apt` komut yapısı şu şekildedir:

```bash
apt [seçenekler] [komut] [paket_adı]
```

### Yaygın Seçenekler
- `update`: Paket listelerini günceller.
- `upgrade`: Yüklenmiş paketleri en son sürümlerine günceller.
- `install`: Belirtilen paketi yükler.
- `remove`: Belirtilen paketi kaldırır.
- `search`: Belirtilen terimi içeren paketleri arar.

## Examples
### Örnek 1: Paket Güncelleme
Yüklenmiş paketlerinizi güncellemek için aşağıdaki komutu kullanabilirsiniz:

```bash
sudo apt update && sudo apt upgrade
```

Bu komut, önce paket listelerini günceller, ardından sistemdeki tüm yüklü paketleri en son sürümlerine günceller.

### Örnek 2: Yeni Bir Paket Yükleme
Örneğin, `curl` adlı bir aracı yüklemek için şu komutu kullanabilirsiniz:

```bash
sudo apt install curl
```

Bu komut, `curl` paketini sisteminize yükler.

## Tips
- `sudo` komutunu kullanmayı unutmayın; çünkü `apt` genellikle yönetici (root) yetkileri gerektirir.
- `apt` komutunu kullanmadan önce `apt update` komutunu çalıştırarak paket listelerinizi güncel tutun.
- Paketleri kaldırmadan önce, hangi dosyaların kaldırılacağını görmek için `apt remove --dry-run paket_adı` komutunu kullanabilirsiniz. Bu, kaldırma işleminin ne yapacağını önceden görmenizi sağlar.