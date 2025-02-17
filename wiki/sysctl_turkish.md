# [Linux] Bash sysctl Kullanımı: Çekirdek parametrelerini ayarlama

## Overview
`sysctl` komutu, Linux çekirdeği ile ilgili ayarları görüntülemek ve değiştirmek için kullanılır. Bu komut, sistem performansını optimize etmek ve çekirdek parametrelerini dinamik olarak ayarlamak için oldukça faydalıdır.

## Usage
Temel sözdizimi şu şekildedir:
```bash
sysctl [options] [arguments]
```

## Common Options
- `-a`: Tüm sysctl ayarlarını ve değerlerini listelemek için kullanılır.
- `-w`: Belirtilen bir parametreyi değiştirmek için kullanılır.
- `-n`: Değerleri yalnızca gösterir, başlık bilgisi olmadan.
- `-p`: Belirtilen bir dosyadan ayarları yüklemek için kullanılır.

## Common Examples
Aşağıda `sysctl` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Tüm sysctl ayarlarını listeleme:
   ```bash
   sysctl -a
   ```

2. Belirli bir parametreyi görüntüleme (örneğin, `vm.swappiness`):
   ```bash
   sysctl vm.swappiness
   ```

3. Bir parametreyi değiştirme (örneğin, `vm.swappiness` değerini 10 olarak ayarlama):
   ```bash
   sysctl -w vm.swappiness=10
   ```

4. Bir dosyadan ayarları yükleme (örneğin, `/etc/sysctl.conf`):
   ```bash
   sysctl -p /etc/sysctl.conf
   ```

## Tips
- Değişikliklerin kalıcı olmasını istiyorsanız, ayarları `/etc/sysctl.conf` dosyasına eklemeyi unutmayın.
- `sysctl` komutunu kullanmadan önce mevcut ayarları yedeklemek iyi bir uygulamadır.
- Performans sorunlarını gidermek için `sysctl` ile oynamadan önce, hangi parametrelerin ne işe yaradığını anlamak önemlidir.