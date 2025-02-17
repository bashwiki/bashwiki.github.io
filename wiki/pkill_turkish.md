# [Linux] Bash pkill Kullanımı: Süreçleri adlarına göre sonlandırma

## Overview
`pkill` komutu, belirli bir isimle eşleşen süreçleri sonlandırmak için kullanılır. Bu, kullanıcıların belirli bir uygulamayı veya işlemi hızlı bir şekilde kapatmalarını sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
pkill [seçenekler] [argümanlar]
```

## Common Options
- `-f`: Tam komut satırıyla eşleşen süreçleri bulur.
- `-n`: En son başlatılan süreci sonlandırır.
- `-o`: En eski başlatılan süreci sonlandırır.
- `-signal`: Belirli bir sinyal göndererek süreci sonlandırır (örneğin, `-9` ile zorla kapatma).

## Common Examples
Aşağıda `pkill` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Belirli bir uygulamayı ad ile sonlandırma:
   ```bash
   pkill firefox
   ```

2. Tüm `java` süreçlerini sonlandırma:
   ```bash
   pkill java
   ```

3. Tam komut satırıyla eşleşen süreçleri sonlandırma:
   ```bash
   pkill -f "python my_script.py"
   ```

4. En son başlatılan `node` sürecini sonlandırma:
   ```bash
   pkill -n node
   ```

5. Zorla bir süreci sonlandırma:
   ```bash
   pkill -9 chrome
   ```

## Tips
- `pkill` komutunu kullanmadan önce hangi süreçlerin çalıştığını görmek için `ps` veya `top` komutlarını kullanabilirsiniz.
- Süreçleri sonlandırmadan önce, hangi süreçlerin kapatılacağını doğrulamak için `pgrep` komutunu kullanarak süreçleri listeleyebilirsiniz.
- Dikkatli olun; yanlışlıkla önemli bir süreci sonlandırmak sistemde sorunlara yol açabilir.