# [리눅스] Bash cron 사용법

## Overview
`cron`, Unix tabanlı sistemlerde zamanlanmış görevleri otomatik olarak çalıştırmak için kullanılan bir arka plan hizmetidir. Kullanıcılar, belirli zaman dilimlerinde veya belirli aralıklarla belirli komutları veya betikleri çalıştırmak için `cron`'u kullanabilirler. Bu, sistem bakım görevleri, yedekleme işlemleri veya belirli zamanlarda rapor oluşturma gibi işlemler için oldukça yararlıdır.

## Usage
`cron`, genellikle bir kullanıcı tarafından `crontab` dosyası aracılığıyla yapılandırılır. Temel sözdizimi şu şekildedir:

```
* * * * * komut
```

Burada, yıldız işaretleri ( `*` ) zamanlama ayarlarını temsil eder ve her bir yıldızın anlamı şudur:

- **Dakika** (0-59)
- **Saat** (0-23)
- **Gün** (1-31)
- **Ay** (1-12)
- **Hafta Günü** (0-7) (0 ve 7 Pazar'ı temsil eder)

### Yaygın Seçenekler
- `*`: Herhangi bir değer (her zaman)
- `,`: Birden fazla değer belirtmek için (örneğin, `1,2,3` her birini temsil eder)
- `-`: Bir aralık belirtmek için (örneğin, `1-5` 1'den 5'e kadar olan günleri temsil eder)
- `/`: Belirli bir sıklık belirtmek için (örneğin, `*/5` her 5 dakikada bir anlamına gelir)

## Examples
### Örnek 1: Her gün saat 2'de bir yedekleme komutu çalıştırma
Aşağıdaki `crontab` girişi, her gün saat 2:00'de `backup.sh` betiğini çalıştıracaktır.

```
0 2 * * * /path/to/backup.sh
```

### Örnek 2: Her 15 dakikada bir bir güncelleme komutu çalıştırma
Aşağıdaki `crontab` girişi, her 15 dakikada bir `update.sh` betiğini çalıştıracaktır.

```
*/15 * * * * /path/to/update.sh
```

## Tips
- `crontab -e` komutunu kullanarak mevcut `crontab` dosyanızı düzenleyebilirsiniz.
- `crontab -l` komutu ile mevcut zamanlanmış görevlerinizi listeleyebilirsiniz.
- Görevlerin çıktısını bir dosyaya yönlendirmek için `>> /path/to/logfile.log` ekleyebilirsiniz. Örneğin:

```
0 2 * * * /path/to/backup.sh >> /path/to/backup.log 2>&1
```

- Zamanlama ayarlarınızı dikkatlice kontrol edin; yanlış ayarlar, istenmeyen sonuçlara yol açabilir.
- `cron` ile ilgili hata ayıklama yapmak için, genellikle `/var/log/syslog` dosyasını kontrol edebilirsiniz.