# [Linux] Bash mpstat Kullanımı: CPU istatistiklerini görüntüleme

## Overview
`mpstat` komutu, sistemdeki CPU kullanım istatistiklerini görüntülemek için kullanılır. Bu komut, çok çekirdekli sistemlerde her bir çekirdek için ayrı ayrı bilgi sağlar ve CPU'nun performansını analiz etmek için faydalıdır.

## Usage
Temel sözdizimi şu şekildedir:
```bash
mpstat [options] [arguments]
```

## Common Options
- `-P ALL`: Tüm CPU'lar için istatistikleri gösterir.
- `-u`: Kullanıcı ve sistem CPU kullanım yüzdelerini gösterir.
- `-r`: Bellek istatistiklerini gösterir.
- `-h`: İnsan tarafından okunabilir biçimde çıktı verir.
- `-o`: Çıktıyı belirtilen dosyaya kaydeder.

## Common Examples
Aşağıda `mpstat` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### Tüm CPU'lar için istatistikleri görüntüleme
```bash
mpstat -P ALL
```

### Kullanıcı ve sistem CPU kullanım yüzdelerini gösterme
```bash
mpstat -u 1
```
Bu komut, her saniyede bir CPU kullanım yüzdelerini güncelleyerek gösterir.

### Bellek istatistiklerini görüntüleme
```bash
mpstat -r
```

### Çıktıyı dosyaya kaydetme
```bash
mpstat -P ALL -o output.txt
```

## Tips
- `mpstat` komutunu düzenli olarak çalıştırarak sistem performansını izleyin.
- Uzun süreli izleme için çıktıyı bir dosyaya kaydedin ve zamanla analiz edin.
- CPU kullanımını etkileyen uygulamaları belirlemek için `mpstat` çıktısını diğer sistem izleme araçlarıyla birleştirin.