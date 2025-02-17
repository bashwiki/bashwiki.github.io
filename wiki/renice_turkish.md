# [Linux] Bash renice Kullanımı: Süreç önceliğini değiştirme

## Overview
`renice` komutu, çalışan bir sürecin önceliğini değiştirmek için kullanılır. Bu komut, sistem kaynaklarını daha verimli kullanmak ve belirli süreçlerin performansını artırmak amacıyla öncelik seviyelerini ayarlamak için idealdir.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
renice [options] [arguments]
```

## Common Options
- `-n`, `--priority`: Yeni öncelik seviyesini belirtir. Bu değer -20 (en yüksek öncelik) ile 19 (en düşük öncelik) arasında olmalıdır.
- `-p`, `--pid`: Önceliği değiştirilecek sürecin PID'sini belirtir.
- `-g`, `--pgroup`: Bir süreç grubunun önceliğini değiştirmek için kullanılır.
- `-u`, `--user`: Belirli bir kullanıcıya ait süreçlerin önceliğini değiştirir.

## Common Examples
Aşağıda `renice` komutunun bazı pratik örnekleri verilmiştir:

1. Belirli bir sürecin önceliğini artırmak:
   ```bash
   renice -n -5 -p 1234
   ```
   Bu komut, PID'si 1234 olan sürecin önceliğini -5 olarak ayarlar.

2. Bir süreç grubunun önceliğini değiştirmek:
   ```bash
   renice -n 10 -g 5678
   ```
   Bu komut, PID'si 5678 olan süreç grubunun önceliğini 10 olarak ayarlar.

3. Belirli bir kullanıcıya ait tüm süreçlerin önceliğini düşürmek:
   ```bash
   renice -n 15 -u kullanıcı_adı
   ```
   Bu komut, "kullanıcı_adı"na ait tüm süreçlerin önceliğini 15 olarak ayarlar.

## Tips
- Öncelik seviyelerini değiştirirken dikkatli olun; yüksek öncelikler sistem kaynaklarını daha fazla tüketebilir.
- Süreçlerin önceliklerini değiştirmeden önce, hangi süreçlerin kritik olduğunu değerlendirin.
- `renice` komutunu kullanmadan önce, sürecin mevcut önceliğini kontrol etmek için `ps` veya `top` komutlarını kullanabilirsiniz.