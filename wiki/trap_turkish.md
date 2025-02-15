# [리눅스] Bash trap 사용법

## Overview
`trap` komutu, bir Bash betiği çalışırken belirli sinyalleri veya olayları yakalamak ve bu olaylar gerçekleştiğinde belirli komutları çalıştırmak için kullanılır. Bu, betiğinizi daha güvenilir hale getirmek ve beklenmedik durumlarla başa çıkmak için oldukça yararlıdır. Örneğin, bir betik çalışırken kullanıcı CTRL+C tuşuna bastığında, `trap` komutu ile bu durumu yakalayabilir ve uygun bir temizleme işlemi gerçekleştirebilirsiniz.

## Usage
`trap` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
trap 'komutlar' sinyal
```

- `komutlar`: Sinyal alındığında çalıştırılacak olan komutlar.
- `sinyal`: Yakalamak istediğiniz sinyalin adı veya numarası. Örneğin, `SIGINT` (CTRL+C) veya `EXIT`.

### Yaygın Sinyaller
- `SIGINT`: Kullanıcının CTRL+C tuşuna basması.
- `SIGTERM`: Bir programın sonlandırılması.
- `EXIT`: Betik sona erdiğinde çalıştırılacak komutlar.

## Examples

### Örnek 1: CTRL+C ile Çıkış Yapıldığında Temizleme
Aşağıdaki örnekte, kullanıcı CTRL+C tuşuna bastığında bir temizleme işlemi gerçekleştirilir.

```bash
#!/bin/bash

trap 'echo "Temizleme işlemi yapılıyor..."; exit' SIGINT

while true; do
    echo "Betiğiniz çalışıyor. CTRL+C ile durdurabilirsiniz."
    sleep 1
done
```

### Örnek 2: Betik Sona Erdiğinde Mesaj Gösterme
Bu örnekte, betik sona erdiğinde bir mesaj gösterilir.

```bash
#!/bin/bash

trap 'echo "Betiğiniz sona erdi."' EXIT

echo "Betiğiniz çalışıyor..."
sleep 5
```

## Tips
- `trap` komutunu kullanırken, her zaman hangi sinyalleri yakalamak istediğinizi net bir şekilde belirleyin.
- Temizleme işlemleri için `trap` kullanmak, betiğinizin düzgün bir şekilde sonlanmasını sağlar ve kaynak sızıntılarını önler.
- Birden fazla sinyali aynı anda yakalamak için, sinyalleri boşlukla ayırarak belirtebilirsiniz. Örneğin: `trap 'komutlar' SIGINT SIGTERM`.
- `trap` komutunu kullanarak hata durumlarını yönetmek için, hata yakalama mekanizmaları ile birleştirebilirsiniz.