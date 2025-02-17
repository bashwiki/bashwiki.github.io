# [Linux] Bash mkfifo Kullanımı: İletişim için özel dosyalar oluşturma

## Overview
`mkfifo` komutu, adlandırılmış bir boru (FIFO) dosyası oluşturmak için kullanılır. Bu dosyalar, birden fazla işlem arasında veri iletimi sağlamak için kullanılır ve verilerin sıralı bir şekilde akmasını sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
mkfifo [seçenekler] [argümanlar]
```

## Common Options
- `-m, --mode=MODE`: Oluşturulan FIFO dosyasının izinlerini belirler.
- `-Z, --context=CONTEXT`: Oluşturulan dosya için SELinux bağlamını ayarlar.

## Common Examples
Aşağıda `mkfifo` komutunun bazı pratik örnekleri bulunmaktadır:

1. Basit bir FIFO dosyası oluşturma:
   ```bash
   mkfifo myfifo
   ```

2. Belirli bir izinle FIFO dosyası oluşturma:
   ```bash
   mkfifo -m 644 myfifo
   ```

3. Bir FIFO dosyasını belirli bir SELinux bağlamıyla oluşturma:
   ```bash
   mkfifo -Z myfifo
   ```

## Tips
- FIFO dosyalarını kullanmadan önce, bu dosyaların hangi işlemler arasında veri iletimi sağlayacağını planlayın.
- FIFO dosyalarını kullanırken, bir işlem veriyi yazmadan önce diğerinin okuma yapmaya hazır olduğundan emin olun; aksi takdirde, yazma işlemi beklemede kalabilir.
- FIFO dosyalarını silmek için `rm` komutunu kullanabilirsiniz. Örneğin:
  ```bash
  rm myfifo
  ```