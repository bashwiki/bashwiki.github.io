# [Linux] Bash rpm Kullanımı: Paket yönetimi aracı

## Genel Bakış
`rpm` (Red Hat Package Manager), Red Hat tabanlı Linux dağıtımlarında kullanılan bir paket yönetim aracıdır. Yazılım paketlerini kurmak, kaldırmak, güncellemek ve sorgulamak için kullanılır. RPM, yazılımın bağımlılıklarını yöneterek sistemin stabilitesini sağlamaya yardımcı olur.

## Kullanım
Temel `rpm` komutunun sözdizimi aşağıdaki gibidir:

```
rpm [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-i`: Yeni bir RPM paketi kurar.
- `-e`: Mevcut bir RPM paketini kaldırır.
- `-U`: Bir RPM paketini günceller.
- `-q`: Yüklenmiş bir paketi sorgular.
- `--info`: Bir RPM paketi hakkında bilgi verir.
- `--verify`: Yüklenmiş bir paketin bütünlüğünü kontrol eder.

## Yaygın Örnekler
Aşağıda `rpm` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. RPM Paketi Kurma
Bir RPM paketini kurmak için:
```bash
rpm -i paket_adı.rpm
```

### 2. RPM Paketi Kaldırma
Bir RPM paketini kaldırmak için:
```bash
rpm -e paket_adı
```

### 3. RPM Paketi Güncelleme
Bir RPM paketini güncellemek için:
```bash
rpm -U paket_adı.rpm
```

### 4. Yüklenmiş Paketleri Sorgulama
Sisteminizde yüklü olan bir paketi sorgulamak için:
```bash
rpm -q paket_adı
```

### 5. Paket Hakkında Bilgi Alma
Bir RPM paketi hakkında detaylı bilgi almak için:
```bash
rpm --info paket_adı.rpm
```

## İpuçları
- Yükleme veya kaldırma işlemlerinde root yetkilerine ihtiyaç duyulabilir, bu nedenle `sudo` kullanmayı unutmayın.
- Paketlerin bağımlılıklarını kontrol etmek için `yum` veya `dnf` gibi araçları tercih edebilirsiniz.
- `rpm` komutunu kullanmadan önce, hangi paketlerin yüklü olduğunu görmek için `rpm -qa` komutunu kullanarak sisteminizi kontrol edin.