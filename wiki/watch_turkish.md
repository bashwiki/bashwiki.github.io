# [Linux] Bash watch Kullanımı: Komutların sürekli izlenmesi

## Overview
`watch` komutu, belirli bir komutu belirli aralıklarla çalıştırarak çıktısını sürekli olarak güncelleyerek görüntülemeye yarar. Bu, sistem durumunu izlemek veya belirli bir işlemin ilerlemesini takip etmek için oldukça faydalıdır.

## Usage
Temel kullanım sözdizimi aşağıdaki gibidir:

```bash
watch [options] [arguments]
```

## Common Options
- `-n, --interval`: Komutun ne sıklıkla çalıştırılacağını belirler. Varsayılan değer 2 saniyedir.
- `-d, --differences`: Çıktıdaki değişiklikleri vurgular.
- `-t, --no-title`: Başlık satırını gizler.
- `-h, --help`: Kullanım bilgilerini gösterir.

## Common Examples
Aşağıda `watch` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. **Sistem kaynaklarını izlemek:**
   ```bash
   watch -n 1 free -h
   ```
   Bu komut, her saniye sistemin bellek kullanımını gösterir.

2. **Disk kullanımını izlemek:**
   ```bash
   watch -n 5 df -h
   ```
   Bu komut, her 5 saniyede bir disk kullanımını güncelleyerek gösterir.

3. **Belirli bir dizindeki dosya değişikliklerini izlemek:**
   ```bash
   watch -d ls -l /path/to/directory
   ```
   Bu komut, belirtilen dizindeki dosyaların listesini ve değişikliklerini vurgulayarak gösterir.

4. **Bir servisin durumunu izlemek:**
   ```bash
   watch systemctl status apache2
   ```
   Bu komut, Apache2 servisini sürekli olarak izler ve durumunu günceller.

## Tips
- `watch` komutunu kullanırken, izlemek istediğiniz komutun çıktısının çok fazla veri üretmediğinden emin olun. Aksi takdirde, ekranınız karmaşık hale gelebilir.
- `-d` seçeneği ile değişiklikleri vurgulamak, hangi bilgilerin güncellendiğini hızlıca görmenizi sağlar.
- Belirli bir komutu izlerken, aralıkları ihtiyaçlarınıza göre ayarlamayı unutmayın; çok sık güncellemeler gereksiz kaynak tüketimine yol açabilir.