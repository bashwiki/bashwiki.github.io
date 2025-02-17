# [Linux] Bash yum Kullanımı: Paket yönetimi aracı

## Genel Bakış
`yum`, Red Hat tabanlı Linux dağıtımlarında kullanılan bir paket yönetim aracıdır. Yazılımları yüklemek, güncellemek ve kaldırmak için kullanılır. Ayrıca, sistemdeki mevcut paketlerin bağımlılıklarını yönetir ve güncellemeleri kontrol eder.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
yum [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `install`: Belirtilen paketi yükler.
- `remove`: Belirtilen paketi kaldırır.
- `update`: Yüklenmiş paketleri günceller.
- `search`: Belirtilen terimi içeren paketleri arar.
- `info`: Belirtilen paket hakkında bilgi verir.

## Yaygın Örnekler
Aşağıda `yum` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### Bir Paketi Yüklemek
```bash
yum install paket_adi
```

### Bir Paketi Kaldırmak
```bash
yum remove paket_adi
```

### Yüklenmiş Paketleri Güncellemek
```bash
yum update
```

### Belirli Bir Paketi Aramak
```bash
yum search arama_terimi
```

### Paket Hakkında Bilgi Almak
```bash
yum info paket_adi
```

## İpuçları
- `yum` komutunu kullanmadan önce, sisteminizin güncel olduğundan emin olun.
- Paketlerin bağımlılıklarını otomatik olarak yönetmek için `yum` kullanmak, sistem kararlılığını artırır.
- `yum clean all` komutunu kullanarak önbelleği temizleyebilir ve disk alanı kazanabilirsiniz.