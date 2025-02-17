# [Linux] Bash at Kullanımı: Zamanlanmış komut çalıştırma

## Genel Bakış
`at` komutu, belirli bir zamanda bir veya daha fazla komutun çalıştırılmasını sağlamak için kullanılır. Bu, kullanıcıların belirli bir zaman diliminde otomatik olarak görevler planlamasına olanak tanır.

## Kullanım
Temel sözdizimi şu şekildedir:
```
at [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-f`: Belirtilen dosyadaki komutları çalıştırır.
- `-m`: Komut çalıştırıldığında e-posta bildirimi gönderir.
- `-q`: Kuyruk belirler (örneğin, a, b, c gibi).
- `-l`: Planlanmış görevlerin listesini gösterir.
- `-d`: Belirli bir görevden kurtulmak için kullanılır.

## Yaygın Örnekler
Aşağıda `at` komutunun bazı pratik örnekleri bulunmaktadır:

1. **Belirli bir zamanda bir komut çalıştırma:**
   ```bash
   echo "echo 'Merhaba Dünya'" | at 14:00
   ```
   Bu komut, her gün saat 14:00'te "Merhaba Dünya" mesajını yazdırır.

2. **Bir dosyadaki komutları çalıştırma:**
   ```bash
   at -f /path/to/komutlar.txt 09:00
   ```
   Bu komut, belirtilen dosyadaki komutları her gün saat 09:00'da çalıştırır.

3. **E-posta bildirimi ile görev planlama:**
   ```bash
   echo "backup.sh" | at -m now + 1 hour
   ```
   Bu komut, `backup.sh` dosyasını bir saat sonra çalıştırır ve işlem tamamlandığında e-posta bildirimi gönderir.

4. **Planlanmış görevlerin listesini görüntüleme:**
   ```bash
   at -l
   ```
   Bu komut, mevcut planlanmış görevlerin listesini gösterir.

5. **Belirli bir görevi iptal etme:**
   ```bash
   at -d 5
   ```
   Bu komut, ID'si 5 olan planlanmış görevi iptal eder.

## İpuçları
- `at` komutunu kullanmadan önce, sisteminizde `atd` hizmetinin çalıştığından emin olun.
- Zaman formatında dikkatli olun; saat dilimlerini ve tarihleri doğru girdiğinizden emin olun.
- Planladığınız görevlerin çıktısını kontrol etmek için, e-posta bildirimlerini etkinleştirmeyi düşünün.