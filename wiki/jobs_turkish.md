# [Linux] Bash jobs Kullanımı: Arka planda çalışan işlemleri listeleme

## Overview
`jobs` komutu, terminalde arka planda çalışan işlemleri listelemek için kullanılır. Bu komut, kullanıcıya hangi işlemlerin çalıştığını ve bunların durumlarını gösterir. Özellikle birden fazla işlemle çalışırken, hangi işlemlerin aktif olduğunu takip etmek için faydalıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
jobs [options] [arguments]
```

## Common Options
- `-l`: İşlemlerin PID (Process ID) numaralarını gösterir.
- `-n`: Sadece durum değiştiren işlemleri listeler.
- `-p`: Sadece işlemlerin PID'lerini gösterir.

## Common Examples
Aşağıda `jobs` komutunun bazı yaygın kullanım örnekleri verilmiştir:

1. Arka planda çalışan tüm işlemleri listelemek:
   ```bash
   jobs
   ```

2. PID numaralarını da içeren bir liste almak:
   ```bash
   jobs -l
   ```

3. Durum değiştiren işlemleri görüntülemek:
   ```bash
   jobs -n
   ```

4. Sadece işlemlerin PID'lerini listelemek:
   ```bash
   jobs -p
   ```

## Tips
- `jobs` komutunu kullanarak arka planda çalışan işlemleri takip etmek, terminaldeki iş akışınızı daha verimli hale getirir.
- Eğer bir işlemi durdurmak veya devam ettirmek istiyorsanız, `bg` ve `fg` komutları ile `jobs` komutunu birleştirerek işlemleri yönetebilirsiniz.
- İşlemlerinizin durumunu kontrol etmek için `jobs` komutunu düzenli olarak kullanmak, sistem kaynaklarınızı daha iyi yönetmenize yardımcı olur.