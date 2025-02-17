# [Linux] Bash free Kullanımı: Bellek durumu hakkında bilgi verir

## Overview
`free` komutu, sistemdeki bellek kullanımını gösterir. Bu komut, RAM ve swap alanının ne kadarının kullanıldığını ve ne kadarının boş olduğunu hızlı bir şekilde görüntülemenizi sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
free [options] [arguments]
```

## Common Options
- `-h`: Bellek miktarlarını insan tarafından okunabilir formatta gösterir (örneğin, KB, MB, GB).
- `-m`: Bellek miktarlarını megabayt cinsinden gösterir.
- `-g`: Bellek miktarlarını gigabayt cinsinden gösterir.
- `-s <saniye>`: Belirtilen saniye aralıklarıyla sürekli güncellemeler yapar.
- `-t`: Toplam bellek kullanımını gösterir.

## Common Examples
1. Bellek durumunu varsayılan formatta görüntülemek için:
   ```bash
   free
   ```

2. Bellek durumunu insan tarafından okunabilir formatta görüntülemek için:
   ```bash
   free -h
   ```

3. Bellek durumunu megabayt cinsinden görüntülemek için:
   ```bash
   free -m
   ```

4. Her 5 saniyede bir bellek durumunu güncellemek için:
   ```bash
   free -s 5
   ```

5. Toplam bellek kullanımını görüntülemek için:
   ```bash
   free -t
   ```

## Tips
- `free` komutunu, sisteminizin bellek kullanımını izlemek için bir zamanlayıcı ile kullanarak, bellek tüketiminin zaman içindeki değişimini gözlemleyebilirsiniz.
- `free -h` seçeneği, bellek miktarlarını daha anlaşılır bir şekilde gösterdiği için genellikle tercih edilir.
- Bellek kullanımını analiz etmek için `vmstat` veya `top` gibi diğer komutlarla birlikte kullanabilirsiniz.