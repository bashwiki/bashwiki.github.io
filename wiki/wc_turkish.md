# [Linux] Bash wc Kullanımı: Metin dosyalarının satır, kelime ve karakter sayısını hesaplar

## Overview
`wc` (word count), metin dosyalarının içeriğini analiz eden bir Bash komutudur. Bu komut, bir dosyadaki satır, kelime ve karakter sayısını hızlı bir şekilde hesaplamaya yarar. `wc`, genellikle metin dosyalarının boyutunu veya içeriğini değerlendirmek için kullanılır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
wc [options] [arguments]
```

## Common Options
- `-l`: Sadece satır sayısını gösterir.
- `-w`: Sadece kelime sayısını gösterir.
- `-c`: Sadece karakter sayısını gösterir.
- `-m`: Sadece karakter sayısını gösterir (UTF-8 karakterleri için).
- `-L`: En uzun satırın uzunluğunu gösterir.

## Common Examples
Aşağıda `wc` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Bir dosyanın satır, kelime ve karakter sayısını gösterme:
   ```bash
   wc dosya.txt
   ```

2. Sadece satır sayısını gösterme:
   ```bash
   wc -l dosya.txt
   ```

3. Sadece kelime sayısını gösterme:
   ```bash
   wc -w dosya.txt
   ```

4. Sadece karakter sayısını gösterme:
   ```bash
   wc -c dosya.txt
   ```

5. Birden fazla dosyanın satır, kelime ve karakter sayısını gösterme:
   ```bash
   wc dosya1.txt dosya2.txt
   ```

## Tips
- `wc` komutunu diğer komutlarla birleştirerek daha karmaşık analizler yapabilirsiniz. Örneğin, `grep` ile birlikte kullanarak belirli bir terimi içeren satırları sayabilirsiniz:
  ```bash
  grep "terim" dosya.txt | wc -l
  ```
- Dosyaların içeriğini incelemeden önce `wc` komutunu kullanarak genel bir bakış elde edebilirsiniz.
- `wc` komutunu sıkça kullandığınız dosyalar için bir alias tanımlayarak işlemlerinizi hızlandırabilirsiniz.