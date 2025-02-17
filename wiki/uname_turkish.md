# [Linux] Bash uname Kullanımı: Sistem bilgilerini görüntüleme

## Genel Bakış
`uname` komutu, işletim sistemi hakkında bilgi sağlar. Bu komut, sistemin çekirdek adı, sürüm numarası ve mimarisi gibi bilgileri görüntülemek için kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
uname [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-a`: Tüm bilgileri gösterir.
- `-s`: Çekirdek adını gösterir.
- `-n`: Ağ ana bilgisayar adını gösterir.
- `-r`: Çekirdek sürümünü gösterir.
- `-v`: Çekirdek versiyon bilgilerini gösterir.
- `-m`: Makine mimarisini gösterir.

## Yaygın Örnekler
Aşağıda `uname` komutunun bazı pratik örnekleri bulunmaktadır:

### Tüm Bilgileri Gösterme
```bash
uname -a
```
Bu komut, sistemin çekirdek adı, sürümü, mimarisi ve diğer bilgileri gösterir.

### Çekirdek Adını Görüntüleme
```bash
uname -s
```
Bu komut, yalnızca çekirdek adını gösterir.

### Çekirdek Sürümünü Görüntüleme
```bash
uname -r
```
Bu komut, sistemdeki çekirdek sürümünü gösterir.

### Makine Mimarisi Bilgisi
```bash
uname -m
```
Bu komut, sistemin mimarisini (örneğin, x86_64) gösterir.

## İpuçları
- `uname -a` komutunu kullanarak sistem hakkında kapsamlı bilgi alabilirsiniz.
- Çekirdek sürümünü kontrol ederek güncellemeleri planlayabilirsiniz.
- Uygulama veya yazılım yüklemeden önce sistem mimarisini kontrol etmek için `uname -m` kullanışlıdır.