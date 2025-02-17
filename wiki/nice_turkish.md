# [Linux] Bash nice Kullanımı: Süreçlerin öncelik seviyesini ayarlama

## Overview
`nice` komutu, Unix benzeri işletim sistemlerinde süreçlerin öncelik seviyesini ayarlamak için kullanılır. Bu komut, bir sürecin CPU kaynaklarını ne kadar öncelikli bir şekilde kullanacağını belirler. Düşük bir öncelik değeri, sürecin daha az CPU kaynağı alacağı anlamına gelirken, yüksek bir değer daha fazla kaynak almasını sağlar.

## Usage
Temel sözdizimi şu şekildedir:

```bash
nice [options] [command]
```

## Common Options
- `-n, --adjustment`: Öncelik değerini ayarlamak için kullanılır. Varsayılan olarak 10'dur.
- `-h, --help`: Komut hakkında yardım bilgilerini görüntüler.
- `-v, --version`: `nice` komutunun sürüm bilgilerini gösterir.

## Common Examples
Aşağıda `nice` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Varsayılan öncelik ile bir komut çalıştırma:
   ```bash
   nice my_script.sh
   ```

2. Öncelik değerini 5 olarak ayarlayarak bir komut çalıştırma:
   ```bash
   nice -n 5 my_script.sh
   ```

3. Öncelik değerini -5 olarak ayarlayarak bir komut çalıştırma (bu, daha yüksek bir öncelik anlamına gelir):
   ```bash
   nice -n -5 my_script.sh
   ```

4. Bir komutun önceliğini kontrol etme:
   ```bash
   ps -o pid,ni,cmd
   ```

## Tips
- `nice` komutunu, sistem kaynaklarını daha verimli kullanmak için arka planda çalışan süreçler için kullanın.
- Öncelik değerini ayarlarken, sistemin genel performansını etkileyebileceğini unutmayın; bu nedenle dikkatli olun.
- `renice` komutunu kullanarak zaten çalışan bir sürecin önceliğini değiştirebilirsiniz.