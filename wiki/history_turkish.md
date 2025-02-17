# [Linux] Bash history Kullanımı: Komut geçmişini görüntüleme

## Overview
`history` komutu, Bash kabuğunda daha önce çalıştırılan komutların listesini görüntülemek için kullanılır. Bu komut, kullanıcıların geçmişteki komutları kolayca bulmasına ve tekrar çalıştırmasına olanak tanır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
history [options] [arguments]
```

## Common Options
- `-c`: Geçmişi temizler.
- `-d offset`: Belirtilen offset'teki komutu geçmişten siler.
- `n`: Son `n` komutu görüntüler.

## Common Examples
Aşağıda `history` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Tüm geçmişi görüntüleme:
   ```bash
   history
   ```

2. Son 10 komutu görüntüleme:
   ```bash
   history 10
   ```

3. Geçmişten belirli bir komutu silme (örneğin, 5. komutu silmek):
   ```bash
   history -d 5
   ```

4. Geçmişi temizleme:
   ```bash
   history -c
   ```

## Tips
- Geçmişteki komutları tekrar çalıştırmak için `!n` kullanabilirsiniz; burada `n`, çalıştırmak istediğiniz komutun numarasıdır.
- `Ctrl + R` tuş kombinasyonu ile geçmişte arama yapabilirsiniz, bu da belirli bir komutu hızlıca bulmanıza yardımcı olur.
- Geçmişi düzenli olarak temizlemek, gereksiz komutların birikmesini önler ve terminalinizin daha düzenli kalmasını sağlar.