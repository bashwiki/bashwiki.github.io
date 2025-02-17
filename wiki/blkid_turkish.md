# [Linux] Bash blkid Kullanımı: Disk ve dosya sistemleri hakkında bilgi edinme

## Overview
`blkid` komutu, sistemdeki blok aygıtlarının (diskler, bölümler vb.) kimlik bilgilerini ve dosya sistemi türlerini görüntülemek için kullanılır. Bu komut, disklerin ve bölümlerin özelliklerini hızlı bir şekilde öğrenmek isteyen kullanıcılar için oldukça faydalıdır.

## Usage
Temel sözdizimi şu şekildedir:
```bash
blkid [options] [arguments]
```

## Common Options
- `-o, --output`: Çıktı formatını belirler. Örneğin, `value` veya `full` gibi.
- `-s, --match-tag`: Belirli bir etiketle eşleşen bilgileri görüntüler.
- `-p, --probe`: Aygıtın dosya sistemini belirlemek için probe işlemi yapar.
- `-c, --cache`: Önbellek dosyasını kullanarak daha hızlı sonuçlar almanızı sağlar.

## Common Examples
Aşağıda `blkid` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Tüm blok aygıtlarını listeleme:
   ```bash
   blkid
   ```

2. Belirli bir aygıtın bilgilerini görüntüleme:
   ```bash
   blkid /dev/sda1
   ```

3. Çıktıyı sadece dosya sistemi türü ile sınırlama:
   ```bash
   blkid -o value -s TYPE /dev/sda1
   ```

4. Önbellek dosyasını kullanarak hızlı bir sorgulama yapma:
   ```bash
   blkid -c /etc/blkid.tab
   ```

## Tips
- `blkid` komutunu `sudo` ile çalıştırmak, bazı aygıtlara erişim izni gerektirebilir.
- Çıktıyı bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz:
  ```bash
  blkid > disk_bilgileri.txt
  ```
- Belirli bir dosya sistemine sahip aygıtları bulmak için `grep` ile birleştirerek kullanabilirsiniz:
  ```bash
  blkid | grep ext4
  ``` 

Bu bilgiler, `blkid` komutunu etkili bir şekilde kullanmanıza yardımcı olacaktır.