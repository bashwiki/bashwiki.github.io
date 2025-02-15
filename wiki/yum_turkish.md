# [리눅스] Bash yum 사용법

## Genel Bakış
`yum`, Red Hat tabanlı Linux dağıtımlarında (örneğin, CentOS, Fedora ve RHEL) kullanılan bir paket yönetim aracıdır. `yum`, kullanıcıların yazılım paketlerini yüklemelerine, güncellemelerine ve kaldırmalarına olanak tanır. Ayrıca, bağımlılıkları otomatik olarak yöneterek kullanıcıların sistemlerini güncel ve güvenli tutmalarına yardımcı olur.

## Kullanım
`yum` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
yum [seçenekler] [komut] [paket_adı]
```

### Yaygın Seçenekler
- `install`: Belirtilen paketi yükler.
- `remove`: Belirtilen paketi kaldırır.
- `update`: Yüklü paketleri günceller.
- `search`: Belirtilen anahtar kelimeye göre paket arar.
- `info`: Belirtilen paket hakkında bilgi verir.

## Örnekler

### Paket Yükleme
Aşağıdaki komut, `httpd` adlı web sunucusu paketini yükler:

```bash
yum install httpd
```

### Paket Güncelleme
Tüm yüklü paketleri güncellemek için aşağıdaki komutu kullanabilirsiniz:

```bash
yum update
```

## İpuçları
- `yum` komutunu çalıştırmadan önce, sisteminizin güncel olduğundan emin olun. Bunun için `yum check-update` komutunu kullanabilirsiniz.
- Paketlerinizi güncellerken, güncellemeleri onaylamadan önce hangi paketlerin güncelleneceğini görmek için `yum update` komutunu `-y` seçeneği olmadan çalıştırın.
- `yum` ile sıkça kullandığınız paketleri yüklemek için bir script oluşturabilir ve bu scripti düzenli olarak çalıştırarak sisteminizi güncel tutabilirsiniz.