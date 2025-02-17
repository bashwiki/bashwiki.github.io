# [Linux] Bash time Kullanımı: Komutların çalışma süresini ölçme

## Overview
`time` komutu, bir komutun veya programın ne kadar sürede çalıştığını ölçmek için kullanılır. Bu komut, çalıştırılan işlemin CPU süresi, gerçek zaman ve sistem zamanı gibi bilgileri sağlar.

## Usage
Temel sözdizimi şu şekildedir:
```bash
time [options] [arguments]
```

## Common Options
- `-p`: POSIX uyumlu çıktı formatı sağlar.
- `-o <file>`: Çıktıyı belirtilen dosyaya yönlendirir.
- `-v`: Daha ayrıntılı bir çıktı verir.

## Common Examples
Aşağıda `time` komutunun bazı pratik kullanımları bulunmaktadır:

1. Basit bir komutun çalışma süresini ölçme:
   ```bash
   time ls -l
   ```

2. Bir dosyayı kopyalama işleminin süresini ölçme:
   ```bash
   time cp largefile.txt /backup/
   ```

3. Çıktıyı bir dosyaya yönlendirme:
   ```bash
   time -o output.txt sleep 5
   ```

4. Daha ayrıntılı bilgi almak için:
   ```bash
   time -v find / -name "*.txt"
   ```

## Tips
- `time` komutunu, uzun süren işlemleri izlemek için kullanarak performans analizi yapabilirsiniz.
- Çıktıyı bir dosyaya yönlendirmek, sonuçları daha sonra incelemek için faydalı olabilir.
- `time` komutunu, birden fazla komutla birlikte kullanarak, her birinin süresini ayrı ayrı ölçebilirsiniz.