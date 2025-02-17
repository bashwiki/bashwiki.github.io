# [Linux] Bash uptime Kullanımı: Sistemin çalışma süresini gösterir

## Genel Bakış
`uptime` komutu, bir Linux veya Unix tabanlı sistemin ne kadar süredir çalıştığını gösterir. Ayrıca, sistemin yük ortalamasını ve kullanıcı sayısını da sağlar. Bu bilgi, sistem yöneticileri için sistemin performansını değerlendirmek açısından oldukça önemlidir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
uptime [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-p`, `--pretty`: Çalışma süresini daha okunabilir bir formatta gösterir.
- `-s`, `--since`: Sistemin en son ne zaman başlatıldığını gösterir.

## Yaygın Örnekler
Aşağıda `uptime` komutunun bazı pratik örnekleri bulunmaktadır:

### Temel Kullanım
Sadece sistemin çalışma süresini ve yük ortalamasını görmek için:

```bash
uptime
```

### Okunabilir Format
Çalışma süresini daha okunabilir bir formatta görmek için:

```bash
uptime -p
```

### Sistem Başlangıç Zamanı
Sistemin en son ne zaman başlatıldığını öğrenmek için:

```bash
uptime -s
```

## İpuçları
- `uptime` komutunu düzenli olarak kontrol ederek sisteminizin performansını izleyebilirsiniz.
- Yük ortalamasını takip etmek, sistemin aşırı yüklü olup olmadığını anlamanıza yardımcı olabilir.
- `uptime` komutunu `watch` komutuyla birleştirerek belirli aralıklarla güncel bilgileri görüntüleyebilirsiniz:

```bash
watch uptime
```