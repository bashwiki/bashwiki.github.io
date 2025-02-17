# [Linux] Bash popd Kullanımı: Dizin yığınından dizin çıkarmak

## Overview
`popd` komutu, dizin yığını (directory stack) üzerinde işlem yaparak en üstteki dizini kaldırır ve kullanıcıyı bir önceki dizine geri döndürür. Bu, kullanıcıların dizinler arasında daha verimli bir şekilde geçiş yapmalarını sağlar.

## Usage
Temel sözdizimi şu şekildedir:
```bash
popd [options] [arguments]
```

## Common Options
- `-n`: Dizin yığınını değiştirmeden sadece dizin listesini görüntüler.
- `+N`: N. dizini yığınından çıkarır. N, dizin yığınının sırasını belirtir.
- `-N`: N. dizini yığınından çıkarır ve ardından dizin yığınındaki bir önceki dizine geçer.

## Common Examples
Aşağıda `popd` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. **En üstteki dizini kaldır ve önceki dizine geç:**
   ```bash
   popd
   ```

2. **Dizin yığınındaki 2. dizini kaldır:**
   ```bash
   popd +1
   ```

3. **Dizin yığınındaki 3. dizini kaldır ve önceki dizine geç:**
   ```bash
   popd -2
   ```

4. **Dizin yığınını görüntülemeden kaldır:**
   ```bash
   popd -n
   ```

## Tips
- `pushd` komutunu kullanarak dizinleri yığına ekleyebilirsiniz. Bu, `popd` ile birlikte etkili bir dizin yönetimi sağlar.
- Dizin yığınının durumunu kontrol etmek için `dirs` komutunu kullanabilirsiniz.
- Dizin yığınındaki dizinlerin sırasını hatırlamak için yorumlar ekleyerek daha iyi bir organizasyon sağlayabilirsiniz.