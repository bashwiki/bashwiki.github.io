# [리눅스] Bash logrotate 사용법

## Genel Bakış
`logrotate`, Linux sistemlerinde günlük dosyalarını yönetmek için kullanılan bir komut ve yapılandırma aracıdır. Temel amacı, sistemdeki günlük dosyalarının boyutunu ve sayısını kontrol altında tutarak disk alanını verimli bir şekilde kullanmaktır. `logrotate`, günlük dosyalarını belirli bir zaman diliminde döndürme, sıkıştırma, silme veya yeniden adlandırma gibi işlemleri otomatikleştirir.

## Kullanım
`logrotate` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
logrotate [seçenekler] [yapılandırma dosyası]
```

### Yaygın Seçenekler
- `-f`: Yapılandırma dosyasındaki ayarları zorla uygular. Normalde, günlük dosyaları döndürülmezse bile bu seçenekle işlem yapılır.
- `-s`: Durum dosyasının yolunu belirtir. Bu dosya, hangi günlük dosyalarının döndürüldüğünü takip eder.
- `-v`: Ayrıntılı modda çalışır ve işlem sırasında daha fazla bilgi gösterir.

## Örnekler

### Örnek 1: Temel Kullanım
Aşağıdaki komut, varsayılan yapılandırma dosyasını kullanarak günlük dosyalarını döndürür:

```bash
logrotate /etc/logrotate.conf
```

### Örnek 2: Zorla Günlük Döndürme
Eğer günlük dosyalarını zorla döndürmek istiyorsanız, aşağıdaki komutu kullanabilirsiniz:

```bash
logrotate -f /etc/logrotate.conf
```

## İpuçları
- `logrotate` yapılandırma dosyalarınızı düzenlerken, her günlük dosyası için ayrı bir yapılandırma dosyası oluşturmak, yönetimi kolaylaştırır.
- Günlük dosyalarının ne sıklıkla döndürüleceğini belirlemek için `daily`, `weekly`, `monthly` gibi zamanlama seçeneklerini kullanabilirsiniz.
- Disk alanı tasarrufu sağlamak için, döndürülen günlük dosyalarını sıkıştırmak için `compress` seçeneğini eklemeyi unutmayın.

Bu bilgilerle, `logrotate` komutunu etkili bir şekilde kullanarak sistem günlüklerinizi yönetebilirsiniz.