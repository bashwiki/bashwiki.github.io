# [Linux] Bash fdisk Kullanımı: Disk bölümlerini yönetme aracı

## Overview
`fdisk`, disk bölümlerini yönetmek için kullanılan bir komut satırı aracıdır. Bu komut, disklerin bölümlerini oluşturma, silme, değiştirme ve görüntüleme işlemlerini gerçekleştirmenizi sağlar. Genellikle, disk yapılandırmalarını yönetmek için kullanılır ve özellikle Linux sistemlerinde yaygındır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
fdisk [options] [arguments]
```

## Common Options
- `-l`: Tüm diskleri ve bölümlerini listelemek için kullanılır.
- `-u`: Boyutları sektör cinsinden göstermek için kullanılır.
- `-n`: Yeni bir bölüm oluşturmak için kullanılır.
- `-d`: Var olan bir bölümü silmek için kullanılır.
- `-s`: Belirtilen bölümün boyutunu görüntülemek için kullanılır.

## Common Examples
Aşağıda `fdisk` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### Tüm Diskleri Listeleme
```bash
fdisk -l
```

### Yeni Bir Bölüm Oluşturma
```bash
fdisk /dev/sda
```
Bu komut ile `sda` diskine yeni bir bölüm eklemek için interaktif bir arayüze geçersiniz.

### Var Olan Bir Bölümü Silme
```bash
fdisk /dev/sda
```
Ardından, silmek istediğiniz bölümü seçip `d` komutunu kullanarak işlemi gerçekleştirebilirsiniz.

### Bölüm Boyutunu Görüntüleme
```bash
fdisk -s /dev/sda1
```
Bu komut, `sda1` bölümünün boyutunu gösterir.

## Tips
- `fdisk` komutunu kullanmadan önce, önemli verilerinizi yedeklemeyi unutmayın. Yanlış bir işlem veri kaybına neden olabilir.
- `fdisk` komutunu kullanırken dikkatli olun; yanlışlıkla bir bölümü silmek veya değiştirmek, sistemin çalışmasını etkileyebilir.
- Disk bölümleri üzerinde değişiklik yapmadan önce, mevcut yapılandırmanızı kontrol etmek için `fdisk -l` komutunu kullanın.