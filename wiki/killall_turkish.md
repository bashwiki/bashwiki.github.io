# [Linux] Bash killall Kullanımı: Belirli bir işlemi durdurma

## Overview
`killall` komutu, belirli bir isimle çalışan tüm süreçleri durdurmak için kullanılır. Bu komut, bir uygulamanın veya sürecin tüm örneklerini hızlı bir şekilde sonlandırmak için oldukça yararlıdır.

## Usage
Temel sözdizimi şu şekildedir:
```bash
killall [seçenekler] [argümanlar]
```

## Common Options
- `-u`: Belirtilen kullanıcıya ait süreçleri durdurur.
- `-i`: Kullanıcıdan onay ister.
- `-q`: Hata mesajlarını gizler.
- `-s`: Gönderilecek sinyalin türünü belirtir (örneğin, `SIGTERM`, `SIGKILL`).

## Common Examples
Aşağıda `killall` komutunun bazı pratik örnekleri verilmiştir:

1. Tüm `firefox` süreçlerini durdurmak için:
   ```bash
   killall firefox
   ```

2. Belirli bir kullanıcıya ait tüm `python` süreçlerini durdurmak için:
   ```bash
   killall -u kullanıcı_adı python
   ```

3. Kullanıcıdan onay alarak tüm `gedit` süreçlerini durdurmak için:
   ```bash
   killall -i gedit
   ```

4. Hata mesajlarını gizleyerek tüm `vlc` süreçlerini durdurmak için:
   ```bash
   killall -q vlc
   ```

5. Tüm `java` süreçlerini `SIGKILL` sinyali ile durdurmak için:
   ```bash
   killall -s SIGKILL java
   ```

## Tips
- `killall` komutunu kullanmadan önce hangi süreçlerin çalıştığını görmek için `ps` veya `top` komutlarını kullanabilirsiniz.
- Yanlışlıkla önemli bir süreci durdurmamak için `-i` seçeneğini kullanarak onay almayı tercih edin.
- Süreç isimlerini tam olarak yazmaya dikkat edin; yanlış bir isim vermek, beklenmedik sonuçlara yol açabilir.