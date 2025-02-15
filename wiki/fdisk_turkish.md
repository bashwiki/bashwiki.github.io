# [리눅스] Bash fdisk 사용법

## Genel Bakış
`fdisk`, Linux ve diğer Unix benzeri işletim sistemlerinde kullanılan bir disk bölümleme aracıdır. Bu komut, sabit disklerin ve diğer depolama aygıtlarının bölüm tablolarını oluşturmak, düzenlemek ve silmek için kullanılır. `fdisk`, özellikle MBR (Master Boot Record) bölümleme şemasını destekler ve kullanıcıların disk alanını yönetmelerine olanak tanır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
fdisk [seçenekler] [cihaz]
```

Burada `cihaz`, üzerinde işlem yapmak istediğiniz disk veya bölümün yolunu belirtir (örneğin, `/dev/sda`).

### Yaygın Seçenekler
- `-l`: Tüm diskleri ve bölümleri listelemek için kullanılır.
- `-u`: Boyutları sektör cinsinden göstermek için kullanılır.
- `-n`: Yeni bir bölüm oluşturmak için kullanılır.
- `-d`: Mevcut bir bölümü silmek için kullanılır.

## Örnekler

### Örnek 1: Diskleri Listeleme
Tüm bağlı diskleri ve bölümleri listelemek için aşağıdaki komutu kullanabilirsiniz:

```bash
sudo fdisk -l
```

Bu komut, sistemdeki tüm disklerin ve bölümlerin detaylı bir listesini gösterir.

### Örnek 2: Yeni Bir Bölüm Oluşturma
Yeni bir bölüm oluşturmak için `fdisk` komutunu şu şekilde kullanabilirsiniz:

```bash
sudo fdisk /dev/sda
```

Bu komut, `/dev/sda` cihazında `fdisk` aracını başlatır. Ardından, `n` tuşuna basarak yeni bir bölüm oluşturma adımlarını takip edebilirsiniz.

## İpuçları
- `fdisk` kullanmadan önce, önemli verilerinizi yedeklemek her zaman iyi bir uygulamadır. Yanlış bölümleme işlemleri veri kaybına neden olabilir.
- `fdisk` ile çalışırken dikkatli olun; yanlış bir bölüm silme veya düzenleme işlemi geri alınamaz sonuçlar doğurabilir.
- Disk bölümleme işlemlerinden sonra, değişikliklerin etkili olması için sistemi yeniden başlatmanız gerekebilir.
- `fdisk` ile birlikte `parted` veya `gparted` gibi diğer araçları da incelemek, daha karmaşık bölümleme ihtiyaçlarınız için faydalı olabilir.