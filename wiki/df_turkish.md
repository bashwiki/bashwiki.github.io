# [Linux] Bash df Kullanımı: Disk alanı bilgisi gösterir

## Overview
`df` komutu, sistemdeki dosya sistemlerinin disk alanı kullanımını gösterir. Bu komut, her bir dosya sisteminin toplam, kullanılan ve boş alan miktarını görüntüleyerek kullanıcıların disk alanı yönetimini kolaylaştırır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
df [options] [arguments]
```

## Common Options
- `-h`: İnsan tarafından okunabilir formatta (örneğin, KB, MB, GB) çıktı verir.
- `-T`: Dosya sisteminin türünü de gösterir.
- `-a`: Tüm dosya sistemlerini, boş olanlar dahil, listeler.
- `-i`: İnod sayısını gösterir; dosya sisteminin inode kullanımını görüntüler.

## Common Examples
Aşağıda `df` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. **Temel Disk Kullanım Bilgisi**
   ```bash
   df
   ```

2. **İnsan Okunabilir Format**
   ```bash
   df -h
   ```

3. **Dosya Sistemi Türü ile Birlikte Gösterim**
   ```bash
   df -T
   ```

4. **Tüm Dosya Sistemlerini Listeleme**
   ```bash
   df -a
   ```

5. **İnod Kullanımını Gösterme**
   ```bash
   df -i
   ```

## Tips
- Disk alanı yönetimi için `df` komutunu düzenli olarak kullanarak sisteminizin durumunu kontrol edin.
- `df -h` seçeneği ile çıktıyı daha anlaşılır hale getirerek, disk alanı kullanımını hızlıca değerlendirin.
- Eğer belirli bir dosya sisteminin durumunu kontrol etmek istiyorsanız, dosya sisteminin yolunu argüman olarak verebilirsiniz. Örneğin:
  ```bash
  df -h /home
  ```