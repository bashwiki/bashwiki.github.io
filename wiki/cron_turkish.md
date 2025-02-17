# [Linux] Bash cron Kullanımı: Zamanlanmış görevleri yönetme

## Genel Bakış
`cron`, Unix benzeri işletim sistemlerinde zamanlanmış görevleri otomatik olarak çalıştırmak için kullanılan bir komut ve zamanlayıcıdır. Kullanıcılar, belirli zaman dilimlerinde veya belirli aralıklarla komutlar veya scriptler çalıştırmak için `cron` kullanabilirler.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
cron [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-l`: Kullanıcının mevcut cron görevlerini listelemek için kullanılır.
- `-e`: Kullanıcının mevcut cron görevlerini düzenlemek için kullanılır.
- `-r`: Kullanıcının cron görevlerini kaldırmak için kullanılır.

## Yaygın Örnekler
Aşağıda `cron` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### 1. Cron Görevini Listeleme
Mevcut cron görevlerinizi listelemek için:

```bash
crontab -l
```

### 2. Cron Görevünü Düzenleme
Mevcut cron görevlerinizi düzenlemek için:

```bash
crontab -e
```

### 3. Her Gün Saat 2'de Bir Script Çalıştırma
Her gün saat 2'de belirli bir scripti çalıştırmak için cron dosyasına şu satırı ekleyebilirsiniz:

```bash
0 2 * * * /path/to/script.sh
```

### 4. Her 15 Dakikada Bir Komut Çalıştırma
Her 15 dakikada bir belirli bir komutu çalıştırmak için:

```bash
*/15 * * * * /path/to/command
```

### 5. Her Pazartesi Saat 10'da Yedekleme Yapma
Her pazartesi saat 10'da yedekleme yapmak için:

```bash
0 10 * * 1 /path/to/backup.sh
```

## İpuçları
- Cron görevlerinizi düzenlerken dikkatli olun; yanlış bir zamanlama, istenmeyen sonuçlara yol açabilir.
- Görevlerin çıktısını bir dosyaya yönlendirmek için `>> /path/to/logfile.log` ekleyebilirsiniz.
- Zamanlama ifadelerini doğru bir şekilde kullanmak için cron zamanlama formatını iyi öğrenin.