# [Linux] Bash ss Kullanımı: Ağ bağlantılarını görüntüleme

## Overview
`ss` komutu, Linux sistemlerinde ağ bağlantılarını ve soketleri görüntülemek için kullanılan bir araçtır. Bu komut, aktif bağlantılar hakkında detaylı bilgi sağlar ve ağ durumu hakkında hızlı bir analiz yapmanıza yardımcı olur.

## Usage
Temel kullanım sözdizimi aşağıdaki gibidir:
```bash
ss [options] [arguments]
```

## Common Options
- `-t`: TCP bağlantılarını gösterir.
- `-u`: UDP bağlantılarını gösterir.
- `-l`: Dinleme durumundaki soketleri listeler.
- `-p`: Bağlantılarla ilişkili süreçleri gösterir.
- `-n`: Adres ve port numaralarını sayısal olarak gösterir.

## Common Examples
Aşağıda `ss` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Tüm aktif bağlantıları listelemek için:
   ```bash
   ss
   ```

2. TCP bağlantılarını görüntülemek için:
   ```bash
   ss -t
   ```

3. UDP bağlantılarını görüntülemek için:
   ```bash
   ss -u
   ```

4. Dinleme durumundaki soketleri listelemek için:
   ```bash
   ss -l
   ```

5. Bağlantılarla ilişkili süreçleri görmek için:
   ```bash
   ss -p
   ```

6. Sayısal adres ve port numaralarını görüntülemek için:
   ```bash
   ss -n
   ```

## Tips
- `ss` komutunu kullanarak ağ sorunlarını hızlı bir şekilde tespit edebilirsiniz.
- Belirli bir portu dinleyen süreçleri bulmak için `ss -ltn 'sport = :80'` gibi bir filtreleme yapabilirsiniz.
- `ss` komutunu `grep` ile birleştirerek belirli bağlantıları veya süreçleri aramak daha kolay olabilir. Örneğin:
  ```bash
  ss -t | grep ESTAB
  ```