# [Linux] Bash logrotate Kullanımı: Log dosyalarını döndürme aracı

## Overview
`logrotate`, sistemdeki log dosyalarını yönetmek ve döndürmek için kullanılan bir araçtır. Bu komut, log dosyalarının boyutunu kontrol altında tutarak, belirli bir süre veya boyut sınırına ulaştığında eski log dosyalarını arşivler veya siler. Böylece disk alanı tasarrufu sağlanır ve log dosyalarının yönetimi kolaylaşır.

## Usage
Temel kullanım şekli aşağıdaki gibidir:

```bash
logrotate [options] [arguments]
```

## Common Options
- `-f`: Zorla döndürme işlemi yapar, yapılandırma dosyasında belirtilen zamanlamaya bakmaz.
- `-s`: Durum dosyasının yolunu belirtir. Bu dosya, logrotate'ın hangi log dosyalarının döndürüldüğünü takip etmesine yardımcı olur.
- `-v`: Ayrıntılı çıktı verir, hangi dosyaların döndürüldüğünü gösterir.
- `-d`: Simülasyon modu, gerçek döndürme işlemi yapmadan ne olacağını gösterir.

## Common Examples
Aşağıda `logrotate` komutunun bazı pratik örnekleri verilmiştir:

1. **Varsayılan yapılandırma dosyasını kullanarak log dosyalarını döndürme:**
   ```bash
   logrotate /etc/logrotate.conf
   ```

2. **Belirli bir yapılandırma dosyası ile döndürme:**
   ```bash
   logrotate -f /path/to/custom_logrotate.conf
   ```

3. **Ayrıntılı çıktı ile döndürme:**
   ```bash
   logrotate -v /etc/logrotate.conf
   ```

4. **Simülasyon modunda çalıştırma:**
   ```bash
   logrotate -d /etc/logrotate.conf
   ```

## Tips
- Logrotate yapılandırma dosyalarınızı düzenli olarak kontrol edin ve güncel tutun.
- Log dosyalarınızın boyutunu ve döndürme sıklığını belirlerken sistem ihtiyaçlarınızı göz önünde bulundurun.
- Logrotate'ın düzgün çalıştığını doğrulamak için düzenli aralıklarla `-d` seçeneği ile simülasyon yapın.