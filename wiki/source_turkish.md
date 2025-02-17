# [Linux] Bash source Kullanımı: Komut dosyalarını çalıştırma

## Overview
`source` komutu, bir Bash betiğini veya komut dosyasını mevcut shell ortamında çalıştırmak için kullanılır. Bu, betikteki değişkenlerin ve fonksiyonların mevcut shell oturumuna yüklenmesini sağlar.

## Usage
Temel sözdizimi şu şekildedir:

```bash
source [seçenekler] [argümanlar]
```

Alternatif olarak, `.` (nokta) ile de kullanılabilir:

```bash
. [seçenekler] [argümanlar]
```

## Common Options
- `-e`: Betik dosyasını çalıştırmadan önce hata kontrolü yapar.
- `-u`: Tanımsız değişkenler için hata verir.
- `-p`: Betik dosyasını çalıştırmadan önce, mevcut ortamda değişiklik yapmadan çalıştırır.

## Common Examples
1. Bir betik dosyasını çalıştırma:
   ```bash
   source myscript.sh
   ```

2. Nokta ile aynı işlemi yapma:
   ```bash
   . myscript.sh
   ```

3. Çevresel değişkenleri yükleme:
   ```bash
   source ~/.bash_profile
   ```

4. Hata kontrolü ile bir betik çalıştırma:
   ```bash
   source -e myscript.sh
   ```

## Tips
- `source` komutunu kullanarak, değişkenlerinizi ve fonksiyonlarınızı her seferinde yeniden tanımlamak zorunda kalmadan mevcut shell oturumunuza yükleyebilirsiniz.
- Betik dosyalarınızı çalıştırmadan önce, dosyanın doğru izinlere sahip olduğundan emin olun.
- Hataları önlemek için, betiklerinizi test ortamında çalıştırmayı düşünün.